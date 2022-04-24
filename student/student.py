# -*- coding: utf-8 -*-
from PySide2 import QtCore
from PySide2.QtCore import QDate, Qt
from PySide2.QtGui import QPixmap
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QMessageBox, QTableWidgetItem, QAbstractItemView, QHeaderView, QFileDialog, QPushButton

# 目录导入
from qt_material import apply_stylesheet

from database import database_base, teacher_operate
from database import student_opreate
from lib.share import SI


# 学生窗口
class Win_Main:
    def __init__(self, j=None):
        # super().__init__()
        # self.ui = uic.loadUi('fund_system/main.ui',self)
        self.ui = QUiLoader().load('UI/main.ui')
        self.ui.buttonChange.clicked.connect(self.onSignOut)  # 切换账号
        self.ui.info_change.clicked.connect(self.on_student_info_change)
        self.ui.button_refresh.clicked.connect(self.reget_info)
        self.ui.student_calendar.clicked[QDate].connect(self.showNews)
        win = self.ui.widget
        win.setObjectName("MainWindow2")
        # #todo 1 设置窗口背景图片
        win.setStyleSheet("#MainWindow2{border-image:url(./img/cool-background.png);}")
        # 个人信息
        pic = QPixmap('img/个人信息.jpg')
        self.ui.student_img.setPixmap(pic)
        self.ui.student_img.setScaledContents(True)

        if database_base.is_has_student(SI.login_username) is False:  # 如果第一次登录没有表
            sql = "INSERT INTO studentinfo(id,name,home,phone,college,class,birth,email,sfzid,live,identity,income,pinkun,hukou,renzhen,zizhu) VALUES('%s','无','无','无','无','无','无','无','无','无','无','无','无','无','无','无')" % SI.login_username
            database_base.exec(sql)
            print("已完成第一次学生建表")

        # 个人信息获取
        self.ui.student_id.setText(SI.login_username)
        SI.student_id = SI.login_username

        a = 'name'
        SI.student_username = student_opreate.student_op.select_studentinfo(a, SI.login_username)
        self.ui.student_username.setText(SI.student_username)
        a = 'home'
        SI.student_home = student_opreate.student_op.select_studentinfo(a, SI.login_username)
        self.ui.student_home.setText(SI.student_home)
        a = 'phone'
        SI.student_phone = student_opreate.student_op.select_studentinfo(a, SI.login_username)
        self.ui.student_phone.setText(SI.student_phone)
        a = 'college'
        SI.student_college = student_opreate.student_op.select_studentinfo(a, SI.login_username)
        self.ui.student_college.setText(SI.student_college)
        a = 'class'
        SI.student_class = student_opreate.student_op.select_studentinfo(a, SI.login_username)
        self.ui.student_class.setText(SI.student_class)
        a = 'email'
        SI.student_email = student_opreate.student_op.select_studentinfo(a, SI.login_username)
        self.ui.student_email.setText(SI.student_email)
        a = 'sfzid'
        SI.student_sfzid = student_opreate.student_op.select_studentinfo(a, SI.login_username)
        self.ui.student_sfzid.setText(SI.student_sfzid)
        a = 'live'
        SI.student_live = student_opreate.student_op.select_studentinfo(a, SI.login_username)
        self.ui.student_live.setText(SI.student_live)
        a = 'identity'
        SI.student_identity = student_opreate.student_op.select_studentinfo(a, SI.login_username)
        self.ui.student_identity.setText(SI.student_identity)
        a = 'income'
        SI.student_income = student_opreate.student_op.select_studentinfo(a, SI.login_username)
        self.ui.student_income.setText(SI.student_income)
        a = 'pinkun'
        SI.comboBox_pinkun = student_opreate.student_op.select_studentinfo(a, SI.login_username)
        self.ui.comboBox_pinkun.setCurrentText(SI.comboBox_pinkun)
        a = 'hukou'
        SI.comboBox_hukou = student_opreate.student_op.select_studentinfo(a, SI.login_username)
        self.ui.comboBox_hukou.setCurrentText(SI.comboBox_hukou)
        a = 'birth'
        SI.student_birth = student_opreate.student_op.select_studentinfo(a, SI.login_username)
        self.ui.student_birth.setText(SI.student_birth)

        # 标题栏
        self.ui.label_huanyin.setText(SI.login_username)
        self.ui.label_huanyin2.setText(SI.student_username)

        # 公告栏
        self.ui.student_news_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.student_news_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.student_news_table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        # 申请资助界面
        self.ui.button_guo1.clicked.connect(
            lambda: self.onApply(fund_name='fundinfo1', table=self.ui.table_guo, kind='国家助学金',fund_re=1))
        self.ui.button_guo2.clicked.connect(
            lambda: self.onApply(fund_name='fundinfo2', table=self.ui.table_guo, kind='国家励志奖学金',fund_re=1))
        self.ui.button_guo3.clicked.connect(
            lambda: self.onApply(fund_name='fundinfo3', table=self.ui.table_guo, kind='国家助学贷款',fund_re=1))
        self.ui.button_she1.clicked.connect(
            lambda: self.onApply(fund_name='fundinfo4', table=self.ui.table_she, kind='1号奖助金',fund_re=2))
        self.ui.button_she2.clicked.connect(
            lambda: self.onApply(fund_name='fundinfo5', table=self.ui.table_she, kind='2号奖助金',fund_re=2))
        self.ui.button_xiao1.clicked.connect(
            lambda: self.onApply(fund_name='fundinfo6', table=self.ui.table_xiao, kind='校内资助金',fund_re=3))
        # 国家资助表设置
        self.ui.table_guo.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.table_guo.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.table_guo.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        database = 1
        self.table_apply_op(self.ui.table_guo, database)
        # 社会资助表
        self.ui.table_she.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.table_she.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.table_she.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        database = 2
        self.table_apply_op(self.ui.table_she, database)
        # 校内资助表
        self.ui.table_xiao.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.table_xiao.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.table_xiao.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        database = 3
        self.table_apply_op(self.ui.table_xiao, database)

        #资助表删除与修改
        self.ui.button_guo_change.clicked.connect(lambda: self.onChange_apply(table=self.ui.table_guo,fund_re=1))
        self.ui.button_guo_del.clicked.connect(lambda: self.onDelete_apply(table=self.ui.table_guo))
        self.ui.button_she_change.clicked.connect(lambda: self.onChange_apply(table=self.ui.table_she,fund_re=2))
        self.ui.button_she_del.clicked.connect(lambda: self.onDelete_apply(table=self.ui.table_she))
        self.ui.button_xiao_change.clicked.connect(lambda: self.onChange_apply(table=self.ui.table_xiao,fund_re=3))
        self.ui.button_xiao_del.clicked.connect(lambda: self.onDelete_apply(table=self.ui.table_xiao))
        #刷新
        self.ui.button_guo_refresh.clicked.connect(lambda:self.table_apply_op(table=self.ui.table_guo,fund=1))
        self.ui.button_she_refresh.clicked.connect(lambda:self.table_apply_op(table=self.ui.table_she,fund=2))
        self.ui.button_xiao_refresh.clicked.connect(lambda:self.table_apply_op(table=self.ui.table_xiao,fund=3))

        #贫困生认定表
        self.table_pinkun_op(self.ui.table_pinkun_id)
        self.ui.button_pinkun_id.clicked.connect(lambda:self.onPinkun(table=self.ui.table_pinkun_id))
        self.ui.table_pinkun_id.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.table_pinkun_id.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.table_pinkun_id.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        #刷新
        self.ui.button_pinkun_refresh.clicked.connect(lambda: self.table_pinkun_op(table=self.ui.table_pinkun_id))
        #修改
        self.ui.button_pinkun_change.clicked.connect(lambda: self.onChange_pinkun(table=self.ui.table_pinkun_id))
        self.ui.button_pinkun_del.clicked.connect(lambda: self.onDelete_pinkun(table=self.ui.table_pinkun_id))

        #工作表
        self.table_job_publish_op(table=self.ui.table_job_1)
        self.ui.table_job_1.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 设置内容不可修改
        self.ui.table_job_1.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 水平自适应
        self.ui.table_job_1.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)  # 垂直自适应
        self.ui.button_job_apply.clicked.connect(self.job_apply)
        self.table_job_record_op(table=self.ui.table_job_record)
        self.ui.button_job_re.clicked.connect(lambda :self.table_job_record_op(table=self.ui.table_job_record))
        self.ui.table_job_record.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 设置内容不可修改
        self.ui.table_job_record.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 水平自适应
        self.ui.table_job_record.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)  # 垂直自适应

        #工作记录
        # self.table_job_record_op(table=self.ui.table_job_2)
    # 公告显示
    def showNews(self, date):
        self.ui.student_news_table.clearContents()
        data = student_opreate.student_op.news_op(date.toString())
        print(data)
        self.ui.student_news_table.setColumnCount(2)
        a = 0
        for i in data:
            a = a + 1
        self.ui.student_news_table.setRowCount(a)
        self.ui.student_news_table.setHorizontalHeaderLabels(['内容', '发布者'])

        x = 0
        for i in data:
            y = 0
            for j in i:
                a = QTableWidgetItem(str(data[x][y]))
                self.ui.student_news_table.setItem(x, y, a)
                y = y + 1
            x = x + 1

    # 学生修改窗口
    def on_student_info_change(self):
        SI.student_change = Win_student_change()
        SI.student_change.ui.show()

    # 登出
    def onSignOut(self):
        SI.mainWin.ui.hide()
        SI.loginWin.ui.show()

    # 信息初始化
    def reget_info(self):
        self.ui.student_username.setText(SI.student_username_2)
        self.ui.student_home.setText(SI.student_home_2)
        self.ui.student_phone.setText(SI.student_phone_2)
        self.ui.student_college.setText(SI.student_college_2)
        self.ui.student_class.setText(SI.student_class_2)
        self.ui.student_email.setText(SI.student_email_2)
        self.ui.student_sfzid.setText(SI.student_sfzid_2)
        self.ui.student_live.setText(SI.student_live_2)
        self.ui.student_identity.setText(SI.student_identity_2)
        self.ui.student_income.setText(SI.student_income_2)
        self.ui.comboBox_pinkun.setCurrentText(SI.comboBox_pinkun_2)
        self.ui.comboBox_hukou.setCurrentText(SI.comboBox_hukou_2)
        self.ui.student_birth.setText(SI.student_birth_2)
        self.ui.label_huanyin2.setText(SI.student_username_2)

    # 申请奖助
    def onApply(self, fund_name, table, kind,fund_re):
        SI.apply_table = table
        SI.apply_fund = fund_name.lstrip('')
        SI.apply_fund_re=fund_re
        SI.apply_kind = kind
        data_pinkun=student_opreate.student_op.apply_pinkun(self)
        print(data_pinkun)
        if database_base.is_has_apply(SI.apply_fund, SI.student_id) is False :
            if data_pinkun is True:
                SI.student_apply = Win_student_apply()
                SI.student_apply.ui.show()
            else:
                QMessageBox.information(self.ui, 'Error', '未认证贫困生', QMessageBox.Yes)
        else:
            QMessageBox.information(self.ui, 'Error', '已申请', QMessageBox.Yes)

    # 奖助表初始化
    def table_apply_op(self, table, fund):
        data = student_opreate.student_op.apply_table(self, fund)
        table.setColumnCount(6)
        a = 0
        for i in data:
            a = a + 1
        table.setRowCount(a)
        table.setHorizontalHeaderLabels(['时间', '学号', '申请人姓名', '审核情况', '附件', '种类'])
        x = 0
        for i in data:
            y = 0
            for j in i:
                a = QTableWidgetItem(str(data[x][y]))
                table.setItem(x, y, a)
                item = table.item(x, y)
                item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                y = y + 1
            x = x + 1
        table.sortItems(0, Qt.DescendingOrder)  # 指定列排序

    # 申请删除
    def onDelete_apply(self, table):
        print('删除所选择行')
        s_items = table.selectedItems()  # 获取当前所有选择的items
        if s_items:
            selected_rows = []  # 求出所选择的行数
            for i in s_items:
                row = i.row()
                if row not in selected_rows:
                    selected_rows.append(row)
            selected_rows1 = sorted(selected_rows)
            for r in range(len(sorted(selected_rows1))):
                id = table.item(selected_rows1[r] - r, 1).text()  # 获取id和kind种类，去数据库进行搜索，删除
                kind = table.item(selected_rows1[r] - r, 5).text()
                table.removeRow(selected_rows1[r] - r)  # 删除行
                student_opreate.student_op.apply_out(self,kind,id)

    # 奖助修改
    def onChange_apply(self,table,fund_re):
        s_items = table.selectedItems()  # 获取当前所有选择的items
        if s_items:
            selected_rows = []  # 求出所选择的行数
            for i in s_items:
                row = i.row()
                if row not in selected_rows:
                    selected_rows.append(row)
            selected_rows1 = sorted(selected_rows)
            for r in range(len(sorted(selected_rows1))):
                id = table.item(selected_rows1[r] - r, 1).text()  # 获取id和kind种类，去数据库进行搜索，删除
                SI.apply_kind = table.item(selected_rows1[r] - r, 5).text()
        SI.apply_table=table
        SI.apply_fund_re = fund_re
        SI.student_apply = Win_student_apply_change()
        SI.student_apply.ui.show()

    #贫困生认定
    def table_pinkun_op(self, table):
        data = student_opreate.student_op.pinkun_table(self)
        table.setColumnCount(4)
        a = 0
        for i in data:
            a = a + 1
        table.setRowCount(a)
        table.setHorizontalHeaderLabels(['时间', '学号', '申请人姓名', '认定情况'])
        x = 0
        for i in data:
            y = 0
            for j in i:
                a = QTableWidgetItem(str(data[x][y]))
                table.setItem(x, y, a)
                item = table.item(x, y)
                item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                y = y + 1
            x = x + 1
        table.sortItems(0, Qt.DescendingOrder)  # 指定列排序
    #贫困生认定申请
    def onPinkun(self,table):
        SI.pinkun_table=table
        if database_base.is_has_pinkun(SI.student_id) is False:
            SI.win_pinkuin = Win_student_pinkun()
            SI.win_pinkuin.ui.show()
        else:
            QMessageBox.information(self.ui, 'Error', '已申请', QMessageBox.Yes)

    def onChange_pinkun(self,table):
        SI.pinkun_table = table
        SI.win_pinkuin = Win_student_pinkun_change()
        SI.win_pinkuin.ui.show()

    def onDelete_pinkun(self, table):
        s_items = table.selectedItems()  # 获取当前所有选择的items
        if s_items:
            selected_rows = []  # 求出所选择的行数
            for i in s_items:
                row = i.row()
                if row not in selected_rows:
                    selected_rows.append(row)
            selected_rows1 = sorted(selected_rows)
            for r in range(len(sorted(selected_rows1))):
                id = table.item(selected_rows1[r] - r, 1).text()
                table.removeRow(selected_rows1[r] - r)  # 删除行
                student_opreate.student_op.pinkun_out(self,id)

    #工作建表
    def table_job_publish_op(self,table):
        data = teacher_operate.teacher_op.job_search(self)
        print(data)
        table.setColumnCount(7)
        table.setHorizontalHeaderLabels(['时间', '地点', '工作名称', '工资', '联系人方式', '截止日期','工作时间'])
        if data!=None:
            a = 0
            for i in data:
                a = a + 1
            table.setRowCount(a)
            x = 0
            for i in data:
                y = 0
                for j in i:
                    content = QTableWidgetItem(str(data[x][y]))
                    table.setItem(x, y, content)
                    item = table.item(x, y)
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    y = y + 1
                x = x + 1
            table.sortItems(0, Qt.DescendingOrder)  # 指定列排序

    #工作申请
    def job_apply(self):
        s_items = self.ui.table_job_1.selectedItems()  # 获取当前所有选择的items
        if s_items:
            selected_rows = []  # 求出所选择的行数
            for i in s_items:
                row = i.row()
                if row not in selected_rows:
                    selected_rows.append(row)
            selected_rows1 = sorted(selected_rows)
            for r in range(len(sorted(selected_rows1))):
                id = SI.student_id
                work_name = self.ui.table_job_1.item(selected_rows1[r] - r,2).text()
                place=self.ui.table_job_1.item(selected_rows1[r] - r,1).text()
                salary=self.ui.table_job_1.item(selected_rows1[r] - r,3).text()
                connect=self.ui.table_job_1.item(selected_rows1[r] - r,4).text()
                end=self.ui.table_job_1.item(selected_rows1[r] - r,5).text()
                work_t=self.ui.table_job_1.item(selected_rows1[r] - r,6).text()
                username=SI.student_username
                student_opreate.student_op.job_apply(self, id,work_name,username,place,salary,connect,end,work_t)
        QMessageBox.information(self.ui, '提示', '申请成功', QMessageBox.Yes)
    #工作记录
    def table_job_record_op(self,table):
        table.clearContents()
        data = teacher_operate.teacher_op.job_search_2(self,SI.student_id)
        print(data)
        table.setColumnCount(5)
        table.setHorizontalHeaderLabels(['时间','学号','工作名称','状态','操作'])
        if data!=None:
            a = 0
            for i in data:
                a = a + 1
            table.setRowCount(a)
            x = 0
            for i in data:
                y = 0
                for j in i:
                    content = QTableWidgetItem(str(data[x][y]))
                    table.setItem(x, y, content)
                    item = table.item(x, y)
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    y = y + 1
                lb1 = QPushButton('详情')
                table.setCellWidget(x, y, lb1)
                lb1.clicked.connect(lambda: self.onCheck_job(table))
                x = x + 1
            table.sortItems(0, Qt.DescendingOrder)  # 指定列排序

    def onCheck_job(self, table):
        r = table.currentRow()
        SI.text = table.item(r, 1).text()
        SI.job_check = Win_student_job_check()
        SI.job_check.ui.show()

