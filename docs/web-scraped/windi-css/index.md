# Source: https://windicss.org/

Title: Windi CSS

URL Source: https://windicss.org/

Markdown Content:
Home | Windi CSS
===============

[![Image 1: Windi CSS logo](https://windicss.org/assets/logo.svg) Windi CSS](https://windicss.org/)

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

![Image 2: Windi CSS logo](https://windicss.org/assets/logo.svg)

Windi CSS
=========

Next generation utility-first CSS framework.

[Get Started](https://windicss.org/guide/)[Learn More](https://windicss.org/features/)

Special Sponsor
---------------

[](https://opencollective.com/nuxtjs)

Sponsors
--------

[![Image 3: suzukey](https://opencollective-production.s3.us-west-1.amazonaws.com/14278ec0-86ed-11eb-a6dc-d564e871483a.png)](https://opencollective.com/suzukey)[Eagle Logistics](https://opencollective.com/eagle-logistics)[![Image 4: Zentered](https://opencollective-production.s3.us-west-1.amazonaws.com/account-avatar/bc5a09ff-fc37-43ee-a77f-29c0d1a781b2/57e1e256-11c6-4bc2-ae16-75779ad24d22.png)](https://opencollective.com/zentered)[![Image 5: OwN, inc.](https://opencollective-production.s3.us-west-1.amazonaws.com/62df0850-8d86-11eb-98af-ed2f1f397415.png)](https://opencollective.com/own)[![Image 6: Codeperate Limited](https://opencollective-production.s3.us-west-1.amazonaws.com/992d72a0-b8c6-11eb-a750-e3fa0f99718c.png)](https://opencollective.com/codeperate-limited)[![Image 7: Paulo Vieira](https://www.gravatar.com/avatar/72c2bcb1ce13d34e81a2acd7b359dbe6?default=404)](https://opencollective.com/paulo-vieira)[![Image 8: Adrian Jefferson Olape](https://opencollective-production.s3.us-west-1.amazonaws.com/94d3ae00-c351-11eb-9d7e-03ca7793adce.jpg)](https://opencollective.com/adrian-jefferson)[![Image 9: Alexander Niebuhr](https://opencollective-production.s3.us-west-1.amazonaws.com/4b01a110-acb8-11eb-a574-2b311951a382.jpg)](https://opencollective.com/alexanderniebuhr)[黄泽辉](https://opencollective.com/guest-705c1455)[![Image 10: MasonZZ](https://opencollective-production.s3.us-west-1.amazonaws.com/f1ef8490-4837-11ec-ba0e-af901d736f4a.jpg)](https://opencollective.com/user-c4227434)[![Image 11: Fajar Firmansyah](https://opencollective-production.s3.us-west-1.amazonaws.com/13b5ae90-2819-11ec-b895-2dd6efbf5fd0.png)](https://opencollective.com/fajar-firmansyah)[Michael](https://opencollective.com/michael81)[![Image 12: Emils Gulbis](https://opencollective-production.s3.us-west-1.amazonaws.com/de8d4570-862e-11eb-854a-6d64d8a87195.jpeg)](https://opencollective.com/emils-gulbis)[Nándor](https://opencollective.com/nandor-dudas)[![Image 13: GoMage](https://opencollective-production.s3.us-west-1.amazonaws.com/account-avatar/81975804-9c1a-4b7a-b4cd-cd518d784c2b/d30cf901-e52b-4197-96bd-be849350ea47.png)](https://opencollective.com/gomage)

 Become a sponsor on [Open Collective](https://opencollective.com/windicss)

​x

bg-gradient-to-r from-green-400 to-blue-500 text-white text-center italic px-4 py-2 rounded cursor-default transition-all duration-400 hover:rounded-2xl dark:(from-teal-400 to-yellow-500)

Config

}

CSS

interpret

.bg-gradient-to-r {
  background-image: -o-linear-gradient(left, var(--tw-gradient-stops));
  background-image: -webkit-gradient(linear, left top, right top, from(var(--tw-gradient-stops)));
  background-image: linear-gradient(to right, var(--tw-gradient-stops));
}
.from-green-400 {
  --tw-gradient-from: rgba(52, 211, 153, var(--tw-from-opacity, 1));
  --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to, rgba(255, 255, 255, 0));
}
.dark .dark\:from-teal-400 {
  --tw-gradient-from: rgba(45, 212, 191, var(--tw-from-opacity, 1));
  --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to, rgba(255, 255, 255, 0));
}
.to-blue-500 {
  --tw-gradient-to: rgba(59, 130, 246, var(--tw-to-opacity, 1));
}
.dark .dark\:to-yellow-500 {
  --tw-gradient-to: rgba(245, 158, 11, var(--tw-to-opacity, 1));
}
.rounded {
  border-radius: 0.25rem;
}
.hover\:rounded-2xl:hover {
  border-radius: 1rem;
}
.cursor-default {
  cursor: default;
}
.px-4 {
  padding-left: 1rem;
  padding-right: 1rem;
}
.py-2 {
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
}
.text-center {
  text-align: center;
}
.text-white {
  --tw-text-opacity: 1;
  color: rgba(255, 255, 255, var(--tw-text-opacity));
}
.italic {
  font-style: italic;
}
.transition-all {
  -webkit-transition-property: all;
  -o-transition-property: all;
  transition-property: all;
  -webkit-transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  -o-transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  -webkit-transition-duration: 150ms;
  -o-transition-duration: 150ms;
  transition-duration: 150ms;
}
.duration-400 {
  -webkit-transition-duration: 400ms;
  -o-transition-duration: 400ms;
  transition-duration: 400ms;
}

[![Image 14: Deploys by Netlify](https://windicss.org/assets/netlify.svg)](https://www.netlify.com/)

MIT Licensed | Copyright © 2020-2021 Windi CSS Contributors

[Windi CSS is Sunsetting We recommend new projects to consider alternatives. Click for more information.](https://windicss.org/posts/sunsetting)
