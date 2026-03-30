# Source: https://docs.skypack.dev/skypack-cdn/code/optimize-for-production.md

# Optimize for Production

## Pinned URLs

{% hint style="info" %}
**Pinned URLs are generated for you automatically by a successful lookup.** \
You should never need to write one yourself.&#x20;
{% endhint %}

```
https://cdn.pika.dev/pin/react@16.13.1-HASH/react.pin.js
```

While Lookup URLs are the easiest way to use Skypack, they aren't the fastest. When you're ready for production-optimized speed and safety, use **Pinned URLs.**

### Pinned URL vs. Lookup URL

Lookup URLs and Pinned URLs are both valid methods to load a package from Skypack. Lookup URLs are great for development, but Pinned URLs are faster and better suited for production use.

Lookup URLs are the recommended way to load a package during development:

* **Human Writeable -** You can write a Lookup URL yourself.
* **Version Resolution -** Lookup URLs resolve by version, SemVer, dist-tag, etc.
* **New Packages -** Lookup URLs will build new packages if none exists.

Pinned URLs, however, have several benefits over Lookup URLs:

* **Faster -** Runs on the edge, and responds in just a few milliseconds.
* **Pinned to a specific version -** Won't change over time (including sub-dependencies).

**If you can, replace all Lookup URLs with Pinned URLs in your codebase.** When new package versions are published to npm, Lookup URLs will automatically point to those new versions. Pinned URLs, by contrast, include a `HASH` in the URL that is always locked to a single version of your package ***and***  all package-dependencies. No matter what changes on npm, Pinned URL will always point to the exact same code.

### How to Get a Pinned URL

Pinned URLs are returned in the response of a successful Lookup URL. You should never need to write one yourself.

There are a few ways to get one:

* **Manual:** Via the package lookup tool on [www.skypack.dev\&#x20](http://www.skypack.dev\&#x20);
* **Manual:** Via the body of a successful Lookup URL.
* **Automatic:** Via tooling like Snowpack or a Skypack bundler plugin (see below).

## Content Security Policy (CSP)

When deploying your site with Skypack, be sure to inspect your site’s [Content Security Policy (CSP) headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP). You’ll want to make sure `script-src cdn.skypack.dev` is part of your site’s CSP.

## Build tools

Build tools for Skypack are coming soon! In the meantime, check out these community resources:

### Community tools

* **Rollup:** [rollup-plugin-skypack-resolver](https://www.npmjs.com/package/@vinicius73/rollup-plugin-skypack-resolver)
