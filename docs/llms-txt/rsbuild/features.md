# Source: https://rsbuild.dev/guide/faq/features.md

# Source: https://rsbuild.dev/guide/start/features.md

# Features

Overview of the main features supported by Rsbuild.

## JavaScript

| Features             | Description                                                                                               | Links                                                                                                                               |
| -------------------- | --------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Rspack               | Use Rspack as the bundler by default                                                                      | <ul><li>[Configure Rspack](/guide/configuration/rspack.md)</li></ul>                                                                   |
| SWC compilation      | Transform and minify JavaScript and TypeScript code using SWC by default                                  | <ul><li>[Configure SWC](/guide/configuration/swc.md)</li></ul>                                                                         |
| TS compilation       | TypeScript files are compiled using SWC by default                                                        | <ul><li>[TypeScript compilation](/guide/basic/typescript.md#typescript-compilation)</li></ul>                                          |
| Code minification    | Code minification is enabled by default in production mode                                                | <ul><li>[output.minify](/config/output/minify.md)</li></ul>                                                                            |
| Polyfill injection   | Optional feature, inject core-js and other polyfills                                                      | <ul><li>[Browser compatibility](/guide/advanced/browser-compatibility.md)</li><li>[output.polyfill](/config/output/polyfill.md)</li></ul> |
| SourceMap generation | Source maps are generated in development mode by default                                                  | <ul><li>[output.sourceMap](/config/output/source-map.md)</li></ul>                                                                     |
| Alias                | Optional feature, set import alias                                                                        | <ul><li>[resolve.alias](/config/resolve/alias.md)</li></ul>                                                                            |
| Babel compilation    | Optional feature, use Babel to transform JavaScript and TypeScript code                                   | <ul><li>[Babel plugin](/plugins/list/plugin-babel.md)</li></ul>                                                                        |
| Node outputs         | Optional feature, build bundles that run in Node.js environment                                           | <ul><li>[Node target](/config/output/target.md#node-target)</li></ul>                                                                  |
| Web Workers          | Optional feature, use Web Workers                                                                         | <ul><li>[Web Workers](/guide/basic/web-workers.md)</li></ul>                                                                           |
| Browserslist         | Optional feature, use browserslist to specify which browsers should be supported in your web application. | <ul><li>[Browserslist](/guide/advanced/browserslist.md)</li></ul>                                                                      |
| Compatibility check  | Optional feature, scan build outputs for advanced syntax that isn't supported by the target browsers      | <ul><li>[@rsbuild/plugin-check-syntax](https://github.com/rstackjs/rsbuild-plugin-check-syntax)</li></ul>                           |
| Environment variable | Optional feature, inject environment variables or expressions into the code                               | <ul><li>[Environment variables](/guide/advanced/env-vars.md)</li></ul>                                                                 |
| Node polyfill        | Optional feature, inject polyfills for Node core modules on the browser side                              | <ul><li>[Node polyfill plugin](https://github.com/rstackjs/rsbuild-plugin-node-polyfill)</li></ul>                                  |
| Type check           | Optional feature, run type checker to check for type issues in code                                       | <ul><li>[Type checking](/guide/basic/typescript.md#type-checking)</li></ul>                                                            |
| Module Federation    | Optional feature, dynamically load modules and share dependencies                                         | <ul><li>[Module Federation](/guide/advanced/module-federation.md)</li></ul>                                                            |

## CSS

| Features                | Description                                                | Links                                                                                                           |
| ----------------------- | ---------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| Lightning CSS           | Use Lightning CSS to downgrade CSS syntax by default       | <ul><li>[CSS](/guide/styling/css-usage.md)</li></ul>                                                               |
| PostCSS transformation  | Optional feature, use PostCSS to transform CSS files       | <ul><li>[CSS](/guide/styling/css-usage.md)</li><li>[tools.postcss](/config/tools/postcss.md)</li></ul>                |
| Tailwind CSS            | Optional feature, use Tailwind CSS                         | <ul><li>[Tailwind CSS](/guide/styling/tailwindcss.md)</li></ul>                                                    |
| UnoCSS                  | Optional feature, use UnoCSS                               | <ul><li>[UnoCSS](/guide/styling/unocss.md)</li></ul>                                                               |
| Sass preprocessing      | Optional feature, compile Sass/Scss files                  | <ul><li>[CSS](/guide/styling/css-usage.md)</li><li>[Sass plugin](/plugins/list/plugin-sass.md)</li></ul>              |
| Less preprocessing      | Optional feature, compile Less files                       | <ul><li>[CSS](/guide/styling/css-usage.md)</li><li>[Less plugin](/plugins/list/plugin-less.md)</li></ul>              |
| Stylus preprocessing    | Optional feature, compile Stylus files                     | <ul><li>[CSS](/guide/styling/css-usage.md)</li><li>[Stylus plugin](/plugins/list/plugin-stylus.md)</li></ul>          |
| CSS Modules compilation | Support compiling `*.module.*` files by default            | <ul><li>[CSS Modules](/guide/styling/css-modules.md)</li><li>[tools.cssLoader](/config/tools/css-loader.md)</li></ul> |
| CSS Modules type        | Optional feature, generate type definition for CSS Modules | <ul><li>[Typed CSS Modules plugin](https://github.com/rstackjs/rsbuild-plugin-typed-css-modules)</li></ul>      |
| CSS minification        | CSS minification is enabled by default in production build | <ul><li>[CSS](/guide/styling/css-usage.md)</li></ul>                                                               |
| Inline CSS into JS      | Optional feature, inline CSS files to JavaScript files     | <ul><li>[CSS](/guide/styling/css-usage.md)</li><li>[output.injectStyles](/config/output/inject-styles.md)</li></ul>   |

## HTML

| Features            | Description                                  | Links                                                                                                                                     |
| ------------------- | -------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Set title           | Set HTML `<title>` tag                       | <ul><li>[Set page title](/guide/basic/html-template.md#set-page-title)</li><li>[html.title](/config/html/title.md)</li></ul>                    |
| Set meta            | Set HTML `<meta>` tag                        | <ul><li>[Set meta tags](/guide/basic/html-template.md#set-meta-tags)</li><li>[html.meta](/config/html/meta.md)</li></ul>                        |
| Set favicon         | Set favicon                                  | <ul><li>[Set page icon](/guide/basic/html-template.md#set-page-icon)</li><li>[html.favicon](/config/html/favicon.md)</li></ul>                  |
| Set app icon        | Set web application icons                    | <ul><li>[Set page icon](/guide/basic/html-template.md#set-page-icon)</li><li>[html.appIcon](/config/html/app-icon.md)</li></ul>                 |
| EJS template engine | Optional feature, use EJS template engine    | <ul><li>[HTML template - EJS](/guide/basic/html-template.md#ejs)</li></ul>                                                                   |
| Pug template engine | Optional feature, use pug template engine    | <ul><li>[Pug plugin](https://github.com/rstackjs/rsbuild-plugin-pug)</li></ul>                                                            |
| Inline JS files     | Optional feature, inline JS files into HTML  | <ul><li>[Inline static assets](/guide/optimization/inline-assets.md)</li><li>[output.inlineScripts](/config/output/inline-scripts.md)</li></ul> |
| Inline CSS files    | Optional feature, inline CSS files into HTML | <ul><li>[Inline static assets](/guide/optimization/inline-assets.md)</li><li>[output.inlineStyles](/config/output/inline-styles.md)</li></ul>   |

## Server

| Features          | Description                                                               | Links                                                           |
| ----------------- | ------------------------------------------------------------------------- | --------------------------------------------------------------- |
| Public dir        | Serves public assets from the `public` directory by default               | <ul><li>[server.publicDir](/config/server/public-dir.md)</li></ul> |
| SSR               | Optional feature, implement server-side rendering                         | <ul><li>[SSR](/guide/advanced/ssr.md)</li></ul>                    |
| Proxy             | Optional feature, proxy requests to the specified service                 | <ul><li>[server.proxy](/config/server/proxy.md)</li></ul>          |
| Open page         | Optional feature, automatically open page in browser when starting server | <ul><li>[server.open](/config/server/open.md)</li></ul>            |
| HTTPS             | Optional feature, enable HTTPS server                                     | <ul><li>[server.https](/config/server/https.md)</li></ul>          |
| Custom middleware | Optional feature, use custom middleware                                   | <ul><li>[Middleware](/guide/basic/server.md#middleware)</li></ul>  |

## UI framework

| Features      | Description                                                                | Links                                                                                              |
| ------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| React         | Optional feature, enable compilation of React JSX                          | <ul><li>[React plugin](/plugins/list/plugin-react.md)</li></ul>                                       |
| React Refresh | Optional feature, enable React Refresh                                     | <ul><li>[Hot module replacement](/guide/advanced/hmr.md)</li><li>[dev.hmr](/config/dev/hmr.md)</li></ul> |
| SVGR          | Optional feature, transform SVG to React component                         | <ul><li>[SVGR plugin](/plugins/list/plugin-svgr.md)</li></ul>                                         |
| Vue 3 SFC     | Optional feature, enable compilation of Vue 3 SFC (Single File Components) | <ul><li>[Vue plugin](/plugins/list/plugin-vue.md)</li></ul>                                           |
| Vue 3 JSX     | Optional feature, enable compilation of Vue 3 JSX syntax                   | <ul><li>[Vue JSX plugin](https://github.com/rstackjs/rsbuild-plugin-vue-jsx)</li></ul>             |
| Vue 2 SFC     | Optional feature, enable compilation of Vue 2 SFC (Single File Components) | <ul><li>[Vue 2 plugin](https://github.com/rstackjs/rsbuild-plugin-vue2)</li></ul>                  |
| Vue 2 JSX     | Optional feature, enable compilation of Vue 2 JSX syntax                   | <ul><li>[Vue 2 JSX plugin](https://github.com/rstackjs/rsbuild-plugin-vue2-jsx)</li></ul>          |
| Svelte        | Optional feature, enable compilation of Svelte component                   | <ul><li>[Svelte plugin](/plugins/list/plugin-svelte.md)</li></ul>                                     |
| Solid         | Optional feature, enable compilation of Solid JSX                          | <ul><li>[Solid plugin](/plugins/list/plugin-solid.md)</li></ul>                                       |

## Static assets

| Features               | Description                                                                  | Links                                                                                                                                    |
| ---------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Image assets           | Support importing image assets in code                                       | <ul><li>[Static assets](/guide/basic/static-assets.md)</li></ul>                                                                            |
| Font assets            | Support importing font assets in code                                        | <ul><li>[Static assets](/guide/basic/static-assets.md)</li></ul>                                                                            |
| Video assets           | Support importing video assets in code                                       | <ul><li>[Static assets](/guide/basic/static-assets.md)</li></ul>                                                                            |
| Wasm assets            | Support importing WebAssembly assets in code                                 | <ul><li>[Static assets](/guide/basic/static-assets.md)</li></ul>                                                                            |
| Node addons            | Support importing Node.js addons in code                                     | <ul><li>[Static assets](/guide/basic/static-assets.md)</li></ul>                                                                            |
| Inline static assets   | Small assets are inlined into JavaScript bundles by default                  | <ul><li>[Inline static assets](/guide/optimization/inline-assets.md)</li><li>[output.dataUriLimit](/config/output/data-uri-limit.md)</li></ul> |
| Clean up static assets | Automatically clean up static assets in the dist directory before each build | <ul><li>[output.cleanDistPath](/config/output/clean-dist-path.md)</li></ul>                                                                |
| Copy static assets     | Optional feature, copy static assets to the dist directory                   | <ul><li>[output.copy](/config/output/copy.md)</li></ul>                                                                                     |
| Generate manifest file | Optional feature, generate `manifest.json` file                              | <ul><li>[output.manifest](/config/output/manifest.md)</li></ul>                                                                             |

## Performance and debugging

| Features                   | Description                                                                                                                  | Links                                                                                                                                    |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Chunk splitting            | A variety of chunk splitting strategies are built into Rsbuild to automatically split the bundle into files of moderate size | <ul><li>[Code splitting](/guide/optimization/code-splitting.md)</li><li>[performance.chunkSplit](/config/performance/chunk-split.md)</li></ul> |
| Print file size            | After the production build, all bundle sizes are displayed by default                                                        | <ul><li>[performance.printFileSize](/config/performance/print-file-size.md)</li></ul>                                                       |
| Analyze build process      | Optional feature, use Rsdoctor to analyze build process                                                                      | <ul><li>[Use Rsdoctor](/guide/debug/rsdoctor.md)</li></ul>                                                                                  |
| Analyze bundle size        | Optional feature, analyze bundle size through Bundle Analyzer                                                                | <ul><li>[performance.bundleAnalyze](/config/performance/bundle-analyze.md)</li></ul>                                                        |
| Remove console             | Optional feature, remove `console.[methodName]` in code                                                                      | <ul><li>[performance.removeConsole](/config/performance/remove-console.md)</li></ul>                                                       |
| Optimize moment.js size    | Optional feature, remove the redundant locale files of moment.js                                                             | <ul><li>[performance.removeMomentLocale](/config/performance/remove-moment-locale.md)</li></ul>                                             |
| Dedupe packages            | Optional feature, remove duplicate npm packages                                                                              | <ul><li>[resolve.dedupe](/config/resolve/dedupe.md)</li></ul>                                                                               |
| Component on-demand import | Optional feature, selectively import code and styles from component libraries                                                | <ul><li>[source.transformImport](/config/source/transform-import.md)</li></ul>                                                              |
| Image compression          | Optional feature, compress used image resources                                                                              | <ul><li>[Image compress plugin](https://github.com/rstackjs/rsbuild-plugin-image-compress)</li></ul>                                     |
| Preload                    | Optional feature, fetches and caches a resource ahead of the current navigation                                              | <ul><li>[performance.preload](/config/performance/preload.md)</li></ul>                                                                     |
| Prefetch                   | Optional feature, fetches and caches a resource for an upcoming navigation                                                   | <ul><li>[performance.prefetch](/config/performance/prefetch.md)</li></ul>                                                                   |
| Preconnect                 | Optional feature, opens a connection to the resource's origin before it's needed                                             | <ul><li>[performance.preconnect](/config/performance/preconnect.md)</li></ul>                                                               |
| DNS prefetch               | Optional feature, preemptively perform DNS resolution for the target resource's origin                                       | <ul><li>[performance.dnsPrefetch](/config/performance/dns-prefetch.md)</li></ul>                                                            |
