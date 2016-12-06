
"""
    脚本启动控制器
"""
import csv
import xlrd

class Excel:
    """
    excel 相关操作封装
    """
    def __init__(self, csv_path='files/week_201631.csv', excel_path='files/AUM.xlsm'):
        """
            初始化工具类
        """
        self.excel_path = excel_path
        self.csv_path = csv_path
        self.work = xlrd.open_workbook(self.excel_path)
        self.work_sheet = self.work.sheet_by_name('明细')
        self.rows = self.work_sheet.nrows
        self.odd_list = []

    def show_excel(self, odd=None):
        """
            查看指定的excel文件
        :return:
        """
             # show sheet all rows

        result = []
        for raw in range(1, self.rows):
            raw_data = self.work_sheet.row_values(raw)
            if self.work_sheet.cell_value(raw, 1) == odd:
                # print(raw_data)
                result.append([str(raw_data[1]),
                               str(raw_data[4]),
                               str(raw_data[6]),
                               str(raw_data[7]),
                               str(raw_data[8]),
                               str("%.2f%%"% (raw_data[10]*100)),
                               str(raw_data[13]),
                               str(raw_data[15]),
                               str(raw_data[16]), ])
                return result[0]

    def show_csv_odd(self, odd):
        """
            查看指定的csv的odd行信息
        :return:
        """
        if odd:
            with open(self.csv_path, encoding='utf-8') as csv_file:
                read = csv.reader(csv_file)
                for line in read:
                    if odd == '1':
                        self.odd_list.append(eval(str(line).replace('\\t', ''))[1])
                    if eval(str(line).replace('\\t', ''))[1] == odd:
                        return eval(str(line).replace('\\t', ''))
        return "odd is none type"

# if __name__ == '__main__':
#     EXCEL = Excel()
#
#     EXCEL.show_csv_odd('1')
#     EXCEL.odd_list.pop(0)
#     for i in EXCEL.odd_list:
#         print(i, EXCEL.show_excel(odd=i)[0])
#
#     print(set(EXCEL.show_excel(odd='796200765922161'))
#           - set(EXCEL.show_csv_odd('796200765922161')))
