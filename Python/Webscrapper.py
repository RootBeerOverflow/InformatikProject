from playwright.sync_api import sync_playwright
from selectolax.parser import HTMLParser
import webbrowser
import requests

def get_html(page, asin):
    url = f"https://www.amazon.de/-/en/dp/{asin}"
    page.goto(url)
    html = HTMLParser(page.content())
    return html

def parse_html(html, asin):
    title = html.css_first("span#productTitle").text()
    price = html.css_first("span#priceblock_ourprice").text()

    print(f"Product Title: {title}")
    print(f"Product Price: {price}")
    print(f"ASIN: {asin}")

def run():


    api_url = 'https://www.pricerunner.dk/public/search/category/categoryoffers/dk/'
    
    req = requests.get(api_url).json()['categoryOffers']
    
    for item in req:
            merchant=item['merchant']['name']
            url='https://www.pricerunner.dk'+item['url']
    
            print(merchant,url)
    #searchword = "blender"
    #baseURL = "https://www.amazon.de/s?k="

    #trueUrl = baseURL + searchword
    #webbrowser.open(trueUrl)
    #asin = "B0BHF1PVCW"
    #pw = sync_playwright().start()
    #browser = pw.chromium.launch()
    #page = browser.new_page()
    #html = get_html(page, asin)
    #parse_html(html, asin)

def main():
    run()

if __name__ == "__main__":
    main()

