import chardet

def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']
    return encoding

def convert_to_unicode(input_file, output_file, label):
    # 检测文件编码
    detected_encoding = detect_encoding(input_file)

    try:
        # 尝试使用检测到的编码读取文件
        with open(input_file, 'r', encoding=detected_encoding) as infile:
            lines = infile.readlines()
    except UnicodeDecodeError:
        # 如果解码错误，则使用latin-1编码
        with open(input_file, 'r', encoding='latin-1') as infile:
            lines = infile.readlines()

    # 为每一行添加 '/t' 分隔符和标签，去掉首尾空格
    lines_with_tabs = [f"{line.strip()}\t{label}\n" for line in lines]

    # 将处理后的内容保存为Unicode编码的文件
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.writelines(lines_with_tabs)

# 转换正面评论文件并添加 '/t' 分隔符和标签 (1)
convert_to_unicode('rt-polarity.pos.txt', 'rt-polarity.pos_labeled.txt', '1')

# 转换负面评论文件并添加 '/t' 分隔符和标签 (0)
convert_to_unicode('rt-polarity.neg.txt', 'rt-polarity.neg_labeled.txt', '0')
