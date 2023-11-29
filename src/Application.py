import sys
import argparse
import logging

class Application:
    _instance = None

    @staticmethod
    def getInstance():
        if Application._instance is None:
            Application._instance = Application()
        return Application._instance
    
    def __init__(self):
        if Application._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Application._instance = self
        
        self.infos = {
            "name": "pyqt6_testapp",
            "display_name": "PyQt6 TestApp",
            "version": "1.0.0",
            "author": "Anonymous"
        }
        
        self.args = None
        self.parser = argparse.ArgumentParser()
        self.parser.description = self.infos["display_name"] + " v" + self.infos["version"]
        
        self.parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
        self.parser.add_argument("-d", "--debug", help="increase output verbosity", action="store_true")

    def parseArguments(self):
        self.args = self.parser.parse_args()

        if self.args.debug is True:
            log_level = logging.DEBUG
        elif self.args.verbose is True:
            log_level = logging.INFO
        else:
            log_level = logging.WARNING

        logging.basicConfig(level=log_level, format='[%(levelname)s] %(message)s')

    def getInfos(self):
        return self.infos

    def run(self):
        logging.info("Starting " + self.infos["display_name"] + " v" + self.infos["version"] + "...")
        from src.UI.QApplication import Application as QApplication
        
        self.qapp = QApplication(sys.argv)
        self.qapp.run()