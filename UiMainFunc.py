import configparser
import os
import re

from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from UiMain import Ui_MainWindow
from moduller import swiss_model_single_file, swiss_model


class UiMainFunc(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.fasta_file_path = ''  # fasta文件路径
        self.out_file_path = 'zdock/outFiles/'
        self.sequence = ''

        self.receptor = ''  # 受配体
        self.ligand = ''

        self.pre_btn = self.PredictPageButton  # 用在高亮显示中

        self.btn_choose_file.clicked.connect(self.choose_fasta_file)  # 选择fasta文件
        self.SubmitButton.clicked.connect(self.submit_data)  # 提交预测
        self.AGLocalFindButton.clicked.connect(self.choose_receptor)  # 选择受体
        self.ABLocalFindButton.clicked.connect(self.choose_ligand)  # 选择配体
        self.DockSubmitButton.clicked.connect(self.docking)  # 对接

        # view页面显示内容
        self.FindButton_l.clicked.connect(self.choose_result_file_l)
        self.FindButton_r.clicked.connect(self.choose_result_file_r)

        # 菜单选择
        self.PredictPageButton.clicked.connect(self.display_menu)
        self.DockPageButton.clicked.connect(self.display_menu)
        self.ViewResiduePageButton.clicked.connect(self.display_menu)

    def choose_fasta_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open", os.path.join('zdock/fastaFiles'), "*.fasta")

        if file_path == '':
            QMessageBox.information(self, '警告', '选择不能为空，请重新选择!',
                                    QMessageBox.Yes, QMessageBox.Yes)
        else:
            self.fasta_file_path = file_path  # 绝对路径 D:/AllProjects/PythonProjs/DaChuang/zdock/fastaFiles/1BZQ_2_Chains E.fast
            # self.out_file_path = 'zdock/outFiles/'

    def submit_data(self):
        # file_name = re.search(r'.+/(.+)', self.fasta_file_path).group(1)
        self.sequence = self.ABSplainTextEdit.toPlainText()+self.AGSplainTextEdit.toPlainText()

        if self.fasta_file_path == '' and self.sequence == '':
            QMessageBox.information(self, '警告', '请先选择fasta文件/输入fasta序列',
                                    QMessageBox.Yes, QMessageBox.Yes)
        elif self.fasta_file_path != '' and self.sequence != '':
            QMessageBox.information(self, '警告', 'fasta文件/fasta序列选其一即可',
                                    QMessageBox.Yes, QMessageBox.Yes)
        elif self.fasta_file_path != '':
            # print(self.fasta_file_path)
            # os.system('set nowPath=%cd%')
            # abs_path = os.path.abspath('predict.py')  # 获取绝对路径
            # abs_path = os.getcwd()  # 获取当前脚本所在路径
            # os.system('python {} -p {} -o {}'.format(os.path.join(abs_path, 'predict.py'), self.fasta_file_path, self.out_file_path))
            config = configparser.ConfigParser()
            config.read('config.ini')
            token = config['SWISS-MODEL']['token']
            print(self.fasta_file_path)
            print(self.out_file_path)
            swiss_model_single_file(token, self.fasta_file_path, self.out_file_path)
            QMessageBox.information(self, '提示', '预测完成',
                                    QMessageBox.Yes, QMessageBox.Yes)
        else:

            print(self.sequence)
            config = configparser.ConfigParser()
            config.read('config.ini')
            token = config['SWISS-MODEL']['token']

            swiss_model(token, self.sequence, "seq", self.out_file_path)
        # if self.fasta_file_path != '':
        #     # print(self.fasta_file_path)
        #     # os.system('set nowPath=%cd%')
        #     # abs_path = os.path.abspath('predict.py')  # 获取绝对路径
        #     # abs_path = os.getcwd()  # 获取当前脚本所在路径
        #     # os.system('python {} -p {} -o {}'.format(os.path.join(abs_path, 'predict.py'), self.fasta_file_path, self.out_file_path))
        #     config = configparser.ConfigParser()
        #     config.read('config.ini')
        #     token = config['SWISS-MODEL']['token']
        #     print(self.fasta_file_path)
        #     print(self.out_file_path)
        #     swiss_model_single_file(token, self.fasta_file_path, self.out_file_path)
        #     QMessageBox.information(self, '提示', '预测完成',
        #                             QMessageBox.Yes, QMessageBox.Yes)
        # else:
        #     QMessageBox.information(self, '警告', '请先选择fasta文件',
        #                             QMessageBox.Yes, QMessageBox.Yes)

    def choose_receptor(self):
        # 选择受体，绝对路径
        file_path, _ = QFileDialog.getOpenFileName(self, "Open", os.path.join('zdock/outFiles'), "*.pdb")
        if file_path == '':
            QMessageBox.information(self, '警告', '选择不能为空，请重新选择!',
                                    QMessageBox.Yes, QMessageBox.Yes)
        else:
            # 只获取文件名，rcsb_pdb_1BZQ
            self.receptor = re.search(r'.+/(.+)\.', file_path).group(1)
            # 填充文本框内容
            self.DockABSplainTextEdit.setPlainText(self.receptor)

    def choose_ligand(self):
        # 选择配体，绝对路径
        file_path, _ = QFileDialog.getOpenFileName(self, "Open", os.path.join('zdock/outFiles'), "*.pdb")
        if file_path == '':
            QMessageBox.information(self, '警告', '选择不能为空，请重新选择!',
                                    QMessageBox.Yes, QMessageBox.Yes)
        else:
            # 只获取文件名，rcsb_pdb_1BZQ
            self.ligand = re.search(r'.+/(.+)\.', file_path).group(1)
            # 填充文本框内容
            self.DockAGSplainTextEdit.setPlainText(self.ligand)

    def docking(self):
        os.system('./enter.sh {} {}'.format(os.path.join('outFiles', self.receptor), os.path.join(
            'outFiles', self.ligand)))

    def choose_result_file_l(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open", os.path.join('zdock/'))
        if file_path == '':
            QMessageBox.information(self, '警告', '选择不能为空，请重新选择!',
                                    QMessageBox.Yes, QMessageBox.Yes)
        else:
            filename = os.path.basename(file_path)
            self.NameTextEdit_l.setPlainText(filename)
            with open(file_path,'r')as f:
                content = f.read()
            self.FliePlainTextEdit_l.setPlainText(content)

    def choose_result_file_r(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open", os.path.join('zdock/'))
        if file_path == '':
            QMessageBox.information(self, '警告', '选择不能为空，请重新选择!',
                                    QMessageBox.Yes, QMessageBox.Yes)
        else:
            filename = os.path.basename(file_path)
            self.NameTextEdit_r.setPlainText(filename)
            with open(file_path, 'r') as f:
                content = f.read()
            self.FilePlainTextEdit_r.setPlainText(content)

    # 高亮显示
    def highLight(self, pre_btn, cur_btn):
        # 获得pre_btn的样式，
        s1 = pre_btn.styleSheet()
        if re.search('background.*;|background-color.*;', s1):
            # search()得到的值是match类型，通过group()函数获取匹配到的字符串
            s1 = s1.replace(re.search('background.*;|background-color.*;', s1).group(0), '')
        # 获得cur_btn的样式
        s2 = cur_btn.styleSheet()
        if re.search('background.*;|background-color.*;', s2):
            s2 = s2.replace(re.search('background.*;|background-color.*;', s2).group(0), '')

        pre_btn.setStyleSheet(s1 + "background:rgb(47, 62, 69);")  # 复原
        cur_btn.setStyleSheet(s2 + "background:rgba(240,240,240,100);")  # 高亮

    def display_menu(self):
        # 信号的使用，多个组件使用同一个触发函数
        sender = self.sender()

        if sender.text() == 'Predict':
            self.highLight(self.pre_btn,self.PredictPageButton)
            self.pre_btn = self.PredictPageButton  # 更新前一按钮
            self.ContentBox.setCurrentIndex(0)

        elif sender.text() == 'Dock':
            self.highLight(self.pre_btn,self.DockPageButton)
            self.pre_btn = self.DockPageButton
            self.ContentBox.setCurrentIndex(2)

        elif sender.text() == 'FileView':
            self.highLight(self.pre_btn,self.ViewResiduePageButton)
            self.pre_btn = self.ViewResiduePageButton
            self.ContentBox.setCurrentIndex(1)