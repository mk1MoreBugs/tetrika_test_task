import re
import csv

import requests
from bs4 import BeautifulSoup, Tag


def main():
    number_animals = count_number_animals_on_all_page()
    save_data_in_csv(number_animals)


def count_number_animals_on_all_page():
    url_path = "/wiki/Категория:Животные_по_алфавиту"
    page = get_html_page(url_path)
    number_animals_on_1_page = count_number_animals_on_page(page)
    number_animals = number_animals_on_1_page[1]

    next_page_tag_parent = number_animals_on_1_page[0]
    while next_page_tag_parent.get("href") is not None:
        url_path = next_page_tag_parent["href"]
        page = get_html_page(url_path)
        next_page_tag_parent, number_animals_on_page = count_number_animals_on_page(page)

        for key in number_animals_on_page.keys():
            number_animals[key] = number_animals.get(key, 0) + number_animals_on_page[key]

    return number_animals


def get_html_page(path: str, host: str = "https://ru.wikipedia.org") -> bytes | None:
    try:
        response = requests.get(host + path)
        return response.content
    except requests.exceptions.ConnectionError:
        print("Не удалось выполнить запрос.")


def count_number_animals_on_page(page: bytes) -> tuple[Tag | None, dict[str, int]]:
    if page is None:
        return None, dict()

    soup = BeautifulSoup(page, features="html.parser")
    tag_mw_pages = soup.find(id="mw-pages")

    dict_of_animals = {}
    tags_div_group_of_animals = tag_mw_pages.find_all("div", {"class":"mw-category-group"})
    for item in tags_div_group_of_animals:
        key = item.h3.string
        value = len(item.find_all("li"))
        dict_of_animals[key] = value
        print(f"Текущая буква: {key}")

    next_page_tag_parent = tag_mw_pages.find(string=re.compile(".*Следующая страница.*")).parent # next_page_path.get("href") != None
    return next_page_tag_parent, dict_of_animals


def save_data_in_csv(data: dict[str, int]):
    with open('beasts.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for key in data.keys():
            writer.writerow((key, data[key]))


if __name__ == '__main__':
    main()
