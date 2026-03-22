# Source: https://docs.testsprite.com/mcp/core/test-progress-dashboard.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.testsprite.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Test Progress Dashboard

> Monitor your entire test suite as it runs with live status updates, detailed test insights, and execution recordings.

## Overview

When you trigger `testsprite_generate_code_and_execute`, TestSprite automatically opens a live progress dashboard where you can monitor your entire test suite as it runs.

<Frame>
  <img src="https://mintcdn.com/testspriteinc/ex3lblqbetJSa-ak/images/generate-execute-code.png?fit=max&auto=format&n=ex3lblqbetJSa-ak&q=85&s=81b4276d217fa86407b36c889c4def24" alt="generate and execute code" width="1906" height="253" data-path="images/generate-execute-code.png" />
</Frame>

<br />

<Tabs>
  <Tab title="Real-Time Monitoring">
    Watch your test cases execute with live status updates. Each test displays its current state—whether it's still running, has passed, or encountered an issue.

    <Frame>
      <img src="https://mintcdn.com/testspriteinc/teCzVODp75jc8wZz/images/real-time-progress.png?fit=max&auto=format&n=teCzVODp75jc8wZz&q=85&s=c3aefbc602f990ccd59c336482ca87e5" alt="modification progress" width="1730" height="513" data-path="images/real-time-progress.png" />
    </Frame>
  </Tab>

  <Tab title="Search & Filter Tests">
    Quickly locate specific tests using the search bar by <kbd>Test Name</kbd> or <kbd>ID</kbd>. Filter your test suite by <kbd>Status</kbd>, <kbd>Creation Date</kbd>, or <kbd>Last Modified Time</kbd> to focus on what matters most.

    <Frame>
      <img src="https://mintcdn.com/testspriteinc/teCzVODp75jc8wZz/images/dashboard-filter.png?fit=max&auto=format&n=teCzVODp75jc8wZz&q=85&s=3625e0290d3dc84ec9a0127250e53474" alt="modification filter" width="1730" height="513" data-path="images/dashboard-filter.png" />
    </Frame>
  </Tab>

  <Tab title="Sort Your Way">
    Organize your test list by <kbd>Created Date</kbd>, <kbd>Last Execution Time</kbd>, or <kbd>Alphabetically</kbd> to streamline your review workflow.

    <Frame>
      <img src="https://mintcdn.com/testspriteinc/teCzVODp75jc8wZz/images/dashboard-sort.png?fit=max&auto=format&n=teCzVODp75jc8wZz&q=85&s=87d504defc8162842a0bfadebeeb3484" alt="modification sort" width="1730" height="513" data-path="images/dashboard-sort.png" />
    </Frame>
  </Tab>
</Tabs>

## Test Detail View

Click on any test case to dive into its detailed execution results.

### Execution Recording

Every test run is recorded, giving you a complete video playback of exactly what happened during execution.

<Frame>
  <img src="https://mintcdn.com/testspriteinc/teCzVODp75jc8wZz/images/dashboard-video.png?fit=max&auto=format&n=teCzVODp75jc8wZz&q=85&s=d4711ffe686c439bf916b8c33ce6a97a" alt="modification video" width="1730" height="895" data-path="images/dashboard-video.png" />
</Frame>

### Test Results at a Glance

Get a quick summary of each test's outcome, including pass/fail status, error details, and timing information.

<Frame>
  <img src="https://mintcdn.com/testspriteinc/teCzVODp75jc8wZz/images/dashboard-results.png?fit=max&auto=format&n=teCzVODp75jc8wZz&q=85&s=847f8b7c4a8d0fee20462e06667cfa76" alt="modification video 1" width="1730" height="895" data-path="images/dashboard-results.png" />
</Frame>

The **Test Result** section shows you:

| Detail                      | Description                       |
| --------------------------- | --------------------------------- |
| <kbd>Pass/Fail Status</kbd> | Clear visual indicators           |
| <kbd>Error Messages</kbd>   | Detailed messages when tests fail |

### Step-by-Step Breakdown

Drill into each test to see every action it performed, from navigation and input to assertions, so you can pinpoint exactly where things went right or wrong.

<Frame>
  <img src="https://mintcdn.com/testspriteinc/qvVl4_9ScMi7zBCG/images/dashboard-actions.png?fit=max&auto=format&n=qvVl4_9ScMi7zBCG&q=85&s=956685d4d99eccf96154c5fb8e124f35" alt="modification actions" width="1730" height="895" data-path="images/dashboard-actions.png" />
</Frame>

Each test displays its individual steps with the corresponding action type:

| Action              | Description                  |
| ------------------- | ---------------------------- |
| <kbd>Navigate</kbd> | URL navigation actions       |
| <kbd>Input</kbd>    | Form field entries           |
| <kbd>Click</kbd>    | Button and link interactions |
| <kbd>Scroll</kbd>   | Page scrolling actions       |
| <kbd>Assert</kbd>   | Verification checkpoints     |

## Review Past Test Runs Anytime

Use the `testsprite_open_test_result_dashboard` tool to reopen the progress dashboard at any time. Simply prompt:

<Frame>
  <img src="https://mintcdn.com/testspriteinc/teCzVODp75jc8wZz/images/dashboard-prompt.png?fit=max&auto=format&n=teCzVODp75jc8wZz&q=85&s=14b0d2e015cc39995b3551b80b7dc8d1" alt="terminal generate" width="1730" height="813" data-path="images/dashboard-prompt.png" />
</Frame>

<CodeGroup>
  ```text Example Prompt theme={null}
  open test result dashboard of testsprite cases
  ```
</CodeGroup>

This brings back the full dashboard view where you can:

* Browse all your historical test suites
* Review execution recordings from previous runs
* Make modifications to any existing test case
* Re-run updated tests with your changes


Built with [Mintlify](https://mintlify.com).