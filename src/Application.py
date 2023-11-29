import sys
import argparse
import logging

class BaseApplication:
    _instance = None

    @staticmethod
    def getInstance():
        if Application._instance is None:
            Application._instance = Application()
        return Application._instance
    
    def __init__(self, default_args=True):
        if Application._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Application._instance = self

        self.infos = {
            "name": "app",
            "display_name": None,
            "version": None,
            "author": None
        }

        
        self.parser = argparse.ArgumentParser()
        self.args = None

        self._default_args = default_args
        if default_args is True:
            self._setup_argument_parser()

    def _setup_argument_parser(self):
        self.parser.description = f"{self.infos['display_name']} v{self.infos['version']}"

        self.parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
        self.parser.add_argument("-d", "--debug", help="enable debug mode", action="store_true")

    def parse_arguments(self):
        self.args = self.parser.parse_args()

        if self._default_args is True:
            if self.args.debug is True:
                log_level = logging.DEBUG
            elif self.args.verbose is True:
                log_level = logging.INFO
            else:
                log_level = logging.WARNING
            logging.basicConfig(level=log_level, format='[%(levelname)s] %(message)s')

    def get_infos(self):
        return self.infos
    
    def set_infos(self, name, display_name=None, version=None, author=None):
        self.infos["name"] = name
        self.infos["display_name"] = display_name
        self.infos["version"] = version
        self.infos["author"] = author



class Application(BaseApplication):
    
    def __init__(self):
        super(Application, self).__init__()
        self.set_infos("pyqt6_testapp", "PyQt6 TestApp", "1.0.0", "SamLDM")

    def run(self):
        logging.info("Starting " + self.infos["display_name"] + " v" + self.infos["version"] + "...")
        from src.UI.QApplication import Application as QApplication
        
        self.qapp = QApplication(sys.argv)
        self.qapp.run()