# 个人信息窗口
class Win_student_change(Win_Main):
    def __init__(self):
        super().__init__()
        self.ui = QUiLoader().load('UI/student_change.ui')
        self.ui.butto_sure.clicked.connect(self.onchangeout)
        self.ui.student_username_2.setText(SI.student_username)
        self.ui.student_home_2.setText(SI.student_home)
        self.ui.student_phone_2.setText(SI.student_phone)
        self.ui.student_college_2.setText(SI.student_college)
        self.ui.student_class_2.setText(SI.student_class)
        self.ui.student_email_2.setText(SI.student_email)
        self.ui.student_sfzid_2.setText(SI.student_sfzid)
        self.ui.student_live_2.setText(SI.student_live)
        self.ui.student_identity_2.setText(SI.student_identity)
        self.ui.student_income_2.setText(SI.student_income)
        self.ui.comboBox_pinkun_2.setCurrentText(SI.comboBox_pinkun)
        self.ui.comboBox_hukou_2.setCurrentText(SI.comboBox_hukou)
        self.ui.student_birth_2.setText(SI.student_birth)
        self.ui.student_id_2.setText(SI.login_username)
        self.ui.student_id_2.setFocusPolicy(QtCore.Qt.NoFocus)

    def onchangeout(self):
        SI.student_username_2 = self.ui.student_username_2.text().strip()
        SI.student_home_2 = self.ui.student_home_2.text().strip()
        SI.student_phone_2 = self.ui.student_phone_2.text().strip()
        SI.student_college_2 = self.ui.student_college_2.text().strip()
        SI.student_class_2 = self.ui.student_class_2.text().strip()
        SI.student_id_2 = self.ui.student_id_2.text().strip()
        SI.student_email_2 = self.ui.student_email_2.text().strip()
        SI.student_sfzid_2 = self.ui.student_sfzid_2.text().strip()
        SI.student_live_2 = self.ui.student_live_2.text().strip()
        SI.student_birth_2 = self.ui.student_birth_2.text().strip()
        SI.student_identity_2 = self.ui.student_identity_2.text().strip()
        SI.student_income_2 = self.ui.student_income_2.text().strip()
        SI.comboBox_pinkun_2 = self.ui.comboBox_pinkun_2.currentText()
        SI.comboBox_hukou_2 = self.ui.comboBox_hukou_2.currentText()
        SI.student_username = SI.student_username_2
        SI.student_home = SI.student_home_2
        SI.student_phone = SI.student_phone_2
        SI.student_college = SI.student_college_2
        SI.student_class = SI.student_class_2
        SI.student_email = SI.student_email_2
        SI.student_sfzid = SI.student_sfzid_2
        SI.student_live = SI.student_live_2
        SI.student_identity = SI.student_identity_2
        SI.student_income = SI.student_income_2
        SI.comboBox_pinkun = SI.comboBox_pinkun_2
        SI.comboBox_hukou = SI.comboBox_hukou_2
        SI.student_birth = SI.student_birth_2
        if not SI.student_id_2:
            QMessageBox.information(self.ui, 'Error', '请输入必选项', QMessageBox.Yes)
        else:
            student_opreate.student_op.info_change_op(self);
            SI.student_change.ui.close()
