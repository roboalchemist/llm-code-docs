# Source: https://docs.datadoghq.com/tracing/other_telemetry/connect_logs_and_traces/nodejs.md

# Source: https://docs.datadoghq.com/tracing/trace_collection/dynamic_instrumentation/enabling/nodejs.md

# Source: https://docs.datadoghq.com/tracing/trace_collection/library_config/nodejs.md

# Source: https://docs.datadoghq.com/tracing/trace_collection/compatibility/nodejs.md

# Source: https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/opentracing/nodejs.md

# Source: https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/nodejs.md

---
title: Tracing Node.js Applications
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > APM > Application Instrumentation > Add the Datadog Tracing Library >
  Tracing Node.js Applications
source_url: https://docs.datadoghq.com/trace_collection/dd_libraries/nodejs/index.html
---

# Tracing Node.js Applications

## Compatibility requirements{% #compatibility-requirements %}

The latest Node.js Tracer supports Node.js versions `>=18`. For a full list of Datadog's Node.js version and framework support (including legacy and maintenance versions), see the [Compatibility Requirements](https://docs.datadoghq.com/tracing/compatibility_requirements/nodejs) page.

## Getting started{% #getting-started %}

Before you begin, make sure you've already [installed and configured the Agent](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/?tab=datadoglibraries#install-and-configure-the-agent). Then, complete the following steps to add the Datadog tracing library to your Node.js application to instrument it.

### Install the Datadog tracing library{% #install-the-datadog-tracing-library %}

To install the Datadog tracing library using npm for Node.js 18+, run:

```shell
npm install dd-trace --save
```

To install the Datadog tracing library (version 4.x of `dd-trace`) for end-of-life Node.js version 16, run:

```shell
npm install dd-trace@latest-node16
```

For more information on Datadog's distribution tags and Node.js runtime version support, see the [Compatibility Requirements](https://docs.datadoghq.com/tracing/compatibility_requirements/nodejs) page. If you are upgrading from a previous major version of the library (0.x, 1.x, 2.x, 3.x or 4.x) to another major version, read the [Migration Guide](https://github.com/DataDog/dd-trace-js/blob/master/MIGRATING.md) to assess any breaking changes.

### Import and initialize the tracer{% #import-and-initialize-the-tracer %}

Import and initialize the tracer either in code or with command line arguments. The Node.js tracing library needs to be imported and initialized **before** any other module.

