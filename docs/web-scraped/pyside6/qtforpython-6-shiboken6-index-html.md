# Source: https://doc.qt.io/qtforpython-6/shiboken6/index.html

Title: Shiboken

URL Source: https://doc.qt.io/qtforpython-6/shiboken6/index.html

Markdown Content:
[Back to top](https://doc.qt.io/qtforpython-6/shiboken6/index.html#)
Shiboken is a fundamental piece on the [Qt for Python](https://doc.qt.io/qtforpython-6/index.html) project that serves two purposes:

*   [Generator](https://doc.qt.io/qtforpython-6/shiboken6/shibokengenerator.html): Extract information from C or C++ headers and generate [CPython](https://github.com/python/cpython) code that allow to bring C or C++ projects to Python. This process uses a library called [ApiExtractor](https://doc.qt.io/qtforpython-6/shiboken6/typesystem.html) which internally uses [Clang](https://clang.llvm.org/).

*   [Module](https://doc.qt.io/qtforpython-6/shiboken6/shibokenmodule.html): An utility Python module that exposed new Python types, functions to handle pointers, among other things, that is written in [CPython](https://github.com/python/cpython) and can use independently of the generator.

Documentation[¶](https://doc.qt.io/qtforpython-6/shiboken6/index.html#documentation "Link to this heading")
-----------------------------------------------------------------------------------------------------------

Install and build from source.

Binding generator executable.

Python utility module.

Reference and functionality.

Using Shiboken.

Generating Python stub files.

Known issues and FAQ.
