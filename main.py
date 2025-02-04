
import numpy as np
import requests
from bs4 import BeautifulSoup
from scraper import Scraper

def typical():
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

 


#price within last four days etc. risking this much money when investing
if __name__ == "__main__":
  Scraper.return_script("AAPL")