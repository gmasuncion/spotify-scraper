#!/bin/python env
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from local_settings import PATH
from Artist import *
from Song import *

# this will be used at deployment
import os

# start point for the scrapes + some arguments to make selenium headless
URL = "https://kworb.net/spotify/artists.html"
args = ['user-agent={user_agent}',"--window-size=1920,1080",'--ignore-certificate-errors', 
        '--allow-running-insecure-content', "--disable-extensions", "--proxy-server='direct://'", 
        "--proxy-bypass-list=*", "--start-maximized", '--disable-gpu','--disable-dev-shm-usage', '--no-sandbox']

class Scraper:
    """
    Instances of the Scraper class will do the grunt work in getting information 
    on both the searched artists and their songs.
    """
    def __init__(self):
        # Adjusting selenium to a headless browser so a window doesn't open everytime we scrape
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
        self.options = webdriver.ChromeOptions()
        self.options.headless = True
        self.binary_location = PATH
        for arg in args:
            self.options.add_argument(arg)
        self.driver = webdriver.Chrome(executable_path=self.binary_location, options=self.options)

    def scrape_artist(self, target):
        """
        Takes in a target artist and returns a list containing:
        - boolean telling us if the the artist exists in the top 100 or not
        - an instance of the Artist class representing the target, if they exist
        """
        self.driver.get(URL)
        innerHTML = self.driver.execute_script("return document.body.innerHTML")
        page = BeautifulSoup(innerHTML, "html.parser")
        tables = page.findChildren("table")
        my_table = tables[0]
        rows = my_table.findChildren(['th', 'tr'])
        for i in range(4,100):
            cells = rows[i].findChildren('td')
            link_raw = cells[1]
            name_clean = cells[1].text
            if target.lower() == name_clean.lower():
                link = link_raw.findChildren('a')
                streams_raw = cells[2].text.split(",")
                streams_clean = '' 
                for e in streams_raw:
                    streams_clean += e
                link_clean = "https://kworb.net/spotify/" + link[0].get('href')
                result_artist = Artist(name_clean,link_clean,streams_clean)
                songs_chart = self.driver.get(link_clean)
                innerHTML = self.driver.execute_script("return document.body.innerHTML")
                page = BeautifulSoup(innerHTML, "html.parser")
                tables = page.findChildren("table")
                my_table = tables[0]
                rows = my_table.findChildren(['th', 'tr'])
                # LMFAO for some reason the relevant rows of the table start showing up at index 69 o.O
                for i in range(69,79):
                    cells = rows[i].findChildren('td')
                    song_name_clean = cells[1].text
                    song_streams_clean = cells[3].text
                    result_artist.songs.append(Song(song_name_clean, song_streams_clean))
                return result_artist
        # fails silently, fix this
 
if __name__ == "__main__":
    x = Scraper()
    t = x.scrape_artist("drake")
    print(t.songs)


            


            
            
            