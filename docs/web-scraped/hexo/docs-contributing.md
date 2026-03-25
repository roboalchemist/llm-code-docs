# Source: https://hexo.io/docs/contributing

Title: Contributing

URL Source: https://hexo.io/docs/contributing

Published Time: 2026-03-12T00:23:04.147Z

Markdown Content:
We welcome you to join the development of Hexo. 🤗

[](https://hexo.io/docs/contributing#Development "Development")Development
--------------------------------------------------------------------------

We welcome you to join the development of Hexo. This document will help you through the process.

### [](https://hexo.io/docs/contributing#Before-You-Start "Before You Start")Before You Start

Please read [Contributor Covenant Code of Conduct](https://github.com/hexojs/hexo/blob/master/CODE_OF_CONDUCT.md) first.

Please follow the coding style:

* Follow [Google JavaScript Style Guide](https://google.github.io/styleguide/jsguide.html).
* Use soft-tabs with a two space indent.
* Don’t put commas first.

Also, Hexo has its own [ESLint config](https://github.com/hexojs/eslint-config-hexo), so please make sure your contribution will make ESLint happy.

### [](https://hexo.io/docs/contributing#Workflow "Workflow")Workflow

1. Fork [hexojs/hexo](https://github.com/hexojs/hexo).
2. Clone the repository to your computer and install dependencies.

$ git clone https://github.com/<username>/hexo.git

$ cd hexo

$ npm install

$ git submodule update --init

1. Create a feature branch.

$ git checkout -b new_feature

1. Start hacking.
2. Push the branch:

$ git push origin new_feature

1. Create a pull request and describe the change.

### [](https://hexo.io/docs/contributing#Notice "Notice")Notice

* Please don’t modify version number in `package.json`.
* Your pull request will only get merged when tests passed. Don’t forget to run tests before submission.

$ npm test

[](https://hexo.io/docs/contributing#Updating-official-plugins "Updating official-plugins")Updating official-plugins
--------------------------------------------------------------------------------------------------------------------

Also, we welcome PR or issue to [official-plugins](https://github.com/hexojs). 🤗

[](https://hexo.io/docs/contributing#Updating-Documentation "Updating Documentation")Updating Documentation
-----------------------------------------------------------------------------------------------------------

The Hexo documentation is open source and you can find the source code on [hexojs/site](https://github.com/hexojs/site).

### [](https://hexo.io/docs/contributing#Workflow-1 "Workflow")Workflow

1. Fork [hexojs/site](https://github.com/hexojs/site)
2. Clone the repository to your computer and install dependencies.

$ npm install hexo-cli -g

$ git clone https://github.com/<username>/site.git

$ cd site

$ npm install

1. Start editing the documentation. You can start the server for live previewing.

$ hexo server

1. Push the branch.
2. Create a pull request and describe the change.

### [](https://hexo.io/docs/contributing#Translating "Translating")Translating

#### [](https://hexo.io/docs/contributing#Contribute-translations "Contribute translations")Contribute translations

[![Image 1: Crowdin](https://badges.crowdin.net/hexo/localized.svg)](https://crowdin.com/project/hexo)

Now we use the [Crowdin](https://crowdin.com/project/hexo) platform for translation, where anyone can contribute translations and vote for translations without manual git operations.

#### [](https://hexo.io/docs/contributing#Add-a-new-language "Add a new language")Add a new language

1. Submit a new issue to let us know. The members with access to the [Crowdin Project](https://crowdin.com/project/hexo) add the language in settings.
2. After adding language in Crowdin, anyone can contribute translations on it.
3. Add the new language to [`source/_data/language.yml`](https://github.com/hexojs/site/blob/master/source/_data/languages.yml).
4. Copy `en.yml` in [`themes/navy/languages`](https://github.com/hexojs/site/tree/master/themes/navy/languages) and rename it to the language name (all lower case).

[](https://hexo.io/docs/contributing#Reporting-Issues "Reporting Issues")Reporting Issues
-----------------------------------------------------------------------------------------

When you encounter some problems when using Hexo, you can find the solutions in [Troubleshooting](https://hexo.io/docs/troubleshooting) or ask me on [GitHub](https://github.com/hexojs/hexo/issues) or [Google Group](https://groups.google.com/group/hexo). If you can’t find the answer, please report it on GitHub.

1. Represent the problem in [debug mode](https://hexo.io/docs/commands#Debug_mode).
2. Follow the steps from the issue template to provide a debug message and version when submitting a new issue at GitHub.
