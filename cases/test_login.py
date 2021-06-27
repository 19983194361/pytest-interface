import pytest
from utils.handle_data import data_obj
from utils.handle_request import send
from utils.handle_assert import assert_obj


class TestLogin:
    """登录用例逻辑"""

    # 获取用例数据集
    cases = data_obj.get(file='platform.xlsx', sheet='login')

    @pytest.mark.parametrize('case', cases['normal'])
    def test_login_success(self, case):
        """
        登录成功
        :param case: 用例数据
        :return: None
        """
        name = case['name']
        try:
            response = send(case=case)
        except Exception as e:
            raise e

        assert_obj.validate(expect=eval(case['except']), actual=response, name=name)

    @pytest.mark.parametrize('case', cases['except'])
    def test_login_fail(self, case):
        """
        登录失败
        :param case: 用例数据
        :return: None
        """
        name = case['name']
        try:
            response = send(case=case)
        except Exception as e:
            raise e

        assert_obj.validate(expect=eval(case['except']), actual=response, name=name)
