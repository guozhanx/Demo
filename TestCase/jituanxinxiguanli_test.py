
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
sys.path.append('../Public/')
sys.path.append('../webApi/')
sys.path.append('../common/')
import time,re
from public import ParametrizedTestCase
from logger import Log
from jituanxinxiguanli_element import open_element,new_group,chaxun_new_group
class GroupInfo(ParametrizedTestCase):
    """集团信息管理"""

    def test_a_openpage(self):
        """打开集团信息管理页面"""
        try:
            driver=self.param
            driver.find_element(*open_element()[0]).click()
            driver.switch_to_frame("iframeId")
            groupname=driver.find_element(*open_element()[1]).text
            self.assertEqual(u'集团名称',groupname)
            Log().info("打开集团信息管理页面成功")
        except AssertionError as e:
            Log().info("打开集团信息管理页面失败")
            Log().error(e)
            raise(e)
        finally:
            driver.switch_to.default_content()

    def test_b_addgroup(self):
        """新建集团"""                              
        try:
            driver=self.param
            driver.switch_to_frame("iframeId")
            #点击新建集团按钮
            driver.find_element(*new_group()[0]).click()
            #输入集团名称
            driver.find_element(*new_group()[1]).send_keys("AutoTesting_01")
            #输入联系人手机号
            driver.find_element(*new_group()[2]).send_keys("18512302010")
            #输入联系人邮箱
            driver.find_element(*new_group()[3]).send_keys("123@qq.com")
            #输入集团描述
            driver.find_element(*new_group()[4]).send_keys("AutoTestCase_01")
            #确认添加
            driver.find_element(*new_group()[5]).click()
            driver.get_screenshot_as_file('../images/添加结果.png')
            time.sleep(10)
            #Login().cutimages(driver)
        except NoSuchElementException as e:
            raise(e)
        finally:
            driver.switch_to.default_content()

    def test_c_browsergroup(self):
        """查询新建的集团"""
        try:
            driver=self.param
            driver.switch_to_frame("iframeId")
            #输入集团名称
            driver.find_element(*chaxun_new_group()[0]).send_keys("AutoTesting_01")
            #点击查询
            driver.find_element(*chaxun_new_group()[1]).click()
            groupname=driver.find_element(*chaxun_new_group()[2]).text
            self.assertEqual(u'AutoTesting_01',groupname)
            phone=driver.find_element(*chaxun_new_group()[3]).text
            self.assertEqual('18512302010',phone)
            time.sleep(10)
            #Login().cutimages(driver)
        except AssertionError as e:
            raise(e)
        finally:
            driver.switch_to.default_content()