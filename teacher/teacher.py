# -*- coding: utf-8 -*-
import numpy as np
from PySide2.QtCore import QDate, Qt, SIGNAL, QFile
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QMessageBox, QAbstractItemView, QHeaderView, QTableWidgetItem, QPushButton, QTableWidget, \
    QHBoxLayout, QWidget, QGridLayout, QFileDialog
# 目录导入
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from qt_material import apply_stylesheet
from database import teacher_operate, database_base, student_opreate
from lib.share import SI
import matplotlib.pyplot as plt


class Win_tcmain:
    def __init__(self, j=None):
        # super().__init__()
        # self.ui = uic.loadUi('fund_system/main.ui',self)
        self.ui = QUiLoader().load('UI/tc_main.ui')
        self.ui.buttonChange.clicked.connect(self.onSignOut)  # 切换账号
        self.ui.button_tcchange.clicked.connect(self.on_teacher_info_change)  # 信息更新
        self.ui.button_refresh.clicked.connect(self.reget_info)
        date_time = ''
        self.ui.tc_calendar.clicked[QDate].connect(self.publish_insert)
        self.ui.button_publish.clicked.connect(self.onPublish)
        self.ui.button_deletenews.clicked.connect(self.onDelete)
        self.ui.button_search.clicked.connect(self.onSearch)
        self.ui.button_search_detail.clicked.connect(self.onDetail)
        self.ui.button_guo1_refresh.clicked.connect(lambda: self.table_fund_op(self.ui.table_guo1, fund='fundinfo1'))
        self.ui.button_guo2_refresh.clicked.connect(lambda: self.table_fund_op(self.ui.table_guo2, fund='fundinfo2'))
        self.ui.button_guo3_refresh.clicked.connect(lambda: self.table_fund_op(self.ui.table_guo3, fund='fundinfo3'))
        self.ui.button_she1_refresh.clicked.connect(lambda: self.table_fund_op(self.ui.table_she1, fund='fundinfo4'))
        self.ui.button_she2_refresh.clicked.connect(lambda: self.table_fund_op(self.ui.table_she2, fund='fundinfo5'))
        self.ui.button_xiao_refresh.clicked.connect(lambda: self.table_fund_op(self.ui.table_xiao1, fund='fundinfo6'))

        label_title = self.ui.label_title
        apply_stylesheet(label_title, theme='light_pink.xml', extra={'font_size': 25, })
        # tabWidget1 = self.ui.tabWidget1
        # apply_stylesheet(tabWidget1, theme='light_pink.xml', extra={'font_size': 20, })

        # 个人信息
        if database_base.is_has_teacher(SI.login_username) is False:  # 如果第一次登录没有表
            sql = "INSERT INTO teacherinfo(id) VALUES('%s')" % SI.login_username
            database_base.exec(sql)
            print("已完成第一次老师建表")
        self.ui.teacher_id.setText(SI.login_username)
        a = 'name'
        SI.teacher_name = teacher_operate.teacher_op.select_teacherinfo(a, SI.login_username)
        self.ui.teacher_name.setText(SI.teacher_name)
        a = 'home'
        SI.teacher_home = teacher_operate.teacher_op.select_teacherinfo(a, SI.login_username)
        self.ui.teacher_home.setText(SI.teacher_home)
        a = 'phone'
        SI.teacher_phone = teacher_operate.teacher_op.select_teacherinfo(a, SI.login_username)
        self.ui.teacher_phone.setText(SI.teacher_phone)
        a = 'college'
        SI.teacher_college = teacher_operate.teacher_op.select_teacherinfo(a, SI.login_username)
        self.ui.teacher_college.setText(SI.teacher_college)
        a = 'email'
        SI.teacher_email = teacher_operate.teacher_op.select_teacherinfo(a, SI.login_username)
        self.ui.teacher_email.setText(SI.teacher_email)

        # 标题栏
        self.ui.label_huanyin.setText(SI.login_username)
        self.ui.label_huanyin2.setText(SI.teacher_name)

        # 公告栏
        self.ui.tc_news_table.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 设置内容不可修改
        self.ui.tc_news_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 水平自适应
        self.ui.tc_news_table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)  # 垂直自适应

        # 搜索栏
        self.ui.search_id.setText("无")
        self.ui.search_college.setText("无")
        self.ui.search_class.setText("无")
        self.ui.search_name.setText("无")
        self.ui.search_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.search_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.search_table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        # 资助审核栏
        # 国家助学金
        self.ui.table_guo1.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.table_guo1.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.table_guo1.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.ui.table_guo1.itemClicked.connect(lambda: self.onFile(self.ui.table_guo1))  # 点击单元格触发
        fund = 'fundinfo1'
        self.table_fund_op(self.ui.table_guo1, fund.lstrip(''))

        # 国家励志奖学金
        self.ui.table_guo2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.table_guo2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.table_guo2.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        fund = 'fundinfo2'
        self.table_fund_op(self.ui.table_guo2, fund.lstrip(''))
        # 国家助学贷款
        self.ui.table_guo3.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.table_guo3.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.table_guo3.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        fund = 'fundinfo3'
        self.table_fund_op(self.ui.table_guo3, fund.lstrip(''))
        # 1号奖助
        self.ui.table_she1.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.table_she1.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.table_she1.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        fund = 'fundinfo4'
        self.table_fund_op(self.ui.table_she1, fund.lstrip(''))
        # 2号奖助
        self.ui.table_she2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.table_she2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.table_she2.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        fund = 'fundinfo5'
        self.table_fund_op(self.ui.table_she2, fund.lstrip(''))
        # 校内奖助
        self.ui.table_xiao1.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.table_xiao1.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.table_xiao1.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        fund = 'fundinfo6'
        self.table_fund_op(self.ui.table_xiao1, fund.lstrip(''))

        # 贫困生认定
        self.table_pinkun_op(self.ui.tc_pinkun_id)
        self.ui.tc_pinkun_id.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.tc_pinkun_id.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tc_pinkun_id.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        # 绘图
        plt.rcParams['font.family'] = 'sans-serif'
        plt.rcParams['font.sans-serif'] = ['Microsoft Yahei']
        self.portray1()
        self.portray2()
        self.portray3()
        self.portray4()
        self.portray5()

    # 登出
    def onSignOut(self):
        SI.mainWin.ui.hide()
        SI.loginWin.ui.show()

    # 公告部分
    # 发布公告
    def onPublish(self):
        data = student_opreate.student_op.news_op(SI.publish_date)
        text = self.ui.publishText.toPlainText().strip()
        self.ui.publishText.clear()
        teacher_operate.teacher_op.publish_on(self, text)
        self.publish_insert(SI.date_time)

    # 表格操作
    def publish_insert(self, date):
        self.ui.tc_news_table.clearContents()
        data = student_opreate.student_op.news_op(date.toString())
        self.ui.tc_news_table.setColumnCount(2)
        a = 0
        for i in data:
            a = a + 1
        self.ui.tc_news_table.setRowCount(a)
        self.ui.tc_news_table.setHorizontalHeaderLabels(['内容', '发布者'])
        x = 0
        for i in data:
            y = 0
            for j in i:
                a = QTableWidgetItem(str(data[x][y]))
                self.ui.tc_news_table.setItem(x, y, a)
                y = y + 1
            print(y)
            x = x + 1

        SI.publish_date = date.toString()  # 时间值
        SI.date_time = date  # 获取原始时间格式

    # 删除公告
    def onDelete(self):
        print('删除所选择行')
        s_items = self.ui.tc_news_table.selectedItems()  # 获取当前所有选择的items
        if s_items:
            selected_rows = []  # 求出所选择的行数
            for i in s_items:
                row = i.row()
                if row not in selected_rows:
                    selected_rows.append(row)
            selected_rows1 = sorted(selected_rows)
            for r in range(len(sorted(selected_rows1))):
                text = self.ui.tc_news_table.item(selected_rows1[r] - r, 0).text()
                self.ui.tc_news_table.removeRow(selected_rows1[r] - r)  # 删除行
                print(text)
                teacher_operate.teacher_op.publish_out(self, text)

    # 管理员信息修改
    def on_teacher_info_change(self):
        SI.teacher_change = Win_teacher_change()
        SI.teacher_change.ui.show()

    # 重新初始化信息
    def reget_info(self):
        self.ui.teacher_name.setText(SI.teacher_name_2)
        self.ui.teacher_home.setText(SI.teacher_home_2)
        self.ui.teacher_phone.setText(SI.teacher_phone_2)
        self.ui.teacher_id.setText(SI.teacher_id_2)
        self.ui.teacher_college.setText(SI.teacher_college_2)
        self.ui.teacher_email.setText(SI.teacher_email_2)
        self.ui.label_huanyin2.setText(SI.teacher_name_2)
        SI.teacher_name = SI.teacher_name_2
        SI.teacher_home = SI.teacher_home_2
        SI.teacher_phone = SI.teacher_phone_2
        SI.teacher_id = SI.teacher_id_2
        SI.teacher_college = SI.teacher_college_2
        SI.teacher_email = SI.teacher_email_2

    # 搜索贫困生信息
    def onSearch(self):
        SI.search_id = self.ui.search_id.text().strip()
        SI.search_college = self.ui.search_college.text().strip()
        SI.search_class = self.ui.search_class.text().strip()
        SI.search_name = self.ui.search_name.text().strip()
        self.ui.search_id.setText("无")
        self.ui.search_college.setText("无")
        self.ui.search_class.setText("无")
        self.ui.search_name.setText("无")
        self.search_insert()

    # 表格操作
    def search_insert(self):
        data = teacher_operate.teacher_op.search(self)
        self.ui.search_table.setColumnCount(4)
        a = 0
        for i in data:
            a = a + 1
        self.ui.search_table.setRowCount(a)
        self.ui.search_table.setHorizontalHeaderLabels(['学院', '班级', '学号', '姓名'])

        x = 0
        for i in data:
            y = 0
            for j in i:
                a = QTableWidgetItem(str(data[x][y]))
                self.ui.search_table.setItem(x, y, a)
                y = y + 1
            print(y)
            x = x + 1

    # 个人详情
    def onDetail(self):
        s_items = self.ui.search_table.selectedItems()
        r = ''
        for i in s_items:
            r = i.row()
            print(r)
            break
        SI.text = self.ui.search_table.item(r, 2).text()
        teacher_operate.teacher_op.search_detail(self)
        SI.teacher_search = Win_teacher_search()
        SI.teacher_search.ui.show()

    # 资助详情
    def table_fund_op(self, table, fund):
        data = teacher_operate.teacher_op.fund_search(self, fund)
        table.setColumnCount(6)
        a = 0
        for i in data:
            a = a + 1
        table.setRowCount(a)
        table.setHorizontalHeaderLabels(['时间', '学号', '申请人姓名', '审核情况', '附件', '操作'])
        x = 0
        for i in data:
            y = 0
            for j in i:
                a = QTableWidgetItem(str(data[x][y]))
                table.setItem(x, y, a)
                item = table.item(x, y)
                item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                y = y + 1
            lb1 = QPushButton('审核')
            table.setCellWidget(x, y, lb1)
            lb1.clicked.connect(lambda: self.onCheck(table, fund))
            x = x + 1
        table.sortItems(0, Qt.DescendingOrder)  # 指定列排序

    # 贫困生认定
    def onCheck(self, table, fund):
        r = table.currentRow()
        SI.text = table.item(r, 1).text()
        teacher_operate.teacher_op.search_detail(self)
        SI.table = table
        SI.fund = fund
        SI.teacher_check = Win_teacher_apply_check()
        SI.teacher_check.ui.show()

    def table_pinkun_op(self, table):
        data = teacher_operate.teacher_op.pinkun_search(self)
        table.setColumnCount(5)
        a = 0
        for i in data:
            a = a + 1
        table.setRowCount(a)
        table.setHorizontalHeaderLabels(['时间', '学号', '申请人姓名', '认定情况', '操作'])
        x = 0
        for i in data:
            y = 0
            for j in i:
                a = QTableWidgetItem(str(data[x][y]))
                table.setItem(x, y, a)
                item = table.item(x, y)
                item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                y = y + 1
            lb1 = QPushButton('审核')
            table.setCellWidget(x, y, lb1)
            lb1.clicked.connect(lambda: self.onCheck_pinkun(table))
            x = x + 1
        table.sortItems(0, Qt.DescendingOrder)  # 指定列排序

    def onCheck_pinkun(self, table):
        r = table.currentRow()
        SI.text = table.item(r, 1).text()
        teacher_operate.teacher_op.search_detail(self)
        SI.table = table
        fund = 'pinkuninfo'
        SI.fund = fund.lstrip('')
        SI.teacher_check = Win_teacher_pinkun_check()
        SI.teacher_check.ui.show()

    def onFile(self, table):
        s = table.currentColumn()  # 返回当前列序号
        r = table.currentRow()
        value = table.item(r, 4).text()
        if s == 4:
            filename = QFileDialog.getOpenFileName(None, 'open file', value)
            with open(filename[0], 'w+') as file:
                my_txt = file.read()
        # 问题：没有实现直接打开文件

    def portray1(self):
        self.figure = plt.figure(facecolor='#ffcfe3')
        self.canves = FigureCanvas(self.figure)

        self.ui.tu1.addWidget(self.canves)

        agelist = teacher_operate.teacher_op.tu_count_college(self)
        name = teacher_operate.teacher_op.tu_kind_college(self)
        namelist = []
        for i in range(len(name)):
            namelist.append(name[i][0])
        self.x = np.arange(len(namelist))
        self.y = np.array(agelist)

        plt.bar(range(len(namelist)), agelist, tick_label=namelist, color='#ffcfe3', width=0.5)
        plt.title('各学院贫困生人数')
        for i, j in zip(self.x, self.y):
            plt.text(i, j + 0.5, '%d' % j, ha='center', va='center')

        self.canves.draw()

    def portray2(self):

        self.figure = plt.figure(facecolor='#ffcfe3')
        self.canves = FigureCanvas(self.figure)
        self.ui.tu2.addWidget(self.canves)

        size = teacher_operate.teacher_op.tu_count_college(self)
        name = teacher_operate.teacher_op.tu_kind_college(self)
        namelist = []
        for i in range(len(name)):
            namelist.append(name[i][0])
        colors = []
        for i in range(len(namelist)):
            colors.append(teacher_operate.randomcolor(i))
        plt.pie(size, labels=namelist, colors=colors, autopct='%1.2f%%')
        plt.title('各学院贫困生比例')

        self.canves.draw()

    def portray3(self):
        self.figure = plt.figure(facecolor='#ffcfe3')
        self.canves = FigureCanvas(self.figure)

        self.ui.tu3.addWidget(self.canves)

        size = [teacher_operate.teacher_op.tu2_count(self), SI.student_number]
        namelist = ['贫困生人数', '总人数']
        colors = []
        for i in range(len(namelist)):
            colors.append(teacher_operate.randomcolor(i))

        plt.pie(size, labels=namelist, colors=colors, autopct='%1.2f%%')
        plt.title('贫困生总比例')

        self.canves.draw()

    def portray4(self):
        self.figure = plt.figure(facecolor='#ffcfe3')
        self.canves = FigureCanvas(self.figure)

        self.ui.tu4.addWidget(self.canves)

        size = [teacher_operate.teacher_op.tu3_count(self), SI.student_number]
        namelist = ['已资助人数', '总人数']
        colors = []
        for i in range(len(namelist)):
            colors.append(teacher_operate.randomcolor(i))

        plt.pie(size, labels=namelist, colors=colors, autopct='%1.2f%%')
        plt.title('已资助占学生人数比')

        self.canves.draw()

    def portray5(self):
        self.figure = plt.figure(facecolor='#ffcfe3')
        self.canves = FigureCanvas(self.figure)

        self.ui.tu5.addWidget(self.canves)

        data = teacher_operate.teacher_op.tu4_count(self)
        print(data)
        namelist = []
        size=[]
        colors = []
        for i in range(len(data)):
            namelist.append(data[i][0])
        for i in range(len(data)):
            size.append(data[i][1])
        print(size)
        for i in range(len(namelist)):
            colors.append(teacher_operate.randomcolor(i))

        plt.pie(size, labels=namelist, colors=colors, autopct='%1.2f%%')
        plt.title('各学院贫困生比例')

        self.canves.draw()


