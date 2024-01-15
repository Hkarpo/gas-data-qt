# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'analiz.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication
import serial.tools.list_ports
import _thread
from PyQt5 import uic
from PyQt5.QtWidgets import   QMessageBox
from mplwidget import MplWidget1,MplWidget2,MplWidget3,MplWidget4,MplWidget5,MplWidget6
import matplotlib.ticker as ticker
from utils import MSerialPort,scan_ports_info
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
import  serial 
import time
import threading
import inspect
import ctypes
sys_name = "Arduino"


class Ui_MainWindow(object):
    global S_list
    global cnt_lim
    cnt_lim = 300
    _isRunning=0

    def get_all_Serial(self):

        # print(self.comboBox_1.currentText().split(' ')[0])
        try:

           

            ser1 = MSerialPort(self.comboBox_1.currentText().split(' ')[0], self.comboBox_7.currentText())
            _thread.start_new_thread(ser1.read_data, ())
        except Exception as e:
            print('错误明细是', e.__class__.__name__, e)
            ser1 ='None'
        try:

          
            ser2 = MSerialPort(self.comboBox_2.currentText().split(' ')[0], self.comboBox_7.currentText())
            _thread.start_new_thread(ser2.read_data, ())
        except:
            ser2 ='None'
        try:

       
            ser3 = MSerialPort(self.comboBox_3.currentText().split(' ')[0], self.comboBox_7.currentText())
            _thread.start_new_thread(ser3.read_data, ())
        except:
            ser3 ='None'
        try:

    
            ser4 = MSerialPort(self.comboBox_4.currentText().split(' ')[0], self.comboBox_7.currentText())
            _thread.start_new_thread(ser4.read_data, ())
        except Exception as e:
            ser4 = 'None'
        try:

    
            ser5 = MSerialPort(self.comboBox_5.currentText().split(' ')[0], self.comboBox_7.currentText())
            _thread.start_new_thread(ser5.read_data, ())
        except:
            ser5 ='None'
        try:

            ser6 = MSerialPort(self.comboBox_6.currentText().split(' ')[0], self.comboBox_7.currentText())
            _thread.start_new_thread(ser6.read_data, ())
        except:
            ser6 ='None'

        return [ser1,ser2,ser3,ser4,ser5,ser6]


    def setupUi(self, MainWindow,ports):
        self.cnt_lim=cnt_lim
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1450, 1070)
        MainWindow.setWindowIcon(QtGui.QIcon("logocut.png"))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # two side
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.centralwidget.setLayout(self.main_layout)
        self.right_widget = QtWidgets.QWidget()
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout)
        self.right_widget.setStyleSheet('''QWidget{border-radius:5px;background-color:rgb(255,255,255);}''')
        self.left_widget = QtWidgets.QWidget()
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()
        self.left_widget.setLayout(self.left_layout)
        # self.left_widget.setStyleSheet('''QWidget{border-radius:7px;background-color:#ee0000;}''')
        self.main_layout.addWidget(self.left_widget, 0, 0, 120, 17)
        self.main_layout.addWidget(self.right_widget, 0, 17, 120, 100)

        # six graph window
        self.MplWidget1 = MplWidget1(self.centralwidget)
        self.MplWidget1.setGeometry(QtCore.QRect(250, 10, 621, 301))
        self.MplWidget1.setObjectName("MplWidget1")
        self.MplWidget2 = MplWidget2(self.centralwidget)
        self.MplWidget2.setGeometry(QtCore.QRect(810, 10, 621, 301))
        self.MplWidget2.setObjectName("MplWidget2")
        self.MplWidget3 = MplWidget3(self.centralwidget)
        self.MplWidget3.setGeometry(QtCore.QRect(250, 360, 621, 301))
        self.MplWidget3.setObjectName("MplWidget3")
        self.MplWidget4 = MplWidget4(self.centralwidget)
        self.MplWidget4.setGeometry(QtCore.QRect(810, 360, 621, 301))
        self.MplWidget4.setObjectName("MplWidget4")
        self.MplWidget5 = MplWidget5(self.centralwidget)
        self.MplWidget5.setGeometry(QtCore.QRect(250, 710, 621, 301))
        self.MplWidget5.setObjectName("MplWidget5")
        self.MplWidget6 = MplWidget6(self.centralwidget)
        self.MplWidget6.setGeometry(QtCore.QRect(810, 710, 621, 301))
        self.MplWidget6.setObjectName("MplWidget6")

        # port & button
        self.label = QtWidgets.QLabel(self.centralwidget)       # scent.co
        self.label.setGeometry(QtCore.QRect(1190, 640, 111, 20))
        self.label.setObjectName("label")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)     # port1
        self.label_1.setGeometry(QtCore.QRect(40, 160, 61, 16))
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)     # port2
        self.label_2.setGeometry(QtCore.QRect(40, 200, 61, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)     # port3
        self.label_3.setGeometry(QtCore.QRect(40, 240, 61, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)     # port4
        self.label_4.setGeometry(QtCore.QRect(40, 280, 61, 16))
        # self.label_4.setText("label_4")
        self.label_4.setObjectName("label_4")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)    # port5
        self.label_15.setGeometry(QtCore.QRect(40, 320, 61, 16))
        # self.label_15.setText("label_15")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)    # port6
        self.label_16.setGeometry(QtCore.QRect(40, 360, 61, 16))
        # self.label_16.setText("label_16")
        self.label_16.setObjectName("label_16")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)  # baudrate
        self.label_5.setGeometry(QtCore.QRect(20, 400, 81, 16))
        self.label_5.setObjectName("label_5")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)     # start button
        self.pushButton.setGeometry(QtCore.QRect(27, 620, 171, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)   # stop button
        self.pushButton_2.setGeometry(QtCore.QRect(27, 655, 171, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_r = QtWidgets.QPushButton(self.centralwidget)  # refresh button
        self.pushButton_r.setGeometry(QtCore.QRect(27, 690, 171, 31))
        self.pushButton_r.setObjectName("pushButton_r")

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(25, 739, 175, 290))
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setStyleSheet("font: 75 8.5pt \"MS Shell Dlg 2\";")


        self.comboBox_1 = QtWidgets.QComboBox(self.centralwidget)   # port1 com
        self.comboBox_1.setGeometry(QtCore.QRect(110, 160, 100, 22))
        self.comboBox_1.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)   # port2 com
        self.comboBox_2.setGeometry(QtCore.QRect(110, 200, 100, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)  # port3 com
        self.comboBox_3.setGeometry(QtCore.QRect(110, 240, 100, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)   # port4 com
        self.comboBox_4.setGeometry(QtCore.QRect(110, 280, 100, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_5 = QtWidgets.QComboBox(self.centralwidget)   # port5 com
        self.comboBox_5.setGeometry(QtCore.QRect(110, 320, 100, 22))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_6 = QtWidgets.QComboBox(self.centralwidget)   # port6 com
        self.comboBox_6.setGeometry(QtCore.QRect(110, 360, 100, 22))
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_7 = QtWidgets.QComboBox(self.centralwidget)   # baudrate choose
        self.comboBox_7.setGeometry(QtCore.QRect(110, 400, 100, 22))
        self.comboBox_7.setObjectName("comboBox_7")

        # TH1-TH6
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(50, 430, 51, 31))
        self.label_7.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(50, 460, 51, 31))
        self.label_8.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(50, 490, 51, 31))
        self.label_9.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(50, 520, 51, 31))
        self.label_10.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(50, 550, 51, 31))
        self.label_11.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(50, 580, 51, 31))
        self.label_12.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_12.setObjectName("label_12")

        # font
        self.label_1.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_2.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_3.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_4.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_5.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_15.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_16.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")

        self.comboBox_1.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.comboBox_2.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.comboBox_3.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.comboBox_4.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.comboBox_5.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.comboBox_6.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.comboBox_7.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")

        # TH1-TH6....
        self.label_data1 = QtWidgets.QLabel(self.centralwidget)
        self.label_data1.setGeometry(QtCore.QRect(120, 430, 51, 31))
        self.label_data1.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_data1.setObjectName("label_data1")
        self.label_dat2 = QtWidgets.QLabel(self.centralwidget)
        self.label_dat2.setGeometry(QtCore.QRect(120, 460, 51, 31))
        self.label_dat2.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_dat2.setObjectName("label_dat2")
        self.label_data3 = QtWidgets.QLabel(self.centralwidget)
        self.label_data3.setGeometry(QtCore.QRect(120, 490, 51, 31))
        self.label_data3.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_data3.setObjectName("label_data3")
        self.label_data4 = QtWidgets.QLabel(self.centralwidget)
        self.label_data4.setGeometry(QtCore.QRect(120, 520, 51, 31))
        self.label_data4.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_data4.setObjectName("label_data4")
        self.label_data5 = QtWidgets.QLabel(self.centralwidget)
        self.label_data5.setGeometry(QtCore.QRect(120, 550, 51, 31))
        self.label_data5.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_data5.setObjectName("label_data1")
        self.label_data6 = QtWidgets.QLabel(self.centralwidget)
        self.label_data6.setGeometry(QtCore.QRect(120, 580, 51, 31))
        self.label_data6.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_data6.setObjectName("label_dat2")

        # logo
        self.label_img = QtWidgets.QLabel(self.centralwidget)
        self.label_img.setGeometry(QtCore.QRect(25,60,200,50))
        self.label_img.setText("")
        self.label_img.setObjectName("label_img")
        self.label_img.setPixmap(QtGui.QPixmap("LOGO.png").scaled(189, 141))

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1300, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        # self.ui = uic.loadUi("analiz.ui")
        self.t1 =[]
        self.signal1 =[]
        self.signal2 =[]
        self.signal3 =[]
        self.signal4 =[]
        self.signal5 = []
        self.signal6 = []
        #this time
        d = time.localtime()
        cur_time = time.strftime('%M:%S', d)
        # this_time.append(cur_time)

        self.i = cur_time

        self.retranslateUi(MainWindow, ports)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(lambda:self.baglan())
        self.pushButton_2.clicked.connect(lambda:self.stop())
        self.pushButton_r.clicked.connect(lambda: self.refresh())

        # self.ui.show

    def retranslateUi(self, MainWindow,ports):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Scentruth INTERFACE 1.3"))
        self.label.setText(_translate("MainWindow", "Scentruth co."))
        self.label_1.setText(_translate("MainWindow", "Port1"))
        self.label_2.setText(_translate("MainWindow", "Port2"))
        self.label_3.setText(_translate("MainWindow", "Port3"))
        self.label_4.setText(_translate("MainWindow", "Port4"))
        self.label_15.setText(_translate("MainWindow", "Port5"))
        self.label_16.setText(_translate("MainWindow", "Port6"))
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.pushButton_2.setText(_translate("MainWindow", "Stop and Save"))
        self.pushButton_r.setText(_translate("MainWindow", "Refresh Ports"))
        self.label_5.setText(_translate("MainWindow", "Baudrate"))
        self.label_7.setText(_translate("MainWindow", "TH1 "))
        self.label_8.setText(_translate("MainWindow", "TH2 "))
        self.label_9.setText(_translate("MainWindow", "TH3 "))
        self.label_10.setText(_translate("MainWindow", "TH4 "))
        self.label_11.setText(_translate("MainWindow", "TH5 "))
        self.label_12.setText(_translate("MainWindow", "TH6 "))

        self.label_data1.setText(_translate("MainWindow", "........."))
        self.label_dat2.setText(_translate("MainWindow", "........."))
        self.label_data4.setText(_translate("MainWindow", "........."))
        self.label_data3.setText(_translate("MainWindow", "........."))
        self.label_data5.setText(_translate("MainWindow", "........."))
        self.label_data6.setText(_translate("MainWindow", "........."))
        self.comboBox_1.addItems(['none'])
        self.comboBox_2.addItems(['none'])
        self.comboBox_3.addItems(['none'])
        self.comboBox_4.addItems(['none'])
        self.comboBox_5.addItems(['none'])
        self.comboBox_6.addItems(['none'])
        self.textBrowser.append("Current Serials:")
        for i in ports:
            self.comboBox_1.addItems([str(i)])
            self.textBrowser.append(str(i))
            self.comboBox_2.addItems([str(i)])
            self.comboBox_3.addItems([str(i)])
            self.comboBox_4.addItems([str(i)])
            self.comboBox_5.addItems([str(i)])
            self.comboBox_6.addItems([str(i)])
        self.comboBox_1.setDuplicatesEnabled(False)

        # self.comboBox_1.setCurrentIndex(0)  # 设置默认显示的值，不设置则默认为0

        # self.comboBox.currentIndexChanged.connect(self.show)

        self.comboBox_7.addItems(["9600", "115200"])
        # Sensor_list=self.get_all_Serial()
        # self.S_list=Sensor_list
        # print(self.S_list)
        # self.comboBox_3.addItems(["NONE"])
        # self.comboBox_4.addItems(["1000(MS)"])

    def check_data_length(self):
        # print(len(self.t1))
        # print(self.cnt_lim)
        if (len(self.t1)>self.cnt_lim):
            self.t1 = self.t1[1:]
            self.signal1 = self.signal1[1:]
            self.signal2 = self.signal2[1:]
            self.signal3 = self.signal3[1:]
            self.signal4 = self.signal4[1:]
            self.signal5 = self.signal5[1:]
            self.signal6 = self.signal6[1:]

    def update_graph(self,data1,data2,data3,data4,data5,data6):
        d = time.localtime()
        cur_time = time.strftime('%H:%M:%S', d)
        tick_spacing = int(len(self.signal1)/7)+1
        # print(int(len(self.signal1)))
        # print(data1)
        self.i = cur_time
        self.t1.append(self.i)
        self.check_data_length()
        # print('.')
        # print(self.signal1)

        # data length
        data1len = len(data1)
        data2len = len(data2)
        data3len = len(data3)
        data4len = len(data4)
        data5len = len(data5)
        data6len = len(data6)
        data6title = 'DATA6,' * data6len
        self.datatitle = ['DATA1,' * data1len, 'DATA2,' * data2len, 'DATA3,' * data3len, 'DATA4,' * data4len, 'DATA5,' * data5len, data6title[:-1]]

        # multi channel
        self.signal1.append(list(np.array(data1).T))
        self.signal2.append(list(np.array(data2).T))
        self.signal3.append(list(np.array(data3).T))
        self.signal4.append(list(np.array(data4).T))
        self.signal5.append(list(np.array(data5).T))
        self.signal6.append(list(np.array(data6).T))

        # single channel
        # self.signal1.append(float(data1[0]))
        # self.signal2.append(float(data2[0]))
        # self.signal3.append(float(data3[0]))
        # self.signal4.append(float(data4[0]))
        # self.signal5.append(float(data5[0]))
        # self.signal6.append(float(data6[0]))

        # no use
        # self.signal2=np.append(self.signal2, data2)
        # self.signal3=np.append(self.signal3, data3)
        # self.signal4=np.append(self.signal4, data4)
        # self.MplWidget1.canvas.axes.set_ylim(0, 5)

        self.MplWidget1.canvas.axes.clear()
        # multi channel
        legendlist1 = []
        if len(self.signal1) > 3:
            for j in range(len(data1)):
                sig1 = []
                legendlist1.append('s' + str(j))
                for i in self.signal1[3:]:
                    sig1.append(i[j])
                self.MplWidget1.canvas.axes.plot(self.t1[3:], sig1)
        # self.MplWidget1.canvas.axes.plot(self.t1, self.signal1)   # single channel
        # self.MplWidget1.canvas.axes.legend(('Sensor1'),loc='upper right') # no use
        self.MplWidget1.canvas.axes.set_title('DATA1 Signal')
        self.MplWidget1.canvas.axes.set_ylim(0, 5)
        self.MplWidget1.canvas.axes.legend(legendlist1, loc='upper right')
        self.MplWidget1.canvas.axes.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
        self.MplWidget1.canvas.draw()
        
        
        self.MplWidget2.canvas.axes.clear()
        legendlist2 = []
        if len(self.signal2) > 3:
            for j in range(len(data2)):
                sig2 = []
                legendlist2.append('s' + str(j))
                for i in self.signal2[3:]:
                    sig2.append(i[j])
                self.MplWidget2.canvas.axes.plot(self.t1[3:], sig2)
        # self.MplWidget2.canvas.axes.plot(self.t1, self.signal2)     # single channel
        # self.MplWidget2.canvas.axes.legend(('Sensor2'),loc='upper right')
        self.MplWidget2.canvas.axes.set_title('DATA2 Signal')
        self.MplWidget2.canvas.axes.set_ylim(0, 5)
        self.MplWidget2.canvas.axes.legend(legendlist2, loc='upper right')
        self.MplWidget2.canvas.axes.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
        self.MplWidget2.canvas.draw()


        self.MplWidget3.canvas.axes.clear()
        legendlist3 = []
        if len(self.signal3) > 3:
            for j in range(len(data3)):
                sig3 = []
                legendlist3.append('s' + str(j))
                for i in self.signal3[3:]:
                    sig3.append(i[j])
                self.MplWidget3.canvas.axes.plot(self.t1[3:], sig3)
        # self.MplWidget3.canvas.axes.plot(self.t1,self.signal3)
        # self.MplWidget3.canvas.axes.legend(('Sensor3'),loc='upper right')
        self.MplWidget3.canvas.axes.set_title('DATA3 Signal')
        self.MplWidget3.canvas.axes.set_ylim(0, 5)
        self.MplWidget3.canvas.axes.legend(legendlist3, loc='upper right')
        self.MplWidget3.canvas.axes.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
        self.MplWidget3.canvas.draw()


        self.MplWidget4.canvas.axes.clear()
        legendlist4 = []
        if len(self.signal4) > 3:
            for j in range(len(data4)):
                sig4 = []
                legendlist4.append('s' + str(j))
                for i in self.signal4[3:]:
                    sig4.append(i[j])
                self.MplWidget4.canvas.axes.plot(self.t1[3:], sig4)
        # self.MplWidget4.canvas.axes.plot(self.t1,self.signal4)
        # self.MplWidget4.canvas.axes.legend(('Sensor4'),loc='upper right')
        self.MplWidget4.canvas.axes.set_title('DATA4 Signal')
        self.MplWidget4.canvas.axes.set_ylim(0, 5)
        self.MplWidget4.canvas.axes.legend(legendlist4, loc='upper right')
        self.MplWidget4.canvas.axes.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
        self.MplWidget4.canvas.draw()


        self.MplWidget5.canvas.axes.clear()
        legendlist5 = []
        if len(self.signal5) > 3:
            for j in range(len(data5)):
                sig5 = []
                legendlist5.append('s' + str(j))
                for i in self.signal5[3:]:
                    sig5.append(i[j])
                self.MplWidget5.canvas.axes.plot(self.t1[3:], sig5)
        # self.MplWidget5.canvas.axes.plot(self.t1, self.signal5)
        # self.MplWidget5.canvas.axes.legend(('Sensor5'),loc='upper right')
        self.MplWidget5.canvas.axes.set_title('DATA5 Signal')
        self.MplWidget5.canvas.axes.set_ylim(0, 5)
        self.MplWidget5.canvas.axes.legend(legendlist5, loc='upper right')
        self.MplWidget5.canvas.axes.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
        self.MplWidget5.canvas.draw()


        self.MplWidget6.canvas.axes.clear()
        legendlist6 = []
        if len(self.signal6) > 3:
            for j in range(len(data6)):
                sig6 = []
                legendlist6.append('s' + str(j))
                for i in self.signal6[3:]:
                    sig6.append(i[j])
                self.MplWidget6.canvas.axes.plot(self.t1[3:], sig6)
        # self.MplWidget6.canvas.axes.plot(self.t1, self.signal6)
        # self.MplWidget6.canvas.axes.legend(('Sensor6'),loc='upper right')
        self.MplWidget6.canvas.axes.set_title('DATA6 Signal')
        self.MplWidget6.canvas.axes.set_ylim(0, 5)
        self.MplWidget6.canvas.axes.legend(legendlist6, loc='upper right')
        self.MplWidget6.canvas.axes.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
        self.MplWidget6.canvas.draw()

        if self.cnnt==0:
            d = time.localtime()
            # self.cur_time_f = time.strftime('%m_%d_%H_%M_%S', d)
            with open(self.cur_time_f + 'out.csv', "a") as out_file1:
                # cur_time_d = time.strftime('%m_%d_%H_%M_%S', d)
                out_file1.write('     ,'*151 + '\n')
                out_file1.flush()
        elif self.cnnt>10000:
            d = time.localtime()
            self.cur_time_f = time.strftime('%m_%d_%H_%M_%S', d)
            with open(self.cur_time_f + 'out.csv', "a") as out_file1:
                # cur_time_d = time.strftime('%m_%d_%H_%M_%S', d)
                out_file1.write(
                    'TIME' + ',' + self.datatitle[0] + self.datatitle[1] + self.datatitle[2] + self.datatitle[3] + self.datatitle[4] + self.datatitle[
                        5] + '\n')
                out_file1.flush()
            self.cnnt=0
            



        with open(self.cur_time_f+'out.csv', "a") as out_file1:
            # self.check_multi_serial_event()
              # Writes data to file
            d = time.localtime()
            cur_time_d = time.strftime('%m_%d_%H_%M_%S', d)
            # print(cur_time_d)
            out_file1.write(cur_time_d + ',' + str(self.signal1[-1])+ ','+str(self.signal2[-1])+ ','+str(self.signal3[-1])+ ','+str(self.signal4[-1])+',' + str(self.signal5[-1])+',' + str(self.signal6[-1])+'\n')
            out_file1.flush()

    def stop(self):

        # print("stoptesting")
        # self.textBrowser.append("stoptesting")
        self._isRunning=0
        # #close all ports
        for i in range(len(self.S_list)):
            if self.S_list[i]!="None":
                self.S_list[i].port_close()
        #close all threads
        # _thread.exit()
        with open(self.cur_time_f+'out.csv', "r+") as out_file1:
            out_file1.write('TIME ,' + self.datatitle[0] + self.datatitle[1] + self.datatitle[2] + self.datatitle[3] + self.datatitle[4] + self.datatitle[5] + '\n')
            out_file1.flush()
        self.datatitle = []





    def refresh(self):
        if self._isRunning == 1:
            print("fuck off")
            self.textBrowser.append("You should stop first!")
        else:
            print("refreshtesting")
            ports = scan_ports_info(Handle_print=1)
            print(ports)
            ui.setupUi(MainWindow, ports)
            # self.retranslateUi(MainWindow,ports)


    def baglan(self):
        self._isRunning=1
        self.textBrowser.append("Start!")

        # self.message=[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
        Sensor_list=self.get_all_Serial()
        self.S_list=Sensor_list
        self.golden_data=[[],[],[],[],[],[]]
        print(self.S_list)
        self.timeout = 0
        d = time.localtime()
        self.cur_time_f = time.strftime('%m_%d_%H_%M_%S', d)
        with open(self.cur_time_f + 'out.csv', "a") as out_file1:
            # out_file1.write('TIME' + ',' + 'DATA1' + ',' + 'DATA2' + ',' + 'DATA3' + ',' + 'DATA4' +',' + 'DATA5' +',' + 'DATA6'+'\n')
            out_file1.flush()
        self.cnnt=0

        self.check_multi_serial_event()






    def check_multi_serial_event(self):
        if self._isRunning==1:
            th_1 = threading.Timer(0, self.check_multi_serial_event)

            data=[[],[],[],[],[],[]]
            lenth=[1,1,1,1,1,1]

            for i in range(len(self.S_list)):
                cnt = 0
                if self.S_list[i] =='None':
                    data[i] = [0.0000, 0.0000, 0.0000]
                    # data[i] = ['None']
                else:
                    try:
                        thiscurdata=self.S_list[i].message
                        # print(thiscurdata)
                        if thiscurdata[0][0]=='.':
                            cnt+=1
                            # data[i] = [0.0000, 0.0000, 0.0000]
                            data[i] = ['None']
                        else:
                            if thiscurdata[-1]=='\n':
                                curdata = list(map(float, thiscurdata[0:len(thiscurdata) - 4]))
                            else:
                                curdata = list(map(float, thiscurdata[0:len(thiscurdata)]))
                            if max(curdata[0:len(curdata)-3])>5:
                                cnt+=1
                            # else:
                            data[i] = curdata
                            lenth[i] = len(curdata)
                            # print(data[i])

                    except Exception as e:
                        cnt+=1
                        print('错误明细是',e.__class__.__name__,e)
                        if len(data[i])==3:
                            data[i]=data[i]
                            self.S_list[i].flush()
                        else:
                            # data[i] = [0.0000, 0.0000, 0.0000]
                            data[i] = ['None']
                            # lenth = 1
            if cnt==0:
                self.golden_data=['0.0000','0.0000','0.0000']
            print(data)
            # print(lenth)
            if ['None'] not in data:
                self.update_graph(data[0][:lenth[0]],data[1][:lenth[1]],data[2][:lenth[2]],data[3][:lenth[3]],data[4][:lenth[4]],data[5][:lenth[5]])
                self.cnnt+=1
            th_1.start()
        else:
            print("See ya!")
            self.textBrowser.append("Save & Stopping now!")







if __name__ == "__main__":
    import sys
    ports = scan_ports_info(Handle_print=1)
    print(ports)
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow,ports)
    MainWindow.show()
    sys.exit(app.exec_())
