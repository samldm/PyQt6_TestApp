from PyQt6.QtWidgets import QHBoxLayout

from .Sidebar import Sidebar
from .Left import Left
from .Right import Right

class MainLayout(QHBoxLayout):
    def __init__(self):
        super().__init__()
        
        self.setContentsMargins(0, 0, 0, 0)
        self.setSpacing(0)

        self.addLayout(Sidebar())
        self.addLayout(Left())
        self.addLayout(Right())

        self.setStretch(0, 2)
        self.setStretch(1, 4)
        self.setStretch(2, 4)
    
    def toggleSidebar(self, state):
        self.setStretch(0, 2 if state else 0)