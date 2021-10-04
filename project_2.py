from selenium import webdriver
import pandas as pd
import time

#connecting to safari driver
driver = webdriver.Safari(executable_path = '/usr/bin/safaridriver')

#connecting to website
def search_cheap_hotel(start_date,end_date):
   
   trivago='https://www.trivago.in/?aDateRange%5Barr%5D='+start_date+'&aDateRange%5Bdep%5D='+end_date+'&aPriceRange%5Bfrom%5D=0&aPriceRange%5Bto%5D=0&iRoomType=9&aRooms%5B0%5D%5Badults%5D=1&aRooms%5B1%5D%5Badults%5D=1&cpt2=2%2F101%2C64991%2F200&hasList=1&hasMap=0&bIsSeoPage=0&sortingId=1&slideoutsPageItemId=&iGeoDistanceLimit=20000&address=&addressGeoCode=&offset=0&ra=&overlayMode='
   driver.get(trivago)
   time.sleep(10)
   print('loading...')
   print('Data got fetched!!')
   print('\n')

#fetching and storing data from the website
df=pd.DataFrame()
def compile_data():
    global hotel_name_list
    global price_list
    global details_list
    global ratings_list
    time.sleep(5)
    #fetching hotel names
    hotels = driver.find_elements_by_xpath("//h3[@itemprop='name']")
    hotel_name_list = [value.text for value in hotels]
    print(hotel_name_list)
    print('\n')
    time.sleep(5)
    #fetching hotel price
    prices = driver.find_elements_by_xpath("//p[@data-qa='recommended-price']")
    price_list = [int(value.text[1:].replace(",","")) for value in prices]
    print(price_list)
    print('\n')
    time.sleep(5)
    #fetching hotel ratings
    ratings = driver.find_elements_by_xpath("//span[@itemprop='ratingValue']")
    ratings_list = [value.text for value in ratings]
    print(ratings_list)
    print('\n')
    time.sleep(5)
    #fetching hotel location details
    details= driver.find_elements_by_xpath("//p[@data-qa='item-location-details']")
    details_list = [value.text for value in details]
    print(details_list)

    for i in range(hotel_name_list):
      try:
            df.loc[i, 'Hotel_Name'] =hotel_name_list[i]
      except Exception as e:
            pass
      try:
            df.loc[i, 'Hotel_price'] =price_list[i]
      except Exception as e:
            pass
      try:
            df.loc[i, 'Hotel_rating'] =ratings_list[i]
      except Exception as e:
            pass
   
#searching cheapest hotel among the stored list of hotels
def search_cheapest():
     min_price=min(price_list)
     index=price_list.index(min_price)
     return index
#getting start date & end date (format [yyyy-mm-dd)]) for bangalore location from user 
start_date=input('enter the start date:')
end_date=input('enter the end date:')

search_cheap_hotel(start_date,end_date)
compile_data()
#printing the result
print('the cheapest hotel available from {} to {} is:'.format(start_date,end_date))
print('\n')
index_value=search_cheapest()
print(df.loc[index_value])
print('\n')
print("The complete flight information is here :")
print(details_list[index_value])
print('\n')
driver.quit()
print('THANK YOU!!!')
    