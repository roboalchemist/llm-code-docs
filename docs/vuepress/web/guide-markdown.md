# Source: https://vuepress.vuejs.org/guide/markdown

Title: Markdown

URL Source: https://vuepress.vuejs.org/guide/markdown

Markdown Content:
Make sure you already know Markdown well before reading this section. If not, please learn some [Markdown tutorials](https://commonmark.org/help/) first.

[Syntax Extensions](https://vuepress.vuejs.org/guide/markdown#syntax-extensions)
--------------------------------------------------------------------------------

The Markdown content in VuePress will be parsed by [markdown-it](https://github.com/markdown-it/markdown-it), which supports [syntax extensions](https://github.com/markdown-it/markdown-it#syntax-extensions) via markdown-it plugins.

This section will introduce built-in Markdown syntax extensions of VuePress.

You can also configure those built-in extensions, load more markdown-it plugins and implement your own extensions via [markdown](https://vuepress.vuejs.org/reference/config#markdown) option and [extendsMarkdown](https://vuepress.vuejs.org/reference/plugin-api#extendsmarkdown) option.

### [Embedded](https://vuepress.vuejs.org/guide/markdown#embedded)

Embedded by markdown-it:

*   [Tables](https://help.github.com/articles/organizing-information-with-tables/) (GFM)
*   [Strikethrough](https://help.github.com/articles/basic-writing-and-formatting-syntax/#styling-text) (GFM)

You might have noticed that, a `#` anchor is displayed when you hover the mouse on the headers of each section. By clicking the `#` anchor, you can jump to the section directly.

### [Links](https://vuepress.vuejs.org/guide/markdown#links)

When using Markdown [link syntax](https://spec.commonmark.org/0.29/#link-reference-definitions), VuePress will implement some conversions for you.

Take our documentation source files as an example:

```
└─ docs
   ├─ guide
   │  ├─ getting-started.md
   │  ├─ introduction.md
   │  └─ markdown.md    # <- Here we are
   ├─ reference
   │  └─ config.md
   └─ README.md
```

**Raw Markdown**

```
<!-- relative path -->

[Home](../README.md)  
[Config Reference](../reference/config.md)  
[Getting Started](./getting-started.md)

<!-- absolute path -->

[Guide > Introduction](/guide/introduction.md)  
[Config Reference > markdown.links](/reference/config.md#links)

<!-- URL -->

[GitHub](https://github.com)
```

**Converted to**

```
<template>
  <RouteLink to="/">Home</RouteLink>
  <RouteLink to="/reference/config.html">Config Reference</RouteLink>
  <RouteLink to="/guide/getting-started.html">Getting Started</RouteLink>
  <RouteLink to="/guide/introduction.html">Guide &gt; Introduction</RouteLink>
  <RouteLink to="/reference/config.html#links">
    Config Reference &gt; markdown.links
  </RouteLink>
  <a href="https://github.com" target="_blank" rel="noopener noreferrer">
    GitHub
  </a>
</template>
```

**Rendered as**

[Home](https://vuepress.vuejs.org/)

[Config Reference](https://vuepress.vuejs.org/reference/config)

[Getting Started](https://vuepress.vuejs.org/guide/getting-started)

[Guide > Introduction](https://vuepress.vuejs.org/guide/introduction)

[Config Reference > markdown.links](https://vuepress.vuejs.org/reference/config#links)

[GitHub](https://github.com/)

**Explanation**

*   Internal links will be converted to [RouteLink](https://vuepress.vuejs.org/reference/components#routelink) for SPA navigation.
*   Internal links to `.md` files will be converted to the [page route path](https://vuepress.vuejs.org/guide/page#routing), and both absolute path and relative path are supported.
*   External links will get `target="_blank" rel="noopener noreferrer"` attrs.

**Suggestion**

Try to use relative paths instead of absolute paths for internal links to markdown files.

*   Relative paths are a valid links to the target files, and they can navigate correctly when browsing the source files in your editor or repository.
*   Relative paths are consistent in different locales, so you don't need to change the locale path when translating your content.

Tips

This links extension is supported by our built-in plugin.

Config reference: [markdown.links](https://vuepress.vuejs.org/reference/config#markdown-links)

### [Emoji 🎉](https://vuepress.vuejs.org/guide/markdown#emoji)

You can add emoji to your Markdown content by typing `:EMOJICODE:`.

For a full list of available emoji and codes, check out [emoji-cheat-sheet](https://github.com/ikatyang/emoji-cheat-sheet).

**Input**

`VuePress 2 is out :tada: !`

**Output**

VuePress 2 is out 🎉 !

### [Table of Contents](https://vuepress.vuejs.org/guide/markdown#table-of-contents)

If you want to put the table of contents (TOC) of your current page inside your Markdown content, you can use the `[[toc]]` syntax.

**Input**

`[[toc]]`

**Output**

*   [Syntax Extensions](https://vuepress.vuejs.org/guide/markdown#syntax-extensions)
    *   [Embedded](https://vuepress.vuejs.org/guide/markdown#embedded)
    *   [Header Anchors](https://vuepress.vuejs.org/guide/markdown#header-anchors)
    *   [Links](https://vuepress.vuejs.org/guide/markdown#links)
    *   [Emoji 🎉](https://vuepress.vuejs.org/guide/markdown#emoji)
    *   [Table of Contents](https://vuepress.vuejs.org/guide/markdown#table-of-contents)
    *   [Code Blocks](https://vuepress.vuejs.org/guide/markdown#code-blocks)
    *   [Import Code Blocks](https://vuepress.vuejs.org/guide/markdown#import-code-blocks)

*   [Using Vue in Markdown](https://vuepress.vuejs.org/guide/markdown#using-vue-in-markdown)
    *   [Template Syntax](https://vuepress.vuejs.org/guide/markdown#template-syntax)
    *   [Components](https://vuepress.vuejs.org/guide/markdown#components)

*   [Markdown Plugins](https://vuepress.vuejs.org/guide/markdown#markdown-plugins)
*   [Cautions](https://vuepress.vuejs.org/guide/markdown#cautions)
    *   [Non-Standard HTML Tags](https://vuepress.vuejs.org/guide/markdown#non-standard-html-tags)

The headers in TOC will link to the corresponding [header anchors](https://vuepress.vuejs.org/guide/markdown#header-anchors), so TOC won't work well if you disable header anchors.

### [Code Blocks](https://vuepress.vuejs.org/guide/markdown#code-blocks)

Following code blocks extensions are implemented during markdown parsing in Node side. That means, the code blocks won't be processed in client side.

With [@vuepress/plugin-prismjs](https://ecosystem.vuejs.press/plugins/markdown/prismjs.html) and [@vuepress/plugin-shiki](https://ecosystem.vuejs.press/plugins/markdown/shiki.html), you can highlight code blocks with [Prism](https://prismjs.com/) or [Shiki](https://shiki.style/).

#### [Code Title](https://vuepress.vuejs.org/guide/markdown#code-title)

You can specify the title of the code block by adding a `title` key-value mark in your fenced code blocks.

**Input**

```
```ts title=".vuepress/config.ts"
import { defaultTheme } from '@vuepress/theme-default'
import { defineUserConfig } from 'vuepress'

export default defineUserConfig({
  title: 'Hello, VuePress',

  theme: defaultTheme({
    logo: 'https://vuejs.org/images/logo.png',
  }),
})
```
```

**Output**

.vuepress/config.ts

```
import { defaultTheme } from '@vuepress/theme-default'
import { defineUserConfig } from 'vuepress'

export default defineUserConfig({
  title: 'Hello, VuePress',

  theme: defaultTheme({
    logo: 'https://vuejs.org/images/logo.png',
  }),
})
```

Tips

Code title is supported by highlight plugins by default. It can be used in combination with the other marks below. Please leave a space between them.

#### [Line Highlighting](https://vuepress.vuejs.org/guide/markdown#line-highlighting)

You can highlight specified lines of your code blocks by adding line ranges mark in your fenced code blocks.

**Input**

```
```ts{1,7-9}
import { defaultTheme } from '@vuepress/theme-default'
import { defineUserConfig } from 'vuepress'

export default defineUserConfig({
  title: 'Hello, VuePress',

  theme: defaultTheme({
    logo: 'https://vuejs.org/images/logo.png',
  }),
})
```
```

**Output**

```
import { defaultTheme } from '@vuepress/theme-default'
import { defineUserConfig } from 'vuepress'

export default defineUserConfig({
  title: 'Hello, VuePress',

  theme: defaultTheme({
    logo: 'https://vuejs.org/images/logo.png',
  }),
})
```

Examples for line ranges mark:

*   Line ranges: `{5-8}`
*   Multiple single lines: `{4,7,9}`
*   Combined: `{4,7-13,16,23-27,40}`

#### [Line Numbers](https://vuepress.vuejs.org/guide/markdown#line-numbers)

You must have noticed that the number of lines is displayed on the left side of code blocks.

You can add `:line-numbers` / `:no-line-numbers` mark in your fenced code blocks to override the value set in config.

**Input**

```
```ts
// line-numbers is enabled by default
const line2 = 'This is line 2'
const line3 = 'This is line 3'
```

```ts:no-line-numbers
// line-numbers is disabled
const line2 = 'This is line 2'
const line3 = 'This is line 3'
```
```

**Output**

```
// line-numbers is enabled by default
const line2 = 'This is line 2'
const line3 = 'This is line 3'
```

```
// line-numbers is disabled
const line2 = 'This is line 2'
const line3 = 'This is line 3'
```

#### [Wrap with v-pre](https://vuepress.vuejs.org/guide/markdown#wrap-with-v-pre)

As [template syntax is allowed in Markdown](https://vuepress.vuejs.org/guide/markdown#template-syntax), it would also work in code blocks, too.

To avoid your code blocks being compiled by Vue, VuePress will add [v-pre](https://vuejs.org/api/built-in-directives.html#v-pre) directive to your code blocks by default, which can be disabled in config.

You can add `:v-pre` / `:no-v-pre` mark in your fenced code blocks to override the value set in config.

Warning

The template syntax characters, for example, the "Mustache" syntax (double curly braces) might be parsed by the syntax highlighter. Thus, as the following example, `:no-v-pre` might not work well in some languages.

If you want to make Vue syntax work in those languages anyway, try to disable the default syntax highlighting and implement your own syntax highlighting in client side.

**Input**

```
```md
<!-- This will be kept as is by default -->

1 + 2 + 3 = {{ 1 + 2 + 3 }}
```

```md:no-v-pre
<!-- This will be compiled by Vue -->

1 + 2 + 3 = {{ 1 + 2 + 3 }}
```

```js:no-v-pre
// This won't be compiled correctly because of js syntax highlighting
const onePlusTwoPlusThree = {{ 1 + 2 + 3 }}
```
```

**Output**

```
<!-- This will be kept as is -->

1 + 2 + 3 = {{ 1 + 2 + 3 }}
```

```
<!-- This will be compiled by Vue -->

1 + 2 + 3 = {{ 1 + 2 + 3 }}
```

```
// This won't be compiled correctly because of js syntax highlighting
const onePlusTwoPlusThree = {{ 1 + 2 + 3 }}
```

Tips

This v-pre extension is supported by our built-in plugin.

Config reference: [markdown.vPre.block](https://vuepress.vuejs.org/reference/config#markdown-vpre-block)

### [Import Code Blocks](https://vuepress.vuejs.org/guide/markdown#import-code-blocks)

You can import code blocks from files with following syntax:

```
<!-- minimal syntax -->

@[code](../foo.js)
```

If you want to partially import the file:

```
<!-- partial import, from line 1 to line 10 -->

@[code{1-10}](../foo.js)
```

The code language is inferred from the file extension, while it is recommended to specify it explicitly:

```
<!-- specify the code language -->

@[code js](../foo.js)
```

In fact, the second part inside the `[]` will be treated as the mark of the code fence, so it supports all the syntax mentioned in the above [Code Blocks](https://vuepress.vuejs.org/guide/markdown#code-blocks) section:

```
<!-- line highlighting -->

@[code js{2,4-5}](../foo.js)
```

Here is a complex example:

*   import line 3 to line 10 of the `'../foo.js'` file
*   specify the language as `'js'`
*   highlight line 3 of the imported code, i.e. line 5 of the `'../foo.js'` file
*   disable line numbers

`@[code{3-10} js{3}:no-line-numbers](../foo.js)`

Notice that path aliases are not available in import code syntax. You can use following config to handle path alias yourself:

```
import { getDirname, path } from 'vuepress/utils'

const __dirname = getDirname(import.meta.url)

export default {
  markdown: {
    importCode: {
      handleImportPath: (str) =>
        str.replace(/^@src/, path.resolve(__dirname, 'path/to/src')),
    },
  },
}
```

```
<!-- it will be resolved to 'path/to/src/foo.js' -->

@[code](@src/foo.js)
```

Tips

This import code extension is supported by our built-in plugin.

Config reference: [markdown.importCode](https://vuepress.vuejs.org/reference/config#markdown-importcode)

[Using Vue in Markdown](https://vuepress.vuejs.org/guide/markdown#using-vue-in-markdown)
----------------------------------------------------------------------------------------

This section will introduce some basic usage of Vue in Markdown.

Check out [Cookbook > Markdown and Vue SFC](https://vuepress.vuejs.org/advanced/cookbook/markdown-and-vue-sfc) for more details.

### [Template Syntax](https://vuepress.vuejs.org/guide/markdown#template-syntax)

As we know:

*   HTML is allowed in Markdown.
*   Vue template syntax is compatible with HTML.

That means, [Vue template syntax](https://vuejs.org/guide/essentials/template-syntax.html) is allowed in Markdown.

**Input**

```
One plus one equals: {{ 1 + 1 }}

<span v-for="i in 3"> span: {{ i }} </span>
```

**Output**

One plus one equals: 2

span: 1 span: 2 span: 3

### [Components](https://vuepress.vuejs.org/guide/markdown#components)

You can use Vue components directly in Markdown.

**Input**

`This is default theme built-in `<Badge />` component <Badge text="demo" />`

**Output**

This is default theme built-in `<Badge />` component demo

[Markdown Plugins](https://vuepress.vuejs.org/guide/markdown#markdown-plugins)
------------------------------------------------------------------------------

You can explore more markdown plugins at [VuePress Marketplace](https://marketplace.vuejs.press/plugins/markdown.html).

[Cautions](https://vuepress.vuejs.org/guide/markdown#cautions)
--------------------------------------------------------------

### [Non-Standard HTML Tags](https://vuepress.vuejs.org/guide/markdown#non-standard-html-tags)

Non-standard HTML tags would not be recognized as native HTML tags by Vue template compiler. Instead, Vue will try to resolve those tags as Vue components, and obviously these components usually don't exist. For example:

*   Deprecated HTML tags such as [<center>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/center) and [<font>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/font).
*   [MathML tags](https://developer.mozilla.org/en-US/docs/Web/MathML), which might be used by some markdown-it LaTeX plugin.

If you want to use those tags anyway, try either of the following workarounds:

*   Adding a [v-pre](https://vuejs.org/api/built-in-directives.html#v-pre) directive to skip the compilation of the element and its children. Notice that the template syntax would also be invalid.
*   Using [compilerOptions.isCustomElement](https://vuejs.org/api/application.html#app-config-compileroptions) to tell Vue template compiler not try to resolve them as components. 
    *   For `@vuepress/bundler-webpack`, set [vue.compilerOptions](https://vuepress.vuejs.org/reference/bundler/webpack#vue)
    *   For `@vuepress/bundler-vite`, set [vuePluginOptions.template.compilerOptions](https://vuepress.vuejs.org/reference/bundler/vite#vuepluginoptions)
