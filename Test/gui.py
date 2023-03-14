import os
import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFileDialog, QInputDialog
from include import *
from PyQt5.QtGui import QTextCursor

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.fontSize = 10  # Default font size
        self.initUI()


    def initUI(self):
        # Create central widget and layout
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)
        hLayout = QHBoxLayout(centralWidget)

        # Add file upload option to the left side
        vLayoutLeft = QVBoxLayout()
        vLayoutLeft.setSpacing(10)
        fileHeading = QLabel("Uploaded file")
        vLayoutLeft.addWidget(fileHeading)
        self.fileLabel = QLabel("No file selected")
        vLayoutLeft.addWidget(self.fileLabel)
        vLayoutLeft.addStretch()
        uploadButton = QPushButton("Upload File", self)
        uploadButton.clicked.connect(self.upload_file)
        vLayoutLeft.addWidget(uploadButton)
        hLayout.addLayout(vLayoutLeft)

        # Add console windows to the right side
        vLayoutRight = QVBoxLayout()
        codeLabel = QLabel("Enter the RISC-V assembly code:")
        vLayoutRight.addWidget(codeLabel)

        # Add code editor to the right side
        self.codeEditor = QTextEdit(self)
        self.codeEditor.setFontPointSize(12) # Set font size to 12
        vLayoutRight.addWidget(self.codeEditor)

        consoleLayout = QHBoxLayout()
        self.console1 = QTextEdit(self)
        self.console1.setReadOnly(True)
        consoleLayout.addWidget(self.console1)
        self.console2 = QTextEdit(self)
        self.console2.setReadOnly(True)
        consoleLayout.addWidget(self.console2)
        vLayoutRight.addLayout(consoleLayout)

        consoleLayout2 = QHBoxLayout()
        self.console3 = QTextEdit(self)
        self.console3.setReadOnly(True)
        consoleLayout2.addWidget(self.console3)
        vLayoutRight.addLayout(consoleLayout2)

        runAction = QAction('Run', self)
        runAction.setShortcut('Ctrl+R')
        runAction.triggered.connect(self.run_main)
        self.toolbar = self.addToolBar('Run')
        self.toolbar.addAction(runAction)
        hLayout.addLayout(vLayoutRight)

        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('RISC-V Simulator')


        # Add font size option to toolbar
        fontSizeAction = QAction('Font Size', self)
        fontSizeAction.triggered.connect(self.set_font_size)
        self.toolbar.addAction(fontSizeAction)

        # Set font size of console widgets
        self.console1.setFontPointSize(self.fontSize)
        self.console2.setFontPointSize(self.fontSize)
        self.console3.setFontPointSize(self.fontSize)

        # Add save button for code editor
        saveButton = QPushButton("Save Code", self)
        saveButton.clicked.connect(self.save_text)
        vLayoutRight.addWidget(saveButton)


    def upload_file(self):
        
        self.fileName, _ = QFileDialog.getOpenFileName(self, "Upload File", "", "All Files (*);;Text Files (*.txt)")
        #self.console1.append(str(os.path.basename(self.fileName)))
        if self.fileName:
            self.fileLabel.setText(str(os.path.basename(self.fileName)))

    def set_font_size(self):
        size, ok = QInputDialog.getInt(self, 'Font Size', 'Enter font size:', self.fontSize)
        if ok:
            self.fontSize = size
            self.console1.setFontPointSize(self.fontSize)
            self.console2.setFontPointSize(self.fontSize)
            self.console3.setFontPointSize(self.fontSize)

    def save_text(self, text):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"Save Text File","","Text Files (*.txt)", options=options)
        if fileName:
            with open(fileName, 'w') as q:
                q.write(text)


    def run_main(self):
        subprocess.call(['python','pyt.py',self.fileName])
        

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

