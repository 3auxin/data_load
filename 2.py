import nltk
import spikingjelly

# 下载词性标注器
# nltk.download('averaged_perceptron_tagger')

text = "I love natural language processing"
tokens = nltk.word_tokenize(text)
tags = nltk.pos_tag(tokens)

# 输出分类结果
for word, pos in tags:
    print(word, pos)
