import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLogin:
    # pytest前置操作
    def setup_class(self):               #这里是类级的，因为类级的只会执行一次
    #     打开浏览器，和基本设置一样
        self.driver = webdriver.Chrome()
        self.driver.get('')
        self.driver.maximize_window()  # 窗口最大化
        self.driver.implicitly_wait(10)  # 隐式等待，全局

    # 后置操作
    def teardown_class(self):          #这里必须用类级别，后面会跑不了
        self.driver.quit()

    @pytest.mark.parametrize('username,password,result',[
        ('user1','password1','断言：欢迎你，test123456'),
        ('user2','password2','用户名错误'),
        ('user3','password3','密码错误')
    ],ids=
                             'test_login_01'
                             'test_login_02'
                             'test_login_03'
                             )        #修改用例标题

    def test_login(self,username,password,result):
        # 下面四个可以优化
        # driver = webdriver.Chrome()
        # driver.get('')
        # driver.maximize_window()  # 窗口最大化
        # driver.implicitly_wait(10)  # 隐式等待，全局

        self.driver.find_element(By.XPATH,'').click()    #点击注册按钮
        self.driver.find_element(By.XPATH,'').send_keys('')  #输入用户名
        self.driver.find_element(By.XPATH,'').send_keys('')  #输入密码
        self.driver.find_element(By.XPATH,'').click()   #点击登录按钮
        self.driver.find_element(By.XPATH,'').click()   #点击退出按钮
        time.sleep(2)

        if '欢迎你' in result:
            text = self.driver.find_element(By.XPATH, '').text  # 查找测试结果
            print(text)  # 打印测试结果
            assert text == result    #断言：判断是否与预期结果相符
        elif '用户名错误' in result:
            text = self.driver.find_element(By.XPATH, '').text
            print(text)
            assert text == result

    # 已优化下面三条测试用例
    # def test_login_02(self):
    #     # driver = webdriver.Chrome()
    #     # driver.get('')
    #     # driver.maximize_window()  # 窗口最大化
    #     # driver.implicitly_wait(10)  # 隐式等待，全局
    #     self.driver.find_element(By.XPATH,'').click()    #点击注册按钮
    #     self.driver.find_element(By.XPATH,'').send_keys('')  #输入用户名
    #     self.driver.find_element(By.XPATH,'').send_keys('')  #输入密码
    #     self.driver.find_element(By.XPATH,'').click()   #点击登录按钮
    #     self.driver.find_element(By.XPATH, '').click()  # 点击退出按钮
    #     time.sleep(2)
    #     text = self.driver.find_element(By.XPATH, '').text  # 查找测试结果
    #     print(text)  # 打印测试结果
    #     assert text=='用户名错误'  #断言：判断是否与预期结果相符
    #
    # def test_login_03(self):
    #     # driver = webdriver.Chrome()
    #     # driver.get('')
    #     # self.driver.maximize_window()  # 窗口最大化
    #     # driver.implicitly_wait(10)  # 隐式等待，全局
    #     self.driver.find_element(By.XPATH,'').click()    #点击注册按钮
    #     self.driver.find_element(By.XPATH,'').send_keys('')  #输入用户名
    #     self.driver.find_element(By.XPATH,'').send_keys('')  #输入密码
    #     self.driver.find_element(By.XPATH,'').click()   #点击登录按钮
    #     self.driver.find_element(By.XPATH, '').click()  # 点击退出按钮
    #     time.sleep(2)
    #     text = self.driver.find_element(By.XPATH, '').text  # 查找测试结果
    #     print(text)  # 打印测试结果
    #     # assert == ''    #断言：判断是否与预期结果相符
    #
    # def test_login_04(self):
    #     # driver = webdriver.Chrome()
    #     # driver.get('')
    #     # driver.maximize_window()  # 窗口最大化
    #     # driver.implicitly_wait(10)  # 隐式等待，全局
    #     self.driver.find_element(By.XPATH,'').click()    #点击注册按钮
    #     self.driver.find_element(By.XPATH,'').send_keys('')  #输入用户名
    #     self.driver.find_element(By.XPATH,'').send_keys('')  #输入密码
    #     self.driver.find_element(By.XPATH,'').click()   #点击登录按钮
    #     self.driver.find_element(By.XPATH, '').click()  # 点击退出按钮
    #     time.sleep(2)
    #     text = self.driver.find_element(By.XPATH, '').text  # 查找测试结果
    #     print(text)  # 打印测试结果
    #     # assert == ''    #断言：判断是否与预期结果相符

# 上面的代码可以优化
# 利用参数化，将test_login_01等进行优化，参数化

