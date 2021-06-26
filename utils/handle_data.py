import openpyxl
from utils.paths import DATA_DIR


class HandleData:
    """用例数据处理类"""

    def get(self, file=None, sheet=None):
        """
        根据传入不同的file参数，返回相应的数据处理结果
        :param file: 数据文件名
        :param sheet: sheet表名
        :return: 处理后的数据
        """
        if file.endswith('.xlsx'):
            file_path = DATA_DIR + '\\' + file
            print(self.get_excel_data(filename=file_path, sheetname=sheet))

    def get_excel_data(self, filename=None, sheetname=None):
        """
        读取excel用例数据，并处理返回
        :param filename: 管理用例数据的excel路径文件名
        :param sheetname: 表名
        :return: 处理后的数据
        """
        pass


a = HandleData()
a.get('platform.xlsx', sheet='login')
