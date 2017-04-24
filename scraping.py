#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time
from selenium import webdriver
import os

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
        # Get google search result
        search_result = browser.find_element_by_id('search')
        anchor_links = [a_tag for a_tag in search_result.find_elements_by_tag_name('a') if a_tag.text]
        time.sleep(1)
        # Print all search result in first page
        for idx, val in enumerate(anchor_links):
            print("idx: %d val: %s" % (idx, val.text))
        print(browser.title)
        # Click first link
        first_link = anchor_links[0]
        first_link.click()
        time.sleep(1)
        # Get current page screen shot
        os.system('webkit2png --ignore-ssl-check -TF %s' % browser.current_url)
    finally:
        print('...END...')
