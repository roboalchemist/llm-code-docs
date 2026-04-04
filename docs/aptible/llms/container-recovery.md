# Source: https://www.aptible.com/docs/core-concepts/architecture/containers/container-recovery.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Container Recovery

When [Containers](/core-concepts/architecture/containers/overview) on Aptible exit unexpectedly (i.e., Aptible did not terminate them as part of a deploy or restart), they are automatically restarted. This feature is called Container Recovery. For most apps, Aptible will automatically restart containers in the event of a crash without requiring user action.

# Overview

When Containers exit, Aptible automatically restarts them from a pristine state. As a result, any changes to the filesystem will be undone (e.g., PID files will be deleted, etc.). As a user, the implication is that if a Container starts properly, Aptible can automatically recover it. To modify this behavior, see [Disabling filesystem wipes](#disabling-filesystem-wipes) below.

Whenever a Container exits and Container Recovery is initiated, Aptible logs the following messages and forwards them to your Log Drains. Note that these logs may not be contiguous; there may be additional log lines between them.

```
container has exited
container recovery initiated
container has started
```

If you wish to set up a log-based alert whenever a Container crashes, we recommend doing so based on the string `container recovery initiated`. This is because the lines `container has started` and `container has exited` will be logged during the normal, healthy [Release Lifecycle](/core-concepts/apps/deploying-apps/releases/overview).

If an App is continuously restarting, Aptible will throttle recovery to a rate of one attempt every 2 minutes.

# Cases where Container Recovery will not work

Container Recovery restarts *Containers* that exit, so if an app crashes but the Container does not exit, then Container Recovery can't help.

Here's an example [Procfile](/how-to-guides/app-guides/define-services) demonstrating this issue:

```yaml  theme={null}
app: (my-app &) && tail -F log/my-app.log
```

In this case, since `my-app` is running in the background, the Container will not exit when `my-app` exits. Instead, it would exit if `tail` exited.

To ensure Container Recovery effectively keeps an App up, make sure that:

* Each Container is only running one App.
* The one App each Container is supposed to run is running in the foreground.

For example, rewrite the above Procfile like so:

```yaml  theme={null}
app: (tail -F log/my-app.log &) && my-app
```

Use a dedicated process manager in a Container, such as [Forever](https://github.com/foreverjs/forever) or [Supervisord](http://supervisord.org/), if multiple processes need to run in a Container or something else needs to run in the foreground.

Contact [Aptible Support](/how-to-guides/troubleshooting/aptible-support) when in doubt.

# Disabling filesystem wipes

Container Recovery automatically restarting containers with a pristine filesystem maximizes the odds of a Container coming back up when recovered and mimics what happens when restarting an App using [`aptible restart`](/reference/aptible-cli/cli-commands/cli-restart).

Set the `APTIBLE_DO_NOT_WIPE` [Configuration](/core-concepts/apps/deploying-apps/configuration) variable on an App to any non-null value (e.g., set it to `1`) to prevent the filesystem from being wiped (assuming it is designed to handle being restarted properly).
