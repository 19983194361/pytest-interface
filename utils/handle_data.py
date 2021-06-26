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


data_obj = GetCaseData()