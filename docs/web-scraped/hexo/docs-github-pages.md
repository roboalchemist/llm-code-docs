# Source: https://hexo.io/docs/github-pages

Title: GitHub Pages

URL Source: https://hexo.io/docs/github-pages

Published Time: 2026-03-12T00:23:04.147Z

Markdown Content:
GitHub Pages | Hexo
===============

[Hexo](https://hexo.io/)
========================

[Docs](https://hexo.io/docs/)[API](https://hexo.io/api/)[News](https://hexo.io/news/)[Plugins](https://hexo.io/plugins/)[Themes](https://hexo.io/themes/)[About](https://hexo.io/about/)[](https://github.com/hexojs/hexo)

English

[](https://hexo.io/docs/github-pages)

GitHub Pages
============

[](https://github.com/hexojs/site/edit/master/source/docs/github-pages.md "Improve this doc")

In this tutorial, we use [GitHub Actions](https://docs.github.com/en/actions) to deploy GitHub Pages. It works in both public and private repositories. Skip to the [One-command deployment](https://hexo.io/docs/github-pages#One-command-deployment) section if you prefer not to upload your source folder to GitHub.

1. Create a repo named **_username_.github.io**, where username is your username on GitHub. If you have already uploaded to another repo, rename the repo instead.
2. Push the files of your Hexo folder to the default branch of your repository. The default branch is usually **main**, older repositories may use **master** branch.

* To push `main` branch to GitHub:

$ git push -u origin main

* The `public/` folder is not (and should not be) uploaded by default, make sure the `.gitignore` file contains `public/` line. The folder structure should be roughly similar to [this repo](https://github.com/hexojs/hexo-starter).

1. Check what version of Node.js you are using on your local machine with `node --version`. Make a note of the major version (e.g., `v20.y.z`)
2. In your GitHub repo’s setting, navigate to **Settings**>**Pages**>**Source**. Change the source to **GitHub Actions** and save.
3. Create `.github/workflows/pages.yml` in your repo with the following contents (substituting `20` to the major version of Node.js that you noted in previous step):

.github/workflows/pages.yml

name: Pages

on:

 push:

 branches:

* main # default branch

jobs:

 build:

 runs-on: ubuntu-latest

 steps:

* uses: actions/checkout@v4

 with:

 token: ${{ secrets.GITHUB_TOKEN }}

# If your repository depends on submodule, please see: https://github.com/actions/checkout

 submodules: recursive

* name: Use Node.js 20

 uses: actions/setup-node@v4

 with:

# Examples: 20, 18.19, >=16.20.2, lts/Iron, lts/Hydrogen, *, latest, current, node

# Ref: https://github.com/actions/setup-node#supported-version-syntax

 node-version: "20"

* name: Cache NPM dependencies

 uses: actions/cache@v4

 with:

 path: node_modules

 key: ${{ runner.OS }}-npm-cache

 restore-keys: |

 ${{ runner.OS }}-npm-cache

* name: Install Dependencies

 run: npm install

* name: Build

 run: npm run build

* name: Upload Pages artifact

 uses: actions/upload-pages-artifact@v3

 with:

 path: ./public

 deploy:

 needs: build

 permissions:

 pages: write

 id-token: write

 environment:

 name: github-pages

 url: ${{ steps.deployment.outputs.page_url }}

 runs-on: ubuntu-latest

 steps:

* name: Deploy to GitHub Pages

 id: deployment

 uses: actions/deploy-pages@v4

1. Once the deployment is finished, check the webpage at _username_.github.io.

Note - if you specify a custom domain name with a `CNAME`, you need to add the `CNAME` file to the `source/` folder. [More info](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site).

[](https://hexo.io/docs/github-pages#Project-page "Project page")Project page[](https://hexo.io/docs/github-pages#Project-page)
-------------------------------------------------------------------------------------------------------------------------------

If you prefer to have a project page on GitHub:

1. Navigate to your repo on GitHub. Go to the **Settings** tab. Change the **Repository name** so your blog is available at **username.github.io/_repository_**, **repository** can be any name, like _blog_ or _hexo_.
2. Edit your **_config.yml**, change the `url:` value to **https://_username_.github.io/_repository_**.
3. In your GitHub repo’s setting, navigate to **Settings**>**Pages**>**Source**. Change the source to **GitHub Actions** and save.
4. Commit and push to the default branch.
5. Once the deployment is finished, check the webpage at _username_.github.io/_repository_.

[](https://hexo.io/docs/github-pages#One-command-deployment "One-command deployment")One-command deployment[](https://hexo.io/docs/github-pages#One-command-deployment)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

The following instruction is adapted from [one-command deployment](https://hexo.io/docs/one-command-deployment) page.

1. Install [hexo-deployer-git](https://github.com/hexojs/hexo-deployer-git).
2. Add the following configurations to **_config.yml**, (remove existing lines if any).

deploy:

 type: git

 repo: https://github.com/<username>/<project>

# example, https://github.com/hexojs/hexojs.github.io

 branch: gh-pages

1. Run `hexo clean && hexo deploy`.
2. Check the webpage at _username_.github.io.

[](https://hexo.io/docs/github-pages#Useful-links "Useful links")Useful links[](https://hexo.io/docs/github-pages#Useful-links)
-------------------------------------------------------------------------------------------------------------------------------

* [GitHub Pages](https://docs.github.com/en/pages)
* [Publishing with a custom GitHub Actions workflow](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site#publishing-with-a-custom-github-actions-workflow)
* [actions/deploy-github-pages-site](https://github.com/marketplace/actions/deploy-github-pages-site)

Last updated: 2026-03-12[Prev](https://hexo.io/docs/generating "Generating")[Next](https://hexo.io/docs/gitlab-pages "GitLab Pages")

**Contents**

1. [Project page](https://hexo.io/docs/github-pages#Project-page)
2. [One-command deployment](https://hexo.io/docs/github-pages#One-command-deployment)
3. [Useful links](https://hexo.io/docs/github-pages#Useful-links)

[Back to Top](https://hexo.io/docs/github-pages#)

**Getting Started**[Overview](https://hexo.io/docs/)[Setup](https://hexo.io/docs/setup)[Configuration](https://hexo.io/docs/configuration)[Commands](https://hexo.io/docs/commands)[Migration](https://hexo.io/docs/migration)**Basic Usage**[Writing](https://hexo.io/docs/writing)[Front-matter](https://hexo.io/docs/front-matter)[Tag Plugins](https://hexo.io/docs/tag-plugins)[Asset Folders](https://hexo.io/docs/asset-folders)[Data Files](https://hexo.io/docs/data-files)[Server](https://hexo.io/docs/server)[Generating](https://hexo.io/docs/generating)**Deployment**[GitHub Pages](https://hexo.io/docs/github-pages)[GitLab Pages](https://hexo.io/docs/gitlab-pages)[One-Command Deployment](https://hexo.io/docs/one-command-deployment)**Customization**[Permalinks](https://hexo.io/docs/permalinks)[Themes](https://hexo.io/docs/themes)[Templates](https://hexo.io/docs/templates)[Variables](https://hexo.io/docs/variables)[Helpers](https://hexo.io/docs/helpers)[Internationalization (i18n)](https://hexo.io/docs/internationalization)[Syntax Highlight](https://hexo.io/docs/syntax-highlight)[Plugins](https://hexo.io/docs/plugins)**Miscellaneous**[Troubleshooting](https://hexo.io/docs/troubleshooting)[Contributing](https://hexo.io/docs/contributing)

 © 2026 [Hexo](https://github.com/hexojs/hexo/graphs/contributors)

 Documentation licensed under [CC BY 4.0](http://creativecommons.org/licenses/by/4.0/).

[![Image 1](https://www.netlify.com/img/global/badges/netlify-dark.svg)](https://www.netlify.com/)[](https://twitter.com/hexojs)[](https://github.com/hexojs/hexo)

[Docs](https://hexo.io/docs/)[API](https://hexo.io/api/)[News](https://hexo.io/news/)[Plugins](https://hexo.io/plugins/)[Themes](https://hexo.io/themes/)[About](https://hexo.io/about/)*   [GitHub](https://github.com/hexojs/hexo)

**Getting Started**[Overview](https://hexo.io/docs/)[Setup](https://hexo.io/docs/setup)[Configuration](https://hexo.io/docs/configuration)[Commands](https://hexo.io/docs/commands)[Migration](https://hexo.io/docs/migration)**Basic Usage**[Writing](https://hexo.io/docs/writing)[Front-matter](https://hexo.io/docs/front-matter)[Tag Plugins](https://hexo.io/docs/tag-plugins)[Asset Folders](https://hexo.io/docs/asset-folders)[Data Files](https://hexo.io/docs/data-files)[Server](https://hexo.io/docs/server)[Generating](https://hexo.io/docs/generating)**Deployment**[GitHub Pages](https://hexo.io/docs/github-pages)[GitLab Pages](https://hexo.io/docs/gitlab-pages)[One-Command Deployment](https://hexo.io/docs/one-command-deployment)**Customization**[Permalinks](https://hexo.io/docs/permalinks)[Themes](https://hexo.io/docs/themes)[Templates](https://hexo.io/docs/templates)[Variables](https://hexo.io/docs/variables)[Helpers](https://hexo.io/docs/helpers)[Internationalization (i18n)](https://hexo.io/docs/internationalization)[Syntax Highlight](https://hexo.io/docs/syntax-highlight)[Plugins](https://hexo.io/docs/plugins)**Miscellaneous**[Troubleshooting](https://hexo.io/docs/troubleshooting)[Contributing](https://hexo.io/docs/contributing)

English
