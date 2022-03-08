import pytest
from base.project_path import test_data_path
from page.login import LoginPage
from base.utils import load_yaml, get_driver, close_driver


class TestLogin:
    def setup_class(self):
        self.driver = get_driver()
        self.lp = LoginPage(self.driver)

    def teardown_class(self):
        close_driver(self.driver)

    @pytest.mark.parametrize('data', load_yaml(test_data_path + '/login.yaml'))
    def test_login(self, data):
        self.lp.login(**data)


if __name__ == '__main__':
    pytest.main(['-s', 'test01_login.py'])
