import re

# 实现对文件中的数据按行读入，并放入list中
def data_input_from_file(filepath):
    data_list = []

    print("input data from", filepath)
    file = open(filepath)
    data_input = file.read().splitlines()
    for data in data_input:
        if data.startswith('#'):
            data_input.remove(data)
    r1 = re.compile(r'[(](.*?)[)]', re.S)
    for data in data_input:
        data_list.append(list(map(int, re.findall(r1, data)[0].split(','))))  # 对每一行数据转化为int后放入data_list中

    file.close()

    return data_list

# 将数据写入文件answer.txt
def data_output_to_file(filepath, content):
    data_output = content
    symbol_used_in_output = ', '
    print("output data to", filepath)
    file = open(filepath, 'w')
    file.write('#(carId,StartTime,RoadId...)\n')
    for data in data_output:
        data = '(' + (symbol_used_in_output.join((map(str, data)))).replace('None', ' ') + ')'
        file.write(data + '\n')
    file.close()
    return None
