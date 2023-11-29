from ..Application import Application as Main
import logging

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication

from .MainWindow import MainWindow

class Application(QApplication):
    _instance = None

    @staticmethod
    def getInstance():
        if Application._instance is None:
            Application._instance = Application()
        return Application._instance
    
    def __init__(self, sys_argv):
        super(Application, self).__init__(sys_argv)

        info = Main.getInstance().get_infos()
        self.setApplicationName(info["name"] + " v" + info["version"])
        self.setApplicationDisplayName(info["display_name"])
        self.setApplicationVersion(info["version"])
        self.setOrganizationName(info["author"])
        
        #self.setWindowIcon(QIcon("icon.png"))

        self.mainWindow = MainWindow()
        self.mainWindow.show()

    def run(self):
        logging.info("Application started")
        return super(Application, self).exec()