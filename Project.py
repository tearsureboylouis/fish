import shutil
import sys
import time
from datetime import datetime

import numpy as np
import pyautogui

from ultralytics import YOLO

import cv2
from PySide6.QtCore import Qt, QPoint, QSize, QThread, Signal, Slot, QTimer
from PySide6.QtGui import QFont, QCursor, QImage, QPixmap, QColor
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox, QPushButton, QSizePolicy, QVBoxLayout, \
    QSpacerItem, QTableWidgetItem, QHBoxLayout, QTableWidget, QHeaderView, QLabel

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas, FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib import rcParams
import pygetwindow as gw

import UI.style
from UI.Open import OpenWindow
from UI.processing import ProcessingWindowUI
from UI.main import MainWindow
from Utils.saveInfo import save_project_info
from Utils.output_yolo_result import *
from Utils.clustering import split_files, cluster_layers
from Utils.visualization import *

rcParams['font.family'] = 'Microsoft YaHei'  # 设置字体为微软雅黑
rcParams['axes.unicode_minus'] = False  # 正确显示负号

global_dict = {
    'path': './_internal/static/ex.xml',
    'project_video': '',
    'project_name': '',
    'project_path': '',
    'FPS': '',
    'total_frame': '',
    'water_layer': 0,
    'xml_url': '',
    'water_depth': 0.0,
    'duration': 0.0,
    'recording_window': ''
}


