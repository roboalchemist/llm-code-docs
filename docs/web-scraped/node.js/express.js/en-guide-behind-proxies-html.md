# Source: https://expressjs.com/en/guide/behind-proxies.html

Title: Express behind proxies

URL Source: https://expressjs.com/en/guide/behind-proxies.html

Published Time: Tue, 03 Mar 2026 11:18:16 GMT

Markdown Content:
Express behind proxies
===============

[](https://expressjs.com/ "Go to homepage")

*   [Getting started](https://expressjs.com/en/starter/installing.html)
    *   [Installing](https://expressjs.com/en/starter/installing.html)
    *   [Hello world](https://expressjs.com/en/starter/hello-world.html)
    *   [Express generator](https://expressjs.com/en/starter/generator.html)
    *   [Basic routing](https://expressjs.com/en/starter/basic-routing.html)
    *   [Static files](https://expressjs.com/en/starter/static-files.html)
    *   [More examples](https://expressjs.com/en/starter/examples.html)
    *   [FAQ](https://expressjs.com/en/starter/faq.html)

*   [Guide](https://expressjs.com/en/guide/routing.html)
    *   [Routing](https://expressjs.com/en/guide/routing.html)
    *   [Writing middleware](https://expressjs.com/en/guide/writing-middleware.html)
    *   [Using middleware](https://expressjs.com/en/guide/using-middleware.html)
    *   [Overriding the Express API](https://expressjs.com/en/guide/overriding-express-api.html)
    *   [Using template engines](https://expressjs.com/en/guide/using-template-engines.html)
    *   [Error handling](https://expressjs.com/en/guide/error-handling.html)
    *   [Debugging](https://expressjs.com/en/guide/debugging.html)
    *   [Express behind proxies](https://expressjs.com/en/guide/behind-proxies.html)
    *   [Moving to Express 4](https://expressjs.com/en/guide/migrating-4.html)
    *   [Moving to Express 5](https://expressjs.com/en/guide/migrating-5.html)
    *   [Database integration](https://expressjs.com/en/guide/database-integration.html)

*   [API reference](https://expressjs.com/en/5x/api.html)
    *   [5.x](https://expressjs.com/en/5x/api.html)
    *   [4.x](https://expressjs.com/en/4x/api.html)
    *   [3.x (deprecated)](https://expressjs.com/en/3x/api.html)
    *   [2.x (deprecated)](https://expressjs.com/2x/)

*   [Advanced topics](https://expressjs.com/en/advanced/developing-template-engines.html)
    *   [Building template engines](https://expressjs.com/en/advanced/developing-template-engines.html)
    *   [Security updates](https://expressjs.com/en/advanced/security-updates.html)
    *   [Security best practices](https://expressjs.com/en/advanced/best-practice-security.html)
    *   [Performance best practices](https://expressjs.com/en/advanced/best-practice-performance.html)
    *   [Health checks & shutdown](https://expressjs.com/en/advanced/healthcheck-graceful-shutdown.html)

*   [Resources](https://expressjs.com/en/resources/community.html)
    *   [Community](https://expressjs.com/en/resources/community.html)
    *   [Glossary](https://expressjs.com/en/resources/glossary.html)
    *   [Middleware](https://expressjs.com/en/resources/middleware.html)
    *   [Utility modules](https://expressjs.com/en/resources/utils.html)
    *   [Contributing to Express](https://expressjs.com/en/resources/contributing.html)
    *   [Release Change Log](https://github.com/expressjs/express/releases)

*   [Support](https://expressjs.com/en/support)
*   [Blog](https://expressjs.com/2026/02/27/security-releases.html)
    *   [Latest post](https://expressjs.com/2026/02/27/security-releases.html)
    *   [All posts](https://expressjs.com/en/blog/posts.html)
    *   [Write a Post](https://expressjs.com/en/blog/write-post.html)

*   [**English**](https://expressjs.com/en/guide/behind-proxies.html)
*   [Français](https://expressjs.com/fr/guide/behind-proxies.html)
*   [Deutsch](https://expressjs.com/de/guide/behind-proxies.html)
*   [Español](https://expressjs.com/es/guide/behind-proxies.html)
*   [Italiano](https://expressjs.com/it/guide/behind-proxies.html)
*   [日本語](https://expressjs.com/ja/guide/behind-proxies.html)
*   [中文 (简体)](https://expressjs.com/zh-cn/guide/behind-proxies.html)
*   [繁體中文](https://expressjs.com/zh-tw/guide/behind-proxies.html)
*   [한국어](https://expressjs.com/ko/guide/behind-proxies.html)
*   [Português](https://expressjs.com/pt-br/guide/behind-proxies.html)

Express behind proxies
======================

When running an Express app behind a reverse proxy, some of the Express APIs may return different values than expected. In order to adjust for this, the 
```plaintext
trust proxy
```
 application setting may be used to expose information provided by the reverse proxy in the Express APIs. The most common issue is express APIs that expose the client’s IP address may instead show an internal IP address of the reverse proxy.

When configuring the 
```plaintext
trust proxy
```
 setting, it is important to understand the exact setup of the reverse proxy. Since this setting will trust values provided in the request, it is important that the combination of the setting in Express matches how the reverse proxy operates.

The application setting 
```plaintext
trust proxy
```
 may be set to one of the values listed in the following table.

| Type | Value |
| --- | --- |
| Boolean | If ```plaintext true ``` , the client’s IP address is understood as the left-most entry in the ```plaintext X-Forwarded-For ``` header. If ```plaintext false ``` , the app is understood as directly facing the client and the client’s IP address is derived from ```plaintext req.socket.remoteAddress ``` . This is the default setting. When setting to ```plaintext true ``` , it is important to ensure that the last reverse proxy trusted is removing/overwriting all of the following HTTP headers: ```plaintext X-Forwarded-For ``` , ```plaintext X-Forwarded-Host ``` , and ```plaintext X-Forwarded-Proto ``` , otherwise it may be possible for the client to provide any value. |
| IP addresses | An IP address, subnet, or an array of IP addresses and subnets to trust as being a reverse proxy. The following list shows the pre-configured subnet names: * loopback - ```plaintext 127.0.0.1/8 ``` , ```plaintext ::1/128 ``` * linklocal - ```plaintext 169.254.0.0/16 ``` , ```plaintext fe80::/10 ``` * uniquelocal - ```plaintext 10.0.0.0/8 ``` , ```plaintext 172.16.0.0/12 ``` , ```plaintext 192.168.0.0/16 ``` , ```plaintext fc00::/7 ``` You can set IP addresses in any of the following ways: ``` app.set('trust proxy', 'loopback') // specify a single subnet app.set('trust proxy', 'loopback, 123.123.123.123') // specify a subnet and an address app.set('trust proxy', 'loopback, linklocal, uniquelocal') // specify multiple subnets as CSV app.set('trust proxy', ['loopback', 'linklocal', 'uniquelocal']) // specify multiple subnets as an array ``` When specified, the IP addresses or the subnets are excluded from the address determination process, and the untrusted IP address nearest to the application server is determined as the client’s IP address. This works by checking if ```plaintext req.socket.remoteAddress ``` is trusted. If so, then each address in ```plaintext X-Forwarded-For ``` is checked from right to left until the first non-trusted address. |
| Number | Use the address that is at most ```plaintext n ``` number of hops away from the Express application. ```plaintext req.socket.remoteAddress ``` is the first hop, and the rest are looked for in the ```plaintext X-Forwarded-For ``` header from right to left. A value of ```plaintext 0 ``` means that the first untrusted address would be ```plaintext req.socket.remoteAddress ``` , i.e. there is no reverse proxy. When using this setting, it is important to ensure there are not multiple, different-length paths to the Express application such that the client can be less than the configured number of hops away, otherwise it may be possible for the client to provide any value. |
| Function | Custom trust implementation. ``` app.set('trust proxy', (ip) => { if (ip === '127.0.0.1' || ip === '123.123.123.123') return true // trusted IPs else return false }) ``` |

Enabling 
```plaintext
trust proxy
```
 will have the following impact:

*   The value of [req.hostname](https://expressjs.com/en/api.html#req.hostname) is derived from the value set in the 
```plaintext
X-Forwarded-Host
```
 header, which can be set by the client or by the proxy.

*   ```plaintext
X-Forwarded-Proto
```
 can be set by the reverse proxy to tell the app whether it is 
```plaintext
https
```
 or 
```plaintext
http
```
 or even an invalid name. This value is reflected by [req.protocol](https://expressjs.com/en/api.html#req.protocol).

*   The [req.ip](https://expressjs.com/en/api.html#req.ip) and [req.ips](https://expressjs.com/en/api.html#req.ips) values are populated based on the socket address and 
```plaintext
X-Forwarded-For
```
 header, starting at the first untrusted address.

The 
```plaintext
trust proxy
```
 setting is implemented using the [proxy-addr](https://www.npmjs.com/package/proxy-addr) package. For more information, see its documentation.

[Previous: Debugging Express](https://expressjs.com/en/guide/debugging.html)[Next: Migrating to Express 4](https://expressjs.com/en/guide/migrating-4.html)[Edit this page](https://github.com/expressjs/expressjs.com/edit/gh-pages/en/guide/behind-proxies.md)

[](https://expressjs.com/en/guide/behind-proxies.html#)

[](https://openjsf.org/ "OpenJS Foundation")
Copyright [OpenJS Foundation](https://openjsf.org/) and Express contributors. All rights reserved. The [OpenJS Foundation](https://openjsf.org/) has registered trademarks and uses trademarks. For a list of trademarks of the [OpenJS Foundation](https://openjsf.org/), please see our [Trademark Policy](https://trademark-policy.openjsf.org/) and [Trademark List](https://trademark-list.openjsf.org/). Trademarks and logos not indicated on the [list of OpenJS Foundation trademarks](https://trademark-list.openjsf.org/) are trademarks™ or registered® trademarks of their respective holders. Use of them does not imply any affiliation with or endorsement by them.

[Terms of Use](https://terms-of-use.openjsf.org/)[Privacy Policy](https://privacy-policy.openjsf.org/)[Code of Conduct](https://github.com/expressjs/.github/blob/HEAD/CODE_OF_CONDUCT.md)[Trademark Policy](https://trademark-policy.openjsf.org/)[Security Policy](https://github.com/expressjs/express/security/policy)

[](https://github.com/expressjs/express)

[](https://www.youtube.com/channel/UCYjxjAeH6TRik9Iwy5nXw7g)

[](https://x.com/UseExpressJS)

[](https://openjs-foundation.slack.com/archives/C02QB1731FH)

[](https://opencollective.com/express)

[](https://bsky.app/profile/expressjs.bsky.social)

[![Image 1: Preview Deploys by Netlify](https://www.netlify.com/v3/img/components/netlify-color-accent.svg)](https://www.netlify.com/)
