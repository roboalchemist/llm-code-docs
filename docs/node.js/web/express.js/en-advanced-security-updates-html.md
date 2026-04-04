# Source: https://expressjs.com/en/advanced/security-updates.html

Title: Express security updates

URL Source: https://expressjs.com/en/advanced/security-updates.html

Published Time: Tue, 03 Mar 2026 11:18:16 GMT

Markdown Content:
Express security updates
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

*   [**English**](https://expressjs.com/en/advanced/security-updates.html)
*   [Français](https://expressjs.com/fr/advanced/security-updates.html)
*   [Deutsch](https://expressjs.com/de/advanced/security-updates.html)
*   [Español](https://expressjs.com/es/advanced/security-updates.html)
*   [Italiano](https://expressjs.com/it/advanced/security-updates.html)
*   [日本語](https://expressjs.com/ja/advanced/security-updates.html)
*   [中文 (简体)](https://expressjs.com/zh-cn/advanced/security-updates.html)
*   [繁體中文](https://expressjs.com/zh-tw/advanced/security-updates.html)
*   [한국어](https://expressjs.com/ko/advanced/security-updates.html)
*   [Português](https://expressjs.com/pt-br/advanced/security-updates.html)

Security updates
================

Node.js vulnerabilities directly affect Express. Therefore, [keep a watch on Node.js vulnerabilities](https://nodejs.org/en/blog/vulnerability/) and make sure you are using the latest stable version of Node.js.

The list below enumerates the Express vulnerabilities that were fixed in the specified version update.

Note

If you believe you have discovered a security vulnerability in Express, please see [Security Policies and Procedures](https://expressjs.com/en/resources/contributing.html#security-policies-and-procedures).

4.x
---

*   4.21.2 
    *   The dependency 
```plaintext
path-to-regexp
```
 has been updated to address a [vulnerability](https://github.com/pillarjs/path-to-regexp/security/advisories/GHSA-rhx6-c78j-4q9w).

*   4.21.1 
    *   The dependency 
```plaintext
cookie
```
 has been updated to address a [vulnerability](https://github.com/jshttp/cookie/security/advisories/GHSA-pxg6-pf52-xh8x), This may affect your application if you use 
```plaintext
res.cookie
```
.

*   4.20.0 
    *   Fixed XSS vulnerability in 
```plaintext
res.redirect
```
 ([advisory](https://github.com/expressjs/express/security/advisories/GHSA-qw6h-vgh9-j6wx), [CVE-2024-43796](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-43796)).
    *   The dependency 
```plaintext
serve-static
```
 has been updated to address a [vulnerability](https://github.com/advisories/GHSA-cm22-4g7w-348p).
    *   The dependency 
```plaintext
send
```
 has been updated to address a [vulnerability](https://github.com/advisories/GHSA-m6fv-jmcg-4jfg).
    *   The dependency 
```plaintext
path-to-regexp
```
 has been updated to address a [vulnerability](https://github.com/pillarjs/path-to-regexp/security/advisories/GHSA-9wv6-86v2-598j).
    *   The dependency 
```plaintext
body-parser
```
 has been updated to addres a [vulnerability](https://github.com/advisories/GHSA-qwcr-r2fm-qrc7), This may affect your application if you had url enconding activated.

*   4.19.0, 4.19.1 
    *   Fixed open redirect vulnerability in 
```plaintext
res.location
```
 and 
```plaintext
res.redirect
```
 ([advisory](https://github.com/expressjs/express/security/advisories/GHSA-rv95-896h-c2vc), [CVE-2024-29041](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-29041)).

*   4.17.3 
    *   The dependency 
```plaintext
qs
```
 has been updated to address a [vulnerability](https://github.com/advisories/GHSA-hrpp-h998-j3pp). This may affect your application if the following APIs are used: 
```plaintext
req.query
```
, 
```plaintext
req.body
```
, 
```plaintext
req.param
```
.

*   4.16.0 
    *   The dependency 
```plaintext
forwarded
```
 has been updated to address a [vulnerability](https://npmjs.com/advisories/527). This may affect your application if the following APIs are used: 
```plaintext
req.host
```
, 
```plaintext
req.hostname
```
, 
```plaintext
req.ip
```
, 
```plaintext
req.ips
```
, 
```plaintext
req.protocol
```
.
    *   The dependency 
```plaintext
mime
```
 has been updated to address a [vulnerability](https://npmjs.com/advisories/535), but this issue does not impact Express.
    *   The dependency 
```plaintext
send
```
 has been updated to provide a protection against a [Node.js 8.5.0 vulnerability](https://nodejs.org/en/blog/vulnerability/september-2017-path-validation/). This only impacts running Express on the specific Node.js version 8.5.0.

*   4.15.5 
    *   The dependency 
```plaintext
debug
```
 has been updated to address a [vulnerability](https://snyk.io/vuln/npm:debug:20170905), but this issue does not impact Express.
    *   The dependency 
```plaintext
fresh
```
 has been updated to address a [vulnerability](https://npmjs.com/advisories/526). This will affect your application if the following APIs are used: 
```plaintext
express.static
```
, 
```plaintext
req.fresh
```
, 
```plaintext
res.json
```
, 
```plaintext
res.jsonp
```
, 
```plaintext
res.send
```
, 
```plaintext
res.sendfile
```

```plaintext
res.sendFile
```
, 
```plaintext
res.sendStatus
```
.

*   4.15.3 
    *   The dependency 
```plaintext
ms
```
 has been updated to address a [vulnerability](https://snyk.io/vuln/npm:ms:20170412). This may affect your application if untrusted string input is passed to the 
```plaintext
maxAge
```
 option in the following APIs: 
```plaintext
express.static
```
, 
```plaintext
res.sendfile
```
, and 
```plaintext
res.sendFile
```
.

*   4.15.2 
    *   The dependency 
```plaintext
qs
```
 has been updated to address a [vulnerability](https://snyk.io/vuln/npm:qs:20170213), but this issue does not impact Express. Updating to 4.15.2 is a good practice, but not required to address the vulnerability.

*   4.11.1 
    *   Fixed root path disclosure vulnerability in 
```plaintext
express.static
```
, 
```plaintext
res.sendfile
```
, and 
```plaintext
res.sendFile
```

*   4.10.7 
    *   Fixed open redirect vulnerability in 
```plaintext
express.static
```
 ([advisory](https://npmjs.com/advisories/35), [CVE-2015-1164](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-1164)).

*   4.8.8 
    *   Fixed directory traversal vulnerabilities in 
```plaintext
express.static
```
 ([advisory](http://npmjs.com/advisories/32) , [CVE-2014-6394](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6394)).

*   4.8.4 
    *   Node.js 0.10 can leak 
```plaintext
fd
```
s in certain situations that affect 
```plaintext
express.static
```
 and 
```plaintext
res.sendfile
```
. Malicious requests could cause 
```plaintext
fd
```
s to leak and eventually lead to 
```plaintext
EMFILE
```
 errors and server unresponsiveness.

*   4.8.0 
    *   Sparse arrays that have extremely high indexes in the query string could cause the process to run out of memory and crash the server.
    *   Extremely nested query string objects could cause the process to block and make the server unresponsive temporarily.

3.x
---

**Express 3.x IS END-OF-LIFE AND NO LONGER MAINTAINED**

Known and unknown security and performance issues in 3.x have not been addressed since the last update (1 August, 2015). It is highly recommended to use the latest version of Express.

If you are unable to upgrade past 3.x, please consider [Commercial Support Options](https://expressjs.com/en/support#commercial-support-options).

*   3.19.1 
    *   Fixed root path disclosure vulnerability in 
```plaintext
express.static
```
, 
```plaintext
res.sendfile
```
, and 
```plaintext
res.sendFile
```

*   3.19.0 
    *   Fixed open redirect vulnerability in 
```plaintext
express.static
```
 ([advisory](https://npmjs.com/advisories/35), [CVE-2015-1164](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-1164)).

*   3.16.10 
    *   Fixed directory traversal vulnerabilities in 
```plaintext
express.static
```
.

*   3.16.6 
    *   Node.js 0.10 can leak 
```plaintext
fd
```
s in certain situations that affect 
```plaintext
express.static
```
 and 
```plaintext
res.sendfile
```
. Malicious requests could cause 
```plaintext
fd
```
s to leak and eventually lead to 
```plaintext
EMFILE
```
 errors and server unresponsiveness.

*   3.16.0 
    *   Sparse arrays that have extremely high indexes in query string could cause the process to run out of memory and crash the server.
    *   Extremely nested query string objects could cause the process to block and make the server unresponsive temporarily.

*   3.3.0 
    *   The 404 response of an unsupported method override attempt was susceptible to cross-site scripting attacks.

[Previous: Developing template engines for Express](https://expressjs.com/en/advanced/developing-template-engines.html)[Next: Security Best Practices for Express in Production](https://expressjs.com/en/advanced/best-practice-security.html)[Edit this page](https://github.com/expressjs/expressjs.com/edit/gh-pages/en/advanced/security-updates.md)

[](https://expressjs.com/en/advanced/security-updates.html#)

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
