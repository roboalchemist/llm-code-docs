# Source: https://docs.skypack.dev/package-authors/package-checks.md

# Package Quality Score

Skypack features a section on each package page called the Package Quality Score. This section features a list of checks on a package manifest that give insight into the quality of any given package. The goal of this is to **increase package quality and help package authors create a better JS ecosystem** (similar to [GitHub’s community checklist](https://docs.github.com/en/free-pro-team@latest/github/building-a-strong-community/about-community-profiles-for-public-repositories)).

**Didn't score a 100 on your package? That's okay!**\
Think of Package Quality like a [Lighthouse](https://developers.google.com/web/tools/lighthouse) score. Achieving 100 out of 100 points is meant to be difficult, and require perfect configuration and distribution. Skypack's Quality Score is a lot like that, where a 100 represents the "perfect" package where nothing could be improved as far as how the package is configured and distributed. We have a high bar to hit on purpose!&#x20;

Below you’ll find documentation on each individual check: what they mean and how to pass each check in your own package. **We recommend passing all checks!** Every check is significant and will improve package quality, package discovery, developer experience and the final deployment size for all of your users.

## Check your score before publishing

{% hint style="success" %}
[**@skypack/package-check**](https://github.com/skypackjs/package-check) **is now available as an npm package!**

* Check your package quality score locally before publishing to npm.&#x20;
* Integrate the CLI into your test suite to find and fix future regressions.
* Get it today → <https://github.com/skypackjs/package-check>
  {% endhint %}

## ESM

ESM stands for *ES Modules* a.k.a [JavaScript modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules), which is the new standard for JavaScript modules. This check ensures that at least one of the following conditions are met:

* **Recommended:** Your `package.json` contains an ESM export, e.g.:`"exports": { "import": "./path/to/entry.js" }` or `"exports": { ".": { "import": "…" } }` ([docs](https://nodejs.org/api/packages.html#packages_approach_1_use_an_es_module_wrapper))
* Your `package.json` contains `"type": "module"` ([docs](https://nodejs.org/api/packages.html#packages_type))
* Your `package.json` contains a `"module": "./path/to/entry.js"` entry (not officially supported by Node.js, but [an organic community convention](https://github.com/rollup/rollup/wiki/pkg.module) we respect).
* *Supported, but not recommended:* Your `package.json` contains a `"main"` field that ends in `.mjs` ([this mimics Node behavior](https://nodejs.org/api/packages.html#packages_determining_module_system)). We’d recommend adding `"exports.import"` as well if this is your only indicator.

#### Why?

This field ensures that you’re shipping modern, standards-compliant JavaScript that works best for users. This ensures your package has more longevity and can be used in more environments, from browsers to Node to newer projects like [Deno](https://deno.land/). Even traditional web bundlers can benefit from ESM for more accurate tree-shaking and code analysis.

*Tip: by using the `"exports": …` approach, you can knock out the* [*Export Map check*](#has-export-map) *below as well!*

#### How to Fix

You can pass this check by meeting any one of the conditions above. Below is our recommended configuration for a package to support ESM using the "module" method for compatibility with older bundlers and an Export Map for compatibility with Node.js v12+ and future bundlers. ([docs](https://nodejs.org/api/packages.html#packages_approach_1_use_an_es_module_wrapper))

```javascript
// recommended: web-only package.json
{
  "module": "./esm/index.js",
  "exports": {
    ".": "./esm/index.js"
  }
}
```

```javascript
// recommended: web + node.js package.json
{
  "main": "./index-cjs.js",
  "module": "./index-esm.js",
  "exports": {
    "require": "./index-cjs.js",
    "import": "./index-esm.js"
  }
}
```

## Export Map

This check ensures that your package.json contains an `"exports"` top-level field ([docs](https://nodejs.org/api/packages.html#packages_subpath_exports)).

#### Why?

Export Maps help package authors accomplish two things: transition from Common.js (CJS)  to ESM & make a package's internal files private.

Historically, it has been impossible for some packages to reliably support multiple module systems (UMD, CJS, ESM) ***and*** multiple environments (Web, Node.js, Deno). Past efforts to standardize have relied solely on community buy-in, with little official support from Node.js or npm. Export Maps aim to solve this problem as the official Node.js standard to define package entrypoints per-environment.

```javascript
{
  "exports": {
    "require": "./index-cjs.js",
    "import": "./index-esm.js",
    "default": "./index-esm.js",
    // "node", "browser", "deno", etc. (env-specific entrypoints, as needed)
  }
}
```

Export maps also solve the problem of unexpected file access within a package. Packages can make up thousands of files, and it's not clear which files are meant to be imported directly or not. When you specify an export map, Node.js v12+ (and other tools) will prevent access to any files not listed in that export map. This makes your package file layout explicit, and locks down private, internal files that may move across non-breaking versions.

Take, for example, the [preact package](http://skypack.dev/view/preact) and how they use export maps:

```javascript
{
  "exports": {
    ".": {
      "import": "./dist/preact.mjs"
    },
    "./hooks": {
      "import": "./hooks/dist/hooks.mjs"
    }
    // ...
  }
}
```

This allows users to import from either `import preact from 'preact'` or `import { useState } from 'preact/hooks'` but not `from 'preact/super-secret-internal-file';`. This helps to protect users from accidental breaking changes, while allowing bundlers and CDNs like Skypack to better optimize package code around these explicit entrypoints.

#### How to Fix

Add something like one of the following to your `package.json`: ([docs](https://nodejs.org/api/packages.html#packages_approach_1_use_an_es_module_wrapper))

```javascript
{
  "exports": {
    ".": {
      "require": "./index-cjs.js",
      "import": "./index-esm.js",
    },
    // add more entrypoints here, only if needed
  }
}
```

## Keywords

This check ensures that your `package.json` contains a `"keywords"` top-level field ([docs](https://docs.npmjs.com/files/package.json#keywords)).

#### Why?

Popular npm search engines like npmjs.org, npms.io, yarnpkg.com, and more will only match your search term against the `name`, `description`, and `keywords`fields of each package. Adding a `keywords` field is a simple way to make sure that you are reaching as many users as possible, without relying on an exact match on the package name or description.

#### How to Fix

Add something like the following to your `package.json`: ([docs](https://docs.npmjs.com/files/package.json#keywords))

```javascript
{
  "keywords": [
    "ui",
    "svelte",
    "svelte-component"
  ]
}
```

## License

This check ensures that your `package.json` contains a `"license"` top-level field ([docs](https://docs.npmjs.com/files/package.json#license)).

#### Why?

Open-source software needs a license to use! Without a license, your package can’t be meaningfully used by companies or individuals. Even if you already have a license file included in your package files, many tools are unable to detect this automatically.

#### How to Fix

Add something like the following to your `package.json`: ([docs](https://docs.npmjs.com/files/package.json#license))

```javascript
{
  "license": "MIT"
}
```

## README

This check ensures you shipped a `README.md` file in the root directory along with your code ([docs](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/about-readmes)).

#### Why?

Open source packages need documentation! Help your users understand how to use your library by adding a README.

#### How to Fix

Simply add a `README.md` file in the root of your project. If you’re new to READMEs in general, [please see GitHub’s guide](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/about-readmes).

## Types

This check ensures that your `package.json` contains a `"types"` or `"typings"` top-level field, pointing to TypeScript types for your package ([docs](https://www.typescriptlang.org/docs/handbook/declaration-files/publishing.html#including-declarations-in-your-npm-package)).

*Note: having an  `index.d.ts` in the root of your project isn’t enough; `types` must be present in `package.json`* [*as recommended in the TypeScript documentation*](https://www.typescriptlang.org/docs/handbook/declaration-files/publishing.html#including-declarations-in-your-npm-package)*.*

#### Why?

In the State of JS 2019 survey, over half of all JavaScript developers said that they had worked with TypeScript. Even if you don’t use TypeScript yourself, authoring declaration files will make your package easier to use for a significant portion of your user-base.&#x20;

If you're looking for help to get started,  you can ask open source contributors to help!

#### How to Fix

Add something like the following to your `package.json`: ([docs](https://www.typescriptlang.org/docs/handbook/declaration-files/publishing.html#including-declarations-in-your-npm-package))

```javascript
{
  "types": "./index.d.ts"
}
```

To generate your `.d.ts` types file(s), check out the following helpful resources:

* [Generate from TypeScript code](https://medium.com/cameron-nokes/the-30-second-guide-to-publishing-a-typescript-package-to-npm-89d93ff7bccd) (automatic)
* [Generate from JavaScript code](https://humanwhocodes.com/snippets/2020/10/create-typescript-declarations-from-javascript-jsdoc/) (automatic, with JSDoc)
* [Author manually](https://www.typescriptlang.org/docs/handbook/declaration-files/by-example.html)

## Repository

This check ensures that your `package.json` contains a `"repository"` top-level field ([docs](https://docs.npmjs.com/files/package.json#repository)).

#### Why?

A good open source package’s source code can be inspected to better examine its contents. It’s also important to see contributors’ additions to the codebase.

#### How to Fix

Add something like the following to your `package.json`: ([docs](https://docs.npmjs.com/files/package.json#repository))

```javascript
{
  "repository": {
    "type": "git",
    "url": "https://github.com/[username]/[project]"
  }
}
```
