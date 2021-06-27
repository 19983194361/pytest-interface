from jsonpath import jsonpath


class HandleAssert:

    def validate(self, expect=None, actual=None, name=None):
        """
        断言方法
        :param expect: 期望结果的字典
        :param actual:实际结果的字典
        :return: None
        """
        try:
            for t, options in expect.items():
                if t == 'equal':
                    for key, value in options.items():
                        assert value == jsonpath(obj=actual, expr='$..{}'.format(key))[0]
                elif t == 'in':
                    for key, value in options.items():
                        assert value in jsonpath(obj=actual, expr='$..{}'.format(key))[0]
        except Exception as e:
            raise e


assert_obj = HandleAssert()
