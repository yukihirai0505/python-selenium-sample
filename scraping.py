#! /usr/bin/env python
# -*- coding: utf-8 -*-


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os

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
        print(browser.title)
        # Get google search result
        WebDriverWait(browser, delay).until(
            EC.presence_of_element_located((By.ID, 'search'))
        )
        search_result = browser.find_element_by_id('search')
        anchor_links = [a_tag for a_tag in search_result.find_elements_by_tag_name('a') if a_tag.text]

        # Print all search result in first page
        for idx, val in enumerate(anchor_links):
            print("idx: %d val: %s" % (idx, val.text))

        # Click first link
        first_link = anchor_links[0]
        first_link.click()

        # Get current page screen shot
        os.system('webkit2png --ignore-ssl-check -TF %s' % browser.current_url)
    except TimeoutException:
        print("Loading took too much time!")
    finally:
        print('...END...')
