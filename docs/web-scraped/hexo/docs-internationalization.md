# Source: https://hexo.io/docs/internationalization

Title: Internationalization (i18n)

URL Source: https://hexo.io/docs/internationalization

Published Time: 2026-03-12T00:23:04.147Z

Markdown Content:
Internationalization (i18n) | Hexo
===============

[Hexo](https://hexo.io/)
========================

[Docs](https://hexo.io/docs/)[API](https://hexo.io/api/)[News](https://hexo.io/news/)[Plugins](https://hexo.io/plugins/)[Themes](https://hexo.io/themes/)[About](https://hexo.io/about/)[](https://github.com/hexojs/hexo)

Search

English

[](https://hexo.io/docs/internationalization)

Internationalization (i18n)
===========================

[](https://github.com/hexojs/site/edit/master/source/docs/internationalization.md "Improve this doc")

You can use internationalization to present your site in different languages. The default language is set by modifying the `language` setting in `_config.yml`. You can also set multiple languages and modify the order of default languages.

language: zh-tw

language:

- zh-tw

- en

### [](https://hexo.io/docs/internationalization#Language-Files "Language Files")Language Files[](https://hexo.io/docs/internationalization#Language-Files)

Language files can be YAML or JSON files. You should put them into the `languages` folder in the theme. There is support for the [printf format](https://github.com/alexei/sprintf.js) in language files.

### [](https://hexo.io/docs/internationalization#Templates "Templates")Templates[](https://hexo.io/docs/internationalization#Templates)

Use `__` or `_p` helpers in templates to get the translated strings. The former is for normal usage and the latter is for plural strings. For example:

en.yml

index:

 title: Home

 add: Add

 video:

 zero: No videos

 one: One video

 other: %d videos

<%=  __ ('index.title') %>

// Home

<%= _p('index.video', 3) %>

// 3 videos

### [](https://hexo.io/docs/internationalization#Path "Path")Path[](https://hexo.io/docs/internationalization#Path)

You can set the language of pages in front-matter, or modify the `i18n_dir` setting in `_config.yml` to enable automatic detection by Hexo.

i18n_dir: :lang

The default value of `i18n_dir` setting is `:lang`, which means that Hexo will detect the language within the first segment of URL. For example:

/index.html => en

/archives/index.html => en

/zh-tw/index.html => zh-tw

The string will only be served as a language when the language file exists. So `archives` in `/archives/index.html` (example 2) will not get served as a language.

Last updated: 2026-03-12[Prev](https://hexo.io/docs/helpers "Helpers")[Next](https://hexo.io/docs/syntax-highlight "Syntax Highlight")

**Contents**

1. [Language Files](https://hexo.io/docs/internationalization#Language-Files)
2. [Templates](https://hexo.io/docs/internationalization#Templates)
3. [Path](https://hexo.io/docs/internationalization#Path)

[Back to Top](https://hexo.io/docs/internationalization#)

**Getting Started**[Overview](https://hexo.io/docs/)[Setup](https://hexo.io/docs/setup)[Configuration](https://hexo.io/docs/configuration)[Commands](https://hexo.io/docs/commands)[Migration](https://hexo.io/docs/migration)**Basic Usage**[Writing](https://hexo.io/docs/writing)[Front-matter](https://hexo.io/docs/front-matter)[Tag Plugins](https://hexo.io/docs/tag-plugins)[Asset Folders](https://hexo.io/docs/asset-folders)[Data Files](https://hexo.io/docs/data-files)[Server](https://hexo.io/docs/server)[Generating](https://hexo.io/docs/generating)**Deployment**[GitHub Pages](https://hexo.io/docs/github-pages)[GitLab Pages](https://hexo.io/docs/gitlab-pages)[One-Command Deployment](https://hexo.io/docs/one-command-deployment)**Customization**[Permalinks](https://hexo.io/docs/permalinks)[Themes](https://hexo.io/docs/themes)[Templates](https://hexo.io/docs/templates)[Variables](https://hexo.io/docs/variables)[Helpers](https://hexo.io/docs/helpers)[Internationalization (i18n)](https://hexo.io/docs/internationalization)[Syntax Highlight](https://hexo.io/docs/syntax-highlight)[Plugins](https://hexo.io/docs/plugins)**Miscellaneous**[Troubleshooting](https://hexo.io/docs/troubleshooting)[Contributing](https://hexo.io/docs/contributing)

 © 2026 [Hexo](https://github.com/hexojs/hexo/graphs/contributors)

 Documentation licensed under [CC BY 4.0](http://creativecommons.org/licenses/by/4.0/).

[![Image 1](https://www.netlify.com/img/global/badges/netlify-dark.svg)](https://www.netlify.com/)[](https://twitter.com/hexojs)[](https://github.com/hexojs/hexo)

[Docs](https://hexo.io/docs/)[API](https://hexo.io/api/)[News](https://hexo.io/news/)[Plugins](https://hexo.io/plugins/)[Themes](https://hexo.io/themes/)[About](https://hexo.io/about/)*   [GitHub](https://github.com/hexojs/hexo)

**Getting Started**[Overview](https://hexo.io/docs/)[Setup](https://hexo.io/docs/setup)[Configuration](https://hexo.io/docs/configuration)[Commands](https://hexo.io/docs/commands)[Migration](https://hexo.io/docs/migration)**Basic Usage**[Writing](https://hexo.io/docs/writing)[Front-matter](https://hexo.io/docs/front-matter)[Tag Plugins](https://hexo.io/docs/tag-plugins)[Asset Folders](https://hexo.io/docs/asset-folders)[Data Files](https://hexo.io/docs/data-files)[Server](https://hexo.io/docs/server)[Generating](https://hexo.io/docs/generating)**Deployment**[GitHub Pages](https://hexo.io/docs/github-pages)[GitLab Pages](https://hexo.io/docs/gitlab-pages)[One-Command Deployment](https://hexo.io/docs/one-command-deployment)**Customization**[Permalinks](https://hexo.io/docs/permalinks)[Themes](https://hexo.io/docs/themes)[Templates](https://hexo.io/docs/templates)[Variables](https://hexo.io/docs/variables)[Helpers](https://hexo.io/docs/helpers)[Internationalization (i18n)](https://hexo.io/docs/internationalization)[Syntax Highlight](https://hexo.io/docs/syntax-highlight)[Plugins](https://hexo.io/docs/plugins)**Miscellaneous**[Troubleshooting](https://hexo.io/docs/troubleshooting)[Contributing](https://hexo.io/docs/contributing)

English