# 申请窗口
class Win_student_apply(Win_Main):
    def __init__(self):
        self.ui = QUiLoader().load('UI/apply.ui')
        self.ui.student_username.setText(SI.student_username)
        self.ui.student_home.setText(SI.student_home)
        self.ui.student_phone.setText(SI.student_phone)
        self.ui.student_college.setText(SI.student_college)
        self.ui.student_class.setText(SI.student_class)
        self.ui.student_email.setText(SI.student_email)
        self.ui.student_sfzid.setText(SI.student_sfzid)
        self.ui.student_live.setText(SI.student_live)
        self.ui.student_identity.setText(SI.student_identity)
        self.ui.student_income.setText(SI.student_income)
        self.ui.comboBox_pinkun.setCurrentText(SI.comboBox_pinkun)
        self.ui.comboBox_hukou.setCurrentText(SI.comboBox_hukou)
        self.ui.student_birth.setText(SI.student_birth)
        self.ui.student_id.setText(SI.student_id)

        self.ui.button_save.clicked.connect(self.file_open)
        self.ui.button_sure.clicked.connect(self.onApply_insert)
        self.ui.button_back.clicked.connect(self.outApply_insert)

    def onApply_insert(self):
        SI.apply_text = self.ui.reason.toPlainText()
        SI.apply_file = self.ui.file_text.toPlainText()
        student_opreate.student_op.apply_insert(self)
        self.table_apply_op(SI.apply_table, SI.apply_fund_re)
        SI.student_apply.ui.close()

    def outApply_insert(self):
        SI.student_apply.ui.close()

    def file_open(self):
        # self.ui.file_text.clear()
        filename = QFileDialog.getOpenFileName(None, 'open file', 'D:/')
        print(filename)
        self.ui.file_text.setPlainText(filename[0])
        # with open(filename[0], 'r') as file:
        #     my_txt = file.read()
        #     print("my_txt")
        #     print(my_txt)
        #     self.ui.file_text.setPlainText(my_txt)

    # def file_save(self):
    #     filename = QFileDialog.getSaveFileName(None, 'save file', 'D:/ceshi')
    #     with open(filename[0], 'w') as file:
    #         my_text = self.ui.file_text.toPlainText()
    #         file.write(my_text)
