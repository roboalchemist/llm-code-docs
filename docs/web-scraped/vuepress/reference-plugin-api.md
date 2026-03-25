# Source: https://vuepress.vuejs.org/reference/plugin-api

Title: Plugin API

URL Source: https://vuepress.vuejs.org/reference/plugin-api

Markdown Content:
You could check out [Node API](https://vuepress.vuejs.org/reference/node-api) for how to use the VuePress app instance in plugin hooks.

[Overview](https://vuepress.vuejs.org/reference/plugin-api#overview)
--------------------------------------------------------------------

Plugins should be used before initialization. The basic options will be handled once the plugin is used:

*   [name](https://vuepress.vuejs.org/reference/plugin-api#name)
*   [multiple](https://vuepress.vuejs.org/reference/plugin-api#multiple)

The following hooks will be processed when initializing app:

*   [extendsMarkdownOptions](https://vuepress.vuejs.org/reference/plugin-api#extendsmarkdownoptions)
*   [extendsMarkdown](https://vuepress.vuejs.org/reference/plugin-api#extendsmarkdown)
*   [extendsPageOptions](https://vuepress.vuejs.org/reference/plugin-api#extendspageoptions)
*   [extendsPage](https://vuepress.vuejs.org/reference/plugin-api#extendspage)
*   [onInitialized](https://vuepress.vuejs.org/reference/plugin-api#oninitialized)

The following hooks will be processed when preparing files:

*   [clientConfigFile](https://vuepress.vuejs.org/reference/plugin-api#clientconfigfile)
*   [onPrepared](https://vuepress.vuejs.org/reference/plugin-api#onprepared)

The following hooks will be processed in dev / build:

*   [extendsBundlerOptions](https://vuepress.vuejs.org/reference/plugin-api#extendsbundleroptions)
*   [alias](https://vuepress.vuejs.org/reference/plugin-api#alias)
*   [define](https://vuepress.vuejs.org/reference/plugin-api#define)
*   [onWatched](https://vuepress.vuejs.org/reference/plugin-api#onwatched)
*   [onGenerated](https://vuepress.vuejs.org/reference/plugin-api#ongenerated)

> Check out [Advanced > Architecture > Core Process and Hooks](https://vuepress.vuejs.org/advanced/architecture#core-process-and-hooks) to understand the process better.

[Basic Options](https://vuepress.vuejs.org/reference/plugin-api#basic-options)
------------------------------------------------------------------------------

### [name](https://vuepress.vuejs.org/reference/plugin-api#name)

*   Type: `string`

*   Details:

Name of the plugin.

It will be used for identifying plugins to avoid using a same plugin multiple times, so make sure to use a unique plugin name.

It should follow the naming convention:

    *   Non-scoped: `vuepress-plugin-foo`
    *   Scoped: `@org/vuepress-plugin-foo`

*   Also see:

    *   [Plugin API > multiple](https://vuepress.vuejs.org/reference/plugin-api#multiple)

### [multiple](https://vuepress.vuejs.org/reference/plugin-api#multiple)

*   Type: `boolean`

*   Default: `false`

*   Details:

Declare whether the plugin can be used multiple times.

If set to `false`, when using plugins with the same name, the one used previously will be replaced by the one used later.

If set to `true`, plugins with the same name could be used multiple times and won't be replaced.

*   Also see:

    *   [Plugin API > name](https://vuepress.vuejs.org/reference/plugin-api#name)

[Development Hooks](https://vuepress.vuejs.org/reference/plugin-api#development-hooks)
--------------------------------------------------------------------------------------

### [alias](https://vuepress.vuejs.org/reference/plugin-api#alias)

*   Type: `Record<string, any> | ((app: App, isServer: boolean) => Record<string, any>)`

*   Details:

Path aliases definition.

This hook accepts an object or a function that returns an object.

*   Example:

```
import { getDirname, path } from 'vuepress/utils'

const __dirname = getDirname(import.meta.url)

export default {
  alias: {
    '@alias': path.resolve(__dirname, './path/to/alias'),
  },
}
```

### [clientConfigFile](https://vuepress.vuejs.org/reference/plugin-api#clientconfigfile)

*   Type: `string | ((app: App) => string | Promise<string>)`

*   Details:

Path of client config file.

This hook accepts an absolute file path, or a function that returns the path.

*   Example:

```
import { getDirname, path } from 'vuepress/utils'

const __dirname = getDirname(import.meta.url)

export default {
  clientConfigFile: path.resolve(__dirname, './path/to/clientConfig.js'),
}
```

*   Also see: 
    *   [Client API > defineClientConfig](https://vuepress.vuejs.org/reference/client-api#defineclientconfig)
    *   [Advanced > Cookbook > Usage of Client Config](https://vuepress.vuejs.org/advanced/cookbook/usage-of-client-config)

### [define](https://vuepress.vuejs.org/reference/plugin-api#define)

*   Type: `Record<string, any> | ((app: App, isServer: boolean) => Record<string, any>)`

*   Details:

Define global constants replacements.

This hook accepts an object or a function that returns an object.

This can be useful for passing variables to client files. Note that the values will be automatically processed by `JSON.stringify()`.

*   Example:

```
export default {
  define: {
    __GLOBAL_BOOLEAN__: true,
    __GLOBAL_STRING__: 'foobar',
    __GLOBAL_OBJECT__: { foo: 'bar' },
  },
}
```

### [extendsBundlerOptions](https://vuepress.vuejs.org/reference/plugin-api#extendsbundleroptions)

*   Type: `(options: BundlerOptions, app: App) => void | Promise<void>`

*   Details:

Bundler options extension.

This hook accepts a function that will receive the bundler options.

This hook can be used for modifying bundler options.

You could determine which bundler the user is using by `app.options.bundler.name`.

*   Example:

Adding default [app.compilerOptions.isCustomElement](https://vuejs.org/api/application.html#app-config-compileroptions) option:

```
export default {
  extendsBundlerOptions: (bundlerOptions, app) => {
    // extends options of @vuepress/bundler-vite
    if (app.options.bundler.name === '@vuepress/bundler-vite') {
      bundlerOptions.vuePluginOptions ??= {}
      bundlerOptions.vuePluginOptions.template ??= {}
      bundlerOptions.vuePluginOptions.template.compilerOptions ??= {}
      const isCustomElement =
        bundlerOptions.vuePluginOptions.template.compilerOptions.isCustomElement
      bundlerOptions.vuePluginOptions.template.compilerOptions.isCustomElement =
        (tag) => {
          if (isCustomElement?.(tag)) return true
          if (tag === 'my-custom-element') return true
        }
    }

    // extends options of @vuepress/bundler-webpack
    if (app.options.bundler.name === '@vuepress/bundler-webpack') {
      bundlerOptions.vue ??= {}
      bundlerOptions.vue.compilerOptions ??= {}
      const isCustomElement = bundlerOptions.vue.compilerOptions.isCustomElement
      bundlerOptions.vue.compilerOptions.isCustomElement = (tag) => {
        if (isCustomElement?.(tag)) return true
        if (tag === 'my-custom-element') return true
      }
    }
  },
}
```

*   Also see: 
    *   [Bundlers > Vite](https://vuepress.vuejs.org/reference/bundler/vite)
    *   [Bundlers > Webpack](https://vuepress.vuejs.org/reference/bundler/webpack)

### [extendsMarkdownOptions](https://vuepress.vuejs.org/reference/plugin-api#extendsmarkdownoptions)

*   Type: `(options: MarkdownOptions, app: App) => void | Promise<void>`

*   Details:

Markdown options extension.

This hook accepts a function that will receive the markdown options.

This hook can be used for modifying markdown options.

*   Example:

Modifying the default header levels that going to be extracted:

```
export default {
  extendsMarkdownOptions: (markdownOptions, app) => {
    if (markdownOptions.headers === false) return
    markdownOptions.headers ??= {}
    if (markdownOptions.headers.level) return
    markdownOptions.headers.level = [2, 3, 4, 5, 6]
  },
}
```

*   Also see: 
    *   [Config > markdown](https://vuepress.vuejs.org/reference/config#markdown)

### [extendsMarkdown](https://vuepress.vuejs.org/reference/plugin-api#extendsmarkdown)

*   Type: `(md: Markdown, app: App) => void | Promise<void>`

*   Details:

Markdown enhancement.

This hook accepts a function that will receive an instance of `Markdown` powered by [markdown-it](https://github.com/markdown-it/markdown-it) in its arguments.

This hook can be used for using extra markdown-it plugins and implementing customizations.

*   Example:

```
export default {
  extendsMarkdown: (md) => {
    md.use(plugin1)
    md.linkify.set({ fuzzyEmail: false })
  },
}
```

### [extendsPageOptions](https://vuepress.vuejs.org/reference/plugin-api#extendspageoptions)

*   Type: `(options: PageOptions, app: App) => void | Promise<void>`

*   Details:

Page options extension.

This hook accepts a function that will receive the options of `createPage`.

This hook can be used for modifying page options

*   Example:

Set permalink pattern for pages in `_posts` directory:

```
export default {
  extendsPageOptions: (pageOptions, app) => {
    if (pageOptions.filePath?.startsWith(app.dir.source('_posts/'))) {
      pageOptions.frontmatter = pageOptions.frontmatter ?? {}
      pageOptions.frontmatter.permalinkPattern = '/:year/:month/:day/:slug.html'
    }
  },
}
```

*   Also see: 
    *   [Node API > Page > createPage](https://vuepress.vuejs.org/reference/node-api#createpage)

### [extendsPage](https://vuepress.vuejs.org/reference/plugin-api#extendspage)

*   Type: `(page: Page, app: App) => void | Promise<void>`

*   Details:

Page extension.

This hook accepts a function that will receive a `Page` instance.

This hook can be used for adding extra properties or modifying current properties on `Page` object.

Notice that changes to `page.data` and `page.routeMeta` can be used in client side code.

*   Example:

```
export default {
  extendsPage: (page) => {
    page.foo = 'foo'
    page.data.bar = 'bar'
  },
}
```

In client component:

```
import { usePageData } from 'vuepress/client'

export default {
  setup() {
    const page = usePageData()
    console.log(page.value.bar) // bar
  },
}
```

*   Also see: 
    *   [Client API > usePageData](https://vuepress.vuejs.org/reference/client-api#usepagedata)
    *   [Node API > Page Properties > data](https://vuepress.vuejs.org/reference/node-api#data)
    *   [Node API > Page Properties > routeMeta](https://vuepress.vuejs.org/reference/node-api#routemeta)

[Lifecycle Hooks](https://vuepress.vuejs.org/reference/plugin-api#lifecycle-hooks)
----------------------------------------------------------------------------------

### [onInitialized](https://vuepress.vuejs.org/reference/plugin-api#oninitialized)

*   Type: `(app: App) => void | Promise<void>`

*   Details:

This hook will be invoked once VuePress app has been initialized.

### [onPrepared](https://vuepress.vuejs.org/reference/plugin-api#onprepared)

*   Type: `(app: App) => void | Promise<void>`

*   Details:

This hook will be invoked once VuePress app has finished preparation.

### [onWatched](https://vuepress.vuejs.org/reference/plugin-api#onwatched)

*   Type: `(app: App, watchers: Closable[], restart: () => Promise<void>) => void | Promise<void>`

*   Details:

This hook will be invoked once VuePress app has started dev-server and watched files change.

The `watchers` is an array of file watchers. When changing config file, the dev command will be restarted and those watchers will be closed. If you are adding new watchers in this hook, you should push your watchers to the `watchers` array, so that they can be closed correctly when restarting.

The `restart` is a method to restart the dev command. When calling this method, the `watchers` array will be closed automatically.

### [onGenerated](https://vuepress.vuejs.org/reference/plugin-api#ongenerated)

*   Type: `(app: App) => void | Promise<void>`

*   Details:

This hook will be invoked once VuePress app has generated static files.

[Prev Built-in Components](https://vuepress.vuejs.org/reference/components)[Next Theme API](https://vuepress.vuejs.org/reference/theme-api)
