from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://web.whatsapp.com/")


rcpt=input("Enter the name of the recepient")
msg=input("Enter the message")
no=int(input("Enter no of times"))

input("Enter any thing after Scanning the code")

sch=driver.find_element_by_class_name('_2zCfw')
sch.send_keys(rcpt)

press=driver.find_element_by_class_name('_2UaNq')
press.click()

elem = driver.find_element_by_xpath('//span[@title = "{}"]'.format(rcpt))
elem.click()

box=driver.find_element_by_class_name('_3u328')

for i in range(no):
	box.send_keys(msg)
	clik=driver.find_element_by_class_name('_3M-N-')
	clik.click()
