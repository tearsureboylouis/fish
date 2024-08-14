import sys
import cv2
import numpy as np
import pyautogui
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, \
    QMessageBox
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import Qt
import keyboard
import pygetwindow as gw

from pages.global_dict import global_dict


class ImageWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.Window | Qt.WindowSystemMenuHint | Qt.WindowCloseButtonHint)
        self.setWindowTitle('窗口选择')

        # 初始化
        self.points = []  # 存储点击的点

        # 创建垂直布局
        self.layout = QVBoxLayout(self)

        # 创建一个水平布局来放置按钮
        self.button_layout = QHBoxLayout()

        # 创建多个按钮
        self.reload_button = QPushButton("获取窗口", self)
        self.button_layout.addWidget(self.reload_button)
        self.reload_button.setStyleSheet("font-size:14px;height:30px")
        self.save_button = QPushButton("保存边框", self)
        self.button_layout.addWidget(self.save_button)
        self.save_button.setStyleSheet("font-size:14px;height:30px")
        self.reset_button = QPushButton("重新绘制", self)
        self.button_layout.addWidget(self.reset_button)
        self.reset_button.setStyleSheet("font-size:14px;height:30px")

        # 连接按钮事件
        self.reset_button.clicked.connect(self.reset)
        self.save_button.clicked.connect(self.save)
        self.reload_button.clicked.connect(self.reload)

        # 将按钮布局添加到垂直布局
        self.layout.addLayout(self.button_layout)

        # 创建并添加标签
        self.label = QLabel(self)
        self.layout.addWidget(self.label)

        # 使 label 能够响应鼠标点击事件
        self.label.mousePressEvent = self.get_pos

    def refresh_image(self):
        # 显示当前图像
        display_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        height, width, channel = display_image.shape
        bytes_per_line = 3 * width
        q_img = QImage(display_image.data, width, height, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(q_img)
        self.label.setPixmap(pixmap)

    def get_pos(self, event):
        x = int(event.position().x())
        y = int(event.position().y())
        self.points.append([x, y])

        # 重绘图像
        self.update_drawing()

    def update_drawing(self):
        self.image = self.original_image.copy()
        if len(self.points) == 1:
            # 只有一个点，绘制一个小圆圈表示点的位置
            cv2.circle(self.image, tuple(self.points[0]), 3, (0, 255, 0), thickness=-1)
        elif len(self.points) == 2:
            # 两个点，绘制一条线
            cv2.line(self.image, tuple(self.points[0]), tuple(self.points[1]), (0, 255, 0), 2)
        elif len(self.points) > 2:
            # 三个或更多点，绘制多边形
            pts = np.array(self.points, np.int32).reshape((-1, 1, 2))
            cv2.polylines(self.image, [pts], isClosed=True, color=(0, 255, 0), thickness=2)
            print(self.points)
        self.refresh_image()

    def reset(self):
        # 重置图片和清空点列表
        self.image = self.original_image.copy()
        self.points = []
        self.refresh_image()

    def save(self):
        if len(self.points) < 3:
            QMessageBox.critical(self, '错误', '请选择三个及以上的点！')
        else:
            height = self.image.shape[0]
            width = self.image.shape[1]
            scale = height / 600
            temp = []
            for point in self.points:
                # width height
                temp.append(((point[0] * scale) - (width / 2), -((point[1] * scale) - (height / 2))))
            global_dict['edge'] = temp

    def reload(self):
        # 获取窗口，截取窗口，加载图像 20240801
        _window = gw.getWindowsWithTitle('20240801')
        if not _window:
            QMessageBox.critical(self, '错误', '未找到指定窗口！')
        else:
            self.points = []
            _window = _window[0]
            screenshot = pyautogui.screenshot(
                region=(
                    _window.left + global_dict['window_offset'][0], _window.top + global_dict['window_offset'][1], 800,
                    600))
            self.original_image = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2RGB)
            self.image = self.original_image.copy()
            self.refresh_image()
