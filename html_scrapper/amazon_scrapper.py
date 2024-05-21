# Must be executed in the command line of the current directory for virtualenv activation
# Set-ExecutionPolicy Unrestricted -Scope Process
from datetime import datetime
import requests
import csv
import bs4
# includding multithreading and  concurrency...
import concurrent.futures
from tqdm import tqdm


# DEFINE headers for the requests module....
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"


HEADERS = {
    'User-Agent': USER_AGENT,
    'Accept-Language': 'en-US, en;q=0.5',

}
# constants
NO_OF_THREADS = 10

def get_page_html(url):
    res = requests.get(url=url, headers=HEADERS)
    return res.content

# html = get_page_html(url)
# soup = bs4.BeautifulSoup(html, 'lxml')

def extract_product_info(url, output):
    product_info = {}
    # print("\n =========================================")
    # print(f"Scrapping url: {url}")
    # print("\n==========================================================================\n")
    html = get_page_html(url)
    soup = bs4.BeautifulSoup(html, 'lxml')
    price_span = soup.find("span", attrs={"class":"a-offscreen"})
    price_span = price_span.getText()
    price_span = price_span.strip("$").replace(",","")
    try:
        price_span = float(price_span)

    except:
        print("unable to pass the product price...")
    
    product_info["Price"]= price_span
    product_info["Title"]= get_title_product(soup)
    product_info["Ratings"] = get_product_ratings(soup)
    product_info.update(get_technical_details(soup))

    output.append(product_info)
    # return product_info
    

def get_technical_details(soup):
    technical_details = {}
    outer_div = soup.find("div", id="prodDetails")
    table_info = outer_div.find_all("table", class_ = "a-keyvalue prodDetTable")
    for table_details in table_info:
        table_detail = table_details.find_all("tr")
        for table in table_detail:
            row_key = table.find("th").text.strip().replace("\u200e","").replace("\n","")
            row_value = table.find("td").text.strip().replace("\u200e","").replace("\n","")
            technical_details[row_key] =row_value
    return technical_details




def get_title_product(soup):
    product_title = soup.find("span",id="productTitle")
    product_title = product_title.text.strip()
    return product_title

def get_product_ratings(soup):
    ratings_outer = soup.find("div", id="averageCustomerReviews")
    ratings = ratings_outer.find("span", id="acrPopover")
    ratings_inner = ratings.find("a")
    actual_ratings = ratings_inner.find("span", class_="a-size-base a-color-base")
    actual_ratings = actual_ratings.text
    try:
        actual_ratings =float(actual_ratings)
    except ValueError:
        print("Value could not be parsed!!!")
    finally:
        return actual_ratings

  

    
if __name__=="__main__":
    # print("main program in execution..")
    products_data = []
    urls = []

    with open("amazon_products_urls.csv", "r", newline= "")as csvfile:
        urls = list(csv.reader(csvfile, delimiter= ','))
        with concurrent.futures.ThreadPoolExecutor(max_workers=NO_OF_THREADS)as executor:

        # for row in reader:
        #     url = row[0]
        #     products_data.append(extract_product_info(url))
            # print(urls)
            for wkn in tqdm(range(0, len(urls))):
                executor.submit(extract_product_info,urls[wkn][0], products_data)
    #
            
            
    output_file = "output-{}.csv".format(datetime.today().strftime("%y-%m-%d"))
    with open(output_file, "w", encoding="utf-8") as output:
        writer = csv.writer(output)
        writer.writerow(products_data[0].keys())
        for product in products_data:
            writer.writerow(product.values())

    # print("\n\n===============================================================\n\n")

# Now introducing beautiful soup into the process
