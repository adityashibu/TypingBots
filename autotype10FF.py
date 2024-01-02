from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from time import sleep

driverPath = r"C:\Users\Aditya Uni\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"

service = ChromeService(driverPath)
driver = webdriver.Chrome(service=service)

driver.get("https://10fastfingers.com/typing-test/english")
sleep(5)

word_list = driver.execute_script("return document.getElementById('wordlist').innerHTML")
words = word_list.split("|")

for i in range(len(words)):
    driver.find_element(By.ID, "inputfield").send_keys(words[i] + " ")
    sleep(0.01)

# Pause to keep the window open
input("Press Enter to close the browser window...")
