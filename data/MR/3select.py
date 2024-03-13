def split_train_dev_test(input_pos_file, input_neg_file, train_file, dev_file, test_file, train_ratio=0.6, dev_ratio=0.2):
    # 读取正面评论文件
    with open(input_pos_file, 'r', encoding='utf-8') as pos_file:
        pos_lines = pos_file.readlines()

    # 读取负面评论文件
    with open(input_neg_file, 'r', encoding='utf-8') as neg_file:
        neg_lines = neg_file.readlines()

    # 计算划分的索引
    pos_train_index = int(len(pos_lines) * train_ratio)
    pos_dev_index = int(len(pos_lines) * (train_ratio + dev_ratio))

    neg_train_index = int(len(neg_lines) * train_ratio)
    neg_dev_index = int(len(neg_lines) * (train_ratio + dev_ratio))

    # 划分训练集、开发集和测试集
    train_lines = pos_lines[:pos_train_index] + neg_lines[:neg_train_index]
    dev_lines = pos_lines[pos_train_index:pos_dev_index] + neg_lines[neg_train_index:]
    test_lines = pos_lines[pos_dev_index:] + neg_lines[neg_dev_index:]

    # 将内容保存为文件
    with open(train_file, 'w', encoding='utf-8') as train_outfile:
        train_outfile.writelines(train_lines)

    with open(dev_file, 'w', encoding='utf-8') as dev_outfile:
        dev_outfile.writelines(dev_lines)

    with open(test_file, 'w', encoding='utf-8') as test_outfile:
        test_outfile.writelines(test_lines)

# 将数据集按照60/20/20的比例划分为训练集、开发集和测试集
split_train_dev_test('rt-polarity.pos_labeled.txt', 'rt-polarity.neg_labeled.txt',
                     'train.txt', 'dev.txt', 'test.txt', train_ratio=0.6, dev_ratio=0.2)
