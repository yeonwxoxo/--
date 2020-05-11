import requests
from bs4 import BeautifulSoup
from book import extract_info
import csv

file = open("naver_books.csv", mode="w", newline="")
writer = csv.writer(file)
writer.writerow(['title', 'image', 'author', 'publisher', ])

final_result = []
for i in range(9):
    print(f'{i+1}번째 페이지 크롤링 중..')
    book_html = requests.get(f'https://book.naver.com/category/index.nhn?cate_code=100&tab=new_book&list_type=list&sort_type=publishday&page={i+1}')
    book_soup = BeautifulSoup(book_html.text, "html.parser")
    book_list_box = book_soup.find("ul", {"class" : "books_list"})
    book_list = book_list_box.find_all("li")

    final_result = final_result + extract_info(book_list)

for result in final_result:
    row = []
    row.append(result['title'])
    row.append(result['image'])
    row.append(result['author'])
    row.append(result['publisher'])
    writer.writerow(row)

print('크롤링 끝!')