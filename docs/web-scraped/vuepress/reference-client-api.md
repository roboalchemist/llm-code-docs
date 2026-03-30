# Source: https://vuepress.vuejs.org/reference/client-api

Title: Client API

URL Source: https://vuepress.vuejs.org/reference/client-api

Markdown Content:
Client API can be imported from `vuepress/client`.

[Composition API](https://vuepress.vuejs.org/reference/client-api#composition-api)
----------------------------------------------------------------------------------

### [useClientData](https://vuepress.vuejs.org/reference/client-api#useclientdata)

*   Details:

Returns all the client data ref objects.

Each property can also be accessed by the following composition APIs.

*   Example:

```
<script setup lang="ts">
import { useClientData } from 'vuepress/client'

const {
  pageData,
  pageFrontmatter,
  pageHead,
  pageHeadTitle,
  pageLang,
  routeLocale,
  siteData,
  siteLocaleData,
} = useClientData()
</script>
```

### [usePageData](https://vuepress.vuejs.org/reference/client-api#usepagedata)

*   Details:

Returns the page data ref object of current page.

*   Also see:

    *   [Node API > Page Properties > data](https://vuepress.vuejs.org/reference/node-api#data)
    *   [Plugin API > extendsPage](https://vuepress.vuejs.org/reference/plugin-api#extendspage)

### [usePageFrontmatter](https://vuepress.vuejs.org/reference/client-api#usepagefrontmatter)

*   Details:

Returns the frontmatter ref object of current page.

The value is the `frontmatter` property of the page data.

### [usePageHead](https://vuepress.vuejs.org/reference/client-api#usepagehead)

*   Details:

Returns the head config ref object of current page.

The value is obtained by merging and deduplicating [head](https://vuepress.vuejs.org/reference/frontmatter#head) frontmatter and [head](https://vuepress.vuejs.org/reference/config#head) config.

### [usePageHeadTitle](https://vuepress.vuejs.org/reference/client-api#usepageheadtitle)

*   Details:

Returns the head title ref object of current page.

The value is obtained by joining the page title and site title.

### [usePageLang](https://vuepress.vuejs.org/reference/client-api#usepagelang)

*   Details:

Returns the language ref object of current page.

The value is the `lang` property of the page data.

### [useRoutes](https://vuepress.vuejs.org/reference/client-api#useroutes)

*   Details:

Returns the routes ref object.

The value is the `routes` property of the site data.

*   Also see:

    *   [Advanced > Cookbook > Resolving Routes](https://vuepress.vuejs.org/advanced/cookbook/resolving-routes)

### [useRouteLocale](https://vuepress.vuejs.org/reference/client-api#useroutelocale)

*   Details:

Returns the locale path ref object of current route.

The value is one of the keys of the [locales](https://vuepress.vuejs.org/reference/config#locales) config.

### [useSiteData](https://vuepress.vuejs.org/reference/client-api#usesitedata)

*   Details:

Returns the site data ref object.

### [useSiteLocaleData](https://vuepress.vuejs.org/reference/client-api#usesitelocaledata)

*   Details:

Returns the site data ref object of current locale.

The properties of current locale have been merged into the root-level properties.

### [onContentUpdated](https://vuepress.vuejs.org/reference/client-api#oncontentupdated)

*   Details:

When the content of the markdown file changes, the callback is triggered.

This function can only be called during the `setup` phase of the component.

```
<script setup>
import { onContentUpdated } from 'vuepress/client'

onContentUpdated((reason) => {
  console.log(`content updated reason: ${reason}`)
})
</script>
``` 

[Helpers](https://vuepress.vuejs.org/reference/client-api#helpers)
------------------------------------------------------------------

### [defineClientConfig](https://vuepress.vuejs.org/reference/client-api#defineclientconfig)

*   Details:

Helper for creating [clientConfigFile](https://vuepress.vuejs.org/reference/plugin-api#clientconfigfile).

*   Also see:

    *   [Advanced > Cookbook > Usage of Client Config](https://vuepress.vuejs.org/advanced/cookbook/usage-of-client-config)

### [resolveRoute](https://vuepress.vuejs.org/reference/client-api#resolveroute)

*   Details:

Parses the route of the given link.

*   Also see:

    *   [Advanced > Cookbook > Resolving Routes](https://vuepress.vuejs.org/advanced/cookbook/resolving-routes)

### [resolveRoutePath](https://vuepress.vuejs.org/reference/client-api#resolveroutepath)

*   Details:

Parses the route path of the given link.

*   Also see:

    *   [Advanced > Cookbook > Resolving Routes](https://vuepress.vuejs.org/advanced/cookbook/resolving-routes)

### [withBase](https://vuepress.vuejs.org/reference/client-api#withbase)

*   Details:

Prefix URL with site [base](https://vuepress.vuejs.org/reference/config#base).

*   Also see:

    *   [Guide > Assets > Base Helper](https://vuepress.vuejs.org/guide/assets#base-helper)

[Constants](https://vuepress.vuejs.org/reference/client-api#constants)
----------------------------------------------------------------------

There are some constants that available in the client side code.

To shim the types of these constants in client side code, add `vuepress/client-types` to your `tsconfig.json`:

```
{
  "compilerOptions": {
    "types": ["vuepress/client-types"]
  }
}
```

### [`__VUEPRESS_VERSION__`](https://vuepress.vuejs.org/reference/client-api#vuepress-version)

*   Type: `string`

*   Details:

Version of VuePress core package.

### [`__VUEPRESS_BASE__`](https://vuepress.vuejs.org/reference/client-api#vuepress-base)

*   Type: `string`

*   Details:

The [base](https://vuepress.vuejs.org/reference/config#base) option from config.

### [`__VUEPRESS_DEV__`](https://vuepress.vuejs.org/reference/client-api#vuepress-dev)

*   Type: `boolean`

*   Details:

An environment flag indicating whether it is currently running in `dev` mode.

### [`__VUEPRESS_SSR__`](https://vuepress.vuejs.org/reference/client-api#vuepress-ssr)

*   Type: `boolean`

*   Details:

An environment flag indicating whether it is currently running in server-side-rendering (SSR) build.

[Advanced](https://vuepress.vuejs.org/reference/client-api#advanced)
--------------------------------------------------------------------

### [resolvers experimental](https://vuepress.vuejs.org/reference/client-api#resolvers)

*   Type: `Record<string, Function>`

*   Details:

An reactive object, methods of which determining how to resolve global computed.

*   Example:

Customizing the format of `<title>` in client config file:

```
import { defineClientConfig, resolvers } from 'vuepress/client'

export default defineClientConfig({
  enhance({ app, router, siteData }) {
    resolvers.resolvePageHeadTitle = (page, siteLocale) =>
      `${siteLocale.title} > ${page.title}`
  },
})
```

Caution

`resolvers` will affect the basic functionality of VuePress. Please make sure you have fully understood its purpose before modifying it.

[Prev Theme API](https://vuepress.vuejs.org/reference/theme-api)[Next Node API](https://vuepress.vuejs.org/reference/node-api)
