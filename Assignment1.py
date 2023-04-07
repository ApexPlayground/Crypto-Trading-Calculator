# Name: Divine Eboigbe
# Date: 12/10/2022
# Student_No: 3046155


import sys

from datetime import date

from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QLabel, QComboBox, QCalendarWidget, QDialog, QApplication, QGridLayout, QSpinBox, \
    QMessageBox, QDoubleSpinBox
from PyQt6 import QtCore, QtWidgets, QtGui
from decimal import Decimal


class CryptoTradeProfitCalculator(QDialog):

    def __init__(self):
        super().__init__()

        # setting up dictionary of Crypto Coins

        self.profit = None
        self.sTotal = None
        self.pTotal = None
        self.data = self.make_data()
        # sorting the dictionary of Crypto Coins by the keys which is date.

        self.cryptoCurrencies = sorted(self.data.keys())

        self.dates = sorted(self.data.keys())

        print("the close price for BTC on 04/29/2013", self.data['BTC'][QDate(2019, 4, 29)])

        self.sellCalendarDefaultDate = sorted(self.data['BTC'].keys())[-1]

        print("self.sellCalendarStartDate", self.sellCalendarDefaultDate)

        self.center()  # displaying widow to center of the screen

        # setting the window title
        self.setWindowTitle("Crypto Profit Calculator")

        # adding icon
        self.setWindowIcon(QtGui.QIcon('Asset\calculator.png'))

        grid = QGridLayout()  # Setting layout to grid
        grid.setSpacing(15)  # setting spacing to 15

        # Selecting cryptocurrency
        cryptoLabel = QLabel("Cryptocurrency Purchased: ")  # LABEL FOR SELECTING CRYPTO

        # creating a combobox and adding the crypto to the combobox from the csv file
        self.cryptoSelect = QComboBox()
        self.cryptoSelect.addItems(self.cryptoCurrencies)

        # positioning cryptoLabel and cryptoSelect combobox
        grid.addWidget(cryptoLabel, 0, 0)
        grid.addWidget(self.cryptoSelect, 0, 1, 1, 2)

        # Label for quantity Purchased
        self.amount = QLabel("Quantity Purchased: ")

        # creating spin box
        self.quantitySelector = QDoubleSpinBox(self)
        self.quantitySelector.setRange(0.01, 100000000.00)
        self.quantitySelector.setValue(1.00000)

        # positioning amount label and quantity spinbox
        grid.addWidget(self.amount, 1, 0)
        grid.addWidget(self.quantitySelector, 1, 1, 1, 2)

        # Adding the calendar widget with purchase and sell total
        self.Purchase = QLabel("Purchase Date: ")  # label for purchase date

        # QCalenderWidget for purchase date is created
        self.calendar1 = QCalendarWidget(self)
        self.calendar1.setGridVisible(True)

        # sell date label
        self.Sell = QLabel("Sell Date: ")  # label for sell date

        # QCalenderWidget for the sell date is created
        self.calendar2 = QCalendarWidget(self)
        self.calendar2.setGridVisible(True)

        # Date Range
        min_date = QDate(2013, 4, 29)
        max_date = QDate(2021, 7, 6)

        # self.calendar1.setSelectedDate(min_date)
        self.calendar1.setDateRange(min_date, max_date)
        self.calendar2.setDateRange(min_date, max_date)

        # assigning selected date to variable
        self.selected_date1 = self.calendar1.selectedDate()
        self.selected_date2 = self.calendar2.selectedDate()

        # label for purchase total
        self.purchaseTotalLabel = QLabel("Purchase Total:")
        # empty label to store the gotten purchase total
        self.purchaseTotal = QLabel("")

        # label for sell total
        self.sellTotalLabel = QLabel("Sell Total:")  # label for sell total
        # empty label to store the gotten sell total
        self.sellTotal = QLabel("")

        # label for profit total
        self.profitTotalLabel = QLabel("Profit Total: ")  # label for profit total
        # empty label to store the gotten profit total
        self.profitTotal = QLabel("")

        self.messageLabel = QLabel("Message")
        self.Pmessage = QLabel("")

        # positioning the calendar widget
        grid.addWidget(self.Purchase, 2, 0)  # positioning the purchase calendar  label
        grid.addWidget(self.calendar1, 2, 1)  # positioning the  purchase calendar widget

        grid.addWidget(self.purchaseTotalLabel, 3, 0)  # positioning the purchase total  label

        grid.addWidget(self.purchaseTotal, 3, 1)  # positioning the purchase total

        grid.addWidget(self.Sell, 2, 2)  # positioning the sel calendar the label
        grid.addWidget(self.calendar2, 2, 3)  # positioning the sell calendar  widget

        grid.addWidget(self.sellTotalLabel, 4, 0)  # positioning the sell total  label

        grid.addWidget(self.sellTotal, 4, 1)  # positioning the sell total

        grid.addWidget(self.profitTotalLabel, 5, 0)  # positioning the profit total  label

        grid.addWidget(self.profitTotal, 5, 1)  # positioning the profit total

        grid.addWidget(self.Pmessage, 6, 3, 1, 6)  # positioning the message

        self.setLayout(grid)  # setting layout to grid

        # Connecting signals to updateUI
        self.cryptoSelect.currentIndexChanged.connect(self.updateUi)
        self.quantitySelector.valueChanged.connect(self.updateUi)
        self.calendar1.clicked[QDate].connect(self.updateUi)
        self.calendar2.clicked[QDate].connect(self.updateUi)

        self.resize(550, 450)

    def updateUi(self):
        """
        This requires substantial development
        Updates the Ui when control values are changed, should also be called when the app initializes
        :return:
        """
        try:

            print("Update UI")
            print(
                self.data[self.cryptoSelect.currentText()][QDate(self.selected_date1)] * self.quantitySelector.value())
            print(self.calendar1.selectedDate().toString("dd/MM/yyyy"))
            print(self.calendar2.selectedDate().toString("yyyy/MM/dd"))

            # TODO: get selected dates from calendars
            # Condition to get starting date and update calendar for each crypto currency
            if self.cryptoSelect.currentText() == "AAVE":
                self.calendar1.setMinimumDate(QDate(2020, 10, 5))
                self.calendar2.setMinimumDate(QDate(self.calendar1.selectedDate()))
            if self.cryptoSelect.currentText() == "BNB":
                self.calendar1.setMinimumDate(QDate(2017, 7, 26))
                self.calendar2.setMinimumDate(QDate(self.calendar1.selectedDate()))
            if self.cryptoSelect.currentText() == "BTC":
                self.calendar1.setMinimumDate(QDate(2013, 4, 29))
                self.calendar2.setMinimumDate(QDate(self.calendar1.selectedDate()))
            if self.cryptoSelect.currentText() == "ADA":
                self.calendar1.setMinimumDate(QDate(2017, 10, 2))
                self.calendar2.setMinimumDate(QDate(self.calendar1.selectedDate()))
            if self.cryptoSelect.currentText() == "LINK":
                self.calendar1.setMinimumDate(QDate(2017, 9, 21))
                self.calendar2.setMinimumDate(QDate(self.calendar1.selectedDate()))
            if self.cryptoSelect.currentText() == "ATOM":
                self.calendar1.setMinimumDate(QDate(2019, 3, 15))
                self.calendar2.setMinimumDate(QDate(self.calendar1.selectedDate()))
            if self.cryptoSelect.currentText() == "CRO":
                self.calendar1.setMinimumDate(QDate(2018, 12, 15))
                self.calendar2.setMinimumDate(QDate(self.calendar1.selectedDate()))
            if self.cryptoSelect.currentText() == "DOGE":
                self.calendar1.setMinimumDate(QDate(2013, 12, 16))
                self.calendar2.setMinimumDate(QDate(self.calendar1.selectedDate()))
            if self.cryptoSelect.currentText() == "EOS":
                self.calendar1.setMinimumDate(QDate(2017, 7, 2))
                self.calendar2.setMinimumDate(QDate(self.calendar1.selectedDate()))
            if self.cryptoSelect.currentText() == "ETH":
                self.calendar1.setMinimumDate(QDate(2015, 8, 8))
                self.calendar2.setMinimumDate(QDate(self.calendar1.selectedDate()))
            if self.cryptoSelect.currentText() == "MIOTA":
                self.calendar1.setMinimumDate(QDate(2017, 6, 14))
                self.calendar2.setMinimumDate(QDate(self.calendar1.selectedDate()))
            if self.cryptoSelect.currentText() == "LTC":
                self.calendar1.setMinimumDate(QDate(2013, 4, 29))
                self.calendar2.setMinimumDate(QDate(self.calendar1.selectedDate()))
            if self.cryptoSelect.currentText() == "XMR":
                self.calendar1.setMinimumDate(QDate(2014, 5, 22))
                self.calendar2.setMinimumDate(QDate(self.calendar1.selectedDate()))
            if self.cryptoSelect.currentText() == "XEM":
                self.calendar1.setMinimumDate(QDate(2015, 4, 2))
                self.calendar2.setMinimumDate(QDate(self.calendar1.selectedDate()))
            if self.cryptoSelect.currentText() == "DOT":
                self.calendar1.setMinimumDate(QDate(2020, 8, 21))
                self.calendar2.setMinimumDate(QDate(self.calendar1.selectedDate()))
            if self.cryptoSelect.currentText() == "SOL":
                self.calendar1.setMinimumDate(QDate(2020, 4, 11))
                self.calendar2.setMinimumDate(QDate(self.calendar1.selectedDate()))
            if self.cryptoSelect.currentText() == "XLM":
                self.calendar1.setMinimumDate(QDate(2014, 8, 6))
                self.calendar2.setMinimumDate(QDate(self.calendar1.selectedDate()))
            if self.cryptoSelect.currentText() == "USDT":
                self.calendar1.setMinimumDate(QDate(2015, 2, 26))
                self.calendar2.setMinimumDate(QDate(self.calendar1.selectedDate()))
            if self.cryptoSelect.currentText() == "TRX":
                self.calendar1.setMinimumDate(QDate(2017, 9, 14))
                self.calendar2.setMinimumDate(QDate(self.calendar1.selectedDate()))
            if self.cryptoSelect.currentText() == "USDC":
                self.calendar1.setMinimumDate(QDate(2018, 10, 9))
                self.calendar2.setMinimumDate(QDate(self.calendar1.selectedDate()))
            if self.cryptoSelect.currentText() == "UNI":
                self.calendar1.setMinimumDate(QDate(2020, 9, 18))
                self.calendar2.setMinimumDate(QDate(self.calendar1.selectedDate()))
            if self.cryptoSelect.currentText() == "WBTC":
                self.calendar1.setMinimumDate(QDate(2019, 1, 31))
                self.calendar2.setMinimumDate(QDate(self.calendar1.selectedDate()))
            if self.cryptoSelect.currentText() == "XRP":
                self.calendar1.setMinimumDate(QDate(2013, 8, 5))
                self.calendar2.setMinimumDate(QDate(self.calendar1.selectedDate()))

            # TODO: perform necessary calculations to calculate totals
            # calculating the purchase total
            self.pTotal = round(self.data[self.cryptoSelect.currentText()][
                                    QDate(self.calendar1.selectedDate())] * self.quantitySelector.value(), 2)

            # calculating the sell total
            self.sTotal = round(self.data[self.cryptoSelect.currentText()][
                                    QDate(self.calendar2.selectedDate())] * self.quantitySelector.value(), 2)

            # calculating the profit total
            self.profit = round(self.sTotal - self.pTotal, 2)

            # EXTRA FEATURE
            # congratulate use if trade is successfully if not, it links user to learning resources about trading
            if self.profit < 0:
                self.Pmessage.setText(
                    "Sorry for you loss checkout " '<a href="https://www.youtube.com/results?search_query=tips+on+cryptocurrency'
                    '+trading">Link</a>' " for more tips on trading ")
                self.Pmessage.setOpenExternalLinks(True)

            else:
                self.Pmessage.setText("Congratulation you made a profit on your investment")

            # TODO: update the label displaying totals
            # Displaying all the totals
            self.purchaseTotal.setText(str(self.pTotal))
            self.sellTotal.setText(str(self.sTotal))
            self.profitTotal.setText(str(self.profit))



        except Exception as e:
            print(e)

    def make_data(self):

        data = {}  # empty data dictionary (will store what we read from the file here)
        try:
            file = open(".//combined.csv", "r")  # open a CSV file for reading
            # https://docs.python.org/3/library/functions.html#open
            file_rows = []  # empty list of file rows
            # add rows to the file_rows list
            for row in file:
                file_rows.append(row.strip())  # https://www.geeksforgeeks.org/python-string-strip-2/
            print("**************************************************************************")
            print("combined.csv read successfully. Rows read from file: " + str(len(file_rows)))

            # get the column headings of the CSV file
            print("____________________________________________________")
            print("Headings of file:")
            row0 = file_rows[0]
            line = row0.split(",")
            column_headings = line
            print(column_headings)

            # get the unique list of CryptoCurrencies from the CSV file
            non_unique_cryptos = []
            file_rows_from_row1_to_end = file_rows[1:len(file_rows) - 1]
            for row in file_rows_from_row1_to_end:
                line = row.split(",")
                non_unique_cryptos.append(line[6])
            cryptos = self.unique(non_unique_cryptos)
            print("____________________________________________________")
            print("Total Currencies found: " + str(len(cryptos)))
            print(str(cryptos))

            # build the base dictionary of CryptoCurrencies
            for crypto in cryptos:
                data[crypto] = {}

            # build the dictionary of dictionaries
            for row in file_rows_from_row1_to_end:
                line = row.split(",")
                dates = self.string_date_into_QDate(line[0])
                crypto = line[6]

                #  print("the close price for BTC on 04/29/2013", self.data[][QDate(2019, 4, 29)])

                close_price = line[4]
                # include error handling code if close price is incorrect
                data[crypto][dates] = float(close_price)
        except:
            print("Error: combined.csv file not found. ")
            print("Make sure you have imported this file into your project.")
        # return the data
        print("____________________________________________________")
        print("Amount of Currencies stored in data:", len(data))  # will be 0 if empty/error
        print("**************************************************************************")
        return data

    def string_date_into_QDate(self, date_String):
        '''
        This method is complete
        Converts a data in a string format like that in a CSV file to QDate Objects for use with QCalendarWidget
        :param date_String: data in a string format
        :return:
        '''
        date_list = date_String.split("-")
        date_QDate = QDate(int(date_list[0]), int(date_list[1]), int(date_list[2]))
        return date_QDate

    def unique(self, non_unique_list):
        '''
        This method is complete
        Converts a list of non-unique values into a list of unique values
        Developed from https://www.geeksforgeeks.org/python-get-unique-values-list/
        :param non_unique_list: a list of non-unique values
        :return: a list of unique values
        '''
        # intilize a null list
        unique_list = []

        # traverse for all elements
        for x in non_unique_list:
            # check if exists in unique_list or not
            if x not in unique_list:
                unique_list.append(x)
                # print list
        return unique_list

    # Function that centers the window
    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()

        qr.moveCenter(cp)
        self.move(qr.topLeft())

        # EXTRA FEATURE 1
        # Added dialog when trying to quit the app

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.StandardButton.Yes |
                                     QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:

            event.accept()
        else:

            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(
        """
                QWidget{
                    background: #f0eee4 ;
                }
                
                QComboBox{
                    border: 1px solid ;
                    padding: 5px;
                    border-radius: 8px;
                    background: #f8f8ff;
                }
                QDoubleSpinBox{
                    border: 1px solid ;
                    padding: 5px;
                    border-radius: 8px;
                    background: #f8f8ff;
                }
                
                QLabel#purchaseTotal{
                    border: 1px solid ;
                    border-radius: 8px;
                    
                }
                QLabel{
                font-style: normal;
                font-size: 10pt;
                font-weight: Medium;
                }
                
                QCalendarWidget QAbstractItemView
                { 
                    selection-background-color: #042944; 
                    selection-color: white;
                }
                QCalendarWidget QWidget 
                {
                  color:grey;
                }
                QCalendarWidget QTableView
                {
                    border-width:0px;
                    background-color:#f8f8ff;
                }
                
               
                
            """
    )
    currency_converter = CryptoTradeProfitCalculator()
    currency_converter.show()
    sys.exit(app.exec())
