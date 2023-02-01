# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'config_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QToolButton, QVBoxLayout,
    QWidget)

class config_widget(object):
    def setupUi(self, config_widget):
        if not config_widget.objectName():
            config_widget.setObjectName(u"config_widget")
        config_widget.resize(769, 488)
        config_widget.setStyleSheet(u"border-radius: 5px;")
        self.verticalLayout = QVBoxLayout(config_widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.central_frame = QFrame(config_widget)
        self.central_frame.setObjectName(u"central_frame")
        self.central_frame.setFrameShape(QFrame.StyledPanel)
        self.central_frame.setFrameShadow(QFrame.Raised)
        self.shadow_layout = QVBoxLayout(self.central_frame)
        self.shadow_layout.setSpacing(0)
        self.shadow_layout.setObjectName(u"shadow_layout")
        self.shadow_layout.setContentsMargins(10, 10, 10, 10)
        self.background_frame = QFrame(self.central_frame)
        self.background_frame.setObjectName(u"background_frame")
        self.background_frame.setStyleSheet(u"background-color: rgb(248, 248, 248)")
        self.background_frame.setFrameShape(QFrame.StyledPanel)
        self.background_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.background_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.top_bar_frame = QFrame(self.background_frame)
        self.top_bar_frame.setObjectName(u"top_bar_frame")
        self.top_bar_frame.setMinimumSize(QSize(0, 39))
        self.top_bar_frame.setMaximumSize(QSize(16777215, 40))
        self.top_bar_frame.setStyleSheet(u"background-color: rgb(28, 60, 108);\n"
"color: rgb(255,255,255)")
        self.top_bar_frame.setFrameShape(QFrame.StyledPanel)
        self.top_bar_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.top_bar_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.title_label = QLabel(self.top_bar_frame)
        self.title_label.setObjectName(u"title_label")

        self.horizontalLayout.addWidget(self.title_label)

        self.button_holder_frame = QFrame(self.top_bar_frame)
        self.button_holder_frame.setObjectName(u"button_holder_frame")
        self.button_holder_frame.setMinimumSize(QSize(0, 30))
        self.button_holder_frame.setMaximumSize(QSize(110, 16777215))
        self.button_holder_frame.setFrameShape(QFrame.StyledPanel)
        self.button_holder_frame.setFrameShadow(QFrame.Raised)
        self.minimize_button = QToolButton(self.button_holder_frame)
        self.minimize_button.setObjectName(u"minimize_button")
        self.minimize_button.setGeometry(QRect(10, 0, 22, 22))
        icon = QIcon()
        icon.addFile(u"./assets/icons/minimize-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_button.setIcon(icon)
        self.minimize_button.setIconSize(QSize(25, 25))
        self.restore_button = QToolButton(self.button_holder_frame)
        self.restore_button.setObjectName(u"restore_button")
        self.restore_button.setGeometry(QRect(40, 0, 22, 22))
        icon1 = QIcon()
        icon1.addFile(u"./assets/icons/restore-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_button.setIcon(icon1)
        self.restore_button.setIconSize(QSize(25, 25))
        self.close_button = QToolButton(self.button_holder_frame)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setGeometry(QRect(70, 0, 22, 22))
        icon2 = QIcon()
        icon2.addFile(u"./assets/icons/close-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_button.setIcon(icon2)
        self.close_button.setIconSize(QSize(25, 25))
        self.maximize_button = QToolButton(self.button_holder_frame)
        self.maximize_button.setObjectName(u"maximize_button")
        self.maximize_button.setGeometry(QRect(40, 0, 22, 22))
        icon3 = QIcon()
        icon3.addFile(u"./assets/icons/maximize-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximize_button.setIcon(icon3)
        self.maximize_button.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.button_holder_frame, 0, Qt.AlignVCenter)


        self.verticalLayout_2.addWidget(self.top_bar_frame)

        self.content_frame = QFrame(self.background_frame)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setFrameShape(QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.content_frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame = QFrame(self.content_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"image: url('./assets/icons/base_datos_config.png');")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 35))
        self.label_5.setStyleSheet(u"color: rgb(28, 60, 108);")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"\n"
"image: url('./assets/icons/postgres.png');")

        self.horizontalLayout_2.addWidget(self.label_7)


        self.verticalLayout_6.addWidget(self.frame)

        self.configuracion = QFrame(self.content_frame)
        self.configuracion.setObjectName(u"configuracion")
        self.configuracion.setMinimumSize(QSize(0, 130))
        self.configuracion.setMaximumSize(QSize(16777215, 100))
        self.configuracion.setFrameShape(QFrame.StyledPanel)
        self.configuracion.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.configuracion)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.configuracion)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.le_host = QLineEdit(self.configuracion)
        self.le_host.setObjectName(u"le_host")
        self.le_host.setStyleSheet(u"background-color: #fff")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.le_host)

        self.label_2 = QLabel(self.configuracion)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_2)

        self.le_puerto = QLineEdit(self.configuracion)
        self.le_puerto.setObjectName(u"le_puerto")
        self.le_puerto.setStyleSheet(u"background-color: #fff\n"
"")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.le_puerto)

        self.label_3 = QLabel(self.configuracion)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_3)

        self.le_user = QLineEdit(self.configuracion)
        self.le_user.setObjectName(u"le_user")
        self.le_user.setStyleSheet(u"background-color: #fff")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.le_user)

        self.label_4 = QLabel(self.configuracion)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_4)

        self.le_password = QLineEdit(self.configuracion)
        self.le_password.setObjectName(u"le_password")
        self.le_password.setStyleSheet(u"background-color: #fff")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.le_password)

        self.label_8 = QLabel(self.configuracion)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_8)

        self.le_base = QLineEdit(self.configuracion)
        self.le_base.setObjectName(u"le_base")
        self.le_base.setStyleSheet(u"background-color: #fff\n"
"")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.le_base)


        self.horizontalLayout_3.addLayout(self.formLayout)


        self.verticalLayout_6.addWidget(self.configuracion)

        self.buttons_frame = QFrame(self.content_frame)
        self.buttons_frame.setObjectName(u"buttons_frame")
        self.buttons_frame.setMaximumSize(QSize(16777215, 100))
        self.buttons_frame.setFrameShape(QFrame.StyledPanel)
        self.buttons_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.buttons_frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.BtnGenerar = QPushButton(self.buttons_frame)
        self.BtnGenerar.setObjectName(u"BtnGenerar")
        self.BtnGenerar.setMinimumSize(QSize(0, 30))
        self.BtnGenerar.setMaximumSize(QSize(16777215, 30))
        self.BtnGenerar.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(204, 170, 28);\n"
