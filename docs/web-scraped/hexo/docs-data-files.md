# Source: https://hexo.io/docs/data-files

Title: Data Files

URL Source: https://hexo.io/docs/data-files

Published Time: 2026-03-12T00:23:04.147Z

Markdown Content:
Data Files | Hexo
===============

[Hexo](https://hexo.io/)
========================

[Docs](https://hexo.io/docs/)[API](https://hexo.io/api/)[News](https://hexo.io/news/)[Plugins](https://hexo.io/plugins/)[Themes](https://hexo.io/themes/)[About](https://hexo.io/about/)[](https://github.com/hexojs/hexo)

Search K

English

[](https://hexo.io/docs/data-files)

Data Files
==========

[](https://github.com/hexojs/site/edit/master/source/docs/data-files.md "Improve this doc")

Sometimes you may need to use some data in templates which is not directly available in your posts, or you want to reuse the data elsewhere. For such use cases, Hexo 3 introduced the new **Data files**. This feature loads YAML or JSON files in `source/_data` folder so you can use them in your site.

For example, add `menu.yml` in `source/_data` folder.

Home: /

Gallery: /gallery/

Archives: /archives/

And you can use them in templates:

<% for (var link in site.data.menu) { %>

 <a href="<%= site.data.menu[link] %>"> <%= link %> </a>

<% } %>

render like this :

<a href="/"> Home </a>

<a href="/gallery/"> Gallery </a>

<a href="/archives/"> Archives </a>

Last updated: 2026-03-12[Prev](https://hexo.io/docs/asset-folders "Asset Folders")[Next](https://hexo.io/docs/server "Server")

**Contents**[Back to Top](https://hexo.io/docs/data-files#)

**Getting Started**[Overview](https://hexo.io/docs/)[Setup](https://hexo.io/docs/setup)[Configuration](https://hexo.io/docs/configuration)[Commands](https://hexo.io/docs/commands)[Migration](https://hexo.io/docs/migration)**Basic Usage**[Writing](https://hexo.io/docs/writing)[Front-matter](https://hexo.io/docs/front-matter)[Tag Plugins](https://hexo.io/docs/tag-plugins)[Asset Folders](https://hexo.io/docs/asset-folders)[Data Files](https://hexo.io/docs/data-files)[Server](https://hexo.io/docs/server)[Generating](https://hexo.io/docs/generating)**Deployment**[GitHub Pages](https://hexo.io/docs/github-pages)[GitLab Pages](https://hexo.io/docs/gitlab-pages)[One-Command Deployment](https://hexo.io/docs/one-command-deployment)**Customization**[Permalinks](https://hexo.io/docs/permalinks)[Themes](https://hexo.io/docs/themes)[Templates](https://hexo.io/docs/templates)[Variables](https://hexo.io/docs/variables)[Helpers](https://hexo.io/docs/helpers)[Internationalization (i18n)](https://hexo.io/docs/internationalization)[Syntax Highlight](https://hexo.io/docs/syntax-highlight)[Plugins](https://hexo.io/docs/plugins)**Miscellaneous**[Troubleshooting](https://hexo.io/docs/troubleshooting)[Contributing](https://hexo.io/docs/contributing)

 © 2026 [Hexo](https://github.com/hexojs/hexo/graphs/contributors)

 Documentation licensed under [CC BY 4.0](http://creativecommons.org/licenses/by/4.0/).

[![Image 1](https://www.netlify.com/img/global/badges/netlify-dark.svg)](https://www.netlify.com/)[](https://twitter.com/hexojs)[](https://github.com/hexojs/hexo)

[Docs](https://hexo.io/docs/)[API](https://hexo.io/api/)[News](https://hexo.io/news/)[Plugins](https://hexo.io/plugins/)[Themes](https://hexo.io/themes/)[About](https://hexo.io/about/)*   [GitHub](https://github.com/hexojs/hexo)

**Getting Started**[Overview](https://hexo.io/docs/)[Setup](https://hexo.io/docs/setup)[Configuration](https://hexo.io/docs/configuration)[Commands](https://hexo.io/docs/commands)[Migration](https://hexo.io/docs/migration)**Basic Usage**[Writing](https://hexo.io/docs/writing)[Front-matter](https://hexo.io/docs/front-matter)[Tag Plugins](https://hexo.io/docs/tag-plugins)[Asset Folders](https://hexo.io/docs/asset-folders)[Data Files](https://hexo.io/docs/data-files)[Server](https://hexo.io/docs/server)[Generating](https://hexo.io/docs/generating)**Deployment**[GitHub Pages](https://hexo.io/docs/github-pages)[GitLab Pages](https://hexo.io/docs/gitlab-pages)[One-Command Deployment](https://hexo.io/docs/one-command-deployment)**Customization**[Permalinks](https://hexo.io/docs/permalinks)[Themes](https://hexo.io/docs/themes)[Templates](https://hexo.io/docs/templates)[Variables](https://hexo.io/docs/variables)[Helpers](https://hexo.io/docs/helpers)[Internationalization (i18n)](https://hexo.io/docs/internationalization)[Syntax Highlight](https://hexo.io/docs/syntax-highlight)[Plugins](https://hexo.io/docs/plugins)**Miscellaneous**[Troubleshooting](https://hexo.io/docs/troubleshooting)[Contributing](https://hexo.io/docs/contributing)

English
