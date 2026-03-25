# Source: https://windicss.org/integrations/rollup

Title: Windi CSS

URL Source: https://windicss.org/integrations/rollup

Markdown Content:
Integration for [Rollup](https://rollupjs.org/)
-----------------------------------------------

[![Image 1](https://img.shields.io/badge/a-rollup--plugin--windicss-gray?logo=github&label=)](https://github.com/windicss/vite-plugin-windicss/tree/main/packages/rollup-plugin-windicss)[![Image 2](https://img.shields.io/npm/v/rollup-plugin-windicss?color=cb0200&label=%20&logo=npm)](https://www.npmjs.com/package/rollup-plugin-windicss)[![Image 3](https://img.shields.io/badge/a-%40antfu-48B0F1?label=)](https://github.com/antfu)

Installations
-------------

```
npm i rollup-plugin-windicss -D # yarn add rollup-plugin-windicss -D
```

rollup.config.js

```
import WindiCSS from 'rollup-plugin-windicss'

export default {
  plugins: [
    ...WindiCSS(),
  ],
}
```

```
// your code entry
import 'virtual:windi.css'
```

That's all.

Configuration
-------------

### Preflight (style resetting)

Preflight is enables on demanded, if you'd like to completely disable it, you can configure it as below

rollup.config.js

```
export default {
  plugins: [
    WindiCSS({
      preflight: false,
    }),
  ],
}
```

### Safelist

By default, we scan your source code statically and find all the usages of the utilities then generated corresponding CSS on-demand. However, there is some limitation that utilities that decided in the runtime can not be matched efficiently, for example

```
<!-- will not be detected -->
<div className={`p-${size}`}>
```

For that, you will need to specify the possible combinations in the `safelist` options of `vite.config.js`.

rollup.config.js

```
export default {
  plugins: [
    WindiCSS({
      safelist: 'p-1 p-2 p-3 p-4',
    }),
  ],
}
```

Or you can do it this way

```
function range(size, startAt = 1) {
  return Array.from(Array(size).keys()).map(i => i + startAt)
}

// rollup.config.js
export default {
  plugins: [
    WindiCSS({
      safelist: [
        range(30).map(i => `p-${i}`), // p-1 to p-3
        range(10).map(i => `mt-${i}`), // mt-1 to mt-10
      ],
    }),
  ],
}
```

### Scanning

On server start, `vite-plugin-windicss` will scan your source code and extract the utilities usages. By default, only files under `src/` with extensions `vue, html, mdx, pug, jsx, tsx` will be included. If you want to enable scanning for other file type of locations, you can configure it via:

rollup.config.js

```
export default {
  plugins: [
    WindiCSS({
      scan: {
        dirs: ['.'], // all files in the cwd
        fileExtensions: ['vue', 'js', 'ts'], // also enabled scanning for js/ts
      },
    }),
  ],
}
```

### More

See [options.ts](https://github.com/windicss/vite-plugin-windicss/blob/main/packages/plugin-utils/src/options.ts) for more configuration reference.
