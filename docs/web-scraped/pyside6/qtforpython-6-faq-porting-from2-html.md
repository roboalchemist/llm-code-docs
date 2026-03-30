# Source: https://doc.qt.io/qtforpython-6/faq/porting_from2.html

Title: Porting Applications from PySide2 to PySide6

URL Source: https://doc.qt.io/qtforpython-6/faq/porting_from2.html

Markdown Content:
Module Availability[¶](https://doc.qt.io/qtforpython-6/faq/porting_from2.html#module-availability "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------

Qt for Python 6.2.0 provides all modules planned for inclusion in Qt 6.

Module-Level Changes[¶](https://doc.qt.io/qtforpython-6/faq/porting_from2.html#module-level-changes "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------

*   The modules _QtMacExtras_, _Qt Quick Controls 1_, _QtWinExtras_, _QtXmlPatterns_ and _QtX11Extras_ have been removed.

*   `QStateMachine` and related classes have been extracted to a new _QtStateMachine_ module.

*   The modules _QtWebKit_ and _QtWebKitWidgets_ have been replaced by the new _QtWebEngineCore_, _QtWebEngineQuick_ and _QtWebEngineWidgets_ modules.

*   `QXmlReader` and related classes (_SAX API_) have been removed.

*   The content of the _QtOpenGL_ module has been replaced. The class `QGLWidget` and related classes (`QGLContext`, `QGLFunctions`, `QGLShaderProgram`) have been removed. Parts of the _Open GL_ functionality from _QtGui_ have been extracted into this module, for example `QOpenGLBuffer` and `QOpenGLShaderProgram`. There is a new module _QtOpenGLWidgets_ which contains the class `QOpenGLWidget`, a replacement for `QGLWidget`.

As _Open GL_ is phasing out, [QRhi](https://doc.qt.io/qt-6/topics-graphics.html) should be considered for graphics applications.

Imports[¶](https://doc.qt.io/qtforpython-6/faq/porting_from2.html#imports "Link to this heading")
-------------------------------------------------------------------------------------------------

The first thing to do when porting applications is to replace the import statements:

from PySide2.QtWidgets import QApplication
from PySide2 import QtCore

needs to be changed to:

from PySide6.QtWidgets import QApplication
from PySide6 import QtCore

Some classes are in a different module now, for example `QAction` and `QShortcut` have been moved from `QtWidgets` to `QtGui`.

For _Qt Charts_ and _Qt Data Visualization_, the additional namespaces have been removed. It is now possible to use:

from PySide6.QtCharts import QChartView

directly.

Class/Function Deprecations[¶](https://doc.qt.io/qtforpython-6/faq/porting_from2.html#class-function-deprecations "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------

Then, the code base needs to be checked for usage of deprecated API and adapted accordingly. For example:

*   The High DPI scaling attributes `Qt.AA_EnableHighDpiScaling`, `Qt.AA_DisableHighDpiScaling` and `Qt.AA_UseHighDpiPixmaps` are deprecated. High DPI is by default enabled in Qt 6 and cannot be turned off.

*   `QDesktopWidget` has been removed. `QScreen` should be used instead, which can be retrieved using `QWidget.screen()`, `QGuiApplication.primaryScreen()` or `QGuiApplication.screens()`.

*   `QFontMetrics.width()` has been renamed to `horizontalAdvance()`.

*   `QMouseEvent.pos()` and `QMouseEvent.globalPos()` returning a `QPoint` as well as `QMouseEvent.x()` and `QMouseEvent.y()` returning `int` are now deprecated. `QMouseEvent.position()` and `QMouseEvent.globalPosition()` returning a `QPointF` should be used instead.

*   `Qt.MidButton` has been renamed to `Qt.MiddleButton`.

*   `QOpenGLVersionFunctionsFactory.get()` instead of `QOpenGLContext.versionFunctions()` should be used to obtain _Open GL_ functions.

*   `QRegExp` has been replaced by `QRegularExpression`.

*   `QWidget.mapToGlobal()` and `QWidget.mapFromGlobal()` now also accept and return `QPointF`.

*   Functions named `exec_` (classes `QCoreApplication`, `QDialog`, `QEventLoop`) have been renamed to `exec` which became possible in Python 3.

More information can be found in the [Porting to Qt 6](https://doc.qt.io/qt-6/portingguide.html) Guide and the [Qt 6.2 Documentation](https://doc.qt.io/qt-6/index.html) .
