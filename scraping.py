#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time
from selenium import webdriver
import re
import os

if __name__ == '__main__':
    try:
        print('Input search word:', end='')
        # input yukihirai0505
        search_word = input()

        browser = webdriver.Chrome('./chromedriver')
        browser.get('http://www.google.com')
        time.sleep(1)
        search_input = browser.find_element_by_name('q')
        search_input.send_keys(search_word)
        search_input.submit()
        time.sleep(1)
        print(browser.title)
        anchor_link = browser.find_element_by_link_text('yukihirai0505 - Qiita')
        time.sleep(1)
        print(anchor_link.click())
        print(browser.title)
        os.system('webkit2png --ignore-ssl-check -TF %s' % browser.current_url)
    finally:
        print('...END...')
