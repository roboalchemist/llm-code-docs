# Source: https://vuepress.vuejs.org/advanced/theme

Title: Writing a Theme

URL Source: https://vuepress.vuejs.org/advanced/theme

Markdown Content:
Tips

Before reading this guide, you'd better learn the guide of [Writing a Plugin](https://vuepress.vuejs.org/advanced/plugin) first.

[Create a Theme](https://vuepress.vuejs.org/advanced/theme#create-a-theme)
--------------------------------------------------------------------------

A VuePress theme is a special plugin, which should satisfy the [Theme API](https://vuepress.vuejs.org/reference/theme-api). Like plugins, a theme should also be a _Theme Object_ or a _Theme Function_, and could be wrapped with a function to receive options:

```
import { getDirname, path } from 'vuepress/utils'

const __dirname = getDirname(import.meta.url)

const fooTheme = (options) =>
  // returns a theme object
  ({
    name: 'vuepress-theme-foo',

    // path to the client config of your theme
    clientConfigFile: path.resolve(__dirname, 'client.js'),

    // set custom dev / build template
    // if the template is not specified, the default template
    templateBuild: path.resolve(__dirname, 'templates/build.html'),
    templateDev: path.resolve(__dirname, 'templates/dev.html'),

    // use plugins
    plugins: [
      // ...
    ],

    // other plugin APIs are also available
  })

const barTheme =
  (options) =>
  // returns a theme function
  (app) => ({
    name: 'vuepress-theme-bar',
    // ...
  })
```

Then, create theme's client config file `client.js` :

```
import { defineClientConfig } from 'vuepress/client'
import Layout from './layouts/Layout.vue'
import NotFound from './layouts/NotFound.vue'

export default defineClientConfig({
  layouts: {
    Layout,
    NotFound,
  },
})
```

The `layouts` field declares the layouts provided by your theme. A theme must provide at least two layouts: `Layout` and `NotFound`. The former is to provide default layout for common pages, while the latter is to provide layout for 404-not-found page.

The `Layout` layout should contain the [Content](https://vuepress.vuejs.org/reference/components#content) component to display the markdown content:

```
<template>
  <div>
    <Content />
  </div>
</template>
```

The `NotFound` layout will be used for the `404.html` page:

```
<template>
  <div>404 Not Found</div>
</template>
```

You can provide more layouts, and users can change layout via [layout](https://vuepress.vuejs.org/reference/frontmatter#layout) frontmatter.

[Publish to NPM](https://vuepress.vuejs.org/advanced/theme#publish-to-npm)
--------------------------------------------------------------------------

Also, there are some conventions for theme in [package.json](https://docs.npmjs.com/cli/v8/configuring-npm/package-json):

```
{
  "name": "vuepress-theme-foo",
  "keywords": ["vuepress-theme"]
}
```

*   Set `name` to follow the naming convention: `vuepress-theme-xxx` or `@org/vuepress-theme-xxx`, which should be consistent with the [name](https://vuepress.vuejs.org/reference/theme-api#name) field of the _Theme Object_.
*   Set `keywords` to include `vuepress-theme`, so that users can search your theme on NPM.