#申请修改界面
class Win_student_apply_change(Win_Main):
    def __init__(self):
        self.ui = QUiLoader().load('UI/apply.ui')
        self.ui.student_username.setText(SI.student_username)
        self.ui.student_home.setText(SI.student_home)
        self.ui.student_phone.setText(SI.student_phone)
        self.ui.student_college.setText(SI.student_college)
        self.ui.student_class.setText(SI.student_class)
        self.ui.student_email.setText(SI.student_email)
        self.ui.student_sfzid.setText(SI.student_sfzid)
        self.ui.student_live.setText(SI.student_live)
        self.ui.student_identity.setText(SI.student_identity)
        self.ui.student_income.setText(SI.student_income)
        self.ui.comboBox_pinkun.setCurrentText(SI.comboBox_pinkun)
        self.ui.comboBox_hukou.setCurrentText(SI.comboBox_hukou)
        self.ui.student_birth.setText(SI.student_birth)
        self.ui.student_id.setText(SI.student_id)
        f = 'file'
        file = student_opreate.student_op.apply_re_search(self,SI.apply_kind,f.lstrip(''))
        f=file[0]
        self.ui.file_text.setPlainText(''.join(map(str, f)))
        f = 'content'
        file = student_opreate.student_op.apply_re_search(self, SI.apply_kind, f.lstrip(''))
        f = file[0]
        self.ui.reason.setPlainText(''.join(map(str, f)))

        self.ui.button_save.clicked.connect(self.file_open)
        self.ui.button_sure.clicked.connect(self.onApply_insert)
        self.ui.button_back.clicked.connect(self.outApply_insert)

    def onApply_insert(self):
        SI.apply_text = self.ui.reason.toPlainText()
        SI.apply_file = self.ui.file_text.toPlainText()
        student_opreate.student_op.apply_change(self,SI.apply_kind)
        self.table_apply_op(SI.apply_table, SI.apply_fund_re)

        SI.student_apply.ui.close()

    def outApply_insert(self):
        SI.student_apply.ui.close()

    def file_open(self):
        # self.ui.file_text.clear()
        filename = QFileDialog.getOpenFileName(None, 'open file', 'D:/')
        print(filename)
        self.ui.file_text.setPlainText(filename[0])