# 老师信息修改
class Win_teacher_change(Win_tcmain):
    def __init__(self):
        self.ui = QUiLoader().load('UI/teacher_change.ui')
        self.ui.button_sure.clicked.connect(self.onchangeout)
        self.ui.teacher_name_2.setText(SI.teacher_name)
        self.ui.teacher_home_2.setText(SI.teacher_home)
        self.ui.teacher_phone_2.setText(SI.teacher_phone)
        self.ui.teacher_id_2.setText(SI.login_username)
        self.ui.teacher_college_2.setText(SI.teacher_college)
        self.ui.teacher_email_2.setText(SI.teacher_email)

    def onchangeout(self):
        SI.teacher_name_2 = self.ui.teacher_name_2.text().strip()
        SI.teacher_home_2 = self.ui.teacher_home_2.text().strip()
        SI.teacher_phone_2 = self.ui.teacher_phone_2.text().strip()
        SI.teacher_id_2 = self.ui.teacher_id_2.text().strip()
        SI.teacher_college_2 = self.ui.teacher_college_2.text().strip()
        SI.teacher_email_2 = self.ui.teacher_email_2.text().strip()

        print(SI.student_id_2)
        if not SI.teacher_id_2:
            QMessageBox.information(self.ui, 'Error', '请输入必选项', QMessageBox.Yes)
        else:
            teacher_operate.teacher_op.info_change_op(self);
            SI.teacher_change.ui.close()


