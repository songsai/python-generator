# coding=utf-8
import xlrd, GenerateFileUtils

class Excel:

    def firstLower(self, string):
        return string[:1].lower() + string[1:]

    def readFileData(self):
        # 读取文件
        filename = 'C:\\Users\\11941\\Desktop\\python\\平安银行能力开放平台电商见证宝接口文档-不验证（非自营标准）V1.0.xlsx'
        workbook = xlrd.open_workbook(filename)
        # 方法一；获取文件中所有的表
        # sheets = workbook.sheet_names() #['Sheet1', 'Sheet2', 'Sheet3']
        # worksheet = workbook.sheet_names()[0]
        # print(worksheet) #得到表名称
        # 方法二：通过索引获取
        # sheets = workbook.sheet_by_index(0)#得到一个内存地址
        # 方法三：通过表名称获取
        records=['KFEJZB6061','KFEJZB6108','KFEJZB6010','KFEJZB6114','KFEJZB6110','KFEJZB6048','KFEJZB6050',
                'KFEJZB6072','KFEJZB6073','KFEJZB6011','KFEJZB6092','KFEJZB6103','KFEJZB6083','KFEJZB6084','KFEJZB6082','KFEJZB6145','KFEJZB6146','KFEJZB6147','KFEJZB6162','KFEJZB6138','KFEJZB6033','KFEJZB6007','KFEJZB6163','KFEJZB6164','KFEJZB6037','KFEJZB6093','KFEJZB6109','KFEJZB6167','KFEJZB6139','KFEJZB6140']
        for record in records:
            # 循环处理Excel数据
            sheets = workbook.sheet_by_name(record)
            '''
            sheets的名称，行数，列数
            sheets.name  表名称
            sheets.nrows 行数
            sheets.ncols 列数
            '''
            # 得到行数
            nums = sheets.nrows
            # 获取整行整列的值-->得到的是个列表
            # rows = sheets.row_values(0) #获取第一行的标题
            # cols = sheets.col_values(1) #获取第二列的数据
            # 获取单元格内容
            # print(sheets.cell(1, 0)) #1行0列
            # print(sheets.cell_value(2, 0))#2行0列
            # print(sheets.row(1)[0])#1行0列
            # # 获取单元格内容的数据类型
            # print(sheets.cell(1, 0).ctype)
            rows = sheets.row_values(1)
            # true是请求消息，false是返回消息
            flag = True
            classComment = rows[1]
            className = rows[2]
            fileds = []
            rspFileds = []
            filedComments = []
            rspFiledComments = []
            isNeeds = []
            rspIsNeeds = []
            for i in range(5, nums):
                rows = sheets.row_values(i)
                filed = rows[0]
                filedComment = rows[1]
                isNeed = rows[3]
                if filed == '输出':
                    flag = False
                    continue
                if flag == True:
                    fileds.append(self.firstLower(filed))
                    filedComments.append(filedComment)
                    isNeeds.append(isNeed)
                else:
                    rspFileds.append(self.firstLower(filed))
                    rspFiledComments.append(filedComment)
                    rspIsNeeds.append('N')

            print("-------获取数据完毕，开始写入--------")
            file = GenerateFileUtils.GenerateFileUtils()
            # 生成请求消息实体
            file.beanFileWriter(className, classComment, fileds, filedComments, isNeeds, 1)
            print("-------请求消息体生成完毕--------")
            # 生成返回消息实体
            file.beanFileWriter(className, classComment, rspFileds, rspFiledComments, rspIsNeeds, 2)
            print("-------返回消息体生成完毕--------")
            file.atomicFileWriter(className, classComment)
            print("-------调用接口方法生成完毕--------")
            file.controllerFileWriter(className, classComment)
            print("-------controller生成完毕--------")


rf = Excel()
print(rf.readFileData())
