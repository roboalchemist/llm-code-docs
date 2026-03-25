# Source: https://barba.js.org/docs/getstarted/intro/

Title: barba.js

URL Source: https://barba.js.org/docs/getstarted/intro/

Published Time: Mon, 02 Dec 2024 22:34:05 GMT

Markdown Content:

* [Get Started -----------](https://barba.js.org/docs/getstarted/intro/)
    1. [Intro -----](https://barba.js.org/docs/getstarted/intro/)
    2. [Install -------](https://barba.js.org/docs/getstarted/install/)
    3. [Markup ------](https://barba.js.org/docs/getstarted/markup/)
    4. [Basic transition ----------------](https://barba.js.org/docs/getstarted/basic-transition/)
    5. [Run custom code ---------------](https://barba.js.org/docs/getstarted/custom-code/)
    6. [Lifecycle ---------](https://barba.js.org/docs/getstarted/lifecycle/)
    7. [Legacy example --------------](https://barba.js.org/docs/getstarted/legacy/)
    8. [Browser support ---------------](https://barba.js.org/docs/getstarted/browser-support/)
    9. [Useful links ------------](https://barba.js.org/docs/getstarted/useful-links/)

* [Advanced --------](https://barba.js.org/docs/advanced/options/)
    1. [Options -------](https://barba.js.org/docs/advanced/options/)
    2. [Hooks -----](https://barba.js.org/docs/advanced/hooks/)
    3. [Transitions -----------](https://barba.js.org/docs/advanced/transitions/)
    4. [Views -----](https://barba.js.org/docs/advanced/views/)
    5. [Strategies ----------](https://barba.js.org/docs/advanced/strategies/)
    6. [Recipes -------](https://barba.js.org/docs/advanced/recipes/)
    7. [Third party scripts -------------------](https://barba.js.org/docs/advanced/third-party/)
    8. [Utils -----](https://barba.js.org/docs/advanced/utils/)
    9. [Developer API -------------](https://barba.js.org/api/)

* [Plugins -------](https://barba.js.org/docs/plugins/intro/)
    1. [Intro -----](https://barba.js.org/docs/plugins/intro/)
    2. [Router ------](https://barba.js.org/docs/plugins/router/)
    3. [Prefetch --------](https://barba.js.org/docs/plugins/prefetch/)
    4. [Css ---](https://barba.js.org/docs/plugins/css/)
    5. [Head ----](https://barba.js.org/docs/plugins/head/)
    6. [Preset ------](https://barba.js.org/docs/plugins/preset/)

![Image 1: Stability](https://img.shields.io/badge/stability-stable-brightgreen.svg?style=flat-square)[![Image 2: CircleCI](https://img.shields.io/circleci/project/github/barbajs/barba/main.svg?style=flat-square)](https://circleci.com/gh/barbajs/barba/tree/main "Badge")[![Image 3: Coverage Status](https://img.shields.io/coveralls/github/barbajs/barba/main.svg?style=flat-square)](https://coveralls.io/github/barbajs/barba?branch=main "Badge")[![Image 4: Commitizen friendly](https://img.shields.io/badge/commitizen-friendly-brightgreen.svg?style=flat-square)](http://commitizen.github.io/cz-cli/ "Badge")[![Image 5: Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg?style=flat-square)](https://conventionalcommits.org/ "Badge")[![Image 6: lerna](https://img.shields.io/badge/maintained%20with-lerna-cc00ff.svg?style=flat-square)](https://lerna.js.org/ "Badge")[![Image 7: License](https://img.shields.io/badge/license-MIT-green.svg?style=flat-square)](https://github.com/barbajs/barba/blob/main/LICENSE "Badge")[![Image 8: Slack workspace](https://img.shields.io/badge/slack-workspace-purple.svg?style=flat-square&logo=slack)](https://join.slack.com/t/barbajs/shared_invite/enQtNTU3NTAyMjkxMzAyLTkxYWUwZmM1YWQxMmNlYmE0ZjY4NDQxMGUxYjkwYWFlMzEzOWM4OTRhMWRmYTQyYzFlMmQ3OGFmYmI3MWY0OWY "Badge")

[](https://barba.js.org/docs/getstarted/intro/#Intro "Intro")Intro
------------------------------------------------------------------

**Barba.js** — aka _Barba_ — is a small _(7kb minified and compressed)_ and easy-to-use library that helps you create fluid and smooth transitions between your website’s pages. It makes your website run like a **SPA**_(Single Page Application)_ and help reduce the delay between your pages, minimize browser HTTP requests and enhance your user’s web experience.

> **Notice**: this guide assumes intermediate knowledge of HTML, CSS, and JavaScript. It is worth mentioning that all code examples use ES6+ syntax. If you are not comfortable with this syntax, we would encourage you to grasp the basics then come back.
>
>
> In case of emergency, check the [“legacy” code example](https://barba.js.org/docs/getstarted/legacy/).
