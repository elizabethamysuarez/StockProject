
import numpy as np
import requests
from bs4 import BeautifulSoup


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
    price = fail_safe(stock)
  price = price.split()
  price = price[0]
  return price

#Calculates the variance of the price of the stock: the amount of money at risk when investing in the stock
def get_stock_stats(stock, api):
  # Construct the URL
  url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock}&apikey={api}'
  r = requests.get(url)
  data = r.json()
  print(data)#
  
  place_holder = data['Time Series (Daily)']
  data_set = []
  
  for date, info in place_holder.items():
    for key, value in info.items():
      if key != '5. volume':
        data_set.append(float(value))
        
  data_set = np.array(data_set)
  
  average = np.mean(data_set) 
  print("\n\nThe average unit price of " + stock.upper() + " within the past 100 days has been: $" + str(average)) 

  variance = np.var(data_set) 
  print("\n\nThe unit price of " + stock.upper() + " has varied by $" + str(variance) + " since then.")
    
  stddev = np.std(data_set) 
  print("\n\nStandard Deviation: ", str(stddev))   

#price within last four days etc. risking this much money when investing
if __name__ == "__main__":
 api = input("Enter Api Key: ")
  #Stock Unit Price Returner Instructions
 print("Welcome to the Stock Price Returner!")
 print("Enter 'quit' to exit.")

  #Take user input and return stock price 
 stock = input("Enter stock symbol: ")
 stock = stock.upper()
 while (stock != 'quit'):
   stock = stock.upper()
   print("The unit price of " + stock + " is $" + get_stock_price(stock) + ".")

  #Stock Statistics Giver
   print("Would you like to know how much is at risk for that stock based on the last 100 days? Reply Y/N ")
   reply = input()
   reply = reply.upper()
   if reply == ('Y'):
      print("Here are the results for " + stock + ": \n")
      get_stock_stats(stock, api)
      
  #Continuation of itseration of stock input loop
   stock = input("Enter next stock symbol or enter 'quit' to quit: ")

  #Exit message
 print("Exited Successfully.")

 
