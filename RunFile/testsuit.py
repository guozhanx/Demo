import sys
sys.path.append('../Public/')
sys.path.append('../TestCase/')
from user_group_info_browser_test import UserGroup
from jituanxinxiguanli_test import GroupInfo
from public import ParametrizedTestCase
import unittest

"""构造测试集"""
def suite(driver):
	suite = unittest.TestSuite()
	suite.addTest(ParametrizedTestCase.parametrize(UserGroup, param=driver))
	suite.addTest(ParametrizedTestCase.parametrize(GroupInfo, param=driver))
	return(suite)