# 搜索窗口
class Win_teacher_search(Win_tcmain):
    def __init__(self):
        self.ui = QUiLoader().load('UI/teacher_search.ui')
        self.ui.search_name.setText(SI.search_name)
        self.ui.search_home.setText(SI.search_home)
        self.ui.search_phone.setText(SI.search_phone)
        self.ui.search_college.setText(SI.search_college)
        self.ui.search_class.setText(SI.search_class)
        self.ui.search_id.setText(str(SI.search_id))
        self.ui.search_birth.setText(SI.search_birth)
        self.ui.search_email.setText(SI.search_email)
        self.ui.search_sfzid.setText(SI.search_sfzid)
        self.ui.search_live.setText(SI.search_live)
        self.ui.search_income.setText(SI.search_income)
        self.ui.search_pinkun.setCurrentText(SI.search_pinkun)
        self.ui.search_hukou.setCurrentText(SI.search_hukou)


# 审核窗口
class Win_teacher_apply_check(Win_tcmain):
    def __init__(self):
        self.ui = QUiLoader().load('UI/teacher_check.ui')
        self.ui.search_name.setText(SI.search_name)
        self.ui.search_home.setText(SI.search_home)
        self.ui.search_phone.setText(SI.search_phone)
        self.ui.search_college.setText(SI.search_college)
        self.ui.search_class.setText(SI.search_class)
        self.ui.search_id.setText(str(SI.search_id))
        self.ui.search_birth.setText(SI.search_birth)
        self.ui.search_email.setText(SI.search_email)
        self.ui.search_sfzid.setText(SI.search_sfzid)
        self.ui.search_live.setText(SI.search_live)
        self.ui.search_income.setText(SI.search_income)
        self.ui.search_pinkun.setCurrentText(SI.search_pinkun)
        self.ui.search_hukou.setCurrentText(SI.search_hukou)

        self.ui.button_reject.clicked.connect(self.onReject)  # 通过
        self.ui.button_pass.clicked.connect(self.onPass)  # 驳回

    def onReject(self):
        teacher_operate.teacher_op.check_reject(self, SI.fund, SI.search_id)
        SI.teacher_check.ui.close()
        self.table_fund_op(SI.table, SI.fund)  # 重新初始化表

    def onPass(self):
        teacher_operate.teacher_op.check_pass(self, SI.fund, SI.search_id)
        SI.teacher_check.ui.close()
        self.table_fund_op(SI.table, SI.fund)  # 重新初始化表


