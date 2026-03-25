# Source: https://metalsmith.io/

Title: Metalsmith

URL Source: https://metalsmith.io/

Markdown Content:
Convenient
----------

Metalsmith works with all the tools and data formats you already know and use: NodeJS, npm, markdown, json, yaml and the templating language of your choice.

Simple
------

Metalsmith translates a directory tree to plain Javascript objects that you can manipulate effortlessly with your selection of plugins.

Pluggable
---------

You shouldn't have to bend your project needs to a specific framework or tool. Metalsmith gives you full control of how you want to conceptualize, structure and build your project.

Versatile
---------

Use Metalsmith to generate anything from a static site, to a scaffolder, backup, command-line, or deploy tool. Configuration over code or code over configuration: Metalsmith supports both.

* * *

Install it
----------

```
npm install metalsmith
```

```
yarn add metalsmith
```

```
pnpm add metalsmith
```

### Or use [a starter](https://metalsmith.io/#use-a-starter)

* * *

Get the feel of it
------------------

### You want to build a website or blog with a static site generator. Well, here is our elevator pitch. It's as easy as that:

`metalsmith.mjs`
```
import { fileURLToPath } from 'node:url'
import { dirname } from 'node:path'
import Metalsmith from 'metalsmith'
import collections from '@metalsmith/collections'
import layouts from '@metalsmith/layouts'
import markdown from '@metalsmith/markdown'
import permalinks from '@metalsmith/permalinks'

const __dirname = dirname(fileURLToPath(import.meta.url))
const t1 = performance.now()

Metalsmith(__dirname)         // parent directory of this file
  .source('./src')            // source directory
  .destination('./build')     // destination directory
  .clean(true)                // clean destination before
  .ignore('.*')               // ignore dotfiles?
  .statik(['assets','CNAME']) // copy static files without processing
  .env({                      // pass NODE_ENV & other environment variables
    DEBUG: process.env.DEBUG,
    NODE_ENV: process.env.NODE_ENV
  })           
  .metadata({                 // add any variable you want & use them in layout-files
    sitename: "My Static Site & Blog",
    siteurl: "https://example.com/",
    description: "It's about saying »Hello« to the world.",
    generatorname: "Metalsmith",
    generatorurl: "https://metalsmith.io/"
  })
  .use(collections({          // group all blog posts by internally
    posts: 'posts/*.md'       // adding key 'collections':'posts'
  }))                         // use `collections.posts` in layouts
  .use(markdown())            // transpile all md into html
  .use(permalinks())          // change URLs to permalink URLs
  .use(layouts({              // wrap layouts around html
    transformer: 'jstransformer-nunjucks',
    pattern: '**/*.html'
  }))
  .build((err) => {           // build process
    if (err) throw err        // error handling is required
    console.log(`Build success in ${((performance.now() - t1) / 1000).toFixed(1)}s`)
  });
```
`metalsmith.cjs`
```
const Metalsmith  = require('metalsmith')
const collections = require('@metalsmith/collections')
const layouts     = require('@metalsmith/layouts')
const markdown    = require('@metalsmith/markdown')
const permalinks  = require('@metalsmith/permalinks')

const t1 = performance.now()

Metalsmith(__dirname)         // parent directory of this file
  .source('./src')            // source directory
  .destination('./build')     // destination directory
  .clean(true)                // clean destination before
  .ignore('.*')               // ignore dotfiles?
  .statik(['assets','CNAME']) // copy static files without processing
  .env({                      // pass NODE_ENV & other environment variables
    DEBUG: process.env.DEBUG,
    NODE_ENV: process.env.NODE_ENV
  })           
  .metadata({                 // add any variable you want & use them in layout-files
    sitename: "My Static Site & Blog",
    siteurl: "https://example.com/",
    description: "It's about saying »Hello« to the world.",
    generatorname: "Metalsmith",
    generatorurl: "https://metalsmith.io/"
  })
  .use(collections({          // group all blog posts by internally
    posts: 'posts/*.md'       // adding key 'collections':'posts'
  }))                         // use `collections.posts` in layouts
  .use(markdown())            // transpile all md into html
  .use(permalinks())          // change URLs to permalink URLs
  .use(layouts({              // wrap layouts around html
    transformer: 'jstransformer-nunjucks',
    pattern: '**/*.html'
  }))
  .build((err) => {           // build process
    if (err) throw err        // error handling is required
    console.log(`Build success in ${((performance.now() - t1) / 1000).toFixed(1)}s`)
  })
```
`metalsmith.json`
```
{
  "source": "src",
  "destination": "build",
  "clean": true,
  "ignore": ".*",
  "statik": ["assets","CNAME"],
  "env": {
    "DEBUG": "$DEBUG",
    "NODE_ENV": "$NODE_ENV"
  },
  "metadata": {
    "sitename": "My Static Site & Blog",
    "siteurl": "https://example.com/",
    "description": "It's about saying »Hello« to the world.",
    "generatorname": "Metalsmith",
    "generatorurl": "https://metalsmith.io/"
  },
  "plugins": [
    { "@metalsmith/collections": { "posts": "posts/*.md" }},
    { "@metalsmith/markdown": {}},
    { "@metalsmith/permalinks": {}},
    { "@metalsmith/layouts": {}},
  ]
}
```

