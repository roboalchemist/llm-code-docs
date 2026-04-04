# Source: https://gojs.net/download.html

Title: Download

URL Source: https://gojs.net/download.html

Markdown Content:
Download GoJS
-------------

If you wish to use the **GoJS** library for your private evaluation, you may do so only under the terms of the [Evaluation License Agreement](https://gojs.net/evaluationlicense.html). We encourage you to [register](https://nwoods.com/register.html) if you discover you need technical support during your evaluation.

You can download the whole web site for this version of **GoJS** by saving and unzipping:

*   [site.zip](https://gojs.net/site.zip)

We also maintain a [GitHub Repository](https://github.com/NorthwoodsSoftware/GoJS) of all libraries, documentation, samples, and extensions. This allows you to [search through documentation and code online](https://github.com/NorthwoodsSoftware/GoJS/search?q=setDataProperty&type=Code).

The contents of both the ZIP file and the GitHub repository are exactly what you find at the [GoJS web site](https://gojs.net/index.html). Having everything downloaded to your development machine allows you to easily search the JavaScript code and to modify the samples for experimentation.

You can also download **GoJS** via [Node package manager (npm)](https://www.npmjs.com/package/gojs): `$ npm install gojs`. The contents of that package are only the library files. If you want to download the extensions, samples, and documentation, they are in the `create-gojs-kit` package. Download its contents by executing: `$ npm create gojs-kit@latest`

Or you can link to a CDN (content delivery network):

*   [JSDELIVR](https://www.jsdelivr.com/package/npm/gojs), such as: 
    *    Latest: `"https://cdn.jsdelivr.net/npm/gojs/release/go.js"`
    *    Most recent 3.0: `"https://cdn.jsdelivr.net/npm/gojs@3.0/release/go.js"`

The **GoJS** library comes in both "debug" and "release" variations in the `release` directory:

*   [go.js](https://gojs.net/release/go.js)
*   [go-debug.js](https://gojs.net/release/go-debug.js), the same functionality as `go.js`, but with more error checking, for use during development.
*   [go-module.js](https://gojs.net/release/go-module.js) and [go-debug-module.js](https://gojs.net/release/go-debug-module.js), the same functionality but as ECMAScript modules.
*   [go.mjs](https://gojs.net/release/go.mjs) and [go-debug.mjs](https://gojs.net/release/go-debug.mjs) are copies of the `*-module.js` ECMAScript modules for Node.js use on a server.

We recommend that you use `go-debug.js` while doing your initial development -- it is more likely to signal errors or provide meaningful error messages than when using `go.js`. Always remember to look at the console log to see if there are any error or warning messages.

After purchasing a license, you may deploy by acquiring a license key for your web site's domain. See [Deployment](https://gojs.net/intro/deployment.html) for more discussion.

### New Versions

You can learn about new releases in several manners:

*   "watch" the [GoJS GitHub repository](https://github.com/NorthwoodsSoftware/GoJS) for new releases
*   read the [GoJS npm package](https://www.npmjs.com/package/gojs) page, or write a "hook" for it
*   follow us on Twitter: [@NorthwoodsGo](https://twitter.com/northwoodsgo)
*   read the GoJS Change Log page ([latest](https://gojs.net/latest/changelog.html))
*   read or follow the [Northwoods GoJS Forum](https://forum.nwoods.com/c/gojs)

When updating or upgrading to a newer version, please read the [Change Log](https://gojs.net/changelog.html). In addition to getting new debug and release libraries, don't forget to use the latest TypeScript definition file, [go.d.ts](https://gojs.net/release/go.d.ts), that is also in the release directory.

More information is at [GoJS home](https://gojs.net/index.html).
