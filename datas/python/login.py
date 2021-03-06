[
    ['id', 'type', 'name', 'method', 'path', 'headers', 'param', 'data', 'json', 'expect'],
    [1, 'normal', '用户名和密码正确', 'POST', 'user/login/', "{'Content-Type': 'application/json'}", None, None,
     "{'username': 'admin', 'password': '123456'}", "{'equal': {'code': 0, 'username': 'admin'}}"],
    [2, 'except', '不传用户名字段', 'POST', 'user/login/', "{'Content-Type': 'application/json'}", None, None,
     "{'password': '123456'}", "{'equal': {'code': 1}, 'in': {'username': '该字段是必填项。'}}"],
    [3, 'except', '不传密码字段', 'POST', 'user/login/', "{'Content-Type': 'application/json'}", None, None,
     "{'username': 'admin'}", "{'equal': {'code': 1}, 'in': {'password': '该字段是必填项。'}}"],
    [4, 'except', '用户名为空', 'POST', 'user/login/', "{'Content-Type': 'application/json'}", None, None,
     "{'username': '', 'password': '123456'}", "{'equal': {'code': 1}, 'in': {'username': '该字段不能为空。'}}"],
    [5, 'except', '密码为空', 'POST', 'user/login/', "{'Content-Type': 'application/json'}", None, None,
     "{'username': 'admin', 'password': ''}", "{'equal': {'code': 1}, 'in': {'password': '该字段不能为空。'}}"],
    [6, 'except', '用户名错误', 'POST', 'user/login/', "{'Content-Type': 'application/json'}", None, None,
     "{'username': 'ad123', 'password': '123456'}", "{'equal': {'code': 1}, 'in': {'username': '账号不存在！'}}"],
    [7, 'except', '密码错误', 'POST', 'user/login/', "{'Content-Type': 'application/json'}", None, None,
     "{'username': 'admin', 'password': '666666'}", "{'equal': {'code': 1}, 'in': {'password': '密码错误！'}}"]
]
