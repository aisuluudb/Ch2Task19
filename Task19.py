from bs4 import BeautifulSoup
import requests
import csv

def get_html(url):
    response = requests.get(url)
    return response.text

def get_total_pages(html):
    soup = BeautifulSoup(html, 'html.parser')
    pages = soup.find('ul', class_='pagn').find_all('li', class_='pagn-page').find('a').get('href')
    total_pages = pages.split('=')[-1]
    return int(total_pages)

def write_csv(data):
    with open('lalafo.csv','a') as f:
        writer = csv.writer(f)

        writer.writerow ((data['title'], data['price'], data ['link_to_photo']))


def get_page_data(html):
    soup = BeautifulSoup(html,'html.parser')

    ads = soup.find('div',class_='mr-3').find_all('article', class_='listing-item')
    
    for ad in ads:
        try:
            title = ad.find('a', class_='item listing-item-title').text
            print(title)
        except:
            title = ''

        try:
            price = ad.find("div", class_ = "listing-item-main").find("p",class_ = "listing-item-title").text.strip()
            print(price)
        except:
            price = ''
        
        try:
            link_to_photo = ad.find('img', class_='listing-item-photo link-image').text.strip()
            print(link_to_photo)
        except:
            link_to_photo = ''

            data = {'title': title, 'price': price, 'link_to_photo': link_to_photo}
            write_csv(data)
        


def main():
    url = 'https://lalafo.kg/kyrgyzstan/mobilnye-telefony-i-aksessuary/mobilnyetelefony'
    base_url = 'https://lalafo.kg/kyrgyzstan/mobilnye-telefony-i-aksessuary'
    page_url = '?page='
    total_pages = get_total_pages(get_html(url))
    
    for i in range(1,10):
        url_gen = base_url + page_url + str(i)
        html = get_html(url_gen)
        data = get_page_data(html)


if __name__ == "__main__":
    main()
