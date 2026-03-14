# Source: https://windicss.org/integrations/vue-cli

Title: Windi CSS

URL Source: https://windicss.org/integrations/vue-cli

Markdown Content:
Integration for [Vue CLI](https://cli.vuejs.org/)
-------------------------------------------------

[![Image 1](https://img.shields.io/badge/a-vue--cli--plugin--windicss-gray?logo=github&label=)](https://github.com/windicss/vue-cli-plugin-windicss)[![Image 2](https://img.shields.io/npm/v/vue-cli-plugin-windicss?color=cb0200&label=%20&logo=npm)](https://www.npmjs.com/package/vue-cli-plugin-windicss)[![Image 3](https://img.shields.io/badge/a-%40harlan--zw-48B0F1?label=)](https://github.com/harlan-zw)

Features
--------

*   ⚡️ **It's FAST** - 20~100x times faster than [vue-cli-plugin-tailwind](https://github.com/forsartis/vue-cli-plugin-tailwind)
*   🧩 On-demand CSS utilities (Compatible with Tailwind CSS v2) and native elements style resetting
*   🍃 Load configurations from `tailwind.config.js`
*   📄 CSS `@apply` / `@screen` directives transforms
*   🎳 Support Utility Groups - e.g. `bg-gray-200 hover:(bg-gray-100 text-red-300)`

Install
-------

Install using Vue CLI. (Vue CLI 4+ is recommended)

```
vue add windicss
```

⚠️ This module is a pre-release, please report any [issues](https://github.com/windicss/vue-cli-plugin-windicss/issues) you find.

Then, add the configuartion

vue.config.js

```
module.exports = {
  pluginOptions: {
    windicss: {
      // see https://github.com/windicss/vite-plugin-windicss/blob/main/packages/plugin-utils/src/options.ts
    },
  },
}
```

And finally, import `windi.css` in your entry

main.js

```
import 'windi.css'
```

That's it! Starting using [classes utilities](https://windicss.org/utilities/) or [CSS directives](https://windicss.org/features/directives) in your app, and enjoy the speed! ⚡️

Migrating
---------

If you were previously using `vue-cli-plugin-tailwind`, please consult the [documentation](https://windicss.netlify.app/guide/migration) on migrating.

```
yarn remove vue-cli-plugin-tailwind
```

Options
-------

*   Default:

```
export default {
  scan: {
    dirs: ['src'],
    exclude: [
      'node_modules',
      '.git',
      'public/**/*',
      '*.template.html',
      'index.html',
    ],
    include: [],
  },
  transformCSS: 'pre',
}
```

*   See [options.ts](https://github.com/windicss/vite-plugin-windicss/blob/main/packages/plugin-utils/src/options.ts) for configuration reference.

### Examples

#### Disable Preflight

_vue.config.js_

```
module.exports = {
  // ...
  pluginOptions: {
    windicss: {
      preflight: false,
    },
  },
}
```

Caveats
-------

### Scoped Style

`@media` directive with scoped style can **only work** with `css``postcss``scss` but not `sass`, `less` nor `stylus`
