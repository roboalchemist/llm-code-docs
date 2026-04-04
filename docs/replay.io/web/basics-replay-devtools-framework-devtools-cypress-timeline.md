# Source: https://docs.replay.io/basics/replay-devtools/framework-devtools/cypress-timeline

Title: Replay - Browser DevTools from the future.

URL Source: https://docs.replay.io/basics/replay-devtools/framework-devtools/cypress-timeline

Markdown Content:
Replay DevTools: Framework DevTools: Cypress Timeline
===============
Replay docs
===============
Replay docs
===============

[](https://docs.replay.io/)

Search docs Ctrl K

Theme 

[](https://github.com/replayio)[](https://replay.io/discord)[Log in](https://app.replay.io/)

[Basics](https://docs.replay.io/basics/time-travel/why-time-travel)[Learn](https://docs.replay.io/learn/replay-course)[Reference](https://docs.replay.io/reference/test-runners/overview)

*   
Getting Started 
    *   [Record your app](https://docs.replay.io/basics/getting-started/record-your-app)
    *   [Record your Cypress.io test](https://docs.replay.io/basics/getting-started/record-your-cypress-tests)
    *   [Record your Playwright test](https://docs.replay.io/basics/getting-started/record-your-playwright-tests)

*   
Time Travel 
    *   [Why time travel?](https://docs.replay.io/basics/time-travel/why-time-travel)
    *   [How does time travel work?](https://docs.replay.io/basics/time-travel/how-does-time-travel-work)

*   
Replay DevTools 
    *   [Overview](https://docs.replay.io/basics/replay-devtools/overview)
    *   Time Travel DevTools  
    *   
Framework DevTools 
        *   [React Panel](https://docs.replay.io/basics/replay-devtools/framework-devtools/react-panel)
        *   [Redux Panel](https://docs.replay.io/basics/replay-devtools/framework-devtools/redux-panel)
        *   [Cypress Timeline](https://docs.replay.io/basics/replay-devtools/framework-devtools/cypress-timeline)
        *   [Playwright Timeline](https://docs.replay.io/basics/replay-devtools/framework-devtools/playwright-timeline)

    *   Browser DevTools  

*   
Replay Chrome Extension 
    *   [Getting Started](https://docs.replay.io/basics/replay-chrome-extension/getting-started)

*   
Replay MCP 
    *   [Overview](https://docs.replay.io/basics/replay-mcp/overview)
    *   [Quickstart](https://docs.replay.io/basics/replay-mcp/quickstart)

*   
Test Suite Dashboard 
    *   [Overview](https://docs.replay.io/basics/test-suites/overview)
    *   [Recent runs](https://docs.replay.io/basics/test-suites/recent-runs)
    *   [Top Failing And Flaky Tests](https://docs.replay.io/basics/test-suites/top-failing-and-flaky-tests)
    *   [PR Comments](https://docs.replay.io/basics/test-suites/pr-comments)

Cypress timeline
================

Inspect your Cypress test as if it’s running locally with the Cypress timeline.
-------------------------------------------------------------------------------

![Image 1: Cypress timeline](https://docs.replay.io/_next/image?url=%2Fimages%2Fcypress.png&w=1920&q=75)

Basics
------

The Cypress timeline includes many of the features you’re accustomed to when debugging your test locally and some functionality that’s only possible with time travel.

### Step actions

When you select a a test step action, you jump to that point in time and the location in the source code where the Cy action was executed.

### Step events

The timeline shows relevant network events and lets you jump to the request in the Network monitor.

### Step details

Selecting a step shows the step details below with the ability to jump from the test subject to the element in the Elements panel.

Time Travel
-----------

### Jump to code

Clicking the **Jump to code** button seeks you from the test step into your React component’s event handler. There’s never been a more powerful way to start debugging a flaky test.

[Check out this replay](https://replay.help/cypress-flake-debug) for a detailed walkthrough on debugging a flaky Cypress test. You'll see the capabilities of Replay DevTools and walk through the debugging process of identifying the root cause.

Previous[Redux Panel](https://docs.replay.io/basics/replay-devtools/framework-devtools/redux-panel)

Next[Playwright Timeline](https://docs.replay.io/basics/replay-devtools/framework-devtools/playwright-timeline)

On this page
------------

1.   ### [Basics](https://docs.replay.io/basics/replay-devtools/framework-devtools/cypress-timeline#basics)

    1.   [Step actions](https://docs.replay.io/basics/replay-devtools/framework-devtools/cypress-timeline#step-actions)
    2.   [Step events](https://docs.replay.io/basics/replay-devtools/framework-devtools/cypress-timeline#step-events)
    3.   [Step details](https://docs.replay.io/basics/replay-devtools/framework-devtools/cypress-timeline#step-details)

2.   ### [Time Travel](https://docs.replay.io/basics/replay-devtools/framework-devtools/cypress-timeline#time-travel)

    1.   [Jump to code](https://docs.replay.io/basics/replay-devtools/framework-devtools/cypress-timeline#jump-to-code)

* * *

Back to top
