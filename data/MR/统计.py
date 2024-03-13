import matplotlib.pyplot as plt

def count_words(line):
    # 这个函数用于计算一行中的词数
    words = line.split()
    return len(words)

def plot_word_count(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    word_counts = [count_words(line) for line in lines]

    plt.figure(figsize=(10, 6))
    plt.bar(range(1, len(lines) + 1), word_counts, color='blue')
    plt.xlabel('行号')
    plt.ylabel('词数')
    plt.title('每行词数统计')
    plt.show()

# 替换'your_file.txt'为你的文本文件路径
plot_word_count('test.txt')
