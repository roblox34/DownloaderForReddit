# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Resources\ui_files\widgets\object_info_widget.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ObjectInfoWidget(object):
    def setupUi(self, ObjectInfoWidget):
        ObjectInfoWidget.setObjectName("ObjectInfoWidget")
        ObjectInfoWidget.resize(354, 361)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(ObjectInfoWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.info_form = QtWidgets.QFormLayout()
        self.info_form.setObjectName("info_form")
        self.label = QtWidgets.QLabel(ObjectInfoWidget)
        self.label.setObjectName("label")
        self.info_form.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(ObjectInfoWidget)
        self.label_2.setObjectName("label_2")
        self.info_form.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(ObjectInfoWidget)
        self.label_3.setObjectName("label_3")
        self.info_form.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(ObjectInfoWidget)
        self.label_4.setObjectName("label_4")
        self.info_form.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(ObjectInfoWidget)
        self.label_5.setObjectName("label_5")
        self.info_form.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.name_label = QtWidgets.QLabel(ObjectInfoWidget)
        self.name_label.setObjectName("name_label")
        self.info_form.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.name_label)
        self.id_label = QtWidgets.QLabel(ObjectInfoWidget)
        self.id_label.setObjectName("id_label")
        self.info_form.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.id_label)
        self.date_created_label = QtWidgets.QLabel(ObjectInfoWidget)
        self.date_created_label.setObjectName("date_created_label")
        self.info_form.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.date_created_label)
        self.date_added_label = QtWidgets.QLabel(ObjectInfoWidget)
        self.date_added_label.setObjectName("date_added_label")
        self.info_form.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.date_added_label)
        self.last_download_label = QtWidgets.QLabel(ObjectInfoWidget)
        self.last_download_label.setObjectName("last_download_label")
        self.info_form.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.last_download_label)
        self.label_27 = QtWidgets.QLabel(ObjectInfoWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.info_form.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_27)
        self.verticalLayout.addLayout(self.info_form)
        self.line = QtWidgets.QFrame(ObjectInfoWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.download_info_form = QtWidgets.QFormLayout()
        self.download_info_form.setObjectName("download_info_form")
        self.label_6 = QtWidgets.QLabel(ObjectInfoWidget)
        self.label_6.setObjectName("label_6")
        self.download_info_form.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.post_count_label = QtWidgets.QLabel(ObjectInfoWidget)
        self.post_count_label.setObjectName("post_count_label")
        self.download_info_form.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.post_count_label)
        self.label_8 = QtWidgets.QLabel(ObjectInfoWidget)
        self.label_8.setObjectName("label_8")
        self.download_info_form.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.associated_comment_count_label = QtWidgets.QLabel(ObjectInfoWidget)
        self.associated_comment_count_label.setObjectName("associated_comment_count_label")
        self.download_info_form.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.associated_comment_count_label)
        self.label_26 = QtWidgets.QLabel(ObjectInfoWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.download_info_form.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_26)
        self.label_10 = QtWidgets.QLabel(ObjectInfoWidget)
        self.label_10.setObjectName("label_10")
        self.download_info_form.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.content_count_label = QtWidgets.QLabel(ObjectInfoWidget)
        self.content_count_label.setObjectName("content_count_label")
        self.download_info_form.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.content_count_label)
        self.comment_author_label = QtWidgets.QLabel(ObjectInfoWidget)
        self.comment_author_label.setObjectName("comment_author_label")
        self.download_info_form.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.comment_author_label)
        self.comment_author_count_label = QtWidgets.QLabel(ObjectInfoWidget)
        self.comment_author_count_label.setObjectName("comment_author_count_label")
        self.download_info_form.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.comment_author_count_label)
        self.verticalLayout.addLayout(self.download_info_form)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(ObjectInfoWidget)
        QtCore.QMetaObject.connectSlotsByName(ObjectInfoWidget)

    def retranslateUi(self, ObjectInfoWidget):
        _translate = QtCore.QCoreApplication.translate
        ObjectInfoWidget.setWindowTitle(_translate("ObjectInfoWidget", "Info"))
        self.label.setText(_translate("ObjectInfoWidget", "Name:"))
        self.label_2.setText(_translate("ObjectInfoWidget", "Id:"))
        self.label_3.setText(_translate("ObjectInfoWidget", "Date Created:"))
        self.label_4.setText(_translate("ObjectInfoWidget", "Date Added:"))
        self.label_5.setText(_translate("ObjectInfoWidget", "Last Download:"))
        self.name_label.setText(_translate("ObjectInfoWidget", "name"))
        self.id_label.setText(_translate("ObjectInfoWidget", "0"))
        self.date_created_label.setText(_translate("ObjectInfoWidget", "date_created"))
        self.date_added_label.setText(_translate("ObjectInfoWidget", "date_added"))
        self.last_download_label.setText(_translate("ObjectInfoWidget", "last_download"))
        self.label_27.setText(_translate("ObjectInfoWidget", "Basic Info:"))
        self.label_6.setText(_translate("ObjectInfoWidget", "Post Count:"))
        self.post_count_label.setText(_translate("ObjectInfoWidget", "post_count"))
        self.label_8.setToolTip(_translate("ObjectInfoWidget", "Number of comments made to posts extracted\n"
"on this objects behalf"))
        self.label_8.setText(_translate("ObjectInfoWidget", "Associated Comment:"))
        self.associated_comment_count_label.setToolTip(_translate("ObjectInfoWidget", "Number of comments made to posts extracted\n"
"on this objects behalf"))
        self.associated_comment_count_label.setText(_translate("ObjectInfoWidget", "comment_count"))
        self.label_26.setText(_translate("ObjectInfoWidget", "Download Info:"))
        self.label_10.setText(_translate("ObjectInfoWidget", "Content Count:"))
        self.content_count_label.setText(_translate("ObjectInfoWidget", "content_count"))
        self.comment_author_label.setToolTip(_translate("ObjectInfoWidget", "Comments made by this user"))
        self.comment_author_label.setText(_translate("ObjectInfoWidget", "Comment Author Count:"))
        self.comment_author_count_label.setToolTip(_translate("ObjectInfoWidget", "Comments made by this user"))
        self.comment_author_count_label.setText(_translate("ObjectInfoWidget", "comment_count"))
