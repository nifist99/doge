
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.remote.webelement import WebElement

from config import STATUS
import random

from random_word import RandomWords
from bs4 import BeautifulSoup

import os
import time

from selenium.webdriver.common.action_chains import ActionChains

class Utils:
    def __init__(self, username, password):
        options = ChromeOptions()
        options.add_argument("--disable-notifications")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument("--log-level=3")
        options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(executable_path='C:\chromedriver_win32\chromedriver.exe',options=options)

        timeout=300

        self.wait = WebDriverWait(self.driver, timeout)
        self.baseurl = "https://dogenetwork.dog/"
        self.targeturl = self.baseurl
        self.username = username
        self.password = password

    def login(self):
        try:
            self.driver.get(self.baseurl)

            element = self.driver.find_element(By.XPATH , '//*[@id="contnet"]/div/div[2]/div/div[3]')

            actionChains = ActionChains(self.driver)

            actionChains.move_to_element(element)

            ## actions.click()

            actionChains.perform()

            time.sleep(3)
            # self.wait.until(EC.presence_of_element_located((By.XPATH, '//button[text()="Log In"]'))).click()
            self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="login"]/div[2]/label[1]/input'))).send_keys(self.username)
            self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="login"]/div[2]/label[2]/input'))).send_keys(self.password)
            time.sleep(5)
            self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="login"]/div[2]/button'))).click()
            time.sleep(10)
            i = 1
            while i < 10000:

                if i % 2 == 0:
                    r = RandomWords()

                    status = r.get_random_word()

                    n = status+' '
                    print(status)
                    time.sleep(5)
                    element1 = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="contnet"]/div/div/div[3]/div[1]/div[1]/button[1]'))).click()
                    time.sleep(5)
                    element2 = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="post-textarea"]/div/textarea'))).click()
                    time.sleep(10)
                    element3 = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="post-textarea"]/div/textarea'))).send_keys(n)
                    time.sleep(5)
                    element4 = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="publisher-button"]'))).click()
                    time.sleep(10)
                # self.driver.refresh()
                time.sleep(10)
                self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="contnet"]/div/div/div[3]/div[1]/div[5]'))).click()
                time.sleep(8)
                post = self.driver.find_element(By.XPATH, '//*[@id="posts"]/div[1]/div[1]')
                id = post.get_attribute("data-post-id")
                print(id)
                time.sleep(8)
                element6  = self.driver.find_element(By.XPATH, '//*[@id="react_'+id+'"]')
                element6.click()

                # self.driver.refresh()
                time.sleep(10)

                self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="contnet"]/div/div/div[3]/div[1]/div[5]'))).click()
                time.sleep(8)
                post7 = self.driver.find_element(By.XPATH, '//*[@id="posts"]/div[1]/div[1]')
                id7 = post7.get_attribute("data-post-id")
                print(id7)
                time.sleep(8)
                element7  = self.driver.find_element(By.XPATH, '//*[@id="react_'+id7+'"]')
                element7.click()

                # self.driver.refresh()
                time.sleep(10)

                self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="contnet"]/div/div/div[3]/div[1]/div[5]'))).click()
                time.sleep(8)
                post8 = self.driver.find_element(By.XPATH, '//*[@id="posts"]/div[1]/div[1]')
                id8 = post8.get_attribute("data-post-id")
                print(id8)
                time.sleep(8)
                element8  = self.driver.find_element(By.XPATH, '//*[@id="react_'+id8+'"]')
                element8.click()
                time.sleep(8)

                i +=1

            Utils.soup(self)
        except:

            Utils.soup(self)

    
    def validate_login(self):
        """
        Validates login
        """
        try:
            # look for user avatar
            self.wait.until(EC.presence_of_element_located((By.XPATH, '///*[@id="contnet"]/div/div/div[3]/div[1]/div[1]/a"]')))
            return True
        except:
            return False

    
    def post(self):
        """
        Initiates login with username and password

        //*[@id="post-textarea"]/div/textarea

        //*[@id="publisher-button"]
        """
        try:
        #menambahkan user agent
            n = 1
            while n < 10:
                status = random.choice(status)
                time.sleep(5)
                self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="contnet"]/div/div/div[3]/div[1]/div[1]/button[1]'))).click()
                time.sleep(5)
                self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="post-textarea"]/div/textarea'))).send_keys(status)
                time.sleep(10)
                self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="publisher-button"]'))).click()
                n +=1
                time.sleep(10)
            return True
        except:
            return False

    
    def like_coment(self):
        
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="contnet"]/div/div/div[3]/div[1]/div[5]'))).click()
        time.sleep(5)
        self.wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div[2]/div/div/div[3]/div[1]/div[6]/div/div[1]/div[1]/div/div/div[2]/div[5]/div[1]/div[1]/div/div/span'))).click()
        time.sleep(5)
        self.wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div[2]/div/div/div[3]/div[1]/div[6]/div/div[1]/div[1]/div/div/div[2]/div[4]/div[1]/div[2]'))).click()
        time.sleep(5)
        self.wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div[2]/div/div/div[3]/div[1]/div[6]/div/div[1]/div[1]/div/div/div[4]/div[4]/div[1]/div/div[2]/textarea'))).click()

        r = RandomWords()

        status = r.get_random_word()

        n = status+' '
        print(status)

        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="post-textarea"]/div/textarea'))).send_keys(status)
        time.sleep(5)
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="post-textarea"]/div/textarea'))).send_keys(Keys.ENTER)
        time.sleep(5)

    def soup(self):

        try:
            time.sleep(10)
            i = 1
            while i < 10000:

                if i % 2 == 0:
                    r = RandomWords()

                    status = r.get_random_word()

                    n = status+' '
                    print(status)
                    time.sleep(5)
                    element1 = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="contnet"]/div/div/div[3]/div[1]/div[1]/button[1]'))).click()
                    time.sleep(5)
                    element2 = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="post-textarea"]/div/textarea'))).click()
                    time.sleep(10)
                    element3 = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="post-textarea"]/div/textarea'))).send_keys(n)
                    time.sleep(5)
                    element4 = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="publisher-button"]'))).click()
                    time.sleep(10)
                # self.driver.refresh()
                time.sleep(10)
                self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="contnet"]/div/div/div[3]/div[1]/div[5]'))).click()
                time.sleep(8)
                post = self.driver.find_element(By.XPATH, '//*[@id="posts"]/div[1]/div[1]')
                id = post.get_attribute("data-post-id")
                print(id)
                time.sleep(8)
                element6  = self.driver.find_element(By.XPATH, '//*[@id="react_'+id+'"]')
                element6.click()

                # self.driver.refresh()
                time.sleep(10)

                self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="contnet"]/div/div/div[3]/div[1]/div[5]'))).click()
                time.sleep(8)
                post7 = self.driver.find_element(By.XPATH, '//*[@id="posts"]/div[1]/div[1]')
                id7 = post7.get_attribute("data-post-id")
                print(id7)
                time.sleep(8)
                element7  = self.driver.find_element(By.XPATH, '//*[@id="react_'+id7+'"]')
                element7.click()

                # self.driver.refresh()
                time.sleep(10)

                self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="contnet"]/div/div/div[3]/div[1]/div[5]'))).click()
                time.sleep(8)
                post8 = self.driver.find_element(By.XPATH, '//*[@id="posts"]/div[1]/div[1]')
                id8 = post8.get_attribute("data-post-id")
                print(id8)
                time.sleep(8)
                element8  = self.driver.find_element(By.XPATH, '//*[@id="react_'+id8+'"]')
                element8.click()
                time.sleep(8)

                i +=1

            Utils.soup(self)
        except:

            Utils.soup(self)