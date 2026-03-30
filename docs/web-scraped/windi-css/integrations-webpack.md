# Source: https://windicss.org/integrations/webpack

Title: Windi CSS

URL Source: https://windicss.org/integrations/webpack

Markdown Content:
Integration for [webpack](https://webpack.js.org/)
--------------------------------------------------

[![Image 1](https://img.shields.io/badge/a-windicss--webpack--plugin-gray?logo=github&label=)](https://github.com/windicss/windicss-webpack-plugin)[![Image 2](https://img.shields.io/npm/v/windicss-webpack-plugin?color=cb0200&label=%20&logo=npm)](https://www.npmjs.com/package/windicss-webpack-plugin)[![Image 3](https://img.shields.io/badge/a-%40harlan--zw-48B0F1?label=)](https://github.com/harlan-zw)

Choosing the right plugin
-------------------------

Windi CSS Webpack Plugin is a language and framework agnostic way to implement Windi CSS in webpack apps.

### First Class Framework Support

If it's below, please use the plugin specifically built for your framework.

| Framework |  |
| --- | --- |
| Nuxt.js | [nuxt-windicss](https://windicss.org/integrations/nuxt) |
| Svelte | [svelte-windicss-preprocess](https://windicss.org/integrations/svelte) |
| Vue CLI | [vue-cli-plugin-windicss](https://windicss.org/integrations/vue-cli) |
| Gridsome | [gridsome-plugin-windicss](https://windicss.org/integrations/gridsome) |

### Second Class Framework Support

Frameworks that have been successfully setup and documented to work with Windi.

| Framework |  |
| --- | --- |
| Next.js | [Install](https://windicss.org/integrations/webpack#next-js) - [Example](https://github.com/windicss/windicss-webpack-plugin/blob/master/example/next/) |
| CRACO | [Install](https://windicss.org/integrations/webpack#create-react-app-craco) - [Example](https://github.com/windicss/windicss-webpack-plugin/blob/master/example/craco/) |
| Storybook | [Install](https://windicss.org/integrations/webpack#storybook) - [Example](https://github.com/windicss/windicss-webpack-plugin/tree/master/example/vue3-storybook) |
| Umi.js | [Example](https://github.com/windicss/windicss-webpack-plugin/tree/master/example/umijs) |

### Non Supported Frameworks

Frameworks which have been tested with this package and did not work.

*   ❌ Angular

Install
-------

If you are proceeding setup with a custom webpack build, then please report any issues you find.

```
yarn add windicss-webpack-plugin -D
# npm i windicss-webpack-plugin -D
```

If you were previously using Tailwind, please see the [migration guide](https://windicss.org/guide/migration).

### Configure webpack

You will need to add the plugin to your webpack configuration. If you have access to modify the `webpack.config.js` directly, then you can do the following.

webpack.config.js

```
import WindiCSSWebpackPlugin from 'windicss-webpack-plugin'

export default {
  // ...
  plugins: [
    new WindiCSSWebpackPlugin(),
  ],
}
```

#### Non ES Modules Install

For webpack configurations which don't support the es module import syntax, you can try the following.

webpack.config.js

```
const WindiCSSWebpackPlugin = require('windicss-webpack-plugin')

export default {
  // ...
  plugins: [
    new WindiCSSWebpackPlugin(),
  ],
}
```

### Include the virtual module

Within an entry point file or something only loaded once, add the import.

ESM

main.js

```
import 'windi.css'
```

CJS

main.js

```
require('windi.css')
```

### Windi Config

Add a file called `windi.config.ts` to your project root if you don't have it already.

#### Scanning

If you have issues when you start Windi that your classes aren't being picked up, you may need to modify the scanning.

On server start, Windi will scan your code and extract the utility usages. By default, only files under `src/` with extensions `"html", "vue", "md", "mdx", "pug", "jsx", "tsx", "svelte", "ts", "js", "css", "postcss"` will be included.

windi.config.ts

```
import { defineConfig } from 'windicss/helpers'

export default defineConfig({
  extract: {
    // A common use case is scanning files from the root directory
    include: ['**/*.{vue,html,jsx,tsx}'],
    // if you are excluding files, make sure you always include node_modules and .git
    exclude: ['node_modules', '.git', 'dist'],
  },
})
```

Configuration
-------------

### Preflight (style resetting)

Preflight is enabled on-demanded. If you'd like to completely disable it, you can configure it as below

windi.config.ts

```
import { defineConfig } from 'windicss/helpers'

export default defineConfig({
  preflight: false,
})
```

### Safelist

By default, we scan your source code statically and find all the usages of the utilities then generated corresponding CSS on-demand. However, there is some limitation that utilities that decided in the runtime can not be matched efficiently, for example

```
<!-- will not be detected -->
<div className={`p-${size}`}>
```

For that, you will need to specify the possible combinations in the `safelist` options of `windi.config.ts`.

windi.config.ts

```
import { defineConfig } from 'windicss/helpers'

export default defineConfig({
  safelist: 'p-1 p-2 p-3 p-4',
})
```

Or you can do it this way

windi.config.ts

```
import { defineConfig } from 'windicss/helpers'

function range(size, startAt = 1) {
  return Array.from(Array(size).keys()).map(i => i + startAt)
}

export default defineConfig({
  safelist: [
    range(30).map(i => `p-${i}`), // p-1 to p-3
    range(10).map(i => `mt-${i}`), // mt-1 to mt-10
  ],
})
```

### Layers Ordering

By default, importing `windi.css` or `virtual:windi.css` will import all the three layers with the order `base - components - utilities`. If you want to have better controls over the orders, you can separate them by:

```
- import 'virtual:windi.css'
+ import 'virtual:windi-base.css'
+ import 'virtual:windi-components.css'
+ import 'virtual:windi-utilities.css'
```

You can also make your custom CSS be able to be overridden by certain layers:

```
import 'virtual:windi-base.css'
  import 'virtual:windi-components.css'
+ import './my-style.css'
  import 'virtual:windi-utilities.css'
```

### Full Configuration

See [options.ts](https://github.com/windicss/vite-plugin-windicss/blob/main/packages/plugin-utils/src/options.ts) for full configuration details.

Install Examples
----------------

### Next.js

next.config.js

```
const WindiCSSWebpackPlugin = require('windicss-webpack-plugin')

module.exports = {
  // ...
  webpack(config) {
    config.plugins.push(new WindiCSSWebpackPlugin())
    return config
  },
}
```

pages/_app.js

```
import 'windi.css'
```

windi.config.js

```
import { defineConfig } from 'windicss/helpers'

export default defineConfig({
  extract: {
    include: ['**/*.{jsx,tsx,css}'],
    exclude: ['node_modules', '.git', '.next'],
  },
})
```

Note: JSX usage is experimental. Please report any issues you find.

### Create React App - CRACO

craco.config.js

```
const WindiCSSWebpackPlugin = require('windicss-webpack-plugin')

module.exports = {
  // ...
  webpack: {
    plugins: {
      add: [
        new WindiCSSWebpackPlugin({
          virtualModulePath: 'src',
        }),
      ],
    },
  },
}
```

src/index.js

```
import './windi.css'
```

windi.config.ts

```
import { defineConfig } from 'windicss/helpers'

export default defineConfig({
  extract: {
    include: ['**/*.{jsx,js,css,html}'],
    exclude: ['node_modules', '.git', '.next'],
  },
})
```

Note: JSX usage is experimental. Please report any issues you find.

### Non ES Modules

For webpack configurations which don't support the es module import syntax, you can try the following.

webpack.config.js

```
const WindiCSSWebpackPlugin = require('windicss-webpack-plugin')

export default {
  // ...
  plugins: [
    new WindiCSSWebpackPlugin(),
  ],
}
```

```
// main.js
require('windi.css')
```

### Storybook

.storybook/main.js

```
const WindiCSSWebpackPlugin = require('windicss-webpack-plugin')

module.exports = {
  // ...
  webpackFinal: (config) => {
    config.plugins.push(new WindiCSSWebpackPlugin())
    return config
  },
}
```

.storybook/preview.js

```
import 'windi.css'
```

Warning: CSS pre-processors (like SCSS, LESS) will not work with `@apply`, use plain css.

### Code Examples

See [examples](https://github.com/windicss/windicss-webpack-plugin/tree/master/example) for sample projects.
