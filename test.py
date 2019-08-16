from selenium import webdriver


print('\n WELCOME \n created by DIbyajitDj \n\n You can Send WhatsApp Messages from CMD' )


def menu():
	print("\n Enter Your Choice for operation in WhatsApp \n 1.Message Bomb \n 2.Normal Message")
	choice=input()

	if choice=="1":
		driver = webdriver.Firefox()
		driver.get("https://web.whatsapp.com/")

		input("Enter any thing after Scanning the code")

		rcpt=input("Enter the name of the recepient")
		msg=input("Enter the message")
		no=int(input("Enter no of times"))

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


	else:

		driver = webdriver.Firefox()
		driver.get("https://web.whatsapp.com/")

		input("Enter any thing after Scanning the code")

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














menu()


