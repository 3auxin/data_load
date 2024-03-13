import csv

tsv_file_path = 'test.tsv'
txt_file_path = 'test.txt'

with open(tsv_file_path, 'r', newline='', encoding='utf-8') as tsvfile:
    # 使用制表符作为分隔符创建csv读取器
    reader = csv.reader(tsvfile, delimiter='\t')

    with open(txt_file_path, 'w', newline='', encoding='utf-8') as txtfile:
        # 使用换行符作为分隔符创建csv写入器
        writer = csv.writer(txtfile, delimiter='\t')

        # 逐行写入文本文件
        for row in reader:
            writer.writerow(row)
