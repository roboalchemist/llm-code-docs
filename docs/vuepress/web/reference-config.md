# Source: https://vuepress.vuejs.org/reference/config

Title: Config

URL Source: https://vuepress.vuejs.org/reference/config

Markdown Content:
[Site Config](https://vuepress.vuejs.org/reference/config#site-config)
----------------------------------------------------------------------

### [base](https://vuepress.vuejs.org/reference/config#base)

*   Type: `string`

*   Default: `/`

*   Details:

The base URL the site will be deployed at.

You will need to set this if you plan to deploy your site under a sub path. It should always start and end with a slash. For example, if you plan to deploy your site to GitHub pages at `https://foo.github.io/bar/`, then you should set `base` to `"/bar/"`.

The `base` is automatically prepended to the URLs that start with `/` in other options, so you only need to specify it once. (Except for attrs of [head](https://vuepress.vuejs.org/reference/config#head))

Notice that `base` should be an absolute URL pathname starting and ending with `/` .

*   Also see:

    *   [Guide > Assets > Base Helper](https://vuepress.vuejs.org/guide/assets#base-helper)
    *   [Guide > Deployment](https://vuepress.vuejs.org/guide/deployment)

### [lang](https://vuepress.vuejs.org/reference/config#lang)

*   Type: `string`

*   Default: `en-US`

*   Details:

Language for the site.

This will be the `lang` attribute of the `<html>` tag in the rendered HTML.

This can be specified in different locales.

*   Also see:

    *   [Config > locales](https://vuepress.vuejs.org/reference/config#locales)
    *   [Frontmatter > lang](https://vuepress.vuejs.org/reference/frontmatter#lang)

### [title](https://vuepress.vuejs.org/reference/config#title)

*   Type: `string`

*   Default: `''`

*   Details:

Title for the site.

This will be the suffix for all page titles, and displayed in the navbar in the default theme.

This can be specified in different locales.

*   Also see:

    *   [Config > locales](https://vuepress.vuejs.org/reference/config#locales)

### [description](https://vuepress.vuejs.org/reference/config#description)

*   Type: `string`

*   Default: `''`

*   Details:

Description for the site.

This will be the `content` attribute of `<meta name="description" />` tag in the rendered HTML, which will be overrode by the `description` field of page frontmatter.

This can be specified in different locales.

*   Also see:

    *   [Config > locales](https://vuepress.vuejs.org/reference/config#locales)
    *   [Frontmatter > description](https://vuepress.vuejs.org/reference/frontmatter#description)

### [head](https://vuepress.vuejs.org/reference/config#head)

*   Type: `HeadConfig[]`

*   Default: `[]`

*   Details:

Extra tags to inject into the `<head>` tag in the rendered HTML.

You can specify each tag in the form of `[tagName, { attrName: attrValue }, innerHTML?]`.

This can be specified in different locales.

Notice that if the `attrValue` is a pathname, it will be kept as-is without prepending [base](https://vuepress.vuejs.org/reference/config#base) automatically, so remember to prepend it manually if needed.

*   Example:

To add a custom favicon:

```
export default {
  head: [['link', { rel: 'icon', href: '/images/logo.png' }]],
}
```

Rendered as：

```
<head>
  <link rel="icon" href="/images/logo.png" />
</head>
```

*   Also see: 
    *   [Config > locales](https://vuepress.vuejs.org/reference/config#locales)
    *   [Frontmatter > head](https://vuepress.vuejs.org/reference/frontmatter#head)

### [locales](https://vuepress.vuejs.org/reference/config#locales)

*   Type: `{ [path: string]: Partial<SiteLocaleData> }`

*   Default: `{}`

*   Details:

Specify locales for i18n support.

Acceptable fields:

    *   [lang](https://vuepress.vuejs.org/reference/config#lang)
    *   [title](https://vuepress.vuejs.org/reference/config#title)
    *   [description](https://vuepress.vuejs.org/reference/config#description)
    *   [head](https://vuepress.vuejs.org/reference/config#head)

*   Also see:

    *   [Guide > I18n](https://vuepress.vuejs.org/guide/i18n)

[Theme Config](https://vuepress.vuejs.org/reference/config#theme-config)
------------------------------------------------------------------------

### [theme](https://vuepress.vuejs.org/reference/config#theme)

*   Type: `Theme`

*   Details:

Set the theme of your site.

If this option is not set, the default theme will be used.

*   Also see:

    *   [Guide > Theme](https://vuepress.vuejs.org/guide/theme)
    *   [Default Theme > Config](https://ecosystem.vuejs.press/themes/default/config.html)

[Bundler Config](https://vuepress.vuejs.org/reference/config#bundler-config)
----------------------------------------------------------------------------

### [bundler](https://vuepress.vuejs.org/reference/config#bundler)

*   Type: `Bundler`

*   Details:

Set the bundler of your site.

If this option is not set, the default bundler will be used:

    *   With `vuepress` or `vuepress-vite`, the default bundler is vite.
    *   With `vuepress-webpack`, the default bundler is webpack.

*   Also see:

    *   [Guide > Bundler](https://vuepress.vuejs.org/guide/bundler)
    *   [Bundlers > Vite](https://vuepress.vuejs.org/reference/bundler/vite)
    *   [Bundlers > Webpack](https://vuepress.vuejs.org/reference/bundler/webpack)

[Common Config](https://vuepress.vuejs.org/reference/config#common-config)
--------------------------------------------------------------------------

### [dest](https://vuepress.vuejs.org/reference/config#dest)

*   Type: `string`

*   Default: ``${sourceDir}/.vuepress/dist``

*   Details:

Specify the output directory for `vuepress build` command.

### [temp](https://vuepress.vuejs.org/reference/config#temp)

*   Type: `string`

*   Default: ``${sourceDir}/.vuepress/.temp``

*   Details:

Specify the directory for temporary files.

Warning

Since VuePress will load temp files during dev and build, the temp directory should be inside project root to resolve dependencies correctly.

### [cache](https://vuepress.vuejs.org/reference/config#cache)

*   Type: `string`

*   Default: ``${sourceDir}/.vuepress/.cache``

*   Details:

Specify the directory for cache files.

### [public](https://vuepress.vuejs.org/reference/config#public)

*   Type: `string`

*   Default: ``${sourceDir}/.vuepress/public``

*   Details:

Specify the directory for public files.

*   Also see:

    *   [Guide > Assets > Public Files](https://vuepress.vuejs.org/guide/assets#public-files)

### [debug](https://vuepress.vuejs.org/reference/config#debug)

*   Type: `boolean`

*   Default: `false`

*   Details:

Enable debug mode or not.

This would be helpful for developers. Also, we are using [debug](https://github.com/visionmedia/debug) package for debug logging, which can be enabled via `DEBUG=vuepress*` environment variable.

### [pagePatterns](https://vuepress.vuejs.org/reference/config#pagepatterns)

*   Type: `string[]`

*   Default: `['**/*.md', '!.vuepress', '!node_modules']`

*   Details:

Specify the patterns of files you want to be resolved as pages. The patterns are relative to the source directory.

### [permalinkPattern](https://vuepress.vuejs.org/reference/config#permalinkpattern)

*   Type: `string | null`

*   Default: `null`

*   Details:

Specify the pattern to generate permalink.

This will be overrode by the `permalinkPattern` field of page frontmatter.

*   Also see:

    *   [Frontmatter > permalinkPattern](https://vuepress.vuejs.org/reference/frontmatter#permalinkpattern)

[Dev Config](https://vuepress.vuejs.org/reference/config#dev-config)
--------------------------------------------------------------------

### [host](https://vuepress.vuejs.org/reference/config#host)

*   Type: `string`

*   Default: `'0.0.0.0'`

*   Details:

Specify the host to use for the dev server.

### [port](https://vuepress.vuejs.org/reference/config#port)

*   Type: `number`

*   Default: `8080`

*   Details:

Specify the port to use for the dev server.

### [open](https://vuepress.vuejs.org/reference/config#open)

*   Type: `boolean`

*   Default: `false`

*   Details:

Whether to open the browser after dev-server had been started.

### [templateDev](https://vuepress.vuejs.org/reference/config#templatedev)

*   Type: `string`

*   Default: `'@vuepress/client/templates/dev.html'`

*   Details:

Specify the path of the HTML template to be used for dev.

[Build Config](https://vuepress.vuejs.org/reference/config#build-config)
------------------------------------------------------------------------

### [shouldPreload](https://vuepress.vuejs.org/reference/config#shouldpreload)

*   Type: `((file: string, type: string) => boolean)) | boolean`

*   Default: `true`

*   Details:

A function to control what files should have `<link rel="preload">` resource hints generated. Set to `true` or `false` to enable or disable totally.

By default, only those files that are required by current page will be preloaded. So you can keep it `true` in most cases.

### [shouldPrefetch](https://vuepress.vuejs.org/reference/config#shouldprefetch)

*   Type: `((file: string, type: string) => boolean)) | boolean`

*   Default: `true`

*   Details:

A function to control what files should have `<link rel="prefetch">` resource hints generated. Set to `true` or `false` to enable or disable for all files.

If you set it to `true`, all files that required by other pages will be prefetched. This is good for small sites, which will speed up the navigation, but it might not be a good idea if you have lots of pages in your site.

### [templateBuild](https://vuepress.vuejs.org/reference/config#templatebuild)

*   Type: `string`

*   Default: `'@vuepress/client/templates/build.html'`

*   Details:

Specify the path of the HTML template to be used for build.

### [templateBuildRenderer](https://vuepress.vuejs.org/reference/config#templatebuildrenderer)

*   Type: `TemplateRenderer`

*   Default: `templateRenderer`

*   Details:

Specify the HTML template renderer to be used for build.

[Markdown Config](https://vuepress.vuejs.org/reference/config#markdown-config)
------------------------------------------------------------------------------

### [markdown](https://vuepress.vuejs.org/reference/config#markdown)

*   Type: `MarkdownOptions`

*   Default: `{}`

*   Details:

Configure VuePress built-in Markdown syntax extensions.

It accepts all options of [markdown-it](https://github.com/markdown-it/markdown-it), and the following additional options.

*   Also see:

    *   [markdown-it > Init with presets and options](https://github.com/markdown-it/markdown-it#init-with-presets-and-options)
    *   [Guide > Markdown > Syntax Extensions](https://vuepress.vuejs.org/guide/markdown#syntax-extensions)

### [markdown.anchor](https://vuepress.vuejs.org/reference/config#markdown-anchor)

*   Type: `AnchorPluginOptions | false`

*   Default:

```
const defaultOptions = {
  level: [1, 2, 3, 4, 5, 6],
  permalink: anchorPlugin.permalink.headerLink({
    class: 'header-anchor',
    safariReaderFix: true,
  }),
}
```

*   Details:

Options for [markdown-it-anchor](https://github.com/valeriangalliat/markdown-it-anchor).

Set to `false` to disable this plugin.

*   Also see:

    *   [Guide > Markdown > Syntax Extensions > Header Anchors](https://vuepress.vuejs.org/guide/markdown#header-anchors)

### [markdown.assets](https://vuepress.vuejs.org/reference/config#markdown-assets)

*   Type: `AssetsPluginOptions | false`

*   Details:

Options for VuePress built-in markdown-it assets plugin.

Set to `false` to disable this plugin.

Caution

You should not configure it unless you understand what it is for.

### [markdown.component](https://vuepress.vuejs.org/reference/config#markdown-component)

*   Type: `undefined | false`

*   Details:

Options for [@mdit-vue/plugin-component](https://github.com/mdit-vue/mdit-vue/tree/main/packages/plugin-component).

Set to `false` to disable this plugin.

Caution

You should not configure it unless you understand what it is for.

### [markdown.emoji](https://vuepress.vuejs.org/reference/config#markdown-emoji)

*   Type: `EmojiPluginOptions | false`

*   Details:

Options for [markdown-it-emoji](https://github.com/markdown-it/markdown-it-emoji).

Set to `false` to disable this plugin.

*   Also see:

    *   [Guide > Markdown > Syntax Extensions > Emoji](https://vuepress.vuejs.org/guide/markdown#emoji)

### [markdown.frontmatter](https://vuepress.vuejs.org/reference/config#markdown-frontmatter)

*   Type: `FrontmatterPluginOptions | false`

*   Details:

Options for [@mdit-vue/plugin-frontmatter](https://github.com/mdit-vue/mdit-vue/tree/main/packages/plugin-frontmatter).

Set to `false` to disable this plugin.

*   Also see:

    *   [Guide > Page > Frontmatter](https://vuepress.vuejs.org/guide/page#frontmatter)
    *   [Node API > Page Properties > frontmatter](https://vuepress.vuejs.org/reference/node-api#frontmatter)

Caution

You should not configure it unless you understand what it is for.

*   Type: `HeadersPluginOptions | false`

*   Default:

```
const defaultOptions = {
  level: [2, 3],
}
```

*   Details:

Options for [@mdit-vue/plugin-headers](https://github.com/mdit-vue/mdit-vue/tree/main/packages/plugin-headers).

Set to `false` to disable this plugin.

*   Also see:

    *   [Node API > Page Properties > headers](https://vuepress.vuejs.org/reference/node-api#headers)

### [markdown.importCode](https://vuepress.vuejs.org/reference/config#markdown-importcode)

*   Type: `ImportCodePluginOptions | false`

*   Details:

Options for VuePress built-in markdown-it import-code plugin.

Set to `false` to disable this plugin.

*   Also see:

    *   [Guide > Markdown > Syntax Extensions > Import Code Blocks](https://vuepress.vuejs.org/guide/markdown#import-code-blocks)

#### [markdown.importCode.handleImportPath](https://vuepress.vuejs.org/reference/config#markdown-importcode-handleimportpath)

*   Type: `(str: string) => string`

*   Default: `(str) => str`

*   Details:

A function to handle the import path of the import code syntax.

### [markdown.links](https://vuepress.vuejs.org/reference/config#markdown-links)

*   Type: `LinksPluginOptions | false`

*   Details:

Options for VuePress built-in markdown-it links plugin.

It will convert the tag of internal links to [internalTag](https://vuepress.vuejs.org/reference/config#markdownlinksinternaltag), and add extra attributes and icon to external links.

Set to `false` to disable this plugin.

*   Also see:

    *   [Guide > Markdown > Syntax Extensions > Links](https://vuepress.vuejs.org/guide/markdown#links)

#### [markdown.links.internalTag](https://vuepress.vuejs.org/reference/config#markdown-links-internaltag)

*   Type: `'a' | 'RouteLink' | 'RouterLink'`

*   Default: `'RouteLink'`

*   Details:

Tag for internal links.

By default, this plugin will transform internal links to [RouteLink](https://vuepress.vuejs.org/reference/components#routelink).

#### [markdown.links.externalAttrs](https://vuepress.vuejs.org/reference/config#markdown-links-externalattrs)

*   Type: `Record<string, string>`

*   Default: `{ target: '_blank', rel: 'noopener noreferrer' }`

*   Details:

Additional attributes for external links.

### [markdown.sfc](https://vuepress.vuejs.org/reference/config#markdown-sfc)

*   Type: `SfcPluginOptions | false`

*   Details:

Options for [@mdit-vue/plugin-sfc](https://github.com/mdit-vue/mdit-vue/tree/main/packages/plugin-sfc).

Set to `false` to disable this plugin.

*   Also see:

    *   [Cookbook > Markdown and Vue SFC](https://vuepress.vuejs.org/advanced/cookbook/markdown-and-vue-sfc)
    *   [Node API > Page Properties > sfcBlocks](https://vuepress.vuejs.org/reference/node-api#sfcblocks)

Caution

You should not configure it unless you understand what it is for.

### [markdown.slugify](https://vuepress.vuejs.org/reference/config#markdown-slugify)

*   Type: `(str: string) => string`

*   Details:

The default slugify function.

### [markdown.title](https://vuepress.vuejs.org/reference/config#markdown-title)

*   Type: `undefined | false`

*   Details:

Options for [@mdit-vue/plugin-title](https://github.com/mdit-vue/mdit-vue/tree/main/packages/plugin-title).

Set to `false` to disable this plugin.

Caution

You should not configure it unless you understand what it is for.

### [markdown.toc](https://vuepress.vuejs.org/reference/config#markdown-toc)

*   Type: `TocPluginOptions | false`

*   Default:

```
const defaultOptions = {
  level: [2, 3],
}
```

*   Details:

Options for [@mdit-vue/plugin-toc](https://github.com/mdit-vue/mdit-vue/tree/main/packages/plugin-toc).

Set to `false` to disable this plugin.

*   Also see:

    *   [Guide > Markdown > Syntax Extensions > Table of Contents](https://vuepress.vuejs.org/guide/markdown#table-of-contents)

#### [markdown.vPre.block](https://vuepress.vuejs.org/reference/config#markdown-vpre-block)

*   Type: `boolean`

*   Default: `true`

*   Details:

Add `v-pre` directive to `<pre>` tag of code block or not.

*   Also see:

    *   [Guide > Markdown > Syntax Extensions > Code Blocks > Wrap with v-pre](https://vuepress.vuejs.org/guide/markdown#wrap-with-v-pre)

#### [markdown.vPre.inline](https://vuepress.vuejs.org/reference/config#markdown-vpre-inline)

*   Type: `boolean`

*   Default: `true`

*   Details:

Add `v-pre` directive to `<code>` tag of inline code or not.

*   Also see:

    *   [Guide > Markdown > Syntax Extensions > Code Blocks > Wrap with v-pre](https://vuepress.vuejs.org/guide/markdown#wrap-with-v-pre)

[Plugin Config](https://vuepress.vuejs.org/reference/config#plugin-config)
--------------------------------------------------------------------------

### [plugins](https://vuepress.vuejs.org/reference/config#plugins)

*   Type: `(Plugin | Plugin[])[]`

*   Details:

Plugins to use.

This option accepts an array, each item of which could be a plugin or an array of plugins.

*   Also see:

    *   [Guide > Plugin](https://vuepress.vuejs.org/guide/plugin)

[Plugin API](https://vuepress.vuejs.org/reference/config#plugin-api)
--------------------------------------------------------------------

User config file also works as a VuePress plugin, so all of the Plugin APIs are available except the `name` and `multiple` options.

Please check out [Plugin API Reference](https://vuepress.vuejs.org/reference/plugin-api) for a full list of Plugin APIs.

[Prev Command Line Interface](https://vuepress.vuejs.org/reference/cli)[Next Frontmatter](https://vuepress.vuejs.org/reference/frontmatter)
