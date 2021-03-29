from time import sleep

import allure
import pytest



@allure.feature("测试登陆页")
class TestLogin:
    """
    测试登录功能
    """
    def test_login(self, login_as):
        page = login_as("JMeter", "123456")
        assert "告警辨析中心" in page.title