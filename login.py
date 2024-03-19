from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
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
        self.news_el = driver.find_element(By.XPATH, "//span[@class='p-button-label' and contains(text(), '查看更多')]/..")
        # self.todo_work = driver.find_element(By.XPATH, "//span[@class='p-button-label' and contains(text(), '待辦工作')]/..")
        # self.todo_work_el = driver.find_element(By.XPATH, "/html/body/app-root/his-navigation-layout/div[2]/his-news-info/div/div[3]/p-fieldset[1]")
    def click_news(self):
        self.news_el.click()
    def click_todo_work(self):
        self.todo_work_el.click()

# Initialize the driver and navigate to the website
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get("https://his.hepiuscare.com.tw/hpc/login")

# Instantiate the LoginPage and login with valid credentials
login_page = LoginPage(driver)
login_page.login("Neo", "Neo")
# 給些時間讓網頁載入
time.sleep(5)

# Instantiate the News and click the news
news = News(driver)
news.click_news()
time.sleep(3)
# news.click_todo_work()
# 給些時間讓網頁載入
time.sleep(600)

