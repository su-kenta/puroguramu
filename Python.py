from selenium.webdriver.common.by import By 
from selenium import webdriver 
import time 

 #ログイン時に必要な情報
USERID = '学籍番号' 
PASSWORD = '誕生日'

#Chromeを開くように指定
driver = webdriver.Chrome()   

#健康アンケート先を指定
driver.get('http://example.ed.jp/port/login.php') 

#待ち時間を0にする
time.sleep(0)
#ログイン情報入力
id = driver.find_element(By.XPATH, '//*[@id="UsrCode"]').send_keys(学籍番号) 
pwd = driver.find_element(By.XPATH,'//*[@id="PasCode"]').send_keys(誕生日)  
login = driver.find_element(By.XPATH, '//*[@id="form1"]/div[3]/table/tbody/tr[3]/td/input') 
login.click()

#ロード時間を0.1秒に設定
time.sleep(0.1)

#1個目の質問を選択しクリック
question1 = driver.find_element(By.XPATH,'//*[@id="form1"]/div[4]/div[4]/input').click()

#2個目の質問を選択しクリック
question2 = driver.find_element(By.XPATH,'//*[@id="form1"]/div[4]/div[9]/input').click()

#3個目の質問を選択しクリック
question3 = driver.find_element(By.XPATH,'//*[@id="form1"]/div[4]/div[19]/input').click()

#4個目の質問を選択しクリック
question4 = driver.find_element(By.XPATH,'//*[@id="form1"]/div[4]/div[24]/input').click()
time.sleep(0)

#アンケートを送信
answer = driver.find_element(By.XPATH, '//*[@id="form1"]/div[4]/div[27]/table/tbody/tr/td[2]/input') 
answer.click()
time.sleep(2)
