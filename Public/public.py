#公共模块，登录和退出
import sys
sys.path.append('../common')
sys.path.append('../webApi')
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import unittest
import datetime
from logger import Log
from selenium.webdriver.common.by import By
from login_element import Login_Element
nowTime=datetime.datetime.now().strftime('%Y-%m-%d:%H:%M:%S')


class Login(unittest.TestCase,Login_Element):
	"""初始化element"""
	def __init__(self):
		Login_Element.__init__(self)

	def user_login(self, driver):
		"""登录网站"""
		try:
			#清空用户名输入框
			driver.find_element(*self.username_loc).clear()
			#输入用户名
			driver.find_element(*self.username_loc).send_keys("admin")
			#清空密码输入框
			driver.find_element(*self.password_loc).clear()
			#输入密码
			driver.find_element(*self.password_loc).send_keys("Tjd123456")
			#点击登录按钮
			driver.find_element(*self.submit_loc).click()
			sleep(5)
			#判断是否登录成功
			if driver.title=="停车场智能管理平台":
				Log().info("登录成功！")

			else:
				Log().info("登录失败！")
		except Exception as e:
			Log().error(e)
			raise(e)


	def OpenGroupManage(self,driver):
		"""打开集团管理"""
		try:
			driver.find_element(*self.one).click()
			driver.find_element(*self.two).click()
			driver.find_element(*self.three).click()
			driver.switch_to_frame("iframeId")
			text=driver.find_element(*self.text).text
			if text=="编号":
				Log().info("打开集团管理成功！")
			else:
				Log().info("打开集团管理失败！")
			driver.switch_to.default_content()
			
		except Exception as e:
			Log().error(e)
			raise(e)

		

	def user_loginout(self,driver):
		"""退出登录"""
		try:
			Loginout = driver.find_element(*self.Loginout) 
			driver.implicitly_wait(5)
			ActionChains(driver).move_to_element(Loginout).perform()
			driver.implicitly_wait(3)
			menu = driver.find_element(*self.menu)
			menu.click()
			driver.find_element(*self.Loginout_sure).click
			"""关闭浏览器"""
			driver.quit()
		except Exception as e:
			print(e)

"""重写unittest，使之可以接受driver，完成一次登陆，运行多用例，然后退出"""
class ParametrizedTestCase(unittest.TestCase):

	def __init__(self, methodName='runTest', param=None):
		super(ParametrizedTestCase, self).__init__(methodName)
		self.param = param
	@staticmethod
	def parametrize(testcase_klass, param=None):
		testloader = unittest.TestLoader()
		testnames = testloader.getTestCaseNames(testcase_klass)
		suite = unittest.TestSuite()
		for name in testnames:
			suite.addTest(testcase_klass(name, param=param))
		return suite

		
