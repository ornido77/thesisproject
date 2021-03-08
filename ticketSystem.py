import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                          QSize, QTime, QUrl, Qt, QEvent, QSizeF)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                         QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient, QIntValidator, QTextDocument)
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog
from PyQt5.QtWidgets import *
import sqlite3

# GUI FILE
from ticket import *

# IMPORT FUNCTIONS
from ticketFunction import *
checkup = 1
vaccine = 1
dental = 1
priority = 1
checkup1 = 0
vaccine1 = 0
dental1 = 0
priority1 = 0
now = QDate.currentDate()
date = now.toString()
time = QTime.currentTime()
timenow = time.toString()


class realMainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # MOVE WINDOW
        def moveWindow(event):
            # RESTORE BEFORE MOVE
            if UIFunctions.returnStatus() == 1:
                UIFunctions.maximize_restore(self)

            # IF LEFT CLICK MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # SET TITLE BAR
        self.ui.frame_title_bar.mouseMoveEvent = moveWindow

        ## ==> SET UI DEFINITIONS
        UIFunctions.uiDefinitions(self)



        self.ui.checkUpBtn.clicked.connect(self.printCuTicket)
        self.ui.checkUpBtn.clicked.connect(self.cuIncre)
        self.ui.vaccineBtn.clicked.connect(self.printVcTicket)
        self.ui.vaccineBtn.clicked.connect(self.vcIncre)
        self.ui.dentalBtn.clicked.connect(self.printDtTicket)
        self.ui.dentalBtn.clicked.connect(self.dtIncre)
        self.ui.priorityBtn.clicked.connect(self.printPtTicket)
        self.ui.priorityBtn.clicked.connect(self.ptIncre)
        self.btn1 = QShortcut(QKeySequence('c'), self)
        self.btn1.activated.connect(self.cprint_preview_dialog)
        self.btn2 = QShortcut(QKeySequence('v'), self)
        self.btn2.activated.connect(self.vprint_preview_dialog)
        self.btn3 = QShortcut(QKeySequence('d'), self)
        self.btn3.activated.connect(self.dprint_preview_dialog)
        self.btn4 = QShortcut(QKeySequence('p'), self)
        self.btn4.activated.connect(self.pprint_preview_dialog)

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        self.ui.cuTicket.setText(str(self.ui.label.text()) + "\nTicket Number: C"+ str(checkup) + "\nService: Check Up" + "\nDate and Time: "+ str(date) + " " + str(timenow))
        self.ui.vcTicket.setText(str(self.ui.label.text()) + "\nTicket Number: V"+ str(checkup) + "\nService: Vaccine" + "\nDate and Time: "+ str(date) + " " + str(timenow))
        self.ui.dtTicket.setText(str(self.ui.label.text()) + "\nTicket Number: D"+ str(checkup) + "\nService: Dental" + "\nDate and Time: "+ str(date) + " " + str(timenow))
        self.ui.ptTicket.setText(str(self.ui.label.text()) + "\nTicket Number: P"+ str(checkup) + "\nPriority" + "\nDate and Time: "+ str(date) + " " + str(timenow))
        self.ui.dateTime.setText(now.toString())
        self.ui.cuTicket1.setText(str(checkup1))
        self.ui.vcTicket1.setText(str(vaccine1))
        self.ui.dtTicket1.setText(str(dental1))
        self.ui.ptTicket1.setText(str(priority1))


    ## APP EVENTS
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def printCuTicket(self):
        printer = QPrinter(QPrinter.HighResolution)
        printer.setOrientation(QPrinter.Landscape)
        printer.setPageSize(QPrinter.A7)
        dialog = QPrintDialog(printer, self)

        if dialog.exec_() == QPrintDialog.Accepted:
            self.ui.cuTicket.print_(printer)
    def printVcTicket(self):
        printer = QPrinter(QPrinter.HighResolution)
        printer.setOrientation(QPrinter.Landscape)
        printer.setPageSize(QPrinter.A7)
        dialog = QPrintDialog(printer, self)

        if dialog.exec_() == QPrintDialog.Accepted:
            self.ui.vcTicket.print_(printer)
    def printDtTicket(self):
        printer = QPrinter(QPrinter.HighResolution)
        printer.setOrientation(QPrinter.Landscape)
        printer.setPageSize(QPrinter.A7)
        dialog = QPrintDialog(printer, self)

        if dialog.exec_() == QPrintDialog.Accepted:
            self.ui.dtTicket.print_(printer)
    def printPtTicket(self):
        printer = QPrinter(QPrinter.HighResolution)
        printer.setOrientation(QPrinter.Landscape)
        printer.setPageSize(QPrinter.A7)
        dialog = QPrintDialog(printer, self)

        if dialog.exec_() == QPrintDialog.Accepted:
            self.ui.ptTicket.print_(printer)
