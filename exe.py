from scrapper import get_reviews
from save import save_to_file


data = get_reviews()
save_to_file(data)
