from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
    
# 指定 WebDriver 的路径
driver = webdriver.Chrome()
driver.implicitly_wait(10)
# 打开醫療資訊系統的登录页面
driver.get("https://his.hepiuscare.com.tw/hpc/login")

# 找到用户名和密码的输入框，并输入凭据
# username_input = driver.find_element(By.NAME, "username")
# password_input = driver.find_element(By.NAME, "password")
# 选择一种定位方式
username_input = driver.find_element(By.ID,"UserName")
username_input.send_keys("Neo")
password_input = driver.find_element(By.CSS_SELECTOR,'input[placeholder="請輸入密碼"]')
password_input.send_keys("Neo")
# username_input.send_keys("your_username")
# password_input.send_keys("your_password")

# 找到登录按钮并点击 ，使用XPATH 通过按钮内部的 span 的类名来定位
login_button = driver.find_element(By.XPATH, "//span[@class='p-button-label' and contains(text(), '登入')]/..")
login_button.click()


# test 最新消息
# test1 
# 等待页面加载
time.sleep(3)

# 导航到病人信息录入页面
driver.get("http://your-medical-info-system.com/patient_entry")

# 输入病人信息
patient_name_input = driver.find_element(By.NAME, "patient_name")
patient_age_input = driver.find_element(By.NAME, "patient_age")
patient_name_input.send_keys("John Doe")
patient_age_input.send_keys("30")

# 提交表单
submit_button = driver.find_element(By.ID, "submit_button")
submit_button.click()

# 验证信息是否正确保存，这里仅示例等待和关闭浏览器，实际应根据页面反馈进行验证
time.sleep(3)

# 关闭浏览器
driver.quit()
