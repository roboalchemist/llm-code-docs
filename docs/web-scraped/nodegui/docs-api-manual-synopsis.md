# Source: https://nodegui.org/docs/api/manual/synopsis

Title: Synopsis | NodeGui

URL Source: https://nodegui.org/docs/api/manual/synopsis

Markdown Content:
Synopsis | NodeGui
===============

[Skip to main content](https://nodegui.org/docs/api/manual/synopsis#__docusaurus_skipToContent_fallback)

[![Image 1: NodeGui Logo](https://nodegui.org/img/logo-circle.png) **NodeGui**](https://nodegui.org/)

[Docs](https://nodegui.org/docs/guides/getting-started)[API](https://nodegui.org/docs/api/manual/synopsis)[Blog](https://nodegui.org/blog)[GitHub](https://github.com/nodegui/nodegui)

Search K

*   [Intro](https://nodegui.org/docs/api/manual/synopsis#) 
    *   [Synopsis](https://nodegui.org/docs/api/manual/synopsis)

*   [Classes](https://nodegui.org/docs/api/manual/synopsis#) 
*   [Enums](https://nodegui.org/docs/api/manual/synopsis#) 
*   [Interfaces](https://nodegui.org/docs/api/manual/synopsis#) 
*   [Others](https://nodegui.org/docs/api/manual/synopsis#) 

*   [](https://nodegui.org/)
*   Intro
*   Synopsis

On this page

Synopsis
========

> How to use Node.js and NodeGui's APIs.

All of [Node.js's built-in modules](https://nodejs.org/api/) are available in NodeGui. Also, third-party node modules that are known to work with Node.Js are fully supported as well (including the native node modules).

Apart from Node.Js ecosystem, NodeGui also provides some extra built-in widget and modules for developing native desktop applications. So, you can think of NodeGui as NodeJs + Gui Widgets powered by Qt.

The app script is like a normal Node.js script:

`const { QMainWindow } = require("@nodegui/nodegui");const win = new QMainWindow();win.show();global.win = win; // To prevent win from being garbage collected.`

To run your app, read [Run your app](https://nodegui.org/docs/guides/tutorial).

Destructuring assignment[​](https://nodegui.org/docs/api/manual/synopsis#destructuring-assignment "Direct link to Destructuring assignment")
--------------------------------------------------------------------------------------------------------------------------------------------

You can use [destructuring assignment](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment) to make it easier to use built-in modules.

`const {  QMainWindow,  QWidget,  QLabel,  FlexLayout} = require("@nodegui/nodegui");const win = new QMainWindow();const centralWidget = new QWidget();centralWidget.setObjectName("myroot");const rootLayout = new FlexLayout();centralWidget.setLayout(rootLayout);const label = new QLabel();label.setInlineStyle("font-size: 16px; font-weight: bold;");label.setText("Hello World");rootLayout.addWidget(label);win.setCentralWidget(centralWidget);win.setStyleSheet(  `    #myroot {      background-color: #009688;    }  `);win.show();global.win = win;`

[Edit this page](https://github.com/nodegui/nodegui/edit/master/website/docs/api/manual/synopsis.md)

[Next CacheTestQObject](https://nodegui.org/docs/api/generated/classes/cachetestqobject)

*   [Destructuring assignment](https://nodegui.org/docs/api/manual/synopsis#destructuring-assignment)

Docs

*   [Getting Started](https://nodegui.org/docs/guides/getting-started)
*   [API](https://nodegui.org/docs/api/manual/synopsis)

Community

*   [Medium](https://medium.com/nodegui)

More

*   [Blog](https://nodegui.org/blog)
*   [React NodeGui](https://react.nodegui.org/)
*   [FAQ](https://nodegui.org/docs/faq)

Copyright © 2025 NodeGui
