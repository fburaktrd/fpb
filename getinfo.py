import requests
from bs4 import BeautifulSoup

def get():
    url1="https://www.sciencenews.org"
    url2="https://www.sciencedaily.com"
    url3="https://futurism.com/latest"

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}


    #url1
    soup1 = BeautifulSoup(requests.get(url1).text, 'html.parser')
    newest1 = soup1.find_all('ul',{'aria-labelledby':"group-heading-930"})[0].find_all("a")[0].get('href')#href linki veriyor.

    #url2
    soup2 = BeautifulSoup(requests.get(url2,headers=headers).text, 'html.parser')
    newest2 = soup2.find_all('div',{'id':'technology_heroes'})[0].find_all('div',{'class':"col-xs-6 col-md-3"})[0].find('a').get('href')

    #url3
    soup3 = BeautifulSoup(requests.get(url3).text, 'html.parser')
    newest3 = soup3.find_all('div',{'class':"space-y-3 sm:space-y-4"})[0].find_all('a')[0].get('href')
    return newest1,url2+newest2,"https://futurism.com"+newest3