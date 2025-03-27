# import pandas as pd

# # 读取txt文件
# txt_file_path = '/home/fuyali/emotionClassification/emotion1/test.txt'
# df = pd.read_csv(txt_file_path, sep='\t', header=None, names=['text', 'label'])

# # 将数据保存为csv文件
# csv_file_path = '/home/fuyali/emotionClassification/emotion/test.csv'
# df.to_csv(csv_file_path, index=False,header=False)

import pandas as pd

def convert_txt_to_csv(txt_file_path, csv_file_path, delimiter='\t'):
    # 读取txt文件，使用strip去除多余空白
    with open(txt_file_path, 'r', encoding='utf-8') as file:
        lines = [line.strip().split(delimiter) for line in file.readlines()]

    # 将数据保存为csv文件，不保存索引和列名
    df = pd.DataFrame(lines)
    df.to_csv(csv_file_path, index=False, header=False)

# 替换为实际的文件路径和文件名
txt_file_path = '/home/fuyali/emotionClassification/emotion1/val.txt'
csv_file_path = '/home/fuyali/emotionClassification/emotion/val.csv'

convert_txt_to_csv(txt_file_path, csv_file_path)
