import random

def split_train_test(input_pos_file, input_neg_file, train_file, test_file, train_ratio=0.9):
    # 读取正面评论文件
    with open(input_pos_file, 'r', encoding='utf-8') as pos_file:
        pos_lines = pos_file.readlines()

    # 读取负面评论文件
    with open(input_neg_file, 'r', encoding='utf-8') as neg_file:
        neg_lines = neg_file.readlines()

    # 随机打乱正面评论和负面评论
    random.shuffle(pos_lines)
    random.shuffle(neg_lines)

    # 计算划分的索引
    pos_split_index = int(len(pos_lines) * train_ratio)
    neg_split_index = int(len(neg_lines) * train_ratio)

    # 划分训练集和测试集
    train_lines = pos_lines[:pos_split_index] + neg_lines[:neg_split_index]
    test_lines = pos_lines[pos_split_index:] + neg_lines[neg_split_index:]

    # 将内容保存为文件
    with open(train_file, 'w', encoding='utf-8') as train_outfile:
        train_outfile.writelines(train_lines)

    with open(test_file, 'w', encoding='utf-8') as test_outfile:
        test_outfile.writelines(test_lines)

# 将80%的数据作为训练集，20%的数据作为测试集
split_train_test('rt-polarity.pos_labeled.txt', 'rt-polarity.neg_labeled.txt',
                 'train.txt', 'test.txt', train_ratio=0.9)
