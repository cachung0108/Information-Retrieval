# -*- coding: utf-8 -*-
import jieba
import json

with open('wiki_article_list_2023_tra.json', 'r', encoding='utf-8') as file:
    docs = json.load(file)

with open('stopwords.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

stopwords = set(line.strip() for line in lines)

inverted_index = {}

for doc_id, doc in enumerate(docs):
    words = jieba.cut(doc)
    for word in words:
        if word not in stopwords:
            if word not in inverted_index:
                inverted_index[word] = []
            inverted_index[word].append(doc_id)

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(inverted_index, f, ensure_ascii=False, indent=4)