# -*- coding: utf-8 -*-
import opchelper
import re
import datetime
from opcua import Client
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # url_group
        self.url_group = QGroupBox('URL')
        self.url_le = QLineEdit()
        self.url_le.setPlaceholderText('ex) opc.tcp://000.000.000.000:51235') 
        self.url_le.setFocus()
        # nodeid_group
        self.nodeid_group = QGroupBox('NodeId')
        self.nodeid_le = QLineEdit()
        self.nodeid_le.setPlaceholderText('ex) ns=12;i=100,ns=12;i=101')
        # search_group
        self.search_group = QGroupBox('Search')
        self.search_label = QLabel('Type:')
        self.search_cb = QComboBox()
        self.search_cb.addItem('current')
        self.search_cb.addItem('history')

        self.search_stdt_label = QLabel('start time:')
        self.search_stdt = QDateTimeEdit(self)
        self.search_stdt.setDateTime(datetime.datetime.now() - datetime.timedelta(hours=1))
        self.search_stdt.setDateTimeRange(datetime.datetime(2015, 1, 1, 00, 00, 00), datetime.datetime.now() + datetime.timedelta(days=1))
        self.search_stdt.setDisplayFormat('yyyy.MM.dd hh:mm:ss')

        self.search_enddt_label = QLabel('end time:')
        self.search_enddt = QDateTimeEdit(self)
        self.search_enddt.setDateTime(datetime.datetime.now())
        self.search_enddt.setDateTimeRange(datetime.datetime(2015, 1, 1, 00, 00, 00), datetime.datetime.now() + datetime.timedelta(days=1))
        self.search_enddt.setDisplayFormat('yyyy.MM.dd hh:mm:ss')

        self.search_stdt.setDisabled(True)
        self.search_enddt.setDisabled(True)
        self.search_stdt.setReadOnly(True)
        self.search_enddt.setReadOnly(True)

        self.search_btn = QPushButton('Search', self)
        self.search_btn.clicked.connect(self.search)

        # activated.connect
        self.search_cb.activated.connect(self.search_changed)

        # url_layout
        self.url_layout = QGridLayout()
        self.url_layout.addWidget(self.url_le, 0, 0)
        self.url_group.setLayout(self.url_layout)

        # nodeid_layout
        self.nodeid_layout = QGridLayout()
        self.nodeid_layout.addWidget(self.nodeid_le, 0, 0)
        self.nodeid_group.setLayout(self.nodeid_layout)

        # search_layout
        self.search_layout = QGridLayout()
        self.search_layout.addWidget(self.search_label, 0, 0)
        self.search_layout.addWidget(self.search_cb, 0, 1)
        self.search_layout.addWidget(self.search_stdt_label, 1, 0)
        self.search_layout.addWidget(self.search_stdt, 1, 1, 1, 2)
        self.search_layout.addWidget(self.search_enddt_label, 1, 4)
        self.search_layout.addWidget(self.search_enddt, 1, 5, 1, 2)
        self.search_layout.addWidget(self.search_btn, 0, 5, 1, 2)
        self.search_group.setLayout(self.search_layout)
        
        # layout
        self.layout = QGridLayout()
        self.layout.addWidget(self.url_group, 0, 0)
        self.layout.addWidget(self.nodeid_group, 1, 0)
        self.layout.addWidget(self.search_group, 2, 0)

        self.te = QTextEdit()
        self.te.setAcceptRichText(True)
        self.layout.addWidget(self.te, 3, 0, 5, 0)
        #self.layout.addWidget(self.serch_btn_group,1, 1)
        
        self.setLayout(self.layout)

        # Application Icon
        self.setWindowTitle('OPC UA Client')
        self.setWindowIcon(QIcon('icon.ico'))

        # Windows location, scale
        self.resize(500, 450)
        
        self.center()
        
        self.show()

    def search(self):
        url = self.url_le.text()      
        nodeid = self.nodeid_le.text()
        
        #URL 정규표현식
        url_regex = re.compile(r"opc\.tcp:\/\/([^:]+):?(\d*)\/?(.*)")
        match = url_regex.match(url)
        if(match == None):
            self.te.setText("Please enter a valid URL.")
            return
        
        #NodeId 정규표현식
        if "ns=" not in nodeid or ";i=" not in nodeid :
            self.te.setText("Please enter a valid NodeId.")
            return

        if ',' in nodeid:
            nodeid = nodeid.split(',')

        # OPC UA Server connect
        client = Client(url)
        client.connect()

        if self.search_cb.currentIndex() == 0:
            if type(nodeid) == str:            
                rtnVal = opchelper.get_current_node_value(client, nodeid)
            else:
                rtnVal = opchelper.get_current_nodes_values(client, nodeid)
        else:
            stdt = self.search_stdt.dateTime().toPyDateTime()
            enddt = self.search_enddt.dateTime().toPyDateTime()
            if type(nodeid) == str:            
                rtnVal = opchelper.get_histroy_node_value(client, nodeid, stdt, enddt)
            else:
                rtnVal = opchelper.get_history_nodes_values(client, nodeid, stdt, enddt)
        self.te.setText(rtnVal)
        # OPC UA Server disconnect
        client.disconnect()

    def search_changed(self, index):
        if index == 0:
            self.search_stdt.setReadOnly(True)
            self.search_stdt.setReadOnly(True)
            self.search_stdt.setDisabled(True)
            self.search_enddt.setDisabled(True)
        elif index == 1:
            self.search_stdt.setReadOnly(False)     
            self.search_enddt.setReadOnly(False)     
            self.search_stdt.setDisabled(False)
            self.search_enddt.setDisabled(False)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())