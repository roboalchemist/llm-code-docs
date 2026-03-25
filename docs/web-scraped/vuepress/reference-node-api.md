# Source: https://vuepress.vuejs.org/reference/node-api

Title: Node API

URL Source: https://vuepress.vuejs.org/reference/node-api

Markdown Content:
Node API can be imported from `vuepress/core`.

[App](https://vuepress.vuejs.org/reference/node-api#app)
--------------------------------------------------------

The app instance is available in all hooks of [Plugin API](https://vuepress.vuejs.org/reference/plugin-api).

The `BuildApp` and `DevApp` share almost the same properties and methods, except [build](https://vuepress.vuejs.org/reference/node-api#build) and [dev](https://vuepress.vuejs.org/reference/node-api#dev) method.

### [createBuildApp](https://vuepress.vuejs.org/reference/node-api#createbuildapp)

*   Signature:

`const createBuildApp: (config: AppConfig) => BuildApp`

*   Parameters:

| Parameter | Type | Description |
| --- | --- | --- |
| config | `AppConfig` | Config to create a VuePress app. |

*   Details:

Create a build mode app instance, which is used for building static files.

*   Example:

```
const build = async () => {
  const app = createBuildApp({
    // ...options
  })

  // initialize and prepare
  await app.init()
  await app.prepare()

  // build
  await app.build()

  // process onGenerated hook
  await app.pluginApi.hooks.onGenerated.process(app)
}
```

*   Also see: 
    *   [Node API > App Methods > build](https://vuepress.vuejs.org/reference/node-api#build)

### [createDevApp](https://vuepress.vuejs.org/reference/node-api#createdevapp)

*   Signature:

`const createDevApp: (config: AppConfig) => DevApp`

*   Parameters:

| Parameter | Type | Description |
| --- | --- | --- |
| config | `AppConfig` | Config to create a VuePress app. |

*   Details:

Create a dev mode app instance, which is used for starting a dev server.

*   Example:

```
const dev = async () => {
  const app = createDevApp({
    // ...options
  })

  // initialize and prepare
  await app.init()
  await app.prepare()

  // start dev server
  const closeDevServer = await app.dev()

  // set up file watchers
  const watchers = []

  // restart dev server
  const restart = async () => {
    await Promise.all([
      // close all watchers
      ...watchers.map((item) => item.close()),
      // close current dev server
      closeDevServer(),
    ])
    await dev()
  }

  // process onWatched hook
  await app.pluginApi.hooks.onWatched.process(app, watchers, restart)
}
```

*   Also see: 
    *   [Node API > App Methods > dev](https://vuepress.vuejs.org/reference/node-api#dev)

[App Properties](https://vuepress.vuejs.org/reference/node-api#app-properties)
------------------------------------------------------------------------------

### [options](https://vuepress.vuejs.org/reference/node-api#options)

*   Type: `AppOptions`

*   Details:

Options of VuePress app.

The options come from the `config` argument in [createBuildApp](https://vuepress.vuejs.org/reference/node-api#createbuildapp) / [createDevApp](https://vuepress.vuejs.org/reference/node-api#createdevapp), while all optional fields will be filled with a default value.

### [siteData](https://vuepress.vuejs.org/reference/node-api#sitedata)

*   Type: `SiteData`

*   Details:

Site data that set by user, including all the [site config](https://vuepress.vuejs.org/reference/config#site-config), which will be used in client side.

### [version](https://vuepress.vuejs.org/reference/node-api#version)

*   Type: `string`

*   Details:

Version of VuePress app, i.e. version of `@vuepress/core` package.

### [env.isBuild](https://vuepress.vuejs.org/reference/node-api#env-isbuild)

*   Type: `boolean`

*   Details:

Environment flag used to identify whether the app is running in build mode, i.e. whether a [BuildApp](https://vuepress.vuejs.org/reference/node-api#createbuildapp) instance.

### [env.isDev](https://vuepress.vuejs.org/reference/node-api#env-isdev)

*   Type: `boolean`

*   Details:

Environment flag used to identify whether the app is running in dev mode, i.e. whether a [DevApp](https://vuepress.vuejs.org/reference/node-api#createdevapp) instance.

### [env.isDebug](https://vuepress.vuejs.org/reference/node-api#env-isdebug)

*   Type: `boolean`

*   Details:

Environment flag used to identify whether the debug mode is enabled.

### [markdown](https://vuepress.vuejs.org/reference/node-api#markdown)

*   Type: `MarkdownIt`

*   Details:

The [markdown-it](https://github.com/markdown-it/markdown-it) instance used for parsing markdown content.

It is only available in and after [onInitialized](https://vuepress.vuejs.org/reference/plugin-api#oninitialized) hook.

### [pages](https://vuepress.vuejs.org/reference/node-api#pages)

*   Type: `Page[]`

*   Details:

The [Page](https://vuepress.vuejs.org/reference/node-api#page) object array.

It is only available in and after [onInitialized](https://vuepress.vuejs.org/reference/plugin-api#oninitialized) hook.

[App Methods](https://vuepress.vuejs.org/reference/node-api#app-methods)
------------------------------------------------------------------------

### [dir](https://vuepress.vuejs.org/reference/node-api#dir)

*   Utils:

    *   `dir.cache()`: resolve to cache directory
    *   `dir.temp()`: resolve to temp directory
    *   `dir.source()`: resolve to source directory
    *   `dir.dest()`: resolve to dest directory
    *   `dir.client()`: resolve to `@vuepress/client` directory
    *   `dir.public()`: resolve to public directory

*   Signature:

`type AppDirFunction = (...args: string[]) => string`

*   Details:

Utils to resolve the absolute file path in corresponding directory.

If you don't provide any arguments, it will return the absolute path of the directory.

*   Example:

```
// resolve the absolute file path of the `${sourceDir}/README.md`
const homeSourceFile = app.dir.source('README.md')
```

### [writeTemp](https://vuepress.vuejs.org/reference/node-api#writetemp)

*   Signature:

`declare const writeTemp = (file: string, content: string) => Promise<string>`

*   Parameters:

| Parameter | Type | Description |
| --- | --- | --- |
| file | `string` | Filepath of the temp file that going to be written. Relative to temp directory. |
| content | `string` | Content of the temp file that going to be written. |

*   Details:

A method to write temp file.

The written file could be imported via `@temp` alias in client files.

*   Example:

```
export default {
  // write temp file in onPrepared hook
  async onPrepared() {
    await app.writeTemp('foo.js', "export const foo = 'bar'")
  },
}
```

```
// import temp file in client code
import { foo } from '@temp/foo'
```

### [init](https://vuepress.vuejs.org/reference/node-api#init)

*   Signature:

`declare const init = () => Promise<void>`

*   Details:

Initialize VuePress app.

*   Also see:

    *   [Advanced > Architecture > Core Process and Hooks](https://vuepress.vuejs.org/advanced/architecture#core-process-and-hooks)

### [prepare](https://vuepress.vuejs.org/reference/node-api#prepare)

*   Signature:

`declare const prepare = () => Promise<void>`

*   Details:

Prepare client temp files.

*   Also see:

    *   [Advanced > Architecture > Core Process and Hooks](https://vuepress.vuejs.org/advanced/architecture#core-process-and-hooks)

### [build](https://vuepress.vuejs.org/reference/node-api#build)

*   Signature:

`declare const build = () => Promise<void>`

*   Details:

Generate static site files.

This method is only available in `BuildApp`.

*   Also see:

    *   [Node API > App > createBuildApp](https://vuepress.vuejs.org/reference/node-api#createbuildapp)
    *   [Advanced > Architecture > Core Process and Hooks](https://vuepress.vuejs.org/advanced/architecture#core-process-and-hooks)

### [dev](https://vuepress.vuejs.org/reference/node-api#dev)

*   Signature:

`declare const dev = () => Promise<() => Promise<void>>`

*   Details:

Start dev server.

This method is only available in `DevApp`.

*   Also see:

    *   [Node API > App > createDevApp](https://vuepress.vuejs.org/reference/node-api#createdevapp)
    *   [Advanced > Architecture > Core Process and Hooks](https://vuepress.vuejs.org/advanced/architecture#core-process-and-hooks)

[Page](https://vuepress.vuejs.org/reference/node-api#page)
----------------------------------------------------------

### [createPage](https://vuepress.vuejs.org/reference/node-api#createpage)

*   Signature:

`const createPage: (app: App, options: PageOptions) => Promise<Page>`

*   Parameters:

| Parameter | Type | Description |
| --- | --- | --- |
| app | `App` | The VuePress app instance. |
| options | `PageOptions` | Options to create VuePress page. |

*   Details:

Create a VuePress page object.

*   Example:

```
import { createPage } from 'vuepress/core'

export default {
  // create an extra page in onInitialized hook
  async onInitialized(app) {
    app.pages.push(
      await createPage(app, {
        path: '/foo.html',
        frontmatter: {
          layout: 'Layout',
        },
        content: `\
# Foo Page

Hello, world.
`,
      }),
    )
  },
}
```

*   Also see: 
    *   [Node API > App Properties > pages](https://vuepress.vuejs.org/reference/node-api#pages)
    *   [Cookbook > Adding Extra Pages](https://vuepress.vuejs.org/advanced/cookbook/adding-extra-pages)

[Page Properties](https://vuepress.vuejs.org/reference/node-api#page-properties)
--------------------------------------------------------------------------------

### [path](https://vuepress.vuejs.org/reference/node-api#path)

*   Type: `string`

*   Details:

Route path of the page.

*   Also see:

    *   [Guide > Page > Routing](https://vuepress.vuejs.org/guide/page#routing)
    *   [Node API > Page Properties > pathInferred](https://vuepress.vuejs.org/reference/node-api#pathinferred)

### [title](https://vuepress.vuejs.org/reference/node-api#title)

*   Type: `string`

*   Details:

Title of the page.

*   Also see:

    *   [Frontmatter > title](https://vuepress.vuejs.org/reference/frontmatter#title)

### [lang](https://vuepress.vuejs.org/reference/node-api#lang)

*   Type: `string`

*   Details:

Language of the page.

*   Example:

    *   `'en-US'`
    *   `'zh-CN'`

*   Also see:

    *   [Frontmatter > lang](https://vuepress.vuejs.org/reference/frontmatter#title)

### [frontmatter](https://vuepress.vuejs.org/reference/node-api#frontmatter)

*   Type: `PageFrontmatter`

*   Details:

Frontmatter of the page.

*   Also see:

    *   [Frontmatter](https://vuepress.vuejs.org/reference/frontmatter)

*   Type: `PageHeader[]`

```
interface PageHeader {
  level: number
  title: string
  slug: string
  children: PageHeader[]
}
```

*   Details:

Headers of the page.

*   Also see:

    *   [Config > markdown.headers](https://vuepress.vuejs.org/reference/config#markdown-headers)

### [data](https://vuepress.vuejs.org/reference/node-api#data)

*   Type: `PageData`

```
interface PageData {
  path: string
  title: string
  lang: string
  frontmatter: PageFrontmatter
}
```

*   Details:

Data of the page.

Page data would be available in client side.

*   Also see:

    *   [Client API > usePageData](https://vuepress.vuejs.org/reference/client-api#usepagedata)
    *   [Plugin API > extendsPage](https://vuepress.vuejs.org/reference/plugin-api#extendspage)

### [content](https://vuepress.vuejs.org/reference/node-api#content)

*   Type: `string`

*   Details:

Raw content of the page.

### [contentRendered](https://vuepress.vuejs.org/reference/node-api#contentrendered)

*   Type: `string`

*   Details:

Rendered content of the page.

### [date](https://vuepress.vuejs.org/reference/node-api#date)

*   Type: `string`

*   Details:

Date of the page, in 'yyyy-MM-dd' format.

*   Example:

    *   `'0000-00-00'`
    *   `'2021-08-16`'

*   Also see:

    *   [Frontmatter > date](https://vuepress.vuejs.org/reference/frontmatter#date)

### [deps](https://vuepress.vuejs.org/reference/node-api#deps)

*   Type: `string[]`

*   Details:

Dependencies of the page.

For example, if users import code snippet in the page, the absolute file path of the imported file would be added to `deps`.

*   Also see:

    *   [Config > markdown.importCode](https://vuepress.vuejs.org/reference/config#markdown-importcode)

### [links](https://vuepress.vuejs.org/reference/node-api#links)

*   Type: `MarkdownLink[]`

```
interface MarkdownLink {
  raw: string
  relative: string
  absolute: string
}
```

*   Details:

Links included in the page content.

### [markdownEnv](https://vuepress.vuejs.org/reference/node-api#markdownenv)

*   Type: `Record<string, unknown>`

*   Details:

The `env` object when parsing markdown content with markdown-it.

Some markdown-it plugins may store extra information inside this object, and you can make use of them for advanced customization.

Notice that some other page properties are also extracted from the original `env` object. Those properties have already been removed from `page.markdownEnv`.

*   Also see:

    *   [markdown-it > API Documentation > MarkdownIt > parse](https://markdown-it.github.io/markdown-it/#MarkdownIt.parse)

### [pathInferred](https://vuepress.vuejs.org/reference/node-api#pathinferred)

*   Type: `string | null`

*   Details:

Route path of the page that inferred from file path.

By default, the route path is inferred from the relative file path of the Markdown source file. However, users may explicitly set the route path, e.g. [permalink](https://vuepress.vuejs.org/reference/node-api#permalink), which would be used as the final route path of the page. So we keep the inferred path as a page property in case you may need it.

It would be `null` if the page does not come from a Markdown source file.

*   Example:

    *   `'/'`
    *   `'/foo.html'`

*   Also see:

    *   [Guide > Page > Routing](https://vuepress.vuejs.org/guide/page#routing)
    *   [Node API > Page Properties > path](https://vuepress.vuejs.org/reference/node-api#path)

### [pathLocale](https://vuepress.vuejs.org/reference/node-api#pathlocale)

*   Type: `string`

*   Details:

Locale prefix of the page route path.

It is inferred from the relative file path of the Markdown source file and the key of `locales` option in user config.

*   Example:

    *   `'/'`
    *   `'/en/'`
    *   `'/zh/'`

*   Also see:

    *   [Config > locales](https://vuepress.vuejs.org/reference/config#locales)

### [permalink](https://vuepress.vuejs.org/reference/node-api#permalink)

*   Type: `string | null`

*   Details:

Permalink of the page.

*   Also see:

    *   [Frontmatter > permalink](https://vuepress.vuejs.org/reference/frontmatter#permalink)
    *   [Frontmatter > permalinkPattern](https://vuepress.vuejs.org/reference/frontmatter#permalinkpattern)

### [routeMeta](https://vuepress.vuejs.org/reference/node-api#routemeta)

*   Type: `Record<string, unknown>`

*   Details:

Custom data to be attached to the page route.

*   Also see:

    *   [Frontmatter > routeMeta](https://vuepress.vuejs.org/reference/frontmatter#routemeta)

What's the difference between route meta and page data?

Both [route meta](https://vuepress.vuejs.org/reference/node-api#routemeta) and [page data](https://vuepress.vuejs.org/reference/node-api#data) is available in client side. However, route meta is attached to the page route record, so the route meta of all pages would be loaded at once when users enter your site. In the contrast, page data is saved in separated files, which would be loaded only when users enter the corresponding page.

Therefore, it's not recommended to store large amounts of info into route meta, otherwise the initial loading speed will be affected a lot when your site has a large number of pages.

### [sfcBlocks](https://vuepress.vuejs.org/reference/node-api#sfcblocks)

*   Type: `MarkdownSfcBlocks`

*   Details:

Extracted vue SFC blocks of the page.

*   Also see:

    *   [Config > markdown.sfc](https://vuepress.vuejs.org/reference/config#markdown-sfc)

### [slug](https://vuepress.vuejs.org/reference/node-api#slug)

*   Type: `string`

*   Details:

Slug of the page.

It is inferred from the filename of the Markdown source file.

### [filePath](https://vuepress.vuejs.org/reference/node-api#filepath)

*   Type: `string | null`

*   Details:

Absolute path of the Markdown source file of the page.

It would be `null` if the page does not come from a Markdown source file.

### [filePathRelative](https://vuepress.vuejs.org/reference/node-api#filepathrelative)

*   Type: `string | null`

*   Details:

Relative path of the Markdown source file of the page.

It would be `null` if the page does not come from a Markdown source file.

[Prev Client API](https://vuepress.vuejs.org/reference/client-api)
