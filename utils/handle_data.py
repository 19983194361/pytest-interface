import openpyxl
from utils.paths import DATA_DIR


class GetCaseData:
    """用例数据处理类"""

    def get(self, file=None, sheet=None):
        """
        根据传入不同的file参数，返回相应的数据处理结果
        :param file: 数据文件名
        :param sheet: sheet表名
        :return: 处理后的数据
        """
        if file.endswith('.xlsx'):
            file_path = DATA_DIR + '\\excel\\' + file
            return self.get_excel_data(filename=file_path, sheetname=sheet)
        elif file.endswith('.py'):
            file_path = DATA_DIR + '\\python\\' + file
            return self.get_python_data(filename=file_path)
        elif file.endswith('.txt'):
            file_path = DATA_DIR + '\\txt\\' + file
            return self.get_txt_data(filename=file_path)

    def get_excel_data(self, filename=None, sheetname=None):
        """
        读取excel用例数据，并处理返回
        :param filename: 管理用例数据的excel路径文件名
        :param sheetname: 表名
        :return: 处理后的数据
        """
        excel_obj = openpyxl.load_workbook(filename=filename)
        sheet_obj = excel_obj[sheetname]
        data_set = list(sheet_obj.rows)

        keys = [key.value for key in data_set[0]]

        data = {'normal': [], 'except': []}
        for line in data_set[1:]:
            item = dict(zip(keys, [value.value for value in line]))
            data['normal'].append(item) if item['type'] == 'normal' else data['except'].append(item)
        return data

    def get_python_data(self, filename=None):
        """
        读取python用例数据集并返回
        :param filename: 数据保存python文件名称
        :return: 用例数据集
        """
        str_datas = ''
        with open(file=filename, mode='r', encoding='utf-8') as f:
            for line in f.readlines():
                str_datas += line
            data_set = eval(str_datas)

        data = {'normal': [], 'except': []}
        for values in data_set[1:]:
            item = dict(zip(data_set[0], values))
            data['normal'].append(item) if item['type'] == 'normal' else data['except'].append(item)
        return data

    def get_txt_data(self, filename=None):
        """
        读取txt用例数据集并返回
        :param filename: 数据保存txt文件名称
        :return: 用例数据集
        """
        with open(file=filename, mode='r', encoding='utf-8') as f:
            contents = f.readlines()
        keys = eval(contents[0])

        data = {'normal': [], 'except': []}
        for values in contents[1:]:
            item = dict(zip(keys, eval(values)))
            data['normal'].append(item) if item['type'] == 'normal' else data['except'].append(item)
        return data


data_obj = GetCaseData()