#贫困生认定
class Win_student_pinkun(Win_Main):
    def __init__(self):
        self.ui = QUiLoader().load('UI/apply.ui')
        self.ui.student_username.setText(SI.student_username)
        self.ui.student_home.setText(SI.student_home)
        self.ui.student_phone.setText(SI.student_phone)
        self.ui.student_college.setText(SI.student_college)
        self.ui.student_class.setText(SI.student_class)
        self.ui.student_email.setText(SI.student_email)
        self.ui.student_sfzid.setText(SI.student_sfzid)
        self.ui.student_live.setText(SI.student_live)
        self.ui.student_identity.setText(SI.student_identity)
        self.ui.student_income.setText(SI.student_income)
        self.ui.comboBox_pinkun.setCurrentText(SI.comboBox_pinkun)
        self.ui.comboBox_hukou.setCurrentText(SI.comboBox_hukou)
        self.ui.student_birth.setText(SI.student_birth)
        self.ui.student_id.setText(SI.student_id)

        self.ui.button_save.clicked.connect(self.file_open)
        self.ui.button_sure.clicked.connect(self.onApply_insert)
        self.ui.button_back.clicked.connect(self.outApply_insert)

    def onApply_insert(self):
        SI.apply_text = self.ui.reason.toPlainText()
        SI.apply_file = self.ui.file_text.toPlainText()
        student_opreate.student_op.pinkun_insert(self)
        self.table_pinkun_op(SI.pinkun_table)
        SI.win_pinkuin.ui.close()

    def outApply_insert(self):
        SI.win_pinkuin.ui.close()

    def file_open(self):
        # self.ui.file_text.clear()
        filename = QFileDialog.getOpenFileName(None, 'open file', 'D:/')
        print(filename)
        self.ui.file_text.setPlainText(filename[0])


