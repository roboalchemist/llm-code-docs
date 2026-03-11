# Source: https://stryker-mutator.io/docs/General/example/

Title: Welcome to the RoboCoasters 🤖🎢 | Stryker Mutator

URL Source: https://stryker-mutator.io/docs/General/example/

Markdown Content:
Welcome to the RoboCoasters 🤖🎢 | Stryker Mutator
===============

[Skip to main content](https://stryker-mutator.io/docs/General/example/#__docusaurus_skipToContent_fallback)

📣 Discover the ["Who's testing the tests? Mutation testing with StrykerJS"](https://fosdem.org/2024/schedule/event/fosdem-2024-1683-who-s-testing-the-tests-mutation-testing-with-strykerjs/) talk on FOSDEM 2024.

[![Image 1: Stryker Mutator Logo](https://stryker-mutator.io/images/stryker.svg) **Stryker Mutator**](https://stryker-mutator.io/)[Blog](https://stryker-mutator.io/blog/)[For JavaScript](https://stryker-mutator.io/docs/stryker-js/introduction/)[For C#](https://stryker-mutator.io/docs/stryker-net/introduction/)[For Scala](https://stryker-mutator.io/docs/stryker4s/getting-started/)[An example](https://stryker-mutator.io/docs/General/example/)[Playground](https://stryker-mutator.io/stryker-playground/)

[Dashboard](https://dashboard.stryker-mutator.io/)

[](https://stryker-mutator.io/docs/General/example/#)
*   [StrykerJS (JS & TS)](https://github.com/stryker-mutator/stryker-js)
*   [Stryker.NET (C#)](https://github.com/stryker-mutator/stryker-net)
*   [Stryker4s (Scala)](https://github.com/stryker-mutator/stryker4s)
*   [Mutation Testing Elements](https://github.com/stryker-mutator/mutation-testing-elements)
*   [Stryker Dashboard](https://github.com/stryker-mutator/stryker-dashboard)
*   [This website](https://github.com/stryker-mutator/stryker-mutator.github.io)

Search Ctrl K

*   [General](https://stryker-mutator.io/docs/General/example/#) 
    *   [Introduction](https://stryker-mutator.io/docs/)
    *   [An example](https://stryker-mutator.io/docs/General/example/)
    *   [Stryker dashboard](https://stryker-mutator.io/docs/General/dashboard/)
    *   [FAQ](https://stryker-mutator.io/docs/General/faq/)

*   [Mutation Testing](https://stryker-mutator.io/docs/General/example/#) 
*   [StrykerJS](https://stryker-mutator.io/docs/General/example/#) 
*   [Stryker.NET](https://stryker-mutator.io/docs/General/example/#) 
*   [Stryker4s](https://stryker-mutator.io/docs/General/example/#) 

*   [](https://stryker-mutator.io/)
*   General
*   An example

On this page

Welcome to the RoboCoasters 🤖🎢
================================

An introduction to mutation testing

_How code coverage of 100% could mean only 60% is tested._

![Image 2: RoboCoasters application](https://stryker-mutator.io/assets/images/robo-coasters-example-33c50b3315336afb954cfe6ba9d14384.png)

TL;DR[​](https://stryker-mutator.io/docs/General/example/#tldr "Direct link to TL;DR")
--------------------------------------------------------------------------------------

No time to run the example yourself? Don't worry; we did it for you. Open it right in your browser:

*   [The RoboCoasters website](https://stryker-mutator.io/robo-coasters-example/)
*   [Coverage report](https://stryker-mutator.io/robo-coasters-example/reports/coverage/lcov-report/index.html)
*   [Mutation report](https://dashboard.stryker-mutator.io/reports/github.com/stryker-mutator/robo-coasters-example/master)

What is this?[​](https://stryker-mutator.io/docs/General/example/#what-is-this "Direct link to What is this?")
--------------------------------------------------------------------------------------------------------------

RoboCoasters is a small application to demo mutation testing. It has a fair amount of unit tests. We didn't try our best to write bad tests when we wrote this application. We just focussed on code coverage and didn't practice Test Driven Development. It turns out it's easy to write bad tests or forget a few important test cases. RoboCoasters even has a fairly large bug. Finding it is easy using the mutation report. Why don't you give it a try? 😁

**Note:** Robo coasters is developed using [native web components](https://developer.mozilla.org/en-US/docs/Web/Web_Components) without a frontend framework. This is done on purpose to keep this example as accessible as possible and to keep the maintenance burden low.

Try it yourself[​](https://stryker-mutator.io/docs/General/example/#try-it-yourself "Direct link to Try it yourself")
---------------------------------------------------------------------------------------------------------------------

1.   Install [git](https://git-scm.com/)
2.   Install [nodejs](https://nodejs.org/)
3.   Open command prompt and clone this repository:`git clone https://github.com/stryker-mutator/robo-coasters-example`   
4.   Change directory into `robo-coasters-example` and install the dependencies.`cd robo-coasters-examplenpm install`   
5.   Run tests with npm. This will generate a code coverage report.`npm test`   
6.   Review the 100% code coverage score. Open up the code coverage report in the `reports/coverage/lcov-report` directory.
7.   Run mutation testing with [Stryker](https://stryker-mutator.io/)`npm run test:mutation`   
8.   Review ~60% mutation score. Open up the mutation report in the `reports/mutation` directory.
9.   Run the website with `npm start`. Can you find the bug?

Try to install stryker yourself.[​](https://stryker-mutator.io/docs/General/example/#try-to-install-stryker-yourself "Direct link to Try to install stryker yourself.")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you want to install stryker yourself, step back in history using git:

`git checkout pre-strykernpm install`

After that you can install stryker for yourself:

`npm init stryker`

Choose the following options in the questionnaire:

*   **Are you using one of these frameworks?**`None/other`
*   **Which test runner do you want to use?**`jest`
*   **Reporters**: `html`, `clear-text`, `progress`
*   **Which package manager do you want to use?**: `npm`
*   **What file type do you want for your config file?**: `json`

After the plugins are installed, open the `stryker.conf.json` file and make the following change:

`{  "$schema": "./node_modules/@stryker-mutator/core/schema/stryker-schema.json",  "_comment": "This config was generated using 'stryker init'",  "packageManager": "npm",  "reporters": [    "html",    "clear-text",    "progress",    "dashboard"  ],  "testRunner": "jest",- "coverageAnalysis": "perTest"+ "coverageAnalysis": "perTest",+ "testRunnerNodeArgs": ["--experimental-vm-modules"]}`

(this is needed because we're using [jest with ECMAScript modules](https://jestjs.io/docs/ecmascript-modules))

After the plugins are installed, try it out:

`npx stryker run`

[Edit this page](https://github.com/stryker-mutator/stryker-mutator.github.io/edit/develop/docs/General/example.mdx)

[Previous Introduction](https://stryker-mutator.io/docs/)[Next Stryker dashboard](https://stryker-mutator.io/docs/General/dashboard/)

*   [TL;DR](https://stryker-mutator.io/docs/General/example/#tldr)
*   [What is this?](https://stryker-mutator.io/docs/General/example/#what-is-this)
*   [Try it yourself](https://stryker-mutator.io/docs/General/example/#try-it-yourself)
*   [Try to install stryker yourself.](https://stryker-mutator.io/docs/General/example/#try-to-install-stryker-yourself)

Docs

*   [FAQ](https://stryker-mutator.io/docs/General/faq/)

Community

*   [Slack](https://join.slack.com/t/stryker-mutator/shared_invite/enQtOTUyMTYyNTg1NDQ0LTU4ODNmZDlmN2I3MmEyMTVhYjZlYmJkOThlNTY3NTM1M2QxYmM5YTM3ODQxYmJjY2YyYzllM2RkMmM1NjNjZjM)
*   [Twitter](https://twitter.com/stryker_mutator)

More

*   [Blog](https://stryker-mutator.io/blog/)
*   [GitHub](https://github.com/stryker-mutator/)

[![Image 3: Info Support Logo](https://stryker-mutator.io/images/info-support.svg)](https://infosupport.com/)

Powered by [Info Support](https://www.infosupport.com/open-source/).

Stryker is released under the Apache 2.0 license. Site by the [Stryker team](https://github.com/orgs/stryker-mutator/people). Logo by Selina van den Top.
