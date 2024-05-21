import bs4
import requests
import csv
from datetime import datetime

USER_AGENT = ""


HEADERS = {
    'User-Agent': USER_AGENT,
    'Accept-Language': 'en-US, en;q=0.5',

}

def get_page_html(url):
    res = requests.get(url=url, headers=HEADERS)
    return res.content

# html = get_page_html(url)
# soup = bs4.BeautifulSoup(html, 'lxml')

def extract_product_info(url):
    product_info = {}
    print(f"Scrapping url: {url}")
    print("\n==========================================================================\n")
    html = get_page_html(url)
    soup = bs4.BeautifulSoup(html, 'lxml')
    outer_div = soup.find("div", id="prodDetails")
    table_info = outer_div.find_all("table", class_ = "a-keyvalue prodDetTable")
    for table_details in table_info:
        table_detail = table_details.find_all("tr")
        for table in table_detail:
            row_key = table.find("th").text.strip().replace("\u200e","")
            row_value = table.find("td").text.strip().replace("\u200e","")
            try:
                row_key.replace("\n","")
                row_value.replace("\n","")
            except:
                pass
            finally:
                product_info[row_key] =row_value

    return product_info


if __name__=="__main__":
    # print("main program in execution..")

    with open("amazon_products_urls.csv", "r", newline= "")as csvfile:
        reader = csv.reader(csvfile, delimiter= ',')
        for row in reader:
            url = row[0]
            print(extract_product_info(url))


        