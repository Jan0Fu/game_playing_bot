from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import threading

chrome_driver = "/Users/jano/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver)

driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(5)
language_select = driver.find_element(By.ID, "langSelect-EN")
language_select.click()
time.sleep(5)
cookie = driver.find_element(By.ID, "bigCookie")


def click_cookie():
    while True:
        try:
            cookie.click()
        except:
            quit()


def click_powerups():
    while True:
        try:
            time.sleep(5)
            no_cookies = int(driver.find_element(By.ID, "cookies").text.split(" ")[0])

            print(no_cookies)
            available_powerups = driver.find_elements(By.CSS_SELECTOR, ".unlocked")
            current_price_list = [int(i.text.split("\n")[1].replace(",", "")) for i in available_powerups]

            print(current_price_list)

            for i in range(len(current_price_list)-1, -1, -1):
                if no_cookies >= current_price_list[i]:
                    available_powerups[i].click()
                else:
                    pass
        except:
            pass


t1 = threading.Thread(target=click_cookie)
t2 = threading.Thread(target=click_powerups)

try:
    t1.start()
    time.sleep(8)
    t2.start()
except:
    exit()






#search_bar = driver.find_element(By.NAME, "q")
#print(search_bar.get_attribute("placeholder"))
#link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")

#driver.find_element(By.XPATH, "//*[@id='container']/li[2]/ul/li[7]/a")
#event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
#event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
# events = {}
#
# for n in range(len(event_times)):
#     events[n] = {
#         "time": event_times[n].text,
#         "name": event_names[n].text
#     }


