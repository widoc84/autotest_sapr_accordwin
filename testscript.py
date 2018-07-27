
from pywinauto import Application

app = Application().start("C:\\Accord.x64\\aced32.exe")
app.window(title=u'Aced32').wait('visible',timeout=3)
app.window(title=u'Aced32')[u"Да"].DoubleClick()
app.window(best_match="TMainForm").wait('visible',timeout=20)
aced32 = app.window(best_match="TMainForm")
acedtree = aced32.TreeView   