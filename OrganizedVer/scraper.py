import numpy as np
import requests
from bs4 import BeautifulSoup


class scraper:

    def bypass(stock):
        # Construct the URL
        url = f'https://www.google.com/search?q={stock}+stock'

            # Send a GET request to the URL
        response = requests.get(url)

            # Check if request was successful (status code 200)
        if response.status_code == 200:
                # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')  

        all_links = []
        for link in soup.find_all('a'):
            all_links.append(link.get('href'))
        
        for item in all_links:
            if (item.find("search?") != -1):
                return str(item)
    
    def wall_scraper(item, stock):
        #getting url: data interface/scraping origin
        url = item

        # Send a GET request to the URL
        response = requests.get(url)

        # Check if request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')

        print(soup.prettify())
        #con't in main
#google updated website front/backend to include defenses against classic webscraping as beautiful soup

    def fail_safe(stock):
        # Construct the URL
        url = f'https://www.google.com/search?q={stock}+price'
        
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')
            #print(soup)
        # Find the element containing the weather information
            element = soup.find('div', class_='BNeawe iBp4i AP7Wnd')

            # Extract the text from element
        try:
            price = element.text.strip()
        except:
            print(soup.text)
            print("Failed to retrieve stock unit price information.")
            return "--"
        price = price.split()
        price = price[0]
        return price


        #gets stock info through url, then process
    def get_stock_price(stock):
        # Construct the URL
        url = f'https://www.google.com/search?q={stock}+stock'

        # Send a GET request to the URL
        response = requests.get(url)

        # Check if request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')
            #print(soup)
        # Find the element containing the weather information
        element = soup.find('div', class_='BNeawe iBp4i AP7Wnd')

        # Extract the text from element
        try:
            price = element.text.strip()
        except:
            price = scraper.fail_safe({stock})
        price = price.split()
        price = price[0]
        return price