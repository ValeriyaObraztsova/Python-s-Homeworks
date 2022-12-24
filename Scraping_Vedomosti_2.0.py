import requests as rq
from bs4 import BeautifulSoup

#ЗАГРУЖАЮ ГЛАВНУЮ СТРАНИЧКУ
url = 'https://www.vedomosti.ru/ecology'
page = rq.get(url)
#print(page.status_code)

#ЗАГРУЖАЮ СУПЬ
soup = BeautifulSoup(page.text, features="html.parser")
#print(soup.prettify())

#ИЗВЛЕКАЮ 4 ССЫЛКИ ВЫПУСКОВ С ГЛАВНОЙ СТРАНИЧКИ
urls = []
for link in soup.find_all('a', class_='release__link'):
    urls.append(link.get('href'))
#print(urls)

#ДОБАВЛЮ ДОМЕННОЕ ИМЯ И ПОЛУЧЕННЫЕ ССЫЛКИ В СПИСОК
full_urls = []
for i in soup.find_all('a', class_='release__link'):
    full_urls.append(f'https://www.vedomosti.ru{i["href"]}')
#print(full_urls)

# красиво соберем все ссылки на все новости из 4 релизов за один шаг:
all_urls_all_releases = []
for link in full_urls:
  page0 = rq.get(link)
  soup0 = BeautifulSoup(page0.text, features="html.parser")
  for i in soup0.find_all('a'):
    if i.get('data-vr-contentbox-url')!= None:
        u = 'https://www.vedomosti.ru'+ i.get('href')
        all_urls_all_releases.append(u)
#print(all_urls_all_releases)

#НАПИШЕМ ФУНКЦИЮ, ПРОСТИ ЕЁ ГОСПОДИ
def GetNews(url0):
    page0 = rq.get(url0)
    soup0 = BeautifulSoup(page0.text, features="html.parser")
    for i in soup0.find_all('a'):
      if 'authors' in i.get('href'):
        author = i.text.strip()
    for i in soup0.find_all('time'):
      date = i.get('datetime')[:10]
    for i in soup0.find_all('h1'):
      title = i.text.strip()
    for i in soup0.find_all('em'):
      subtitle = i.text.strip()
    text_list = soup0.find_all('p', class_='box-paragraph__text')
    text = []
    for i in text_list:
        text.append(i.text)
    final_text = ''.join(text)
    return url0, author, date, title, subtitle, final_text

#СОЗДАЁМ СПИСОК С НОВОСТЯМИ
news = []
for link in all_urls_all_releases:
    new = GetNews(link)
    news.append(new)
#print(news)

#ЗАКИНЕМ ВСЁ В ТАБЛИЧКУ
import pandas as pd
df = pd.DataFrame(news)
df.head()
#print(df)

#ПЕРЕИМЕНУЮ СТОЛБЦЫ
df.columns = ['link', 'author', 'date', 'title', 'subtitle', 'text']

#ЗАКИНЕМ В ЭКСЕЛЬ
df.to_excel('Vedomosti_Ecology_News.xlsx')