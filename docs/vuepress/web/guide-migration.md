# Source: https://vuepress.vuejs.org/guide/migration

Title: Migrating from v1

URL Source: https://vuepress.vuejs.org/guide/migration

Markdown Content:
Warning

Plugins and themes of VuePress v1 are not compatible with VuePress v2. You need to update them to corresponding v2 version.

Some major changes and enhancements of VuePress v2:

*   VuePress v2 is now using Vue 3, so make sure your components and other client files are compatible with Vue 3.
*   VuePress v2 is developed with TypeScript, so it provides better TS support now. It's highly recommended to use TypeScript to develop plugins and themes. VuePress config file also supports TypeScript, and you can use `.vuepress/config.ts` directly.
*   VuePress v2 supports both Webpack and Vite as bundler. You can choose the bundler you like in your config file.
*   VuePress v2 is now released as pure ESM packages, and CommonJS config files are no longer supported.

Core ideas and processes of VuePress v2 are the same with v1, while v2 API has been re-designed and becomes more normalized. So you might encounter breaking changes when migrating an existing v1 project to v2. This guide is here to help you migrating v1 sites / plugins / themes to v2.

*   If you are a common user, you need to read the guide [for users](https://vuepress.vuejs.org/guide/migration#for-users).
*   If you are a plugin author, you need to read the guide [for plugin authors](https://vuepress.vuejs.org/guide/migration#for-plugin-authors).
*   If you are a theme author, you need to read the guide [for theme authors](https://vuepress.vuejs.org/guide/migration#for-theme-authors).

[For Users](https://vuepress.vuejs.org/guide/migration#for-users)
-----------------------------------------------------------------

### [User Config Change](https://vuepress.vuejs.org/guide/migration#user-config-change)

Config file should be in ESM format, and CommonJS format config file is no longer supported.

.vuepress/config.ts

```
- module.exports = {
-   // user config
- }

+ import { defineUserConfig } from 'vuepress'
+
+ export default defineUserConfig({
+   // user config
+ })
```

#### [bundler](https://vuepress.vuejs.org/guide/migration#bundler)

Now we support using different bundlers.

Install and use the vite bundler in your config file:

`npm i -D @vuepress/bundler-vite@next`

.vuepress/config.ts

```
import { viteBundler } from '@vuepress/bundler-vite'
import { defineUserConfig } from 'vuepress'

export default defineUserConfig({
  bundler: viteBundler(),
})
```

Or using the webpack bundler:

`npm i -D @vuepress/bundler-webpack@next`

.vuepress/config.ts

```
import { webpackBundler } from '@vuepress/bundler-webpack'
import { defineUserConfig } from 'vuepress'

export default defineUserConfig({
  bundler: webpackBundler(),
})
```

#### [theme](https://vuepress.vuejs.org/guide/migration#theme)

Using a theme via string is not supported, and the default theme is not integrated into vuepress package by default.

Install and use the default theme in your config file:

`npm i -D @vuepress/theme-default@next`

.vuepress/config.ts

```
- module.exports = {
-   theme: '@vuepress/theme-default',
-   themeConfig: {
-     // default theme config
-   },
- }

+ import { defaultTheme } from '@vuepress/theme-default'
+ import { defineUserConfig } from 'vuepress'
+
+ export default defineUserConfig({
+   theme: defaultTheme({
+     // default theme config
+   }),
+ })
```

#### [themeConfig](https://vuepress.vuejs.org/guide/migration#themeconfig)

Removed. Set config to the theme directly.

#### [plugins](https://vuepress.vuejs.org/guide/migration#plugins)

Using a plugin via string is not supported. Import the plugin directly.

.vuepress/config.ts

```
- module.exports = {
-   plugins: [
-     [
-       '@vuepress/plugin-google-analytics',
-       {
-         id: 'G-XXXXXXXXXX',
-       },
-     ],
-   ],
- }

+ import { googleAnalyticsPlugin } from '@vuepress/plugin-google-analytics'
+ import { defineUserConfig } from 'vuepress'
+
+ export default defineUserConfig({
+   plugins: [
+     googleAnalyticsPlugin({
+         id: 'G-XXXXXXXXXX',
+     }),
+   ],
+ })
```

#### [shouldPrefetch](https://vuepress.vuejs.org/guide/migration#shouldprefetch)

Default value is changed from `() => true` to `true`.

Removed.

You can watch files manually in [onWatched](https://vuepress.vuejs.org/reference/plugin-api#onwatched) hook.

#### [patterns](https://vuepress.vuejs.org/guide/migration#patterns)

Renamed to `pagePatterns`

#### [markdown.lineNumbers](https://vuepress.vuejs.org/guide/migration#markdown-linenumbers)

Removed.

The same feature is implemented in [@vuepress/plugin-prismjs](https://ecosystem.vuejs.press/plugins/prismjs.html) and [@vuepress/plugin-shiki](https://ecosystem.vuejs.press/plugins/shiki.html).

#### [markdown.pageSuffix](https://vuepress.vuejs.org/guide/migration#markdown-pagesuffix)

Removed.

#### [markdown.externalLinks](https://vuepress.vuejs.org/guide/migration#markdown-externallinks)

Moved to [markdown.links.externalAttrs](https://vuepress.vuejs.org/reference/config#markdown-links).

#### [markdown.toc](https://vuepress.vuejs.org/guide/migration#markdown-toc)

Changed.

See [Config > markdown.toc](https://vuepress.vuejs.org/reference/config#markdown-toc)

#### [markdown.plugins](https://vuepress.vuejs.org/guide/migration#markdown-plugins)

Removed.

Use markdown-it plugins in [extendsMarkdown](https://vuepress.vuejs.org/reference/plugin-api#extendsmarkdown) hook.

#### [markdown.extendMarkdown](https://vuepress.vuejs.org/guide/migration#markdown-extendmarkdown)

Removed.

Use [extendsMarkdown](https://vuepress.vuejs.org/reference/plugin-api#extendsmarkdown) hook.

Moved to [markdown.headers](https://vuepress.vuejs.org/reference/config#markdown-headers).

All webpack related configs are moved to options of `@vuepress/bundler-webpack`, including:

*   `postcss`
*   `stylus`
*   `scss`
*   `sass`
*   `less`
*   `chainWebpack`
*   `configureWebpack`
*   `evergreen`: default value is changed from `false` to `true`

.vuepress/config.ts

```
- module.exports = {
-   sass: { /* ... */ },
- }

+ import { webpackBundler } from '@vuepress/bundler-webpack'
+ import { defineUserConfig } from 'vuepress'
+
+ export default defineUserConfig({
+   bundler: webpackBundler({
+     sass: { /* ... */ },
+   }),
+ })
```

Please refer to [Guide > Bundler](https://vuepress.vuejs.org/guide/bundler).

### [Frontmatter Change](https://vuepress.vuejs.org/guide/migration#frontmatter-change)

#### [meta](https://vuepress.vuejs.org/guide/migration#meta)

Removed.

Use [head](https://vuepress.vuejs.org/reference/frontmatter#head) instead. For example:

```
head:
  - - meta
    - name: foo
      content: bar
  - - link
    - rel: canonical
      href: foobar
  - - script
    - {}
    - console.log('hello from frontmatter');
```

Has the same structure with:

.vuepress/config.ts

```
import { defineUserConfig } from 'vuepress'

export default defineUserConfig({
  // ...
  head: [
    ['meta', { name: 'foo', content: 'bar' }],
    ['link', { rel: 'canonical', href: 'foobar' }],
    ['script', {}, `console.log('hello from frontmatter');`],
  ],
  // ...
})
```

### [Permalink Patterns Change](https://vuepress.vuejs.org/guide/migration#permalink-patterns-change)

*   `:i_month`: removed
*   `:i_day`: removed
*   `:minutes`: removed (undocumented in v1)
*   `:seconds`: removed (undocumented in v1)
*   `:regular`: renamed to `:raw`

See [Frontmatter > permalinkPattern](https://vuepress.vuejs.org/reference/frontmatter#permalinkpattern).

### [Palette System Change](https://vuepress.vuejs.org/guide/migration#palette-system-change)

The stylus palette system of VuePress v1 (i.e. `styles/palette.styl` and `styles/index.styl`) is no longer provided by VuePress Core.

The palette system is extracted to [@vuepress/plugin-palette](https://ecosystem.vuejs.press/plugins/palette.html).

Theme authors can use their own way to allow users to customize styles, and not be limited with stylus.

If you are using default theme, the palette system is still available but migrated to SASS, while most variables have been migrated to CSS variables. See [Default Theme > Styles](https://ecosystem.vuejs.press/themes/default/styles.html).

### [Conventional Files Change](https://vuepress.vuejs.org/guide/migration#conventional-files-change)

#### [.vuepress/enhanceApp.js](https://vuepress.vuejs.org/guide/migration#vuepress-enhanceapp-js)

Renamed to `.vuepress/client.{js,ts}`, and the usage has been changed, too.

See [Advanced > Cookbook > Usage of Client Config](https://vuepress.vuejs.org/advanced/cookbook/usage-of-client-config).

#### [.vuepress/components/](https://vuepress.vuejs.org/guide/migration#vuepress-components)

Files in this directory will not be registered as Vue components automatically.

You need to use [@vuepress/plugin-register-components](https://ecosystem.vuejs.press/plugins/register-components.html), or register your components manually in `.vuepress/client.{js,ts}`.

#### [.vuepress/theme/](https://vuepress.vuejs.org/guide/migration#vuepress-theme)

This directory will not be used as local theme implicitly if it is existed.

You need to import and set your local theme via [theme](https://vuepress.vuejs.org/reference/config#theme) option.

### [Markdown Change](https://vuepress.vuejs.org/guide/migration#markdown-change)

*   Markdown slot is no longer supported.
*   Markdown image syntax does not support webpack aliases anymore. Links without `./` prefix are also treated as relative links, which is aligned with the behavior of the native markdown image syntax. If you want to use aliases in image paths, or use images from external packages, you should use `<img>` tag instead.

```
- ![](@alias/foo.png)
- ![](package-name/bar.png)

+ <img src="@alias/foo.png">
+ <img src="package-name/bar.png">
```

### [CLI Change](https://vuepress.vuejs.org/guide/migration#cli-change)

#### [eject command](https://vuepress.vuejs.org/guide/migration#eject-command)

Removed.

#### [cache options](https://vuepress.vuejs.org/guide/migration#cache-options)

*   `-c, --cache [cache]`: changed to `--cache <cache>`, which means that the shorthand `-c` is not for `cache` option, and the value of `cache` option is not optional.
*   `--no-cache`: renamed to `--clean-cache` .

### [Default Theme Change](https://vuepress.vuejs.org/guide/migration#default-theme-change)

#### [Built-in Components](https://vuepress.vuejs.org/guide/migration#built-in-components)

*   `<CodeGroup />` and `<CodeBlock />` are replaced by [code tab feature](https://ecosystem.vuejs.press/themes/default/markdown.html#code-tabs)
*   `<Badge />`
    *   `$badgeErrorColor` palette variable renamed to `$badgeDangerColor`
    *   `type` prop only accepts `tip`, `warning` and `danger` now

#### [Palette System](https://vuepress.vuejs.org/guide/migration#palette-system)

The palette system of default theme has migrated to SASS and CSS variables.

See [Default Theme > Styles](https://ecosystem.vuejs.press/themes/default/styles.html).

#### [Theme Config](https://vuepress.vuejs.org/guide/migration#theme-config)

Default theme config has been changed a lot. You'd better check the config reference of v2 default theme to migrate it properly.

See [Default Theme > Config](https://ecosystem.vuejs.press/themes/default/config.html).

Here we list some notable changes:

```
- sidebar: {
-   title: 'Foo Bar',
-   path: '/foo/bar.html',
-   collapsable: true,
-   children: [
-     ['/baz', 'Baz'],
-   ],
- }

+ sidebar: {
+   text: 'Foo Bar',
+   link: '/foo/bar.html',
+   collapsible: true,
+   children: [
+     {
+       text: 'Baz',
+       link: '/baz',
+     }
+   ],
+ }
```

### [Official Plugins Change](https://vuepress.vuejs.org/guide/migration#official-plugins-change)

Check the v2 docs of official plugins.

### [Community Themes and Plugins](https://vuepress.vuejs.org/guide/migration#community-themes-and-plugins)

Themes and plugins of v1 are not compatible with v2.

Please make sure that those themes and plugins you are using have supported v2, and refer to their own documentation for migration guide.

Some major breaking changes:

*   You cannot use other plugins in your plugin anymore, which avoids lots of potential issues caused by plugin nesting. If your plugin depends on other plugins, you could list them in the docs to ask users import them manually. Alternatively, you can provide users with an array of plugins for convenience.
*   Most of the v1 hooks have equivalents in v2. The only exception is `extendsCli`, which has been removed.
*   Webpack related hooks are removed, because VuePress Core has decoupled with webpack. You can try to use [extendsBundlerOptions](https://vuepress.vuejs.org/reference/plugin-api#extendsbundleroptions) hook for similar purpose, and make sure to work with all bundlers.

For more detailed guide about how to write a plugin in v2, see [Advanced > Writing a Plugin](https://vuepress.vuejs.org/advanced/plugin).

### [Plugin API Change](https://vuepress.vuejs.org/guide/migration#plugin-api-change)

*   `plugins`: removed
*   `ready`: renamed to `onPrepared`
*   `updated`: renamed to `onWatched`
*   `generated`: renamed to `onGenerated`
*   `additionalPages`: removed, use `app.pages.push(createPage())` in `onInitialized` hook
*   `clientDynamicModules`: removed, use `app.writeTemp()` in `onPrepared` hook
*   `enhanceAppFiles`: removed, use `clientConfigFile` hook
*   `globalUIComponents`: removed, use `clientConfigFile` hook
*   `clientRootMixin`: removed, use `clientConfigFile` hook
*   `extendMarkdown`: renamed to `extendsMarkdown`
*   `chainMarkdown`: removed
*   `extendPageData`: renamed to `extendsPage`
*   `extendsCli`: removed
*   `configureWebpack`: removed
*   `chainWebpack`: removed
*   `beforeDevServer`: removed
*   `afterDevServer`: removed

See [Plugin API](https://vuepress.vuejs.org/reference/plugin-api).

[For Theme Authors](https://vuepress.vuejs.org/guide/migration#for-theme-authors)
---------------------------------------------------------------------------------

Although we do not allow using other plugins in a plugin anymore, you can still use plugins in your theme.

Some major breaking changes:

*   There is no **conventional theme directory structure** anymore. 
    *   The file `theme/enhanceApp.js` will not be used as client app enhance file implicitly. You need to specify it explicitly in `clientConfigFile` hook.
    *   Files in `theme/global-components/` directory will not be registered as Vue components automatically. You need to use [@vuepress/plugin-register-components](https://ecosystem.vuejs.press/plugins/register-components.html), or register components manually in `clientConfigFile`.
    *   Files in `theme/layouts/` directory will not be registered as layout components automatically. You need to specify it explicitly in `layouts` option in `clientConfigFile`.
    *   Files in `theme/templates/` directory will not be used as dev / ssr template automatically. You need to specify theme explicitly in `templateBuild` and `templateDev` option.
    *   Always provide a valid js entry file, and do not use `"main": "layouts/Layout.vue"` as the theme entry anymore.

*   `themeConfig` is removed from user config and site data. To access the `themeConfig` as you would via `this.$site.themeConfig` in v1, we now recommend using the [@vuepress/plugin-theme-data](https://ecosystem.vuejs.press/plugins/theme-data.html) plugin and its `useThemeData` composition API.
*   Stylus is no longer the default CSS pre-processor, and the stylus palette system is not embedded. If you still want to use similar palette system as v1, [@vuepress/plugin-palette](https://ecosystem.vuejs.press/plugins/palette.html) may help.
*   Markdown code blocks syntax highlighting by Prism.js is not embedded by default. You can use either [@vuepress/plugin-prismjs](https://ecosystem.vuejs.press/plugins/prismjs.html) or [@vuepress/plugin-shiki](https://ecosystem.vuejs.press/plugins/shiki.html), or implement syntax highlighting in your own way.
*   For scalability concerns, `this.$site.pages` is not available any more. See [Advanced > Cookbook > Resolving Routes](https://vuepress.vuejs.org/advanced/cookbook/resolving-routes) for how to retrieve pages data in v2.

For more detailed guide about how to write a theme in v2, see [Advanced > Writing a Theme](https://vuepress.vuejs.org/advanced/theme).

### [Theme API Change](https://vuepress.vuejs.org/guide/migration#theme-api-change)

#### [layouts](https://vuepress.vuejs.org/guide/migration#layouts)

Removed.

Now you need to specify layout component in the client config file of your theme.

See [Advanced > Writing a theme](https://vuepress.vuejs.org/advanced/theme).

#### [extend](https://vuepress.vuejs.org/guide/migration#extend)

Renamed to `extends`.

You can still inherit a parent theme with `extends: parentTheme()`, which will extends the plugins, layouts, etc.

You can refer to [Default Theme > Extending](https://ecosystem.vuejs.press/themes/default/extending.html) for how to extend default theme.

The `@theme` and `@parent-theme` aliases are removed by default, but you can still make a extendable theme with similar approach, see [Advanced > Cookbook > Making a Theme Extendable](https://vuepress.vuejs.org/advanced/cookbook/making-a-theme-extendable).
