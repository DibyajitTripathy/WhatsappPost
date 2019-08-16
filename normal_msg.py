from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://web.whatsapp.com/")

input("Enter any thing after Scanning the code")

while True:

	print("Choose \n 1.Keep Logged In \n 2.Leave")
	choice = input()

	if choice=="1":
		
		rcpt=input("Enter the name of the recepient")
		msg=input("Enter the message")

		sch=driver.find_element_by_class_name('_2zCfw')
		sch.send_keys(rcpt)

		press=driver.find_element_by_class_name('_2UaNq')
		press.click()

		elem = driver.find_element_by_xpath('//span[@title = "{}"]'.format(rcpt))
		elem.click()

		box=driver.find_element_by_class_name('_3u328')

		box.send_keys(msg)
		clik=driver.find_element_by_class_name('_3M-N-')
		clik.click()

	if(choice=="2"):
		break

driver.quit()












