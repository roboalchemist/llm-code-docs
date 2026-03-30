# Source: https://docs.skypack.dev/skypack-cdn/code/javascript.md

# JavaScript / TypeScript

## Hello, React!

Skypack will load code in any JavaScript environment, without any tooling or setup needed. To see it yourself, [open up the Skypack REPL](https://www.skypack.dev/npm/react) to run some JavaScript in your browser:

```javascript
// 👋 Welcome to Skypack! 

// Skypack is a Package Delivery Network (PDN) for everything on npm.
// Load any JavaScript package directly in the browser.

// Try loading the "react" package in the example below. 
// When you have something you like, copy the code onto your website!

import * as pkg from 'https://cdn.skypack.dev/react@^16.13.1';
console.log('react loaded:', pkg);
```

Open up your browser's dev console, and you should see `"react loaded: Module {...}"` (or something similar) printed to the console. Feel free to inspect the module object in your console log, if it's supported.

You can play around with this example as much as you like, replacing the `/react` in the URL with whatever package name you'd like.

## Getting Started

In this example, we'll start by using Preact and a helpful templating library called HTM. These two libraries were built to run directly in the browser, so they'll let us get pretty far without more complex tooling.

To run through these examples locally, you'll need a local dev server to serve files to the browser. We recommend [servor](https://github.com/lukejacksonn/servor) for it's light footprint and ability to run in any directory without an install step via `npx servor`.

### Step 1: A Single HTML File

```markup
<!-- Example 1: Preact in HTML (no build tooling required!) -->
<!-- View Code: https://glitch.com/edit/#!/familiar-warm-monday -->
<!DOCTYPE html>
<html>
  <body>
    <script type="module">
      import { h, Component, render } from 'https://cdn.skypack.dev/preact';
      import htm from 'https://cdn.skypack.dev/htm';
      const html = htm.bind(h);

      const app = html`<h1>Hello World!</h1>`;
      render(app, document.body);
    </script>
  </body>
</html>
```

### Step 2: Separating the JavaScript

A single HTML file may be all you need, but complex sites and applications will usually pull their JavaScript files out of HTML and into their own file tree:

{% tabs %}
{% tab title="index.html" %}

```markup
<!-- Example 2: Preact in JS (still... no build tooling required!) -->
<!DOCTYPE html>
<html>
  <body>
    <script type="module" src="/src/index.js"></script>
  </body>
</html>
```

{% endtab %}

{% tab title="src/index.js" %}

```javascript
import { h, Component, render } from 'https://cdn.skypack.dev/preact';
import htm from 'https://cdn.skypack.dev/htm';
const html = htm.bind(h);

const app = html`<h1>Hello World!</h1>`;
render(app, document.body);
```

{% endtab %}
{% endtabs %}

### Step 3: Adding More Files, Dependencies

From there, you can keep expanding your application. Start using new libraries and create more and more files in your application.

```
TODO: Example with multiple files, some preact component library.
```

### Step 4: Moving to Snowpack for TypeScript, Babel, Sass, etc.

At a certain point, you will probably run into limitations with your static dev server:

* No React support (JSX)
* No build tool support (Babel, Sass, etc.)
* No TypeScript support
* No production optimization support

For application development of any size, we recommend using Snowpack as your ESM-powered dev environment & build tool. It supports TypeScript, JSX, React, and more out of the box. You can learn more about it here: <https://www.snowpack.dev/>

## Using Skypack URLs in TypeScript

To use Skypack URLs directly, first create a `types/skypack.d.ts` file in the root of your project:

```typescript
// First, let TypeScript allow all module names starting with "https://". This will suppress TS errors.
declare module 'https://*';

// Second, list out all your dependencies. For every URL, you must map it to its local module.
declare module 'https://cdn.skypack.dev/preact' {
  export * from 'preact';
}

declare module 'https://cdn.skypack.dev/preact-router' {
  export * from 'preact-router';
}
```

{% hint style="info" %}
**Note**: you must have types installed locally for all your packages for this to work. Even though you’ll be using Skypack URLs in the end, TypeScript still needs to read these types from your local machine, so you’ll have to `npm install` them just like you would have before.
{% endhint %}

Lastly, add the `types/` folder to your `tsconfig.json` “includes” like so:

```diff
  {
    "compilerOptions": { … },
    "include": [
      "src",
+     "types"
    ],
    "exclude": ["node_modules"]
  }
```

Now you can use Skypack URLs directly in your projects, and have full TypeScript typings:

```diff
- import preact from 'preact';
+ import preact from 'https://cdn.skypack.dev/preact';
```

### Using Pinned URLs

You may want to just go ahead and use [Pinned URLs](https://docs.skypack.dev/skypack-cdn/api-reference/pinned-urls-optimized) directly in your app. You can do this by simply adding them to `types/skypack.d.ts` the same you would a basic lookup URL. In fact, you can have both in there side-by-side without any problem. Once you have them set up as aliases, TypeScript will treat them as such.
