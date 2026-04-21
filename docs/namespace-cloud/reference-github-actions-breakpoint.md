<!-- Source: https://namespace.so/docs/reference/github-actions/breakpoint -->

# namespacelabs/breakpoint-action

namespacelabs/breakpoint-action@v0

[namespacelabs/breakpoint-action](https://github.com/namespacelabs/breakpoint-action) is a GitHub action that allows
you to pause the execution of a workflow, enter a live SSH session, debug the environment and
finally resume the run when you are done.

**Note**: Workflows that have active breakpoint sessions are still running and continue to count towards your total CI usage.

## Example

```
jobs:
  go-tests:
    runs-on: ubuntu-latest
 
    steps:
      - name: Checkout
        uses: actions/checkout@v4
 
      - name: Run Go tests
        run: |
          go test ./...
 
      - name: Breakpoint if tests failed
        if: failure()
        uses: namespacelabs/breakpoint-action@v0
        with:
          duration: 30m
          authorized-users: jack123, alice321
```

When the above `breakpoint` runs, you'll see a log message like the following:

```
┌───────────────────────────────────────────────────────────────────────────┐
│                                                                           │
│ Breakpoint running until 2023-05-24T16:06:48+02:00 (29 minutes from now). │
│                                                                           │
│ Connect with: ssh -p 40812 runner@rendezvous.namespace.so                 │
│                                                                           │
└───────────────────────────────────────────────────────────────────────────┘
```

The SSH service in `breakpoint` only accepts sessions from public SSH keys configured by GitHub users, listed by `authorized-users`.

And there you have it, an SSH session to connect to debug your workflow.

Check out [the actions GitHub](https://github.com/namespacelabs/breakpoint) page for a more detailed documentation.

## Options

### mode

*`string`* One of `pause` or `background`. In `pause` mode the workflow is paused until you tell it to continue (or `duration` is reached). In `background` mode the breakpoint runs in the background allowing you to connect at any time during your workflow.

Required. Default is `pause`.

### duration

*`string`* The initial breakpoint duration. This input is ignored when `mode` is set to `background`.

Required. Default is `30m`.

### authorized-users

*`string`* A comma-separated list of authorized GitHub users.

### authorized-keys

*`string`* A comma-separated list of authorized SSH keys.

### slack-announce-channel

*`string`* A Slack channel where webhook sends notifications.

### shell

*`string`* The path of the login shell.

Optional.

Last updated February 13, 2026
