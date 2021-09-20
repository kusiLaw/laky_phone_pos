# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pages.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(1060, 623)
        self.main_pages_layout = QVBoxLayout(MainPages)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(0, 0, 5, 5)
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.home_page.setStyleSheet(u"font-size: 14pt; background: white; ")
        self.page_1_layout = QVBoxLayout(self.home_page)
        self.page_1_layout.setSpacing(5)
        self.page_1_layout.setObjectName(u"page_1_layout")
        self.page_1_layout.setContentsMargins(5, 5, 5, 5)
        self.frame_3 = QFrame(self.home_page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.page_1_layout.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.home_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.logo_layout = QVBoxLayout(self.frame_4)
        self.logo_layout.setObjectName(u"logo_layout")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.logo_layout.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame_4)


        self.page_1_layout.addWidget(self.frame_2)

        self.frame = QFrame(self.home_page)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(160, 30, 113, 22))
        self.textEdit = QTextEdit(self.frame)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(60, 60, 104, 87))
        self.listView = QListView(self.frame)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(390, 0, 256, 192))

        self.page_1_layout.addWidget(self.frame)

        self.pages.addWidget(self.home_page)
        self.phone_page = QWidget()
        self.phone_page.setObjectName(u"phone_page")
        self.phone_page.setStyleSheet(u"font-size: 14pt; background : #2c313c; ")
        self.verticalLayout_3 = QVBoxLayout(self.phone_page)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.phone_page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.contents = QWidget()
        self.contents.setObjectName(u"contents")
        self.contents.setGeometry(QRect(0, 0, 1055, 618))
        self.verticalLayout_4 = QVBoxLayout(self.contents)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.phone_bg_layout = QFrame(self.contents)
        self.phone_bg_layout.setObjectName(u"phone_bg_layout")
        self.phone_bg_layout.setFrameShape(QFrame.NoFrame)
        self.phone_bg_layout.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.phone_bg_layout)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.phone_form_section = QFrame(self.phone_bg_layout)
        self.phone_form_section.setObjectName(u"phone_form_section")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phone_form_section.sizePolicy().hasHeightForWidth())
        self.phone_form_section.setSizePolicy(sizePolicy)
        self.phone_form_section.setMinimumSize(QSize(934, 226))
        self.phone_form_section.setMaximumSize(QSize(16777215, 16777215))
        self.phone_form_section.setStyleSheet(u"")
        self.phone_form_section.setFrameShape(QFrame.StyledPanel)
        self.phone_form_section.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.phone_form_section)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.phoneform_customer_section = QFrame(self.phone_form_section)
        self.phoneform_customer_section.setObjectName(u"phoneform_customer_section")
        sizePolicy.setHeightForWidth(self.phoneform_customer_section.sizePolicy().hasHeightForWidth())
        self.phoneform_customer_section.setSizePolicy(sizePolicy)
        self.phoneform_customer_section.setMinimumSize(QSize(284, 0))
        self.phoneform_customer_section.setMaximumSize(QSize(600, 16777215))
        self.phoneform_customer_section.setStyleSheet(u"")
        self.phoneform_customer_section.setFrameShape(QFrame.NoFrame)
        self.phoneform_customer_section.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.phoneform_customer_section)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(10, 0, 10, 0)
        self.customer_group = QGroupBox(self.phoneform_customer_section)
        self.customer_group.setObjectName(u"customer_group")
        self.formLayout = QFormLayout(self.customer_group)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(12)
        self.formLayout.setContentsMargins(15, 5, 20, 5)
        self.label_3 = QLabel(self.customer_group)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.customer_name = QFrame(self.customer_group)
        self.customer_name.setObjectName(u"customer_name")
        self.customer_name.setStyleSheet(u"")
        self.customer_name.setFrameShape(QFrame.NoFrame)
        self.customer_name.setFrameShadow(QFrame.Raised)
        self.customer_name_edit = QVBoxLayout(self.customer_name)
        self.customer_name_edit.setSpacing(0)
        self.customer_name_edit.setObjectName(u"customer_name_edit")
        self.customer_name_edit.setContentsMargins(0, 0, 0, 0)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.customer_name)

        self.label_2 = QLabel(self.customer_group)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.customer_contact = QFrame(self.customer_group)
        self.customer_contact.setObjectName(u"customer_contact")
        self.customer_contact.setStyleSheet(u"")
        self.customer_contact.setFrameShape(QFrame.NoFrame)
        self.customer_contact.setFrameShadow(QFrame.Raised)
        self.customer_contact_edit = QVBoxLayout(self.customer_contact)
        self.customer_contact_edit.setSpacing(0)
        self.customer_contact_edit.setObjectName(u"customer_contact_edit")
        self.customer_contact_edit.setContentsMargins(0, 0, 0, 0)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.customer_contact)

        self.frame_8 = QFrame(self.customer_group)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setEnabled(False)
        self.frame_8.setMinimumSize(QSize(50, 50))
        self.frame_8.setMaximumSize(QSize(16777215, 100))
        self.frame_8.setStyleSheet(u"")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_8)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 5, 0)
        self.cart_id = QFrame(self.frame_8)
        self.cart_id.setObjectName(u"cart_id")
        self.cart_id.setStyleSheet(u"")
        self.cart_id.setFrameShape(QFrame.NoFrame)
        self.cart_id.setFrameShadow(QFrame.Raised)
        self.cutomer_cart_id_edit = QVBoxLayout(self.cart_id)
        self.cutomer_cart_id_edit.setSpacing(0)
        self.cutomer_cart_id_edit.setObjectName(u"cutomer_cart_id_edit")
        self.cutomer_cart_id_edit.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_4.addWidget(self.cart_id, 1, 1, 1, 1)

        self.frame_14 = QFrame(self.frame_8)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.phone_cart_total_edit = QVBoxLayout(self.frame_14)
        self.phone_cart_total_edit.setSpacing(0)
        self.phone_cart_total_edit.setObjectName(u"phone_cart_total_edit")
        self.phone_cart_total_edit.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_4.addWidget(self.frame_14, 2, 1, 1, 1)

        self.label_4 = QLabel(self.frame_8)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.label_4, 1, 0, 1, 1)

        self.label_25 = QLabel(self.frame_8)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_4.addWidget(self.label_25, 2, 0, 1, 1)

        self.line = QFrame(self.frame_8)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line, 0, 0, 1, 2)


        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.frame_8)


        self.verticalLayout_6.addWidget(self.customer_group)


        self.horizontalLayout.addWidget(self.phoneform_customer_section)

        self.phoneform_phone_section = QFrame(self.phone_form_section)
        self.phoneform_phone_section.setObjectName(u"phoneform_phone_section")
        self.phoneform_phone_section.setMinimumSize(QSize(396, 0))
        self.phoneform_phone_section.setMaximumSize(QSize(600, 16777215))
        self.phoneform_phone_section.setStyleSheet(u"")
        self.phoneform_phone_section.setFrameShape(QFrame.StyledPanel)
        self.phoneform_phone_section.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.phoneform_phone_section)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(5, 0, 5, 0)
        self.phone_group = QGroupBox(self.phoneform_phone_section)
        self.phone_group.setObjectName(u"phone_group")
        self.gridLayout_2 = QGridLayout(self.phone_group)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setVerticalSpacing(12)
        self.gridLayout_2.setContentsMargins(10, 5, 5, 10)
        self.frame_22 = QFrame(self.phone_group)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(100, 0))
        self.frame_22.setStyleSheet(u"")
        self.frame_22.setFrameShape(QFrame.NoFrame)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.phone_type_edit = QVBoxLayout(self.frame_22)
        self.phone_type_edit.setSpacing(0)
        self.phone_type_edit.setObjectName(u"phone_type_edit")
        self.phone_type_edit.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_2.addWidget(self.frame_22, 0, 1, 1, 1)

        self.label_7 = QLabel(self.phone_group)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 2, 0, 1, 1)

        self.label_6 = QLabel(self.phone_group)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(60, 0))
        self.label_6.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_2.addWidget(self.label_6, 0, 2, 1, 1)

        self.label_5 = QLabel(self.phone_group)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(60, 0))
        self.label_5.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)

        self.frame_9 = QFrame(self.phone_group)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.phone_imei_edit = QVBoxLayout(self.frame_9)
        self.phone_imei_edit.setSpacing(0)
        self.phone_imei_edit.setObjectName(u"phone_imei_edit")
        self.phone_imei_edit.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_2.addWidget(self.frame_9, 2, 1, 1, 3)

        self.frame_24 = QFrame(self.phone_group)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMinimumSize(QSize(100, 0))
        self.frame_24.setMaximumSize(QSize(16777215, 16777215))
        self.frame_24.setFrameShape(QFrame.NoFrame)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.phone_model_edit = QVBoxLayout(self.frame_24)
        self.phone_model_edit.setSpacing(0)
        self.phone_model_edit.setObjectName(u"phone_model_edit")
        self.phone_model_edit.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_2.addWidget(self.frame_24, 0, 3, 1, 1)

        self.label_8 = QLabel(self.phone_group)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.label_8, 3, 0, 1, 1)

        self.frame_10 = QFrame(self.phone_group)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.phone_sn_edit = QVBoxLayout(self.frame_10)
        self.phone_sn_edit.setSpacing(0)
        self.phone_sn_edit.setObjectName(u"phone_sn_edit")
        self.phone_sn_edit.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_2.addWidget(self.frame_10, 3, 1, 1, 1)

        self.label_18 = QLabel(self.phone_group)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_2.addWidget(self.label_18, 3, 2, 1, 1)

        self.label_16 = QLabel(self.phone_group)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.label_16, 5, 0, 1, 1)

        self.frame_21 = QFrame(self.phone_group)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setStyleSheet(u"")
        self.frame_21.setFrameShape(QFrame.NoFrame)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.phone_qr = QVBoxLayout(self.frame_21)
        self.phone_qr.setSpacing(0)
        self.phone_qr.setObjectName(u"phone_qr")
        self.phone_qr.setContentsMargins(10, 0, 0, 0)

        self.gridLayout_2.addWidget(self.frame_21, 5, 1, 1, 1)

        self.frame_23 = QFrame(self.phone_group)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_23)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 7)
        self.label_17 = QLabel(self.frame_23)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"")
        self.label_17.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_13.addWidget(self.label_17)


        self.gridLayout_2.addWidget(self.frame_23, 5, 2, 1, 2)


        self.verticalLayout_7.addWidget(self.phone_group)


        self.horizontalLayout.addWidget(self.phoneform_phone_section)

        self.phoneform_cost_section = QFrame(self.phone_form_section)
        self.phoneform_cost_section.setObjectName(u"phoneform_cost_section")
        self.phoneform_cost_section.setMinimumSize(QSize(284, 0))
        self.phoneform_cost_section.setMaximumSize(QSize(600, 16777215))
        self.phoneform_cost_section.setStyleSheet(u"")
        self.phoneform_cost_section.setFrameShape(QFrame.StyledPanel)
        self.phoneform_cost_section.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.phoneform_cost_section)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.cost_group = QGroupBox(self.phoneform_cost_section)
        self.cost_group.setObjectName(u"cost_group")
        self.formLayout_3 = QFormLayout(self.cost_group)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setHorizontalSpacing(7)
        self.formLayout_3.setVerticalSpacing(12)
        self.formLayout_3.setContentsMargins(15, 5, 20, 0)
        self.label_9 = QLabel(self.cost_group)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_9)

        self.label_10 = QLabel(self.cost_group)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_10)

        self.label_11 = QLabel(self.cost_group)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_11)

        self.label_12 = QLabel(self.cost_group)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_12)

        self.frame_26 = QFrame(self.cost_group)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setStyleSheet(u"\\")
        self.frame_26.setFrameShape(QFrame.NoFrame)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.phone_price_edit = QVBoxLayout(self.frame_26)
        self.phone_price_edit.setObjectName(u"phone_price_edit")
        self.phone_price_edit.setContentsMargins(0, 0, 0, 0)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.frame_26)

        self.frame_27 = QFrame(self.cost_group)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setStyleSheet(u"\\")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.phone_discount_edit = QVBoxLayout(self.frame_27)
        self.phone_discount_edit.setObjectName(u"phone_discount_edit")
        self.phone_discount_edit.setContentsMargins(0, 0, 0, 0)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.frame_27)

        self.frame_28 = QFrame(self.cost_group)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setStyleSheet(u"\\")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.phone_tax_edit = QVBoxLayout(self.frame_28)
        self.phone_tax_edit.setObjectName(u"phone_tax_edit")
        self.phone_tax_edit.setContentsMargins(0, 0, 0, 0)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.frame_28)

        self.payment = QFrame(self.cost_group)
        self.payment.setObjectName(u"payment")
        self.payment.setStyleSheet(u"\\")
        self.payment.setFrameShape(QFrame.NoFrame)
        self.payment.setFrameShadow(QFrame.Raised)
        self.phone_payment_edit = QVBoxLayout(self.payment)
        self.phone_payment_edit.setObjectName(u"phone_payment_edit")
        self.phone_payment_edit.setContentsMargins(0, 0, 0, 0)

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.payment)


        self.verticalLayout_8.addWidget(self.cost_group)


        self.horizontalLayout.addWidget(self.phoneform_cost_section)


        self.verticalLayout_5.addWidget(self.phone_form_section)

        self.phone_cart_button_section = QFrame(self.phone_bg_layout)
        self.phone_cart_button_section.setObjectName(u"phone_cart_button_section")
        self.phone_cart_button_section.setMinimumSize(QSize(934, 156))
        self.phone_cart_button_section.setMaximumSize(QSize(16777215, 180))
        self.phone_cart_button_section.setStyleSheet(u"")
        self.phone_cart_button_section.setFrameShape(QFrame.NoFrame)
        self.phone_cart_button_section.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.phone_cart_button_section)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.phone_cart_section = QFrame(self.phone_cart_button_section)
        self.phone_cart_section.setObjectName(u"phone_cart_section")
        self.phone_cart_section.setMaximumSize(QSize(600, 16777215))
        self.phone_cart_section.setStyleSheet(u"")
        self.phone_cart_section.setFrameShape(QFrame.NoFrame)
        self.phone_cart_section.setFrameShadow(QFrame.Raised)
        self.phone_cart_layout = QVBoxLayout(self.phone_cart_section)
        self.phone_cart_layout.setSpacing(0)
        self.phone_cart_layout.setObjectName(u"phone_cart_layout")
        self.phone_cart_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_2.addWidget(self.phone_cart_section)

        self.phone_button_section = QFrame(self.phone_cart_button_section)
        self.phone_button_section.setObjectName(u"phone_button_section")
        self.phone_button_section.setMinimumSize(QSize(484, 0))
        self.phone_button_section.setStyleSheet(u"")
        self.phone_button_section.setFrameShape(QFrame.NoFrame)
        self.phone_button_section.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.phone_button_section)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setContentsMargins(10, 10, 10, 0)
        self.frame_13 = QFrame(self.phone_button_section)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(150, 30))
        self.frame_13.setStyleSheet(u"")
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_13)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.frame_13, 2, 2, 1, 1)

        self.phone_clear = QFrame(self.phone_button_section)
        self.phone_clear.setObjectName(u"phone_clear")
        self.phone_clear.setMinimumSize(QSize(150, 30))
        self.phone_clear.setStyleSheet(u"")
        self.phone_clear.setFrameShape(QFrame.StyledPanel)
        self.phone_clear.setFrameShadow(QFrame.Raised)
        self.phone_clear_layout = QVBoxLayout(self.phone_clear)
        self.phone_clear_layout.setSpacing(0)
        self.phone_clear_layout.setObjectName(u"phone_clear_layout")
        self.phone_clear_layout.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.phone_clear, 1, 1, 1, 1)

        self.phone_buyme = QFrame(self.phone_button_section)
        self.phone_buyme.setObjectName(u"phone_buyme")
        self.phone_buyme.setMinimumSize(QSize(150, 30))
        self.phone_buyme.setStyleSheet(u"")
        self.phone_buyme.setFrameShape(QFrame.NoFrame)
        self.phone_buyme.setFrameShadow(QFrame.Raised)
        self.phone_buyme_layout = QVBoxLayout(self.phone_buyme)
        self.phone_buyme_layout.setSpacing(0)
        self.phone_buyme_layout.setObjectName(u"phone_buyme_layout")
        self.phone_buyme_layout.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.phone_buyme, 0, 1, 1, 1)

        self.phone_print = QFrame(self.phone_button_section)
        self.phone_print.setObjectName(u"phone_print")
        self.phone_print.setMinimumSize(QSize(150, 30))
        self.phone_print.setStyleSheet(u"")
        self.phone_print.setFrameShape(QFrame.NoFrame)
        self.phone_print.setFrameShadow(QFrame.Raised)
        self.phone_print_layout = QVBoxLayout(self.phone_print)
        self.phone_print_layout.setSpacing(0)
        self.phone_print_layout.setObjectName(u"phone_print_layout")
        self.phone_print_layout.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.phone_print, 0, 2, 1, 1)

        self.remov_from_cart = QFrame(self.phone_button_section)
        self.remov_from_cart.setObjectName(u"remov_from_cart")
        self.remov_from_cart.setMinimumSize(QSize(150, 30))
        self.remov_from_cart.setStyleSheet(u"")
        self.remov_from_cart.setFrameShape(QFrame.NoFrame)
        self.remov_from_cart.setFrameShadow(QFrame.Raised)
        self.remov_from_cart_layout = QVBoxLayout(self.remov_from_cart)
        self.remov_from_cart_layout.setSpacing(0)
        self.remov_from_cart_layout.setObjectName(u"remov_from_cart_layout")
        self.remov_from_cart_layout.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.remov_from_cart, 1, 0, 1, 1)

        self.add_to_cart = QFrame(self.phone_button_section)
        self.add_to_cart.setObjectName(u"add_to_cart")
        self.add_to_cart.setMinimumSize(QSize(150, 30))
        self.add_to_cart.setStyleSheet(u"")
        self.add_to_cart.setFrameShape(QFrame.NoFrame)
        self.add_to_cart.setFrameShadow(QFrame.Raised)
        self.phone_add_to_cart_layout = QVBoxLayout(self.add_to_cart)
        self.phone_add_to_cart_layout.setSpacing(0)
        self.phone_add_to_cart_layout.setObjectName(u"phone_add_to_cart_layout")
        self.phone_add_to_cart_layout.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.add_to_cart, 0, 0, 1, 1)

        self.phone_delete = QFrame(self.phone_button_section)
        self.phone_delete.setObjectName(u"phone_delete")
        self.phone_delete.setMinimumSize(QSize(150, 30))
        self.phone_delete.setStyleSheet(u"")
        self.phone_delete.setFrameShape(QFrame.StyledPanel)
        self.phone_delete.setFrameShadow(QFrame.Raised)
        self.phone_delete_layout = QVBoxLayout(self.phone_delete)
        self.phone_delete_layout.setSpacing(0)
        self.phone_delete_layout.setObjectName(u"phone_delete_layout")
        self.phone_delete_layout.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.phone_delete, 2, 1, 1, 1)

        self.phone_all_in_one = QFrame(self.phone_button_section)
        self.phone_all_in_one.setObjectName(u"phone_all_in_one")
        self.phone_all_in_one.setMinimumSize(QSize(150, 30))
        self.phone_all_in_one.setStyleSheet(u"")
        self.phone_all_in_one.setFrameShape(QFrame.NoFrame)
        self.phone_all_in_one.setFrameShadow(QFrame.Raised)
        self.phone_all_in_one_layout = QVBoxLayout(self.phone_all_in_one)
        self.phone_all_in_one_layout.setSpacing(0)
        self.phone_all_in_one_layout.setObjectName(u"phone_all_in_one_layout")
        self.phone_all_in_one_layout.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.phone_all_in_one, 1, 2, 1, 1)

        self.phone_clear_cart = QFrame(self.phone_button_section)
        self.phone_clear_cart.setObjectName(u"phone_clear_cart")
        self.phone_clear_cart.setMinimumSize(QSize(150, 30))
        self.phone_clear_cart.setStyleSheet(u"")
        self.phone_clear_cart.setFrameShape(QFrame.NoFrame)
        self.phone_clear_cart.setFrameShadow(QFrame.Raised)
        self.phone_clear_cart_layout = QVBoxLayout(self.phone_clear_cart)
        self.phone_clear_cart_layout.setSpacing(0)
        self.phone_clear_cart_layout.setObjectName(u"phone_clear_cart_layout")
        self.phone_clear_cart_layout.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.phone_clear_cart, 2, 0, 1, 1)

        self.frame_12 = QFrame(self.phone_button_section)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 30))
        self.frame_12.setStyleSheet(u"")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.frame_12)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setHorizontalSpacing(0)
        self.formLayout_2.setVerticalSpacing(0)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_23 = QLabel(self.frame_12)
        self.label_23.setObjectName(u"label_23")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_23)

        self.frame_15 = QFrame(self.frame_12)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.NoFrame)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.phone_search_key_edit = QVBoxLayout(self.frame_15)
        self.phone_search_key_edit.setSpacing(0)
        self.phone_search_key_edit.setObjectName(u"phone_search_key_edit")
        self.phone_search_key_edit.setContentsMargins(-1, 0, 0, 0)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.frame_15)


        self.gridLayout.addWidget(self.frame_12, 3, 0, 1, 1)

        self.phone_search = QFrame(self.phone_button_section)
        self.phone_search.setObjectName(u"phone_search")
        self.phone_search.setMinimumSize(QSize(307, 30))
        self.phone_search.setFrameShape(QFrame.NoFrame)
        self.phone_search.setFrameShadow(QFrame.Raised)
        self.phone_search_layout = QVBoxLayout(self.phone_search)
        self.phone_search_layout.setSpacing(0)
        self.phone_search_layout.setObjectName(u"phone_search_layout")
        self.phone_search_layout.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.phone_search, 3, 1, 1, 2)


        self.horizontalLayout_2.addWidget(self.phone_button_section)


        self.verticalLayout_5.addWidget(self.phone_cart_button_section)

        self.phone_table_section = QFrame(self.phone_bg_layout)
        self.phone_table_section.setObjectName(u"phone_table_section")
        sizePolicy.setHeightForWidth(self.phone_table_section.sizePolicy().hasHeightForWidth())
        self.phone_table_section.setSizePolicy(sizePolicy)
        self.phone_table_section.setMinimumSize(QSize(934, 226))
        self.phone_table_section.setMaximumSize(QSize(16777215, 16777215))
        self.phone_table_section.setStyleSheet(u"")
        self.phone_table_section.setFrameShape(QFrame.NoFrame)
        self.phone_table_section.setFrameShadow(QFrame.Raised)
        self.phone_table = QHBoxLayout(self.phone_table_section)
        self.phone_table.setObjectName(u"phone_table")
        self.phone_table.setContentsMargins(0, -1, 0, 0)

        self.verticalLayout_5.addWidget(self.phone_table_section)


        self.verticalLayout_4.addWidget(self.phone_bg_layout)

        self.scrollArea.setWidget(self.contents)

        self.verticalLayout_3.addWidget(self.scrollArea)

        self.pages.addWidget(self.phone_page)
        self.service_page = QWidget()
        self.service_page.setObjectName(u"service_page")
        self.service_page.setStyleSheet(u"font-size: 14pt; background: lightblue; ")
        self.page_2_layout = QVBoxLayout(self.service_page)
        self.page_2_layout.setSpacing(0)
        self.page_2_layout.setObjectName(u"page_2_layout")
        self.page_2_layout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.service_page)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setFrameShape(QFrame.NoFrame)
        self.scrollArea_2.setWidgetResizable(True)
        self.Contents = QWidget()
        self.Contents.setObjectName(u"Contents")
        self.Contents.setGeometry(QRect(0, 0, 1055, 618))
        self.verticalLayout_2 = QVBoxLayout(self.Contents)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.service_bg = QFrame(self.Contents)
        self.service_bg.setObjectName(u"service_bg")
        self.service_bg.setFrameShape(QFrame.NoFrame)
        self.service_bg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.service_bg)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.service_forms_section = QFrame(self.service_bg)
        self.service_forms_section.setObjectName(u"service_forms_section")
        self.service_forms_section.setMinimumSize(QSize(0, 202))
        self.service_forms_section.setMaximumSize(QSize(16777215, 600))
        self.service_forms_section.setStyleSheet(u"background :rgb(255, 188, 19)")
        self.service_forms_section.setFrameShape(QFrame.NoFrame)
        self.service_forms_section.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.service_forms_section)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.service_customer_section = QFrame(self.service_forms_section)
        self.service_customer_section.setObjectName(u"service_customer_section")
        self.service_customer_section.setMaximumSize(QSize(280, 16777215))
        self.service_customer_section.setStyleSheet(u"background :rgb(0, 255, 127)")
        self.service_customer_section.setFrameShape(QFrame.NoFrame)
        self.service_customer_section.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.service_customer_section)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.service_customer_group = QGroupBox(self.service_customer_section)
        self.service_customer_group.setObjectName(u"service_customer_group")
        self.formLayout_4 = QFormLayout(self.service_customer_group)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setHorizontalSpacing(7)
        self.formLayout_4.setVerticalSpacing(7)
        self.formLayout_4.setContentsMargins(10, 0, 10, 0)
        self.label_13 = QLabel(self.service_customer_group)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_13)

        self.frame_11 = QFrame(self.service_customer_group)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"background: rgb(255, 255, 255)")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.frame_11)

        self.label_14 = QLabel(self.service_customer_group)
        self.label_14.setObjectName(u"label_14")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_14)

        self.frame_18 = QFrame(self.service_customer_group)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setStyleSheet(u"background: rgb(255, 255, 255)")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.frame_18)

        self.label_15 = QLabel(self.service_customer_group)
        self.label_15.setObjectName(u"label_15")

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.label_15)

        self.label_30 = QLabel(self.service_customer_group)
        self.label_30.setObjectName(u"label_30")

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.label_30)


        self.verticalLayout_20.addWidget(self.service_customer_group)


        self.horizontalLayout_4.addWidget(self.service_customer_section)

        self.service_phone_section = QFrame(self.service_forms_section)
        self.service_phone_section.setObjectName(u"service_phone_section")
        self.service_phone_section.setMaximumSize(QSize(400, 16777215))
        self.service_phone_section.setStyleSheet(u"background :rgb(170, 170, 127)")
        self.service_phone_section.setFrameShape(QFrame.NoFrame)
        self.service_phone_section.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.service_phone_section)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.service_phon_group = QGroupBox(self.service_phone_section)
        self.service_phon_group.setObjectName(u"service_phon_group")
        self.gridLayout_3 = QGridLayout(self.service_phon_group)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.service_phon_group)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_3.addWidget(self.label_19, 0, 0, 1, 1)

        self.label_22 = QLabel(self.service_phon_group)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_3.addWidget(self.label_22, 0, 3, 1, 1)

        self.label_20 = QLabel(self.service_phon_group)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_3.addWidget(self.label_20, 2, 0, 1, 1)

        self.label_27 = QLabel(self.service_phon_group)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_3.addWidget(self.label_27, 1, 3, 1, 1)

        self.label_26 = QLabel(self.service_phon_group)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_3.addWidget(self.label_26, 2, 3, 1, 1)

        self.label_21 = QLabel(self.service_phon_group)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_3.addWidget(self.label_21, 1, 0, 1, 1)

        self.frame_25 = QFrame(self.service_phon_group)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.frame_25, 0, 2, 1, 1)

        self.frame_30 = QFrame(self.service_phon_group)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.frame_30, 0, 5, 1, 1)

        self.label_28 = QLabel(self.service_phon_group)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_3.addWidget(self.label_28, 3, 0, 1, 1)

        self.frame_17 = QFrame(self.service_phon_group)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.frame_17, 0, 4, 1, 1)

        self.frame_19 = QFrame(self.service_phon_group)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.frame_19, 0, 1, 1, 1)


        self.verticalLayout_22.addWidget(self.service_phon_group)


        self.horizontalLayout_4.addWidget(self.service_phone_section)

        self.service_cost_section = QFrame(self.service_forms_section)
        self.service_cost_section.setObjectName(u"service_cost_section")
        self.service_cost_section.setMaximumSize(QSize(400, 16777215))
        self.service_cost_section.setStyleSheet(u"background :rgb(85, 255, 0)")
        self.service_cost_section.setFrameShape(QFrame.NoFrame)
        self.service_cost_section.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.service_cost_section)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.service_cost_group = QGroupBox(self.service_cost_section)
        self.service_cost_group.setObjectName(u"service_cost_group")

        self.verticalLayout_19.addWidget(self.service_cost_group)


        self.horizontalLayout_4.addWidget(self.service_cost_section)

        self.frame_16 = QFrame(self.service_forms_section)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.frame_16)


        self.verticalLayout_18.addWidget(self.service_forms_section)

        self.service_cart_buttons_section = QFrame(self.service_bg)
        self.service_cart_buttons_section.setObjectName(u"service_cart_buttons_section")
        self.service_cart_buttons_section.setMinimumSize(QSize(0, 202))
        self.service_cart_buttons_section.setMaximumSize(QSize(16777215, 600))
        self.service_cart_buttons_section.setStyleSheet(u"background :rgb(24, 8, 255)")
        self.service_cart_buttons_section.setFrameShape(QFrame.StyledPanel)
        self.service_cart_buttons_section.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.service_cart_buttons_section)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.service_cart_buttons_section)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background: rgb(122, 18, 42)")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.service_cart_buttons_section)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background: rgb(170, 170, 0)")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_6)


        self.verticalLayout_18.addWidget(self.service_cart_buttons_section)

        self.service_table_section = QFrame(self.service_bg)
        self.service_table_section.setObjectName(u"service_table_section")
        self.service_table_section.setMinimumSize(QSize(0, 202))
        self.service_table_section.setMaximumSize(QSize(16777215, 600))
        self.service_table_section.setStyleSheet(u"background : rgb(255, 43, 199)")
        self.service_table_section.setFrameShape(QFrame.StyledPanel)
        self.service_table_section.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.service_table_section)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.frame_7 = QFrame(self.service_table_section)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.verticalLayout_23.addWidget(self.frame_7)


        self.verticalLayout_18.addWidget(self.service_table_section)


        self.verticalLayout_2.addWidget(self.service_bg)

        self.scrollArea_2.setWidget(self.Contents)

        self.page_2_layout.addWidget(self.scrollArea_2)

        self.pages.addWidget(self.service_page)
        self.stock = QWidget()
        self.stock.setObjectName(u"stock")
        self.stock.setStyleSheet(u"background-color:#2c313c;\n"
"/**#2c313c;**/\n"
"")
        self.page_3_layout = QVBoxLayout(self.stock)
        self.page_3_layout.setSpacing(0)
        self.page_3_layout.setObjectName(u"page_3_layout")
        self.page_3_layout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_3 = QScrollArea(self.stock)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setFrameShape(QFrame.NoFrame)
        self.scrollArea_3.setWidgetResizable(True)
        self.stockContents = QWidget()
        self.stockContents.setObjectName(u"stockContents")
        self.stockContents.setGeometry(QRect(0, 0, 1055, 618))
        self.verticalLayout_9 = QVBoxLayout(self.stockContents)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 5, 0, 0)
        self.inventories = QTabWidget(self.stockContents)
        self.inventories.setObjectName(u"inventories")
        self.inventories.setFocusPolicy(Qt.TabFocus)
        self.inventories.setStyleSheet(u"QTabWidget::pane { /* The tab widget frame */\n"
"    border-top: 1px solid #C2C7CB;\n"
"	color: white\n"
"}\n"
"QTabWidget::tab-bar {\n"
"    left: 5px; /* move to the right by 5px */\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background: #1b1e23;\n"
"		font-size: 18px;\n"
"	\n"
"}\n"
"\n"
"")
        self.inventories.setTabPosition(QTabWidget.North)
        self.inventories.setTabShape(QTabWidget.Triangular)
        self.inventories.setElideMode(Qt.ElideNone)
        self.phone_inventory = QWidget()
        self.phone_inventory.setObjectName(u"phone_inventory")
        self.verticalLayout_11 = QVBoxLayout(self.phone_inventory)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 10, 0, 0)
        self.phone_inventory_inner = QTabWidget(self.phone_inventory)
        self.phone_inventory_inner.setObjectName(u"phone_inventory_inner")
        self.phone_inventory_inner.setStyleSheet(u"")
        self.phone_inventory_inner.setTabPosition(QTabWidget.North)
        self.phone_inventory_inner.setTabShape(QTabWidget.Triangular)
        self.detailed = QWidget()
        self.detailed.setObjectName(u"detailed")
        self.phone_inventory_inner.addTab(self.detailed, "")
        self.simple = QWidget()
        self.simple.setObjectName(u"simple")
        self.simple.setFocusPolicy(Qt.StrongFocus)
        self.phone_inventory_inner.addTab(self.simple, "")

        self.verticalLayout_11.addWidget(self.phone_inventory_inner)

        self.inventories.addTab(self.phone_inventory, "")
        self.accessories_inventory = QWidget()
        self.accessories_inventory.setObjectName(u"accessories_inventory")
        self.accessories_inventory.setFocusPolicy(Qt.StrongFocus)
        self.verticalLayout_12 = QVBoxLayout(self.accessories_inventory)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 10, 0, 0)
        self.accessories_inventory_inner = QTabWidget(self.accessories_inventory)
        self.accessories_inventory_inner.setObjectName(u"accessories_inventory_inner")
        self.accessories_inventory_inner.setTabPosition(QTabWidget.North)
        self.accessories_inventory_inner.setTabShape(QTabWidget.Triangular)
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.accessories_inventory_inner.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.accessories_inventory_inner.addTab(self.tab_6, "")

        self.verticalLayout_12.addWidget(self.accessories_inventory_inner)

        self.inventories.addTab(self.accessories_inventory, "")

        self.verticalLayout_9.addWidget(self.inventories)

        self.scrollArea_3.setWidget(self.stockContents)

        self.page_3_layout.addWidget(self.scrollArea_3)

        self.pages.addWidget(self.stock)

        self.main_pages_layout.addWidget(self.pages)


        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(1)
        self.inventories.setCurrentIndex(0)
        self.phone_inventory_inner.setCurrentIndex(0)
        self.accessories_inventory_inner.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.label.setText(QCoreApplication.translate("MainPages", u"HOME PAGE", None))
        self.customer_group.setTitle(QCoreApplication.translate("MainPages", u"Customer | Cart", None))
        self.label_3.setText(QCoreApplication.translate("MainPages", u"Name :", None))
        self.label_2.setText(QCoreApplication.translate("MainPages", u"Contact :", None))
        self.label_4.setText(QCoreApplication.translate("MainPages", u"Cart id", None))
        self.label_25.setText(QCoreApplication.translate("MainPages", u"total Cart", None))
        self.phone_group.setTitle(QCoreApplication.translate("MainPages", u"Phone", None))
        self.label_7.setText(QCoreApplication.translate("MainPages", u"Imei / meid :", None))
        self.label_6.setText(QCoreApplication.translate("MainPages", u"Model :", None))
        self.label_5.setText(QCoreApplication.translate("MainPages", u"Type :", None))
        self.label_8.setText(QCoreApplication.translate("MainPages", u"SN :", None))
        self.label_18.setText(QCoreApplication.translate("MainPages", u"Qty", None))
        self.label_16.setText(QCoreApplication.translate("MainPages", u"Read Bar/QR ", None))
        self.label_17.setText(QCoreApplication.translate("MainPages", u".....................................", None))
        self.cost_group.setTitle(QCoreApplication.translate("MainPages", u"Cost", None))
        self.label_9.setText(QCoreApplication.translate("MainPages", u"Price :", None))
        self.label_10.setText(QCoreApplication.translate("MainPages", u"discount :", None))
        self.label_11.setText(QCoreApplication.translate("MainPages", u"tax :", None))
        self.label_12.setText(QCoreApplication.translate("MainPages", u"paymant :", None))
        self.label_23.setText(QCoreApplication.translate("MainPages", u"Search :", None))
        self.service_customer_group.setTitle(QCoreApplication.translate("MainPages", u"Customer", None))
        self.label_13.setText(QCoreApplication.translate("MainPages", u"Name : ", None))
        self.label_14.setText(QCoreApplication.translate("MainPages", u"contact :", None))
        self.label_15.setText(QCoreApplication.translate("MainPages", u"Email", None))
        self.label_30.setText(QCoreApplication.translate("MainPages", u"Next of kin", None))
        self.service_phon_group.setTitle(QCoreApplication.translate("MainPages", u"GroupBox", None))
        self.label_19.setText(QCoreApplication.translate("MainPages", u"Type:", None))
        self.label_22.setText(QCoreApplication.translate("MainPages", u"Model:", None))
        self.label_20.setText(QCoreApplication.translate("MainPages", u"imei/meid", None))
        self.label_27.setText(QCoreApplication.translate("MainPages", u"repairer", None))
        self.label_26.setText(QCoreApplication.translate("MainPages", u"SN", None))
        self.label_21.setText(QCoreApplication.translate("MainPages", u"Fault ", None))
        self.label_28.setText(QCoreApplication.translate("MainPages", u"state", None))
        self.service_cost_group.setTitle(QCoreApplication.translate("MainPages", u"GroupBox", None))
        self.phone_inventory_inner.setTabText(self.phone_inventory_inner.indexOf(self.detailed), QCoreApplication.translate("MainPages", u"Detailed ", None))
        self.phone_inventory_inner.setTabText(self.phone_inventory_inner.indexOf(self.simple), QCoreApplication.translate("MainPages", u"Simple", None))
        self.inventories.setTabText(self.inventories.indexOf(self.phone_inventory), QCoreApplication.translate("MainPages", u"PHONE", None))
#if QT_CONFIG(tooltip)
        self.inventories.setTabToolTip(self.inventories.indexOf(self.phone_inventory), QCoreApplication.translate("MainPages", u"tho sodn dikd", None))
#endif // QT_CONFIG(tooltip)
        self.accessories_inventory_inner.setTabText(self.accessories_inventory_inner.indexOf(self.tab_5), QCoreApplication.translate("MainPages", u"Detailed", None))
        self.accessories_inventory_inner.setTabText(self.accessories_inventory_inner.indexOf(self.tab_6), QCoreApplication.translate("MainPages", u"Simple", None))
        self.inventories.setTabText(self.inventories.indexOf(self.accessories_inventory), QCoreApplication.translate("MainPages", u"Accesssories", None))
    # retranslateUi

