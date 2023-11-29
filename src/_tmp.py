from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QFileDialog
import sys

class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)

        self.createMenuBar()

        self.setWindowTitle("Text Editor")
        self.setGeometry(0, 0, 800, 600)

    def createMenuBar(self):
        menuBar = self.menuBar()
        self.menuBar

        # File menu
        fileMenu = menuBar.addMenu("File")

        # New action
        newAction = QAction(QIcon(), 'New', self)
        newAction.triggered.connect(self.newDocument)
        fileMenu.addAction(newAction)

        # Open action
        openAction = QAction(QIcon(), 'Open', self)
        openAction.triggered.connect(self.openDocument)
        fileMenu.addAction(openAction)

        # Save action
        saveAction = QAction(QIcon(), 'Save', self)
        saveAction.triggered.connect(self.saveDocument)
        fileMenu.addAction(saveAction)

        # Exit action
        exitAction = QAction(QIcon(), 'Exit', self)
        exitAction.triggered.connect(self.close)
        fileMenu.addAction(exitAction)

    def newDocument(self):
        self.textEdit.clear()

    def openDocument(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Text File", "", "Text Files (*.txt);;All Files (*)", options=options)
        if fileName:
            with open(fileName, 'r') as file:
                self.textEdit.setText(file.read())

    def saveDocument(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self, "Save Text File", "", "Text Files (*.txt);;All Files (*)", options=options)
        if fileName:
            with open(fileName, 'w') as file:
                file.write(self.textEdit.toPlainText())

if __name__ == "__main__":
    app = QApplication(sys.argv)

    main = TextEditor()
    main.show()

    sys.exit(app.exec())