### INCREMENT
    def cuIncre(self):
        global checkup, checkup1
        checkup += 1
        checkup1 += 1
        self.ui.cuTicket.setText(str(self.ui.label.text()) + "\nTicket Number: C"+ str(checkup) + "\nService: Check Up" + "\nDate and Time: "+ str(date) + " " + str(timenow))
        self.ui.cuTicket1.setText("C" + str(checkup1))
    def vcIncre(self):
        global vaccine, vaccine1
        vaccine += 1
        vaccine1 += 1
        self.ui.vcTicket.setText(str(self.ui.label.text()) + "\nTicket Number: V"+ str(vaccine) + "\nService: Vaccine" + "\nDate and Time: "+ str(date) + " " + str(timenow))
        self.ui.vcTicket1.setText("V" + str(vaccine1))
    def dtIncre(self):
        global dental, dental1
        dental += 1
        dental1 += 1
        self.ui.dtTicket.setText(str(self.ui.label.text()) + "\nTicket Number: D"+ str(dental) + "\nService: Dental" + "\nDate and Time: "+ str(date) + " " + str(timenow))
        self.ui.dtTicket1.setText("D" + str(dental1))
    def ptIncre(self):
        global priority, priority1
        priority += 1
        priority1
        self.ui.ptTicket.setText(str(self.ui.label.text()) + "\nTicket Number: P"+ str(priority) + "\nService: Priority" + "\nDate and Time: "+ str(date) + " " + str(timenow))
        self.ui.ptTicket1.setText("P" + str(priority1))

### PREVIEW
    def cprint_preview_dialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        printer.setOrientation(QPrinter.Landscape)
        printer.setPageSize(QPrinter.A7)
        previewDialog = QPrintPreviewDialog(printer, self)
        previewDialog.paintRequested.connect(self.cprint_preview)
        previewDialog.exec()

    def cprint_preview(self, printer):
        self.ui.cuTicket.print_(printer)

    def vprint_preview_dialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        printer.setOrientation(QPrinter.Landscape)
        printer.setPageSize(QPrinter.A7)
        previewDialog = QPrintPreviewDialog(printer, self)
        previewDialog.paintRequested.connect(self.vprint_preview)
        previewDialog.exec()

    def vprint_preview(self, printer):
        self.ui.vcTicket.print_(printer)

    def dprint_preview_dialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        printer.setOrientation(QPrinter.Landscape)
        printer.setPageSize(QPrinter.A7)
        previewDialog = QPrintPreviewDialog(printer, self)
        previewDialog.paintRequested.connect(self.dprint_preview)
        previewDialog.exec()

    def dprint_preview(self, printer):
        self.ui.dtTicket.print_(printer)

    def pprint_preview_dialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        printer.setOrientation(QPrinter.Landscape)
        printer.setPageSize(QPrinter.A7)
        previewDialog = QPrintPreviewDialog(printer, self)
        previewDialog.paintRequested.connect(self.pprint_preview)
        previewDialog.exec()

    def pprint_preview(self, printer):
        self.ui.ptTicket.print_(printer)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = realMainWindow()
    try:
        sys.exit(app.exec_())
    except:
        print("EXITING SYSTEM")

