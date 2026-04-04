# Source: https://www.aptible.com/docs/how-to-guides/troubleshooting/common-errors-issues/before-released-commands-fail.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# before_release Commands Failed

## Cause

If any of the [`before_release`](/core-concepts/apps/deploying-apps/releases/aptible-yml#before-release) commands specified in your [`.aptible.yml`](/core-concepts/apps/deploying-apps/releases/aptible-yml) fails i.e. exits with a non-zero status code, Aptible will abort your deployment.

If you are using `before_release` commands for e.g. database migrations, this is usually what you want.

## Resolution

When this happens, the deploy logs will include the output of your `before_release` commands so that you can start there for debugging.

Alternatively, it's often a good idea to try running your `before_release` commands via a [`aptible ssh`](/reference/aptible-cli/cli-commands/cli-ssh) session in order to reproduce the issue.
