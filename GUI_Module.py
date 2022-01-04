import sys
from PyQt5.QtWidgets import QLabel, QPushButton, QWidget, QApplication, QLineEdit
from get_News_item import Crawling_news
import pandas as pd


class Ui_MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle('LineEdit')
        self.resize(300, 300)

        self.line_edit_keyword = QLineEdit(self)
        self.line_edit_keyword.move(75, 75)

        self.line_deit_counter = QLineEdit(self)
        self.line_deit_counter.move(75, 125)

        self.text_label_keywork = QLabel(self)
        self.text_label_keywork.move(75, 60)
        self.text_label_keywork.setText('키워드')

        self.text_label_counter = QLabel(self)
        self.text_label_counter.move(75, 110)
        self.text_label_counter.setText('갯수')

        self.button_csv = QPushButton(self)
        self.button_csv.move(130, 175)
        self.button_csv.setText('Export CSV file')
        self.button_csv.clicked.connect(self.button_event_df2csv)

        self.button_cafe = QPushButton(self)
        self.button_cafe.move(50, 175)
        self.button_cafe.setText('Export cafe')
        # self.button_cafe.clicked.connect(self.button_event_df2csv)

        self.show()

    def button_event_df2csv(self):
        text_keyword = self.line_edit_keyword.text()  # line_edit text 값 가져오기
        # self.text_label_keywork.setText(text_keyword)  # label에 text 설정하기

        text_counter = self.line_deit_counter.text()  # line_edit text 값 가져오기
        # self.text_label_counter.setText(text_counter)  # label에 text 설정하기

        crawling = Crawling_news(text_keyword, int(text_counter))
        urls, names = crawling.get_item()

        newsDic = {
            'addresses': urls,
            'names' : names
        }

        df = pd.DataFrame(newsDic)
        print(df)
        df.to_csv('./temp_news.csv', encoding='utf-8-sig')

    def button_event_write_blog(self):
        text_keyword = self.line_edit_keyword.text()  # line_edit text 값 가져오기
        self.text_label_keywork.setText(text_keyword)  # label에 text 설정하기


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Ui_MainWindow()

    sys.exit(app.exec_())