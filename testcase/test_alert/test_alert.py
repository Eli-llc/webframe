import allure
import pytest
from pages.IndexPage import IndexPage
from common.page_manage import pm
from pages.LoginPage import LoginPage
from time import sleep
from pages.alert_work.event_page import EventPage

@pytest.fixture(scope="module")
def sign_in(login_as):
    page = login_as("admin", "admin123")
    page.click_platform("指标解析中心")
    yield page

class TestAlert:
    def test_alert(self, sign_in):
        page.
