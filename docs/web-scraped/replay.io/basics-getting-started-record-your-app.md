# Source: https://docs.replay.io/basics/getting-started/record-your-app

Title: Replay - Browser DevTools from the future.

URL Source: https://docs.replay.io/basics/getting-started/record-your-app

Markdown Content:
Getting Started

Record your application
-----------------------

Recording your application with the Replay browser lets you capture a bug once and inspect it after the fact without having to reproduce it again. This makes it possible to:

*   [Share the replay as a URL with your team so others can inspect it as if they were there when you recorded it.](https://docs.replay.io/basics/replay-devtools/time-travel-devtools/collaborative-devtools)
*   [Debug your application by adding new `console.log` statements anywhere in the replay.](https://docs.replay.io/basics/replay-devtools/time-travel-devtools/live-console-logs)
*   [Inspect Network requests](https://docs.replay.io/basics/replay-devtools/browser-devtools/network-monitor), [React components](https://docs.replay.io/basics/replay-devtools/framework-devtools/react-panel), and [DOM elements](https://docs.replay.io/basics/replay-devtools/browser-devtools/elements-panel) as if the application were running live on your laptop.

In this guide, we'll use the Replay CLI to record your interactions on the page `https://first.replay.io`. If you'd like to record your Playwright or Cypress tests instead, feel free to [jump ahead](https://docs.replay.io/reference/test-runners/overview).

1

Install the Replay CLI
----------------------

Run the following command to install the Replay CLI:

Terminal

```
npm i -g replayio
```

2

Record your replay
------------------

Run the following command to open the Replay browser and start recording.

Terminal

```
replayio record https://first.replay.io
```

This command:

*   Prompts you to log in to your Replay account with Google (if not already logged in)
*   Installs the Replay browser (if not already installed)
*   Opens the Replay browser to begin recording `https://first.replay.io`

3

Inspect your replay
-------------------

When you close the browser, you'll be prompted to upload your recordings. Once the upload is completed, you will get a URL where you can inspect your application with Replay DevTools.

Terminal

```
Uploading recordings...
a616009e.. overboard.dev Now 7.5s (uploaded)
View recording at:
https://app.replay.io/recording/a616009e-b825-4c54-83b4-e20bd8c0cb25
```

Now that we've recorded our first [replay](https://app.replay.io/recording/a616009e-b825-4c54-83b4-e20bd8c0cb25), let's [inspect it with Replay DevTools](https://docs.replay.io/basics/getting-started/inspect-replay).

FAQ
---

Next Steps

### [Inspect your replay](https://docs.replay.io/basics/getting-started/inspect-replay)

Walk through the steps of inspecting your new replay.

### [Replay DevTools](https://docs.replay.io/basics/replay-devtools/overview)

Overview of Replay's browser, framework, and time travel DevTools.

### [Set up a team](https://docs.replay.io/reference/replay-teams/setting-up-a-team)

Learn how to share replays as a team.

### [Test Suites Analytics](https://docs.replay.io/basics/test-suites/recent-runs)

Stay on top of your Test Suite's health.

Next[Record your Cypress.io test](https://docs.replay.io/basics/getting-started/record-your-cypress-tests)
