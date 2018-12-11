# -*- coding: utf-8 -*-
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep
sys.path.append('../Public/')
sys.path.append('../webApi/')
sys.path.append('../common/')
from logger import Log
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from public import ParametrizedTestCase
from yonghuzuxinxiguanli_element import chaxun_element,new_usergroupinfo



class UserGroup(ParametrizedTestCase):
    """用户组信息管理"""

    def test_a_new_usergroup(self):
        """新建用户组"""
        try:
            driver=self.param
            driver.switch_to_frame("iframeId")
            driver.find_element(*new_usergroupinfo()[0]).click()#button_new
            driver.find_element(*new_usergroupinfo()[1]).click()#input_park
            driver.find_element(*new_usergroupinfo()[1]).send_keys("151")#input_park
            driver.find_element(*new_usergroupinfo()[2]).click()
            driver.find_element(*new_usergroupinfo()[3]).send_keys("Automation_test07")
            driver.find_element(*new_usergroupinfo()[4]).send_keys("Automation_test07")
            driver.find_element(*new_usergroupinfo()[5]).click()
            #driver.implicitly_wait(20)
            sleep(20)
            driver.get_screenshot_as_file('../images/添加结果截图.png')
        except NoSuchElementException as e:
            Log().error(e)
            raise(e)
        finally:
            driver.switch_to.default_content()
            #driver.implicitly_wait(3)
            sleep(3)

    def test_b_browser(self):
        """查询用户组信息,查询用户组名为2018071801的信息"""
        
        try:
            driver=self.param
            driver.switch_to_frame("iframeId")
            driver.find_element(*chaxun_element()[0]).send_keys("2018071801")
            Log().info("输入查询的用户组名称2018071801")
            driver.find_element(*chaxun_element()[1]).click()
            driver.get_screenshot_as_file('../images/查询结果.png')
            groupname=driver.find_element(*chaxun_element()[2]).text
            driver.implicitly_wait(3)
            self.assertEqual(u'海澜中苑停车场',groupname)
            Log().info("查询到2018071801的停车场是海澜中苑停车场")

        except AssertionError as e:
            Log().error(e)
            raise(e)
        finally:
            driver.switch_to.default_content()
            driver.implicitly_wait(3)

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True