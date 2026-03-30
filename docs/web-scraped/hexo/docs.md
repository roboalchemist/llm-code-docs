# Source: https://hexo.io/docs/

Title: Documentation

URL Source: https://hexo.io/docs/

Published Time: 2026-03-12T00:23:04.147Z

Markdown Content:
Documentation | Hexo
===============

[Hexo](https://hexo.io/)
========================

[Docs](https://hexo.io/docs/)[API](https://hexo.io/api/)[News](https://hexo.io/news/)[Plugins](https://hexo.io/plugins/)[Themes](https://hexo.io/themes/)[About](https://hexo.io/about/)[](https://github.com/hexojs/hexo)

English

[](https://hexo.io/docs/)

Documentation
=============

[](https://github.com/hexojs/site/edit/master/source/docs/index.md "Improve this doc")

Welcome to the Hexo documentation. If you encounter any problems when using Hexo, have a look at the [troubleshooting guide](https://hexo.io/docs/troubleshooting), raise an issue on [GitHub](https://github.com/hexojs/hexo/issues) or start a topic on the [Google Group](https://groups.google.com/group/hexo).

[](https://hexo.io/docs/#What-is-Hexo "What is Hexo?")What is Hexo?[](https://hexo.io/docs/#What-is-Hexo)
---------------------------------------------------------------------------------------------------------

Hexo is a fast, simple and powerful blog framework. You write posts in [Markdown](http://daringfireball.net/projects/markdown/) (or other markup languages) and Hexo generates static files with a beautiful theme in seconds.

[](https://hexo.io/docs/#Installation "Installation")Installation[](https://hexo.io/docs/#Installation)
-------------------------------------------------------------------------------------------------------

It only takes a few minutes to set up Hexo. If you encounter a problem and can’t find the solution here, please [submit a GitHub issue](https://github.com/hexojs/hexo/issues) and we’ll help.

### [](https://hexo.io/docs/#Requirements "Requirements")Requirements[](https://hexo.io/docs/#Requirements)

Installing Hexo is quite easy and only requires the following beforehand:

* [Node.js](http://nodejs.org/) (See [Required Node.js version](https://hexo.io/docs/#Required-Node-js-version))
* [Git](http://git-scm.com/)

If your computer already has these, congratulations! You can skip to the [Hexo installation](https://hexo.io/docs/#Install-Hexo) step.

If not, please follow the following instructions to install all the requirements.

### [](https://hexo.io/docs/#Install-Git "Install Git")Install Git[](https://hexo.io/docs/#Install-Git)

* Windows: Download & install [git](https://git-scm.com/download/win).
* Mac: Install it with [Homebrew](https://brew.sh/), [MacPorts](http://www.macports.org/) or [installer](http://sourceforge.net/projects/git-osx-installer/).
* Linux (Ubuntu, Debian): `sudo apt-get install git-core`
* Linux (Fedora, Red Hat, CentOS): `sudo yum install git-core`

> **For Mac users**
> You may encounter some problems when compiling. Please install Xcode from App Store first. After Xcode is installed, open Xcode and go to **Preferences -> Download -> Command Line Tools -> Install** to install command line tools.

### [](https://hexo.io/docs/#Install-Node-js "Install Node.js")Install Node.js[](https://hexo.io/docs/#Install-Node-js)

Node.js provides [official installer](https://nodejs.org/en/download/) for most platforms.

Alternative installation methods:

* Windows: Install it with [nvs](https://github.com/jasongin/nvs/) (recommended) or [nvm](https://github.com/nvm-sh/nvm).
* Mac: Install it with [Homebrew](https://brew.sh/) or [MacPorts](http://www.macports.org/).
* Linux (DEB/RPM-based): Install it with [NodeSource](https://github.com/nodesource/distributions).
* Others: Install it through respective package manager. Refer to [the guide](https://nodejs.org/en/download/package-manager/) provided by Node.js.

nvs is also recommended for Mac and Linux to avoid possible permission issue.

> **Windows**
> If you use the official installer, make sure **Add to PATH** is checked (it’s checked by default).

> **Mac / Linux**
> If you encounter `EACCES` permission error when trying to install Hexo, please follow [the workaround](https://docs.npmjs.com/resolving-eacces-permissions-errors-when-installing-packages-globally) provided by npmjs; overriding with root/sudo is highly discouraged.

> **Linux**
> If you installed Node.js using Snap, you may need to manually run `npm install` in the target folder when [initializing](https://hexo.io/docs/commands#init) a blog.

### [](https://hexo.io/docs/#Install-Hexo "Install Hexo")Install Hexo[](https://hexo.io/docs/#Install-Hexo)

Once all the requirements are installed, you can install Hexo with npm:

$ npm install -g hexo-cli

### [](https://hexo.io/docs/#Advanced-installation-and-usage "Advanced installation and usage")Advanced installation and usage[](https://hexo.io/docs/#Advanced-installation-and-usage)

Advanced users may prefer to install and use `hexo` package instead.

$ npm install hexo

Once installed, you can run Hexo in two ways:

1. `npx hexo <command>`
2. Linux users can set relative path of `node_modules/` folder:

echo 'PATH="$PATH:./node_modules/.bin"' >> ~/.profile

then run Hexo using `hexo <command>`

### [](https://hexo.io/docs/#Required-Node-js-version "Required Node.js version")Required Node.js version[](https://hexo.io/docs/#Required-Node-js-version)

If you are stuck with older Node.js, you can consider installing a past version of Hexo.

Please note we do not provide bugfixes to past versions of Hexo.

We highly recommend to always install the [latest version](https://www.npmjs.com/package/hexo?activeTab=versions) of Hexo and the [recommended version](https://hexo.io/docs/#Requirements) of Node.js, whenever possible.

| Hexo version | Minimum (Node.js version) | Less than (Node.js version) |
| --- | --- | --- |
| 8.0+ | 20.19.0 | latest |
| 7.0+ | 14.0.0 | latest |
| 6.2+ | 12.13.0 | latest |
| 6.0+ | 12.13.0 | 18.5.0 |
| 5.0+ | 10.13.0 | 12.0.0 |
| 4.1 - 4.2 | 8.10 | 10.0.0 |
| 4.0 | 8.6 | 8.10.0 |
| 3.3 - 3.9 | 6.9 | 8.0.0 |
| 3.2 - 3.3 | 0.12 | unknown |
| 3.0 - 3.1 | 0.10 or iojs | unknown |
| 0.0.1 - 2.8 | 0.10 | unknown |

Last updated: 2026-03-12[Next](https://hexo.io/docs/setup "Setup")

**Contents**

1. [What is Hexo?](https://hexo.io/docs/#What-is-Hexo)
2. [Installation](https://hexo.io/docs/#Installation)
    1.   [Requirements](https://hexo.io/docs/#Requirements)
    2.   [Install Git](https://hexo.io/docs/#Install-Git)
    3.   [Install Node.js](https://hexo.io/docs/#Install-Node-js)
    4.   [Install Hexo](https://hexo.io/docs/#Install-Hexo)
    5.   [Advanced installation and usage](https://hexo.io/docs/#Advanced-installation-and-usage)
    6.   [Required Node.js version](https://hexo.io/docs/#Required-Node-js-version)

[Back to Top](https://hexo.io/docs/#)

**Getting Started**[Overview](https://hexo.io/docs/)[Setup](https://hexo.io/docs/setup)[Configuration](https://hexo.io/docs/configuration)[Commands](https://hexo.io/docs/commands)[Migration](https://hexo.io/docs/migration)**Basic Usage**[Writing](https://hexo.io/docs/writing)[Front-matter](https://hexo.io/docs/front-matter)[Tag Plugins](https://hexo.io/docs/tag-plugins)[Asset Folders](https://hexo.io/docs/asset-folders)[Data Files](https://hexo.io/docs/data-files)[Server](https://hexo.io/docs/server)[Generating](https://hexo.io/docs/generating)**Deployment**[GitHub Pages](https://hexo.io/docs/github-pages)[GitLab Pages](https://hexo.io/docs/gitlab-pages)[One-Command Deployment](https://hexo.io/docs/one-command-deployment)**Customization**[Permalinks](https://hexo.io/docs/permalinks)[Themes](https://hexo.io/docs/themes)[Templates](https://hexo.io/docs/templates)[Variables](https://hexo.io/docs/variables)[Helpers](https://hexo.io/docs/helpers)[Internationalization (i18n)](https://hexo.io/docs/internationalization)[Syntax Highlight](https://hexo.io/docs/syntax-highlight)[Plugins](https://hexo.io/docs/plugins)**Miscellaneous**[Troubleshooting](https://hexo.io/docs/troubleshooting)[Contributing](https://hexo.io/docs/contributing)

 © 2026 [Hexo](https://github.com/hexojs/hexo/graphs/contributors)

 Documentation licensed under [CC BY 4.0](http://creativecommons.org/licenses/by/4.0/).

[![Image 1](https://www.netlify.com/img/global/badges/netlify-dark.svg)](https://www.netlify.com/)[](https://twitter.com/hexojs)[](https://github.com/hexojs/hexo)

[Docs](https://hexo.io/docs/)[API](https://hexo.io/api/)[News](https://hexo.io/news/)[Plugins](https://hexo.io/plugins/)[Themes](https://hexo.io/themes/)[About](https://hexo.io/about/)*   [GitHub](https://github.com/hexojs/hexo)

**Getting Started**[Overview](https://hexo.io/docs/)[Setup](https://hexo.io/docs/setup)[Configuration](https://hexo.io/docs/configuration)[Commands](https://hexo.io/docs/commands)[Migration](https://hexo.io/docs/migration)**Basic Usage**[Writing](https://hexo.io/docs/writing)[Front-matter](https://hexo.io/docs/front-matter)[Tag Plugins](https://hexo.io/docs/tag-plugins)[Asset Folders](https://hexo.io/docs/asset-folders)[Data Files](https://hexo.io/docs/data-files)[Server](https://hexo.io/docs/server)[Generating](https://hexo.io/docs/generating)**Deployment**[GitHub Pages](https://hexo.io/docs/github-pages)[GitLab Pages](https://hexo.io/docs/gitlab-pages)[One-Command Deployment](https://hexo.io/docs/one-command-deployment)**Customization**[Permalinks](https://hexo.io/docs/permalinks)[Themes](https://hexo.io/docs/themes)[Templates](https://hexo.io/docs/templates)[Variables](https://hexo.io/docs/variables)[Helpers](https://hexo.io/docs/helpers)[Internationalization (i18n)](https://hexo.io/docs/internationalization)[Syntax Highlight](https://hexo.io/docs/syntax-highlight)[Plugins](https://hexo.io/docs/plugins)**Miscellaneous**[Troubleshooting](https://hexo.io/docs/troubleshooting)[Contributing](https://hexo.io/docs/contributing)

English
