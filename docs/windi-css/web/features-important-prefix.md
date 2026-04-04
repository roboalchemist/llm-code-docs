# Source: https://windicss.org/features/important-prefix

Title: Windi CSS

URL Source: https://windicss.org/features/important-prefix

Markdown Content:
Important Prefix | Windi CSS
===============

[![Image 1: Logo](https://windicss.org/assets/logo.svg) Windi CSS](https://windicss.org/)

Search K

Overview 

Utilities 

Plugins 

Posts 

Community 

[Play](https://windicss.org/play)

[](https://github.com/windicss/windicss)

[](https://github.com/windicss/windicss)

 Overview

 Utilities

 Plugins

 Posts

 Community

[Play](https://windicss.org/play)

*   ##### Guide

    *   [Getting Started](https://windicss.org/guide/)
    *   [Installation](https://windicss.org/guide/installation)
    *   [Configuration](https://windicss.org/guide/configuration)
    *   [Extractions](https://windicss.org/guide/extractions)
    *   [Migration from Tailwind](https://windicss.org/guide/migration)

*   ##### Features

    *   [Overview](https://windicss.org/features/)
    *   [Value Auto-infer](https://windicss.org/features/value-auto-infer)
    *   [Variant Groups](https://windicss.org/features/variant-groups)
    *   [Shortcuts](https://windicss.org/features/shortcuts)
    *   [Responsive Design](https://windicss.org/features/responsive-design)
    *   [Dark Mode](https://windicss.org/features/dark-mode)
    *   [RTL](https://windicss.org/features/rtl)
    *   [Important Prefix](https://windicss.org/features/important-prefix)
    *   [Directives](https://windicss.org/features/directives)
    *   [Attributify Mode](https://windicss.org/features/attributify)
    *   [Visual Analyzer](https://windicss.org/features/analyzer)

*   ##### Integrations

    *   [Vite](https://windicss.org/integrations/vite)
    *   [Webpack](https://windicss.org/integrations/webpack)
    *   [Rollup](https://windicss.org/integrations/rollup)
    *   [Nuxt](https://windicss.org/integrations/nuxt)
    *   [Vue CLI](https://windicss.org/integrations/vue-cli)
    *   [Gridsome](https://windicss.org/integrations/gridsome)
    *   [Svelte](https://windicss.org/integrations/svelte)
    *   [PostCSS](https://windicss.org/integrations/postcss)
    *   [CLI](https://windicss.org/integrations/cli)
    *   [JavaScript API](https://windicss.org/integrations/javascript)
    *   [VS Code](https://windicss.org/editors/vscode)
    *   [WebStorm](https://windicss.org/editors/webstorm)

Important Prefix [#](https://windicss.org/features/important-prefix#important-prefix)
=====================================================================================

You can prefix any utility classes with `!` to set them as `!important`. This could be very useful when you want to override previous styling rules for a specific property.

```css
!text-green-300
```

​x

text-blue-200!text-green-300

Config

{}

CSS

.text-blue-200 {
  --tw-text-opacity: 1;
  color: rgba(191, 219, 254, var(--tw-text-opacity));
}
.\!text-green-300 {
  --tw-text-opacity: 1 !important;
  color: rgba(110, 231, 183, var(--tw-text-opacity)) !important;
}

[Suggest changes to this page](https://github.com/windicss/docs/edit/main/features/important-prefix.md)

[RTL](https://windicss.org/features/rtl)

[Directives](https://windicss.org/features/directives)

[Windi CSS is Sunsetting We recommend new projects to consider alternatives. Click for more information.](https://windicss.org/posts/sunsetting)
