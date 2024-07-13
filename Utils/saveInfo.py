import xml.etree.ElementTree as ET
import random


def save_project_info(name, url, mp4):
    path = r'./_internal/static/ex.xml'
    tree = ET.parse(path)
    root = tree.getroot()
    # 查找
    file_node = root.find('.//file')
    recent_file = root.findall('.//recentFile')

    if len(recent_file) > 5:
        first_recent_file = file_node.find('.//recentFile')
        file_node.remove(first_recent_file)

    # 添加
    new_recent_file = ET.Element('recentFile')
    new_file_name = ET.SubElement(new_recent_file, 'fileName')
    new_file_name.text = name
    new_file_path = ET.SubElement(new_recent_file, 'filePath')
    new_file_path.text = url
    new_mp4_file = ET.SubElement(new_recent_file, 'mp4File')
    new_mp4_file.text = mp4

    # 将新的recentFile添加到file节点
    file_node.append(new_recent_file)

    # 创建一个ElementTree对象
    tree = ET.ElementTree(root)

    # 保存修改后的XML到文件
    tree.write(path, encoding='utf-8', xml_declaration=True)
