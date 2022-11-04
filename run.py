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

from utils import Utils


def main():
  doge = Utils(USERNAME,PASS)
  
  doge.login()


if __name__ == "__main__":
    main()