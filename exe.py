# -*- coding: utf-8 -*-
from scrapper import get_reviews
from save import save_to_file
from wordclouding import tabelog_wordcloud
from make_dict import make_dict


data = get_reviews()
# 워드클라우드로 표현
tabelog_wordcloud(make_dict(data))
# 크롤링한 리뷰정보를 스프레드시트로 저장
save_to_file(data)
