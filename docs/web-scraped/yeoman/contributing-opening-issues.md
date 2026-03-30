# Source: https://yeoman.io/contributing/opening-issues

Title: How to open an helpful issue

URL Source: https://yeoman.io/contributing/opening-issues

Markdown Content:
How to open an helpful issue | Yeoman
===============

[![Image 1: Yeoman](https://yeoman.io/static/logo.2a54d87108.png)](https://yeoman.io/)
======================================================================================

open

* [Using Yeoman](https://yeoman.io/learning/)
  * [Getting started](https://yeoman.io/learning/)
  * [Tutorial (codelab)](https://yeoman.io/codelab/)
  * [Resources](https://yeoman.io/learning/resources)
  * [Deployment](https://yeoman.io/learning/deployment)
  * [FAQ](https://yeoman.io/learning/faq)
  * [Support](https://yeoman.io/learning/support)

* [Discovering generators](https://yeoman.io/generators/)
* [Creating a generator](https://yeoman.io/authoring/)
  * [Getting started](https://yeoman.io/authoring/)
  * [Running Context](https://yeoman.io/authoring/running-context)
  * [User Interactions](https://yeoman.io/authoring/user-interactions)
  * [Composability](https://yeoman.io/authoring/composability)
  * [Managing Dependencies](https://yeoman.io/authoring/dependencies)
  * [Interacting with the file system](https://yeoman.io/authoring/file-system)
  * [Storing user configs](https://yeoman.io/authoring/storage)
  * [Unit testing](https://yeoman.io/authoring/testing)
  * [Debugging Generators](https://yeoman.io/authoring/debugging)
  * [Integrating Yeoman in other tools](https://yeoman.io/authoring/integrating-yeoman)
  * [Full API documentation](https://yeoman.github.io/generator/)

* [Blog](https://yeoman.io/blog/)
* [Contributing](https://yeoman.io/contributing/)
  * [Contributing](https://yeoman.io/contributing/)
  * [How to open an issue](https://yeoman.io/contributing/opening-issues)
  * [How to submit a PR](https://yeoman.io/contributing/pull-request)
  * [Style Guide](https://yeoman.io/contributing/style-guide)
  * [Testing Guidelines](https://yeoman.io/contributing/testing-guidelines)
  * [Issue system overview](https://yeoman.io/contributing/ticketing)

How to open an helpful issue
----------------------------

* [Contributing](https://yeoman.io/contributing/)
* [How to open an issue](https://yeoman.io/contributing/opening-issues)
* [How to submit a PR](https://yeoman.io/contributing/pull-request)
* [Style Guide](https://yeoman.io/contributing/style-guide)
* [Testing Guidelines](https://yeoman.io/contributing/testing-guidelines)
* [Issue system overview](https://yeoman.io/contributing/ticketing)

In order for us to help you please check that you’ve completed the following steps:

* Made sure you’re on the latest version `npm update -g yo`
* Used the search feature to ensure that the bug hasn’t been reported before
* Included as much information about the bug as possible, including any output you’ve received, what OS and version you’re on, etc.
* Shared the output from running the following command in your project root as this can also help track down the issue.

Unix:

`yo --version && echo $PATH $NODE_PATH && node -e 'console.log(process.platform, process.versions)' && cat Gruntfile.js`

Windows:

`yo --version && echo %PATH% %NODE_PATH% && node -e "console.log(process.platform, process.versions)" && type Gruntfile.js`

Then submit your issue on the relevant repository

* [General concerns on the project](https://github.com/yeoman/yeoman/issues/new)
* [Issues with `yo`](https://github.com/yeoman/yo/issues/new)
* [Issues when writing a generator](https://github.com/yeoman/generator/issues/new)

For any issues related to a particular generator (`grunt build` not working, you’d like a new feature, etc), then search on github for the relevant repository. They’re usually named `generator-X`.

![Image 2: Stickers!](https://yeoman.io/static/yeoman-character-sticker.51cef7e007.png)

[Show your love for **Yeoman**, wear our **merch**!](https://yeoman.threadless.com/)

* [![Image 3: Twitter](https://yeoman.io/static/social-twitter.c359540fc8.svg)](https://twitter.com/yeoman)
* [![Image 4: GitHub](https://yeoman.io/static/social-github.89959ef390.svg)](https://github.com/yeoman/yeoman)
* [![Image 5: Feed](https://yeoman.io/static/social-feed.ad4bea7819.svg)](https://yeoman.io/blog/atom.xml)

* [API](https://yeoman.github.io/generator/)
* [Improve this page](https://github.com/yeoman/yeoman.github.io/blob/source/app/contributing/opening-issues.md "Edit this page on GitHub to help improve the site")
