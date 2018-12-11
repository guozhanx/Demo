from selenium.webdriver.common.by import By

def new_usergroupinfo():
	button_new=(By.XPATH,"html/body/div[1]/div[2]/div/span")
	input_park=(By.XPATH,".//*[@id='content']/article/div[1]/div[2]/form/div[1]/div[1]/div/div/div/div[1]/input")
	select_park=(By.XPATH,".//*[@id='content']/article/div[1]/div[2]/form/div[1]/div[1]/div/div/div/div[2]/ul[2]/li[10]")
	input_usergroupname=(By.XPATH,".//*[@id='content']/article/div[1]/div[2]/form/div[1]/div[2]/div/div/div/input")
	input_usergrouName_dec=(By.XPATH,".//*[@id='content']/article/div[1]/div[2]/form/div[2]/div/div/div/div/textarea")
	button_seru=(By.XPATH,".//*[@id='userGroupSubmit']")
	return(button_new,input_park,select_park,input_usergroupname,input_usergrouName_dec,button_seru)


def chaxun_element():
	input_usergroupsname=(By.XPATH,"html/body/div[1]/div[1]/div[2]/div/input")
	button_chaxun=(By.XPATH,"html/body/div[1]/div[1]/div[6]/button")
	text=(By.XPATH,"html/body/div[1]/div[3]/div/table/tr[2]/td[3]")
	return(input_usergroupsname,button_chaxun,text)


