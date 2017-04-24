#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time
from selenium import webdriver

if __name__ == '__main__':
    try:
        print('Input search word:', end='')
        search_word = input()

        browser = webdriver.Chrome('./chromedriver')
        browser.get('http://www.google.com')
        time.sleep(1)
        search_input = browser.find_element_by_name('q')
        search_input.send_keys(search_word)
        search_input.submit()
        time.sleep(1)
        print(browser.title)
    finally:
        print('...END...')
