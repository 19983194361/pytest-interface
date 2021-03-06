import traceback
from jsonpath import jsonpath
from utils.handle_log import logger


class HandleAssert:

    def validate(self, expect=None, actual=None, name=None):
        """
        断言方法
        :param expect: 期望结果的字典
        :param actual:实际结果的字典
        :return: None
        """
        try:
            logger.info('[{}]->正在断言，请稍等...'.format(name))
            for t, options in expect.items():
                if t == 'equal':
                    for key, value in options.items():
                        assert value == jsonpath(obj=actual, expr='$..{}'.format(key))[0]
                elif t == 'in':
                    for key, value in options.items():
                        assert value in jsonpath(obj=actual, expr='$..{}'.format(key))[0]
            logger.info('[{}]->断言完毕，用例执行成功！'.format(name))
        except Exception as e:
            logger.error('[{}]->断言完毕，出现异常！\n{}'.format(name, traceback.format_exc()))
            raise e


assert_obj = HandleAssert()
