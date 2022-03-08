import pytest
from base.project_path import test_data_path
from page.index import SearchPage
from page.login import LoginPage
from base.utils import load_yaml, get_driver, close_driver


class TestSearch:
    def setup_class(self):
        self.driver = get_driver()
        self.lp = LoginPage(self.driver)
        self.sp = SearchPage(self.driver)
        self.lp.login(**load_yaml(test_data_path + '/login_success.yaml')[0])

    def teardown_class(self):
        close_driver(self.driver)

    @pytest.mark.parametrize('txt', load_yaml(test_data_path + '/search.yaml'))
    def test_search(self, txt):
        self.sp.search(**txt)


if __name__ == '__main__':
    pytest.main(['-s', 'test02_search.py'])
