from PyQt6.QtWidgets import QVBoxLayout
from ...utils import Color

class Left(QVBoxLayout):
    def __init__(self):
        super().__init__()
        
        self.setContentsMargins(0, 0, 0, 0)
        self.setSpacing(0)

        self.addWidget(Color('green'))