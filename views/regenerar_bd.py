# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'regenerar_bd.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QProgressBar,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QToolButton, QVBoxLayout, QWidget)

class regenerar_widget(object):
    def setupUi(self, regenerar_widget):
        if not regenerar_widget.objectName():
            regenerar_widget.setObjectName(u"regenerar_widget")
        regenerar_widget.resize(769, 488)
        regenerar_widget.setStyleSheet(u"border-radius: 5px;")
        self.verticalLayout = QVBoxLayout(regenerar_widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.central_frame = QFrame(regenerar_widget)
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
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.ETHasta = QDateEdit(self.content_frame)
        self.ETHasta.setObjectName(u"ETHasta")
        self.ETHasta.setStyleSheet(u"background-color: #fff")

        self.gridLayout.addWidget(self.ETHasta, 1, 1, 1, 1)

        self.ETDesde = QDateEdit(self.content_frame)
        self.ETDesde.setObjectName(u"ETDesde")
        self.ETDesde.setStyleSheet(u"background-color: #fff")

        self.gridLayout.addWidget(self.ETDesde, 0, 1, 1, 1)

        self.BTNSeleccionarCarpeta = QPushButton(self.content_frame)
        self.BTNSeleccionarCarpeta.setObjectName(u"BTNSeleccionarCarpeta")
        self.BTNSeleccionarCarpeta.setMaximumSize(QSize(16777215, 20))
        self.BTNSeleccionarCarpeta.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(204, 170, 28);\n"
"color: white;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: #ffc13b;\n"
"}")

        self.gridLayout.addWidget(self.BTNSeleccionarCarpeta, 2, 2, 1, 1)

        self.label_2 = QLabel(self.content_frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label = QLabel(self.content_frame)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(self.content_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 20))

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.ETUbicacionArchivos = QLineEdit(self.content_frame)
        self.ETUbicacionArchivos.setObjectName(u"ETUbicacionArchivos")
        self.ETUbicacionArchivos.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.ETUbicacionArchivos, 2, 1, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout)

        self.frame = QFrame(self.content_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.RBBanco = QRadioButton(self.frame)
        self.RBBanco.setObjectName(u"RBBanco")
        self.RBBanco.setChecked(True)

        self.verticalLayout_3.addWidget(self.RBBanco)

        self.RBFinanciera = QRadioButton(self.frame)
        self.RBFinanciera.setObjectName(u"RBFinanciera")

        self.verticalLayout_3.addWidget(self.RBFinanciera)


        self.verticalLayout_6.addWidget(self.frame)

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
        self.label_info.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_5.addWidget(self.label_info)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.PBEstado = QProgressBar(self.foot_frame)
        self.PBEstado.setObjectName(u"PBEstado")
        self.PBEstado.setMinimumSize(QSize(100, 0))
        self.PBEstado.setMaximumSize(QSize(100, 16777215))
        self.PBEstado.setStyleSheet(u"color: #FFFFFF;\n"
"text-align: center;")
        self.PBEstado.setValue(0)

        self.horizontalLayout_5.addWidget(self.PBEstado)


        self.verticalLayout_2.addWidget(self.foot_frame)


        self.shadow_layout.addWidget(self.background_frame)


        self.verticalLayout.addWidget(self.central_frame)


        self.retranslateUi(regenerar_widget)

        QMetaObject.connectSlotsByName(regenerar_widget)
    # setupUi

    def retranslateUi(self, regenerar_widget):
        regenerar_widget.setWindowTitle(QCoreApplication.translate("regenerar_widget", u"Form", None))
        self.title_label.setText(QCoreApplication.translate("regenerar_widget", u"Boletines - MF Econom\u00eda e Inversiones", None))
        self.minimize_button.setText(QCoreApplication.translate("regenerar_widget", u"...", None))
        self.restore_button.setText(QCoreApplication.translate("regenerar_widget", u"...", None))
        self.close_button.setText(QCoreApplication.translate("regenerar_widget", u"...", None))
        self.maximize_button.setText(QCoreApplication.translate("regenerar_widget", u"...", None))
        self.BTNSeleccionarCarpeta.setText(QCoreApplication.translate("regenerar_widget", u"Seleccionar carperta", None))
        self.label_2.setText(QCoreApplication.translate("regenerar_widget", u"<html><head/><body><p>Hasta<span style=\" color:#ff0000;\">*</span>:</p></body></html>", None))
        self.label.setText(QCoreApplication.translate("regenerar_widget", u"<html><head/><body><p>Desde<span style=\" color:#ff0000;\">*</span>:</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("regenerar_widget", u"<html><head/><body><p>Ubicaci\u00f3n<span style=\" color:#ff0000;\">*</span>:</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.ETUbicacionArchivos.setToolTip(QCoreApplication.translate("regenerar_widget", u"<html><head/><body><p>Seleccionar la carpeta donde se encuentra los archivos de bolbal o bolfin ya estructurados con el nombre BOLB_MM_AAAA.xls o BOLF_MM_AAAA.xls</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.RBBanco.setText(QCoreApplication.translate("regenerar_widget", u"Bancos", None))
        self.RBFinanciera.setText(QCoreApplication.translate("regenerar_widget", u"Financieras", None))
        self.BtnGenerar.setText(QCoreApplication.translate("regenerar_widget", u"Generar", None))
        self.error_label.setText("")
        self.label_info.setText("")
    # retranslateUi

