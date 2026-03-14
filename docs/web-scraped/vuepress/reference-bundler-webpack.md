# Source: https://vuepress.vuejs.org/reference/bundler/webpack

Title: Webpack

URL Source: https://vuepress.vuejs.org/reference/bundler/webpack

Markdown Content:
[![Image 1: @vuepress/bundler-webpack](https://badgen.net/npm/v/@vuepress/bundler-webpack/next?label=%40vuepress%2Fbundler-webpack%40next)](https://www.npmjs.com/package/@vuepress/bundler-webpack "@vuepress/bundler-webpack")

Webpack bundler is provided by [@vuepress/bundler-webpack](https://www.npmjs.com/package/@vuepress/bundler-webpack) package.

[Usage](https://vuepress.vuejs.org/reference/bundler/webpack#usage)
-------------------------------------------------------------------

Install the bundler package:

`npm i -D @vuepress/bundler-webpack@next`

Specify the bundler option in your config file:

.vuepress/config.ts

```
import { webpackBundler } from '@vuepress/bundler-webpack'
import { defineUserConfig } from 'vuepress'

export default defineUserConfig({
  bundler: webpackBundler({
    postcss: {},
    vue: {},
  }),
})
```

[Options](https://vuepress.vuejs.org/reference/bundler/webpack#options)
-----------------------------------------------------------------------

### [configureWebpack](https://vuepress.vuejs.org/reference/bundler/webpack#configurewebpack)

*   Type: `(config: WebpackConfiguration, isServer: boolean, isBuild: boolean) => WebpackConfiguration | void`

*   Details:

Edit the internal webpack config.

This option accepts a function that will receive a webpack config object as the 1st argument, an `isServer` flag as the 2nd argument and an `isBuild` flag as the 3rd argument. You can either mutate the config directly, or return an object to be merged by [webpack-merge](https://github.com/survivejs/webpack-merge).

### [chainWebpack](https://vuepress.vuejs.org/reference/bundler/webpack#chainwebpack)

*   Type: `(config: WebpackChainConfig, isServer: boolean, isBuild: boolean) => void`

*   Details:

Edit the internal webpack config with [webpack-chain](https://github.com/mozilla-neutrino/webpack-chain).

This option accepts a function that will receive a `Config` instance that provided by `webpack-chain` as the 1st argument an `isServer` flag as the 2nd argument and an `isBuild` flag as the 3rd argument.

### [devServerSetupMiddlewares](https://vuepress.vuejs.org/reference/bundler/webpack#devserversetupmiddlewares)

*   Type: `(middlewares: Middleware[], devServer: Server) => Middleware[]`

*   Details:

A hook to be called in `devServer.setupMiddlewares` of webpack.

The arguments of the function are those of `devServer.setupMiddlewares`.

*   Also see:

    *   [Webpack > Configuration > DevServer > devServer.setupMiddlewares](https://webpack.js.org/configuration/dev-server/#devserversetupmiddlewares)

### [vue](https://vuepress.vuejs.org/reference/bundler/webpack#vue)

*   Type: `VueLoaderOptions`

*   Details:

Options for `vue-loader`.

*   Also see:

    *   [vue-loader > Options Reference](https://vue-loader.vuejs.org/options.html)

### [postcss](https://vuepress.vuejs.org/reference/bundler/webpack#postcss)

*   Type: `PostcssLoaderOptions`

*   Details:

Options for `postcss-loader`.

*   Also see:

    *   [postcss-loader > Options](https://github.com/webpack-contrib/postcss-loader#options)

### [stylus](https://vuepress.vuejs.org/reference/bundler/webpack#stylus)

*   Type: `StylusLoaderOptions`

*   Details:

Options for `stylus-loader`.

*   Also see:

    *   [stylus-loader > Options](https://github.com/webpack-contrib/stylus-loader#options)

### [scss](https://vuepress.vuejs.org/reference/bundler/webpack#scss)

*   Type: `SassLoaderOptions`

*   Details:

Options for `sass-loader` for `.scss` files.

*   Also see:

    *   [sass-loader > Options](https://github.com/webpack-contrib/sass-loader#options)

### [sass](https://vuepress.vuejs.org/reference/bundler/webpack#sass)

*   Type: `SassLoaderOptions`

*   Details:

Options for `sass-loader` for `.sass` files.

*   Also see:

    *   [sass-loader > Options](https://github.com/webpack-contrib/sass-loader#options)

### [less](https://vuepress.vuejs.org/reference/bundler/webpack#less)

*   Type: `LessLoaderOptions`

*   Details:

Options for `less-loader`.

*   Also see:

    *   [less-loader > Options](https://github.com/webpack-contrib/less-loader#options)

### [evergreen](https://vuepress.vuejs.org/reference/bundler/webpack#evergreen)

*   Type: `boolean`

*   Default: `true`

*   Details:

Set to `true` if you are only targeting evergreen browsers. This will disable some transpilation and polyfills, and result in faster builds and smaller files.

[FAQ](https://vuepress.vuejs.org/reference/bundler/webpack#faq)
---------------------------------------------------------------

### [Referencing Public Files after Changing `base`](https://vuepress.vuejs.org/reference/bundler/webpack#referencing-public-files-after-changing-base)

Unlike Vite, Webpack won't handle `base` for public files automatically. So if you change the `base` of your site, you'd better to use [Base Helper](https://vuepress.vuejs.org/guide/assets#base-helper) when referencing an public image file.

### [Using with Default Theme](https://vuepress.vuejs.org/reference/bundler/webpack#using-with-default-theme)

Default theme is using [SASS](https://sass-lang.com/) as CSS pre-processor, so you might need to install [sass-loader](https://www.npmjs.com/package/sass-loader) as a peer dependency to make it work with Webpack, especially when you are using [pnpm](https://pnpm.io/).

[Prev Vite](https://vuepress.vuejs.org/reference/bundler/vite)
