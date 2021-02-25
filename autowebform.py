# autowebform.py

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driverpath = r'C:\Users\prat_\Desktop\Python Bootcamp\RPA EP3\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(driverpath)


url = 'http://uncle-machine.com/login/'

driver.get(url)


username = driver.find_element_by_id('username')
username.send_keys('PND69@gmail.com')

password = driver.find_element_by_id('password')
password.send_keys('12345678')
password.send_keys(Keys.RETURN) # พิม password เสร็จ กด enter

#button = driver.find_element_by_xpath('/html/body/div[2]/form/button')
#button.click() # กด enter เพื่อ login

addurl = 'http://uncle-machine.com/addproduct/'

driver.get(addurl) # 

pdname = driver.find_element_by_id('name')
pdprice = driver.find_element_by_id('price')
pddetail = driver.find_element_by_id('detail')

pd1_name = 'Lufi'
pd1_price = '300000000'
pd1_detail = '''เป็นตัวละครจากการ์ตูนญี่ปุ่นเรื่อง วันพีซ และถือว่าเป็นตัวละครเอกของเรื่อง 
เรื่องราวของวันพีซได้เริ่มต้นขึ้นเมื่อลูฟี่เดินทางออกทะเล เพื่อรวบรวมพวกพ้อง 
ทั้งกลุ่มโจรสลัด และเดินทางผจญภัยสุดขอบโลกเพื่อตามสมบัติที่มีอยู่ชิ้นเดียวในโลกที่เรียกว่า "วันพีซ" (One Piece) ที่เมื่อได้ครอบครองจะได้เป็นราชาโจรสลัด 
ซึ่งลูฟี่มีความฝันสูงสุดคือเป็นราชาโจรสลัด ตามรอยราชาโจรสลัด โกล ดี. โรเจอร์
'''

pdname.send_keys(pd1_name)
pdprice.send_keys(pd1_price)
pddetail.send_keys(pd1_detail)

button = driver.find_element_by_xpath('/html/body/div[2]/form/button')
button.click()

# button = driver.find_element_by_class_name('btn btn-primary')
