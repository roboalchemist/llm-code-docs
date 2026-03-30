# Source: https://esbuild.github.io/

Title: esbuild - An extremely fast bundler for the web

URL Source: https://esbuild.github.io/

Published Time: Thu, 12 Mar 2026 19:14:25 GMT

Markdown Content:
esbuild - An extremely fast bundler for the web
===============

[](javascript:void 0)

[esbuild](https://esbuild.github.io/)
*   [Try in the browser](https://esbuild.github.io/try/)
*   [Getting Started](https://esbuild.github.io/getting-started/)
    *   [Install esbuild](https://esbuild.github.io/getting-started/#install-esbuild)
    *   [Your first bundle](https://esbuild.github.io/getting-started/#your-first-bundle)
    *   [Build scripts](https://esbuild.github.io/getting-started/#build-scripts)
    *   [Bundling for the browser](https://esbuild.github.io/getting-started/#bundling-for-the-browser)
    *   [Bundling for node](https://esbuild.github.io/getting-started/#bundling-for-node)
    *   [Simultaneous platforms](https://esbuild.github.io/getting-started/#simultaneous-platforms)
    *   [Using Yarn Plug'n'Play](https://esbuild.github.io/getting-started/#yarn-pnp)
    *   [Additional npm flags](https://esbuild.github.io/getting-started/#additional-npm-flags)
    *   [Other ways to install](https://esbuild.github.io/getting-started/#other-ways-to-install)

*   [API](https://esbuild.github.io/api/)
    *   [Overview](https://esbuild.github.io/api/#overview)
    *   [General options](https://esbuild.github.io/api/#general-options)
    *   [Input](https://esbuild.github.io/api/#input)
    *   [Output contents](https://esbuild.github.io/api/#output-contents)
    *   [Output location](https://esbuild.github.io/api/#output-location)
    *   [Path resolution](https://esbuild.github.io/api/#path-resolution)
    *   [Transformation](https://esbuild.github.io/api/#transformation)
    *   [Optimization](https://esbuild.github.io/api/#optimization)
    *   [Source maps](https://esbuild.github.io/api/#source-maps)
    *   [Build metadata](https://esbuild.github.io/api/#build-metadata)
    *   [Logging](https://esbuild.github.io/api/#logging)

*   [Content Types](https://esbuild.github.io/content-types/)
    *   [JavaScript](https://esbuild.github.io/content-types/#javascript)
    *   [TypeScript](https://esbuild.github.io/content-types/#typescript)
    *   [JSX](https://esbuild.github.io/content-types/#jsx)
    *   [JSON](https://esbuild.github.io/content-types/#json)
    *   [CSS](https://esbuild.github.io/content-types/#css)
    *   [Text](https://esbuild.github.io/content-types/#text)
    *   [Binary](https://esbuild.github.io/content-types/#binary)
    *   [Base64](https://esbuild.github.io/content-types/#base64)
    *   [Data URL](https://esbuild.github.io/content-types/#data-url)
    *   [External file](https://esbuild.github.io/content-types/#external-file)
    *   [Empty file](https://esbuild.github.io/content-types/#empty-file)

*   [Plugins](https://esbuild.github.io/plugins/)
    *   [Finding plugins](https://esbuild.github.io/plugins/#finding-plugins)
    *   [Using plugins](https://esbuild.github.io/plugins/#using-plugins)
    *   [Concepts](https://esbuild.github.io/plugins/#concepts)
    *   [On-resolve callbacks](https://esbuild.github.io/plugins/#on-resolve)
    *   [On-load callbacks](https://esbuild.github.io/plugins/#on-load)
    *   [On-start callbacks](https://esbuild.github.io/plugins/#on-start)
    *   [On-end callbacks](https://esbuild.github.io/plugins/#on-end)
    *   [On-dispose callbacks](https://esbuild.github.io/plugins/#on-dispose)
    *   [Accessing build options](https://esbuild.github.io/plugins/#build-options)
    *   [Resolving paths](https://esbuild.github.io/plugins/#resolve)
    *   [Example plugins](https://esbuild.github.io/plugins/#example-plugins)
    *   [Plugin API limitations](https://esbuild.github.io/plugins/#plugin-api-limitations)

*   [FAQ](https://esbuild.github.io/faq/)
    *   [Why is esbuild fast?](https://esbuild.github.io/faq/#why-is-esbuild-fast)
    *   [Benchmark details](https://esbuild.github.io/faq/#benchmark-details)
    *   [Upcoming roadmap](https://esbuild.github.io/faq/#upcoming-roadmap)
    *   [Production readiness](https://esbuild.github.io/faq/#production-readiness)
    *   [Anti-virus software](https://esbuild.github.io/faq/#anti-virus-software)
    *   [Outdated version of Go](https://esbuild.github.io/faq/#old-go-version)
    *   [Minified newlines](https://esbuild.github.io/faq/#minified-newlines)
    *   [Avoiding name collisions](https://esbuild.github.io/faq/#top-level-name-collisions)
    *   [Strict mode](https://esbuild.github.io/faq/#strict-mode)
    *   [Top-level `var`](https://esbuild.github.io/faq/#top-level-var)

*   [Bundle Size Analyzer](https://esbuild.github.io/analyze/)

[](https://github.com/evanw/esbuild)[](javascript:void 0)

esbuild
=======

> An extremely fast bundler for the web

[esbuild](https://esbuild.github.io/)

0.39s

[parcel 2](https://parceljs.org/)

14.91s

[rollup 4](https://rollupjs.org/) + [terser](https://terser.org/)

34.10s

[webpack 5](https://webpack.js.org/)

41.21s

0s

10s

20s

30s

40s

Above: the time to do a production bundle of 10 copies of the [three.js](https://github.com/mrdoob/three.js) library from scratch using default settings, including minification and source maps. More info [here](https://esbuild.github.io/faq/#benchmark-details).

Our current build tools for the web are 10-100x slower than they could be. The main goal of the esbuild bundler project is to bring about a new era of build tool performance, and create an easy-to-use modern bundler along the way.

Major features:

*   Extreme speed without needing a cache
*   [JavaScript](https://esbuild.github.io/content-types/#javascript), [CSS](https://esbuild.github.io/content-types/#css), [TypeScript](https://esbuild.github.io/content-types/#typescript), and [JSX](https://esbuild.github.io/content-types/#jsx) built-in
*   A straightforward [API](https://esbuild.github.io/api/) for CLI, JS, and Go
*   Bundles ESM and CommonJS modules
*   Bundles CSS including [CSS modules](https://github.com/css-modules/css-modules)
*   Tree shaking, [minification](https://esbuild.github.io/api/#minify), and [source maps](https://esbuild.github.io/api/#sourcemap)
*   [Local server](https://esbuild.github.io/api/#serve), [watch mode](https://esbuild.github.io/api/#watch), and [plugins](https://esbuild.github.io/plugins/)

Check out the [getting started](https://esbuild.github.io/getting-started/) instructions if you want to give esbuild a try.
