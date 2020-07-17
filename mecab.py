import sys
import MeCab
m = MeCab.Tagger()


def text_parsing(word):
    text = m.parse(word)
    splited_text = text.split("\n")
    text_list = []
    for text in splited_text:
        text = text.replace("\t", ",").split(",")
        text_list.append(text[0:2])
    NVA = []
    for text in text_list:
        part_of_speech = text[-1]
        if part_of_speech == "名詞":
            NVA.append(text[0])
        elif part_of_speech == "動詞":
            NVA.append(text[0])
        elif part_of_speech == "形容詞":
            NVA.append(text[0])

    return NVA
