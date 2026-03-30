# Source: https://vuepress.vuejs.org/guide/getting-started

Title: Getting Started

URL Source: https://vuepress.vuejs.org/guide/getting-started

Markdown Content:
Warning

VuePress v2 is currently in RC (Release Candidate) stage. It's ready to be used for building your site, but the config and API are not stable enough, which is possibly to have minor breaking changes. So make sure to read the [changelog](https://github.com/vuepress/core/blob/main/CHANGELOG.md) carefully each time you upgrade a RC version.

[Try It Online](https://vuepress.vuejs.org/guide/getting-started#try-it-online)
-------------------------------------------------------------------------------

You can try VuePress directly in your browser on [StackBlitz](https://stackblitz.com/fork/vuepress).

[Installation](https://vuepress.vuejs.org/guide/getting-started#installation)
-----------------------------------------------------------------------------

### [Prerequisites](https://vuepress.vuejs.org/guide/getting-started#prerequisites)

*   [Node.js v20.9.0+](https://nodejs.org/)
*   Package manager like [pnpm](https://pnpm.io/), [yarn](https://classic.yarnpkg.com/en/), [npm](https://www.npmjs.com/), etc.

Tips

*   When using [pnpm](https://pnpm.io/), you need to install `vue` as peer-dependencies.
*   When using [yarn 2+](https://yarnpkg.com/), you need to set `nodeLinker: 'node-modules'` in your [`.yarnrc.yml`](https://yarnpkg.com/configuration/yarnrc#nodeLinker) file.

### [Project Setup](https://vuepress.vuejs.org/guide/getting-started#project-setup)

#### [Setup via CLI](https://vuepress.vuejs.org/guide/getting-started#setup-via-cli)

You can use [create-vuepress](https://www.npmjs.com/package/create-vuepress) to generate a template directly.

pnpm

`pnpm create vuepress vuepress-starter`

yarn

`yarn create vuepress vuepress-starter`

npm

`npm init vuepress vuepress-starter`

#### [Setup Manually](https://vuepress.vuejs.org/guide/getting-started#setup-manually)

This section will help you build a basic VuePress documentation site from ground up.

*   Create and change into a new directory

```
mkdir vuepress-starter
cd vuepress-starter
```

*   Initialize your project

pnpm

```
git init
pnpm init
```

yarn

```
git init
yarn init
```

npm

```
git init
npm init
```

*   Install VuePress

pnpm

```
# install vuepress and vue
pnpm add -D vuepress@next vue
# install bundler and theme
pnpm add -D @vuepress/bundler-vite@next @vuepress/theme-default@next
```

yarn

```
# install vuepress
yarn add -D vuepress@next
# install bundler and theme
yarn add -D @vuepress/bundler-vite@next @vuepress/theme-default@next
```

npm

```
# install vuepress
npm install -D vuepress@next
# install bundler and theme
npm install -D @vuepress/bundler-vite@next @vuepress/theme-default@next
```

*   Create `docs` directory and `docs/.vuepress` directory

```
mkdir docs
mkdir docs/.vuepress
```

*   Create the VuePress config file `docs/.vuepress/config.js`

```
import { viteBundler } from '@vuepress/bundler-vite'
import { defaultTheme } from '@vuepress/theme-default'
import { defineUserConfig } from 'vuepress'

export default defineUserConfig({
  bundler: viteBundler(),
  theme: defaultTheme(),
})
```

*   Create your first document

`echo '# Hello VuePress' > docs/README.md`

[Directory Structure](https://vuepress.vuejs.org/guide/getting-started#directory-structure)
-------------------------------------------------------------------------------------------

After the setup, the minimal structure of your project should look like this:

```
├─ docs
│  ├─ .vuepress
│  │  └─ config.js
│  └─ README.md
└─ package.json
```

The `docs` directory is where you put your markdown files, and it will be used as the source directory of VuePress.

The `docs/.vuepress` directory, i.e. the `.vuepress` directory in the source directory, is where all VuePress-specific files will be placed. Currently there is only one config file in it. By default, the temp, cache and output directory will also be generated inside this directory. It is suggested to add them to your `.gitignore` file.

Example `.gitignore` file

```
# VuePress default temp directory
.vuepress/.temp
# VuePress default cache directory
.vuepress/.cache
# VuePress default build output directory
.vuepress/dist
```

[Work with VuePress](https://vuepress.vuejs.org/guide/getting-started#work-with-vuepress)
-----------------------------------------------------------------------------------------

### [Start Dev Server](https://vuepress.vuejs.org/guide/getting-started#start-dev-server)

You can add some [scripts](https://classic.yarnpkg.com/en/docs/package-json#toc-scripts) to `package.json`:

```
{
  "scripts": {
    "docs:dev": "vuepress dev docs",
    "docs:build": "vuepress build docs"
  }
}
```

Then, run `docs:dev` script to start the dev server:

pnpm

`pnpm docs:dev`

yarn

`yarn docs:dev`

npm

`npm run docs:dev`

VuePress will start a hot-reloading development server at [http://localhost:8080](http://localhost:8080/). When you modify your markdown files, the content in the browser will be auto updated.

### [Build Your Site](https://vuepress.vuejs.org/guide/getting-started#build-your-site)

To build your site, run `docs:build` script:

pnpm

`pnpm docs:build`

yarn

`yarn docs:build`

npm

`npm run docs:build`

You will see the generated static files in the `docs/.vuepress/dist` directory. You can check out [deployment](https://vuepress.vuejs.org/guide/deployment) for how to deploy them.

[Learn More about VuePress](https://vuepress.vuejs.org/guide/getting-started#learn-more-about-vuepress)
-------------------------------------------------------------------------------------------------------

By now, you should have a basic but functional VuePress site. But you may still need to read the subsequent guide to learn more about VuePress.

Next step, learn more about the [configuration](https://vuepress.vuejs.org/guide/configuration).

[Prev Introduction](https://vuepress.vuejs.org/guide/introduction)[Next Configuration](https://vuepress.vuejs.org/guide/configuration)
