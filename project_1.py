from selenium import webdriver
import pandas as pd
import time
#connecting to safari driver
driver = webdriver.Safari(executable_path = '/usr/bin/safaridriver')
#connecting to website
def search_cheap_ticket(city_from,city_to,start_date,end_date):
   kayak='https://www.kayak.co.in/flights/'+city_from+'-'+city_to+'/'+start_date+'/'+end_date+'?sort=price_a'
   driver.get(kayak)
   print('loading...')
   time.sleep(20)
   print('Data got fetched!!')
   print('\n')

#fetching and storing data from the website
df=pd.DataFrame()
def compile_data():
    global airlines_list
    global price_list
    global details_list
    #fetching airline names
    airlines = driver.find_elements_by_xpath("//span[@class='codeshares-airline-names']")
    airlines_list = [value.text for value in airlines]
    print(airlines_list)
    print('\n')
    #fetching airline prices
    prices = driver.find_elements_by_xpath("//a[@class='book-direct-text']")
    price_list = [int((value.text.split()[1].replace("'","")).replace(",","")) for value in prices]
    print(price_list)
    print('\n')
    #fetching airline details
    details= driver.find_elements_by_xpath("//p[@style='display: none']")
    details_list = [value.text for value in details]


    for i in range(len(airlines_list)):
      try:
            df.loc[i, 'Airline_Name'] =airlines_list[i]
      except Exception as e:
            pass
      try:
            df.loc[i, 'Airline_price'] =price_list[i]
      except Exception as e:
            pass
        
   
#searching cheapest flight among the stored list of flights
def search_cheapest():
     min_price=min(price_list)
     index=price_list.index(min_price)
     return index
#getting start date & end date (format [yyyy-mm-dd)]) and from city & to city from user 
start_date=input('enter the start date:')
end_date=input('enter the end date:')
city_from=input('enter the city from:')
city_to=input('enter the city to:')
search_cheap_ticket(city_from,city_to,start_date,end_date)
compile_data()
#printing the result
print('the cheapest ticket available from {} to {} is:'.format(city_from,city_to))
print('\n')
index_value=search_cheapest()
print(df.loc[index_value])
print('\n')
print("The complete flight information is here :")
print(details_list[index_value])
print('\n')
driver.quit()
print('THANK YOU!!!')