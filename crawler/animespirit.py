import httpx
from parsel import Selector
from pprint import pprint


class AnimeSpiritCrawler:
    MAIN_URL = "https://animespirit.tv/"


    def get_anime(self):
        self.response = httpx.get(AnimeSpiritCrawler.MAIN_URL)
        print(self.response.status_code)
        print(self.response.text[:250])

    def get_page_title(self):
        selector = Selector(self.response.text)
        title = selector.css("title::text").get()
        # print(title),

    def get_anime_links(self):
        selector = Selector(self.response.text)
        animes = selector.css("div.custom-poster a::attr(href)").getall()
        animes = [f"{anime}" for anime in animes]
        return animes[:10]

if __name__ == "__main__":
    crawler = AnimeSpiritCrawler()
    crawler.get_anime()
    cars = crawler.get_anime_links()
    pprint(cars)