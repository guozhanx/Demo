"""
集团信息管理-用户组信息管理-新建用户组：用户组名称和描述的参数
"""
import random
def test_data():
	randomdata = range(99,999)
	randomlist = random.sample(randomdata,1)
	str1="AutoTest_"
	return(str1+str(randomlist))
