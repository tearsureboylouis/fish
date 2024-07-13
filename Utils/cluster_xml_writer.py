import xml.etree.ElementTree as ET


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
    file = ET.SubElement(root, "file")
    file_url = ET.SubElement(file, "url")
    file_url.text = file_path

    ET.SubElement(root, "coordinate")
    number = ET.SubElement(root, "number")
    ET.SubElement(number, "eachLayer")
    ET.SubElement(number, "total")
    # 写入
    tree = ET.ElementTree(root)
    tree.write(file_path, encoding="utf-8", xml_declaration=True)


def add_result(layer_count, total_count, file_path):
    """
    用于输出每一层的数据到Xml文件中
    """
    tree = ET.parse(file_path)
    root = tree.getroot()

    number = root.find('number')
    _eachLayer = ET.SubElement(number, "eachLayer")
    _eachLayer.text = str(layer_count)

    _total = ET.SubElement(number, "total")
    _total.text = str(total_count)

    tree.write(file_path, encoding="utf-8", xml_declaration=True)


def add_coordinate(layer_num, cluster_num, x, y, z, file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    coordinate = root.find('coordinate')
    print(layer_num)
    layer = ET.SubElement(coordinate, f"layer{layer_num}")

    cluster = ET.SubElement(layer, "cluster")
    cluster.text = str(cluster_num)

    _x = ET.SubElement(layer, "x")
    _x.text = str(x)
    _y = ET.SubElement(layer, "y")
    _y.text = str(y)
    _z = ET.SubElement(layer, "z")
    _z.text = str(z)

    tree.write(file_path, encoding="utf-8", xml_declaration=True)
