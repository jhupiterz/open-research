# Main code where other modules are called

from startupjh.data import scraper_api
from startupjh.reports import pub_per_year
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
import re
from bs4 import BeautifulSoup

APIKEY = "e3ca696e087b4afc19a116f42f24b9aa"
BASE_URL = f"http://api.scraperapi.com?api_key={APIKEY}&url="

if __name__ == "__main__":
    topic_title = input("Enter key words: ")
    topic = topic_title.replace(" ", "+")
    
    pub_per_year(topic)
    