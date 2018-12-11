#test.py
from selenium import webdriver
from time import sleep
import sys,time
from HTMLTestRunner import HTMLTestRunner
import unittest
sys.path.append('../Public/')
from public import Login,ParametrizedTestCase
import testsuit



if __name__ == '__main__':
	#driver=webdriver.Firefox()
	driver=webdriver.Chrome()
	driver.maximize_window()
	driver.implicitly_wait(10)
	driver.get("http://prep.tingjiandan.com/bmp-web/login")
	suite=testsuit.suite(driver)

	now = time.strftime("%Y-%m-%d %H_%M_%S")
	filename = '../report/' + now + '_result.html'
	fp = open(filename, 'wb')
	#生成报告
	runner = HTMLTestRunner(stream=fp,
							title='集团管理自动化测试',  #报告title
							description='运行环境：MySQL(PyMySQL), Requests, unittest，selenium ')



	#调用登录，执行一次
	Login().user_login(driver)
	sleep(3)
	#打开集团管理，执行一次
	Login().OpenGroupManage(driver)
	sleep(3)
	#运行测试用例
	runner.run(suite)
	fp.close()

	#退出登录，执行一次
	'''
	Login().user_loginout(driver)'''
	driver.quit()