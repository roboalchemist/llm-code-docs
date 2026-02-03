# Source: https://www.aptible.com/docs/how-to-guides/troubleshooting/common-errors-issues/git-push-everything-utd.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# git Push "Everything up-to-date."

## Cause

This message means that the local branch you're pushing to Aptible is already at exactly the same revision as is currently deployed on Aptible.

## Resolution

* If you've already pushed your code to Aptible and simply want to restart the app, you can do so by running the [`aptible restart`](/reference/aptible-cli/cli-commands/cli-restart) command. If you actually want to trigger a new build from the same code you've already pushed, you can use [`aptible rebuild`](/reference/aptible-cli/cli-commands/cli-rebuild) instead.

* If you're pushing a branch other than `master`, you must still push to the remote branch named `master` in order to trigger a build. Assuming you've got a Git remote named `aptible`, you can do so with a command like the following `git push aptible local-branch:master`.
