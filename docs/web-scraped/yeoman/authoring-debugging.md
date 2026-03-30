# Source: https://yeoman.io/authoring/debugging

Title: Debugging Generators | Yeoman

URL Source: https://yeoman.io/authoring/debugging

Markdown Content:
Debugging Generators | Yeoman
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

Debugging Generators
--------------------

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

To debug a generator, you can pass Node.js debug flags by running it like this:

```
# OS X / Linux / Windows
npx --node-options="--inspect" yo <generator> [arguments]
```

You can then debug your generator using the Chrome Devtools or your preferred IDE. See [Node Debugging Guide](https://nodejs.org/en/docs/inspector/) for more info.

Yeoman generators also provide a debug mode to log relevant lifecycle information. You can activate it by setting the `DEBUG` environment variable to the desired scope (the scope of the generator system is `yeoman:generator`).

```
# OS X / Linux
DEBUG=yeoman:generator

# Windows
set DEBUG=yeoman:generator
```

![Image 2: Stickers!](https://yeoman.io/static/yeoman-character-sticker.51cef7e007.png)

[Show your love for **Yeoman**, wear our **merch**!](https://yeoman.threadless.com/)

* [![Image 3: Twitter](https://yeoman.io/static/social-twitter.c359540fc8.svg)](https://twitter.com/yeoman)
* [![Image 4: GitHub](https://yeoman.io/static/social-github.89959ef390.svg)](https://github.com/yeoman/yeoman)
* [![Image 5: Feed](https://yeoman.io/static/social-feed.ad4bea7819.svg)](https://yeoman.io/blog/atom.xml)

* [API](https://yeoman.github.io/generator/)
* [Improve this page](https://github.com/yeoman/yeoman.github.io/blob/source/app/authoring/debugging.md "Edit this page on GitHub to help improve the site")
