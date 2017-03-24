import sys
from PyQt4.QtGui import *

a = QApplication(sys.argv)

w = QWidget()

result = QMessageBox.question(w, 'practice' , "Do you like Python?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

if result == QMessageBox.Yes:
    print 'yes'
else:
    print 'no'

w.show()

sys.exit(a.exec_())





