# Plugins

Source: https://knip.dev/explanations/plugins

This page describes why Knip uses plugins and the difference betweenconfigandentryfiles.

Knip has an extensive and growinglist of built-in plugins. Feel free towrite a pluginso others can benefit too!

## What does a plugin do?

Plugins are enabled if the related package is listed in the list of dependencies
inpackage.json. For instance, ifastrois listed independenciesordevDependencies, then the Astro plugin is enabled. And this means that this
plugin will:

- Handleconfiguration fileslikeastro.config.mjs
- Addentry filessuch assrc/pages/**/*.astro
- Definecommand-line arguments

## Configuration files

Knip usesentry filesas starting points to scan your source code and
resolve other internal files and external dependencies. The module graph can be
statically resolved through therequireandimportstatements in those
source files. However, configuration files reference external dependencies in
various ways. Knip uses a plugin for each tool to parse configuration files and
find those dependencies.

### Example: ESLint

In the first example we look atthe ESLint plugin. The defaultconfigfile patterns include.eslintrc.json. Here’s a minimal example:

```typescript
{"extends":["airbnb","prettier"],"plugins":["@typescript-eslint"]}
```

Configuration files like this don’timportorrequireanything, but they do
require the referenced dependencies to be installed.

In this case, the plugin will return three dependencies:

- eslint-config-airbnb
- eslint-config-prettier
- @typescript-eslint/eslint-plugin

Knip will then look for missing dependencies inpackage.jsonand report those
as unlisted. And vice versa, if there are any ESLint plugins listed inpackage.json, but unused, those will be reported as well.

### Example: Vitest

The second example usesthe Vitest plugin. Here’s a minimal example of a
Vitest configuration file:

```typescript
import{ defineConfig }from'vitest/config';exportdefaultdefineConfig({test:{coverage:{provider:'istanbul',},environment:'happy-dom',},});
```

The Vitest plugin reads this configuration and returns two dependencies:

- @vitest/coverage-istanbul
- vitest-environment-happy-dom

Knip will look for missing and unused dependencies inpackage.jsonand report
accordingly.

Some tools allow configuration to be stored inpackage.json, that’s why some
plugins containpackage.jsonin the list ofconfigfiles.

Plugins parseconfigfiles to find external dependencies. Knip uses this to
determine unused and unlisted dependencies.

## Entry files

Many plugins have defaultentryfiles configured. When the plugin is enabled,
Knip will add entry files as configured by the plugin to resolve used files and
dependencies.

For example, ifnextis listed as a dependency inpackage.json, the Next.js
plugin will automatically add multiple patterns as entry files, such aspages/**/*.{js,jsx,ts,tsx}. Ifvitestis listed, the Vitest plugin adds**/*.{test,test-d,spec}.tsas entry file patterns. Most plugins have entry
files configured, so you don’t have to.

It’s mostly plugins for meta frameworks and test runners that haveentryfiles
configured.

Plugins result in less configuration

Plugins uses entry file patterns as defined in your configuration file of these
tools. So you don’t need to repeat this in your Knip configuration.

For example, let’s say your Playwright configuration contains the following:

```typescript
importtype{ PlaywrightTestConfig }from'@playwright/test';constconfig:PlaywrightTestConfig={testDir:'integration',testMatch:['**/*-test.ts'],};exportdefaultconfig;
```

The Playwright plugin will read this configuration file and return those entry
patterns (integration/**/*-test.ts). Knip will then not use the default entry
patterns.

You can still override this behavior in your Knip configuration:

```typescript
{"playwright":{"entry":"src/**/*.integration.ts"}}
```

This should not be necessary though. Please consider opening a pull request or a
bug report if any plugin is not behaving as expected.

Plugins try hard to automatically add the correct entry files.

## Entry files from config files

Entry files are part of plugin configuration (as described in the previous
section). Yet plugins can also return additional entry files after parsing
configuration files. Below are some examples of configuration files parsed by
plugins to return additional entry files. The goal of these examples is to give
you an idea about the various ways Knip and its plugins try to find entry files
so you don’t need to configure them yourself.

### Angular

The Angular plugin parses the Angular configuration file. Here’s a fragment:

```typescript
{"$schema":"./node_modules/@angular/cli/lib/config/schema.json","projects":{"knip-angular-example":{"architect":{"build":{"builder":"@angular-devkit/build-angular:browser","options":{"outputPath":"dist/knip-angular-example","main":"src/main.ts","tsConfig":"tsconfig.app.json"}}}}}}
```

This will result insrc/main.tsbeing added as an entry file (and@angular-devkit/build-angularas a referenced dependency).

Additionally, the Angular plugin returnstsconfig.app.jsonas a configuration
file for the TypeScript plugin.

### GitHub Actions

This plugin parses workflow YAML files. This fragment contains threerunscripts:

```typescript
jobs:integration:runs-on:ubuntu-lateststeps:-run:npm install-run:node scripts/build.js-run:node --loader tsx scripts/deploy.ts-run:playwright test -c playwright.web.config.tsworking-dir:e2e
```

From these scripts, thescripts/build.jsandscripts/deploy.tsfiles will be
added as entry files by the GitHub Actions plugin.

Additionally, the filee2e/playwright.web.config.tsis detected and will be
handed over as a Playwright configuration file.

Read more about this incommand-line arguments.

### webpack

Let’s take a look at this example webpack configuration file:

```typescript
module.exports=env=>{return{entry:{main:'./src/app.ts',vendor:'./src/vendor.ts',},module:{rules:[{test:/\.(woff|ttf|ico|woff2|jpg|jpeg|png|webp)$/i,use:'base64-inline-loader',},],},};};
```

The webpack plugin will parse this and add./src/app.tsand./src/vendor.tsas entry files. It will also addbase64-inline-loaderas a referenced
dependency.

In your config files, plugins can find additional entry files and also other
config files recursively.

## Bringing it all together

Sometimes a configuration file is a JavaScript or TypeScript file that imports
dependencies, but also contains configuration that needs to be parsed by a
plugin to find additional dependencies.

Let’s take a look at this example Vite configuration file:

```typescript
import{ defineConfig }from'vite';importreactfrom'@vitejs/plugin-react';exportdefaultdefineConfig(async({ mode,command })=>{return{plugins:[react()],test:{setupFiles:['./setup-tests.ts'],environment:'happy-dom',coverage:{provider:'c8',},},};});
```

This file importsviteand@vitejs/plugin-reactdirectly, but also
indirectly references thehappy-domand@vitest/coverage-c8packages.

The Vite plugin of Knip willdynamicallyload this configuration file and
parse the exported configuration. But it’s not aware of theviteand@vitejs/plugin-reactimports. This is why suchconfigfiles are also
automatically added asentryfiles for Knip tostaticallyresolve theimportandrequirestatements.

Additionally,./setup-tests.tswill be added as anentryfile.

When plugins dynamically load configuration files, conditional dependencies may
not be detected if the condition evaluates differently during analysis. Seeconditional or dynamic dependenciesfor details and workarounds.

## Command-Line Arguments

Plugins may define the arguments where Knip should look for entry files,
configuration files and dependencies. We’ve already seen some examples above:

```typescript
node--loadertsxscripts/deploy.tsplaywrighttest-cplaywright.web.config.ts
```

Please seescript parserfor more details.

## Summary

Plugins are configured with two distinct types of files:

- configfiles are dynamically loaded and parsed by the plugin
- entryfiles are added to the module graph
- Both can recursively lead to additional entry files, config files and
dependencies

ISC License© 2024Lars Kappert

