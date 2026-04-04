# Source: https://socket.io/blog/chat-platform/

Title: Chat platform | Socket.IO

URL Source: https://socket.io/blog/chat-platform/

Published Time: 2024-01-12T00:00:00.000Z

Markdown Content:
Chat platform | Socket.IO
===============

[Skip to main content](https://socket.io/blog/chat-platform/#__docusaurus_skipToContent_fallback)

Latest blog post (July 25, 2024): [npm package provenance](https://socket.io/blog/npm-package-provenance/).

[![Image 3: Socket.IO logo](https://socket.io/images/logo.svg) **Socket.IO**](https://socket.io/)

[Docs](https://socket.io/blog/chat-platform/#)
*   [Guide](https://socket.io/docs/v4/)
*   [Tutorial](https://socket.io/docs/v4/tutorial/introduction)
*   [Examples](https://socket.io/get-started/)
*   [Emit cheatsheet](https://socket.io/docs/v4/emit-cheatsheet/)

[Server API](https://socket.io/docs/v4/server-api/)[Client API](https://socket.io/docs/v4/client-api/)

[Ecosystem](https://socket.io/blog/chat-platform/#)
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

[About](https://socket.io/blog/chat-platform/#)
*   [FAQ](https://socket.io/docs/v4/faq/)
*   [Changelog](https://socket.io/docs/v4/changelog/)
*   [Roadmap](https://github.com/orgs/socketio/projects/3)
*   [Become a sponsor](https://opencollective.com/socketio)

[4.x](https://socket.io/docs/v4/)
*   [4.x](https://socket.io/docs/v4/)
*   [3.x](https://socket.io/docs/v3/)
*   [2.x](https://socket.io/docs/v2/)
*   
* * *

*   [Changelog](https://socket.io/docs/v4/changelog/)

[English](https://socket.io/blog/chat-platform/#)
*   [English](https://socket.io/blog/chat-platform/)
*   [Español](https://socket.io/es/blog/chat-platform/)
*   [Français](https://socket.io/fr/blog/chat-platform/)
*   [Português (Brasil)](https://socket.io/pt-br/blog/chat-platform/)
*   [中文（中国）](https://socket.io/zh-CN/blog/chat-platform/)

[](https://github.com/socketio/socket.io)

Search K

Recent posts

*   [Bun engine](https://socket.io/blog/bun-engine/)
*   [npm package provenance](https://socket.io/blog/npm-package-provenance/)
*   [Socket.IO monorepo](https://socket.io/blog/monorepo/)
*   [Three new adapters](https://socket.io/blog/three-new-adapters/)
*   [Chat platform](https://socket.io/blog/chat-platform/)
*   [Socket.IO on Azure](https://socket.io/blog/socket-io-on-azure-preview/)
*   [Redis Streams adapter](https://socket.io/blog/socket-io-redis-streams-adapter/)
*   [Socket.IO server for Deno](https://socket.io/blog/socket-io-deno/)
*   [Socket.IO 4.5.0](https://socket.io/blog/socket-io-4-5-0/)
*   [Socket.IO 4.4.0](https://socket.io/blog/socket-io-4-4-0/)

Chat platform
=============

January 12, 2024 · 2 min read

[![Image 4: Damien Arrachequesne](https://github.com/darrachequesne.png)](https://github.com/darrachequesne)

[Damien Arrachequesne](https://github.com/darrachequesne)

Maintainer of Socket.IO

Hello everyone!

A new sample project is available: the **Chat platform**.

The source code can be found [here](https://github.com/socketio/socket.io-chat-platform).

for newcomers

Socket.IO is a library that enables low-latency, bidirectional and event-based communication between a client and a server.

To achieve this, it automatically selects the best available low-level transport between [WebTransport](https://developer.mozilla.org/en-US/docs/Web/API/WebTransport_API), [WebSocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) and HTTP long-polling, based on the capabilities of the client platform and the network.

Goal[​](https://socket.io/blog/chat-platform/#goal "Direct link to Goal")
-------------------------------------------------------------------------

The goal of this project is to provide a full-blown project based on Socket.IO with:

*   authentication/user registration
*   public and private messaging
*   proper reconnection management
*   presence management

The source code is provided with a permissive MIT license, so that you can use it/extend it to your will.

How to use[​](https://socket.io/blog/chat-platform/#how-to-use "Direct link to How to use")
-------------------------------------------------------------------------------------------

Check out the code [here](https://github.com/socketio/socket.io-chat-platform) and follow the instructions in the README.

Features[​](https://socket.io/blog/chat-platform/#features "Direct link to Features")
-------------------------------------------------------------------------------------

### Channel-based messages[​](https://socket.io/blog/chat-platform/#channel-based-messages "Direct link to Channel-based messages")

![Image 5: Screenshot of a public channel](https://socket.io/assets/images/channel_based_messages-e47afe4bd8d7b48f77493987d1cbdc23.png)

### Private messages[​](https://socket.io/blog/chat-platform/#private-messages "Direct link to Private messages")

![Image 6: Screenshot of a private channel](https://socket.io/assets/images/private_messages-da29f732b66ddc3c178de377d9ba6725.png)

Tools[​](https://socket.io/blog/chat-platform/#tools "Direct link to Tools")
----------------------------------------------------------------------------

### Server[​](https://socket.io/blog/chat-platform/#server "Direct link to Server")

The server is written in plain JavaScript, with the [`express`](https://expressjs.com/), `express-session` and [`passport`](https://www.passportjs.org/) packages. The database is [PostgreSQL](https://www.postgresql.org/).

### Client[​](https://socket.io/blog/chat-platform/#client "Direct link to Client")

The client is a [Vue.js](https://vuejs.org/) single-page application, with the [`vue-router`](https://router.vuejs.org/) and [`pinia`](https://pinia.vuejs.org/) packages. It uses [Bootstrap v5](https://getbootstrap.com/) for the styles.

Roadmap[​](https://socket.io/blog/chat-platform/#roadmap "Direct link to Roadmap")
----------------------------------------------------------------------------------

*   React client ([link](https://github.com/socketio/socket.io-chat-platform/issues/1))
*   MongoDB server ([link](https://github.com/socketio/socket.io-chat-platform/issues/2))

Any additional suggestion is welcome!

[Edit this page](https://github.com/socketio/socket.io-website/edit/main/blog/2024-01-12-chat-platform.md)

[Newer Post Three new adapters](https://socket.io/blog/three-new-adapters/)[Older Post Socket.IO on Azure](https://socket.io/blog/socket-io-on-azure-preview/)

*   [Goal](https://socket.io/blog/chat-platform/#goal)
*   [How to use](https://socket.io/blog/chat-platform/#how-to-use)
*   [Features](https://socket.io/blog/chat-platform/#features)
    *   [Channel-based messages](https://socket.io/blog/chat-platform/#channel-based-messages)
    *   [Private messages](https://socket.io/blog/chat-platform/#private-messages)

*   [Tools](https://socket.io/blog/chat-platform/#tools)
    *   [Server](https://socket.io/blog/chat-platform/#server)
    *   [Client](https://socket.io/blog/chat-platform/#client)

*   [Roadmap](https://socket.io/blog/chat-platform/#roadmap)

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
