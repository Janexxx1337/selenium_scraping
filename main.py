from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.python.org/")
time.sleep(2)

year = 2023
date_arr = []
month_day = driver.find_elements(By.CSS_SELECTOR, '.event-widget li time')

for d in month_day:
    date_arr.append(f"{year}-{d.text}")

events = driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')

events_arr = []
num_events = 1

for event in events:
        for num_events in range(len(events)):
            events_arr.append(f"{num_events+1}) {event.text}")
uniq = dict(zip(date_arr, events_arr))

print(uniq)
