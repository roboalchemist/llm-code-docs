# Source: https://doc.qt.io/qt/build-sources.html

Title: Building Qt Sources | Qt 6.10

URL Source: https://doc.qt.io/qt/build-sources.html

Markdown Content:
You can install Qt by building Qt sources. This is useful if, for example:

* You need a custom build (for example, with patches or debug options).
* Your platform isn't supported by pre-built packages.
* You're contributing to Qt or debugging its internals.

**Note:**In most use cases, other than those listed above, the best way to install Qt is with Qt Online Installer. See [Get and Install Qt with Qt Online Installer](https://doc.qt.io/qt-6/qt-online-installation.html).

The installation procedure is different on each Qt platform. This page provides relevant information for the supported platforms and links to module-specific system requirements.

General Installation Information[](https://doc.qt.io/qt/build-sources.html#general-installation-information "Direct link to this headline")
-------------------------------------------------------------------------------------------------------------------------------------------

When you build Qt sources, you use the _configure_ tool to configure Qt for a particular platform with a particular set of Qt features or modules. For more information, see [Qt Configure Options](https://doc.qt.io/qt-6/configure-options.html).

### The Build and Installation Process[](https://doc.qt.io/qt/build-sources.html#the-build-and-installation-process "Direct link to this headline")

A brief overview of the build and installation process:

1. Download the Qt source code and set up the initial environment.
2. Configure the build according to the use case, such as development on the host system or cross-compilation for a target platform.
3. Build (compile) in a separate directory.
4. Optional. Install the built artifacts.

Platform-Specific Installation Information[](https://doc.qt.io/qt/build-sources.html#platform-specific-installation-information "Direct link to this headline")
---------------------------------------------------------------------------------------------------------------------------------------------------------------

### Windows[](https://doc.qt.io/qt/build-sources.html#windows "Direct link to this headline")

* [Qt for Windows - Building from Source](https://doc.qt.io/qt-6/windows-building.html)

### macOS[](https://doc.qt.io/qt/build-sources.html#macos "Direct link to this headline")

* [Qt for macOS - Building from Source](https://doc.qt.io/qt-6/macos-building.html)

### Linux/X11[](https://doc.qt.io/qt/build-sources.html#linux-x11 "Direct link to this headline")

* [Qt for X11 Requirements](https://doc.qt.io/qt-6/linux-requirements.html)
* [Qt for Linux/X11 - Building from Source](https://doc.qt.io/qt-6/linux-building.html)

### Embedded Linux[](https://doc.qt.io/qt/build-sources.html#embedded-linux "Direct link to this headline")

* [Configure an Embedded Linux Device](https://doc.qt.io/qt-6/configure-linux-device.html)
* [Qt for Embedded Linux](https://doc.qt.io/qt-6/embedded-linux.html)

### Android[](https://doc.qt.io/qt/build-sources.html#android "Direct link to this headline")

* [Qt for Android - Building from Source](https://doc.qt.io/qt-6/android-building.html)

### iOS[](https://doc.qt.io/qt/build-sources.html#ios "Direct link to this headline")

* [Qt for iOS - Building from Source](https://doc.qt.io/qt-6/ios-building-from-source.html)

### Module-specific System Requirements[](https://doc.qt.io/qt/build-sources.html#module-specific-system-requirements "Direct link to this headline")

* [Building Qt WebEngine from Source](https://doc.qt.io/qt-6/qtwebengine-platform-notes.html)
* [Building Qt Quick 3D from Source](https://doc.qt.io/qt-6/qtquick3d-index.html#building-from-source)
* [Building Qt Multimedia from Source](https://doc.qt.io/qt-6/qtmultimedia-building-from-source.html)
* [Qt GRPC and Qt Protobuf Module Requirements](https://doc.qt.io/qt-6/qtgrpc-index.html#module-prerequisites)

Additional Information[](https://doc.qt.io/qt/build-sources.html#additional-information "Direct link to this headline")
-----------------------------------------------------------------------------------------------------------------------

The top-level qt5 Git repository contains a set of build instructions in the form of _provisioning scripts_, used by Qt's continuous integration (CI) system to build and test the [Supported Platforms](https://doc.qt.io/qt-6/supported-platforms.html). These scripts are useful for anyone building Qt from source, as they provide information on the tools and components that are required for each configuration.

* [Building Optimized Qt](https://doc.qt.io/qt-6/build-optimized-qt.html)
* [qt/qt5.git CI provisioning for Qt 6.10](https://code.qt.io/cgit/qt/qt5.git/tree/coin?h=6.10)
* [CI Overview in Qt Wiki](https://wiki.qt.io/CI_Overview)
* [Building Qt Documentation](https://wiki.qt.io/Building_Qt_Documentation)
