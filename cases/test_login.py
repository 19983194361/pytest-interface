import pytest
import requests
from utils.handle_data import data_obj
from utils.handle_request import send


class TestLogin:
    """登录用例逻辑"""

    # 获取用例数据集
    cases = data_obj.get(file='platform.xlsx', sheet='login')

    @pytest.mark.skip
    @pytest.mark.parametrize('case', cases['normal'])
    def test_login_success(self, case):
        """
        登录成功
        :param case: 用例数据
        :return: None
        """
        response = send(case=case)
        print(case['name'])

    @pytest.mark.parametrize('case', cases['except'])
    def test_login_fail(self, case):
        """
        登录失败
        :param case: 用例数据
        :return: None
        """
        print(case['name'])
