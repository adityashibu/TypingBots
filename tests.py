import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from time import sleep

@pytest.fixture
def setup_driver():
    driver_path = r"C:\Users\Aditya Uni\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
    service = ChromeService(driver_path)
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

def test_typing_speed_calculation(setup_driver):
    driver = setup_driver
    driver.get("https://10fastfingers.com/typing-test/english")
    sleep(5)

    word_list = driver.execute_script("return document.getElementById('wordlist').innerHTML")
    words = word_list.split("|")

    for i in range(len(words)):
        driver.find_element(By.ID, "inputfield").send_keys(words[i] + " ")
        sleep(0.01)

    actual_typing_speed = int(driver.find_element(By.ID, "words").text)
    expected_typing_speed = len(words)

    assert actual_typing_speed == expected_typing_speed, "Typing speed calculation is incorrect."

def test_correct_words_typed(setup_driver):
    driver = setup_driver
    driver.get("https://10fastfingers.com/typing-test/english")
    sleep(5)

    word_list = driver.execute_script("return document.getElementById('wordlist').innerHTML")
    words = word_list.split("|")

    for i in range(len(words)):
        driver.find_element(By.ID, "inputfield").send_keys(words[i] + " ")
        sleep(0.01)

    typed_words = driver.find_element(By.ID, "inputfield").get_attribute("value").split(" ")
    assert typed_words == words, "Typed words do not match the expected words."

# Add more test cases as needed.
