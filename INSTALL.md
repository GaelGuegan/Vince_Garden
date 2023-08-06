todo

pip3 install apscheduler
pip3 install pyside6
pyside6-designer
pyside6-uic src/mainwindow.ui  > src/ui_mainwindow.py | sed -i 's|import rc_resource_rc||' src/ui_mainwindow.py
pyside6-rcc res/resource.qrc -o sr/resource.py