class OpenProjectWindow(QWidget, OpenWindow):

    def __init__(self, other):
        super().__init__()
        self.setupUi(self)

        self.other_window = other
        self.processing = ProcessingWindow()
        self.recordingWindow = RecordingWindow()

        self.set_style()
        self.bind()
        self.recent_file()
        self.init_combox()

    def mousePressEvent(self, event):
        self.oldPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPosition().toPoint() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPosition().toPoint()

    def recent_file(self):
        font1 = QFont()
        font1.setPointSize(10)

        root = ET.parse(r'_internal/static/ex.xml').getroot()
        recent_file_name = root.findall('.//fileName')
        index = len(recent_file_name)

        for i in range(index):
            file_name = recent_file_name[index - i - 1].text
            button = QPushButton(file_name, self)
            button.setMinimumSize(QSize(0, 40))
            button.setFont(font1)
            button.setProperty('class', 'recent_file')
            button.setCursor(QCursor(Qt.PointingHandCursor))
            self.gridLayout_recently.addWidget(button, i // 2, i % 2, 1, 1)

            button.clicked.connect(lambda _, file_name=file_name: self.open_recent_file(file_name))

    def open_recent_file(self, target_fileName):
        try:
            path = global_dict['path']
            tree = ET.parse(path)
            root = tree.getroot()
            fileName = ''
            filePath = ''
            mp4File = ''
            for recentFile in root.findall('.//recentFile'):
                fileName = recentFile.find('.//fileName').text
                if fileName == target_fileName:
                    filePath = recentFile.find('filePath').text
                    mp4File = recentFile.find('mp4File').text
                    break

            file_node = root.find('.//file')
            if True:
                for item in root.findall('.//recentFile'):
                    _fileName = item.find('.//fileName')
                    if _fileName.text == target_fileName:
                        file_node.remove(item)

                        new_recent_file = ET.Element('recentFile')
                        new_file_name = ET.SubElement(new_recent_file, 'fileName')
                        new_file_name.text = fileName
                        global_dict['project_name'] = fileName
                        new_file_path = ET.SubElement(new_recent_file, 'filePath')
                        new_file_path.text = filePath
                        global_dict['project_path'] = filePath
                        new_xml_file = ET.SubElement(new_recent_file, 'mp4File')
                        new_xml_file.text = mp4File
                        global_dict['project_video'] = filePath
                        # 将新的recentFile添加到file节点
                        file_node.append(new_recent_file)

                        tree.write(path, encoding='utf-8', xml_declaration=True)
                        break

                global_dict['xml_url'] = os.path.join(global_dict['project_path'], global_dict['project_name'],
                                                      'data/output.xml')
                self.other_window.initial_data()
                self.other_window.show()
                self.close()
        except Exception as e:
            path = global_dict['path']
            tree = ET.parse(path)
            root = tree.getroot()
            file_node = root.find('.//file')
            for item in root.findall('.//recentFile'):
                _fileName = item.find('.//fileName')
                if _fileName.text == target_fileName:
                    file_node.remove(item)
                    tree.write(path, encoding='utf-8', xml_declaration=True)
            QMessageBox.critical(self, 'error', f'{e}')
        finally:
            self.update()

    def set_style(self):
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.main_window.setProperty('class', 'window')
        self.frame_header.setProperty("class", 'menu header')
        self.frame_footer.setProperty("class", 'menu footer')
        self.newProject.setProperty("class", 'menu body')
        self.openProject.setProperty("class", 'menu body')
        self.pushButton_exit.setProperty("class", 'exit')

        self.pushButton_new_project.setProperty("class", "side_label side_label_unclick")
        self.pushButton_open_project.setProperty("class", "side_label side_label_click")
        self.pushButton_recording.setProperty("class", "side_label side_label_unclick")

        self.stackedWidget_body.setProperty("class", 'menu body')

        self.lineEdit_name.setProperty("class", 'input_text')
        self.lineEdit_path.setProperty("class", 'input_text')
        self.lineEdit_video.setProperty("class", 'input_text')
        self.lineEdit_water_depth.setProperty("class", 'input_text')
        self.lineEdit_time.setProperty("class", 'input_text')

        self.lineEdit_xml_file.setProperty("class", 'input_text')

        self.lineEdit_project_name_r.setProperty("class", 'input_text')
        self.lineEdit_save_path_r.setProperty("class", 'input_text')
        self.lineEdit_water_deep_r.setProperty("class", 'input_text')
        # self.comboBox_body_r.setProperty("class", 'input_text')

    def bind(self):
        self.pushButton_new_project.clicked.connect(self.new_project)
        self.pushButton_open_project.clicked.connect(self.open_project)
        self.pushButton_open_folder.clicked.connect(self.open_folder)
        self.pushButton_open_file.clicked.connect(self.open_file)
        self.pushButton_finish.clicked.connect(self.finish)
        self.pushButton_exit.clicked.connect(self.exit)
        self.pushButton_choose_xml.clicked.connect(self.choose_xml)
        self.pushButton.clicked.connect(self.open_xml)
        self.pushButton_recording.clicked.connect(self.recording)

        self.pushButton_save_path_r.clicked.connect(self.save_path_r)
        self.comboBox_body_r.currentTextChanged.connect(self.choose_window)
        # self.comboBox_body_r.activated.connect(self.init_combox)
        self.pushButton_start_recording.clicked.connect(self.start_recording)

    def new_project(self):
        self.pushButton_new_project.setProperty("class", "side_label side_label_click")
        self.pushButton_open_project.setProperty("class", "side_label side_label_unclick")
        self.pushButton_recording.setProperty("class", "side_label side_label_unclick")
        self.update_style()  # 更新样式
        self.stackedWidget_body.setCurrentIndex(0)

    def open_project(self):
        self.pushButton_new_project.setProperty("class", "side_label side_label_unclick")
        self.pushButton_open_project.setProperty("class", "side_label side_label_click")
        self.pushButton_recording.setProperty("class", "side_label side_label_unclick")
        self.update_style()  # 更新样式
        self.stackedWidget_body.setCurrentIndex(2)

    def recording(self):
        self.pushButton_new_project.setProperty("class", "side_label side_label_unclick")
        self.pushButton_open_project.setProperty("class", "side_label side_label_unclick")
        self.pushButton_recording.setProperty("class", "side_label side_label_click")
        self.update_style()  # 更新样式
        self.stackedWidget_body.setCurrentIndex(1)

    def update_style(self):
        # 触发样式的重新应用
        self.pushButton_new_project.style().unpolish(self.pushButton_new_project)
        self.pushButton_new_project.style().polish(self.pushButton_new_project)
        self.pushButton_open_project.style().unpolish(self.pushButton_open_project)
        self.pushButton_open_project.style().polish(self.pushButton_open_project)
        self.pushButton_recording.style().unpolish(self.pushButton_recording)
        self.pushButton_recording.style().polish(self.pushButton_recording)

    def open_folder(self):
        path = QFileDialog.getExistingDirectory(self, 'Open Folder', '.')
        if path == "":
            return
        global_dict['project_path'] = path
        self.lineEdit_path.setText(path)

    def open_file(self):
        video = QFileDialog.getOpenFileName(self, 'Open File', '.', '视频文件(*.mp4))')[0]
        if video == "":
            return
        global_dict['project_video'] = video
        self.lineEdit_video.setText(video)

    def finish(self):
        global_dict['project_name'] = self.lineEdit_name.text()

        if global_dict['project_name'] == "":
            QMessageBox.critical(self, "Error", "请输入项目名称!")
            return
        elif global_dict['project_path'] == "":
            QMessageBox.critical(self, "Error", "请选择项目保存的文件夹!")
            return
        elif global_dict['project_video'] == "":
            QMessageBox.critical(self, "Error", "请选择要识别的视频!")
            return

        # 创建文件夹
        path = os.path.join(global_dict['project_path'], global_dict['project_name'])
        os.makedirs(path, exist_ok=True)
        folder_name = ['video', 'data/metadata', 'data/results']
        for i in folder_name:
            os.makedirs(os.path.join(path, i), exist_ok=True)

        # 复制视频文件
        new_file_name = os.path.join(global_dict['project_path'], global_dict['project_name'], 'video',
                                     datetime.now().strftime('%Y%m%d') + '_' + global_dict[
                                         'project_name'] + '_row.mp4')
        shutil.copy(global_dict['project_video'], new_file_name)
        global_dict['project_video'] = new_file_name
        global_dict['water_depth'] = float(self.lineEdit_water_depth.text())
        global_dict['duration'] = float(self.lineEdit_time.text())

        save_project_info(global_dict['project_name'], global_dict['project_path'],
                          global_dict['project_video'])

        self.processing.show()
        self.setEnabled(False)

    def exit(self):
        self.close()

    def choose_xml(self):
        config = QFileDialog.getOpenFileName(self, 'Open Config file', '.', '配置文件(*.xml))')[0]
        if config == "":
            return
        self.config = config
        self.lineEdit_xml_file.setText(config)

    def open_xml(self):
        video_path = os.path.join(self.config.split(r"/data")[0], 'video')
        if not os.path.isdir(video_path):
            return
        global_dict['xml_url'] = str(self.config)
        global_dict['is_open'] = True
        self.other_window.initial_data()
        self.close()
        self.other_window.show()

    def init_combox(self):
        windows = gw.getAllTitles()
        self.open_windows = [window for window in windows if window]
        # if not self.comboBox_body_r.currentData():
        #     self.comboBox_body_r.clear()
        for i in self.open_windows:
            if len(i) > 40:
                self.comboBox_body_r.addItem(i[:30] + "...")
            else:
                self.comboBox_body_r.addItem(i)

    def choose_window(self):
        global_dict['recording_window'] = self.open_windows[self.comboBox_body_r.currentIndex()]

    def save_path_r(self):
        path = QFileDialog.getExistingDirectory(self, 'Open Folder', '.')
        if path == "":
            return
        global_dict['project_path'] = path
        self.lineEdit_save_path_r.setText(path)

    def start_recording(self):
        global_dict['project_name'] = self.lineEdit_project_name_r.text()
        global_dict['project_path'] = self.lineEdit_save_path_r.text()
        global_dict['water_depth'] = self.lineEdit_water_deep_r.text()
        if global_dict['project_name'] == "" or global_dict['project_path'] == "" or global_dict[
            'recording_window'] == "" or global_dict['water_depth'] == 0:
            QMessageBox.critical(self, "Error", "请输入项目信息！")
            return

        path = os.path.join(global_dict['project_path'], global_dict['project_name'])
        os.makedirs(path, exist_ok=True)
        folder_name = ['video', 'data/metadata', 'data/results']
        for i in folder_name:
            os.makedirs(os.path.join(path, i), exist_ok=True)

        global_dict['project_video'] = new_file_name = os.path.join(global_dict['project_path'],
                                                                    global_dict['project_name'], 'video',
                                                                    datetime.now().strftime('%Y%m%d') + '_' +
                                                                    global_dict[
                                                                        'project_name'] + '_row.mp4')
        save_project_info(global_dict['project_name'], global_dict['project_path'], new_file_name)

        self.recordingWindow.show()
        self.setEnabled(False)


class VideoProcessingThread(QThread):
    update_progress = Signal(int)

    def __init__(self, video_path, model_path, parent=None):
        super().__init__(parent)
        # 初始化变量
        self.video_path = video_path
        self.model_path = model_path
        self.is_running = True

    def run(self):
        '''
        第一步：创建工程文件夹和工程文件
        第二步：识别并生成标签和视频
        第三步：计算与分析，并删除模型中的预测文件
        第四步：
        '''
        # 获取视频的参数
        cap = cv2.VideoCapture(self.video_path)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        global_dict['fps'] = fps = cap.get(cv2.CAP_PROP_FPS)
        global_dict['total_frames'] = total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        current_frame = 0
        # 设置YOLO模型
        model = YOLO(self.model_path)

        video_path = os.path.join(global_dict['project_path'], global_dict['project_name'], 'video',
                                  datetime.now().strftime('%Y%m%d') + '_' + global_dict[
                                      'project_name'] + '_predict.mp4').replace('\\', "/")
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(video_path, fourcc, fps, (width, height))

        # 读帧并识别
        while self.is_running and current_frame < total_frames:
            ret, frame = cap.read()
            if not ret:
                break
            # 模型预测
            results = model.predict(source=frame, save=True, save_txt=True)
            # 写入帧到视频文件
            save_path = os.path.join(global_dict['project_path'], global_dict['project_name'], 'data/metadata',
                                     f"{current_frame}.txt")
            results[0].save_txt(save_path)
            out.write(results[0].plot())
            current_frame += 1
            progress = int((current_frame / total_frames) * 99)
            self.update_progress.emit(progress)  # 更新进度条
            window.processing.label_process.setText(f'正在处理第 {current_frame} 帧，共 {total_frames} 帧')
        out.release()
        cap.release()

        window.processing.label_process.setText('正在处理识别结果')
        base_path = os.path.join(global_dict['project_path'], global_dict['project_name'], 'data')
        out_put_result(base_path, int(total_frames), int(fps), global_dict['duration'], global_dict['water_depth'])

        split_files(base_path)
        cluster_layers(base_path, global_dict['duration'], global_dict['water_depth'])

        self.update_progress.emit(100)
        window.processing.pushButton_finish.setText('完成')
        window.processing.pushButton_finish.setEnabled(True)
        window.processing.pushButton_cencel.setEnabled(False)
        window.processing.label_process.setText('已完成')


class ProcessingWindow(QWidget, ProcessingWindowUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.thread = None
        self.bind()

    def bind(self):
        self.pushButton_finish.clicked.connect(self.finish)
        self.pushButton_cencel.clicked.connect(self.cancel)

    def finish(self):
        if self.pushButton_finish.text() == '开始':
            self.pushButton_finish.setText('运行中')
            self.pushButton_finish.setEnabled(False)
            self.pushButton_cencel.setEnabled(True)
            self.label_process.setText('正在处理中…')
            self.startProcessing()
        else:  # 完成
            shutil.rmtree('runs')
            global_dict['xml_url'] = os.path.join(global_dict['project_path'], global_dict['project_name'],
                                                  'data/output.xml')
            window.other_window.initial_data()
            window.other_window.show()
            window.close()
            self.close()

    def cancel(self):
        self.thread.quit()
        # 删除文件夹
        # 删除xml
        self.close()
        window.setEnabled(True)

    def startProcessing(self):
        video_path = global_dict['project_video']
        model_path = r"./_internal/static/best.pt"
        self.thread = VideoProcessingThread(video_path, model_path)
        self.thread.update_progress.connect(self.progressBar.setValue)
        self.thread.start()


class RecordingThread(QThread):
    def __init__(self, parent=None):
        super().__init__(parent)
        # 初始化变量
        self.row_array = []
        self.predict_array = []
        self.isFirst = True
        self.start_time = 0.0

    def run(self):
        current_frame = 0
        window.recordingWindow.label.setText('正在初始化中')
        window.recordingWindow.button_function.setEnabled(False)
        window.recordingWindow.close_button.setEnabled(False)
        _window = gw.getWindowsWithTitle(global_dict['recording_window'])[0]
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        x, y, width, height = _window.left + 10, _window.top + 50, _window.width - 20, _window.height - 60
        model = YOLO('_internal/static/best.pt')

        if _window.isMinimized:  # 如果窗口最小化了，则先恢复
            _window.restore()
        _window.activate()  # 激活窗口，使其获得焦点

        while not window.recordingWindow.isFinish:
            # 窗口的坐标和尺寸

            # 使用pyautogui捕获指定区域的屏幕
            screenshot = pyautogui.screenshot(region=(x, y, width, height))
            frame = np.array(screenshot)
            self.row_array.append(frame)

            frame_p = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

            # 进行模型的预测
            results = model.predict(source=frame_p, save=True, save_txt=True)
            self.predict_array.append(results[0].plot())
            save_path = os.path.join(global_dict['project_path'], global_dict['project_name'], 'data/metadata',
                                     f"{current_frame}.txt")
            results[0].save_txt(save_path)
            current_frame += 1
            if self.isFirst:
                window.recordingWindow.label.setText('请确保录制窗口无遮挡，3秒后开始录制')
                time.sleep(1)
                window.recordingWindow.label.setText('请确保录制窗口无遮挡，2秒后开始录制')
                time.sleep(1)
                window.recordingWindow.label.setText('请确保录制窗口无遮挡，1秒后开始录制')
                time.sleep(1)
                window.recordingWindow.label.setText('录制中，请勿移动窗口！')
                _window.activate()
                self.isFirst = False
                self.start_time = time.time()
                window.recordingWindow.button_function.setText("结束录制")
                window.recordingWindow.button_function.setEnabled(True)

        window.recordingWindow.label.setText('正在处理数据中，请稍后…')
        window.recordingWindow.button_function.setEnabled(False)

        global_dict['duration'] = int(self.start_time - time.time())
        fps = float(len(self.row_array)) / (time.time() - self.start_time)
        self.row_video = cv2.VideoWriter(global_dict['project_video'], fourcc, fps,
                                         (_window.width - 20, _window.height - 60))
        self.predict_video = cv2.VideoWriter(global_dict['project_video'][:-7] + 'predict.mp4', fourcc, fps,
                                             (_window.width - 20, _window.height - 60))
        for frame in self.row_array:
            frame_1 = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            self.row_video.write(frame_1)
        for frame in self.predict_array:
            self.predict_video.write(frame)
        self.row_video.release()
        self.predict_video.release()

        base_path = os.path.join(global_dict['project_path'], global_dict['project_name'], 'data')
        out_put_result(base_path, int(len(self.row_array)), int(fps), global_dict['duration'],
                       global_dict['water_depth'])
        split_files(base_path)
        cluster_layers(base_path, global_dict['duration'], global_dict['water_depth'])

        window.recordingWindow.label.setText('数据处理完成，请点击完成按钮')
        window.recordingWindow.button_function.setText("完成")
        window.recordingWindow.button_function.setEnabled(True)


class RecordingWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.thread = None

        self.setupUI()
        self.bind()
        self.init()

        self.isFinish = False

    def setupUI(self):
        self.setWindowFlag(Qt.FramelessWindowHint)

        # 设置窗口的标题和大小
        self.resize(300, 100)

        # 创建一个垂直布局
        v_layout = QVBoxLayout()

        font1 = QFont()
        font1.setPointSize(10)

        # 创建顶部的水平布局
        top_layout = QHBoxLayout()

        self.label = QLabel("请点击开始录制")
        self.label.setAlignment(Qt.AlignLeft)
        self.label.setFont(font1)

        self.close_button = QPushButton("x")
        self.close_button.setFixedSize(20, 20)
        self.close_button.clicked.connect(lambda: self.window().close())  # 连接按钮的点击信号到窗口的close()方法

        # 将关闭按钮放在水平布局的右侧
        top_layout.addSpacing(20)
        top_layout.addWidget(self.label)
        top_layout.addStretch()  # 添加弹性空间，将关闭按钮推到右侧
        top_layout.addWidget(self.close_button)

        # 创建两个按钮
        self.button_function = QPushButton("开始录制")
        self.button_function.setFixedSize(80, 30)

        # 创建一个水平布局来放置按钮
        h_layout = QHBoxLayout()
        h_layout.addWidget(self.button_function)

        # 将标签和按钮布局添加到垂直布局中
        v_layout.addLayout(top_layout)
        v_layout.addWidget(self.label)
        v_layout.addLayout(h_layout)

        # 设置窗体的主布局
        self.setLayout(v_layout)

    def bind(self):
        self.button_function.clicked.connect(self.functions)

    def init(self):
        pass

    def run_recording(self):
        self.thread = RecordingThread()
        self.thread.start()

    def functions(self):
        if self.button_function.text() == "开始录制":
            self.run_recording()
        elif self.button_function.text() == "结束录制":
            self.isFinish = True
        elif self.button_function.text() == "完成":
            shutil.rmtree('runs')
            global_dict['xml_url'] = os.path.join(global_dict['project_path'], global_dict['project_name'],
                                                  'data/output.xml')
            window.other_window.initial_data()
            window.other_window.show()
            window.close()
            self.close()


class MainWindows(QWidget, MainWindow):
    indexChanged = Signal(int)

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.LayerWindow = LayerWindow(self)
        self.TotalWindow = TotalLayer()

    def initial_data(self):
        if global_dict['xml_url'] == '':
            return

        self.bind()

        self.buttons = []
        self.video_path = os.path.join(global_dict['xml_url'].split(r"data")[0], 'video')
        files = os.listdir(self.video_path)
        for f in files:
            if 'predict' in f:
                self.video_path = os.path.join(self.video_path, f)

        self.video_capture = cv2.VideoCapture(self.video_path)
        self.PFS = int(self.video_capture.get(cv2.CAP_PROP_FPS))

        self.is_paused = False
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(int(1000 / self.PFS - 33))  # 程序运行需要30ms左右

        base_url = global_dict['xml_url'].split('output.xml')[0]
        layer_count, total_count = get_layers_data(base_url)

        for i in range(len(layer_count)):
            self.pushButton = QPushButton(f"pushButton_{i + 1}")
            self.pushButton.setMinimumSize(QSize(0, 45))
            self.verticalLayout_layer_list.addWidget(self.pushButton)
            self.pushButton.setText(f"水层{i + 1}\n当前 {layer_count[i]} 条鱼")
            self.pushButton.setProperty("class", "layer_button")
            self.pushButton.clicked.connect(self.button_clicked)
            self.buttons.append(self.pushButton)

        self.verticalSpacer = QSpacerItem(20, 1000, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.verticalLayout_layer_list.addItem(self.verticalSpacer)

        self.pushButton_total = QPushButton(self.frame)
        self.pushButton_total.setObjectName(u"pushButton_total")
        self.pushButton_total.setMinimumSize(QSize(0, 40))
        self.pushButton_total.setText(f"预计共 {total_count} 条鱼")
        self.pushButton_total.setProperty("class", "layer_button")
        self.pushButton_total.clicked.connect(self.init_data)

        self.verticalLayout_layer_list.addWidget(self.pushButton_total)

    @Slot()
    def button_clicked(self):
        button = self.sender()
        index = self.buttons.index(button) + 1
        self.indexChanged.emit(int(index))

        self.is_paused = False
        self.video_capture = cv2.VideoCapture(self.video_path)

        main_window_position = self.frameGeometry().topLeft()

        # 设置子窗口的位置为主窗口左侧
        self.LayerWindow.move(main_window_position.x() - self.LayerWindow.width() - 10,
                              main_window_position.y() + (self.height() - self.LayerWindow.height()) / 2)

    def bind(self):
        self.pushButton_play.clicked.connect(self._play)
        self.pushButton_purse.clicked.connect(self._pause)
        self.pushButton_reset.clicked.connect(self.reset)

    def update_frame(self):
        if not self.is_paused:
            ret, frame = self.video_capture.read()
            if ret:
                # 将 OpenCV BGR 帧转换为 RGB 帧
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # 将 OpenCV 帧转换为 QImage
                h, w, ch = frame.shape
                bytes_per_line = ch * w
                qt_image = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
                self.video_label.setPixmap(QPixmap.fromImage(qt_image))

            else:
                self.video_capture.release()  # 释放捕捉

    def _play(self):
        self.is_paused = not self.is_paused
        self.pushButton_play.setEnabled(False)
        self.pushButton_purse.setEnabled(True)

    def _pause(self):
        self.is_paused = not self.is_paused
        self.pushButton_play.setEnabled(True)
        self.pushButton_purse.setEnabled(False)

    def reset(self):
        self.is_paused = False
        self.video_capture = cv2.VideoCapture(self.video_path)

    def init_data(self):
        self.TotalWindow.plot_point()
        self.TotalWindow.show()


class LayerWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent, Qt.Window)
        self.fig = Figure(figsize=(5, 5), dpi=100)
        self.canvas = FigureCanvas(self.fig)

        self.axes = self.fig.add_subplot(111)

        layout = QVBoxLayout()
        self.setLayout(layout)

        # 添加画布到布局中
        layout.addWidget(self.canvas)

        if parent:
            parent.indexChanged.connect(self.update_plot)

        self.cid = self.fig.canvas.mpl_connect('button_press_event', self.onclick)

    def update_plot(self, index):
        self.axes.clear()
        base_url = global_dict['xml_url'].split('output.xml')[0]
        self.num, self.x, self.y = get_xy_point(base_url, index)
        self.axes.scatter(self.x, self.y)
        split = os.path.join(base_url, 'results/split_layer')
        split_file = sorted(os.listdir(split), key=lambda x: int(x.split('_')[0]))

        if self.num == []:
            maxxy = 100
            self.axes.set_title(
                f"当前水层预计 0 条鱼\n水层深度 {split_file[index - 1].split('.')[0].replace('_', '-')} cm",
                fontsize=12)
        else:
            maxxy = max(max(abs(min(self.x)), max(self.x)), max(abs(min(self.y)), max(self.y)))
            self.axes.set_title(
                f"当前水层预计 {self.num[-1]} 条鱼\n水层深度 {split_file[index - 1].split('.')[0].replace('_', '-')} cm",
                fontsize=12)
        self.axes.set_xlim(-maxxy - 50, maxxy + 50)
        self.axes.set_ylim(-maxxy - 50, maxxy + 50)

        self.axes.axhline(y=0, color='b', linestyle='--')
        self.axes.axvline(x=0, color='b', linestyle='--')

        self.canvas.draw()  # 重绘画布

        self.show()  # 确保窗口显示

    def onclick(self, event):
        if event.xdata is not None and event.ydata is not None:
            # 计算点击位置与所有点的距离
            distances = np.hypot(self.x - event.xdata, self.y - event.ydata)
            min_distance = distances.min()
            if min_distance < 10:  # 设置一个阈值
                # 找到最近的点
                min_index = distances.argmin()
                # 将此点标红
                colors = ['#1f77b4'] * len(self.x)  # 重设所有点为蓝色
                colors[min_index] = '#d62728'
                self.axes.scatter(self.x, self.y, color=colors)  # 重新绘制散点图
                self.text = self.fig.text(0, 0, f'({round(self.x[min_index], 3)}, {round(self.y[min_index], 3)})',
                                          ha="left",
                                          fontsize=10)
                self.canvas.draw()


class TotalLayer(QWidget):
    def __init__(self):
        super().__init__()
        self.column_names = ["Layer", "index", "X", "Y", "Z"]

        # Figure (Left)
        self.fig = Figure(figsize=(8, 8), dpi=100)
        self.canvas = FigureCanvasQTAgg(self.fig)

        # Table (Right)
        self.table = QTableWidget()
        self.table.verticalHeader().setVisible(False)
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

        # Right layout
        rlayout = QVBoxLayout()
        rlayout.setContentsMargins(1, 1, 1, 1)
        rlayout.addWidget(self.table)

        # Left layout
        llayout = QVBoxLayout()
        llayout.setContentsMargins(1, 1, 1, 1)
        llayout.addWidget(self.canvas)

        # Main layout
        layout = QHBoxLayout(self)
        layout.addLayout(llayout, 70)
        layout.addLayout(rlayout, 30)

    def set_table_data(self, layer, index, X, Y, Z):
        row = 0
        current_color = QColor(240, 240, 240)  # 初始颜色
        last_layer = None

        for i in range(len(X)):
            if layer[i] != last_layer:
                current_color = QColor(
                    np.random.randint(100, 150),
                    np.random.randint(100, 150),
                    np.random.randint(100, 150)
                )
                self.layer_color = []
                print(current_color.getRgb())
                self.layer_color.append(current_color.getRgb())
                last_layer = layer[i]

            for j in range(5):
                item = QTableWidgetItem([f"{layer[i]}", f"{index[i]}", f"{X[i]:.2f}", f"{Y[i]:.2f}", f"{Z[i]:.2f}"][j])
                item.setBackground(current_color)
                item.setTextAlignment(Qt.AlignCenter)
                self.table.setItem(row, j, item)

            row += 1

            if i < len(X) - 1 and layer[i] != layer[i + 1]:
                self.table.insertRow(row)  # Insert empty row
                row += 1

    def set_canvas(self):
        self.fig.set_canvas(self.canvas)
        self.axes = self.canvas.figure.add_subplot(projection="3d")

        self.axes.set_xlabel(self.column_names[2])
        self.axes.set_ylabel(self.column_names[3])
        self.axes.set_zlabel(self.column_names[4])

    def set_table(self, row_count, data):
        self.table.setRowCount(row_count)
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(self.column_names)
        self.set_table_data(data[0], data[1], data[2], data[3], data[4])

    # Plot methods

    def plot_point(self):
        # Data
        base_url = global_dict['xml_url'].split('output.xml')[0]
        data = get_layer_data(base_url)
        self.data_dict = {}
        self.layer = list()
        self.index = list()
        self.X = list()
        self.Y = list()
        self.Z = list()
        for i in range(len(data)):
            self.data_dict[f'layer{i + 1}'] = {
                "index": data[i][0],
                "x": data[i][1],
                "y": data[i][2],
                "z": data[i][3]
            }
        self.set_canvas()
        k = 1
        for i in self.data_dict.items():
            self.axes.scatter(i[1]['x'], i[1]['y'], i[1]['z'], s=100, alpha=0.8)

            for j in range(len(i[1]['index'])):
                self.layer.append(f"layer_{k}")
            k += 1
            self.index += i[1]['index']
            self.X += i[1]['x']
            self.Y += i[1]['y']
            self.Z += i[1]['z']

        self.set_table(len(self.X), (self.layer, self.index, self.X, self.Y, self.Z))

        self.canvas.draw()

        self.axes.view_init(30, 45)
        self.fig.subplots_adjust(left=0.05, right=0.95, top=1, bottom=0)
        self.canvas.mpl_connect("scroll_event", self.on_mouse_wheel)

    def on_mouse_wheel(self, event):
        if self.axes is not None:
            x_min, x_max = self.axes.get_xlim()
            x_delta = (x_max - x_min) / 10  # 控制缩放X轴的比例
            y_min, y_max = self.axes.get_ylim()
            y_delta = (y_max - y_min) / 10  # 控制缩放Y轴的比例
            if event.button == "up":
                self.axes.set(xlim=(x_min + x_delta, x_max - x_delta))
                self.axes.set(ylim=(y_min + y_delta, y_max - y_delta))
            elif event.button == "down":
                self.axes.set(xlim=(x_min - x_delta, x_max + x_delta))
                self.axes.set(ylim=(y_min - y_delta, y_max + y_delta))

            self.canvas.draw_idle()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(UI.style.style)

    Mwindow = MainWindows()
    window = OpenProjectWindow(Mwindow)

    window.show()
    sys.exit(app.exec())
