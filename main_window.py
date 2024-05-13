# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowriGiAh.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import resource_rc
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(801, 533)
        MainWindow.setStyleSheet(u"#menu_widget {\n"
"	background-color:  #313a46;\n"
"}\n"
"#menu_widget QPushButton, QLabel{\n"
"	height: 50px;\n"
"	border: none;\n"
"}\n"
"#menu_widget QPushButton:hover{\n"
"	background-color: rgba(86,101,115,0.5);\n"
"}\n"
"#menu_widget QLabel{\n"
"	color: #fff;\n"
"}\n"
"#menu_widget QPushButton{\n"
"	color:  #737373;\n"
"}\n"
"#menu_widget QPushButton:hover{\n"
"	color:  #fff;\n"
"}\n"
"#MainWindow{\n"
"	background-color:#fff;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.menu_widget = QWidget(self.centralwidget)
        self.menu_widget.setObjectName(u"menu_widget")
        self.menu_widget.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.menu_widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.logo = QLabel(self.menu_widget)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(35, 35))
        self.logo.setMaximumSize(QSize(35, 35))
        self.logo.setPixmap(QPixmap(u":/icons/icons/icons8-\ucd9c\uc11d-\ud45c-64.png"))
        self.logo.setScaledContents(True)

        self.horizontalLayout.addWidget(self.logo)

        self.title = QLabel(self.menu_widget)
        self.title.setObjectName(u"title")
        font = QFont()
        font.setFamily(u"Pretendard Variable ExtraBold")
        font.setPointSize(20)
        self.title.setFont(font)

        self.horizontalLayout.addWidget(self.title)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.home_button = QPushButton(self.menu_widget)
        self.home_button.setObjectName(u"home_button")
        font1 = QFont()
        font1.setFamily(u"Pretendard Variable SemiBold")
        font1.setPointSize(13)
        self.home_button.setFont(font1)
        icon = QIcon()
        icon.addFile(u":/icons/icons/icons8-\uc9d1-48 (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_button.setIcon(icon)
        self.home_button.setIconSize(QSize(18, 18))
        self.home_button.setCheckable(True)
        self.home_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.home_button)

        self.data_button = QPushButton(self.menu_widget)
        self.data_button.setObjectName(u"data_button")
        self.data_button.setFont(font1)
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/icons8-\uc601\uc0c1-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.data_button.setIcon(icon1)
        self.data_button.setIconSize(QSize(18, 18))
        self.data_button.setCheckable(True)
        self.data_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.data_button)

        self.learn_button = QPushButton(self.menu_widget)
        self.learn_button.setObjectName(u"learn_button")
        self.learn_button.setFont(font1)
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/icons8-\ucc45-\uacf5\uac1c-\uc2dc\ud5d8-48 (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.learn_button.setIcon(icon2)
        self.learn_button.setIconSize(QSize(18, 18))
        self.learn_button.setCheckable(True)
        self.learn_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.learn_button)

        self.detect_button = QPushButton(self.menu_widget)
        self.detect_button.setObjectName(u"detect_button")
        self.detect_button.setFont(font1)
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/icons8-\uac80\uc0ac-48 (3).png", QSize(), QIcon.Normal, QIcon.Off)
        self.detect_button.setIcon(icon3)
        self.detect_button.setIconSize(QSize(18, 18))
        self.detect_button.setCheckable(True)
        self.detect_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.detect_button)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 248, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.helper_button = QPushButton(self.menu_widget)
        self.helper_button.setObjectName(u"helper_button")
        self.helper_button.setFont(font1)
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/icons8-search-more-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.helper_button.setIcon(icon4)
        self.helper_button.setIconSize(QSize(18, 18))
        self.helper_button.setCheckable(True)
        self.helper_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.helper_button)


        self.gridLayout.addWidget(self.menu_widget, 0, 0, 1, 1)

        self.content_widget = QWidget(self.centralwidget)
        self.content_widget.setObjectName(u"content_widget")
        self.gridLayout_4 = QGridLayout(self.content_widget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.stackedWidget = QStackedWidget(self.content_widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.main_page = QWidget()
        self.main_page.setObjectName(u"main_page")
        self.gridLayout_2 = QGridLayout(self.main_page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.main_page)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamily(u"Pretendard Variable ExtraBold")
        font2.setPointSize(30)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.main_page)
        self.data_page = QWidget()
        self.data_page.setObjectName(u"data_page")
        self.gridLayout_3 = QGridLayout(self.data_page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalSpacer_3 = QSpacerItem(20, 458, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 0, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.data_add_button = QPushButton(self.data_page)
        self.data_add_button.setObjectName(u"data_add_button")
        font3 = QFont()
        font3.setFamily(u"Pretendard Variable SemiBold")
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.data_add_button.setFont(font3)
        self.data_add_button.setStyleSheet(u"border: 4px solid#a6aaaf;\n"
"border-radius: 5px;\n"
"padding: 1px 5px;\n"
"background-color: #a6aaaf;\n"
"")

        self.horizontalLayout_3.addWidget(self.data_add_button)

        self.data_label_button = QPushButton(self.data_page)
        self.data_label_button.setObjectName(u"data_label_button")
        self.data_label_button.setFont(font3)
        self.data_label_button.setStyleSheet(u"border: 4px solid#a6aaaf;\n"
"border-radius: 5px;\n"
"padding: 1px 5px;\n"
"background-color: #a6aaaf;\n"
"")

        self.horizontalLayout_3.addWidget(self.data_label_button)

        self.data_split_button = QPushButton(self.data_page)
        self.data_split_button.setObjectName(u"data_split_button")
        self.data_split_button.setFont(font3)
        self.data_split_button.setStyleSheet(u"border: 4px solid#a6aaaf;\n"
"border-radius: 5px;\n"
"padding: 1px 5px;\n"
"background-color: #a6aaaf;\n"
"")

        self.horizontalLayout_3.addWidget(self.data_split_button)


        self.gridLayout_3.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.data_page)
        self.train_page = QWidget()
        self.train_page.setObjectName(u"train_page")
        self.gridLayout_6 = QGridLayout(self.train_page)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalSpacer_4 = QSpacerItem(20, 434, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_4, 1, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.train_page)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        font4 = QFont()
        font4.setPointSize(9)
        self.lineEdit_2.setFont(font4)
        self.lineEdit_2.setStyleSheet(u"border: 2px solid#a6aaaf;\n"
"border-radius: 5px;\n"
"padding: 1px 5px;\n"
"\n"
"")

        self.gridLayout_6.addWidget(self.lineEdit_2, 0, 0, 1, 1)

        self.train_data_upload_button = QPushButton(self.train_page)
        self.train_data_upload_button.setObjectName(u"train_data_upload_button")
        self.train_data_upload_button.setFont(font3)
        self.train_data_upload_button.setStyleSheet(u"border: 4px solid#a6aaaf;\n"
"border-radius: 5px;\n"
"padding: 1px 5px;\n"
"background-color: #a6aaaf;\n"
"")

        self.gridLayout_6.addWidget(self.train_data_upload_button, 0, 1, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.autoencoder_button = QPushButton(self.train_page)
        self.autoencoder_button.setObjectName(u"autoencoder_button")
        self.autoencoder_button.setFont(font3)
        self.autoencoder_button.setStyleSheet(u"border: 4px solid#a6aaaf;\n"
"border-radius: 5px;\n"
"padding: 1px 5px;\n"
"background-color: #a6aaaf;\n"
"")

        self.gridLayout_5.addWidget(self.autoencoder_button, 0, 1, 1, 1)

        self.yolo_button = QPushButton(self.train_page)
        self.yolo_button.setObjectName(u"yolo_button")
        self.yolo_button.setMinimumSize(QSize(0, 0))
        self.yolo_button.setMaximumSize(QSize(16777215, 16777215))
        self.yolo_button.setFont(font3)
        self.yolo_button.setStyleSheet(u"border: 4px solid#a6aaaf;\n"
"border-radius: 5px;\n"
"padding: 1px 5px;\n"
"background-color: #a6aaaf;\n"
"")

        self.gridLayout_5.addWidget(self.yolo_button, 0, 0, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_5, 2, 0, 1, 3)

        self.stackedWidget.addWidget(self.train_page)
        self.detect_page = QWidget()
        self.detect_page.setObjectName(u"detect_page")
        self.gridLayout_9 = QGridLayout(self.detect_page)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit = QLineEdit(self.detect_page)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"border: 2px solid#a6aaaf;\n"
"border-radius: 5px;\n"
"padding: 1px 5px;\n"
"")

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.upload_button = QPushButton(self.detect_page)
        self.upload_button.setObjectName(u"upload_button")
        self.upload_button.setFont(font3)
        self.upload_button.setStyleSheet(u"border: 4px solid#a6aaaf;\n"
"border-radius: 5px;\n"
"padding: 1px 5px;\n"
"background-color: #a6aaaf;\n"
"")

        self.horizontalLayout_2.addWidget(self.upload_button)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.gridLayout_9.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 432, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_2, 1, 0, 1, 1)

        self.anomaly_button = QPushButton(self.detect_page)
        self.anomaly_button.setObjectName(u"anomaly_button")
        self.anomaly_button.setFont(font3)
        self.anomaly_button.setStyleSheet(u"border: 4px solid#a6aaaf;\n"
"border-radius: 5px;\n"
"padding: 1px 5px;\n"
"background-color: #a6aaaf;\n"
"")

        self.gridLayout_9.addWidget(self.anomaly_button, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.detect_page)
        self.helper_page = QWidget()
        self.helper_page.setObjectName(u"helper_page")
        self.gridLayout_7 = QGridLayout(self.helper_page)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.textBrowser = QTextBrowser(self.helper_page)
        self.textBrowser.setObjectName(u"textBrowser")
        font5 = QFont()
        font5.setFamily(u"Pretendard Variable SemiBold")
        self.textBrowser.setFont(font5)

        self.gridLayout_7.addWidget(self.textBrowser, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.helper_page)

        self.gridLayout_4.addWidget(self.stackedWidget, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.content_widget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo.setText("")
        self.title.setText(QCoreApplication.translate("MainWindow", u"\uccb4\ud06c\uba54\uc774\ud2b8", None))
        self.home_button.setText(QCoreApplication.translate("MainWindow", u"\ud648", None))
        self.data_button.setText(QCoreApplication.translate("MainWindow", u"\ub370\uc774\ud130", None))
        self.learn_button.setText(QCoreApplication.translate("MainWindow", u"\ud559\uc2b5", None))
        self.detect_button.setText(QCoreApplication.translate("MainWindow", u"\uac80\ucd9c", None))
        self.helper_button.setText(QCoreApplication.translate("MainWindow", u"\ub3c4\uc6c0\ub9d0", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\uccb4\ud06c\uba54\uc774\ud2b8", None))
        self.data_add_button.setText(QCoreApplication.translate("MainWindow", u"\ub370\uc774\ud130\uc14b \ucd94\uac00", None))
        self.data_label_button.setText(QCoreApplication.translate("MainWindow", u"\ub370\uc774\ud130\uc14b \ub77c\ubca8\ub9c1", None))
        self.data_split_button.setText(QCoreApplication.translate("MainWindow", u"\ub370\uc774\ud130\uc14b \ubd84\ud560", None))
        self.train_data_upload_button.setText(QCoreApplication.translate("MainWindow", u"\ubd88\ub7ec\uc624\uae30", None))
        self.autoencoder_button.setText(QCoreApplication.translate("MainWindow", u"AUTOENCODER \ud6c8\ub828", None))
        self.yolo_button.setText(QCoreApplication.translate("MainWindow", u"YOLO \ud6c8\ub828", None))
        self.upload_button.setText(QCoreApplication.translate("MainWindow", u"\ubd88\ub7ec\uc624\uae30", None))
        self.anomaly_button.setText(QCoreApplication.translate("MainWindow", u"\uac80\ucd9c", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Pretendard Variable SemiBold'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Gulim';\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Gulim';\">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu "
                        "fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</span></p></body></html>", None))
    # retranslateUi

