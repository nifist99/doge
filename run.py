from config import PASS,USERNAME
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import pyfiglet as f
from utils import Utils

def authors():
    style = f.figlet_format("Tanlalana")
    print(style)
    print("\033[31m----- \033[93mVersi : \033[92mhttps://www.youtube.com/c/Tanlalana/channels \033[31m-----")
    print("\033[31m----- \033[93mAuthor : \033[92mTanlalana Bot Pyton   \033[31m-----")
    print("\033[31m----- \033[93mNote : \033[92mSilahkan Di Modif Sesuka Anda Kawan   \033[31m-----")

def main():
  authors()

  doge = Utils(USERNAME,PASS)
  
  doge.login()


if __name__ == "__main__":
    main()