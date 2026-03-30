# Source: https://socket.io/docs/v4/changelog/

Title: Changelog | Socket.IO

URL Source: https://socket.io/docs/v4/changelog/

Markdown Content:
*   [](https://socket.io/)
*   Changelog

Version: 4.x

Versioning Policy[​](https://socket.io/docs/v4/changelog/#versioning-policy "Direct link to Versioning Policy")
---------------------------------------------------------------------------------------------------------------

Socket.IO releases closely follow [Semantic Versioning](https://semver.org/).

That means that with a version number `x.y.z`:

*   when releasing critical bug fixes, we make a patch release by increasing the `z` number (ex: `1.2.3` to `1.2.4`).
*   when releasing new features or non-critical fixes, we make a minor release by increasing the `y` number (ex: `1.2.3` to `1.3.0`).
*   when releasing breaking changes, we make a major release by increasing the `x` number (ex: `1.2.3` to `2.0.0`).

Breaking changes[​](https://socket.io/docs/v4/changelog/#breaking-changes "Direct link to Breaking changes")
------------------------------------------------------------------------------------------------------------

Breaking changes are inconvenient for everyone, so we try to minimize the number of major releases.

We have had two major breaking changes impacting the Socket.IO protocol over the years:

*   Socket.IO v2 was released in **May 2017**
*   Socket.IO v3 was released in **November 2020**

info

Socket.IO v4 (released in March 2021) did not include any update to the Socket.IO protocol (only a couple of breaking changes in the Node.js server API), so it isn't counted here.

Reference: [Migrating from 3.x to 4.0](https://socket.io/docs/v4/migrating-from-3-x-to-4-0/)

Important milestones[​](https://socket.io/docs/v4/changelog/#important-milestones "Direct link to Important milestones")
------------------------------------------------------------------------------------------------------------------------

Aside from the breaking changes listed above, here are the latest important changes in Socket.IO:

| Version | Date | Description |
| --- | --- | --- |
| [`4.7.0`](https://socket.io/docs/v4/changelog/4.7.0) | June 2023 | Support for WebTransport |
| [`4.6.0`](https://socket.io/docs/v4/changelog/4.6.0) | February 2023 | Introduction of [Connection state recovery](https://socket.io/docs/v4/connection-state-recovery) |
| `4.4.0` | November 2021 | Support for [uWebSockets.js](https://socket.io/docs/v4/server-installation/#usage-with-uwebsockets) |
| `4.1.0` | May 2021 | Introduction of [`serverSideEmit()`](https://socket.io/docs/v4/server-instance/#serversideemit) |
| `4.0.0` | March 2021 | Rewrite to [TypeScript](https://www.typescriptlang.org/) |

Version usage[​](https://socket.io/docs/v4/changelog/#version-usage "Direct link to Version usage")
---------------------------------------------------------------------------------------------------

As of June 2024:

`socket.io` package

![Image 1: Client downloads per version](https://socket.io/images/server-downloads-per-version.png)

`socket.io-client` package

![Image 2: Client downloads per version](https://socket.io/images/client-downloads-per-version.png)

[Next 4.8.3 (December 23, 2025)](https://socket.io/docs/v4/changelog/4.8.3)
