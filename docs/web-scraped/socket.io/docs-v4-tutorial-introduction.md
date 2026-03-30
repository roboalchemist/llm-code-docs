# Source: https://socket.io/docs/v4/tutorial/introduction

Title: Tutorial - Introduction | Socket.IO

URL Source: https://socket.io/docs/v4/tutorial/introduction

Markdown Content:
Tutorial - Introduction | Socket.IO
===============

[Skip to main content](https://socket.io/docs/v4/tutorial/introduction#__docusaurus_skipToContent_fallback)

Latest blog post (July 25, 2024): [npm package provenance](https://socket.io/blog/npm-package-provenance/).

[![Image 2: Socket.IO logo](https://socket.io/images/logo.svg) **Socket.IO**](https://socket.io/)

[Docs](https://socket.io/docs/v4/tutorial/introduction#)
*   [Guide](https://socket.io/docs/v4/)
*   [Tutorial](https://socket.io/docs/v4/tutorial/introduction)
*   [Examples](https://socket.io/get-started/)
*   [Emit cheatsheet](https://socket.io/docs/v4/emit-cheatsheet/)

[Server API](https://socket.io/docs/v4/server-api/)[Client API](https://socket.io/docs/v4/client-api/)

[Ecosystem](https://socket.io/docs/v4/tutorial/introduction#)
*   **Help**
*   [Troubleshooting](https://socket.io/docs/v4/troubleshooting-connection-issues/)
*   [Stack Overflow](https://stackoverflow.com/questions/tagged/socket.io)
*   [GitHub Discussions](https://github.com/socketio/socket.io/discussions)
*   [Slack](https://socketio-slackin.herokuapp.com/)
*   
* * *

*   **News**
*   [Blog](https://socket.io/blog)
*   [Twitter](https://twitter.com/SocketIO)
*   
* * *

*   **Tools**
*   [CDN](https://cdn.socket.io/)
*   [Admin UI](https://admin.socket.io/)

[About](https://socket.io/docs/v4/tutorial/introduction#)
*   [FAQ](https://socket.io/docs/v4/faq/)
*   [Changelog](https://socket.io/docs/v4/changelog/)
*   [Roadmap](https://github.com/orgs/socketio/projects/3)
*   [Become a sponsor](https://opencollective.com/socketio)

[4.x](https://socket.io/docs/v4/)
*   [4.x](https://socket.io/docs/v4/tutorial/introduction)
*   [3.x](https://socket.io/docs/v3/)
*   [2.x](https://socket.io/docs/v2/)
*   
* * *

*   [Changelog](https://socket.io/docs/v4/changelog/)

[English](https://socket.io/docs/v4/tutorial/introduction#)
*   [English](https://socket.io/docs/v4/tutorial/introduction)
*   [Español](https://socket.io/es/docs/v4/tutorial/introduction)
*   [Français](https://socket.io/fr/docs/v4/tutorial/introduction)
*   [Português (Brasil)](https://socket.io/pt-br/docs/v4/tutorial/introduction)
*   [中文（中国）](https://socket.io/zh-CN/docs/v4/tutorial/introduction)

[](https://github.com/socketio/socket.io)

Search K

[![Image 3: Socket.IO logo](https://socket.io/images/logo.svg)**Socket.IO**](https://socket.io/)
*   [Introduction](https://socket.io/docs/v4/tutorial/introduction)
*   [Step #1: Project initialization](https://socket.io/docs/v4/tutorial/step-1)
*   [Step #2: Serving HTML](https://socket.io/docs/v4/tutorial/step-2)
*   [Step #3: Integrating Socket.IO](https://socket.io/docs/v4/tutorial/step-3)
*   [Step #4: Emitting events](https://socket.io/docs/v4/tutorial/step-4)
*   [Step #5: Broadcasting](https://socket.io/docs/v4/tutorial/step-5)
*   [Overview of the API](https://socket.io/docs/v4/tutorial/api-overview)
*   [Handling disconnections](https://socket.io/docs/v4/tutorial/handling-disconnections)
*   [Step #6: Connection state recovery](https://socket.io/docs/v4/tutorial/step-6)
*   [Step #7: Server delivery](https://socket.io/docs/v4/tutorial/step-7)
*   [Step #8: Client delivery](https://socket.io/docs/v4/tutorial/step-8)
*   [Step #9: Scaling horizontally](https://socket.io/docs/v4/tutorial/step-9)
*   [Ending notes](https://socket.io/docs/v4/tutorial/ending-notes)

*   [](https://socket.io/)
*   Introduction

Version: 4.x

On this page

Getting started
===============

Welcome to the Socket.IO tutorial!

In this tutorial we'll create a basic chat application. It requires almost no basic prior knowledge of Node.JS or Socket.IO, so it’s ideal for users of all knowledge levels.

Introduction[​](https://socket.io/docs/v4/tutorial/introduction#introduction "Direct link to Introduction")
-----------------------------------------------------------------------------------------------------------

Writing a chat application with popular web applications stacks like LAMP (PHP) has normally been very hard. It involves polling the server for changes, keeping track of timestamps, and it’s a lot slower than it should be.

Sockets have traditionally been the solution around which most real-time chat systems are architected, providing a bi-directional communication channel between a client and a server.

This means that the server can _push_ messages to clients. Whenever you write a chat message, the idea is that the server will get it and push it to all other connected clients.

How to use this tutorial[​](https://socket.io/docs/v4/tutorial/introduction#how-to-use-this-tutorial "Direct link to How to use this tutorial")
-----------------------------------------------------------------------------------------------------------------------------------------------

### Tooling[​](https://socket.io/docs/v4/tutorial/introduction#tooling "Direct link to Tooling")

Any text editor (from a basic text editor to a complete IDE such as [VS Code](https://code.visualstudio.com/)) should be sufficient to complete this tutorial.

Additionally, at the end of each step you will find a link to some online platforms ([CodeSandbox](https://codesandbox.io/) and [StackBlitz](https://stackblitz.com/), namely), allowing you to run the code directly from your browser:

![Image 4: Screenshot of the CodeSandbox platform](https://socket.io/assets/images/codesandbox-2e332899094eb186d2e1ced75ac2cded.png)

### Syntax settings[​](https://socket.io/docs/v4/tutorial/introduction#syntax-settings "Direct link to Syntax settings")

In the Node.js world, there are two ways to import modules:

*   the standard way: ECMAScript modules (or ESM)

`import { Server } from "socket.io";`

Reference: [https://nodejs.org/api/esm.html](https://nodejs.org/api/esm.html)

*   the legacy way: CommonJS

`const { Server } = require("socket.io");`

Reference: [https://nodejs.org/api/modules.html](https://nodejs.org/api/modules.html)

Socket.IO supports both syntax.

tip

We recommend using the ESM syntax in your project, though this might not always be feasible due to some packages not supporting this syntax.

For your convenience, throughout the tutorial, each code block allows you to select your preferred syntax:

*   CommonJS
*   ES modules

`const { Server } = require("socket.io");`

`import { Server } from "socket.io";`

Ready? Click "Next" to get started.

[Edit this page](https://github.com/socketio/socket.io-website/edit/main/docs/tutorial/01-introduction.md)

Last updated on **Jan 22, 2026**

[Next Step #1: Project initialization](https://socket.io/docs/v4/tutorial/step-1)

*   [Introduction](https://socket.io/docs/v4/tutorial/introduction#introduction)
*   [How to use this tutorial](https://socket.io/docs/v4/tutorial/introduction#how-to-use-this-tutorial)
    *   [Tooling](https://socket.io/docs/v4/tutorial/introduction#tooling)
    *   [Syntax settings](https://socket.io/docs/v4/tutorial/introduction#syntax-settings)

Documentation

*   [Guide](https://socket.io/docs/v4/)
*   [Tutorial](https://socket.io/docs/v4/tutorial/introduction)
*   [Examples](https://socket.io/get-started/)
*   [Server API](https://socket.io/docs/v4/server-api/)
*   [Client API](https://socket.io/docs/v4/client-api/)

Help

*   [Troubleshooting](https://socket.io/docs/v4/troubleshooting-connection-issues/)
*   [Stack Overflow](https://stackoverflow.com/questions/tagged/socket.io)
*   [GitHub Discussions](https://github.com/socketio/socket.io/discussions)
*   [Slack](https://socketio-slackin.herokuapp.com/)

News

*   [Blog](https://socket.io/blog)
*   [Twitter](https://twitter.com/SocketIO)

Tools

*   [CDN](https://cdn.socket.io/)
*   [Admin UI](https://admin.socket.io/)

About

*   [FAQ](https://socket.io/docs/v4/faq/)
*   [Changelog](https://socket.io/docs/v4/changelog/)
*   [Roadmap](https://github.com/orgs/socketio/projects/3)
*   [Become a sponsor](https://opencollective.com/socketio)

Copyright © 2026 Socket.IO
