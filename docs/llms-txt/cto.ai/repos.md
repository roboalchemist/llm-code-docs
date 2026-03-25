# Source: https://docs.cto.new/essentials/repos.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.cto.new/llms.txt
> Use this file to discover all available pages before exploring further.

# Repositories

Depending on the type of project you're working on, cto can connect to existing repos in GitHub or GitLab, create new repos in your own connected git accounts, or manage your repos for you without linking to a git provider.

## Task runner

Make sure to configure the task runner environment for connected repos. This is the virtual environment where the agent works on your code.

You can run system setup steps, install project dependencies, and define code checks steps. This allows [cto.new](http://cto.new) to do things like build, run, test, lint, and format your code.

<Note>
  Try the setup agent which can configure most of this for you
</Note>

Once you have completed setup, run a test so that you know everything works as it should. If you used the setup agent it will do this for you.

## Permissions

In order to create repos in your linked git account, cto needs admin permissions.


Built with [Mintlify](https://mintlify.com).