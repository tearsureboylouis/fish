import os
import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN

import torch
import xml.etree.ElementTree as ET

all_data = []


def split_files(base_path):
    """
    每次将从小数点前数字为 m 的行到 n 的行的所有数据提取并保存到一个新的 Excel 文件中，并保存到m_10cm_n文件夹中
    """
    # 创建主文件夹
    main_folder_path = os.path.join(base_path, r'results\split_layer')
    os.makedirs(main_folder_path, exist_ok=True)

    # 创建xlsx文件
    file_path = os.path.join(base_path, r'results\deep_frame_coordinates.xlsx')
    deep_file = pd.read_excel(file_path)

    # 初始化数据
    deep_from = 0
    deep_to = 40
    deep = deep_file['Depth (cm)'].iloc[-1]

    while True:

        # 判断第三列数值的小数点前两位是否在当前范围内
        selected_rows = deep_file[(deep_file['Depth (cm)'] >= deep_from) & (deep_file['Depth (cm)'] <= deep_to)]

        # 将选定的行写入新的 Excel 文件
        new_file_path = os.path.join(main_folder_path, f'{deep_from}_{deep_to}.xlsx')
        selected_rows.to_excel(new_file_path, index=False)

        # 更新 m 和 n
        deep_from += 25
        deep_to += 25
        if deep_from >= deep:
            break


def cluster_layers(base_path, water_depth, duration):
    """
    读取文件中的第四列坐标数据和depth数据，组成三维坐标，进行聚类分析，划分簇，计算出每个簇的中心点；将中心点和噪声点记为鱼
    """
    # 初始化数据
    deep_from = 0
    deep_to = 40
    layer = 1
    total_fish_count = 0  # 鱼总数
    each_layer_count = []  # 每层的鱼的数量
    file_path = os.path.join(base_path, r'results\deep_frame_coordinates.xlsx')
    deep_file = pd.read_excel(file_path)['Depth (cm)'].iloc[-1]

    xml_path = os.path.join(base_path, 'output.xml')
    init_file(xml_path)  # 初始化Xml文件
    # 读取Excel文件
    while deep_from <= deep_file:
        df = pd.read_excel(
            os.path.join(base_path, r'results\split_layer', f'{deep_from}_{deep_to}.xlsx'))

        # 初始化结果数组
        all_coordinates = []
        # 遍历每一行
        for index, row in df.iterrows():
            # 提取坐标数据
            coordinates_str = row['Coordinates']

            # 使用 eval 函数将字符串转换为列表
            coordinates_list = eval(coordinates_str)

            # 使用该行左边的深度值
            depth_value = row['Depth (cm)']

            # 添加到大的数组中，每个坐标点使用相同的深度值
            all_coordinates.extend([(coord[0], coord[1], depth_value) for coord in coordinates_list])

        # 转换为 NumPy 数组
        coordinates_3d = np.array(all_coordinates)

        if len(coordinates_3d) == 0:
            each_layer_count.append(0)

        else:
            # 设置DBSCAN的参数，epsilon是半径，min_samples是核心点所需的最小样本数
            epsilon = 20.0
            min_samples = 1

            # 使用DBSCAN
            dbscan = DBSCAN(eps=epsilon, min_samples=min_samples)
            dbscan.fit(coordinates_3d)

            # 获取每个点所属的簇 (-1 表示噪声点)
            labels = dbscan.labels_

            # 计算每个簇的中心点坐标
            unique_labels = set(labels)
            cluster_centers = []

            for label in unique_labels:
                if label == -1:
                    # 跳过噪声点
                    continue

                cluster_points = coordinates_3d[labels == label]
                center = np.mean(cluster_points, axis=0)
                cluster_centers.append(center)

            # 输出每个簇的中心点坐标
            for i, center in enumerate(cluster_centers):
                all_data.append([layer, (center[0], center[1], center[2])])
                # add_coordinate(layer, i + 1, center[0], center[1], center[2], xml_path)

            # 绘制噪声点
            noise_points = coordinates_3d[labels == -1]

            # # 移除重复点
            # total_fish_count += (len(cluster_centers) + len(noise_points))
            # each_layer_count.append(len(cluster_centers) + len(noise_points))

        # 更新 m 和 n
        deep_from += 25
        deep_to += 25
        layer += 1

    data = combine_point(combine_data())

    for i in data:
        total_fish_count += len(i)
        each_layer_count.append(len(i))

    add_coordinate(data, xml_path)
    add_result(each_layer_count, total_fish_count, xml_path, water_depth, duration)


def init_file(file_path):
    '''
    文件结构：
    <data>
        <coodinate>
            <layer1>
                <cluster>1</cluster>
                <x></x>
                <y></y>
                <z></z>
            </layer1>
        </coodinate>
        <number>
            <eachLayer>[1, 2 ,3, 0]</eachLayer>
            <total>1</total>
        </number>
    </data>
    '''
    # 创建元素
    root = ET.Element("data")
    ET.SubElement(root, "coordinate")
    ET.SubElement(root, "number")
    ET.SubElement(root, "parameter")
    # 写入
    tree = ET.ElementTree(root)
    tree.write(file_path, encoding="utf-8", xml_declaration=True)


def add_result(layer_count, total_count, file_path, depth, duration):
    """
    用于总数据到Xml文件中
    """

    tree = ET.parse(file_path)
    root = tree.getroot()

    number = root.find('number')
    _eachLayer = ET.SubElement(number, "eachLayer")
    _eachLayer.text = str(layer_count)

    _total = ET.SubElement(number, "total")
    _total.text = str(total_count)

    parameter = root.find('parameter')
    _water_depth = ET.SubElement(parameter, "waterDepth")
    _water_depth.text = str(depth)

    _water_depth = ET.SubElement(parameter, "Duration")
    _water_depth.text = str(duration)

    tree.write(file_path, encoding="utf-8", xml_declaration=True)


def add_coordinate(data, file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    for index in range(len(data)):
        for point in data[index]:
            coordinate = root.find('coordinate')
            layer = ET.SubElement(coordinate, f"layer{index + 1}")

            cluster = ET.SubElement(layer, "cluster")
            cluster.text = str(point)

            _x = ET.SubElement(layer, "x")
            _x.text = str(point[0])
            _y = ET.SubElement(layer, "y")
            _y.text = str(point[1])
            _z = ET.SubElement(layer, "z")
            _z.text = str(point[2])

    tree.write(file_path, encoding="utf-8", xml_declaration=True)


def combine_data():
    classified_data = {}
    data = []
    for item in all_data:
        key = item[0]
        value = item[1]

        if key not in classified_data:
            classified_data[key] = []
        classified_data[key].append(value)

    for value in classified_data.values():
        data.append(value)

    return data


def combine_point(data):
    temp = []
    for index in range(len(data) - 1):
        data_1 = data[index]
        data_2 = data[index + 1]
        if not data_1:
            temp.append([])
        elif not data_2:
            temp.append(data_1)
        else:
            layer = []
            for i in data_1:
                flag = True
                for j in data_2:
                    if ((i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2 + (i[2] - j[2]) ** 2) ** 0.5 < 5:
                        flag = False
                        break
                if flag:
                    layer.append(i)
            temp.append(layer)
    temp.append(data[-1])
    return temp
