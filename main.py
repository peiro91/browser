import sys
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navigation bar
        navbar = QToolBar()
        self.addToolBar(navbar)

        # back button
        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        # forward button
        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        # reload button
        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        # home button
        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        # invert color button
        invert_btn = QAction('Invert Colors', self)
        invert_btn.triggered.connect(self.invert_colors)
        navbar.addAction(invert_btn)

        # URL bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        # go button
        go_btn = QAction('Go', self)
        go_btn.triggered.connect(self.navigate_to_url)
        navbar.addAction(go_btn)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url
        try:
            self.browser.setUrl(QUrl(url))
        except Exception as e:
            print(e)

    def update_url(self, q):
        self.url_bar.setText(q.toString())

    def invert_colors(self):
        inverted_css = "html {-webkit-filter: invert(1); filter: invert(1);}"
        self.browser.page().runJavaScript("var style = document.createElement('style'); style.innerHTML = '{}'; document.head.appendChild(style);".format(inverted_css))

app = QApplication(sys.argv)
QApplication.setApplicationName('My Browser')
main = MainWindow()
app.exec_()
