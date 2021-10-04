import requests
from selenium import webdriver
import time
#connecting to safari driver
driver = webdriver.Safari(executable_path = '/usr/bin/safaridriver')
#connecting to website
websiteUrl='https://medium.datadriveninvestor.com/build-your-own-chat-bot-using-python-95fdaaed620f'
driver.get(websiteUrl)
print('loading...')
time.sleep(10)
#fetching the youtube link available in given website
element = driver.find_element_by_xpath("//a[@class='bv kt']")
url = element.get_attribute("href")
r = requests.get(url, allow_redirects=True)
#downloading video
open('chatbot_video.mp4', 'wb').write(r.content)
driver.quit()
print("Download completed..!!")