# Source: https://doc.qt.io/qtforpython-6/deployment/index.html

Title: Deployment - Qt for Python

URL Source: https://doc.qt.io/qtforpython-6/deployment/index.html

Markdown Content:
Deploying or freezing an application is an important part of a Python project, this means to bundle all required resources so that the application finds everything it needs to be able to run on a client’s machine. However, because most large projects aren’t based on a single Python file, distributing these applications can be a challenge.

Here are a few distribution options that you can use:
1.   Send a normal ZIP file with the application’s content.

2.   Build a proper [Python package (wheel)](https://packaging.python.org/).

3.   Freeze the application into a single binary file or directory.

4.   Provide native installer (msi, dmg)

If you are considering Option 3, then starting with 6.4, we ship a new tool called pyside6-deploy that deploys your PySide6 application to all desktop platforms - Windows, Linux, and macOS. To know more about how to use the tool see [pyside6-deploy: the deployment tool for Qt for Python](https://doc.qt.io/qtforpython-6/deployment/deployment-pyside6-deploy.html#pyside6-deploy). For Android deployment, see [pyside6-android-deploy: the Android deployment tool for Qt for Python](https://doc.qt.io/qtforpython-6/deployment/deployment-pyside6-android-deploy.html#pyside6-android-deploy). Additionally, you can also use other popular deployment tools shown below:

*   [fbs](https://build-system.fman.io/)

*   [PyInstaller](https://www.pyinstaller.org/)

*   [cx_Freeze](https://marcelotduarte.github.io/cx_Freeze/)

*   [py2exe](http://www.py2exe.org/)

*   [py2app](https://py2app.readthedocs.io/en/latest/)

*   [briefcase](https://briefcase.readthedocs.io/)

Although you can deploy PySide6 application using these tools, it is recommended to use pyside6-deploy as it is easier to use and also to get the most optimized executable. Since Qt for Python is a cross-platform framework, we focus on solutions for the three major platforms that Qt supports: Windows, Linux, and macOS.

The following table summarizes the platform support for those packaging tools:

| Name | License | Qt 6 | Qt 5 | Linux | macOS | Windows |
| --- | --- | --- | --- | --- | --- | --- |
| fbs | GPL |  | yes | yes | yes | yes |
| PyInstaller | GPL | partial | yes | yes | yes | yes |
| cx_Freeze | MIT | yes | yes | yes | yes | yes |
| py2exe | MIT | partial | partial | no | no | yes |
| py2app | MIT | yes | yes | no | yes | no |
| briefcase | BSD3 | partial | yes | yes | yes | yes |
| Nuitka | MIT | yes | yes | yes | yes | yes |

Notice that only _fbs_, _cx\_Freeze_, _briefcase_, and _PyInstaller_ meet our cross-platform requirement.

Since these are command-line tools, you’ll need special hooks or scripts to handle resources such as images, icons, and meta-information, before adding them to your package. Additionally, these tools don’t offer a mechanism to update your application packages.

To create update packages, use the [PyUpdater](https://www.pyupdater.org/), which is a tool built around PyInstaller.

The [fbs](https://build-system.fman.io/) tool offers a nice UI for the user to install the application step-by-step.

Note

Deployment is supported only from Qt for Python 5.12.2 and later.

Here’s a set of tutorials on how to use these tools:

*   [pyside6-deploy: the deployment tool for Qt for Python](https://doc.qt.io/qtforpython-6/deployment/deployment-pyside6-deploy.html)
    *   [How to use it?](https://doc.qt.io/qtforpython-6/deployment/deployment-pyside6-deploy.html#how-to-use-it)
    *   [pysidedeploy.spec](https://doc.qt.io/qtforpython-6/deployment/deployment-pyside6-deploy.html#pysidedeploy-spec)
    *   [Command Line Options](https://doc.qt.io/qtforpython-6/deployment/deployment-pyside6-deploy.html#command-line-options)
    *   [Considerations](https://doc.qt.io/qtforpython-6/deployment/deployment-pyside6-deploy.html#considerations)
    *   [Creating a bug report](https://doc.qt.io/qtforpython-6/deployment/deployment-pyside6-deploy.html#creating-a-bug-report)

*   [pyside6-android-deploy: the Android deployment tool for Qt for Python](https://doc.qt.io/qtforpython-6/deployment/deployment-pyside6-android-deploy.html)
    *   [Prerequisites](https://doc.qt.io/qtforpython-6/deployment/deployment-pyside6-android-deploy.html#prerequisites)
    *   [How to use it?](https://doc.qt.io/qtforpython-6/deployment/deployment-pyside6-android-deploy.html#how-to-use-it)
    *   [pysidedeploy.spec](https://doc.qt.io/qtforpython-6/deployment/deployment-pyside6-android-deploy.html#pysidedeploy-spec)
    *   [Command Line Options](https://doc.qt.io/qtforpython-6/deployment/deployment-pyside6-android-deploy.html#command-line-options)
    *   [Cross-compile Qt for Python wheels for Android](https://doc.qt.io/qtforpython-6/deployment/deployment-pyside6-android-deploy.html#cross-compile-qt-for-python-wheels-for-android)

*   [Qt for Python & fbs](https://doc.qt.io/qtforpython-6/deployment/deployment-fbs.html)
    *   [Preparation](https://doc.qt.io/qtforpython-6/deployment/deployment-fbs.html#preparation)
    *   [Starting a new project](https://doc.qt.io/qtforpython-6/deployment/deployment-fbs.html#starting-a-new-project)
    *   [Freezing the application](https://doc.qt.io/qtforpython-6/deployment/deployment-fbs.html#freezing-the-application)

*   [Qt for Python & PyInstaller](https://doc.qt.io/qtforpython-6/deployment/deployment-pyinstaller.html)
    *   [Status of Qt 6 Support](https://doc.qt.io/qtforpython-6/deployment/deployment-pyinstaller.html#status-of-qt-6-support)
    *   [Preparation](https://doc.qt.io/qtforpython-6/deployment/deployment-pyinstaller.html#preparation)
    *   [Freeze an application](https://doc.qt.io/qtforpython-6/deployment/deployment-pyinstaller.html#freeze-an-application)
    *   [Some Caveats](https://doc.qt.io/qtforpython-6/deployment/deployment-pyinstaller.html#some-caveats)

*   [Qt for Python & cx_Freeze](https://doc.qt.io/qtforpython-6/deployment/deployment-cxfreeze.html)
    *   [Preparation](https://doc.qt.io/qtforpython-6/deployment/deployment-cxfreeze.html#preparation)
    *   [Freezing an application](https://doc.qt.io/qtforpython-6/deployment/deployment-cxfreeze.html#freezing-an-application)

*   [Qt for Python & Briefcase](https://doc.qt.io/qtforpython-6/deployment/deployment-briefcase.html)
    *   [Status of Qt 6 Support](https://doc.qt.io/qtforpython-6/deployment/deployment-briefcase.html#status-of-qt-6-support)
    *   [Preparation](https://doc.qt.io/qtforpython-6/deployment/deployment-briefcase.html#preparation)
    *   [Use Briefcase Assistant](https://doc.qt.io/qtforpython-6/deployment/deployment-briefcase.html#use-briefcase-assistant)
    *   [Set up your project](https://doc.qt.io/qtforpython-6/deployment/deployment-briefcase.html#set-up-your-project)
    *   [Build the package](https://doc.qt.io/qtforpython-6/deployment/deployment-briefcase.html#build-the-package)

*   [Qt for Python & py2exe](https://doc.qt.io/qtforpython-6/deployment/deployment-py2exe.html)
*   [Qt for Python & Nuitka](https://doc.qt.io/qtforpython-6/deployment/deployment-nuitka.html)
    *   [Preparation](https://doc.qt.io/qtforpython-6/deployment/deployment-nuitka.html#preparation)
    *   [Freeze an application](https://doc.qt.io/qtforpython-6/deployment/deployment-nuitka.html#freeze-an-application)