class Win_teacher_pinkun_check(Win_tcmain):
    def __init__(self):
        self.ui = QUiLoader().load('UI/teacher_check.ui')
        self.ui.search_name.setText(SI.search_name)
        self.ui.search_home.setText(SI.search_home)
        self.ui.search_phone.setText(SI.search_phone)
        self.ui.search_college.setText(SI.search_college)
        self.ui.search_class.setText(SI.search_class)
        self.ui.search_id.setText(str(SI.search_id))
        self.ui.search_birth.setText(SI.search_birth)
        self.ui.search_email.setText(SI.search_email)
        self.ui.search_sfzid.setText(SI.search_sfzid)
        self.ui.search_live.setText(SI.search_live)
        self.ui.search_income.setText(SI.search_income)
        self.ui.search_pinkun.setCurrentText(SI.search_pinkun)
        self.ui.search_hukou.setCurrentText(SI.search_hukou)

        self.ui.button_reject.clicked.connect(self.onReject)  # 通过
        self.ui.button_pass.clicked.connect(self.onPass)  # 驳回

    def onReject(self):
        teacher_operate.teacher_op.pinkun_reject(self, SI.search_id)
        SI.teacher_check.ui.close()
        self.table_pinkun_op(SI.table)  # 重新初始化表

    def onPass(self):
        teacher_operate.teacher_op.pinkun_pass(self, SI.search_id)
        SI.teacher_check.ui.close()
        self.table_pinkun_op(SI.table)  # 重新初始化表
