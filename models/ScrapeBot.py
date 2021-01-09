#!/bin/python env
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from local_settings import PATH

# this will be used at deployment
import os

URL = "https://kworb.net/spotify/artists.html"

class ScrapeBot:
    def __init__(self):
        # Adjusting selenium so that a browser doesn't open everytime we scrape
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
        self.options = webdriver.ChromeOptions()
        self.options.headless = True
        self.binary_location = PATH
        self.options.add_argument('user-agent={user_agent}')
        self.options.add_argument("--window-size=1920,1080")
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument('--allow-running-insecure-content')
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("--proxy-server='direct://'")
        self.options.add_argument("--proxy-bypass-list=*")
        self.options.add_argument("--start-maximized")
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument('--no-sandbox')
        self.driver = webdriver.Chrome(executable_path=self.binary_location, options=self.options)
        self.driver.get(URL)
        print(self.driver.title)


