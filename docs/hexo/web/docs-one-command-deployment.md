# Source: https://hexo.io/docs/one-command-deployment

Title: One-Command Deployment

URL Source: https://hexo.io/docs/one-command-deployment

Published Time: 2026-03-12T00:23:04.147Z

Markdown Content:
One-Command Deployment | Hexo
===============

[Hexo](https://hexo.io/)
========================

[Docs](https://hexo.io/docs/)[API](https://hexo.io/api/)[News](https://hexo.io/news/)[Plugins](https://hexo.io/plugins/)[Themes](https://hexo.io/themes/)[About](https://hexo.io/about/)[](https://github.com/hexojs/hexo)

English

[](https://hexo.io/docs/one-command-deployment)

One-Command Deployment
======================

[](https://github.com/hexojs/site/edit/master/source/docs/one-command-deployment.md "Improve this doc")

Hexo provides a fast and easy deployment strategy. You only need one single command to deploy your site to your server.

$ hexo deploy

Install the necessary plugin(s) that is compatible with the deployment method provided by your server/repository.

Deployment is usually configured through **_config.yml**. A valid configuration must have the `type` field. For example:

deploy:

 type: git

You can use multiple deployers. Hexo will execute each deployer in order.

deploy:

- type: git

 repo:

- type: heroku

 repo:

Refer to the [Plugins](https://hexo.io/plugins/) list for more deployment plugins.

[](https://hexo.io/docs/one-command-deployment#Git "Git")Git[](https://hexo.io/docs/one-command-deployment#Git)
---------------------------------------------------------------------------------------------------------------

1. Install [hexo-deployer-git](https://github.com/hexojs/hexo-deployer-git).

$ npm install hexo-deployer-git --save

1. Edit **_config.yml** (with example values shown below as comments):

deploy:

 type: git

 repo: <repository url> # https://bitbucket.org/JohnSmith/johnsmith.bitbucket.io

 branch: [branch]

 message: [message]

| Option | Description | Default |
| --- | --- | --- |
| `repo` | URL of the target repository |  |
| `branch` | Branch name. | `gh-pages` (GitHub) `coding-pages` (Coding.net) `master` (others) |
| `message` | Customize commit message. | `Site updated: {{ now('YYYY-MM-DD HH:mm:ss') }}` |
| `token` | Optional token value to authenticate with the repo. Prefix with `$` to read token from environment variable |  |

1. Deploy your site `hexo clean && hexo deploy`.

- You will be prompted with username and password of the target repository, unless you authenticate with a token or ssh key.
- hexo-deployer-git does not store your username and password. Use [git-credential-cache](https://git-scm.com/docs/git-credential-cache) to store them temporarily.

1. Navigate to your repository settings and change the “Pages” branch to `gh-pages` (or the branch specified in your config). The deployed site should be live on the link shown on the “Pages” setting.

[](https://hexo.io/docs/one-command-deployment#Heroku "Heroku")Heroku[](https://hexo.io/docs/one-command-deployment#Heroku)
---------------------------------------------------------------------------------------------------------------------------

Install [hexo-deployer-heroku](https://github.com/hexojs/hexo-deployer-heroku).

$ npm install hexo-deployer-heroku --save

Edit settings.

deploy:

 type: heroku

 repo: <repository url>

 message: [message]

| Option | Description |
| --- | --- |
| `repo`, `repository` | Heroku repository URL |
| `message` | Customize commit message (Default to `Site updated: {{ now('YYYY-MM-DD HH:mm:ss') }}`) |

[](https://hexo.io/docs/one-command-deployment#Netlify "Netlify")Netlify[](https://hexo.io/docs/one-command-deployment#Netlify)
-------------------------------------------------------------------------------------------------------------------------------

[Netlify](https://www.netlify.com/) provides continuous deployment (Git-triggered builds), an intelligent global CDN, full DNS (including custom domains), automated HTTPS, asset acceleration, and a lot more. It is a unified platform that automates your code to create high-performance, easily maintainable sites and web apps.

There are two different ways to deploy your sites on Netlify. The most common way is to use the web UI. Go to the [create a new site page](https://app.netlify.com/start), select your project repo from GitHub, GitLab, or Bitbucket, and follow the prompts.

Alternatively, you can use Netlify’s [Node based CLI](https://www.netlify.com/docs/cli/) tool to manage and deploy sites on Netlify without leaving your terminal.

You can also add a [Deploy to Netlify Button](https://www.netlify.com/docs/deploy-button/) in your README.file to allow others to create a copy of your repository and be deployed to Netlify via one click.

[](https://hexo.io/docs/one-command-deployment#Rsync "Rsync")Rsync[](https://hexo.io/docs/one-command-deployment#Rsync)
-----------------------------------------------------------------------------------------------------------------------

Install [hexo-deployer-rsync](https://github.com/hexojs/hexo-deployer-rsync).

$ npm install hexo-deployer-rsync --save

Edit settings.

deploy:

 type: rsync

 host: <host>

 user: <user>

 root: <root>

 port: [port]

 delete: [true|false]

 verbose: [true|false]

 ignore_errors: [true|false]

| Option | Description | Default |
| --- | --- | --- |
| `host` | Address of remote host |  |
| `user` | Username |  |
| `root` | Root directory of remote host |  |
| `port` | Port | 22 |
| `delete` | Delete old files on remote host | true |
| `verbose` | Display verbose messages | true |
| `ignore_errors` | Ignore errors | false |

[](https://hexo.io/docs/one-command-deployment#FTPSync "FTPSync")FTPSync[](https://hexo.io/docs/one-command-deployment#FTPSync)
-------------------------------------------------------------------------------------------------------------------------------

Install [hexo-deployer-ftpsync](https://github.com/hexojs/hexo-deployer-ftpsync).

$ npm install hexo-deployer-ftpsync --save

Edit settings.

deploy:

 type: ftpsync

 host: <host>

 user: <user>

 pass: <password>

 remote: [remote]

 port: [port]

 clear: [true|false]

 verbose: [true|false]

| Option | Description | Default |
| --- | --- | --- |
| `host` | Address of remote host |  |
| `user` | Username |  |
| `pass` | Password |  |
| `remote` | Root directory of remote host | `/` |
| `port` | Port | 21 |
| `clear` | Remove all files and directories from the remote directory before upload | false |
| `verbose` | Display verbose messages | false |

[](https://hexo.io/docs/one-command-deployment#SFTP "SFTP")SFTP[](https://hexo.io/docs/one-command-deployment#SFTP)
-------------------------------------------------------------------------------------------------------------------

Install [hexo-deployer-sftp](https://github.com/lucascaro/hexo-deployer-sftp). Deploys the site via SFTP, allowing for passwordless connections using ssh-agent.

$ npm install hexo-deployer-sftp --save

Edit settings.

deploy:

 type: sftp

 host: <host>

 user: <user>

 pass: <password>

 remotePath: [remote path]

 port: [port]

 privateKey: [path/to/privateKey]

 passphrase: [passphrase]

 agent: [path/to/agent/socket]

| Option | Description | Default |
| --- | --- | --- |
| `host` | Address of remote host |  |
| `port` | Port | 22 |
| `user` | Username |  |
| `pass` | Password |  |
| `privateKey` | Path to a ssh private key |  |
| `passphrase` | Optional passphrase for the private key |  |
| `agent` | Path to the ssh-agent socket | `$SSH_AUTH_SOCK` |
| `remotePath` | Root directory of remote host | `/` |
| `forceUpload` | Override existing files | false |
| `concurrency` | Max number of SFTP tasks processed concurrently | 100 |

[](https://hexo.io/docs/one-command-deployment#Vercel "Vercel")Vercel[](https://hexo.io/docs/one-command-deployment#Vercel)
---------------------------------------------------------------------------------------------------------------------------

[Vercel](https://vercel.com/) is a cloud platform that enables developers to host Jamstack websites and web services that deploy instantly, scale automatically, and require no supervision, all with zero configuration. They provide a global edge network, SSL encryption, asset compression, cache invalidation, and more.

Step 1: Add a build script to your `package.json` file:

{

 "scripts": {

 "build": "hexo generate"

 }

}

Step 2: Deploy your Hexo Website to Vercel

To deploy your Hexo app with a [Vercel for Git Integration](https://vercel.com/docs/git-integrations), make sure it has been pushed to a Git repository.

Import the project into Vercel using the [Import Flow](https://vercel.com/import/git). During the import, you will find all relevant options preconfigured for you; however, you can choose to change any of these options, a list of which can be found [here](https://vercel.com/docs/build-step#build-&-development-settings).

After your project has been imported, all subsequent pushes to branches will generate [Preview Deployments](https://vercel.com/docs/platform/deployments#preview), and all changes made to the [Production Branch](https://vercel.com/docs/git-integrations#production-branch) (commonly “main”) will result in a [Production Deployment](https://vercel.com/docs/platform/deployments#production).

Alternatively, you can click the deploy button below to create a new project:

[![Image 1: Deploy Vercel](https://vercel.com/button)](https://vercel.com/new/hexo)

[](https://hexo.io/docs/one-command-deployment#Bip "Bip")Bip[](https://hexo.io/docs/one-command-deployment#Bip)
---------------------------------------------------------------------------------------------------------------

[Bip](https://bip.sh/) is a commercial hosting service that provides zero downtime deployment, a global CDN, SSL, unlimited bandwidth and more for static websites. Plans are available on a pay as you go, per domain basis.

Getting started is quick and easy, as Bip provides out the box support for Hexo. This guide assumes you already have [a Bip domain and Bip CLI installed](https://bip.sh/getstarted).

1: Initialise your project directory

$ bip init

Follow the prompts, where you’ll be asked which domain you’d like to deploy to. Bip will detect that you’re using Hexo, and set project settings like the source file directory automatically.

2: Deploy your website

$ hexo generate —deploy && bip deploy

After a few moments, your website will be deployed.

[](https://hexo.io/docs/one-command-deployment#Other-Methods "Other Methods")Other Methods[](https://hexo.io/docs/one-command-deployment#Other-Methods)
-------------------------------------------------------------------------------------------------------------------------------------------------------

All generated files are saved in the `public` folder. You can copy them to wherever you like.

Last updated: 2026-03-12[Prev](https://hexo.io/docs/gitlab-pages "GitLab Pages")[Next](https://hexo.io/docs/permalinks "Permalinks")

**Contents**

1. [Git](https://hexo.io/docs/one-command-deployment#Git)
2. [Heroku](https://hexo.io/docs/one-command-deployment#Heroku)
3. [Netlify](https://hexo.io/docs/one-command-deployment#Netlify)
4. [Rsync](https://hexo.io/docs/one-command-deployment#Rsync)
5. [FTPSync](https://hexo.io/docs/one-command-deployment#FTPSync)
6. [SFTP](https://hexo.io/docs/one-command-deployment#SFTP)
7. [Vercel](https://hexo.io/docs/one-command-deployment#Vercel)
8. [Bip](https://hexo.io/docs/one-command-deployment#Bip)
9. [Other Methods](https://hexo.io/docs/one-command-deployment#Other-Methods)

[Back to Top](https://hexo.io/docs/one-command-deployment#)

**Getting Started**[Overview](https://hexo.io/docs/)[Setup](https://hexo.io/docs/setup)[Configuration](https://hexo.io/docs/configuration)[Commands](https://hexo.io/docs/commands)[Migration](https://hexo.io/docs/migration)**Basic Usage**[Writing](https://hexo.io/docs/writing)[Front-matter](https://hexo.io/docs/front-matter)[Tag Plugins](https://hexo.io/docs/tag-plugins)[Asset Folders](https://hexo.io/docs/asset-folders)[Data Files](https://hexo.io/docs/data-files)[Server](https://hexo.io/docs/server)[Generating](https://hexo.io/docs/generating)**Deployment**[GitHub Pages](https://hexo.io/docs/github-pages)[GitLab Pages](https://hexo.io/docs/gitlab-pages)[One-Command Deployment](https://hexo.io/docs/one-command-deployment)**Customization**[Permalinks](https://hexo.io/docs/permalinks)[Themes](https://hexo.io/docs/themes)[Templates](https://hexo.io/docs/templates)[Variables](https://hexo.io/docs/variables)[Helpers](https://hexo.io/docs/helpers)[Internationalization (i18n)](https://hexo.io/docs/internationalization)[Syntax Highlight](https://hexo.io/docs/syntax-highlight)[Plugins](https://hexo.io/docs/plugins)**Miscellaneous**[Troubleshooting](https://hexo.io/docs/troubleshooting)[Contributing](https://hexo.io/docs/contributing)

 © 2026 [Hexo](https://github.com/hexojs/hexo/graphs/contributors)

 Documentation licensed under [CC BY 4.0](http://creativecommons.org/licenses/by/4.0/).

[![Image 2](https://www.netlify.com/img/global/badges/netlify-dark.svg)](https://www.netlify.com/)[](https://twitter.com/hexojs)[](https://github.com/hexojs/hexo)

[Docs](https://hexo.io/docs/)[API](https://hexo.io/api/)[News](https://hexo.io/news/)[Plugins](https://hexo.io/plugins/)[Themes](https://hexo.io/themes/)[About](https://hexo.io/about/)*   [GitHub](https://github.com/hexojs/hexo)

**Getting Started**[Overview](https://hexo.io/docs/)[Setup](https://hexo.io/docs/setup)[Configuration](https://hexo.io/docs/configuration)[Commands](https://hexo.io/docs/commands)[Migration](https://hexo.io/docs/migration)**Basic Usage**[Writing](https://hexo.io/docs/writing)[Front-matter](https://hexo.io/docs/front-matter)[Tag Plugins](https://hexo.io/docs/tag-plugins)[Asset Folders](https://hexo.io/docs/asset-folders)[Data Files](https://hexo.io/docs/data-files)[Server](https://hexo.io/docs/server)[Generating](https://hexo.io/docs/generating)**Deployment**[GitHub Pages](https://hexo.io/docs/github-pages)[GitLab Pages](https://hexo.io/docs/gitlab-pages)[One-Command Deployment](https://hexo.io/docs/one-command-deployment)**Customization**[Permalinks](https://hexo.io/docs/permalinks)[Themes](https://hexo.io/docs/themes)[Templates](https://hexo.io/docs/templates)[Variables](https://hexo.io/docs/variables)[Helpers](https://hexo.io/docs/helpers)[Internationalization (i18n)](https://hexo.io/docs/internationalization)[Syntax Highlight](https://hexo.io/docs/syntax-highlight)[Plugins](https://hexo.io/docs/plugins)**Miscellaneous**[Troubleshooting](https://hexo.io/docs/troubleshooting)[Contributing](https://hexo.io/docs/contributing)

English
