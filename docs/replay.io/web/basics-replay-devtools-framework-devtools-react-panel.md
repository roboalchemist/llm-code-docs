# Source: https://docs.replay.io/basics/replay-devtools/framework-devtools/react-panel

Title: Replay - Browser DevTools from the future.

URL Source: https://docs.replay.io/basics/replay-devtools/framework-devtools/react-panel

Markdown Content:
Replay DevTools: Framework DevTools
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

Replay DevTools

React panel
===========

Inspect React components at any point in time.
----------------------------------------------

![Image 1: React panel](https://docs.replay.io/_next/image?url=%2Fimages%2Freact.png&w=1920&q=75)

Basics
------

Replay’s React panel is similar to the React DevTools browser extension, but includes functionality only possible with time travel.

### Select component picker

Select components with the component picker.

### Inspect the component tree

Explore the current component tree with higher ordered components highlighted on the right.

### Search for components

Press `cmd+f` or select the search input to find components within the component tree.

### Inspect Props + State

Inspect component props, state, and hook values with built in object formatting and jump to function definition.

### Jump to definition

Click the Jump button in the top right to go to where the component is defined.

Time Travel
-----------

### View changed props and state

Because we’re able to compare the current component’s render with the prior, we are able to highlight the props, state, and hook values that have changed in yellow.

### View hook values

Because we’re able to collect more information at while replaying the replay, we’re able to stop showing the hook index and start showing the hook value and function definition.

### Mapped component names

Because we’re not concerned about the performance overhead of processing sourcemaps while replaying, we’re able to source map component names so you’re able to see the original names.

Learn more
----------

Learn how to use the React panel to examine hooks and properties, and observe how they change over time. This tutorial will also teach you how to navigate from the React panel to the specific element that it rendered. You can find the whole course at [replay.help/course](https://replay.help/course)

##### Upload in progress...

Your video file is being uploaded. The currently loaded video is the source file.

Previous[Focus window](https://docs.replay.io/basics/replay-devtools/time-travel-devtools/focus-window)

Next[Redux Panel](https://docs.replay.io/basics/replay-devtools/framework-devtools/redux-panel)

On this page
------------

1.   ### [Basics](https://docs.replay.io/basics/replay-devtools/framework-devtools/react-panel#basics)

    1.   [Select component picker](https://docs.replay.io/basics/replay-devtools/framework-devtools/react-panel#select-component-picker)
    2.   [Inspect the component tree](https://docs.replay.io/basics/replay-devtools/framework-devtools/react-panel#inspect-the-component-tree)
    3.   [Search for components](https://docs.replay.io/basics/replay-devtools/framework-devtools/react-panel#search-for-components)
    4.   [Inspect Props + State](https://docs.replay.io/basics/replay-devtools/framework-devtools/react-panel#inspect-props--state)
    5.   [Jump to definition](https://docs.replay.io/basics/replay-devtools/framework-devtools/react-panel#jump-to-definition)

2.   ### [Time Travel](https://docs.replay.io/basics/replay-devtools/framework-devtools/react-panel#time-travel)

    1.   [View changed props and state](https://docs.replay.io/basics/replay-devtools/framework-devtools/react-panel#view-changed-props-and-state)
    2.   [View hook values](https://docs.replay.io/basics/replay-devtools/framework-devtools/react-panel#view-hook-values)
    3.   [Mapped component names](https://docs.replay.io/basics/replay-devtools/framework-devtools/react-panel#mapped-component-names)

3.   ### [Learn more](https://docs.replay.io/basics/replay-devtools/framework-devtools/react-panel#learn-more)

* * *

Back to top
