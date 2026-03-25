# Source: https://hexo.io/docs/setup

Title: Setup

URL Source: https://hexo.io/docs/setup

Published Time: 2026-03-12T00:23:04.147Z

Markdown Content:
Once Hexo is installed, run the following commands to initialize Hexo in the target `<folder>`.

$ hexo init <folder>

$ cd <folder>

$ npm install

Once initialized, here’s what your project folder will look like:

.

├── _config.yml

├── package.json

├── scaffolds

├── source

| ├── _drafts

| └── _posts

└── themes

### [](https://hexo.io/docs/setup#config-yml "_config.yml")_config.yml

Site [configuration](https://hexo.io/docs/configuration) file. You can configure most settings here.

### [](https://hexo.io/docs/setup#package-json "package.json")package.json

Application data. The [EJS](https://ejs.co/), [Stylus](http://learnboost.github.io/stylus/) and [Markdown](http://daringfireball.net/projects/markdown/) renderers are installed by default. If you want, you can uninstall them later.

package.json

{

 "name": "hexo-site",

 "version": "0.0.0",

 "private": true,

 "hexo": {

 "version": ""

 },

 "dependencies": {

 "hexo": "^7.0.0",

 "hexo-generator-archive": "^2.0.0",

 "hexo-generator-category": "^2.0.0",

 "hexo-generator-index": "^3.0.0",

 "hexo-generator-tag": "^2.0.0",

 "hexo-renderer-ejs": "^2.0.0",

 "hexo-renderer-stylus": "^3.0.0",

 "hexo-renderer-marked": "^6.0.0",

 "hexo-server": "^3.0.0",

 "hexo-theme-landscape": "^1.0.0"

 }

}

### [](https://hexo.io/docs/setup#scaffolds "scaffolds")scaffolds

[Scaffold](https://hexo.io/docs/writing#Scaffolds) folder. When you create a new post, Hexo bases the new file on the scaffold.

### [](https://hexo.io/docs/setup#source "source")source

Source folder. This is where you put your site’s content. Hexo ignores hidden files and files or folders whose names are prefixed with `_` (underscore) - except the `_posts` folder. Renderable files (e.g. Markdown, HTML) will be processed and put into the `public` folder, while other files will simply be copied.

### [](https://hexo.io/docs/setup#themes "themes")themes

[Theme](https://hexo.io/docs/themes) folder. Hexo generates a static website by combining the site contents with the theme.
