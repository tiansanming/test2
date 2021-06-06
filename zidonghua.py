from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.get('https://blog.csdn.net/dpl12/article/details/102808985')
shou = driver.find_element_by_xpath('//*[@id="csdn-toolbar"]/div/div/div[1]/ul/li[1]/a')
shou.click()
py = driver.find_element_by_xpath('//*[@id="floor-nav_62"]/div/div/div[2]/ul/li[1]/a')
sleep(10)
py.click()
sleep(10)
quit = driver.find_element_by_xpath('//*[@id="csdn-nav-second"]/div/div/ul/li[1]/a')
sleep(10)
quit.click()



