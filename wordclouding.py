# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from PIL import Image
import numpy
from wordcloud import WordCloud, ImageColorGenerator

mask = numpy.array(Image.open("./masks/korea.png"))
image_colors = ImageColorGenerator(mask)


def remove_word_from_dict(words_counted):
    counted_words_dict = words_counted
    stopwords = ["ある", "いる", "あ", "い", "の", "する", "ます", "ｗ",
                 "www", "ｗｗｗ", "れ", "し", "ん", "円", "あり", "／", "ー", "杯", "さ", "枚", ]
    for stopword in stopwords:
        try:
            counted_words_dict.pop(stopword)
        except:
            pass

    return counted_words_dict


def tabelog_wordcloud(words_counted):
    keywords = remove_word_from_dict(words_counted)
    font_path = "./font/NotoSansJP-Bold.otf"
    wordcloud = WordCloud(
        font_path=font_path,
        width=1200,
        height=1200,
        background_color="white",
        mask=mask,
    )
    wordcloud = wordcloud.generate_from_frequencies(keywords)

    plt.figure(figsize=(10, 10))
    plt.imshow(wordcloud.recolor(color_func=image_colors),
               interpolation="bilinear")
    plt.axis("off")
    plt.show()
