# Source: https://parceljs.org/

Title: Parcel – The zero configuration build tool for the web.

URL Source: https://parceljs.org/

Published Time: Thu, 12 Mar 2026 16:06:42 GMT

Markdown Content:
Parcel starts with a great development experience, from starting a new project, to iterating and debugging, and shipping to production. No more fiddling with configuration, or spending hours to keep up with best practices – it just works!

#### Zero config

Start with an HTML file. Add a `<script>` tag. Maybe some CSS. How about TypeScript? SASS? Images? No problem. Parcel works out of the box just as you'd expect.

Parcel supports many languages and file types out of the box, from web technologies like HTML, CSS, and JavaScript, to assets like images, fonts, videos, and more. And when you use a file type that isn't included by default, Parcel will **automatically install** all of the necessary plugins and dev dependencies for you!

[Get started →](https://parceljs.org/getting-started/webapp/)

index.html

```
​<html>
  <head>
    <title>My First Parcel App</title>
    <link rel="stylesheet" href="styles.css">
  </head>
  <body>
    <h1>Hello, World!</h1>
    <script type="module" src="app.tsx"></script>
  </body>
</html>
```

#### Dev server

Parcel includes a development server out of the box. Just run `parcel index.html` to get started.

http://localhost:1234

Hello world!

Need HTTPS? Run Parcel with the `--https` flag, and it will automatically generate a certificate for you! Or, if you like, you can provide your own.

Parcel also has a built-in API proxy, which can help simulate your production environment.

[Learn more →](https://parceljs.org/features/development/#dev-server)

#### Hot reloading

When you make a change, Parcel automatically updates your code in the browser – no page reload necessary!

http://localhost:1234

Hello world!

Greeting.tsx

```
import React from 'react';

export function Greeting() {
  return <h1>Hello Parc!</h1>;
}
```

Parcel also integrates with **React Fast Refresh** and the **Vue Hot Reloading API** to automatically preserve your application state between updates. This gives you instant feedback as you make changes, without taking you out of context.

[Learn more →](https://parceljs.org/features/development/#hot-reloading)

#### Diagnostics

If you make an error in your code or configuration, Parcel displays **beautiful diagnostics** in your terminal and in the browser.

Every error includes a syntax highlighted code frame pointing to the exact location where the error occurred, along with hints about how to fix the issue.

Many diagnostics even include a documentation link where you can learn more.

```
$ parcel index.html
Server running at http://localhost:1234
🚨 Build failed.

@parcel/core: Cannot resolve 'ract' from './index.js'
/dev/app/index.js:1:19
> 1 | import React from 'ract';
>   |                   ^^^^^^
  2 | 
  3 | function Test() {

@parcel/resolver-default: Cannot find module 'ract'
Did you mean 'react'?
```

Parcel builds your code in parallel using worker threads, utilizing all of the cores on your machine. Everything is cached, so you never build the same code twice. It's like using watch mode, but even when you restart Parcel!

#### Native performance

Parcel's JavaScript, CSS, HTML, and SVG compilers are written in **Rust** for maximum performance. These are **10-100x faster** than other JavaScript-based tools!

Parcel's JavaScript compiler is built on [SWC](https://swc.rs/), which handles transpiling JavaScript, JSX, and TypeScript. On top of SWC, Parcel implements dependency collection, bundling, scope hoisting, tree shaking, Node emulation, hot reloading, and more.

Parcel's CSS transformer and minifier is built in Rust on top of the browser-grade CSS parser used in Firefox. It's over **100x faster** than other JavaScript-based transformers and minifiers.

#### Multi-core

**Parcel is designed around a multi-core architecture that parallelizes work across all of your cores and takes full advantage of modern hardware.**

Transforming individual source files is parallelized, as well as packaging and optimizing output bundles. All of this is completely automatic and does not require any work by plugin authors or other tools that integrate with Parcel.

#### Reliable caching

**Everything Parcel does is cached** – transformation, dependency resolution, bundling, optimizing, and everything in between. This means the dev server restarts instantly, and the same code is never built twice.

Parcel automatically tracks all of the files, configuration, plugins, and dev dependencies that are involved in your build, and granularly invalidates the cache when something changes. It integrates with low-level operating system APIs to determine what files have changed in milliseconds, no matter the project size.

#### Lazy dev builds

**In development, Parcel can defer building files until they are requested in the browser.** This means you only need to wait for the page you're actually working on to build! If your project has many entries or code split points, this can massively reduce dev server startup time.

And when you do request a page, Parcel is smart enough to eagerly build all of the dependencies of that page at once, without waiting for them to be requested as well – no network waterfalls!

[Learn more →](https://parceljs.org/features/development/#lazy-mode)

Parcel optimizes your whole app for production automatically. This includes tree-shaking and minifying your JavaScript, CSS, and HTML, resizing and optimizing images, content hashing, automatic code splitting, and much more.

#### Tree shaking

**Parcel supports tree-shaking both ES modules and CommonJS out of the box!** It statically analyzes the imports and exports of each module, and removes everything that isn't used.

Tree shaking even works across dynamic `import()` boundaries, shared bundles, and even across languages! If you use **CSS modules**, unused classes will be removed automatically.

[Learn more →](https://parceljs.org/features/scope-hoisting/)

index.js

```
import {add} from './math';

console.log(add(2, 3));
```

math.js

```
export function add(a, b) {
  return a + b;
}
```

```
export function square(a) {
  return a * a;
}
```

#### Minification

Parcel includes minifiers for JavaScript, CSS, HTML, and SVG out of the box! Just run `parcel build index.html`, and your whole application will be built and optimized automatically.

[Learn more →](https://parceljs.org/features/production/#minification)

233.56 kB

#### Image optimization

**Parcel supports resizing, converting, and optimizing images!** Just pass query parameters for the format and size you need when referencing the image file in your HTML, CSS, JavaScript, etc. and Parcel will take care of the conversion and optimization process.

You can even request multiple sizes or formats of the same source image for different devices or browsers!

[Learn more →](https://parceljs.org/recipes/image/)

index.html

```
<picture>
  <source type="image/webp" srcset="image.jpg?as=webp&width=400, image.jpg?as=webp&width=800 2x">
  <source type="image/jpeg" srcset="image.jpg?width=400, image.jpg?width=800 2x">
  <img src="image.jpg?width=400" width="400">
</picture>
```

#### Compression

Compress your app before you deploy using Gzip and Brotli.

[Learn more →](https://parceljs.org/features/production/#compression)

#### Code splitting

When multiple parts of your application depend on the same common modules, they are **automatically deduplicated into a separate bundle.** This allows commonly used dependencies to be loaded in parallel with your application code and cached separately by the browser!

**Code splitting is also supported for CSS.** If you import CSS from your JavaScript, a sibling CSS bundle will be produced and loaded in parallel with the JS bundle.

[Learn more →](https://parceljs.org/features/code-splitting/)

#### Content hashing

Parcel automatically includes content hashes in the names of all output files. This enables **long-term browser caching**, because the output is guaranteed not to change unless the name does.

Parcel also resolves all referenced bundles relative to their parent using a manifest in each entry. This means that changes to referenced bundles don't invalidate the cache for their parents as well, and output files can be moved between locations without rebuilding.

[Learn more →](https://parceljs.org/features/production/#content-hashing)

Parcel automatically transforms your code for your target environments. From modern and legacy browser support, to zero config JSX and TypeScript compilation, Parcel makes it easy to build for any target – or many!

#### Transpilation

Parcel transpiles your JavaScript and CSS for your target browsers automatically! Just declare a `browserslist` in your `package.json`, and Parcel takes care of transpiling only what's needed.

In addition to standard JavaScript, Parcel automatically handles **JSX**, **TypeScript**, and **Flow**, along with Node.js features like **process.env** and **fs.readFileSync** – no configuration needed!

When it comes to CSS, Parcel supports transpiling modern syntax features like `lab()` colors, logical properties, and CSS nesting syntax, as well as automatically adding the necessary vendor prefixes for your browser targets.

And if you need more advanced control, or support for custom transforms, just add a `.babelrc` or `.postcssrc` and it'll be picked up automatically.

[Learn more →](https://parceljs.org/languages/javascript/#transpilation)

```
function DogName(props) {
  return (
    <span>
      {props.dog?.name ?? 'Buddy'}
    </span>
  );
}
```

```
function DogName(props) {
  var ref, ref1;
  return /*#__PURE__*/ React.createElement(
    "span",
    null,
    (ref1 = (ref = props.dog) === null || ref === void 0 ? void 0 : ref.name) !== null && ref1 !== void 0 ? ref1 : "Buddy"
  );
}
```

#### Differential bundling

When you use `<script type="module">`, Parcel automatically generates a `nomodule` fallback for old browsers as well, depending on your browser targets.

This results in **much smaller bundles** for a majority of users in modern browsers, while still supporting older browsers as well!

[Learn more →](https://parceljs.org/features/targets/#differential-bundling)

`​<script type="module" src="app.js"></script>`
```
​<script type="module" src="app.c9a6fe.js"></script>
<script nomodule="" src="app.f7d631.js"></script>
```

#### Workers

Parcel supports **web workers**, **service workers**, and **worklets** out of the box! Just use the standard browser APIs and Parcel will automatically follow the dependency.

It even generates **native ES module workers** when possible, depending on your browser targets!

[Learn more →](https://parceljs.org/languages/javascript/#workers)

App.js

```
let worker = new Worker(
  new URL('./worker.js', import.meta.url),
  {type: 'module'}
);

navigator.serviceWorker.register(
  new URL('./sw.js', import.meta.url),
  {type: 'module'}
);
```

#### Libraries

**Parcel can build libraries for multiple targets at once!** For example, your source code can be compiled to a modern ES module, a legacy CommonJS module, and a TypeScript definition file all automatically. Just add the relevant fields to your `package.json` and Parcel takes care of the rest.

You can even build a whole monorepo of packages in a single command! 🤯 `parcel build packages/*`

[Learn more →](https://parceljs.org/getting-started/library/)

package.json

```
{
  "name": "my-great-library",
  "version": "1.0.0",
  "source": "src/index.js",
  "module": "dist/module.js",
  "main": "dist/main.js",
  "types": "dist/types.d.ts"
}
```

Parcel requires zero configuration to get started. But as your application grows and your build requirements become more complex, it's possible to extend Parcel in just about every way.

#### Simple configuration?!

Configuring Parcel is like a breath of fresh air. `.parcelrc` is a simple JSON-based config format that uses globs to match your source files to build pipelines. You can extend the default config and add plugins to handle custom file types, or override and extend the defaults.

[Learn more →](https://parceljs.org/features/plugins/)

Extends

Start with the default config, or a community preset.

Transformers

Compile individual source files and extract dependencies.

Resolvers

Resolve a dependency to a file path or virtual module.

Namers

Determine the name of an output file.

Packagers

Combine multiple assets together into a single output file.

Optimizers

Minify, optimize, and transform output files.

Compressors

Compress and encode output files in multiple formats.

Reporters

Receive events on build progress and completion.

.parcelrc

{
`"extends": ["@parcel/config-default"],`

```
"transformers": {
    "*.svg": ["@parcel/transformer-svg-jsx"]
  },
```

`"resolvers": ["@parcel/resolver-glob", "..."],`
`"namers": ["@company/parcel-namer", "..."],`

```
"packagers": {
    "*.{jpg,png}": "parcel-packager-image-sprite"
  },
```

```
"optimizers": {
    "*.js": ["parcel-optimizer-license-headers"]
  },
```

```
"compressors": {
    "*.js": ["...", "@parcel/compressor-gzip"]
  },
```

`"reporters": ["...", "parcel-reporter-manifest"]`
}

#### Powerful plugins

Transformer.js

Resolver.js

Namer.js

Packager.js

Optimizer.js

Compressor.js

Reporter.js

```
import {Transformer} from '@parcel/plugin';

export default new Transformer({
  async transform({asset}) {
    let source = await asset.getCode();
    let sourceMap = await asset.getMap();

    let {code, map} = compile(source, sourceMap);
    asset.setCode(code);
    asset.setMap(map);

    return [asset];
  }
});
```

Parcel has a plugin for everything. In fact, Parcel core is **completely language agnostic**! From transforming files, to resolving dependencies, to bundling and optimizing – everything is customizable.

Each plugin type has a specific, well defined API designed for its purpose. All objects and methods are **fully documented, and include TypeScript definitions** for autocomplete and type safety.

As you're developing a plugin, it even hot reloads as you save without needing to re-run your build from scratch! This makes it super fast to debug and iterate. It even works with dependencies in `node_modules`!

[Learn more →](https://parceljs.org/plugin-system/authoring-plugins/)

#### Named pipelines

Want to transform the same types of files in multiple ways in a single build? Create a named pipeline, and use it as a URL scheme in your code.

For example, you could inline the compiled contents of a bundle as text, a data URL, an ArrayBuffer, or anything else! Or if you're building a documentation site, you could import both the generated API docs and source code for a file. The possibilities are endless.

[Learn more →](https://parceljs.org/features/plugins/#named-pipelines)

.parcelrc

```
{
  "extends": "@parcel/config-default",
  "transformers": {
    "buffer:*": ["...", "parcel-transformer-buffer"]
  }
}
```

App.js

`import buffer from 'buffer:./logo.png';`

#### Designed for performance

Parcel's plugin system has been designed from the ground up with performance in mind. Plugins are automatically parallelized across multiple threads, and integrated with Parcel's cache. Any dependencies or configs your plugin uses are automatically tracked and invalidate the build.

[Learn more →](https://parceljs.org/plugin-system/authoring-plugins/)
#### API

Integrate Parcel into any existing build system using Parcel's API, which allows you to perform builds programmatically.

[Learn more →](https://parceljs.org/features/parcel-api/)
#### Diagnostics

All Parcel plugins use a unified diagnostic format that supports highlighted code frames, rich Markdown formatting, hints, and documentation links.

[Learn more →](https://parceljs.org/plugin-system/logging/)

Parcel is an open source project, powered by code and financial contributions from companies and individuals around the world.

#### 🥇 Gold sponsors

Gold sponsors donate $1,000 or more per month to Parcel.

#### 🥈 Silver sponsors

Silver sponsors donate $500 or more per month to Parcel.

#### 🥉 Bronze sponsors

Bronze sponsors donate $100 or more per month to Parcel.

#### 💵 Backers

Backers have donated any amount of money to Parcel. [Become a backer →](https://opencollective.com/parcel#support)

#### 😍 Contributors

Contributors help fix bugs and implement new features in Parcel. [Become a contributor →](https://github.com/parcel-bundler/parcel)
