# Source: https://doc.qt.io/qtforpython-6/tools/index.html

Title: Tools - Qt for Python

URL Source: https://doc.qt.io/qtforpython-6/tools/index.html

Markdown Content:
Following the same idea from the modules, we also include in the packages (wheels) Qt tools that are important for any Qt application development workflow, like `uic`, `rcc`, etc.

All the tools **must** be used from the PySide wrappers, and not directly. For example, if exploring the `site-packages/` directory on your installation you find `uic.exe` (on Windows), you should not click on that, and use `pyside6-uic.exe` instead. The reason for this is the proper setup of PATHs, plugins, and more, to properly work with the installed Python package.

Here you can find all the tools we include in Qt for Python starting from 6.3.0, grouped by different topics:

Project development[¶](https://doc.qt.io/qtforpython-6/tools/index.html#project-development "Link to this heading")
-------------------------------------------------------------------------------------------------------------------

`pyside6-project`

to build _Qt Widgets Designer_ forms (`.ui` files), resource files (`.qrc`) and QML type files (`.qmltype`) from a `.pyproject` file.

[pyside6-project](https://doc.qt.io/qtforpython-6/tools/pyside-project.html#pyside6-project)

Widget Development[¶](https://doc.qt.io/qtforpython-6/tools/index.html#widget-development "Link to this heading")
-----------------------------------------------------------------------------------------------------------------

`pyside6-uic`

to generate Python code from `.ui` form files.

[pyside6-uic](https://doc.qt.io/qtforpython-6/tools/pyside-uic.html#pyside6-uic)

`pyside6-rcc`

to generate serialized data from `.qrc` resources files. Keep in mind these files can be used in other non-widget projects.

[pyside6-rcc](https://doc.qt.io/qtforpython-6/tools/pyside-rcc.html#pyside6-rcc)

QML Development[¶](https://doc.qt.io/qtforpython-6/tools/index.html#qml-development "Link to this heading")
-----------------------------------------------------------------------------------------------------------

`pyside6-qmllint`

that verifies the syntactic validity of QML files.

[pyside6-qmllint](https://doc.qt.io/qtforpython-6/tools/pyside-qmllint.html#pyside6-qmllint)

`pyside6-qmltyperegistrar`

to read metatypes files and generate files that contain the necessary code to register all the types marked with relevant macros.

[pyside6-qmltyperegistrar](https://doc.qt.io/qtforpython-6/tools/pyside-qmltyperegistrar.html#pyside6-qmltyperegistrar)

`pyside6-qmlimportscanner`

to identify the QML modules imported from a project/QML files and dump the result as a JSON array.

[pyside6-qmlimportscanner](https://doc.qt.io/qtforpython-6/tools/pyside6-qmlimportscanner.html#pyside6-qmlimportscanner)

`pyside6-qmlcachegen`

to compile QML to bytecode at compile time for bundling inside the binary.

[pyside6-qmlcachegen](https://doc.qt.io/qtforpython-6/tools/pyside-qmlcachegen.html#pyside6-qmlcachegen)

`pyside6-qmlsc`

replaces `pyside6-qmlcachegen`. This tool generates C++ code in addition to byte code for functions it can exhaustively analyze.

pyside6-qmlsc

`pyside6-qml`

to enable quick prototyping with QML files. This tool mimics some of the capabilities of Qt’s `QML` runtime utility by directly invoking QQmlEngine/QQuickView.

[pyside6-qml](https://doc.qt.io/qtforpython-6/tools/pyside-qml.html#pyside6-qml)

Translations[¶](https://doc.qt.io/qtforpython-6/tools/index.html#translations "Link to this heading")
-----------------------------------------------------------------------------------------------------

`pyside6-lrelease`

to create run-time translation files for the application.

[pyside6-lrelease](https://doc.qt.io/qtforpython-6/tools/pyside-lrelease.html#pyside6-lrelease)

`pyside6-lupdate`

to synchronize source code and translations.

[pyside6-lupdate](https://doc.qt.io/qtforpython-6/tools/pyside-lupdate.html#pyside6-lupdate)

Qt Help[¶](https://doc.qt.io/qtforpython-6/tools/index.html#qt-help "Link to this heading")
-------------------------------------------------------------------------------------------

PySide Utilities[¶](https://doc.qt.io/qtforpython-6/tools/index.html#pyside-utilities "Link to this heading")
-------------------------------------------------------------------------------------------------------------

`pyside6-genpyi`

to generate Python stubs (`.pyi` files) for Qt modules.

[pyside6-genpyi](https://doc.qt.io/qtforpython-6/tools/pyside-genpyi.html#pyside6-genpyi)

`pyside6-metaobjectdump`

a tool to print out the metatype information in JSON to be used as input for `qmltyperegistrar`.

[pyside6-metaobjectdump](https://doc.qt.io/qtforpython-6/tools/pyside-metaobjectdump.html#pyside6-metaobjectdump)

IDE Integration[¶](https://doc.qt.io/qtforpython-6/tools/index.html#ide-integration "Link to this heading")
-----------------------------------------------------------------------------------------------------------

Qt Python VSCode Extension

Visual Studio Code extension for PySide6 development with project templates, debugging, build tasks, and more.

[Qt Python VSCode Extension](https://doc.qt.io/qtforpython-6/tools/vscode-ext.html#vscode-ext)

Deployment[¶](https://doc.qt.io/qtforpython-6/tools/index.html#deployment "Link to this heading")
-------------------------------------------------------------------------------------------------

Shader Tools[¶](https://doc.qt.io/qtforpython-6/tools/index.html#shader-tools "Link to this heading")
-----------------------------------------------------------------------------------------------------

`pyside6-qsb`

a command-line tool provided by the Qt Shader Tools modules to generate and inspect .qsb files.

[pyside6-qsb](https://doc.qt.io/qtforpython-6/tools/pyside6-qsb.html#pyside6-qsb)

Qt Quick 3D[¶](https://doc.qt.io/qtforpython-6/tools/index.html#qt-quick-3d "Link to this heading")
---------------------------------------------------------------------------------------------------

`pyside6-balsam`

a command line tool that takes assets created in digital content creation tools like Maya, 3ds Max or Blender and converts them into an efficient runtime format for use with Qt Quick 3D.

[pyside6-balsam](https://doc.qt.io/qtforpython-6/tools/pyside6-balsam.html#pyside6-balsam)

`pyside6-balsamui`

a graphical user interface for the `pyside6-balsam` tool.

[pyside6-balsamui](https://doc.qt.io/qtforpython-6/tools/pyside6-balsamui.html#pyside6-balsamui)
