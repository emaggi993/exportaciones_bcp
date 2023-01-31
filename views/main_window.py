# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QToolButton, QVBoxLayout, QWidget)


class MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1014, 443)
        MainWindow.setStyleSheet(u"border-radius: 5px;")
        self.verticalLayout = QVBoxLayout(MainWindow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.central_frame = QFrame(MainWindow)
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
        self.verticalLayout_3 = QVBoxLayout(self.background_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.content_frame = QFrame(self.background_frame)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setStyleSheet(u"")
        self.content_frame.setFrameShape(QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.content_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.top_bar_frame = QFrame(self.content_frame)
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

        self.action_bar_frame_2 = QFrame(self.content_frame)
        self.action_bar_frame_2.setObjectName(u"action_bar_frame_2")
        self.action_bar_frame_2.setMinimumSize(QSize(0, 39))
        self.action_bar_frame_2.setFrameShape(QFrame.StyledPanel)
        self.action_bar_frame_2.setFrameShadow(QFrame.Raised)
        self.grup_box_base = QGroupBox(self.action_bar_frame_2)
        self.grup_box_base.setObjectName(u"grup_box_base")
        self.grup_box_base.setGeometry(QRect(10, 10, 941, 81))
        self.grup_box_base.setStyleSheet(u"color: #1c3c6c")
        self.horizontalLayout_2 = QHBoxLayout(self.grup_box_base)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_agregar_nuevo = QPushButton(self.grup_box_base)
        self.btn_agregar_nuevo.setObjectName(u"btn_agregar_nuevo")
        font = QFont()
        font.setBold(True)
        self.btn_agregar_nuevo.setFont(font)
        self.btn_agregar_nuevo.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(204, 170, 28);\n"
"color: white;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: #ffc13b;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"./assets/icons/csv_black_2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_agregar_nuevo.setIcon(icon4)
        self.btn_agregar_nuevo.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.btn_agregar_nuevo)

        self.btn_rehacer_rango = QPushButton(self.grup_box_base)
        self.btn_rehacer_rango.setObjectName(u"btn_rehacer_rango")
        self.btn_rehacer_rango.setFont(font)
        self.btn_rehacer_rango.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(204, 170, 28);\n"
"color: white;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: #ffc13b;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"./assets/icons/reload.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_rehacer_rango.setIcon(icon5)
        self.btn_rehacer_rango.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.btn_rehacer_rango)

        self.btn_verificar_bancos = QPushButton(self.grup_box_base)
        self.btn_verificar_bancos.setObjectName(u"btn_verificar_bancos")
        self.btn_verificar_bancos.setFont(font)
        self.btn_verificar_bancos.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(204, 170, 28);\n"
"color: white;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: #ffc13b;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"./assets/icons/lupa.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_verificar_bancos.setIcon(icon6)
        self.btn_verificar_bancos.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.btn_verificar_bancos)

        self.btn_delete = QPushButton(self.grup_box_base)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setFont(font)
        self.btn_delete.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 0, 0);\n"
"color: white;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(225, 94, 0);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"./assets/icons/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_delete.setIcon(icon7)
        self.btn_delete.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.btn_delete)

        self.groupBox_informes = QGroupBox(self.action_bar_frame_2)
        self.groupBox_informes.setObjectName(u"groupBox_informes")
        self.groupBox_informes.setGeometry(QRect(10, 110, 541, 81))
        self.groupBox_informes.setStyleSheet(u"color: #1c3c6c")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_informes)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_configuracion = QPushButton(self.groupBox_informes)
        self.btn_configuracion.setObjectName(u"btn_configuracion")
        self.btn_configuracion.setFont(font)
        self.btn_configuracion.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(204, 170, 28);\n"
"color: white;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: #ffc13b;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"./assets/icons/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_configuracion.setIcon(icon8)
        self.btn_configuracion.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.btn_configuracion)

        self.footer = QFrame(self.action_bar_frame_2)
        self.footer.setObjectName(u"footer")
        self.footer.setGeometry(QRect(20, 300, 941, 52))
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.footer)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_info = QFrame(self.footer)
        self.frame_info.setObjectName(u"frame_info")
        self.frame_info.setMinimumSize(QSize(400, 0))
        self.frame_info.setFrameShape(QFrame.StyledPanel)
        self.frame_info.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_info)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_info = QLabel(self.frame_info)
        self.label_info.setObjectName(u"label_info")

        self.verticalLayout_4.addWidget(self.label_info)


        self.horizontalLayout_3.addWidget(self.frame_info)

        self.horizontalSpacer = QSpacerItem(358, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.label_imagen = QLabel(self.footer)
        self.label_imagen.setObjectName(u"label_imagen")
        self.label_imagen.setMinimumSize(QSize(150, 60))
        self.label_imagen.setStyleSheet(u"image: url('./assets/backgrounds/logo-mf-blanco-512.png');")

        self.horizontalLayout_3.addWidget(self.label_imagen)


        self.verticalLayout_2.addWidget(self.action_bar_frame_2)


        self.verticalLayout_3.addWidget(self.content_frame)


        self.shadow_layout.addWidget(self.background_frame)


        self.verticalLayout.addWidget(self.central_frame)


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Form", None))
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"Exportaciones - MF Econom\u00eda e Inversiones", None))
        self.minimize_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.restore_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.close_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.maximize_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.grup_box_base.setTitle(QCoreApplication.translate("MainWindow", u"Base de datos", None))
        self.btn_agregar_nuevo.setText(QCoreApplication.translate("MainWindow", u"Agregar datos de exporaciones", None))
        self.btn_rehacer_rango.setText(QCoreApplication.translate("MainWindow", u"Generar BD por fecha", None))
        self.btn_verificar_bancos.setText(QCoreApplication.translate("MainWindow", u"Verificar Integridad datos", None))
        self.btn_delete.setText(QCoreApplication.translate("MainWindow", u"Borrar datos por fecha", None))
        self.groupBox_informes.setTitle(QCoreApplication.translate("MainWindow", u"Configuraciones", None))
        self.btn_configuracion.setText(QCoreApplication.translate("MainWindow", u"Configuraci\u00f3n", None))
        self.label_info.setText("")
        self.label_imagen.setText("")
    # retranslateUi

