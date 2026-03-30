# Source: https://symfony.com/doc/8.0/frontend/asset_mapper.html

Title: AssetMapper: Simple, Modern CSS & JS Management (Symfony Docs)

URL Source: https://symfony.com/doc/8.0/frontend/asset_mapper.html

Markdown Content:
The AssetMapper component lets you write modern JavaScript and CSS without the complexity of using a bundler. Browsers _already_ support many modern JavaScript features like the `import` statement and ES6 classes. And the HTTP/2 protocol means that combining your assets to reduce HTTP connections is no longer urgent. This component is a light layer that helps serve your files directly to the browser.

The component has two main features:

* [Mapping & Versioning Assets](https://symfony.com/doc/current/frontend/asset_mapper.html#mapping-assets): All files inside of `assets/` are made available publicly and **versioned**. You can reference the file `assets/images/product.jpg` in a Twig template with `{{ asset('images/product.jpg') }}`. The final URL will include a version hash, like `/assets/images/product-3c16d92m.jpg`.
* [Importmaps](https://symfony.com/doc/current/frontend/asset_mapper.html#importmaps-javascript): A native browser feature that makes it easier to use the JavaScript `import` statement (e.g. `import { Modal } from 'bootstrap'`) without a build system. It's supported in all browsers (thanks to a shim) and is part of the [HTML standard](https://html.spec.whatwg.org/multipage/webappapis.html#import-maps).

[Installation](https://symfony.com/doc/8.0/frontend/asset_mapper.html#installation "Permalink to this headline")
----------------------------------------------------------------------------------------------------------------

To install the AssetMapper component, run:

In addition to `symfony/asset-mapper`, this also makes sure that you have the [Asset Component](https://symfony.com/doc/current/components/asset.html) and Twig available.

If you're using [Symfony Flex](https://symfony.com/doc/current/setup.html#symfony-flex), you're done! The recipe just added a number of files:

* `assets/app.js` Your main JavaScript file;
* `assets/styles/app.css` Your main CSS file;
* `config/packages/asset_mapper.yaml` Where you define your asset "paths";
* `importmap.php` Your importmap config file.

It also _updated_ the `templates/base.html.twig` file:

If you're not using Flex, you'll need to create & update these files manually. See the [latest asset-mapper recipe](https://github.com/symfony/recipes/tree/main/symfony/asset-mapper) for the exact content of these files.

[Mapping and Referencing Assets](https://symfony.com/doc/8.0/frontend/asset_mapper.html#mapping-and-referencing-assets "Permalink to this headline")
----------------------------------------------------------------------------------------------------------------------------------------------------

The AssetMapper component works by defining directories/paths of assets that you want to expose publicly. These assets are then versioned and easy to reference. Thanks to the `asset_mapper.yaml` file, your app starts with one mapped path: the `assets/` directory.

If you create an `assets/images/duck.png` file, you can reference it in a template with:

The path - `images/duck.png` - is relative to your mapped directory (`assets/`). This is known as the **logical path** to your asset.

If you look at the HTML in your page, the URL will be something like: `/assets/images/duck-3c16d92m.png`. If you change the file, the version part of the URL will also change automatically.

### [Serving Assets in dev vs prod](https://symfony.com/doc/8.0/frontend/asset_mapper.html#serving-assets-in-dev-vs-prod "Permalink to this headline")

In the `dev` environment, the URL `/assets/images/duck-3c16d92m.png` is handled and returned by your Symfony app.

For the `prod` environment, before deploy, you should run:

This will physically copy all the files from your mapped directories to `public/assets/` so that they're served directly by your web server. See [Deployment](https://symfony.com/doc/current/frontend/asset_mapper.html#asset-mapper-deployment) for more details.

Warning

If you run the `asset-map:compile` command on your development machine, you won't see any changes made to your assets when reloading the page. To resolve this, delete the contents of the `public/assets/` directory. This will allow your Symfony application to serve those assets dynamically again.

Tip

If you need to copy the compiled assets to a different location (e.g. upload them to S3), create a service that implements `Symfony\Component\AssetMapper\Path\PublicAssetsFilesystemInterface` and set its service id (or an alias) to `asset_mapper.local_public_assets_filesystem` (to replace the built-in service).

### [Debugging: Seeing All Mapped Assets](https://symfony.com/doc/8.0/frontend/asset_mapper.html#debugging-seeing-all-mapped-assets "Permalink to this headline")

To see all of the mapped assets in your app, run:

This will show you all the mapped paths and the assets inside of each:

The "Logical Path" is the path to use when referencing the asset, like from a template.

The `debug:asset-map` command provides several options to filter results:

[Importmaps & Writing JavaScript](https://symfony.com/doc/8.0/frontend/asset_mapper.html#importmaps-writing-javascript "Permalink to this headline")
----------------------------------------------------------------------------------------------------------------------------------------------------

All modern browsers support the JavaScript [import statement](https://caniuse.com/es6-module-dynamic-import) and modern [ES6](https://caniuse.com/es6) features like classes. So this code "just works":

Thanks to the `{{ importmap('app') }}` Twig function call, which you'll learn about in this section, the `assets/app.js` file is loaded & executed by the browser.

Tip

When importing relative files, be sure to include the `.js` filename extension. Unlike in Node.js, this extension is required in the browser environment.

### [Importing 3rd Party JavaScript Packages](https://symfony.com/doc/8.0/frontend/asset_mapper.html#importing-3rd-party-javascript-packages "Permalink to this headline")

Suppose you want to use an [npm package](https://www.npmjs.com/), like [bootstrap](https://www.npmjs.com/package/bootstrap). Technically, this can be done by importing its full URL, like from a CDN:

But yikes! Needing to include that URL is a pain! Instead, we can add this package to our "importmap" via the `importmap:require` command. This command can be used to add any [npm package](https://www.npmjs.com/):

Tip

Add the `--dry-run` option to simulate package installation without actually making any changes (e.g. `php bin/console importmap:require bootstrap --dry-run`)

This adds the `bootstrap` package to your `importmap.php` file:

Note

Sometimes, a package - like `bootstrap` - will have one or more dependencies, such as `@popperjs/core`. The `importmap:require` command will add both the main package _and_ its dependencies. If a package includes a main CSS file, that will also be added (see [Handling 3rd-Party CSS](https://symfony.com/doc/current/frontend/asset_mapper.html#asset-mapper-3rd-party-css)).

Note

If you get a 404 error, there might be some issue with the JavaScript package that prevents it from being served by the `jsDelivr` CDN. For example, the package might be missing properties like `main` or `module` in its [package.json configuration file](https://docs.npmjs.com/creating-a-package-json-file). Try to contact the package maintainer to ask them to fix those issues.

Tip

If you see a network error like *Connection was reset for "[https://cdn.jsdelivr.net/npm/..."*](https://cdn.jsdelivr.net/npm/...), it may be caused by a proxy or firewall restriction. In that case, you can temporarily configure a proxy to connect to the `jsDelivr` CDN:

Now you can import the `bootstrap` package like usual:

All packages in `importmap.php` are downloaded into an `assets/vendor/` directory, which should be ignored by git (the Flex recipe adds it to `.gitignore` for you). You'll need to run the following command to download the files on other computers if some are missing:

You can update your third-party packages to their current versions by running:

### [Using Local npm Packages](https://symfony.com/doc/8.0/frontend/asset_mapper.html#using-local-npm-packages "Permalink to this headline")

By default, `importmap:require` downloads packages from a CDN. If you prefer to install packages locally via npm (e.g. to use a specific build or a package not available on the CDN), you can point AssetMapper to your `node_modules/` directory.

First, install the package with npm and register the directory containing its browser-compatible files in your AssetMapper paths:

Using a namespace (like `hpcc`) for registered directories is highly recommended to avoid collisions in logical paths. For example, if both `assets/` and `node_modules/@hpcc-js/wasm-graphviz/dist/` contained an `index.js` file, only one of them would be mapped without namespaces.

Then, require the package in the importmap using the `--path` option to point to the local file using its logical path:

Now you can import the package as usual:

Note

Only the registered directories are served by AssetMapper. All relative imports inside those directories are resolved automatically. Make sure the registered directory includes every file the package needs for its browser imports.

### [Removing JavaScript Packages](https://symfony.com/doc/8.0/frontend/asset_mapper.html#removing-javascript-packages "Permalink to this headline")

If you need to remove a JavaScript package that was previously added to your `importmap.php` file, use the `importmap:remove` command. For example, to remove the `lodash` package:

This updates your `importmap.php` file and removes the specified package (along with any dependencies that were added with it).

After running this command, it's recommended to also run the following to ensure that your `assets/vendor/` directory is in sync with the updated import map:

Tip

Removing a package from the import map does not automatically remove any references to it in your JavaScript files. Make sure to update your code and remove any `import` statements that reference the removed package.

### [How does the importmap Work?](https://symfony.com/doc/8.0/frontend/asset_mapper.html#how-does-the-importmap-work "Permalink to this headline")

How does this `importmap.php` file allow you to import `bootstrap`? That's thanks to the `{{ importmap() }}` Twig function in `base.html.twig`, which outputs an [importmap](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script/type/importmap):

Import maps are a native browser feature. When you import `bootstrap` from JavaScript, the browser will look at the `importmap` and see that it should fetch the package from the associated path.

But where did the `/assets/duck.js` import entry come from? That doesn't live in `importmap.php`. Great question!

The `assets/app.js` file above imports `./duck.js`. When you import a file using a relative path, your browser looks for that file relative to the one importing it. So, it would look for `/assets/duck.js`. That URL _would_ be correct, except that the `duck.js` file is versioned. Fortunately, the AssetMapper component sees the import and adds a mapping from `/assets/duck.js` to the correct, versioned filename. The result: importing `./duck.js` just works!

The `importmap()` function also outputs an [ES module shim](https://www.npmjs.com/package/es-module-shims) so that [older browsers](https://caniuse.com/import-maps) understand importmaps (see the [polyfill config](https://symfony.com/doc/current/frontend/asset_mapper.html#config-importmap-polyfill)).

### [The "app" Entrypoint & Preloading](https://symfony.com/doc/8.0/frontend/asset_mapper.html#the-app-entrypoint-preloading "Permalink to this headline")

An "entrypoint" is the main JavaScript file that the browser loads, and your app starts with one by default:

In addition to the importmap, the `{{ importmap('app') }}` in `base.html.twig` outputs a few other things, including:

This line tells the browser to load the `app` importmap entry, which causes the code in `assets/app.js` to be executed.

The `importmap()` function also outputs a set of "preloads":

This is a performance optimization and you can learn more about below in [Performance: Add Preloading](https://symfony.com/doc/current/frontend/asset_mapper.html#performance-preloading).

### [Importing Specific Files From a 3rd Party Package](https://symfony.com/doc/8.0/frontend/asset_mapper.html#importing-specific-files-from-a-3rd-party-package "Permalink to this headline")

Sometimes you'll need to import a specific file from a package. For example, suppose you're integrating [highlight.js](https://www.npmjs.com/package/highlight.js) and want to import just the core and a specific language:

In this case, adding the `highlight.js` package to your `importmap.php` file won't work: whatever you import - e.g. `highlight.js/lib/core` - needs to _exactly_ match an entry in the `importmap.php` file.

Instead, use `importmap:require` and pass it the exact paths you need. This also shows how you can require multiple packages at once:

### [Global Variables like jQuery](https://symfony.com/doc/8.0/frontend/asset_mapper.html#global-variables-like-jquery "Permalink to this headline")

You might be accustomed to relying on global variables - like jQuery's `$` variable:

But in a module environment (like with AssetMapper), when you import a library like `jquery`, it does _not_ create a global variable. Instead, you should import it and set it to a variable in _every_ file you need it:

You can even do this from an inline script tag:

If you _do_ need something to become a global variable, you do it manually from inside `app.js`:

[Handling CSS](https://symfony.com/doc/8.0/frontend/asset_mapper.html#handling-css "Permalink to this headline")
----------------------------------------------------------------------------------------------------------------

CSS can be added to your page by importing it from a JavaScript file. The default `assets/app.js` already imports `assets/styles/app.css`:

When you call `importmap('app')` in `base.html.twig`, AssetMapper parses `assets/app.js` (and any JavaScript files that it imports) looking for `import` statements for CSS files. The final collection of CSS files is rendered onto the page as `link` tags in the order they were imported.

Note

Importing a CSS file is _not_ something that is natively supported by JavaScript modules. AssetMapper makes this work by adding an empty importmap entry for each CSS file (e.g. `"/assets/app.css": "data:application/javascript,"`). These special entries are valid, but do nothing: AssetMapper adds a `<link>` tag for each CSS file, and when JavaScript executes the `import` statement, nothing additional happens.

When using a **Content-Security-Policy** with `script-src 'self'`, this triggers an error because of the `data:` URL. You can either ignore the error or relax the directive to `script-src 'strict-dynamic'`.

### [Handling 3rd-Party CSS](https://symfony.com/doc/8.0/frontend/asset_mapper.html#handling-3rd-party-css "Permalink to this headline")

Sometimes a JavaScript package will contain one or more CSS files. For example, the `bootstrap` package has a [dist/css/bootstrap.min.css file](https://www.jsdelivr.com/package/npm/bootstrap?tab=files&path=dist%2Fcss#tabRouteFiles).

You can require CSS files in the same way as JavaScript files:

To include it on the page, import it from a JavaScript file:

Tip

Some packages - like `bootstrap` - advertise that they contain a CSS file. In those cases, when you `importmap:require bootstrap`, the CSS file is also added to `importmap.php` for convenience. If some package doesn't advertise its CSS file in the `style` property of the [package.json configuration file](https://docs.npmjs.com/creating-a-package-json-file) try to contact the package maintainer to ask them to add that.

### [Paths Inside of CSS Files](https://symfony.com/doc/8.0/frontend/asset_mapper.html#paths-inside-of-css-files "Permalink to this headline")

From inside CSS, you can reference other files using the normal CSS `url()` function and a relative path to the target file:

The path in the final `app.css` file will automatically include the versioned URL for `duck.png`:

### [Lazily Importing CSS from a JavaScript File](https://symfony.com/doc/8.0/frontend/asset_mapper.html#lazily-importing-css-from-a-javascript-file "Permalink to this headline")

If you have some CSS that you want to load lazily, you can do that via the normal, "dynamic" import syntax:

In this case, `lazy.css` will be downloaded asynchronously and then added to the page. If you use a dynamic import to lazily-load a JavaScript file and that file imports a CSS file (using the non-dynamic `import` syntax), that CSS file will also be downloaded asynchronously.

[Importing JSON files](https://symfony.com/doc/8.0/frontend/asset_mapper.html#importing-json-files "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------------------

Modern browsers support importing JSON files using the `import data from './foo.json' with { type: 'json' }` syntax, but browser support is still limited. AssetMapper provides a compatible alternative that works in all modern browsers without requiring any bundler.

Instead of using the native syntax, import JSON files using a standard import:

Consider a JSON file containing user data:

You can import and use this data in your JavaScript:

How it Works? When you import a JSON file, AssetMapper detects the import during asset processing, creates a JavaScript module that exports a Promise resolving to the JSON content, and adds it to the importmap. The imported JSON file is versioned like any other asset, so changes to the JSON content will produce a new filename and browsers will load the updated version.

[Issues and Debugging](https://symfony.com/doc/8.0/frontend/asset_mapper.html#issues-and-debugging "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------------------

There are a few common errors and problems you might run into.

### [Missing importmap Entry](https://symfony.com/doc/8.0/frontend/asset_mapper.html#missing-importmap-entry "Permalink to this headline")

One of the most common errors will come from your browser's console, and will look something like this:

> Failed to resolve module specifier "bootstrap". Relative references must start with either "/", "./", or "../".

or

> The specifier "bootstrap" was a bare specifier, but was not remapped to anything. Relative module specifiers must start with "./", "../" or "/".

This means that, somewhere in your JavaScript, you're importing a 3rd party package - e.g. `import 'bootstrap'`. The browser tries to find this package in your `importmap` file, but it's not there.

The fix is almost always to add it to your `importmap`:

Note

Some browsers, like Firefox, show _where_ this "import" code lives, while others like Chrome currently do not.

### [404 Not Found for a JavaScript, CSS or Image File](https://symfony.com/doc/8.0/frontend/asset_mapper.html#404-not-found-for-a-javascript-css-or-image-file "Permalink to this headline")

Sometimes a JavaScript file you're importing (e.g. `import './duck.js'`), or a CSS/image file you're referencing won't be found, and you'll see a 404 error in your browser's console. You'll also notice that the 404 URL is missing the version hash in the filename (e.g. a 404 to `/assets/duck.js` instead of a path like `/assets/duck-1b7a64b3.js`).

This is usually because the path is wrong. If you're referencing the file directly in a Twig template:

Then the path that you pass `asset()` should be the "logical path" to the file. Use the `debug:asset-map` command to see all valid logical paths in your app.

More likely, you're importing the failing asset from a CSS file (e.g. `@import url('other.css')`) or a JavaScript file:

When doing this, the path should be _relative_ to the file that's importing it (and, in JavaScript files, should start with `./` or `../`). In this case, `../farm/chicken.js` would point to `assets/farm/chicken.js`. To see a list of _all_ invalid imports in your app, run:

Any invalid imports will show up as warnings on top of the screen (make sure you have `symfony/monolog-bundle` installed):

The AssetMapper component looks in your JavaScript files for `import` lines so that it can [automatically add them to your importmap](https://symfony.com/doc/current/frontend/asset_mapper.html#automatic-import-mapping). This is done via regex and works very well, though it isn't perfect. If you comment-out an import, it will still be found and added to your importmap. That doesn't harm anything, but could be surprising.

If the imported path cannot be found, you'll see warning log when that asset is being built, which you can ignore.

[Deploying with the AssetMapper Component](https://symfony.com/doc/8.0/frontend/asset_mapper.html#deploying-with-the-assetmapper-component "Permalink to this headline")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

When you're ready to deploy, "compile" your assets by running this command:

This will write all your versioned asset files into the `public/assets/` directory, along with a few JSON files (`manifest.json`, `importmap.json`, etc.) so that the `importmap` can be rendered lightning fast.

[Optimizing Performance](https://symfony.com/doc/8.0/frontend/asset_mapper.html#optimizing-performance "Permalink to this headline")
------------------------------------------------------------------------------------------------------------------------------------

To make your AssetMapper-powered site fly, there are a few things you need to do. If you want to take a shortcut, you can use a service like [Cloudflare](https://www.cloudflare.com/), which will automatically do most of these things for you:

* **Use HTTP/2**: Your web server should be running HTTP/2 or HTTP/3 so the browser can download assets in parallel. HTTP/2 is automatically enabled in Caddy and can be activated in Nginx and Apache. Or, proxy your site through a service like Cloudflare, which will automatically enable HTTP/2 for you.
* **Compress your assets**: Your web server should compress (e.g. using gzip) your assets (JavaScript, CSS, images) before sending them to the browser. This is automatically enabled in Caddy and can be activated in Nginx and Apache. In Cloudflare, assets are compressed by default. AssetMapper also supports [precompressing your web assets](https://symfony.com/doc/current/frontend/asset_mapper.html#performance-precompressing) to further improve performance.
* **Set long-lived cache expiry**: Your web server should set a long-lived `Cache-Control` HTTP header on your assets. Because the AssetMapper component includes a version hash in the filename of each asset, you can safely set `max-age` to a very long time (e.g. 1 year). This isn't automatic in any web server, but can be easily enabled.

Once you've done these things, you can use a tool like [Lighthouse](https://developers.google.com/web/tools/lighthouse) to check the performance of your site.

### [Performance: Understanding Preloading](https://symfony.com/doc/8.0/frontend/asset_mapper.html#performance-understanding-preloading "Permalink to this headline")

One issue that Lighthouse may report is:

> Avoid Chaining Critical Requests

To understand the problem, imagine this theoretical setup:

* `assets/app.js` imports `./duck.js`
* `assets/duck.js` imports `bootstrap`

Without preloading, when the browser downloads the page, the following would happen:

1. The browser downloads `assets/app.js`;
2. It _then_ sees the `./duck.js` import and downloads `assets/duck.js`;
3. It _then_ sees the `bootstrap` import and downloads `assets/bootstrap.js`.

Instead of downloading all 3 files in parallel, the browser would be forced to download them one-by-one as it discovers them. That would hurt performance.

AssetMapper avoids this problem by outputting "preload" `link` tags. The logic works like this:

**A) When you call `importmap('app')` in your template**, the AssetMapper component looks at the `assets/app.js` file and finds all of the JavaScript files that it imports or files that those files import, etc.

**B) It then outputs a `link` tag** for each of those files with a `rel="preload"` attribute. This tells the browser to start downloading those files immediately, even though it hasn't yet seen the `import` statement for them.

Additionally, if the [WebLink Component](https://symfony.com/doc/current/web_link.html) is available in your application, Symfony will add a `Link` header in the response to preload the CSS files.

[Pre-Compressing Assets](https://symfony.com/doc/8.0/frontend/asset_mapper.html#pre-compressing-assets "Permalink to this headline")
------------------------------------------------------------------------------------------------------------------------------------

Although most web servers (Caddy, Nginx, Apache, FrankenPHP) and services like Cloudflare provide asset compression features, AssetMapper also allows you to compress all your assets before serving them.

This improves performance because you can compress assets using the highest (and slowest) compression ratios beforehand and provide those compressed assets to the server, which then returns them to the client without wasting CPU resources on compression.

AssetMapper supports [Brotli](https://en.wikipedia.org/wiki/Brotli), [Zstandard](https://en.wikipedia.org/wiki/Zstd) and [gzip](https://en.wikipedia.org/wiki/Gzip) compression formats. Before using any of them, the machine that pre-compresses assets must have installed the following PHP extensions or CLI commands:

* Brotli: `brotli` CLI command; [brotli PHP extension](https://pecl.php.net/package/brotli);
* Zstandard: `zstd` CLI command; [zstd PHP extension](https://pecl.php.net/package/zstd);
* gzip: `zopfli` (better) or `gzip` CLI command; [zlib PHP extension](https://www.php.net/manual/en/book.zlib.php).

Then, update your AssetMapper configuration to define which compression to use and which file extensions should be compressed:

Now, when running the `asset-map:compile` command, all matching files will be compressed in the configured format and at the highest compression level. The compressed files are created with the same name as the original but with the `.br`, `.zst`, or `.gz` extension appended.

Then, you need to configure your web server to serve the precompressed assets instead of the original ones:

Tip

AssetMapper provides an `assets:compress` CLI command and a service called `asset_mapper.compressor` that you can use anywhere in your application to compress any kind of files (e.g. files uploaded by users to your application).

[Frequently Asked Questions](https://symfony.com/doc/8.0/frontend/asset_mapper.html#frequently-asked-questions "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------------------------------

### [Does the AssetMapper Component Combine Assets?](https://symfony.com/doc/8.0/frontend/asset_mapper.html#does-the-assetmapper-component-combine-assets "Permalink to this headline")

Nope! But that's because this is no longer necessary!

In the past, it was common to combine assets to reduce the number of HTTP requests that were made. Thanks to advances in web servers like HTTP/2, it's typically not a problem to keep your assets separate and let the browser download them in parallel. In fact, by keeping them separate, when you update one asset, the browser can continue to use the cached version of all of your other assets.

See [Optimization](https://symfony.com/doc/current/frontend/asset_mapper.html#optimization) for more details.

### [Does the AssetMapper Component Minify Assets?](https://symfony.com/doc/8.0/frontend/asset_mapper.html#does-the-assetmapper-component-minify-assets "Permalink to this headline")

Nope! In most cases, this is perfectly fine. The web asset compression performed by web servers before sending them is usually sufficient. However, if you think you could benefit from minifying assets (in addition to later compressing them), you can use the [SensioLabs Minify Bundle](https://github.com/sensiolabs/minify-bundle).

This bundle integrates seamlessly with AssetMapper and minifies all web assets automatically when running the `asset-map:compile` command (as explained in the [serving assets in production](https://symfony.com/doc/current/frontend/asset_mapper.html#asset-mapper-compile-assets) section).

See [Optimization](https://symfony.com/doc/current/frontend/asset_mapper.html#optimization) for more details.

### [Is the AssetMapper Component Production Ready? Is it Performant?](https://symfony.com/doc/8.0/frontend/asset_mapper.html#is-the-assetmapper-component-production-ready-is-it-performant "Permalink to this headline")

Yes! Very! The AssetMapper component leverages advances in browser technology (like importmaps and native `import` support) and web servers (like HTTP/2, which allows assets to be downloaded in parallel). See the other questions about minimization and combination and [Optimization](https://symfony.com/doc/current/frontend/asset_mapper.html#optimization) for more details.

The [https://ux.symfony.com](https://ux.symfony.com/) site runs on the AssetMapper component and has a 99% Google Lighthouse score.

### [Does the AssetMapper Component work in All Browsers?](https://symfony.com/doc/8.0/frontend/asset_mapper.html#does-the-assetmapper-component-work-in-all-browsers "Permalink to this headline")

Yes! Features like importmaps and the `import` statement are supported in all modern browsers, but the AssetMapper component ships with an [ES module shim](https://www.npmjs.com/package/es-module-shims) to support `importmap` in old browsers. So, it works everywhere (see note below).

Inside your own code, if you're relying on modern [ES6](https://caniuse.com/es6) JavaScript features like the [class syntax](https://caniuse.com/es6-class), this is supported in all but the oldest browsers. If you _do_ need to support very old browsers, you should use a tool like [Encore](https://symfony.com/doc/current/frontend.html#frontend-webpack-encore) instead of the AssetMapper component.

Note

The [import statement](https://caniuse.com/es6-module-dynamic-import) can't be polyfilled or shimmed to work on _every_ browser. However, only the **oldest** browsers don't support it.

The `importmap` feature **is** shimmed to work in **all** browsers by the AssetMapper component (using [es-module-shims](https://www.npmjs.com/package/es-module-shims)). However, this shim only polyfills **import map** support; it does **not** polyfill the `import()` syntax itself, which is a native JavaScript feature.

AssetMapper correctly rewrites dynamic imports when the path is a string literal:

Browsers without [native import support](https://caniuse.com/es6-module-dynamic-import)) will fail regardless of AssetMapper. For those browsers, you can use [the importShim() function](https://www.npmjs.com/package/es-module-shims#polyfill-edge-case-dynamic-import) provided by the shim.

If you use a transpiler (e.g. Babel, TypeScript) that transforms `import()` calls, make sure to run it **before** AssetMapper compiles the assets. Otherwise the file hashes will change after transpilation and the versioned URLs will break.

### [Can I Use it with JSX or Vue?](https://symfony.com/doc/8.0/frontend/asset_mapper.html#can-i-use-it-with-jsx-or-vue "Permalink to this headline")

Probably not. And if you're writing an application in React, Svelte or another frontend framework, you'll probably be better off using _their_ tools directly.

JSX _can_ be compiled directly to a native JavaScript file but if you're using a lot of JSX, you'll probably want to use a tool like [Encore](https://symfony.com/doc/current/frontend.html#frontend-webpack-encore). See the [UX React Documentation](https://symfony.com/bundles/ux-react/current/index.html) for more details about using it with the AssetMapper component.

Vue files _can_ be written in native JavaScript, and those _will_ work with the AssetMapper component. But you cannot write single-file components (i.e. `.vue` files) with component, as those must be used in a build system. See the [UX Vue.js Documentation](https://symfony.com/bundles/ux-vue/current/index.html) for more details about using with the AssetMapper component.

### [Can I Lint and Format My Code?](https://symfony.com/doc/8.0/frontend/asset_mapper.html#can-i-lint-and-format-my-code "Permalink to this headline")

Not with AssetMapper, but you can install [kocal/biome-js-bundle](https://github.com/Kocal/BiomeJsBundle) in your project to lint and format your front-end assets. It's much faster than alternatives like Prettier and requires no configuration to handle your JavaScript, TypeScript and CSS files.

[Third-Party Bundles & Custom Asset Paths](https://symfony.com/doc/8.0/frontend/asset_mapper.html#third-party-bundles-custom-asset-paths "Permalink to this headline")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

All bundles that have a `Resources/public/` or `public/` directory will automatically have that directory added as an "asset path", using the namespace: `bundles/<BundleName>`. For example, if you're using [BabdevPagerfantaBundle](https://github.com/BabDev/PagerfantaBundle) and you run the `debug:asset-map` command, you'll see an asset whose logical path is `bundles/babdevpagerfanta/css/pagerfanta.css`.

This means you can render these assets in your templates using the `asset()` function:

Actually, this path - `bundles/babdevpagerfanta/css/pagerfanta.css` - already works in applications _without_ the AssetMapper component, because the `assets:install` command copies the assets from bundles into `public/bundles/`. However, when the AssetMapper component is enabled, the `pagerfanta.css` file will automatically be versioned! It will output something like:

### [Overriding 3rd-Party Assets](https://symfony.com/doc/8.0/frontend/asset_mapper.html#overriding-3rd-party-assets "Permalink to this headline")

If you want to override a 3rd-party asset, you can do that by creating a file in your `assets/` directory with the same name. For example, if you want to override the `pagerfanta.css` file, create a file at `assets/bundles/babdevpagerfanta/css/pagerfanta.css`. This file will be used instead of the original file.

Note

If a bundle renders their _own_ assets, but they use a non-default [asset package](https://symfony.com/doc/current/components/asset.html#asset-packages), then the AssetMapper component will not be used. This happens, for example, with [EasyAdminBundle](https://github.com/EasyCorp/EasyAdminBundle).

[Importing Assets Outside of the `assets/` Directory](https://symfony.com/doc/8.0/frontend/asset_mapper.html#importing-assets-outside-of-the-assets-directory "Permalink to this headline")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You _can_ import assets that live outside of your asset path (i.e. the `assets/` directory). For example:

However, if you get an error like this:

> The "app" importmap entry contains the path "vendor/some/package/assets/foo.js" but it does not appear to be in any of your asset paths.

It means that you're pointing to a valid file, but that file isn't in any of your asset paths. You can fix this by adding the path to your `asset_mapper.yaml` file:

Then try the command again.

[Configuration Options](https://symfony.com/doc/8.0/frontend/asset_mapper.html#configuration-options "Permalink to this headline")
----------------------------------------------------------------------------------------------------------------------------------

You can see every available configuration options and some info by running:

Some of the more important options are described below.

### [`framework.asset_mapper.paths`](https://symfony.com/doc/8.0/frontend/asset_mapper.html#framework-asset-mapper-paths "Permalink to this headline")

This config holds all of the directories that will be scanned for assets. This can be a simple list:

Or you can give each path a "namespace" that will be used in the asset map:

In this case, the "logical path" to all of the files in the `vendor/some/package/assets/` directory will be prefixed with `some-package` - e.g. `some-package/foo.js`.

### [`framework.asset_mapper.excluded_patterns`](https://symfony.com/doc/8.0/frontend/asset_mapper.html#framework-asset-mapper-excluded-patterns "Permalink to this headline")

This is a list of glob patterns that will be excluded from the asset map:

You can use the `debug:asset-map` command to double-check that the files you expect are being included in the asset map.

### [`framework.asset_mapper.exclude_dotfiles`](https://symfony.com/doc/8.0/frontend/asset_mapper.html#framework-asset-mapper-exclude-dotfiles "Permalink to this headline")

Whether to exclude any file starting with a `.` from the asset mapper. This is useful if you want to avoid leaking sensitive files like `.env` or `.gitignore` in the files published by the asset mapper.

This option is enabled by default.

### [`framework.asset_mapper.importmap_polyfill`](https://symfony.com/doc/8.0/frontend/asset_mapper.html#framework-asset-mapper-importmap-polyfill "Permalink to this headline")

Configure the polyfill for older browsers. By default, the [ES module shim](https://www.npmjs.com/package/es-module-shims) is loaded via a CDN (i.e. the default value for this setting is `es-module-shims`):

Tip

You can tell the AssetMapper to load the [ES module shim](https://www.npmjs.com/package/es-module-shims) locally by using the following command, without changing your configuration:

### [`framework.asset_mapper.importmap_script_attributes`](https://symfony.com/doc/8.0/frontend/asset_mapper.html#framework-asset-mapper-importmap-script-attributes "Permalink to this headline")

This is a list of attributes that will be added to the `<script>` tags rendered by the `{{ importmap() }}` Twig function:

[Page-Specific CSS & JavaScript](https://symfony.com/doc/8.0/frontend/asset_mapper.html#page-specific-css-javascript "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------------------------------------

Sometimes you may choose to include CSS or JavaScript files only on certain pages. For JavaScript, an easy way is to load the file with a [dynamic import](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import):

Another option is to create a separate [entrypoint](https://symfony.com/doc/current/frontend/asset_mapper.html#app-entrypoint). For example, create a `checkout.js` file that contains whatever JavaScript and CSS you need:

Next, add this to `importmap.php` and mark it as an entrypoint:

Finally, on the page that needs this JavaScript, call `importmap()` and pass both `app` and `checkout`:

The `importmap()` function always includes the full import map to ensure all module definitions are available on the page. It also adds a `<script type="module">` tag to load the specific JavaScript entry files you pass to it (in the example above, the `app.js` file _and_ the `checkout.js` file).

Warning

Do not call `parent()` inside the `{% block importmap %}` Twig block. Each page can include only one import map, so `importmap()` must be called exactly once.

If you want to execute _only_`checkout.js` (and not `app.js`), call `{{ importmap('checkout') }}`. In this case, the full import map will still be included in the page, but only the `checkout.js` file will actually be loaded.

[Using a Content Security Policy (CSP)](https://symfony.com/doc/8.0/frontend/asset_mapper.html#using-a-content-security-policy-csp "Permalink to this headline")
----------------------------------------------------------------------------------------------------------------------------------------------------------------

If you're using a [Content Security Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP) (CSP) to prevent cross-site scripting attacks, the inline `<script>` tags rendered by the `importmap()` function will likely violate that policy and will not be executed by the browser.

To allow these scripts to run without disabling the security provided by the CSP, you can generate a secure random string for every request (called a _nonce_) and include it in the CSP header and in a `nonce` attribute on the `<script>` tags. The `importmap()` function accepts an optional second argument that can be used to pass attributes to the rendered `<script>` tags. You can use the [NelmioSecurityBundle](https://symfony.com/bundles/NelmioSecurityBundle/current/index.html#nonce-for-inline-script-handling) to generate the nonce and include it in the CSP header, and then pass the same nonce to the Twig function:

### [Content Security Policy and CSS Files](https://symfony.com/doc/8.0/frontend/asset_mapper.html#content-security-policy-and-css-files "Permalink to this headline")

If your importmap includes CSS files, AssetMapper uses a trick to load those by adding `data:application/javascript` to the rendered importmap (see [Handling CSS](https://symfony.com/doc/current/frontend/asset_mapper.html#asset-mapper-handling-css)).

This can cause browsers to report CSP violations and block the CSS files from being loaded. To prevent this, you can add [strict-dynamic](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/script-src#strict-dynamic) to the `script-src` directive of your Content Security Policy, to tell the browser that the importmap is allowed to load other resources.

Note

When using `strict-dynamic`, the browser will ignore any other sources in `script-src` such as `'self'` or `'unsafe-inline'`, so any other `<script>` tags will also need to be trusted via a nonce.

[The AssetMapper Component Caching System in dev](https://symfony.com/doc/8.0/frontend/asset_mapper.html#the-assetmapper-component-caching-system-in-dev "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

When developing your app in debug mode, the AssetMapper component will calculate the content of each asset file and cache it. Whenever that file changes, the component will automatically re-calculate the content.

The system also accounts for "dependencies": If `app.css` contains `@import url('other.css')`, then the `app.css` file contents will also be re-calculated whenever `other.css` changes. This is because the version hash of `other.css` will change... which will cause the final content of `app.css` to change, since it includes the final `other.css` filename inside.

Mostly, this system just works. But if you have a file that is not being re-calculated when you expect it to, you can run:

This will force the AssetMapper component to re-calculate the content of all files.

[Run Security Audits on Your Dependencies](https://symfony.com/doc/8.0/frontend/asset_mapper.html#run-security-audits-on-your-dependencies "Permalink to this headline")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Similar to `npm`, the AssetMapper component comes bundled with a command that checks security vulnerabilities in the dependencies of your application:

The command will return the `0` exit code if no vulnerability is found, or the `1` exit code otherwise. This means that you can seamlessly integrate this command as part of your CI to be warned anytime a new vulnerability is found.

Tip

The command takes a `--format` option to choose the output format between `txt` and `json`.

This work, including the code samples, is licensed under a [Creative Commons BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) license.
