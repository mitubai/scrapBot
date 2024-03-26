import asyncio
import httpx
from parsel import Selector


class AnimeCrawler:
    MAIN_URL = "https://animespirit.tv/page/"

    async def get_page(self, url: str, client: httpx.AsyncClient):
        response = await client.get(url)
        return response

    def get_page_title(self):
        selector = Selector(self.response.text)
        title = selector.css("title::text").get()
        print(title)

    def get_anime_links(self, html):
        selector = Selector(html)
        cars = selector.css("div.custom-post a::attr(href)").getall()
        cars = [f"{car}" for car in cars]
        return cars[:1]

    async def get_anime_data(self):
        async with httpx.AsyncClient() as client:
            tasks = []
            for i in range(1,11):
                new_task = asyncio.create_task(self.get_page(f"{AnimeCrawler.MAIN_URL}{i}/", client))
                tasks.append(new_task)

            results = await asyncio.gather(*tasks)
            all_car_links = []
            for res in results:
                cars = self.get_anime_links(res.text)
                print(cars)
                all_car_links.extend(cars)
            return all_car_links


if __name__ == "__main__":
    crawler = AnimeCrawler()
    asyncio.run(crawler.get_anime_data())
