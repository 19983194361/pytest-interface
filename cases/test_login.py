import pytest
from utils.handle_data import data_obj
from utils.handle_request import send
from utils.handle_assert import assert_obj
from utils.handle_log import logger


class TestLogin:
    """登录用例逻辑"""

    # 获取用例数据集
    # cases = data_obj.get(file='platform.xlsx', sheet='login')
    # cases = data_obj.get(file='login.py')
    # cases = data_obj.get(file='login.txt')
    cases = data_obj.get(file='login.yaml')

    @pytest.mark.parametrize('case', cases['normal'])
    def test_login_success(self, case):
        """
        登录成功
        :param case: 用例数据
        :return: None
        """
        name = case['name']
        try:
            logger.info('[{}]->开始执行用例！'.format(name))
            response = send(case=case)
            logger.info('[{}]->请求成功！'.format(name))
        except Exception as e:
            logger.error('[{}]->请求失败！\n{}'.format(name, e))
            raise e

        assert_obj.validate(expect=eval(case['expect']), actual=response, name=name)

    @pytest.mark.parametrize('case', cases['except'])
    def test_login_fail(self, case):
        """
        登录失败
        :param case: 用例数据
        :return: None
        """
        name = case['name']
        try:
            logger.info('[{}]->开始执行用例！'.format(name))
            response = send(case=case)
            logger.info('[{}]->请求成功！'.format(name))
        except Exception as e:
            logger.error('[{}]->请求失败！\n{}'.format(name, e))
            raise e

        assert_obj.validate(expect=eval(case['expect']), actual=response, name=name)
