from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import WebDriverWait
from dotenv import load_dotenv
import os
load_dotenv()

username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
HEP = os.getenv('HEP')

class LoginPage:
    def __init__(self,driver) :
        self.driver = driver
        self.username_input = driver.find_element(By.ID,"UserName")
        self.password_input = driver.find_element(By.CSS_SELECTOR,'input[placeholder="請輸入密碼"]')
        self.login_button = driver.find_element(By.XPATH, "//span[@class='p-button-label' and contains(text(), '登入')]/..")
    def login(self,username,password):
        self.username_input.send_keys(username)
        self.password_input.send_keys(password)
        # 使用XPATH 來定位 「登入」按鈕
        self.login_button.click()

class News:
    def __init__(self,driver):
        self.driver = driver
        

    def click_news(self):
        # 使用XPATH 來定位 「查看更多」按鈕，使用dev_tools 的copy XPATH
        # self.news_el = driver.find_element(By.XPATH, "//span[@class='p-button-label' and contains(text(), '查看更多')]/..")
        self.news_el = driver.find_element(By.XPATH, "/html/body/app-root/his-navigation-layout/div[2]/his-user-profile/div/div[2]/div[1]/div/button/span")
        self.news_el.click()
    
    def search_news(self,text):
        wait = WebDriverWait(self.driver, 10)  # 等待最多10秒
        self.search_input = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="搜尋"]')))
        self.search_input.send_keys(text)
    # def click_todo_work(self):
    #     wait = WebDriverWait(self.driver, 10)  # 等待最多10秒
    #     self.fieldset_legend = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'fieldset p-fieldset-legend')))
    #             # 验证是否为“公告訊息”，并点击
    #     if self.fieldset_legend.text == '公告訊息':
    #         print('找到“公告訊息”，现在点击它。')
    #         self.fieldset_legend.click()
    #     else:
    #         print('没有找到“公告訊息”。')
        # self.fieldset_legend.click()

# Initialize the driver and navigate to the website
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(HEP)

# Instantiate the LoginPage and login with valid credentials
login_page = LoginPage(driver)
login_page.login(username, password)
# 給些時間讓網頁載入
time.sleep(5)

# Instantiate the News and click the news
news = News(driver)
news.click_news()
time.sleep(2)

# jump to the news page and type whatever text to the search bar.
news.search_news('de')
time.sleep(6)
# 給些時間讓網頁載入
time.sleep(600)