The package exposes both a [JavaScript API](https://metalsmith.io/api), and a [CLI](https://github.com/metalsmith/metalsmith#cli) if you prefer. To see how they're used check out the [examples](https://github.com/metalsmith/metalsmith/tree/master/examples) or [the walkthrough](https://metalsmith.io/step-by-step).

[You can follow along with a detailed walkthrough](https://metalsmith.io/step-by-step) or have a go with a very minimal example:

```
git clone https://github.com/metalsmith/metalsmith.git
cd metalsmith/examples/static-site
npm install
npm start
```

* * *

Build anything
--------------

We mainly refer to Metalsmith as a "static site generator", but it's a lot more than that. Since everything is a plugin, the core library is just an abstraction for manipulating a directory of files.

Which means you could just as easily use it to make...

*   A Project Scaffolder
--------------------

    1.   Read template files from a directory.
    2.   Parse files for template placeholders.
    3.   Prompt user to fill in each placeholder.
    4.   Render files with a templating engine.
    5.   Write filled-in files to a new directory.

*   A Build Tool
------------

    1.   Read files from a source directory.
    2.   Convert Sass files to CSS.
    3.   Concatenate CSS files.
    4.   Minify the CSS file.
    5.   Compress images files.
    6.   Sprite images in a certain folder.
    7.   Write files to a public directory.

*   An eBook Generator
------------------

    1.   Read chapter files from a directory.
    2.   Build a table of contents from the tree.
    3.   Convert Markdown to HTML.
    4.   Convert Markdown to PDF.
    5.   Convert Markdown to ePUB.
    6.   Convert Markdown to MOBI.
    7.   Write compiled files to a directory.

*   Technical Docs
--------------

    1.   Read files from a source directory.
    2.   Convert Markdown files to HTML.
    3.   Build a navigation from the tree.
    4.   Render each file with a template.
    5.   Write HTML to the static directory.

* * *

Deploy anywhere
---------------

### Metalsmith builds are static folders. They can be compressed, archived, deployed to a CDN, Netlify, Github Pages, Gitlab Pages, SFTP'd to a shared host, or SSH'd to a custom server.

* * *

Showcase
--------

### Built with Metalsmith

* * *

Use a starter
-------------

*   ![Image 1: metalsmith/startbootstrap-clean-blog](https://metalsmith.io/img/starter/startbootstrap-clean-blog.png)
metalsmith/startbootstrap-clean-blog

[Code](https://github.com/metalsmith/startbootstrap-clean-blog)|[Demo](https://startbootstrap.github.io/startbootstrap-clean-blog/)

```
git clone https://github.com/metalsmith/startbootstrap-clean-blog
cd startbootstrap-clean-blog && npm install
```
*   ![Image 2: wernerglinka/metalsmith-bare-bones-starter](https://metalsmith.io/img/starter/bare-bones-starter.png)
wernerglinka/metalsmith-bare-bones-starter

[Code](https://github.com/wernerglinka/metalsmith-bare-bones-starter)|[Demo](https://metalsmith-bare-bones-starter.netlify.app/)

```
git clone https://github.com/wernerglinka/metalsmith-bare-bones-starter
cd metalsmith-bare-bones-starter && npm install
```
*   ![Image 3: wernerglinka/metalsmith-blog-starter](https://metalsmith.io/img/starter/blog-starter.png)
wernerglinka/metalsmith-blog-starter

[Code](https://github.com/wernerglinka/metalsmith-blog-starter)|[Demo](https://metalsmith-blog-starter.netlify.app/)

```
git clone https://github.com/wernerglinka/metalsmith-blog-starter
cd metalsmith-blog-starter && npm install
```
*   ![Image 4: wernerglinka/metalsmith-company-starter](https://metalsmith.io/img/starter/company-starter.png)
wernerglinka/metalsmith-company-starter

[Code](https://github.com/wernerglinka/metalsmith-company-starter)|[Demo](https://metalsmith-company-starter.netlify.app/)

```
git clone https://github.com/wernerglinka/metalsmith-company-starter
cd metalsmith-company-starter && npm install
```
*   ![Image 5: webketje/metalsmith-starter-resume](https://metalsmith.io/img/starter/resume-starter.png)
webketje/metalsmith-starter-resume

[Code](https://github.com/webketje/metalsmith-starter-resume)

```
git clone https://github.com/webketje/metalsmith-starter-resume
cd metalsmith-starter-resume && npm install
```

* * *
