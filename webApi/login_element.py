from selenium.webdriver.common.by import By
import sys

class Login_Element(object):
    #定位器，通过元素属性定位元素对象
	def __init__(self):
		self.username_loc =(By.NAME,'login')
		self.password_loc =(By.NAME,'password')
		self.submit_loc =(By.ID,'submit')
		self.one=(By.XPATH,"//div[@id='app']/div[4]/header/nav/ul/li[4]")
		self.two=(By.XPATH,"//div[@id='app']/div[4]/div/section/nav/ul/li[5]/p")
		self.three=(By.XPATH,".//*[@id='app']/div[4]/div/section[1]/nav/ul/li[5]/ul/li[1]")
		self.text=(By.XPATH,"html/body/div[1]/div[3]/div/table/tr[1]/td[1]")
		self.Loginout=(By.XPATH,".//*[@id='app']/div[4]/header/ul/li/span[2]")
		self.menu=(By.XPATH,".//*[@id='app']/div[4]/header/ul/li/div/p[2]/a")
		self.Loginout_sure=(By.CSS_SELECTOR,(".logout"))