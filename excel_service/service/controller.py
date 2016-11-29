
"""
    脚本启动控制器
"""
import csv
import xlrd

class Excel:
    """
    excel 相关操作封装
    """
    def __init__(self, path='../files/week_201631.csv'):
        """
            初始化工具类
        """
        self.path = path

    @staticmethod
    def show_excel(path="../files/AUM.xlsm", odd=None):
        """
            查看指定的excel文件
        :return:
        """
        work = xlrd.open_workbook(path)
        work_sheet = work.sheet_by_name('明细')
        rows = work_sheet.nrows     # show sheet all rows

        result = []
        for raw in range(1, rows):
            raw_data = work_sheet.row_values(raw)
            if raw_data[1] == odd:
                result.append([raw_data[1], raw_data[4], raw_data[6], str(raw_data[7]),
                               str(raw_data[8]), "%.2f%%" %(raw_data[10] * 100), str(raw_data[13]),
                               str(raw_data[15]), str(raw_data[16]), ])
                return result[0]

    def show_csv_odd(self, odd):
        """
            查看指定的csv的odd行信息
        :return:
        """
        if odd:
            with open(self.path, encoding='utf-8') as csv_file:
                read = csv.reader(csv_file)
                for line in read:
                    if eval(str(line).replace('\\t', ''))[1] == odd:
                        return eval(str(line).replace('\\t', ''))
        return "odd is none type"

if __name__ == '__main__':
    EXCEL = Excel()
    print(sorted(EXCEL.show_excel(odd='796200765922161')))
    print(sorted(EXCEL.show_csv_odd('796200765922161')))
