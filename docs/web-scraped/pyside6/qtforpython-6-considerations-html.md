# Source: https://doc.qt.io/qtforpython-6/considerations.html

Title: Considerations - Qt for Python

URL Source: https://doc.qt.io/qtforpython-6/considerations.html

Markdown Content:
API Changes[¶](https://doc.qt.io/qtforpython-6/considerations.html#api-changes "Link to this heading")
------------------------------------------------------------------------------------------------------

One of the goals of PySide6 is to be API compatible with PyQt, with certain exceptions.

The latest considerations and known issues will be also reported in the [Developer Notes](https://doc.qt.io/qtforpython-6/developer/index.html#developer-notes).

### __hash__() function return value[¶](https://doc.qt.io/qtforpython-6/considerations.html#hash-function-return-value "Link to this heading")

The hash value returned for the classes [`PySide6.QtCore.QDate`](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QDate.html#PySide6.QtCore.QDate "PySide6.QtCore.QDate"), [`PySide6.QtCore.QDateTime`](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QDateTime.html#PySide6.QtCore.QDateTime "PySide6.QtCore.QDateTime"), [`PySide6.QtCore.QTime`](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QTime.html#PySide6.QtCore.QTime "PySide6.QtCore.QTime"), [`PySide6.QtCore.QUrl`](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QUrl.html#PySide6.QtCore.QUrl "PySide6.QtCore.QUrl") will be based on their string representations, thus objects with the same value will produce the same hash.

### QString[¶](https://doc.qt.io/qtforpython-6/considerations.html#qstring "Link to this heading")

Methods and functions that change the contents of a QString argument were modified to receive an immutable Python Unicode (or str) and return another Python Unicode/str as the modified string.

The following methods had their return types modified this way:

**Classes:** QAbstractSpinBox, QDateTimeEdit, QDoubleSpinBox, QSpinBox, QValidator

*   `fixup(string): string`

*   `validate(string, int): [QValidator.State, string, int]`

**Classes:** QDoubleValidator, QIntValidator, QRegExpValidator

*   `validate(string, int): [QValidator.State, string, int]`

**Class:** QClipboard

*   `text(string, QClipboard.Mode mode=QClipboard.Clipboard): [string, string]`

**Class:** QFileDialog

Instead of `getOpenFileNameAndFilter()`, `getOpenFileNamesAndFilter()` and `getSaveFileNameAndFilter()` like PyQt does, PySide has modified the original methods to return a tuple.

*   `getOpenFileName(QWidget parent=None, str caption=None, str dir=None, str filter=None, QFileDialog.Options options=0): [string, filter]`

*   `getOpenFileNames(QWidget parent=None, str caption=None, str dir=None, str filter=None, QFileDialog.Options options=0): [list(string), filter]`

*   `getSaveFileName(QWidget parent=None, str caption=None, str dir=None, str filter=None, QFileDialog.Options options=0): [string, filter]`

**Class:** QWebPage

*   `javaScriptPrompt(QWebFrame, string, string): [bool, string]`

**Classes:** QFontMetrics and QFontMetricsF

They had two new methods added. Both take a string of one character and convert to a QChar (to call the C++ counterpart):

*   `widthChar(string)`

*   `boundingRectChar(string)`

### QTextStream[¶](https://doc.qt.io/qtforpython-6/considerations.html#qtextstream "Link to this heading")

Inside this class some renames were applied to avoid clashes with native Python functions. They are: `bin_()`, `hex_()` and `oct_()`. The only modification was the addition of the ‘_’ character.

### QVariant[¶](https://doc.qt.io/qtforpython-6/considerations.html#qvariant "Link to this heading")

As `QVariant` was removed, any function expecting it can receive any Python object (`None` is an invalid `QVariant`). The same rule is valid when returning something: the returned `QVariant` will be converted to its original Python object type.

When a method expects a `QVariant::Type` the programmer can use a string (the type name) or the type itself.

### qApp “macro”[¶](https://doc.qt.io/qtforpython-6/considerations.html#qapp-macro "Link to this heading")

The C++ API of QtWidgets provides a macro called `qApp` that roughly expands to `QtWidgets::QApplication->instance()`.

In PySide, we tried to create a macro-like experience. For that, the `qApp` variable was implemented as a normal variable that lives in the builtins. After importing `PySide6`, you can immediately use `qApp`.

As a useful shortcut for the action “create an application if it was not created”, we recommend:

qApp or QtWidgets.QApplication()

or if you want to check if there is one, simply use the truth value:

if qApp:
    # do something if an application was created
    pass

Comparing to `None` is also possible, but slightly over-specified.

#### Testing support[¶](https://doc.qt.io/qtforpython-6/considerations.html#testing-support "Link to this heading")

For testing purposes, you can also get rid of the application by calling:

qApp.shutdown()

As for 5.14.2, this is currently an experimental feature that is not fully tested.

#### Embedding status[¶](https://doc.qt.io/qtforpython-6/considerations.html#embedding-status "Link to this heading")

In embedded mode, application objects that are pre-created in C++ don’t have a Python wrapper. The `qApp` variable is created together with a wrapped application. Therefore, `qApp` does not exist in that embedded mode. Please note that you always can use `QtWidgets.QApplication.instance()` instead.

#### Abandoned Alternative[¶](https://doc.qt.io/qtforpython-6/considerations.html#abandoned-alternative "Link to this heading")

We also tried an alternative implementation with a `qApp()` function that was more _pythonic_ and problem free, but many people liked the `qApp` macro better for its brevity, so here it is.

### Rich Comparison[¶](https://doc.qt.io/qtforpython-6/considerations.html#rich-comparison "Link to this heading")

There was a long-standing bug in the `tp_richcompare` implementation of PySide classes.

*   When a class did not implement it, the default implementation of `object` is used. This implements `==` and `!=` like the `is` operator.

*   When a class implements only a single function like `<`, then the default implementation was disabled, and expressions like `obj in sequence` failed with `NotImplemented`.

This oversight was fixed in version 5.15.1 .

Features[¶](https://doc.qt.io/qtforpython-6/considerations.html#features "Link to this heading")
------------------------------------------------------------------------------------------------

In Qt for Python, we begin for the first time to support a more pythonic user interface. With a special import statement, you can switch on features which replace certain aspects of the Python interpreter. This is done by an import statement right after the PySide6 import.

### snake_case[¶](https://doc.qt.io/qtforpython-6/considerations.html#snake-case "Link to this heading")

With the statement:

from  __feature__  import snake_case

all methods in the current module are switched from `camelCase` to `snake_case`. A single upper case letter is replaced by an underscore and the lower case letter.

### true_property[¶](https://doc.qt.io/qtforpython-6/considerations.html#true-property "Link to this heading")

With the statement:

from  __feature__  import true_property

all getter and setter functions which are marked as a property in the Qt6 docs are replaced by Python property objects. Properties are also listed as such in the according QMetaObject of a class.

### Example for both features[¶](https://doc.qt.io/qtforpython-6/considerations.html#example-for-both-features "Link to this heading")

Some Qt for Python snippet might read:

self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

With the above features selected, this reads:

self.table.horizontal_header().section_resize_mode = QHeaderView.Stretch

Additionally, properties can also be declared directly in Shiboken for non Qt-libraries, see property-declare.

### More about features[¶](https://doc.qt.io/qtforpython-6/considerations.html#more-about-features "Link to this heading")

Detailed info about features can be found here: [Why do we have a __feature__?](https://doc.qt.io/qtforpython-6/developer/feature-motivation.html#feature-why)

### Tools[¶](https://doc.qt.io/qtforpython-6/considerations.html#tools "Link to this heading")

Qt for Python ships some Qt tools:

*   `pyside6-rcc`: Qt Resource Compiler. This is a command line tool that compiles `.qrc` files containing binary data, for example images, into executable Python code (see [Using .qrc Files (pyside6-rcc)](https://doc.qt.io/qtforpython-6/tutorials/basictutorial/qrcfiles.html#tutorial-qrcfiles)).

*   `pyside6-uic`: Qt User Interface Compiler. This is a command line tool that compiles `.ui` files containing designs of Qt Widget-based forms into executable Python code (see [Using .ui files from Designer or QtCreator with QUiLoader and pyside6-uic](https://doc.qt.io/qtforpython-6/tutorials/basictutorial/uifiles.html#tutorial-uifiles)).

*   `pyside6-assistant`: Qt Help Viewer. This is a graphical tool that can be used to view Qt documentation from Qt Compressed Help files (`.qhc`). Currently, only the binary without documentation sets is shipped to reduce the wheel size. For building the documentation, see [Building the documentation](https://doc.qt.io/qtforpython-6/building_from_source/index.html#building-documentation).

*   `pyside6-designer`: Qt User Interface Designer. This is a graphical tool to create designs of Qt Widget-based forms and use custom widgets (see [Using .ui files from Designer or QtCreator with QUiLoader and pyside6-uic](https://doc.qt.io/qtforpython-6/tutorials/basictutorial/uifiles.html#tutorial-uifiles), [Custom Widgets in Qt Widgets Designer](https://doc.qt.io/qtforpython-6/tutorials/basictutorial/uifiles.html#designer-custom-widgets)).

The New Python Enums[¶](https://doc.qt.io/qtforpython-6/considerations.html#the-new-python-enums "Link to this heading")
------------------------------------------------------------------------------------------------------------------------

### The Motivation to use new Enums[¶](https://doc.qt.io/qtforpython-6/considerations.html#the-motivation-to-use-new-enums "Link to this heading")

For a long time, there were just the Shiboken enums, which were modelled as exact as possible after the existing enums in Qt. These enums are small classes which also inherit from int.

Meanwhile, Python enums have been developed over the years. They have become a natural part of modern Python. The implementation is perfectly modelled after the needs of Python users. It is therefore just consequent to stop having two different enum implementations in the same application and instead to use the new Python implementation everywhere.

### Existing Work[¶](https://doc.qt.io/qtforpython-6/considerations.html#existing-work "Link to this heading")

The new enums beginning with PySide 6.3, replace the Shiboken enums with Python variants, which harmonize the builtin enums with the already existing `QEnum` “macro” shown in the QEnum section.

### Enums behavior in PySide[¶](https://doc.qt.io/qtforpython-6/considerations.html#enums-behavior-in-pyside "Link to this heading")

In `PySide 6.3` there was a double implementation of old and new enums, where the default was old enums. The new approach to enum is the default in `PySide 6.4` and becomes mandatory in `PySide 6.6`. There exists the environment variable `PYSIDE6_OPTION_PYTHON_ENUM` with the default value of “1”. There can also variations be selected by specifying different flags, but the value of “0” (switching off) is no longer supported.

The still available options for switching some enum features off can be found in the [The Set of Enum Features](https://doc.qt.io/qtforpython-6/developer/enumfeatures_doc.html#enum-features) section.

### The Differences between old and new Enums[¶](https://doc.qt.io/qtforpython-6/considerations.html#the-differences-between-old-and-new-enums "Link to this heading")

Python enums and Shiboken enums are more or less compatible with each other. Tiny differences are in restrictions:

*   Python enums cannot inherit from each other, whereas Shiboken enums can

*   Python enums don’t allow undefined values, Shiboken enums do

*   Python enums always need exactly one argument, Shiboken enums have a default zero value

*   Python enums rarely inherit from int, Shiboken enums always do

More visible are the differences between flags, as shown in the following:

The Shiboken flag constructor example has been in PySide prior to 6.3:

flags = Qt.Alignment()
enum = Qt.AlignmentFlag

with enum shortcuts like

Qt.AlignLeft = Qt.AlignmentFlag.AlignLeft
Qt.AlignTop  = Qt.AlignmentFlag.AlignTop

In PySide 6.3, these shortcuts and flags no longer exist (officially). Instead, Python has an enum.Flags class which is a subclass of the enum.Enum class. But don’t be too scared, here comes the good news…

### Doing a Smooth Transition from the Old Enums[¶](https://doc.qt.io/qtforpython-6/considerations.html#doing-a-smooth-transition-from-the-old-enums "Link to this heading")

Changing all the enum code to suddenly use the new syntax is cumbersome and error-prone, because such necessary changes are not easy to find. Therefore a `forgiveness mode` was developed:

The `forgiveness mode` allows you to continue using the old constructs but translates them silently into the new ones. If you for example write

flags = Qt.Alignment()
enum = Qt.AlignLeft

item.setForeground(QColor(Qt.green))

flags_type = QPainter.RenderHints
flags = QPainter.RenderHints()

chart_view.setRenderHint(QPainter.Antialiasing)

you get in reality a construct that mimics the following code which is the recommended way of writing Flags and Enums:

flags = Qt.AlignmentFlag(0)
enum = Qt.AlignmentFlag.AlignLeft

item.setForeground(QColor(Qt.GlobalColor.green))

flags_type = QPainter.RenderHint
flags = QPainter.RenderHint(0)

chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)

This has the effect that you can initially ignore the difference between old and new enums, as long as the new enums are properties of classes. (This does not work on global enums which don’t have a class, see `Limitations` below.)

### Forgiveness Mode and Type Hints[¶](https://doc.qt.io/qtforpython-6/considerations.html#forgiveness-mode-and-type-hints "Link to this heading")

When you inspect for instance `QtCore.pyi`, you will only find the new enums, although the old ones are still allowed. Also, line completion will only work with the new constructs and never propose the old ones.

The reason to implement `forgiveness mode` this way was

*   to make the transition as smooth as possible, but

*   to encourage people to use the new enums whenever new code is written.

So you can continue to write:

self.text.setAlignment(Qt.AlignCenter)

but this construct is used and recommended for the future:

self.text.setAlignment(Qt.AlignmentFlag.AlignCenter)

### Limitations[¶](https://doc.qt.io/qtforpython-6/considerations.html#limitations "Link to this heading")

The forgiveness mode works very well whenever the enum class is embedded in a normal PySide class. But there are a few global enums, where especially the `QtMsgType` is a problem:

t = QtMsgType.QtDebugMsg

cannot be written in the shortcut form

t = QtDebugMsg

because there is no surrounding PySide class that provides the forgiving mode implementation. Typically, the needed changes are easily found because they often occur in an import statement.

Permission API[¶](https://doc.qt.io/qtforpython-6/considerations.html#permission-api "Link to this heading")
------------------------------------------------------------------------------------------------------------

The cross-platform permission APIs were introduced to Qt in version 6.5 which are currently relevant to platforms macOS, iOS, Android and WebAssembly. With this API, your Qt application can check and request permission for certain features like Camera, Microphone, Location, Bluetooth, Contacts, Calendar. More about permission API can be read in this [Blog post](https://www.qt.io/blog/permission-apis-in-qt-6.5).

When a PySide6 application that uses the permission API is run in interpreted mode, i.e., `python <main_file>.py`, the code implementing the permission API _will not work_. The only way to make your PySide6 application using permission API work is to bundle the application. For Android, this means using the [pyside6-android-deploy: the Android deployment tool for Qt for Python](https://doc.qt.io/qtforpython-6/deployment/deployment-pyside6-android-deploy.html#pyside6-android-deploy) tool and for macOS, this means using the [pyside6-deploy: the deployment tool for Qt for Python](https://doc.qt.io/qtforpython-6/deployment/deployment-pyside6-deploy.html#pyside6-deploy) tool.

When running in interpreted mode, you can skip over the permission check/request using the following _if_ condition

is_deployed = "__compiled__" in globals()
if not is_deployed and sys.platform == "darwin":
    # code implementing permission check and request

This can also be seen in the PySide6 [Camera example](https://doc.qt.io/qtforpython-6/examples/example_multimedia_camera.html#camera-example). * __compiled__ * is a Nuitka attribute to check if the application is run as a standalone application or run in interpreted mode with Python.

### Android[¶](https://doc.qt.io/qtforpython-6/considerations.html#android "Link to this heading")

For Android, [pyside6-android-deploy: the Android deployment tool for Qt for Python](https://doc.qt.io/qtforpython-6/deployment/deployment-pyside6-android-deploy.html#pyside6-android-deploy) takes care of identifying the necessary permissions needed by the application and adding those permissions to the _AndroidManifest.xml_ using the _<uses-permission>_ element.

### macOS[¶](https://doc.qt.io/qtforpython-6/considerations.html#macos "Link to this heading")

Since the Android platform does not automatically come bundled with a Python interpreter, it is evident that to make a PySide6 application run on Android you have to package the PySide6 application. This is not the case for desktop platforms like macOS where a Python interpreter and its packages can be installed and run quite easily.

The problem for macOS is that for the permission API to work you need a macOS bundle with an _Info.plist_ file that lists all the permissions required using the _usage description_ string for each permission used. When Python is run in interpreted mode, i.e., when you run Python, the Qt permission API fetches the _Info.plist_ from the Python interpreter by default which does not contain the _usage description_ strings for the permissions required. You can certainly modify the _Info.plist_ of the Python framework installation to make the Qt permission API work when running a PySide6 application from the terminal. However, this is not recommended. Therefore, the only viable solution is to bundle the PySide6 application as a macOS application bundle using [pyside6-deploy: the deployment tool for Qt for Python](https://doc.qt.io/qtforpython-6/deployment/deployment-pyside6-deploy.html#pyside6-deploy). This macOS application bundle will have its own Info.plist file.
