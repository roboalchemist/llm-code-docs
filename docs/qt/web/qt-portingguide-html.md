# Source: https://doc.qt.io/qt/portingguide.html

Title: Porting to Qt 6 | Qt 6.10

URL Source: https://doc.qt.io/qt/portingguide.html

Published Time: Thu, 29 Jan 2026 10:00:49 GMT

Markdown Content:
There are many changes to Qt from the previous version, Qt 5, to Qt 6. Before upgrading to Qt 6, make sure that your Qt 5 application is updated to Qt 5.15. The latest Qt 5 version has the least amount of changes when porting to Qt 6. However, APIs marked as deprecated or obsolete in Qt 5.15 may have been removed in Qt 6.

Here are things you should check if you are porting your Qt 5 applications into Qt 6.

Disable use of C++ API deprecated in Qt 5.15[](https://doc.qt.io/qt/portingguide.html#disable-use-of-c-api-deprecated-in-qt-5-15 "Direct link to this headline")
----------------------------------------------------------------------------------------------------------------------------------------------------------------

Usage of API deprecated in Qt will typically show up in the form of a compiler warning. You can also make the use an error by defining the [QT_DISABLE_DEPRECATED_UP_TO](https://doc.qt.io/qt-6/qtdeprecationmarkers.html#QT_DISABLE_DEPRECATED_UP_TO) C++ macro in your build system. To disable any API deprecated in 5.15 or older Qt versions, define the macro to `0x050F00`, which is '5.15.0' encoded as a hexadecimal number.

For example, in a qmake project file, define the macro with:

DEFINES += QT_DISABLE_DEPRECATED_UP_TO=0x050F00

In CMake, you can use add_compile_definitions:

add_compile_definitions(QT_DISABLE_DEPRECATED_UP_TO=0x050F00)

* [Qt 5.15 Obsolete C++ Classes](https://doc.qt.io/qt-5/obsoleteclasses.html)
* [Qt 5.15 Obsolete QML Types](https://doc.qt.io/qt-5/obsoleteqmltypes.html)
* [Qt 6 Obsolete C++ Classes](https://doc.qt.io/qt-6/obsoleteclasses.html)
* [Qt 6 Obsolete QML Types](https://doc.qt.io/qt-6/obsoleteqmltypes.html)

Check the Changes to the Modules[](https://doc.qt.io/qt/portingguide.html#check-the-changes-to-the-modules "Direct link to this headline")
------------------------------------------------------------------------------------------------------------------------------------------

A goal for the Qt 6 release is to maintain a streamlined framework which means the removal of some Qt 5 modules in Qt 6. In some cases, APIs from a deprecated module are available in another module. In future Qt 6 releases, new or previous modules may be added.

* [Removed Modules in Qt 6.0](https://doc.qt.io/qt-6/whatsnew60.html#removed-modules-in-qt-6-0)
* [New Modules in Qt 6.0](https://doc.qt.io/qt-6/whatsnew60.html#new-modules-in-qt-6-0)
* [New and Restored Modules in Qt 6.1](https://doc.qt.io/qt-6/whatsnew61.html#new-and-restored-modules-in-qt-6-1)
* [New and Restored Modules in Qt 6.2](https://doc.qt.io/qt-6/whatsnew62.html#new-and-restored-modules-in-qt-6-2)
* [Changes to Qt Modules in Qt 6](https://doc.qt.io/qt-6/modulechanges.html) - list of changes per Qt module

Test for Graphical Regressions[](https://doc.qt.io/qt/portingguide.html#test-for-graphical-regressions "Direct link to this headline")
--------------------------------------------------------------------------------------------------------------------------------------

QML applications have a new graphical backend, which you should test for regressions. OpenGL is no longer guaranteed as default on target platforms and you should check that your graphics code is still creating the same effects you want.

It is still possible to use OpenGL calls in Qt applications, but the OpenGL APIs are moved to the [Qt OpenGL](https://doc.qt.io/qt-6/qtopengl-index.html) module. The graphical backend for Qt Widgets applications are unchanged from Qt 5.

* [Graphics](https://doc.qt.io/qt-6/topics-graphics.html)
* [Changes to Qt Quick](https://doc.qt.io/qt-6/quick-changes-qt6.html) - changes to Qt Quick graphics that may affect Qt 5 applications

### High-DPI[](https://doc.qt.io/qt/portingguide.html#high-dpi "Direct link to this headline")

Qt 6 supports high-DPI displays on all platforms, and will automatically account for the display resolution when using higher level APIs such as Qt Widgets or Qt Quick. Applications only need to provide high-resolution assets, such as images and icons. The feature is always enabled.

Qt 6 changes the default scale factor rounding policy from [Qt::HighDpiScaleFactorRoundingPolicy::Round](https://doc.qt.io/qt-6/qt.html#HighDpiScaleFactorRoundingPolicy-enum) to [Qt::HighDpiScaleFactorRoundingPolicy::PassThrough](https://doc.qt.io/qt-6/qt.html#HighDpiScaleFactorRoundingPolicy-enum) in order to track operating system DPI settings accurately. Applications that use Qt Widgets may encounter graphical glitches at non-integer scale factors, for example on Windows with a display configured for 175%. In that case, set the rounding policy to [Round](https://doc.qt.io/qt-6/qt.html#HighDpiScaleFactorRoundingPolicy-enum) to restore Qt 5 behavior.

See [High DPI](https://doc.qt.io/qt-6/highdpi.html) for more details.

Use the Platform Integration APIs[](https://doc.qt.io/qt/portingguide.html#use-the-platform-integration-apis "Direct link to this headline")
--------------------------------------------------------------------------------------------------------------------------------------------

There is better integration with the native APIs on target platforms in Qt 6. You can use platform integration APIs to implement native behavior that is not provided by Qt. For Qt 6, check for any updates to your application's target platform.

* [Platform Integration](https://doc.qt.io/qt-6/platform-integration.html)
* [Qt Platform Abstraction](https://doc.qt.io/qt-6/qpa.html)
* [Supported Platforms](https://doc.qt.io/qt-6/supported-platforms.html)

Use Porting Tool[](https://doc.qt.io/qt/portingguide.html#use-porting-tool "Direct link to this headline")
----------------------------------------------------------------------------------------------------------

A Clazy-based tool is available to facilitate porting from Qt 5 to Qt 6: [Porting C++ Applications to Qt 6 using Clazy checks](https://doc.qt.io/qt-6/porting-to-qt6-using-clazy.html).

Further Reading[](https://doc.qt.io/qt/portingguide.html#further-reading "Direct link to this headline")
--------------------------------------------------------------------------------------------------------

* [What's new in Qt 6](https://doc.qt.io/qt-6/whatsnewqt6.html) - changes in Qt 6 minor versions
* [Build System Changes in Qt 6](https://doc.qt.io/qt-6/qt6-buildsystem.html) - for building Qt 6 from source
* [CMake: Qt 5 and Qt 6 compatibility](https://doc.qt.io/qt-6/cmake-qt5-and-qt6-compatibility.html) - how to support both Qt 5 and Qt 6 in CMake

### QTextStream Changes[](https://doc.qt.io/qt/portingguide.html#qtextstream-changes "Direct link to this headline")

The method QTextStream::setCodec() has been removed in Qt 6. Use [QTextStream::setEncoding](https://doc.qt.io/qt-6/qtextstream.html#setEncoding)() instead.
