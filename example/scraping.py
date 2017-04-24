#! /usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

browser = webdriver.Chrome('./chromedriver')
browser.get('http://www.google.com')
# seconds
delay = 3

if __name__ == '__main__':
    try:
        print('Input search word:', end='')
        search_word = input()

        WebDriverWait(browser, delay).until(
            EC.presence_of_element_located((By.NAME, 'q'))
        )
        search_input = browser.find_element_by_name('q')
        search_input.send_keys(search_word)
        search_input.submit()

        # Get google search result
        WebDriverWait(browser, delay).until(
            EC.presence_of_element_located((By.ID, 'search'))
        )
        print(browser.title)
    except TimeoutException:
        print("Loading took too much time!")
    finally:
        print('...END...')
