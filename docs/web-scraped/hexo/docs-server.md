# Source: https://hexo.io/docs/server

Title: Server

URL Source: https://hexo.io/docs/server

Published Time: 2026-03-12T00:23:04.147Z

Markdown Content:
Server | Hexo
===============

[Hexo](https://hexo.io/)
========================

[Docs](https://hexo.io/docs/)[API](https://hexo.io/api/)[News](https://hexo.io/news/)[Plugins](https://hexo.io/plugins/)[Themes](https://hexo.io/themes/)[About](https://hexo.io/about/)[](https://github.com/hexojs/hexo)

Search K

English

[](https://hexo.io/docs/server)

Server
======

[](https://github.com/hexojs/site/edit/master/source/docs/server.md "Improve this doc")

[](https://hexo.io/docs/server#hexo-server "hexo-server")[hexo-server](https://github.com/hexojs/hexo-server)[](https://hexo.io/docs/server#hexo-server)
--------------------------------------------------------------------------------------------------------------------------------------------------------

With the release of Hexo 3, the server has been separated from the main module. To start using the server, you will first have to install [hexo-server](https://github.com/hexojs/hexo-server).

$ npm install hexo-server --save

Once the server has been installed, run the following command to start the server. Your website will run at `http://localhost:4000` by default. When the server is running, Hexo will watch for file changes and update automatically so it’s not necessary to manually restart the server.

$ hexo server

If you want to change the port or if you’re encountering `EADDRINUSE` errors, use the `-p` option to set a different port.

$ hexo server -p 5000

### [](https://hexo.io/docs/server#Static-Mode "Static Mode")Static Mode[](https://hexo.io/docs/server#Static-Mode)

In static mode, only files in the `public` folder will be served and file watching is disabled. You have to run `hexo generate` before starting the server. Usually used in production.

$ hexo server -s

### [](https://hexo.io/docs/server#Custom-IP "Custom IP")Custom IP[](https://hexo.io/docs/server#Custom-IP)

Hexo runs the server at `0.0.0.0` by default. You can override the default IP setting.

$ hexo server -i 192.168.1.1

Last updated: 2026-03-12[Prev](https://hexo.io/docs/data-files "Data Files")[Next](https://hexo.io/docs/generating "Generating")

**Contents**

1. [hexo-server](https://hexo.io/docs/server#hexo-server)
    1.   [Static Mode](https://hexo.io/docs/server#Static-Mode)
    2.   [Custom IP](https://hexo.io/docs/server#Custom-IP)

[Back to Top](https://hexo.io/docs/server#)

**Getting Started**[Overview](https://hexo.io/docs/)[Setup](https://hexo.io/docs/setup)[Configuration](https://hexo.io/docs/configuration)[Commands](https://hexo.io/docs/commands)[Migration](https://hexo.io/docs/migration)**Basic Usage**[Writing](https://hexo.io/docs/writing)[Front-matter](https://hexo.io/docs/front-matter)[Tag Plugins](https://hexo.io/docs/tag-plugins)[Asset Folders](https://hexo.io/docs/asset-folders)[Data Files](https://hexo.io/docs/data-files)[Server](https://hexo.io/docs/server)[Generating](https://hexo.io/docs/generating)**Deployment**[GitHub Pages](https://hexo.io/docs/github-pages)[GitLab Pages](https://hexo.io/docs/gitlab-pages)[One-Command Deployment](https://hexo.io/docs/one-command-deployment)**Customization**[Permalinks](https://hexo.io/docs/permalinks)[Themes](https://hexo.io/docs/themes)[Templates](https://hexo.io/docs/templates)[Variables](https://hexo.io/docs/variables)[Helpers](https://hexo.io/docs/helpers)[Internationalization (i18n)](https://hexo.io/docs/internationalization)[Syntax Highlight](https://hexo.io/docs/syntax-highlight)[Plugins](https://hexo.io/docs/plugins)**Miscellaneous**[Troubleshooting](https://hexo.io/docs/troubleshooting)[Contributing](https://hexo.io/docs/contributing)

 © 2026 [Hexo](https://github.com/hexojs/hexo/graphs/contributors)

 Documentation licensed under [CC BY 4.0](http://creativecommons.org/licenses/by/4.0/).

[![Image 1](https://www.netlify.com/img/global/badges/netlify-dark.svg)](https://www.netlify.com/)[](https://twitter.com/hexojs)[](https://github.com/hexojs/hexo)

[Docs](https://hexo.io/docs/)[API](https://hexo.io/api/)[News](https://hexo.io/news/)[Plugins](https://hexo.io/plugins/)[Themes](https://hexo.io/themes/)[About](https://hexo.io/about/)*   [GitHub](https://github.com/hexojs/hexo)

**Getting Started**[Overview](https://hexo.io/docs/)[Setup](https://hexo.io/docs/setup)[Configuration](https://hexo.io/docs/configuration)[Commands](https://hexo.io/docs/commands)[Migration](https://hexo.io/docs/migration)**Basic Usage**[Writing](https://hexo.io/docs/writing)[Front-matter](https://hexo.io/docs/front-matter)[Tag Plugins](https://hexo.io/docs/tag-plugins)[Asset Folders](https://hexo.io/docs/asset-folders)[Data Files](https://hexo.io/docs/data-files)[Server](https://hexo.io/docs/server)[Generating](https://hexo.io/docs/generating)**Deployment**[GitHub Pages](https://hexo.io/docs/github-pages)[GitLab Pages](https://hexo.io/docs/gitlab-pages)[One-Command Deployment](https://hexo.io/docs/one-command-deployment)**Customization**[Permalinks](https://hexo.io/docs/permalinks)[Themes](https://hexo.io/docs/themes)[Templates](https://hexo.io/docs/templates)[Variables](https://hexo.io/docs/variables)[Helpers](https://hexo.io/docs/helpers)[Internationalization (i18n)](https://hexo.io/docs/internationalization)[Syntax Highlight](https://hexo.io/docs/syntax-highlight)[Plugins](https://hexo.io/docs/plugins)**Miscellaneous**[Troubleshooting](https://hexo.io/docs/troubleshooting)[Contributing](https://hexo.io/docs/contributing)

English