class Win_student_pinkun_change(Win_Main):
    def __init__(self):
        self.ui = QUiLoader().load('UI/apply.ui')
        self.ui.student_username.setText(SI.student_username)
        self.ui.student_home.setText(SI.student_home)
        self.ui.student_phone.setText(SI.student_phone)
        self.ui.student_college.setText(SI.student_college)
        self.ui.student_class.setText(SI.student_class)
        self.ui.student_email.setText(SI.student_email)
        self.ui.student_sfzid.setText(SI.student_sfzid)
        self.ui.student_live.setText(SI.student_live)
        self.ui.student_identity.setText(SI.student_identity)
        self.ui.student_income.setText(SI.student_income)
        self.ui.comboBox_pinkun.setCurrentText(SI.comboBox_pinkun)
        self.ui.comboBox_hukou.setCurrentText(SI.comboBox_hukou)
        self.ui.student_birth.setText(SI.student_birth)
        self.ui.student_id.setText(SI.student_id)
        f = 'file'
        file = student_opreate.student_op.pinkun_table_op(self, f.lstrip(''))
        f = file[0]
        self.ui.file_text.setPlainText(''.join(map(str, f)))
        f = 'content'
        file = student_opreate.student_op.pinkun_table_op(self,  f.lstrip(''))
        f = file[0]
        self.ui.reason.setPlainText(''.join(map(str, f)))

        self.ui.button_save.clicked.connect(self.file_open)
        self.ui.button_sure.clicked.connect(self.onApply_insert)
        self.ui.button_back.clicked.connect(self.outApply_insert)

    def onApply_insert(self):
        SI.apply_text = self.ui.reason.toPlainText()
        SI.apply_file = self.ui.file_text.toPlainText()
        student_opreate.student_op.pinkun_change(self)
        self.table_pinkun_op(SI.pinkun_table)

        SI.win_pinkuin.ui.close()

    def outApply_insert(self):
        SI.win_pinkuin.ui.close()

    def file_open(self):
        # self.ui.file_text.clear()
        filename = QFileDialog.getOpenFileName(None, 'open file', 'D:/')
        print(filename)
        self.ui.file_text.setPlainText(filename[0])


class Win_student_job_check(Win_Main):
    def __init__(self):
        self.ui = QUiLoader().load('UI/job_record.ui')
        data=student_opreate.student_op.job_search(self)
        print(data)
        self.ui.job_name.setText(data[0][0])
        self.ui.job_place.setText(data[0][1])
        self.ui.job_time.setText(data[0][2])
        self.ui.job_connect.setText(data[0][3])
        self.ui.job_salary.setText(data[0][4])
        self.ui.job_end.setText(data[0][5])
        self.ui.button_reapply.clicked.connect(self.job_unapply)

    def job_unapply(self):
        student_opreate.student_op.job_del(self,SI.student_id)
        SI.job_check.ui.close()
        QMessageBox.information(self.ui, '提示', '删除成功，请刷新', QMessageBox.Yes)
