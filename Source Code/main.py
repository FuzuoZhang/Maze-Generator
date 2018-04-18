from MazeGeneClass import MazeGenerator
from mazeui import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox  #QmessageBox是弹出框函数
import sys

class MazeGui(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MazeGui,self).__init__()
        self.setupUi(self)
        self.button.clicked.connect(self.pressbutton)  # 槽函数不用加括号
    def pressbutton(self):   ##槽函数点击生成按钮
        self.height=self.box_gd.value()
        self.width=self.box_kd.value()
        if(self.height%2==0 or self.width%2==0):
            QMessageBox.information(self,  # 使用infomation信息框
                                    "提示",
                                   "高度和宽度均不能为偶数！")
            return
        method=self.xlcd.currentIndex()+1  # 1 kruscal  2 DFS  3 BFS
        mazeGene=MazeGenerator(self.width,self.height,method)
        self.maze=mazeGene.maze

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui=MazeGui()
    ui.show()
    sys.exit(app.exec_())


