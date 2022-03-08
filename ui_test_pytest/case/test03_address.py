import pytest
from base.project_path import test_data_path
from page.login import LoginPage
from base.utils import load_yaml, get_driver, close_driver
from page.personal import AddressPage


class TestAddress:
    def setup_class(self):
        self.driver = get_driver()
        self.lp = LoginPage(self.driver)
        self.ap = AddressPage(self.driver)
        self.lp.login(**load_yaml(test_data_path + '/login_success.yaml')[0])

    def teardown_class(self):
        close_driver(self.driver)

    @pytest.mark.parametrize('data', load_yaml(test_data_path + '/test_address.yaml'))
    def test_address(self, data):
        self.ap.test_update_address(**data)


if __name__ == '__main__':
    pytest.main(['-s', 'test03_address.py'])
