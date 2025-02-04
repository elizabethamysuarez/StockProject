import numpy as np
import requests

class data:

     #Calculates the variance of the price of the stock: the amount of money at risk when investing in the stock
    def get_stock_stats(stock, pwd):
        # Construct the URL
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock}&apikey={pwd}'
        r = requests.get(url)
        data = r.json()
        #print(data)
        
        place_holder = data['Time Series (Daily)']
        data_set = []
        one_hunnit = []

        data_set = np.array(data_set)
        one_hunnit = np.array(one_hunnit)
        
        for date, info in place_holder.items():
            temp = []
            temp = np.array(temp)
            for key, value in info.items():
                if key != '5. volume':
                    temp.append(float(value))
                    if (temp.__len__() == 4):
                        day = np.mean(temp)
                        data_set.append(float(day))
                        if (one_hunnit.__len__ < 100):
                            one_hunnit.append(float(day))
        
        return [data_set, one_hunnit] #returns all days vs 100 days

    def hundred_day_mean(data_set):
        data = data_set[1]
        array = np.array(data)
        mean = np.mean(array)
        return mean
             
    def variance(data_set):
        data = data_set[1]
        array = np.array(data)
        variance = np.var(array)
        return variance

    def standard_dev(data_set): #square root of varience
        data = data_set[1]
        array = np.array(data)
        stddev = np.std(array) 
        return stddev
    
    def sphiel(stock, mean, var, std): 
        print("\nThe average unit price of ", str(stock.upper()) , " within the past 100 days has been: $" , str(mean)) 

        print("\nThe unit price of " , str(stock.upper()) , "has varied by $" , str(var) , "since then.")
            
        print("\nStandard Deviation of stock price: $", str(std), "(AKA the square root of the variance).")   

        #price within last four days etc. risking this much money when investing