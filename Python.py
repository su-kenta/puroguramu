from selenium.webdriver.common.by import By 
from selenium import webdriver 
import time 
 
USERID = '学籍番号' 
PASSWORD = '誕生日'
driver = webdriver.Chrome()   
driver.get('http://kyomu.komagome.ed.jp/port/login.php') 
time.sleep(0)
id = driver.find_element(By.XPATH, '//*[@id="UsrCode"]').send_keys(学籍番号) 
pwd = driver.find_element(By.XPATH,'//*[@id="PasCode"]').send_keys(誕生日)  
login = driver.find_element(By.XPATH, '//*[@id="form1"]/div[3]/table/tbody/tr[3]/td/input') 
login.click()
time.sleep(0.1)

question1 = driver.find_element(By.XPATH,'//*[@id="form1"]/div[4]/div[4]/input').click()
question2 = driver.find_element(By.XPATH,'//*[@id="form1"]/div[4]/div[9]/input').click()
question3 = driver.find_element(By.XPATH,'//*[@id="form1"]/div[4]/div[19]/input').click()
question4 = driver.find_element(By.XPATH,'//*[@id="form1"]/div[4]/div[24]/input').click()
time.sleep(0)

answer = driver.find_element(By.XPATH, '//*[@id="form1"]/div[4]/div[27]/table/tbody/tr/td[2]/input') 
answer.click()
time.sleep(2)
