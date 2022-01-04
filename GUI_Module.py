import sys
from PyQt5.QtWidgets import QLabel, QPushButton, QWidget, QApplication, QLineEdit
from get_News_item import Crawling_news
import pandas as pd
from UpLoadModule import naver_login
import time
import os


class Ui_MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle('LineEdit')
        self.resize(500, 500)

        self.line_edit_keyword = QLineEdit(self)
        self.line_edit_keyword.move(75, 75)

        self.line_deit_counter = QLineEdit(self)
        self.line_deit_counter.move(75, 125)

        self.line_deit_id = QLineEdit(self)
        self.line_deit_id.move(75, 175)

        self.line_deit_pwd = QLineEdit(self)
        self.line_deit_pwd.setEchoMode(QLineEdit.Password)
        self.line_deit_pwd.move(75, 225)

        self.text_label_keywork = QLabel(self)
        self.text_label_keywork.move(75, 60)
        self.text_label_keywork.setText('키워드')

        self.text_label_counter = QLabel(self)
        self.text_label_counter.move(75, 110)
        self.text_label_counter.setText('개수')

        self.text_label_id = QLabel(self)
        self.text_label_id.move(75, 160)
        self.text_label_id.setText('아이디')

        self.text_label_pwd = QLabel(self)
        self.text_label_pwd.move(75, 215)
        self.text_label_pwd.setText('비밀번호')

        self.button_csv = QPushButton(self)
        self.button_csv.move(130, 300)
        self.button_csv.setText('Export CSV file')
        self.button_csv.clicked.connect(self.button_event_df2csv)

        self.button_cafe = QPushButton(self)
        self.button_cafe.move(50, 300)
        self.button_cafe.setText('Export cafe')
        self.button_cafe.clicked.connect(self.button_event_write_blog)

        self.show()

    def button_event_df2csv(self):
        text_keyword = self.line_edit_keyword.text()  # line_edit text 값 가져오기
        text_counter = self.line_deit_counter.text()  # line_edit text 값 가져오기

        crawling = Crawling_news(text_keyword, int(text_counter))
        urls, names = crawling.get_item()

        print(urls)
        print(names)

        newsDic = {
            'addresses': urls,
            'names' : names
        }

        df = pd.DataFrame(newsDic)
        ctime = time.strftime("%Y_%m_%d_%H%M%S")
        path = './csv_files'
        os.makedirs(path, exist_ok=True)
        df.to_csv(f'{path}/{ctime}.csv', encoding='utf-8-sig')

        print('Save Csv Finish!!!')

    def button_event_write_blog(self):
        text_keyword = self.line_edit_keyword.text()  # line_edit text 값 가져오기
        text_counter = self.line_deit_counter.text()  # line_edit text 값 가져오기
        id = self.line_deit_id.text()
        pwd = self.line_deit_pwd.text()

        crawling = Crawling_news(text_keyword, int(text_counter))
        urls, names = crawling.get_item()

        naver_login(names, urls, id, pwd)

        print('Finish Upload!!!')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Ui_MainWindow()

    sys.exit(app.exec_())