# Source: https://windicss.org/features/variant-groups

Title: Windi CSS

URL Source: https://windicss.org/features/variant-groups

Markdown Content:
Variant Groups | Windi CSS
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

Variant Groups [#](https://windicss.org/features/variant-groups#variant-groups)
===============================================================================

Apply utilities for the same variant by grouping them with a parenthesis.

```html
<div class="hover:(bg-gray-400 font-medium) bg-white font-light"/>
```

Play with it:

​x

bg-blue-200 font-light p-2 hover:(bg-gray-400 font-medium)

Config

{}

CSS

interpret

.bg-blue-200 {
  --tw-bg-opacity: 1;
  background-color: rgba(191, 219, 254, var(--tw-bg-opacity));
}
.hover\:bg-gray-400:hover {
  --tw-bg-opacity: 1;
  background-color: rgba(156, 163, 175, var(--tw-bg-opacity));
}
.font-light {
  font-weight: 300;
}
.hover\:font-medium:hover {
  font-weight: 500;
}
.p-2 {
  padding: 0.5rem;
}

[Suggest changes to this page](https://github.com/windicss/docs/edit/main/features/variant-groups.md)

[Value Auto-infer](https://windicss.org/features/value-auto-infer)

[Shortcuts](https://windicss.org/features/shortcuts)

[Windi CSS is Sunsetting We recommend new projects to consider alternatives. Click for more information.](https://windicss.org/posts/sunsetting)
