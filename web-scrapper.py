from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


def main():
    driver = webdriver.Chrome('/Users/botour-pc/node_modules/chromedriver/bin/chromedriver')
    products = []
    prices = []
    ratings = []
    driver.get('https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniq')
    content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')
    for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
        name=a.find('div', attrs={'class':'_3wU53n'})
        price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
        rating=a.find('div', attrs={'class':'hGSR34'})
        products.append(name.text)
        prices.append(price.text)
        ratings.append(rating.text) 
    df = pd.DataFrame({'Product Name':products,'Price':prices, 'Rating': ratings}) 
    df.to_csv('products.csv', index=False, encoding='utf-8')


if __name__ == '__main__':
    main()






