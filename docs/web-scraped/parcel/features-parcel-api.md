# Source: https://parceljs.org/features/parcel-api/

Title: Parcel API

URL Source: https://parceljs.org/features/parcel-api/

Markdown Content:
The Parcel API can be used to programmatically run builds or watch a project for changes. It is the same API as is used by the Parcel CLI. Use the API when you need more flexibility, or need to integrate Parcel into another build system.

The `Parcel` constructor
------------------------

[#](https://parceljs.org/features/parcel-api/#the-parcel-constructor)
The Parcel API can be used through the `@parcel/core` package. You'll also need a default configuration, such as `@parcel/config-default`.

`yarn add @parcel/core @parcel/config-default`
Next, import this package into your program and call the `Parcel` constructor. It accepts an [`InitialParcelOptions`](https://parceljs.org/plugin-system/api/#InitialParcelOptions) object, which contains all of the options used by the Parcel CLI and a few more.

There are two required parameters:

*   `entries` – A string or an array of strings describing the entry points to build. See [Entries](https://parceljs.org/features/targets/#entries).
*   `config` or `defaultConfig` – A file path or package specifier for a Parcel config to use. If `config` is set, the provided config is always used and the project `.parcelrc` is ignored. If `defaultConfig` is set, the project's `.parcelrc` takes precedence, and `defaultConfig` is used as a fallback. If a relative path or package specifier is given, it is resolved relative to the project root.

_build.mjs:_

`import {Parcel} from '@parcel/core';let bundler = new Parcel({  entries: 'a.js',  defaultConfig: '@parcel/config-default'});`

### Targets

[#](https://parceljs.org/features/parcel-api/#targets)
By default, Parcel does a development build, but this can be changed by setting the `mode` option to `production`, which enable scope hoisting, minification, etc. See [Production](https://parceljs.org/features/production/).

You can also use the `defaultTargetOptions` to set values for [Targets](https://parceljs.org/features/targets/) if they aren't configured in the project. For example, to override the default browser targets, use the `engines` option.

_build.mjs:_

`import {Parcel} from '@parcel/core';let bundler = new Parcel({  entries: 'a.js',  defaultConfig: '@parcel/config-default',  mode: 'production',  defaultTargetOptions: {    engines: {      browsers: ['last 1 Chrome version']    }  }});`

When set to an array, the `targets` option can be used to specify which of the project’s targets (as described in `package.json`) to build. For example, to only build the project’s `modern` target:

_build.mjs:_

`import {Parcel} from '@parcel/core';let bundler = new Parcel({  entries: 'a.js',  defaultConfig: '@parcel/config-default',  targets: ['modern']});`

Alternatively, `targets` may be set to an object, which will override any targets defined in the project. See [Targets](https://parceljs.org/features/targets/) for more details on the available options.

_build.mjs:_

`import {Parcel} from '@parcel/core';let bundler = new Parcel({  entries: 'a.js',  defaultConfig: '@parcel/config-default',  mode: 'production',  targets: {    modern: {      engines: {        browsers: ['last 1 Chrome version']      }    },    legacy: {      engines: {        browsers: ['IE 11']      }    }  }});`

### Environment variables

[#](https://parceljs.org/features/parcel-api/#environment-variables)
Environment variables such as `NODE_ENV` may be set using the `env` option. This allows variables to be set without overriding the values on `process.env`.

_build.mjs:_

`import {Parcel} from '@parcel/core';let bundler = new Parcel({  entries: 'a.js',  defaultConfig: '@parcel/config-default',  mode: 'production',  env: {    NODE_ENV: 'production'  }});`

### Reporters

[#](https://parceljs.org/features/parcel-api/#reporters)
By default, Parcel does not write any output to the CLI when you use the API. That means it won’t report status information, and provides no pretty formatting for diagnostics. These can be enabled using the `additionalReporters` option, which run in addition to any reporters specified in `.parcelrc`. The `@parcel/reporter-cli` plugin provides the default reporter used by the CLI, but you can use any other reporter plugins as well.

_build.mjs:_

`import {Parcel} from '@parcel/core';import {fileURLToPath} from 'url';let bundler = new Parcel({  entries: 'a.js',  defaultConfig: '@parcel/config-default',  additionalReporters: [    {      packageName: '@parcel/reporter-cli',      resolveFrom: fileURLToPath(import.meta.url)    }  ]});`

Building
--------

[#](https://parceljs.org/features/parcel-api/#building)
Once you’ve constructed a `Parcel` instance, you can use it to build a project or watch for changes. To build once, use the `run` API. This returns a Promise, which will be resolved with a [`BuildSuccessEvent`](https://parceljs.org/plugin-system/reporter/#BuildSuccessEvent) containing the [`BundleGraph`](https://parceljs.org/plugin-system/bundler/#BundleGraph) and some other information if the build was successful, or reject with an error if it failed. Build errors have one or more [`Diagnostic`](https://parceljs.org/plugin-system/logging/#Diagnostic) objects attached to them with the details of what went wrong.

_build.mjs:_

`import {Parcel} from '@parcel/core';let bundler = new Parcel({  entries: 'a.js',  defaultConfig: '@parcel/config-default'});try {  let {bundleGraph, buildTime} = await bundler.run();  let bundles = bundleGraph.getBundles();  console.log(`✨ Built ${bundles.length} bundles in ${buildTime}ms!`);} catch (err) {  console.log(err.diagnostics);}`

Watching
--------

[#](https://parceljs.org/features/parcel-api/#watching)
To watch a project for changes and be notified of each rebuild, use the `watch` API. Pass a callback to be called whenever a build succeeds or fails. The callback receives an error parameter and an event object. The error parameter is only used for fatal errors during watching. Normal build failures are represented by a [`BuildFailureEvent`](https://parceljs.org/plugin-system/reporter/#BuildFailureEvent), which includes a list of [`Diagnostic`](https://parceljs.org/plugin-system/logging/#Diagnostic) objects.

`watch` also returns a subscription object, and you should call the `unsubscribe` method when you’d like to stop watching.

_build.mjs:_

`import {Parcel} from '@parcel/core';let bundler = new Parcel({  entries: 'a.js',  defaultConfig: '@parcel/config-default'});let subscription = await bundler.watch((err, event) => {  if (err) {    // fatal error    throw err;  }  if (event.type === 'buildSuccess') {    let bundles = event.bundleGraph.getBundles();    console.log(`✨ Built ${bundles.length} bundles in ${event.buildTime}ms!`);  } else if (event.type === 'buildFailure') {    console.log(event.diagnostics);  }});// some time later...await subscription.unsubscribe();`

Dev server
----------

[#](https://parceljs.org/features/parcel-api/#dev-server)
The development server is included in the default Parcel config. It can be enabled by passing `serveOptions` to the `Parcel` constructor and running Parcel in watch mode. Hot reloading can be enabled by setting `hmrOptions`. A `port` is the only required option, but others such as HTTPS options may also be set.

_build.mjs:_

`import {Parcel} from '@parcel/core';let bundler = new Parcel({  entries: 'a.js',  defaultConfig: '@parcel/config-default',  serveOptions: {    port: 3000  },  hmrOptions: {    port: 3000  }});await bundler.watch();`

File system
-----------

[#](https://parceljs.org/features/parcel-api/#file-system)
Parcel uses an abstracted file system throughout core and in most plugins. By default, it relies on the Node.js `fs` API, but Parcel also has a `MemoryFS` implementation. You can use the `inputFS` option to override the file system Parcel reads source files from, and the `outputFS` option to override the file system Parcel writes output (including the cache) to.

The `MemoryFS` is located in the `@parcel/fs` package. Constructing it requires passing a `WorkerFarm` instance so that the file system can be read and written to from multiple threads. You’ll need to create a worker farm using the `createWorkerFarm` function exported from `@parcel/core`, and pass this to both the `MemoryFS` and `Parcel` constructors. When you are done, make sure to call `end` on the worker farm to allow the process to exit.

This example writes its output into an in-memory file system, and logs the contents of each built bundle.

_build.mjs:_

`import {Parcel, createWorkerFarm} from '@parcel/core';import {MemoryFS} from '@parcel/fs';let workerFarm = createWorkerFarm();let outputFS = new MemoryFS(workerFarm);let bundler = new Parcel({  entries: 'a.js',  defaultConfig: '@parcel/config-default',  workerFarm,  outputFS});try {  let {bundleGraph} = await bundler.run();  for (let bundle of bundleGraph.getBundles()) {    console.log(bundle.filePath);    console.log(await outputFS.readFile(bundle.filePath, 'utf8'));  }} finally {  await workerFarm.end();}`
