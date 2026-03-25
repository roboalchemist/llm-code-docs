# Source: https://docs.replay.io/basics/test-suites/pr-comments

Title: Replay - Browser DevTools from the future.

URL Source: https://docs.replay.io/basics/test-suites/pr-comments

Markdown Content:
Test Suite Dashboard

Pull Request Comments
---------------------

Pull Request Comments show updated results of your test run with links to replays and the Test Suite Dashboard, all from the pull request in GitHub.
----------------------------------------------------------------------------------------------------------------------------------------------------

![Image 1: Pull Request Comments](https://docs.replay.io/_next/image?url=%2Fimages%2Fpr-comment.png&w=1920&q=75)

Overview
--------

Once you have your test suites integrated with Replay in CI, you can add our bot to your GitHub repository. The bot will leave comments on PRs with a summary of the most recent test run.

The comment also includes links to replays of the tests and the test run in the Test Suite Dashboard. The comment will automatically update with the most recent results every time a new commit is pushed.

1

Install the app
---------------

Go to the Replay [Github App](https://github.com/apps/replay-io) page and click on **Configure**. You will be prompted to select the organization and repositories that the PR Comments bot will access to.

![Image 2: PR Comment bot installation](https://docs.replay.io/_next/image?url=%2Fimages%2Fpr_comments_installation.png&w=1920&q=75)

2

Set up your workflow file
-------------------------

The PR Comment bot listens to the `pull_request` event. It will collect links from your test runs and show them as a comment in your pull request conversation tab on GitHub. This means that your workflow file needs to have run on the `pull_request` event.

```
name: Playwright Tests
on: [pull_request]
jobs:
  ### ...your jobs
```

3

Run your tests
--------------

After you run your test, PR comment bot will collect links from your test step, and show them as a comment in your pull request conversation tab on GitHub.

![Image 3: PR Comment bot in GitHub](https://docs.replay.io/_next/image?url=%2Fimages%2Fpull-request-comments.png&w=1920&q=75)

PR comment bot currently only listens to `pull_request` event, which means that comments will not appear on events such as `push` or `workflow_dispatch`. If you are running your tests against Vercel preview deployments, you can [check out this page](https://docs.replay.io/learn/examples/vercel) to learn how to set up your workflow file.

Previous[Top Failing And Flaky Tests](https://docs.replay.io/basics/test-suites/top-failing-and-flaky-tests)

Next[Managing replays](https://docs.replay.io/reference/replay-teams/managing-replays)
