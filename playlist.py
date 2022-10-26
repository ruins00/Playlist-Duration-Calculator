from itertools import count
from selenium.webdriver.common.keys import Keys
import selenium
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
import datetime

choice = input("Enter a YouTube playlist URL or press enter to select default playlist ")

service = Service("D:\chromedriver_win32\chromedriver.exe")
service.start()

driver = webdriver.Remote(service.service_url)
if choice == "":
    URL = "https://www.youtube.com/playlist?list=PLBlnK6fEyqRiVhbXDGLXDk_OQAeuVcp2O"
else:
    URL = choice
driver.get(URL)
time.sleep(5)
main_body = driver.find_element_by_css_selector("body")
main_body.send_keys(Keys.CONTROL,Keys.END)
time.sleep(2)
main_body.send_keys(Keys.CONTROL,Keys.HOME)

num1 = driver.find_element_by_xpath('//*[@id="stats"]/yt-formatted-string[1]/span[1]').text
#//*[@id="page-manager"]/ytd-browse/ytd-playlist-header-renderer/div/div[2]/div[1]/div/div[1]/div[1]/ytd-playlist-byline-renderer/div/yt-formatted-string[1]/span[1]
num = int(num1.replace(',',''))

name = driver.find_element_by_xpath('//*[@id="title"]/yt-formatted-string/a').text

p1 = '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-playlist-video-list-renderer/div[3]/ytd-playlist-video-renderer[1]/div[2]/div[1]/ytd-thumbnail/a/div[1]/ytd-thumbnail-overlay-time-status-renderer/span'
lst=[]
lst.append("0:0:0")

print(lst)
for i in range(1,num+1):
    p1 = '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-playlist-video-list-renderer/div[3]/ytd-playlist-video-renderer[{}]/div[2]/div[1]/ytd-thumbnail/a/div[1]/ytd-thumbnail-overlay-time-status-renderer/span'.format(i)
    tim = driver.find_element_by_xpath(p1).text
    if tim=="":
        tim="0:0:0"
    elif tim.count(":")==1:
        tim = "0:"+tim
    lst.append(tim)
    time.sleep(0.05)

main_body.send_keys(Keys.CONTROL,Keys.END)
time.sleep(2)
main_body.send_keys(Keys.CONTROL,Keys.HOME)
time.sleep(2)

for i in lst:
    if i == 0.0 and lst.index(i)!=0 :
        ind = lst.index(i)
        for i in range((ind//10)+1):
            main_body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        for i in range((ind//10)+1):
            main_body.send_keys(Keys.PAGE_UP)
        
        p1 = '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-playlist-video-list-renderer/div[3]/ytd-playlist-video-renderer[{}]/div[2]/div[1]/ytd-thumbnail/a/div[1]/ytd-thumbnail-overlay-time-status-renderer/span'.format(ind)
        tim = driver.find_element_by_xpath(p1).text
        if tim=="":
            tim="0:0:0"
        elif tim.count(":")==1:
            tim = "0:"+tim
        lst[ind]=tim
        time.sleep(0.05)

cnt = 0
sum=datetime.timedelta()

for i in lst:

    (h, m, s) = i.split(':')

    d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
    sum += d
    if i == "0:0:0":
        cnt+=1

print("Playlist Name :",name)
print("Total no. of videos in the playlist is",num)
print("Information about",cnt-1,"videos could not be received, the total calculated duration might be inaccurate.")
print("Total duration of the playlist is calculated to be : ")
(h,m,s) = str(sum).split(':')
print(h,"HOURS")
print(m,"MINUTES")
print(s,"SECONDS")




driver.quit()
