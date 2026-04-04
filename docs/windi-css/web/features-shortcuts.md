# Source: https://windicss.org/features/shortcuts

Title: Windi CSS

URL Source: https://windicss.org/features/shortcuts

Markdown Content:
Shortcuts | Windi CSS
===============

[![Image 1: Logo](https://windicss.org/assets/logo.svg) Windi CSS](https://windicss.org/)

Search K

Overview 

Utilities 

Plugins 

Posts 

Community 

[Play](https://windicss.org/play)

[](https://github.com/windicss/windicss)

[](https://github.com/windicss/windicss)

 Overview

 Utilities

 Plugins

 Posts

 Community

[Play](https://windicss.org/play)

*   ##### Guide

    *   [Getting Started](https://windicss.org/guide/)
    *   [Installation](https://windicss.org/guide/installation)
    *   [Configuration](https://windicss.org/guide/configuration)
    *   [Extractions](https://windicss.org/guide/extractions)
    *   [Migration from Tailwind](https://windicss.org/guide/migration)

*   ##### Features

    *   [Overview](https://windicss.org/features/)
    *   [Value Auto-infer](https://windicss.org/features/value-auto-infer)
    *   [Variant Groups](https://windicss.org/features/variant-groups)
    *   [Shortcuts](https://windicss.org/features/shortcuts)
    *   [Responsive Design](https://windicss.org/features/responsive-design)
    *   [Dark Mode](https://windicss.org/features/dark-mode)
    *   [RTL](https://windicss.org/features/rtl)
    *   [Important Prefix](https://windicss.org/features/important-prefix)
    *   [Directives](https://windicss.org/features/directives)
    *   [Attributify Mode](https://windicss.org/features/attributify)
    *   [Visual Analyzer](https://windicss.org/features/analyzer)

*   ##### Integrations

    *   [Vite](https://windicss.org/integrations/vite)
    *   [Webpack](https://windicss.org/integrations/webpack)
    *   [Rollup](https://windicss.org/integrations/rollup)
    *   [Nuxt](https://windicss.org/integrations/nuxt)
    *   [Vue CLI](https://windicss.org/integrations/vue-cli)
    *   [Gridsome](https://windicss.org/integrations/gridsome)
    *   [Svelte](https://windicss.org/integrations/svelte)
    *   [PostCSS](https://windicss.org/integrations/postcss)
    *   [CLI](https://windicss.org/integrations/cli)
    *   [JavaScript API](https://windicss.org/integrations/javascript)
    *   [VS Code](https://windicss.org/editors/vscode)
    *   [WebStorm](https://windicss.org/editors/webstorm)

Shortcuts [#](https://windicss.org/features/shortcuts#shortcuts)
================================================================

It's quite common to get repetitive when you work on similar utility sets. We provide this "shortcuts" feature allowing you to give the combinations of utility names which you can reuse everywhere inside your app without needing to repeat yourself.

Simply add the `shortcuts` field to your configuration:

windi.config.js

```js
export default {
  theme: {
    /* ... */
  },
  shortcuts: {
    'btn': 'py-2 px-4 font-semibold rounded-lg shadow-md',
    'btn-green': 'text-white bg-green-500 hover:bg-green-700',
  },
}
```

xxxxxxxxxx

btn btn-green

Config

xxxxxxxxxx

{ shortcuts: { btn: 'py-2 px-4 font-semibold rounded-lg shadow-md', 'btn-green': 'text-white bg-green-500 hover:bg-green-700', },}

CSS

.btn {
  border-radius: 0.5rem;
  font-weight: 600;
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
  padding-left: 1rem;
  padding-right: 1rem;
  --tw-shadow: 0 4px 6px -1px rgb(0 0 0/0.1),0 2px 4px -2px rgb(0 0 0/0.1);
  --tw-shadow-colored: 0 4px 6px -1px var(--tw-shadow-color),0 2px 4px -2px var(--tw-shadow-color);
  -webkit-box-shadow: var(--tw-ring-offset-shadow,0 0 #0000),var(--tw-ring-shadow,0 0 #0000),var(--tw-shadow);
  box-shadow: var(--tw-ring-offset-shadow,0 0 #0000),var(--tw-ring-shadow,0 0 #0000),var(--tw-shadow);
}
.btn-green {
  --tw-bg-opacity: 1;
  background-color: rgba(16, 185, 129, var(--tw-bg-opacity));
  --tw-text-opacity: 1;
  color: rgba(255, 255, 255, var(--tw-text-opacity));
}
.btn-green:hover {
  --tw-bg-opacity: 1;
  background-color: rgba(4, 120, 87, var(--tw-bg-opacity));
}

CSS-in-JS syntax is also supported for complex utilities:

windi.config.js

```js
export default {
  theme: {
    /* ... */
  },
  shortcuts: {
    'btn': {
      'color': 'white',
      '@apply': 'py-2 px-4 font-semibold rounded-lg',
      '&:hover': {
        '@apply': 'bg-green-700',
        'color': 'black',
      },
    },
    'btn-green': 'text-white bg-green-500 hover:bg-green-700',
  },
}
```

​x

btn btn-green

Config

xxxxxxxxxx

{ shortcuts: { btn: { color: 'white', '@apply': 'py-2 px-4 font-semibold rounded-lg', '&:hover': { '@apply': 'bg-green-700', color: 'black', }, }, 'btn-green': 'text-white bg-green-500 hover:bg-green-700', },}

CSS

.btn {
  color: white;
  border-radius: 0.5rem;
  font-weight: 600;
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
  padding-left: 1rem;
  padding-right: 1rem;
}
.btn:hover {
  --tw-bg-opacity: 1;
  background-color: rgba(4, 120, 87, var(--tw-bg-opacity));
  color: black;
}
.btn-green {
  --tw-bg-opacity: 1;
  background-color: rgba(16, 185, 129, var(--tw-bg-opacity));
  --tw-text-opacity: 1;
  color: rgba(255, 255, 255, var(--tw-text-opacity));
}
.btn-green:hover {
  --tw-bg-opacity: 1;
  background-color: rgba(4, 120, 87, var(--tw-bg-opacity));
}

The utility added by this configuration can also be directly wrapped in variants, such as sm:btn. The purpose of this feature is similar to the `@apply` directive, it will merge all utilities into one style.

[Suggest changes to this page](https://github.com/windicss/docs/edit/main/features/shortcuts.md)

[Variant Groups](https://windicss.org/features/variant-groups)

[Responsive Design](https://windicss.org/features/responsive-design)

[Windi CSS is Sunsetting We recommend new projects to consider alternatives. Click for more information.](https://windicss.org/posts/sunsetting)
