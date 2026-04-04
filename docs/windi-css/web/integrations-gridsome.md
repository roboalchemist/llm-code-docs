# Source: https://windicss.org/integrations/gridsome

Title: Windi CSS

URL Source: https://windicss.org/integrations/gridsome

Markdown Content:
Integration for [Gridsome](https://gridsome.org/)
-------------------------------------------------

[![Image 1](https://img.shields.io/badge/a-gridsome--plugin--windicss-gray?logo=github&label=)](https://github.com/windicss/gridsome-plugin-windicss)[![Image 2](https://img.shields.io/npm/v/gridsome-plugin-windicss?color=cb0200&label=%20&logo=npm)](https://www.npmjs.com/package/gridsome-plugin-windicss)[![Image 3](https://img.shields.io/badge/a-%40harlan--zw-48B0F1?label=)](https://github.com/harlan-zw)

Install
-------

```
yarn add gridsome-plugin-windicss -D
# npm i gridsome-plugin-windicss -D
```

⚠️ This module is a pre-release, please report any [issues](https://github.com/windicss/gridsome-plugin-windicss/issues) you find.

Usage
-----

Within your `gridsome.config.js` add the following.

gridsome.config.js

```
export default {
  // ...
  plugins: [
    {
      use: 'gridsome-plugin-windicss',
      options: {
        // see https://github.com/windicss/vite-plugin-windicss/blob/main/packages/plugin-utils/src/options.ts
      },
    },
  ],
}
```

This module won't work with `gridsome-plugin-tailwindcss`, you will need to remove it.

```
plugins: [
    {
-      use: 'gridsome-plugin-tailwindcss',
-      options: {
-        // ...
-      }
    },
  ],
```

If you have a `tailwind.config.js`, please rename it to `windi.config.js` or `windi.config.ts`.

See [here](https://windicss.netlify.app/guide/configuration) for configuration details.

Migrating
---------

If you were previously using `gridsome-plugin-tailwindcss`, please consult the [documentation](https://windicss.netlify.app/guide/migration) on migrating.

Configuration
-------------

*   Default:

```
export default {
  scan: {
    dirs: ['./'],
    exclude: [
      'node_modules',
      '.git',
      'dist',
      '.cache',
      '*.template.html',
      'app.html',
    ],
    include: [],
  },
  transformCSS: 'pre',
  preflight: {
    alias: {
      // add gridsome aliases
      'g-link': 'a',
      'g-image': 'img',
    },
  },
}
```

*   See [options.ts](https://github.com/windicss/vite-plugin-windicss/blob/main/packages/plugin-utils/src/options.ts) for configuration reference.

### Examples

#### Disable Preflight

_gridsome.config.js_

```
export default {
  // ...
  plugins: [
    {
      use: 'gridsome-plugin-windicss',
      options: {
        preflight: false,
      },
    },
  ],
}
```

Caveats
-------

### Scoped Style

`@media` directive with scoped style can **only work** with `css``postcss``scss` but not `sass`, `less` nor `stylus`
