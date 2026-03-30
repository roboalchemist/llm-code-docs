# Source: https://docs.skypack.dev/skypack-cdn/getting-started.md

# Getting Started

If you haven’t familiarized yourself with the main concepts of the Skypack CDN, please visit the [Introduction](https://docs.skypack.dev/master) section.

If you’ve decided to use Skypack to boost your app’s speed, there are 2 main ways to start using it: either manually, using **code**. Or automatically, using **plugins**.

## Code

Because Skypack works with [ES Modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules), you can start using Skypack today with a simple change to your codebase:

```diff
-import React from "react";
+import React from "https://cdn.skypack.dev/react";
```

Basically, for any package you used to install locally via `npm`, you now load from Skypack. Simply prepend `https://cdn.skypack.dev/` before any npm-loaded package to start loading that package from anywhere. You can even try this today in [CodePen](https://codepen.io), or your favorite online editor.

### Demo

{% embed url="<https://codepen.io/dangodev/full/eYJKoXj>" %}

### Learn more

Use Skypack in the following languages:

* [JavaScript](https://docs.skypack.dev/skypack-cdn/code/javascript)
* [Node.js](https://docs.skypack.dev/skypack-cdn/code/node)
* [Deno](https://docs.skypack.dev/skypack-cdn/code/deno)

## Plugins (Coming soon)

Skypack’s plugins are currently under development, but when finished will allow easy drop-in support for:

* Next.js
* Create React App
* Gatsby&#x20;
* webpack
* Parcel
* Rollup
* Nuxt

To be notified of when these release, [please sign up for our mailing list](http://eepurl.com/g-czY9).
