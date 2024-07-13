import os
import xml.etree.ElementTree as ET


def get_layers_data(base_path):
    path = os.path.join(base_path, "output.xml")
    tree = ET.parse(path)
    root = tree.getroot()

    each_layer = root.findall(".//eachLayer")
    total_num = root.findall(".//total")
    for i in range(len(each_layer)):
        if each_layer[i].text != None:
            each_layer = each_layer[i].text[1:-1].split(', ')

    for i in range(len(total_num)):
        if total_num[i].text != None:
            total_num = total_num[i].text
    return each_layer, total_num


def get_layer_data(base_path):
    path = os.path.join(base_path, "output.xml")
    tree = ET.parse(path)
    root = tree.getroot()

    xyz = []

    each_layer = root.find(".//eachLayer").text[1:-1].split(', ')
    for i in range(len(each_layer)):
        data = root.findall(f".//layer{i + 1}")
        index, x, y, z = [], [], [], []
        for j in range(len(data)):
            index.append(j + 1)
            x.append(float(data[j].find("x").text))
            y.append(float(data[j].find("y").text))
            z.append(-float(data[j].find("z").text))
        xyz.append([index, x, y, z])
    return xyz


def get_xy_point(base_path, index):
    path = os.path.join(base_path, "output.xml")
    tree = ET.parse(path)
    root = tree.getroot()

    fish_index, x, y = [], [], []
    data = root.findall(f".//layer{index}")
    for i in range(len(data)):
        fish_index.append(i + 1)
        x.append(float(data[i].find("x").text))
        y.append(float(data[i].find("y").text))
    return fish_index, x, y
