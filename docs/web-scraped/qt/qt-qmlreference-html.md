# Source: https://doc.qt.io/qt/qmlreference.html

Title: The QML Reference | Qt Qml

URL Source: https://doc.qt.io/qt/qmlreference.html

Markdown Content:
The QML Reference | Qt Qml | Qt 6.10.2
===============

[Back to Qt.io](https://www.qt.io/)

[Contact Us](https://www.qt.io/contact-us/)[Blog](https://blog.qt.io/)[Download Qt](https://www.qt.io/download/)

[![Image 1: Qt documentation](https://doc.qt.io/style/qt-logo-documentation.png)](https://doc.qt.io/)

* [](https://doc.qt.io/qt/qmlreference.html)
  * [English](https://doc.qt.io/qt/qmlreference.html)
  * [中文](https://doc.qt.io/qt/qmlreference.html)
  * [日本語](https://doc.qt.io/qt/qmlreference.html)
  * [한국어](https://doc.qt.io/qt/qmlreference.html)
  * [Deutsch](https://doc.qt.io/qt/qmlreference.html)
  * [français](https://doc.qt.io/qt/qmlreference.html)
  * [italiano](https://doc.qt.io/qt/qmlreference.html)
  * [español](https://doc.qt.io/qt/qmlreference.html)
  * [português](https://doc.qt.io/qt/qmlreference.html)

* * [x]
* [Archives](https://doc.qt.io/archives)
* [Snapshots](https://doc-snapshots.qt.io/)

* [Reference](https://doc.qt.io/qt/reference-overview.html)
* [Getting Started](https://doc.qt.io/qt/gettingstarted.html)
* [What's new in Qt 6](https://doc.qt.io/qt/whatsnewqt6.html)
* [Product information](https://doc.qt.io/qt/qt-framework-product-information.html)
* [Overviews](https://doc.qt.io/qt/overviews.html)
* [List of Overviews](https://doc.qt.io/qt/overviews-main.html)
* [Qt Core](https://doc.qt.io/qt/qtcore-index.html)
* [Qt GUI](https://doc.qt.io/qt/qtgui-index.html)
* [Qt Network](https://doc.qt.io/qt/qtnetwork-index.html)
* [Qt Qml](https://doc.qt.io/qt/qtqml-index.html)
  * [The QML Reference](https://doc.qt.io/qt/qmlreference.html)
    * [QML Syntax Basics](https://doc.qt.io/qt/qtqml-syntax-basics.html)
    * [Import Statements](https://doc.qt.io/qt/qtqml-syntax-imports.html)
    * [Importing QML Document Directories](https://doc.qt.io/qt/qtqml-syntax-directoryimports.html)
    * [QML Object Attributes](https://doc.qt.io/qt/qtqml-syntax-objectattributes.html)
    * [Property Binding](https://doc.qt.io/qt/qtqml-syntax-propertybinding.html)
    * [Signal and Handler Event System](https://doc.qt.io/qt/qtqml-syntax-signals.html)
    * [The QML Type System](https://doc.qt.io/qt/qtqml-typesystem-topic.html)
    * [QML Modules](https://doc.qt.io/qt/qtqml-modules-topic.html)
    * [QML Documents](https://doc.qt.io/qt/qtqml-documents-topic.html)

  * [Singletons in QML](https://doc.qt.io/qt/qml-singleton.html)
  * [The QML Disk Cache](https://doc.qt.io/qt/qmldiskcache.html)
  * [QML and C++ Integration](https://doc.qt.io/qt/qtqml-cppintegration-overview.html)
  * [QML and JavaScript Integration](https://doc.qt.io/qt/qtqml-javascript-topic.html)
  * [Writing QML Modules](https://doc.qt.io/qt/qtqml-writing-a-module.html)
  * [Modern QML modules](https://doc.qt.io/qt/qt6-modernize-qml-modules.html)
  * [Prototyping with the QML Runtime Tool](https://doc.qt.io/qt/qtquick-qml-runtime.html)
  * [Debugging QML Applications](https://doc.qt.io/qt/qtquick-debugging.html)
  * [Deploying QML applications](https://doc.qt.io/qt/qtquick-deployment.html)
  * [Qt Qml Tooling](https://doc.qt.io/qt/qtqml-tooling.html)
  * [Upgrade from Qt 5](https://doc.qt.io/qt/qml-changes-qt6.html)
  * [QML Lint Warning and Errors](https://doc.qt.io/qt/qmllint-warnings-and-errors.html)
  * [CMake Global Properties](https://doc.qt.io/qt/cmake-global-properties-qtqml.html)
  * [CMake Source File Properties](https://doc.qt.io/qt/cmake-source-file-properties-qtqml.html)
  * [CMake Global Variables](https://doc.qt.io/qt/cmake-variables-qtqml.html)
  * [QML Types](https://doc.qt.io/qt/qtqml-qmlmodule.html)
  * [C++ Classes](https://doc.qt.io/qt/qtqml-module.html)
  * [Qt QML Compiler](https://doc.qt.io/qt/qtqmlcompiler-index.html)
  * [Qt Qml Core](https://doc.qt.io/qt/qtqmlcore-index.html)
  * [Qt Qml Models](https://doc.qt.io/qt/qtqmlmodels-index.html)
  * [Qt XmlListModel](https://doc.qt.io/qt/qml-xmllistmodel.html)
  * [Qt QML Network](https://doc.qt.io/qt/qtqmlnetwork-index.html)
  * [Qt Qml WorkerScript](https://doc.qt.io/qt/qmlworkerscript-index.html)

* [Qt Quick](https://doc.qt.io/qt/qtquick-index.html)
* [Qt Widgets](https://doc.qt.io/qt/qtwidgets-index.html)
* [Qt Test](https://doc.qt.io/qt/qttest-index.html)
* [Modules](https://doc.qt.io/qt/qt-additional-modules.html)
* [Tools and utilities](https://doc.qt.io/qt/qt-tools-utilities.html)

Search

* [Qt 6.10](https://doc.qt.io/qt/index.html)
* [Qt Qml](https://doc.qt.io/qt/qtqml-index.html)
* [The QML Reference](https://doc.qt.io/qt/qmlreference.html)

[QML Syntax Basics](https://doc.qt.io/qt/qtqml-syntax-basics.html)

The QML Reference
=================

QML is a multi-paradigm language for creating highly dynamic applications. With QML, application building blocks such as UI components are _declared_ and various properties set to define the application behavior. Application behavior can be further scripted through JavaScript, which is a subset of the language. In addition, QML heavily uses Qt, which allows types and other Qt features to be accessible directly from QML applications.

This reference guide describes the features of the QML language. Many of the QML types in the guide originate from the [Qt Qml](https://doc.qt.io/qt/qtqml-index.html) or [Qt Quick](https://doc.qt.io/qt/qtquick-index.html) modules.

* [QML Syntax Basics](https://doc.qt.io/qt/qtqml-syntax-basics.html)
  * [Import Statements](https://doc.qt.io/qt/qtqml-syntax-imports.html)
  * [Object Declarations](https://doc.qt.io/qt/qtqml-syntax-basics.html#object-declarations)
    * [Child Objects](https://doc.qt.io/qt/qtqml-syntax-basics.html#child-objects)

  * [Comments](https://doc.qt.io/qt/qtqml-syntax-basics.html#comments)

* [QML Object Attributes](https://doc.qt.io/qt/qtqml-syntax-objectattributes.html)
  * [The _id_ Attribute](https://doc.qt.io/qt/qtqml-syntax-objectattributes.html#the-id-attribute)
  * [Property Attributes](https://doc.qt.io/qt/qtqml-syntax-objectattributes.html#property-attributes)
  * [Signal Attributes](https://doc.qt.io/qt/qtqml-syntax-objectattributes.html#signal-attributes)
  * [Method Attributes](https://doc.qt.io/qt/qtqml-syntax-objectattributes.html#method-attributes)
  * [Attached Properties and Attached Signal Handlers](https://doc.qt.io/qt/qtqml-syntax-objectattributes.html#attached-properties-and-attached-signal-handlers)
  * [Enumeration Attributes](https://doc.qt.io/qt/qtqml-syntax-objectattributes.html#enumeration-attributes)

* [Property Binding](https://doc.qt.io/qt/qtqml-syntax-propertybinding.html)
* [Signal and Handler Event System](https://doc.qt.io/qt/qtqml-syntax-signals.html)
* [Integrating QML and JavaScript](https://doc.qt.io/qt/qtqml-javascript-topic.html)
  * [Using JavaScript Expressions with QML](https://doc.qt.io/qt/qtqml-javascript-expressions.html)
  * [Dynamic QML Object Creation from JavaScript](https://doc.qt.io/qt/qtqml-javascript-dynamicobjectcreation.html)
  * [Defining JavaScript Resources In QML](https://doc.qt.io/qt/qtqml-javascript-resources.html)
  * [Importing JavaScript Resources In QML](https://doc.qt.io/qt/qtqml-javascript-imports.html)
  * [JavaScript Host Environment](https://doc.qt.io/qt/qtqml-javascript-hostenvironment.html)
  * [Configuring the JavaScript engine](https://doc.qt.io/qt/qtqml-javascript-finetuning.html)

* [The QML Type System](https://doc.qt.io/qt/qtqml-typesystem-topic.html)
  * [QML Value Types](https://doc.qt.io/qt/qtqml-typesystem-valuetypes.html)
  * [JavaScript Types](https://doc.qt.io/qt/qtqml-typesystem-topic.html#javascript-types)
  * [QML Object Types](https://doc.qt.io/qt/qtqml-typesystem-objecttypes.html)
    * [Defining Object Types from QML](https://doc.qt.io/qt/qtqml-documents-definetypes.html)
    * [Defining Object Types from C++](https://doc.qt.io/qt/qtqml-cppintegration-definetypes.html)

  * [QML Sequence Types](https://doc.qt.io/qt/qtqml-typesystem-sequencetypes.html)
  * [QML Namespaces](https://doc.qt.io/qt/qtqml-typesystem-namespaces.html)

* [QML Modules](https://doc.qt.io/qt/qtqml-modules-topic.html)
  * [Specifying A QML Module](https://doc.qt.io/qt/qtqml-modules-qmldir.html)
  * [Supported QML Module Types](https://doc.qt.io/qt/qtqml-modules-topic.html#supported-qml-module-types)
    * [Identified Modules](https://doc.qt.io/qt/qtqml-modules-identifiedmodules.html)
    * [Legacy Modules](https://doc.qt.io/qt/qtqml-modules-legacymodules.html)

  * [Providing Types and Functionality in a C++ Plugin](https://doc.qt.io/qt/qtqml-modules-cppplugins.html)

* [QML Documents](https://doc.qt.io/qt/qtqml-documents-topic.html)
  * [Structure of a QML Document](https://doc.qt.io/qt/qtqml-documents-structure.html)
  * [Syntax of the QML Language](https://doc.qt.io/qt/qtqml-documents-topic.html#syntax-of-the-qml-language)
  * [Defining Object Types through QML Documents](https://doc.qt.io/qt/qtqml-documents-definetypes.html)
    * [Defining an Object Type with a QML File](https://doc.qt.io/qt/qtqml-documents-definetypes.html#defining-an-object-type-with-a-qml-file)
    * [Accessible Attributes of Custom Types](https://doc.qt.io/qt/qtqml-documents-definetypes.html#accessible-attributes-of-custom-types)

  * [Resource Loading and Network Transparency](https://doc.qt.io/qt/qtqml-documents-networktransparency.html)
  * [Scope and Naming Resolution](https://doc.qt.io/qt/qtqml-documents-scope.html)

[QML Syntax Basics](https://doc.qt.io/qt/qtqml-syntax-basics.html)

© 2026 The Qt Company Ltd. Documentation contributions included herein are the copyrights of their respective owners. The documentation provided herein is licensed under the terms of the [GNU Free Documentation License version 1.3](http://www.gnu.org/licenses/fdl.html) as published by the Free Software Foundation. Qt and respective logos are [trademarks](https://doc.qt.io/qt/trademarks.html) of The Qt Company Ltd. in Finland and/or other countries worldwide. All other trademarks are property of their respective owners.

###### **Next**

* [QML Syntax Basics](https://doc.qt.io/qt/qtqml-syntax-basics.html)

[![Image 2](https://doc.qt.io/images/qtgroup.svg)](https://www.qt.io/?hsLang=en)

[](https://twitter.com/qtproject)[](https://www.facebook.com/qt/)[](https://www.youtube.com/user/QtStudios)[](https://www.linkedin.com/company/qtgroup/)

[Contact Us](https://www.qt.io/contact-us?hsLang=en)

* [Qt Group](javascript:;)
  * [Our Story](https://www.qt.io/group)
  * [Brand](https://www.qt.io/brand)
  * [News](https://www.qt.io/newsroom)
  * [Careers](https://www.qt.io/careers)
  * [Investors](https://www.qt.io/investors)
  * [Qt Products](https://www.qt.io/product)
  * [Quality Assurance Products](https://www.qt.io/product/quality-assurance)

* [Licensing](javascript:;)
  * [License Agreement](https://www.qt.io/terms-conditions)
  * [Open Source](https://www.qt.io/licensing/open-source-lgpl-obligations)
  * [Plans and pricing](https://www.qt.io/pricing)
  * [Download](https://www.qt.io/download)
  * [FAQ](https://www.qt.io/faq/overview)

* [Learn Qt](javascript:;)
  * [For Learners](https://www.qt.io/academy)
  * [For Students and Teachers](https://www.qt.io/qt-educational-license)
  * [Qt Documentation](https://doc.qt.io/)
  * [Qt Forum](https://forum.qt.io/)

* [Support & Services](javascript:;)
  * [Professional Services](https://www.qt.io/qt-professional-services)
  * [Customer Success](https://www.qt.io/customer-success)
  * [Support Services](https://www.qt.io/qt-support/)
  * [Partners](https://www.qt.io/contact-us/partners)
  * [Qt World](https://www.qt.io/qt-world)

* [© 2026 The Qt Company](javascript:;)
* [Feedback](mailto:feedback@qt.io?Subject=Feedback%20about%20doc.qt.io%20site)

Qt Group includes The Qt Company Oy and its global subsidiaries and affiliates.

[](https://doc.qt.io/qt/qmlreference.html)