"color: white;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: #ffc13b;\n"
"}")

        self.horizontalLayout_4.addWidget(self.BtnGenerar)

        self.btn_test = QPushButton(self.buttons_frame)
        self.btn_test.setObjectName(u"btn_test")
        self.btn_test.setMinimumSize(QSize(0, 30))
        self.btn_test.setMaximumSize(QSize(16777215, 30))
        self.btn_test.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(0, 141, 0);\n"
"color: white;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(0, 200, 0);\n"
"}")

        self.horizontalLayout_4.addWidget(self.btn_test)


        self.verticalLayout_6.addWidget(self.buttons_frame)


        self.verticalLayout_2.addWidget(self.content_frame)

        self.foot_frame = QFrame(self.background_frame)
        self.foot_frame.setObjectName(u"foot_frame")
        self.foot_frame.setMinimumSize(QSize(0, 40))
        self.foot_frame.setMaximumSize(QSize(16777215, 40))
        self.foot_frame.setFrameShape(QFrame.StyledPanel)
        self.foot_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.foot_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.error_label = QLabel(self.foot_frame)
        self.error_label.setObjectName(u"error_label")
        self.error_label.setStyleSheet(u"color:rgb(255, 85, 0)")

        self.horizontalLayout_5.addWidget(self.error_label)

        self.label_info = QLabel(self.foot_frame)
        self.label_info.setObjectName(u"label_info")
        self.label_info.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_5.addWidget(self.label_info)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.PBEstado = QProgressBar(self.foot_frame)
        self.PBEstado.setObjectName(u"PBEstado")
        self.PBEstado.setMinimumSize(QSize(100, 0))
        self.PBEstado.setMaximumSize(QSize(100, 16777215))
        self.PBEstado.setStyleSheet(u"color: #000;\n"
"text-align: center;")
        self.PBEstado.setValue(0)

        self.horizontalLayout_5.addWidget(self.PBEstado)


        self.verticalLayout_2.addWidget(self.foot_frame)


        self.shadow_layout.addWidget(self.background_frame)


        self.verticalLayout.addWidget(self.central_frame)


        self.retranslateUi(config_widget)

        QMetaObject.connectSlotsByName(config_widget)
    # setupUi

    def retranslateUi(self, config_widget):
        config_widget.setWindowTitle(QCoreApplication.translate("config_widget", u"Form", None))
        self.title_label.setText(QCoreApplication.translate("config_widget", u"<html><head/><body><p>Exportaciones - MF Econom\u00eda e Inversiones</p></body></html>", None))
        self.minimize_button.setText(QCoreApplication.translate("config_widget", u"...", None))
        self.restore_button.setText(QCoreApplication.translate("config_widget", u"...", None))
        self.close_button.setText(QCoreApplication.translate("config_widget", u"...", None))
        self.maximize_button.setText(QCoreApplication.translate("config_widget", u"...", None))
        self.label_6.setText(QCoreApplication.translate("config_widget", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("config_widget", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">Base de datos</span></p></body></html>", None))
        self.label_7.setText("")
        self.label.setText(QCoreApplication.translate("config_widget", u"<html><head/><body><p>Host<span style=\" color:#ff0000;\">*</span><span style=\" color:#000000;\">:</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("config_widget", u"<html><head/><body><p><span style=\" color:#000000;\">Puerto</span><span style=\" color:#ff0000;\">*</span>:</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("config_widget", u"<html><head/><body><p>Usuario<span style=\" color:#ff0000;\">*</span>:</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("config_widget", u"<html><head/><body><p>Contrase\u00f1a<span style=\" color:#ff0000;\">*</span>:</p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("config_widget", u"<html><head/><body><p>Base de datos<span style=\" color:#ff0000;\">*</span>:</p></body></html>", None))
        self.BtnGenerar.setText(QCoreApplication.translate("config_widget", u"Generar", None))
        self.btn_test.setText(QCoreApplication.translate("config_widget", u"Test", None))
        self.error_label.setText("")
        self.label_info.setText("")
    # retranslateUi

