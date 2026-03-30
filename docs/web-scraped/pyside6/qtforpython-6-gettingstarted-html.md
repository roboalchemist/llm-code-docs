# Source: https://doc.qt.io/qtforpython-6/gettingstarted.html

Title: Getting Started - Qt for Python

URL Source: https://doc.qt.io/qtforpython-6/gettingstarted.html

Markdown Content:
Here you can find the steps to install and create a simple application using the two technologies that Qt provides: Qt Widgets and Qt Quick.

Note

If you are new to Qt, you can check the [Frequently Asked Questions](https://doc.qt.io/qtforpython-6/gettingstarted.html#faq-section) section at the end of this page to understand concepts, file types, compatibles IDEs, etc. In case you own a Qt License, please refer to [Commercial Use](https://doc.qt.io/qtforpython-6/commercial/index.html#commercial-page).

Requirements[¶](https://doc.qt.io/qtforpython-6/gettingstarted.html#requirements "Link to this heading")
--------------------------------------------------------------------------------------------------------

Before you can install Qt for Python, first you must install the following software:

*   [Official](https://www.python.org/downloads/) Python 3.9+

*   We **highly** recommend using a virtual environment, such as [venv](https://docs.python.org/3/library/venv.html) or [virtualenv](https://virtualenv.pypa.io/en/latest) and avoid installing PySide6 via `pip` in your system.

Installation[¶](https://doc.qt.io/qtforpython-6/gettingstarted.html#installation "Link to this heading")
--------------------------------------------------------------------------------------------------------

*   **Creating and activating an environment** You can do this by running the following on a terminal:

    *   Create environment (Your Python executable might be called `python3`):

python -m venv env 
    *   Activate the environment (Linux and macOS):

source env/bin/activate 
    *   Activate the environment (Windows):

env\Scripts\activate.bat 

Check this animation on how to do it:

![Image 1: PySide6 Installation GIF](https://qt-wiki-uploads.s3.amazonaws.com/images/8/8a/Pyside6_install.gif)

Note

Having Qt installed in your system will not interfere with your PySide6 installation if you do it via `pip install`, because the Python packages (wheels) already includes Qt binaries. Most notably, style plugins from the system won’t have any effect on PySide applications.

*   **Installing PySide6**

Now you are ready to install the Qt for Python packages using `pip`. From the terminal, run the following command:

    *   For the latest version:

pip install pyside6 
    *   For a specific version, like 6.10.1:

pip install pyside6==6.10.1 
    *   It is also possible to install a specific snapshot from our servers. To do so, you can use the following command:

pip install --index-url=https://download.qt.io/snapshots/ci/pyside/6.10/latest pyside6 --trusted-host download.qt.io 

*   **Test your installation**

Now that you have Qt for Python installed, test your setup by running the following Python constructs to print version information:

import PySide6.QtCore

# Prints PySide6 version
print(PySide6. __version__ )

# Prints the Qt version used to compile PySide6
print(PySide6.QtCore. __version__ ) Note

For more information about what’s included in the `pyside6` package, check [Package Details](https://doc.qt.io/qtforpython-6/package_details.html#package-details). 

Create your first Qt Application[¶](https://doc.qt.io/qtforpython-6/gettingstarted.html#create-your-first-qt-application "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------

![Image 2: Qt Widgets and Qt Quick comparison header animation](https://qt-wiki-uploads.s3.amazonaws.com/images/e/eb/Pyside6_widgets_quick.gif)
Qt provides two technologies to build User Interfaces:

*   Qt Widgets, an imperative programming and design approach that has been around since the beginning of Qt, making it a stable and reliable technology for UI applications.

*   Qt Quick, a declarative programming and design approach, which enables you to create fluid UIs by describing them in terms of simple elements.

Both technologies offer you the possibility to use _drag and drop_ tools to create your interfaces. [pyside6-designer](https://doc.qt.io/qtforpython-6/tools/pyside-designer.html#pyside6-designer) for Qt Widgets (included when you install pyside6), and Qt Design Studio for Qt Quick ([Get it here](https://doc.qt.io/qt-6/install-qt-design-studio.html)).

Note

After reading this page, it is recommended that you check the [pyside6-project](https://doc.qt.io/qtforpython-6/tools/pyside-project.html#pyside6-project) tool to learn how to create projects automatically without writing all the code by hand.

### Create your first Qt Application with Qt Widgets[¶](https://doc.qt.io/qtforpython-6/gettingstarted.html#create-your-first-qt-application-with-qt-widgets "Link to this heading")

Your Qt for Python setup is ready. You can explore it further by developing a simple application that prints `"Hello World"` in several languages. The following instructions will guide you through the development process:

*   **Imports**

Create a new file named `hello_world.py`, and add the following imports to it.:

import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui 
The PySide6 Python module provides access to the Qt APIs as its submodule. In this case, you are importing the QtCore, QtWidgets, and QtGui submodules.

*   **Main Class**

Define a class named `MyWidget`, which extends QWidget and includes a QPushButton and QLabel.:

class MyWidget(QtWidgets.QWidget):
    def  __init__ (self):
        super(). __init__ ()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World",
                                     alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello)) 
The `MyWidget` class has the `magic` member function that randomly chooses an item from the `hello` list. When you click the button, the `magic` function is called.

*   **Application execution**

Now, add a main function where you instantiate `MyWidget` and `show` it.:

if  __name__  == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec()) 
Run your example by writing the following command:

python hello_world.py 
Try clicking the button at the bottom to see which greeting you get.

![Image 3: Hello World application in Qt Widgets](https://doc.qt.io/qtforpython-6/_images/screenshot_hello_widgets.png)

### Create your first Qt Application with Qt Quick[¶](https://doc.qt.io/qtforpython-6/gettingstarted.html#create-your-first-qt-application-with-qt-quick "Link to this heading")

To do the same using Qt Quick:

*   **Imports**

Create a new file named `hello_world_quick.py`, and add the following imports to it.:

import sys
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine 
*   **Declarative UI**

The UI can be described in the QML language:

import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Window {
 width: 300
 height: 200
 visible: true
 title: "Hello World"

 readonly property list<string> texts: ["Hallo Welt", "Hei maailma",
 "Hola Mundo", "Привет мир"]

 function setText() {
 var i = Math.round(Math.random() * 3)
 text.text = texts[i]
 }

 ColumnLayout {
 anchors.fill: parent

 Text {
 id: text
 text: "Hello World"
 Layout.alignment: Qt.AlignHCenter
 }
 Button {
 text: "Click me"
 Layout.alignment: Qt.AlignHCenter
 onClicked: setText()
 }
 }
} 
Put the this into a file named `Main.qml` into a directory named `Example` along with a file named `qmldir` to describe a basic QML module:

module Example
Main 254.0 Main.qml 
*   **Application execution**

Now, add a main function where you instantiate a QQmlApplicationEngine and load the QML:

import sys
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

if  __name__  == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.addImportPath(sys.path[0])
    engine.loadFromModule("Example", "Main")
    if not engine.rootObjects():
        sys.exit(-1)
    exit_code = app.exec()
    del engine
    sys.exit(exit_code) 
Run your example by writing the following command:

python main.py 
Try clicking the button at the bottom to see which greeting you get.

![Image 4: Hello World application in Qt Quick](https://doc.qt.io/qtforpython-6/_images/screenshot_hello_quick.png)

Next steps[¶](https://doc.qt.io/qtforpython-6/gettingstarted.html#next-steps "Link to this heading")
----------------------------------------------------------------------------------------------------

Now that you have use both technologies, you can head to our [Examples](https://doc.qt.io/qtforpython-6/examples/index.html#pyside6-examples) and [Tutorials](https://doc.qt.io/qtforpython-6/tutorials/index.html#pyside6-tutorials) sections.

Tip

**Visual Studio Code Users**: If you use VSCode, check out the [Qt Python VSCode Extension](https://doc.qt.io/qtforpython-6/tools/vscode-ext.html#vscode-ext) which provides project templates, debugging support, build tasks, and other productivity features for PySide6 development.

Frequently Asked Questions[¶](https://doc.qt.io/qtforpython-6/gettingstarted.html#frequently-asked-questions "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------

Here you can find a couple of common questions and situations that will clarify questions before you start programming.

Why Qt for Python?

As a Qt/C++ developer, why should I consider Qt for Python?

[Why Qt for Python?](https://doc.qt.io/qtforpython-6/faq/whyqtforpython.html#whyqtforpython)
