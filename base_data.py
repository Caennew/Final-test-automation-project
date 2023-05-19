from selenium.webdriver.common.by import By
from urllib.parse import urlparse


class BaseForm(object):
    def __init__(self, driver, url, timeout=5):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

    def get_base_url(self):
        url = urlparse(self.driver.current_url)
        return url.hostname


class AuthForm(BaseForm):
    def __init__(self, driver, timeout=5):
        super().__init__(driver, timeout)
        url = 'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c' \
              '&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid& '
