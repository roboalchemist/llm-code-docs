# Source: https://vuepress.vuejs.org/reference/theme-api

Title: Theme API

URL Source: https://vuepress.vuejs.org/reference/theme-api

Markdown Content:
A VuePress theme also works as a plugin, so Theme API can accept all the options of [Plugin API](https://vuepress.vuejs.org/reference/plugin-api) with following differences.

[Basic Options](https://vuepress.vuejs.org/reference/theme-api#basic-options)
-----------------------------------------------------------------------------

### [name](https://vuepress.vuejs.org/reference/theme-api#name)

*   Type: `string`

*   Details:

Name of the theme.

It should follow the naming convention, and ensure consistency with the package name when publishing to NPM:

    *   Non-scoped: `vuepress-theme-foo`
    *   Scoped: `@org/vuepress-theme-foo`

### [multiple](https://vuepress.vuejs.org/reference/theme-api#multiple)

*   Details:

A theme should never be used multiple times, so this option is not supported in theme API.

[Theme Specific Options](https://vuepress.vuejs.org/reference/theme-api#theme-specific-options)
-----------------------------------------------------------------------------------------------

### [extends](https://vuepress.vuejs.org/reference/theme-api#extends)

*   Type: `Theme`

*   Details:

The theme to inherit.

All of the Theme API of the parent theme will be inherited, but the child theme will not override the parent theme directly. Theme specific options will override according to following rules:

    *   [plugins](https://vuepress.vuejs.org/reference/theme-api#plugins): When a same plugin is used in both child and parent theme, if the plugin does not support to be used multiple times, only the one used in the child theme will take effect.
    *   [templateBuild](https://vuepress.vuejs.org/reference/theme-api#templatebuild) / [templateDev](https://vuepress.vuejs.org/reference/theme-api#templatedev): Child theme templates will override parent theme templates.

Multi-level inheritance is supported, i.e. theme B could be extended from theme A, and then theme C could be extended from theme B. In other words, a theme could have a parent theme, a grandparent theme and so on.

*   Example:

```
import { defaultTheme } from '@vuepress/theme-default'
import { getDirname, path } from 'vuepress/utils'

const __dirname = getDirname(import.meta.url)

export default {
  // inherit the default theme
  extends: defaultTheme(),
}
```

### [plugins](https://vuepress.vuejs.org/reference/theme-api#plugins)

*   Type: `(Plugin | Plugin[])[]`

*   Details:

Plugins to use in the theme.

*   Also see:

    *   [Config > plugins](https://vuepress.vuejs.org/reference/config#plugins)

### [templateBuild](https://vuepress.vuejs.org/reference/theme-api#templatebuild)

*   Type: `string`

*   Details:

Specify the path of the HTML template for build.

It would override the default value of [templateBuild](https://vuepress.vuejs.org/reference/config#templatebuild), and could be overridden by user config.

*   Also see:

    *   [Config > templateBuild](https://vuepress.vuejs.org/reference/config#templatebuild)

### [templateBuildRenderer](https://vuepress.vuejs.org/reference/theme-api#templatebuildrenderer)

*   Type: `TemplateRenderer`

*   Details:

Specify the HTML template renderer to be used for build.

It would override the default value of [templateBuildRenderer](https://vuepress.vuejs.org/reference/config#templatebuildrenderer), and could be overridden by user config.

*   Also see:

    *   [Config > templateBuildRenderer](https://vuepress.vuejs.org/reference/config#templatebuildrenderer)

### [templateDev](https://vuepress.vuejs.org/reference/theme-api#templatedev)

*   Type: `string`

*   Details:

Specify the HTML template for dev.

It would override the default value of [templateDev](https://vuepress.vuejs.org/reference/config#templatedev), but could be overridden by user config.

*   Also see:

    *   [Config > templateDev](https://vuepress.vuejs.org/reference/config#templatedev)
