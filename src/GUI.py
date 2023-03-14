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

        text1 = "<b style='font-size: 12pt'>Register:</b> <br>"
        self.console1.setText(text1)
        txt1 = ""
        for i in range(0, len(mem.RegisterFile)):
            txt1 += "X" + str(i) + ": "+ str(mem.RegisterFile[i]) + "\n"
        self.console1.append(txt1)


        text2 = "<b style='font-size: 12pt'>Memory:</b> <br>"
        self.console2.setText(text2)
        self.console2.append("<b style='font-size: 10pt'>Address : Data </b> <br>")
        txt2 = ""
        for i in mem.data_memory:
            txt2 += "{}:  {}\n".format(hex(i), mem.data_memory[i])
        self.console1.append(txt2)
        self.fileName =""


    def upload_file(self):
        
        self.fileName, _ = QFileDialog.getOpenFileName(self, "Upload File", "", "All Files (*);;Text Files (*.txt)")
        self.console1.append(str(os.path.basename(self.fileName)))
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
        self.fileName, _ = QFileDialog.getSaveFileName(self,"Save Text File","","Text Files (*.txt)", options=options)
        if self.fileName:
            with open(self.fileName, 'w') as q:
                q.write(text)


    def run_main(self):

        dirname = os.path.dirname(os.path.abspath(__file__))
        cmd = [sys.executable, os.path.join(dirname, 'main.py'),self.fileName]
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        # dirname = os.path.dirname(os.path.abspath(__file__))
        # cmd = [sys.executable, os.path.join(dirname, 'main.py')]
        # filename = r"C:\Users\rohit\OneDrive\6th Sem (3rd Yr)\CS204\CS204-Project\Risc-V_Final\Risc-V_Final\Risc-V\test\BubbleSort.mc"
        # with open(filename, 'r') as f:
        #     contents = f.read()
        # process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # output, error = process.communicate(contents.encode())
        output = output.decode('utf-8') + error.decode('utf-8')

        self.console3.setText("<b style='font-size: 12pt'>Console Output Describing the operations in a detailed manner:</b>")
        self.console3.append("\n" + output)
        self.console3.moveCursor(QTextCursor.Start)


        text2 = "<b style='font-size: 12pt'>Memory:</b> <br>"
        self.console2.setText(text2)
        self.console2.append("<b style='font-size: 10pt'>Address : Data </b> <br>")
        

        with open('data_mem.mc', 'r+') as p:
            lines = p.readlines()
            text = ''.join(lines)
            self.console2.append(text)
            self.console2.moveCursor(QTextCursor.Start)


        text1 = "<b style='font-size: 12pt'>Register:</b> <br>"
        self.console1.setText(text1)
        

        with open('register_values.mc', 'r') as f:
            lines = f.readlines()
            text = ''.join(lines)
            self.console1.append(text)
            self.console1.moveCursor(QTextCursor.Start)
        

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())