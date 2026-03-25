# Source: https://parceljs.org/languages/javascript/

Title: JavaScript

URL Source: https://parceljs.org/languages/javascript/

Markdown Content:
Parcel includes first-class support for JavaScript, including ES modules and CommonJS, many types of dependencies, automatic transpilation for browser targets, JSX and TypeScript support, and much more.

Modules
-------

[#](https://parceljs.org/languages/javascript/#modules)
Modules allow you to break up your code into different files, and share functionality between them by importing and exporting values. This can help you structure your code into independent parts, with well-defined interfaces for communicating between them.

Parcel includes support for both ES modules and CommonJS syntax. Module specifiers are resolved as described in [Dependency resolution](https://parceljs.org/features/dependency-resolution/).

### ES modules

[#](https://parceljs.org/languages/javascript/#es-modules)
ES module syntax is the standard way to import and export values between files in JavaScript. It should be preferred over CommonJS for new code. The [`import`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import) statement can be used to reference a value exposed by the [`export`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/export) statement in another file.

This example imports a `multiply` function from `math.js`, and uses it to implement a `square` function.

_square.js:_

`import {multiply} from './math.js';export function square(x) {  return multiply(x, x);}`

_math.js:_

`export function multiply(a, b) {  return a * b;}`

To learn more about ES modules, see the documentation on [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules).

### CommonJS

[#](https://parceljs.org/languages/javascript/#commonjs)
CommonJS is a legacy module system supported in Node, and widely used by libraries on npm. If you’re writing new code, you should generally prefer ES module syntax as described above. CommonJS provides a `require` function, which can be used to access the `exports` object exposed by another file.

This example uses `require` to load the `math.js` module, and uses the `multiply` function on its exports object to implement a `square` function.

_square.js:_

`let math = require('./math');exports.square = function(x) {  return math.multiply(x, x);};`

_math.js:_

`exports.multiply = function(a, b) {  return a * b;};`

In addition to `require` and `exports`, Parcel also supports `module.exports`, as well as the `__dirname` and `__filename` module globals, and `process.env` for access to environment variables. See the [Node emulation](https://parceljs.org/features/node-emulation/) docs for more details.

To learn more about CommonJS, see the [Node.js docs](https://nodejs.org/dist/latest-v16.x/docs/api/modules.html).

### Dynamic import

[#](https://parceljs.org/languages/javascript/#dynamic-import)
Both the ES module `import` statement and CommonJS `require` function load dependencies _synchronously_: that is, the module can be referenced immediately without waiting for a network request. Typically, modules that are imported synchronously are bundled together into the same file as their parent, or referenced in another bundle that is already loaded.

The dynamic [`import()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import#dynamic_imports) function can be used to load dependencies _asynchronously_. This allows loading code lazily, on demand, and is a good technique for reducing the file size of the initial page load of your app. `import()` returns a [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise), which notifies you when the dependency has been loaded.

`import('./pages/about').then(function(page) {  page.render()});`
See the [code splitting](https://parceljs.org/features/code-splitting/) docs for more details on how to use dynamic imports.

### Classic scripts

[#](https://parceljs.org/languages/javascript/#classic-scripts)
One of the benefits of modules (both ES modules and CommonJS) is that they isolate functionality. This means that variables declared in the top-level scope cannot be accessed outside the module unless they are exported. This is generally a great characteristic, but modules in JavaScript are relatively recent and there are many legacy libraries and scripts that do not expect to be isolated.

A **classic script**, is a JavaScript file that is loaded via the traditional `<script>` tag in HTML (without `type="module"`) or other means such as Workers. Classic scripts treat variables in the top-level scope as globals which can be accessed even between different scripts.

For example, when loading a library like jQuery, a `$` variable is available globally to other scripts on the page. If jQuery were loaded as a module, `$` would not be accessible unless it were assigned as a property to the `window` object manually.

`<script src="jquery.js"></script><script>// The $ variable is now available globally.$('.banner').show();</script>`
In addition, classic scripts do not support synchronous imports or exports via either ES modules or CommonJS, and [Node emulation](https://parceljs.org/features/node-emulation/) is disabled. However, dynamic `import()`_is_ supported to load a module from within a classic script.

Parcel matches browser behavior for classic scripts and modules. If you wish to use imports or exports within your code, you’ll need to use `<script type="module">` to reference your JavaScript from an HTML file. For workers, use the `{type: 'module'}` option (see below). If this is missing, you'll see a diagnostic like the one below.

![Image 1: Screenshot of an error message showing "Browser scripts cannot have imports or exports. Add the type='module' attribute to the script tag."](https://parceljs.org/script-module-error.8ad5e048.png)

[#](https://parceljs.org/languages/javascript/#import.meta)
The [`import.meta`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import.meta) object includes information about the module it is referenced in. Parcel currently supports a single property, `import.meta.url`, which includes a `file://` url for the module on the file system. This URL is relative to your project root (e.g. the directory where Git is initialized) to avoid exposing any build system details.

`console.log(import.meta);// => {url: 'file:///src/App.js'}console.log(import.meta.url);// => 'file:///src/App.js'`
URL dependencies
----------------

[#](https://parceljs.org/languages/javascript/#url-dependencies)
You can reference non-JavaScript assets such as images or videos from a JavaScript file using the [`URL`](https://developer.mozilla.org/en-US/docs/Web/API/URL/URL) constructor. These are resolved relative to the module by using `import.meta.url` as the base URL parameter. The first argument must be a string literal to be recognized (not a variable or expression).

This example references an image named `hero.jpg` in the same directory as the JavaScript file, and creates an `<img>` element from it.

`let img = document.createElement('img');img.src = new URL('hero.jpg', import.meta.url);document.body.appendChild(img);`
Parcel will process any files referenced by a URL dependency as it does any other dependency. For example, images will be processed by the image transformer, and you can use [query parameters](https://parceljs.org/features/dependency-resolution/#query-parameters) to specify options to resize and convert them. If no transformers are configured for a particular file type, then the file will be copied into the dist directory unmodified. The resulting file names will also include a [content hash](https://parceljs.org/features/production/#content-hashing) for long term cacheability in the browser.

Workers
-------

[#](https://parceljs.org/languages/javascript/#workers)
Parcel has built in support for web workers, service workers, and worklets, which allow moving work to a different thread.

### Web workers

[#](https://parceljs.org/languages/javascript/#web-workers)
Web workers are the most general type of worker. They allow you to run arbitrary CPU-heavy work in a background thread to avoid blocking the user interface. Workers are created using the [`Worker`](https://developer.mozilla.org/en-US/docs/Web/API/Worker/Worker) constructor, and referencing another JavaScript file using the `URL` constructor as described above.

To use ES module or CommonJS syntax in a worker, use the `type: 'module'` option as described in [Classic scripts](https://parceljs.org/languages/javascript/#classic-scripts) above. Parcel will compile your worker to a non-module worker if necessary, depending on your [targets](https://parceljs.org/features/targets/) and current browser support.

`new Worker(  new URL('worker.js', import.meta.url),  {type: 'module'});`
Parcel also supports the [`SharedWorker`](https://developer.mozilla.org/en-US/docs/Web/API/SharedWorker/SharedWorker) constructor, which creates a worker that can be accessed in different browser windows or iframes. It supports the same options as described above for `Worker`.

To learn more about web workers, see the docs on [MDN](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Using_web_workers).

### Service workers

[#](https://parceljs.org/languages/javascript/#service-workers)
Service workers run in the background and provide features like offline caching, background sync, and push notifications. They are created using the [`navigator.serviceWorker.register`](https://developer.mozilla.org/en-US/docs/Web/API/ServiceWorkerContainer/register) function, and using the `URL` constructor to reference another JavaScript file.

To use ES module or CommonJS syntax in a service worker, use the `type: 'module'` option as described in [Classic scripts](https://parceljs.org/languages/javascript/#classic-scripts) above. Parcel will compile your service worker to a non-module worker if necessary, depending on your [targets](https://parceljs.org/features/targets/) and current browser support.

`navigator.serviceWorker.register(  new URL('service-worker.js', import.meta.url),  {type: 'module'});`
**Note**: dynamic `import()` is not supported in service workers.

Service workers are commonly used for pre-caching static assets like JavaScript, CSS, and images. `@parcel/service-worker` can be used to access a list of bundle URLs from within your service worker. It also provides a `version` hash, which changes every time the manifest does. You can use this to generate a cache name.

First, install it as a dependency into your project.

`yarn add @parcel/service-worker`
This example shows how you could pre-cache all bundles when the service worker is installed, and clean up old versions when it is activated.

_service-worker.js:_

`import {manifest, version} from '@parcel/service-worker';async function install() {  const cache = await caches.open(version);  await cache.addAll(manifest);}addEventListener('install', e => e.waitUntil(install()));async function activate() {  const keys = await caches.keys();  await Promise.all(    keys.map(key => key !== version && caches.delete(key))  );}addEventListener('activate', e => e.waitUntil(activate()));`

To learn more about service workers, see the docs on [MDN](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API/Using_Service_Workers), and the [Offline Cookbook](https://web.dev/offline-cookbook/) on web.dev.

### Classic script workers

[#](https://parceljs.org/languages/javascript/#classic-script-workers)
The `type: 'module'` option may also be omitted to treat workers and service workers as classic scripts instead of modules. The [`importScripts`](https://developer.mozilla.org/en-US/docs/Web/API/WorkerGlobalScope/importScripts) function can be used to load additional code in classic script workers, however, the code will loaded at runtime and will not be processed by Parcel. This is because `importScripts` resolves URLs relative to the page, not the worker script. Therefore, the parameter to `importScripts` must be a fully-qualified absolute URL, not a relative path.

The following examples show patterns that are supported and unsupported.

`// ✅ absolute URLimportScripts('http://some-cdn.com/worker.js');// ✅ computed URLimportScripts(location.origin + '/worker.js');// 🚫 relative pathimportScripts('worker.js');// 🚫 absolute pathimportScripts('/worker.js');`
### Worklets

[#](https://parceljs.org/languages/javascript/#worklets)
Parcel also supports worklets, including [CSS Houdini paint worklets](https://developers.google.com/web/updates/2018/01/paintapi) as well as [web audio worklets](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API/Using_AudioWorklet). These let you hook into low level aspects of the rendering process or audio processing pipeline in the browser.

Paint worklets are detected automatically using the following syntax:

`CSS.paintWorklet.addModule(  new URL('worklet.js', import.meta.url));`
Web audio worklets are not statically analyzable, so for these you can use the `worklet:` scheme to import a URL to the worklet file compiled for the correct environment.

`import workletUrl from 'worklet:./worklet.js';context.audioWorklet.addModule(workletUrl);`
Worklets are always modules – there are no classic script worklets. This means the `type: 'module'` option is not required for worklets, and `importScripts` is not supported.

In addition, dynamic `import()` is not supported in worklets.

Transpilation
-------------

[#](https://parceljs.org/languages/javascript/#transpilation)
Parcel includes support for transpiling JSX, TypeScript, and Flow out of the box, as well as transpiling modern JavaScript syntax to support older browsers. In addition, Babel is supported to enable experimental or custom JavaScript transformations.

### JSX

[#](https://parceljs.org/languages/javascript/#jsx)
Parcel supports JSX out of the box. JSX is automatically enabled in a `.jsx` or `.tsx` file, or when one of the following libraries is defined as a dependency in your package.json:

*   `react`
*   `preact`
*   `nervjs`
*   `hyperapp`

The correct JSX pragma is also automatically inferred based on the library you use. Parcel also automatically detects the version of React or Preact that is installed, and enables the [modern JSX transform](https://reactjs.org/blog/2020/09/22/introducing-the-new-jsx-transform.html) if supported.

JSX compilation can also be configured using a `tsconfig.json` or `jsconfig.json` file. This allows overriding the runtime, pragma, and other options. See the [TSConfig reference](https://www.typescriptlang.org/tsconfig) for more information.

_tsconfig.json:_

`{  "compilerOptions": {    "jsx": "react-jsx",    "jsxImportSource": "preact"  }}`

### Flow

[#](https://parceljs.org/languages/javascript/#flow)
[Flow](https://flow.org/) support is automatically enabled when `flow-bin` is listed as a dependency in your project's root package.json. You must also use a `@flow` directive in the files you wish to be compiled.

Parcel currently uses Babel to strip flow types. If you have a custom Babel config, you will need to add the Flow plugin yourself. See [Babel](https://parceljs.org/languages/javascript/#babel) for more details.

### TypeScript

[#](https://parceljs.org/languages/javascript/#typescript)
See [TypeScript](https://parceljs.org/languages/typescript/).

### Browser compatibility

[#](https://parceljs.org/languages/javascript/#browser-compatibility)
By default Parcel does not perform any transpilation of JavaScript syntax for older browsers. This means that if you write your code using modern language features, that’s what Parcel will output. You can declare your app’s supported browsers using the `browserslist` field in your package.json. When this field is declared, Parcel will transpile your code accordingly to ensure compatibility with your supported browsers.

_package.json:_

`{  "browserslist": "> 0.5%, last 2 versions, not dead"}`

See the [Targets](https://parceljs.org/features/targets/) docs for more details on how to configure this, as well as Parcel's support for automatic [differential bundling](https://parceljs.org/features/targets/#differential-bundling).

By default, Parcel supports all standard JavaScript features, as well as proposals that have shipped in one or more browsers. You can also enable support for future proposals using a `tsconfig.json` or `jsconfig.json` file. Currently, the only supported proposal is [decorators](https://github.com/tc39/proposal-decorators), which you may be using through TypeScript.

_tsconfig.json:_

`{  "compilerOptions": {    "experimentalDecorators": true  }}`

More experimental features can be enabled using [Babel](https://parceljs.org/languages/javascript/#babel).

### Babel

[#](https://parceljs.org/languages/javascript/#babel)
[Babel](https://babeljs.io/) is a popular transpiler for JavaScript, with a large plugin ecosystem. Using Babel with Parcel works the same way as using it standalone or with other build tools. Create a Babel config file such as `.babelrc` and Parcel will pick it up automatically.

Parcel supports both project wide config files such as `babel.config.json`, as well as file relative configs such as `.babelrc`. See the [Babel docs](https://babeljs.io/docs/en/config-files) for details on configuration for more details.

**Note**: JavaScript Babel configs (e.g. `babel.config.js`) should be avoided. These cause Parcel’s caching to be less effective, which means all of your JS files will be recompiled each time you restart Parcel. To avoid this, use a JSON-based config format instead (e.g. `babel.config.json`).

#### Default presets

[#](https://parceljs.org/languages/javascript/#default-presets)
Parcel includes transpilation for browser targets (equivalent to `@babel/preset-env`), JSX (equivalent to `@babel/preset-react`), TypeScript (equivalent to `@babel/preset-typescript`), and Flow (equivalent to `@babel/preset-flow`) by default. If these are the only transforms you need in your project, then you may not need Babel at all.

If you have an existing project with a Babel config containing only the above presets, you may be able to remove it. This can significantly improve build performance since Parcel’s builtin transpiler is much faster than Babel.

#### Custom plugins

[#](https://parceljs.org/languages/javascript/#custom-plugins)
If you have custom Babel presets or plugins beyond the ones listed above, you can configure Babel to only include these custom plugins and omit the standard presets. This will improve build performance by allowing Babel to do less work and letting Parcel handle the default transformations.

_babel.config.json:_

`{  "plugins": ["@emotion/babel-plugin"]}`

Since Parcel uses Babel to transpile Flow, you'll need to keep `@babel/preset-flow` in your Babel config along with any custom plugins. Otherwise, your Babel config overrides Parcel's defaults. Other Babel presets listed above can be removed.

`@babel/preset-env` and `@babel/plugin-transform-runtime` are not aware of Parcel's [Targets](https://parceljs.org/features/targets/), which means [differential bundling](https://parceljs.org/features/targets/#differential-bundling) will not work properly. This will likely result in unnecessary transpilation and larger bundle sizes. In addition, `@babel/preset-env` transpiles ES modules by default, which can cause issues with [scope hoisting](https://parceljs.org/features/scope-hoisting/).

`@babel/preset-env` and `@babel/plugin-transform-runtime` are not necessary, since transpilation for your browser targets is handled automatically by Parcel. However, if you need them for some reason, you can use Parcel's wrappers which are aware of Parcel's targets instead.

_babel.config.json:_

`{  "presets": ["@parcel/babel-preset-env"],  "plugins": ["@parcel/babel-plugin-transform-runtime"]}`

#### Usage with other tools

[#](https://parceljs.org/languages/javascript/#usage-with-other-tools)
While Parcel includes transpilation by default, you may still need to use Babel with other tools such as test runners like [Jest](https://jestjs.io/), and linters like [ESLint](https://eslint.org/). If this is the case, you may not be able to completely remove your Babel config. You can make Parcel ignore your Babel config instead, which will have performance benefits and prevent the other issues described above.

To disable Babel transpilation in Parcel, override the default Parcel config for JavaScript to exclude `@parcel/transformer-babel`.

_.parcelrc:_

`{  "extends": "@parcel/config-default",  "transformers": {    "*.{js,mjs,jsx,cjs,ts,tsx}": [      "@parcel/transformer-js",      "@parcel/transformer-react-refresh-wrap"    ]  }}`

This will allow other tools to continue using your Babel config, but disable Babel transpilation in Parcel.

Production
----------

[#](https://parceljs.org/languages/javascript/#production)
In production mode, Parcel includes optimizations to reduce the file size of your code. See [Production](https://parceljs.org/features/production/) for more details about how this works.

### Minification

[#](https://parceljs.org/languages/javascript/#minification)
In production mode, Parcel automatically minifies your code to reduce the file sizes of your bundles. By default, Parcel uses [SWC](https://swc.rs/) to perform minification. For backward compatibility, this supports [Terser](https://github.com/terser/terser) config files. To configure the minifier, you can create a `.terserrc` file in your project root directory. See the [SWC docs](https://swc.rs/docs/configuration/minification) for information about the available options.

Previous versions of Parcel used Terser as the default JavaScript minifier. To continue using Terser instead of SWC, you can configure Parcel to use the `@parcel/optimizer-terser` plugin in your `.parcelrc`. See [Plugins](https://parceljs.org/features/plugins/) for more information.

### Tree shaking

[#](https://parceljs.org/languages/javascript/#tree-shaking)
In production builds, Parcel statically analyzes the imports and exports of each module, and removes everything that isn't used. This is called "tree shaking" or "dead code elimination". Tree shaking is supported for both static and dynamic `import()`, CommonJS and ES modules, and even across languages with CSS modules.

Parcel also concatenates modules into a single scope when possible, rather than wrapping each module in a separate function. This is called “scope hoisting”. This helps make minification more effective, and also improves runtime performance by making references between modules static rather than dynamic object lookups.

See the [Scope hoisting](https://parceljs.org/features/scope-hoisting/) docs for tips to make tree shaking more effective.
