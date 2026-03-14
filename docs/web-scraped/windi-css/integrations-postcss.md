# Source: https://windicss.org/integrations/postcss

Title: Windi CSS

URL Source: https://windicss.org/integrations/postcss

Markdown Content:
Integration for [PostCSS](https://postcss.org/)
-----------------------------------------------

[![Image 1](https://img.shields.io/badge/a-postcss--windicss-gray?logo=github&label=)](https://github.com/windicss/postcss-windicss)[![Image 2](https://img.shields.io/npm/v/postcss-windicss?color=cb0200&label=%20&logo=npm)](https://www.npmjs.com/package/postcss-windicss)[![Image 3](https://img.shields.io/badge/a-%40antfu-48B0F1?label=)](https://github.com/antfu)

> 🧪 Experimental.

> ⚠️ Using this package is **discouraged** as there are some limitations of PostCSS's API. Use our [first-class integrations](https://windicss.org/guide/installation) for each dedicated framework/build tool to get **the best develop experience and performance**. This plugin should be your last option to integrate Windi CSS.

Install
-------

Install `postcss-windicss` from NPM

```
npm i -D postcss-windicss
```

Create `postcss.config.js` under your project root

postcss.config.js

```
module.exports = {
  plugins: {
    'postcss-windicss': { /* ... */ },
  },
}
```

Add `@windicss` to your main css entry:

```
/* main.css */
@windicss;
```

Create `windi.config.js` / `windi.config.ts` under your project root with this configurations

windi.config.js

```
import { defineConfig } from 'windicss/helpers'

export default defineConfig({
  extract: {
    include: ['src/**/*.{html,vue,jsx,tsx,svelte}'],
  },
  /* ... */
})
```

And enjoy!
