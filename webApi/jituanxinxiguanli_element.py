from selenium.webdriver.common.by import By

def open_element():
	groupInfoManage=(By.XPATH,".//*[@id='app']/div[4]/div/section[1]/nav/ul/li[5]/ul/li[2]")
	groupName=(By.XPATH,"html/body/div[1]/div[3]/div/table/tr[1]/td[2]")
	return(groupInfoManage,groupName)

def new_group():
	button_addnewgroup=(By.XPATH,"html/body/div[1]/div[2]/div/span")
	input_groupname=(By.XPATH,".//*[@id='content']/article/div[1]/div[2]/form/div[1]/div[1]/div/div/div/input")
	input_Phone=(By.XPATH,".//*[@id='content']/article/div[1]/div[2]/form/div[1]/div[2]/div/div/div/input")
	input_Email=(By.XPATH,".//*[@id='content']/article/div[1]/div[2]/form/div[2]/div[1]/div/div/div/input")
	input_other=(By.XPATH,".//*[@id='content']/article/div[1]/div[2]/form/div[3]/div/div/div/div/textarea")
	button_sure=(By.XPATH,".//*[@id='groupSubmit']")
	return(button_addnewgroup,input_groupname,input_Phone,input_Email,input_other,button_sure)

def chaxun_new_group():
	new_groupname=(By.XPATH,"html/body/div[1]/div[1]/div[2]/div/input")
	button_chaxun=(By.XPATH,"html/body/div[1]/div[1]/div[3]/button")
	assert_text=(By.XPATH,"html/body/div[1]/div[3]/div/table/tr[2]/td[2]")
	assert_phone=(By.XPATH,"html/body/div[1]/div[3]/div/table/tr[2]/td[3]")
	return(new_groupname,button_chaxun,assert_text,assert_phone)
