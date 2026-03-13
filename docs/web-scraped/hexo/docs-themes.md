# Source: https://hexo.io/docs/themes

Title: Themes

URL Source: https://hexo.io/docs/themes

Published Time: 2026-03-12T00:23:04.147Z

Markdown Content:
[](https://github.com/hexojs/site/edit/master/source/docs/themes.md "Improve this doc")

It’s easy to build a Hexo theme - you just have to create a new folder. To start using your theme, modify the `theme` setting in your site’s `_config.yml`. A theme should have the following structure:

.

├── _config.yml

├── languages

├── layout

├── scripts

└── source

### [](https://hexo.io/docs/themes#config-yml "_config.yml")_config.yml

Theme configuration file. Unlike the site’s primary configuration file, modifying this doesn’t require a server restart.

### [](https://hexo.io/docs/themes#languages "languages")languages

Language folder. See [internationalization (i18n)](https://hexo.io/docs/internationalization) for more info.

### [](https://hexo.io/docs/themes#layout "layout")layout

Layout folder. This folder contains the theme’s template files, which define the appearance of your website. Hexo provides the [Nunjucks](https://mozilla.github.io/nunjucks/) template engine by default, but you can easily install additional plugins to support alternative engines such as [EJS](https://github.com/hexojs/hexo-renderer-ejs) or [Pug](https://github.com/hexojs/hexo-renderer-pug). Hexo chooses the template engine based on the file extension of the template (just like the posts). For example:

layout.ejs - uses EJS

layout.njk - uses Nunjucks

See [templates](https://hexo.io/docs/templates) for more info.

### [](https://hexo.io/docs/themes#scripts "scripts")scripts

Script folder. Hexo will automatically load all JavaScript files in this folder during initialization. For more info, see [plugins](https://hexo.io/docs/plugins).

### [](https://hexo.io/docs/themes#source "source")source

Source folder. Place your assets (e.g. CSS and JavaScript files) here. Hexo ignores hidden files and files or folders prefixed with `_` (underscore).

Hexo will process and save all renderable files to the `public` folder. Non-renderable files will be copied to the `public` folder directly.

### [](https://hexo.io/docs/themes#Publishing "Publishing")Publishing

When you have finished building your theme, you can publish it to the [theme list](https://hexo.io/themes). Before doing so, you should run the [theme unit test](https://github.com/hexojs/hexo-theme-unit-test) to ensure that everything works. The steps for publishing a theme are very similar to those for [updating documentation](https://hexo.io/docs/contributing#Updating_Documentation).

1. Fork [hexojs/site](https://github.com/hexojs/site)

2. Clone the repository to your computer and install dependencies.

$ git clone https://github.com/<username>/site.git

$ cd site

$ npm install
3.   Create a new yaml file in `source/_data/themes/`, use your theme name as the file name

1. Edit `source/_data/themes/<your-theme-name>.yml` and add your theme. For example:

description: A brand new default theme for Hexo.

link: https://github.com/hexojs/hexo-theme-landscape

preview: http://hexo.io/hexo-theme-landscape

tags:

- official

- responsive

- widget

- two_column

- one_column
1. Add a screenshot (with the same name as the theme) to `source/themes/screenshots`. It must be a 800*500px PNG.

2. Push the branch.

3. Create a pull request and describe the change.