{% alert level="info" %}
With frameworks like **Next.js** and **Nest.js** you must either provide an environment variable or add an additional Node.js flag. See [Complex framework usage](https://docs.datadoghq.com/tracing/trace_collection/compatibility/nodejs/#complex-framework-usage) for more information.
{% /alert %}

After you have completed setup, if you are not receiving complete traces, including missing URL routes for web requests, or disconnected or missing spans, **confirm the tracer has been imported and initialized correctly**. The tracing library being initialized first is necessary for the tracer to properly patch all of the required libraries for automatic instrumentation.

When using a transpiler such as TypeScript, Webpack, Babel, or others, import and initialize the tracer library in an external file and then import that file as a whole when building your application.

#### Option 1: Add the tracer in code{% #option-1-add-the-tracer-in-code %}

##### JavaScript{% #javascript %}

```javascript
// This line must come before importing any instrumented module.
const tracer = require('dd-trace').init();
```

**Note**: `DD_TRACE_ENABLED` is `true` by default, which means some instrumentation occurs at import time, before initialization. To fully disable instrumentation, you can do one of the following:

- import the module conditionally
- set `DD_TRACE_ENABLED=false` (if, for example, static or top-level ESM imports prevent conditional loading)

##### TypeScript and bundlers{% #typescript-and-bundlers %}

For TypeScript and bundlers that support ECMAScript Module syntax, initialize the tracer in a separate file to maintain correct load order.

```typescript
// server.ts
import './tracer'; // must come before importing any instrumented module.

// tracer.ts
import tracer from 'dd-trace';
tracer.init(); // initialized in a different file to avoid hoisting.
export default tracer;
```

If the default config is sufficient, or all configuration is done via environment variables, you can also use `dd-trace/init`, which loads and initializes in one step.

```typescript
import 'dd-trace/init';
```

#### Option 2: Add the tracer with command line arguments{% #option-2-add-the-tracer-with-command-line-arguments %}

Use the `--require` option to Node.js to load and initialize the tracer in one step.

```sh
node --require dd-trace/init app.js
```

**Note:** This approach requires using environment variables for all configuration of the tracer.

#### ESM applications only: Import the loader{% #esm-applications-only-import-the-loader %}

ECMAScript Modules (ESM) applications require an *additional* command line argument. Add this argument regardless of how the tracer is otherwise imported and initialized:

- **Node.js < v20.6:** `--loader dd-trace/loader-hook.mjs`
- **Node.js >= v20.6:** `--import dd-trace/register.js`

For example, in Node.js 22, if initializing the tracer using option one from above, you would start it like this:

```sh
node --import dd-trace/register.js app.js
```

This can also be combined with the `--require dd-trace/init` command line argument (option two):

```sh
node --import dd-trace/register.js --require dd-trace/init app.js
```

A shorthand exists to combine both command line arguments in Node.js v20.6 and above:

```sh
node --import dd-trace/initialize.mjs app.js
```

### Bundling{% #bundling %}

`dd-trace` works by intercepting `require()` calls that a Node.js application makes when loading modules. This includes modules that are built-in to Node.js, like the `fs` module for accessing the filesystem, as well as modules installed from the NPM registry, like the `pg` database module.

Bundlers crawl all of the `require()` calls that an application makes to files on disk. It replaces the `require()` calls with custom code and combines all of the resulting JavaScript into one "bundled" file. When a built-in module is loaded, such as `require('fs')`, that call can then remain the same in the resulting bundle.

APM tools like `dd-trace` stop working at this point. They can continue to intercept the calls for built-in modules but don't intercept calls to third party libraries. This means that when you bundle a `dd-trace` app with a bundler it is likely to capture information about disk access (through `fs`) and outbound HTTP requests (through `http`), but omit calls to third party libraries. For example:

- Extracting incoming request route information for the `express` framework.
- Showing which query is run for the `mysql` database client.

A common workaround is to treat all third party modules that the APM needs to instrument as being "external" to the bundler. With this setting the instrumented modules remain on disk and continue to be loaded with `require()` while the non-instrumented modules are bundled. However, this results in a build with many extraneous files and starts to defeat the purpose of bundling.

Datadog recommends you have custom-built bundler plugins. These plugins are able to instruct the bundler on how to behave, inject intermediary code and intercept the "translated" `require()` calls. As a result, more packages are included in the bundled JavaScript file.

**Note**: Some applications can have 100% of modules bundled, however native modules still need to remain external to the bundle.

#### Bundling with esbuild{% #bundling-with-esbuild %}

This library provides experimental esbuild support in the form of an esbuild plugin, and requires at least Node.js v16.17 or v18.7. To use the plugin, make sure you have `dd-trace@3+` installed, and then require the `dd-trace/esbuild` module when building your bundle.

Here's an example of how one might use `dd-trace` with esbuild:

```javascript
const ddPlugin = require('dd-trace/esbuild')
const esbuild = require('esbuild')

esbuild.build({
  entryPoints: ['app.js'],
  bundle: true,
  outfile: 'out.js',
  plugins: [ddPlugin],
  platform: 'node', // allows built-in modules to be required
  target: ['node16'],
  external: [
    // required if you use native metrics
    '@datadog/native-metrics',

    // required if you use profiling
    '@datadog/pprof',

    // required if you use Datadog security features
    '@datadog/native-appsec',
    '@datadog/native-iast-taint-tracking',
    '@datadog/native-iast-rewriter',

    // required if you encounter graphql errors during the build step
    'graphql/language/visitor',
    'graphql/language/printer',
    'graphql/utilities'
  ]
}).catch((err) => {
  console.error(err)
  process.exit(1)
})
```

#### Bundling with Next.js{% #bundling-with-nextjs %}

If you are using Next.js or another framework relying on webpack to bundle your application, add a declaration similar to the one for webpack inside your `next.config.js` configuration file:

```javascript
/** @type {import('next').NextConfig} */
const nextConfig = {
  // ... non-relevant parts omitted, substitute your own config ...

  // this custom webpack config is required for Datadog tracing to work
  webpack: (
    config,
    { buildId, dev, isServer, defaultLoaders, nextRuntime, webpack }
  ) => {
    const externals = [
      // required if you use native metrics
      '@datadog/native-metrics',

      // required if you use profiling
      '@datadog/pprof',

      // required if you use Datadog security features
      '@datadog/native-appsec',
      '@datadog/native-iast-taint-tracking',
      '@datadog/native-iast-rewriter',

      // required if you encounter graphql errors during the build step
      'graphql/language/visitor',
      'graphql/language/printer',
      'graphql/utilities'
    ];
    config.externals.push(...externals);
    return config;
  },
};

export default nextConfig;
```

#### Unsupported Datadog features{% #unsupported-datadog-features %}

The following features are turned off by default in the Node.js tracer. They do not support bundling and cannot be used if your application is bundled.

- APM: Dynamic Instrumentation

#### General bundling remarks{% #general-bundling-remarks %}

**Note**: Due to the usage of native modules in the tracer, which are compiled C++ code, (usually ending with a `.node` file extension), you need to add entries to your `external` list. Currently native modules used in the Node.js tracer live inside of `@datadog` prefixed packages. This will also require that you ship a `node_modules/` directory alongside your bundled application. You don't need to ship your entire `node_modules/` directory as it would contain many superfluous packages that should be contained in your bundle.

To generate a smaller `node_modules/` directory with only the required native modules, (and their dependencies) you can first determine the versions of packages that you need, then create a temporary directory to install them into, and copy the resulting `node_modules/` directory from it. For example:

```sh
cd path/to/project
npm ls @datadog/native-metrics
# dd-trace@5.4.3-pre ./dd-trace-js
# âââ @datadog/native-metrics@2.0.0
$ npm ls @datadog/pprof
# dd-trace@5.4.3-pre ./dd-trace-js
# âââ @datadog/pprof@5.0.0
mkdir temp && cd temp
npm init -y
npm install @datadog/native-metrics@2.0.0 @datadog/pprof@5.0.0
cp -R ./node_modules path/to/bundle
```

**Note**: In case of Next.js the `path/to/bundle` is usually the `.next/standalone` directory of your app.

At this stage you should be able to deploy your bundle, (which is your application code and most of your dependencies), with the `node_modules/` directory, which contains the native modules and their dependencies.

## Configuration{% #configuration %}

If needed, configure the tracing library to send application performance telemetry data as you require, including setting up Unified Service Tagging. Read [Library Configuration](https://docs.datadoghq.com/tracing/trace_collection/library_config/nodejs/) for details.

Read [tracer settings](https://datadog.github.io/dd-trace-js/#tracer-settings) for a list of initialization options.

## Further Reading{% #further-reading %}

- [Source code](https://github.com/DataDog/dd-trace-js)
- [API documentation](https://datadog.github.io/dd-trace-js)
- [Explore your services, resources and traces](https://docs.datadoghq.com/tracing/glossary/)
- [Advanced Usage](https://docs.datadoghq.com/tracing/)
