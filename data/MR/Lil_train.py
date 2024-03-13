import random

def reduce_train_file(train_file, num_train_samples=2000, output_file='reduced_train.txt'):
    # 读取训练集文件
    with open(train_file, 'r', encoding='utf-8') as train_infile:
        train_lines = train_infile.readlines()

    # 随机打乱训练集
    random.shuffle(train_lines)

    # 选择前 num_train_samples 条数据
    reduced_train_lines = train_lines[:num_train_samples]

    # 将内容保存为新文件
    with open(output_file, 'w', encoding='utf-8') as reduced_train_outfile:
        reduced_train_outfile.writelines(reduced_train_lines)

# 从 train.txt 文件中提取前 1000 条数据，并保存到 reduced_train.txt 文件中
reduce_train_file('train.txt', num_train_samples=1000, output_file='reduced_train.txt')
