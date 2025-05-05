from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(515, 425)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 491, 401))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.back_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.back_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.back_btn.setMaximumSize(QtCore.QSize(16777215, 40))
        self.back_btn.setObjectName("back_btn")
        self.horizontalLayout.addWidget(self.back_btn)
        self.path_edit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.path_edit.setMinimumSize(QtCore.QSize(0, 40))
        self.path_edit.setMaximumSize(QtCore.QSize(16777215, 40))
        self.path_edit.setObjectName("path_edit")
        self.horizontalLayout.addWidget(self.path_edit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.listWidget = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "文件浏览器"))
        self.back_btn.setText(_translate("Form", "&lt;-"))
