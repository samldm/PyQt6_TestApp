from ..Application import Application as Main
import logging

from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PyQt6.QtGui import QAction, QPalette, QColor

from .utils import Color
from .Layout.Main.MainLayout import MainLayout


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.app = Main.getInstance()
        self.sidebar_visible = True

        self.setWindowTitle("Main Window")
        self.setMinimumSize(600, 400)
        self.setGeometry(100, 100, 1080, 720)

        self.create_menu()

        self.layout = MainLayout()

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)
    
    def closeEvent(self, event):
        logging.info("MainWindow closed")
        event.accept()
    
    def create_menu(self):
        menuBar = self.menuBar()

        # File menu
        fileMenu = menuBar.addMenu("File")

        # Exit action
        exitAction = QAction('Exit', self)
        exitAction.triggered.connect(self.close)
        fileMenu.addAction(exitAction)

        # View menu
        viewMenu = menuBar.addMenu("View")

        # Toggle sidebar action
        toggleSidebarAction = QAction('Toggle Sidebar', self)
        toggleSidebarAction.triggered.connect(self.toggleSidebar)
        viewMenu.addAction(toggleSidebarAction)

        # Help menu
        helpMenu = menuBar.addMenu("Help")

        # About action
        aboutAction = QAction('About', self)
        helpMenu.addAction(aboutAction)
    
    def toggleSidebar(self):
        self.sidebar_visible = not self.sidebar_visible
        self.layout.toggleSidebar(self.sidebar_visible)