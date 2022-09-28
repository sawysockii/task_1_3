import requests as req
from bs4 import BeautifulSoup
import time
import json
import tqdm

url_main = 'https://spb.hh.ru/search/vacancy?area=113&text=python+разработчик&items_on_page=15'
postfix = ['&experience=noExperience','&experience=between1And3','&experience=between3And6','&experience=moreThan6']
postfix_translated = ['без опыта', 'от 1 до 3 лет', 'от 3 до 6 лет', 'более 6 лет']

sess = req.Session()
sess.headers.update({
    'location': 'https://spb.hh.ru/',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ru',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
})

data = {"data":[]}

for i in range(0,len(postfix_translated)):
    url = url_main + postfix[i]
    response = sess.get(url)
    soup = BeautifulSoup(response.text,"lxml")
    pages = soup.find_all(attrs={"data-qa":"pager-page"})
    final_page = int(pages[-1].text)+1
    for page in tqdm.tqdm(range(0,final_page)):
        time.sleep(2)
        new_url = url + f'&page={page}'
        response_new = sess.get(new_url)
        soup_new = BeautifulSoup(response_new.text,"lxml")
        vacancies = soup_new.find_all(class_="vacancy-serp-item-body__main-info")
        for vacancy in vacancies:
            vacancy_name = vacancy.find(class_="serp-item__title").text
            vacancy_salary = vacancy.find(attrs={"data-qa":"vacancy-serp__vacancy-compensation"})
            if vacancy_salary != None:
                vacancy_salary = vacancy.find(attrs={"data-qa":"vacancy-serp__vacancy-compensation"}).text
            else:
                vacancy_salary = 'не указано'
            vacancy_location = str.split(vacancy.find(attrs={"data-qa":"vacancy-serp__vacancy-address"}).text)[0]
            data["data"].append({"Title":vacancy_name,"Salary":vacancy_salary,"Region":vacancy_location,"Experience":postfix_translated[i]})

with open("data.json","w") as file:
    json.dump(data,file,ensure_ascii=False)