# Source: https://www.aptible.com/docs/core-concepts/apps/connecting-to-apps/ssh-sessions.md

# Ephemeral SSH Sessions

> Learn about using Ephemeral SSH sessions on Aptible

# Overview

Aptible offers Ephemeral SSH Sessions for accessing containers that are configured identically to App containers, making them ideal for managing consoles and running ad-hoc jobs.

Unlike regular containers, ephemeral containers won't be restarted when they crash. If your connection to Aptible drops, the remote Container will be terminated.

## Creating Ephemeral SSH Sessions

Ephemeral SSH Sessions can be created using the [`aptible ssh`](/reference/aptible-cli/cli-commands/cli-ssh) command.

<Note> Ephemeral containers are not the same size as your App Container. By default, ephemeral containers are scaled to 1024 MB. </Note>

# Terminating Ephemeral SSH Sessions

### Manually Terminating

You can terminate your SSH sessions by closing the terminal session you spawned it in or exiting the container.

<Tip> It may take a bit of time for our API to acknowledge that the SSH session is shut down. If you're running into Plan Limits trying to create another one, wait a few minutes and try again.</Tip>

### Expiration

SSH sessions will automatically terminate upon expiration. By default, SSH sessions will expire after seven days. Contact [Aptible Support](/how-to-guides/troubleshooting/aptible-support) to reduce the default SSH session duration for Dedicated [Stacks](/core-concepts/architecture/stacks). Please note that this setting takes effect regardless of whether the session is active or idle.

<Note> When you create a SSH session using [`aptible ssh`](/reference/aptible-cli/cli-commands/cli-ssh), you're logging in to an **ephemeral** container. You are **not** logging to one of your running app containers. This means that running commands like `ps` won't reflect what's actually running in your App containers, and that files that exist in your App containers will not be present in the ephemeral session. </Note>

# Logging

<Warning> **If you process PHI or  sensitive information in your app or database:** it's very likely that PHI will at some point leak in your SSH session logs. To ensure compliance, make sure you have the appropriate agreements in place with your logging provider before sending your SSH logs there. For PHI, you'll need a BAA. </Warning>

Logs from Ephemeral SSH Sessions can be routed to [Log Drains](/core-concepts/observability/logs/log-drains/overview).

Note that for interactive sessions, Aptible allocates a TTY for your container, so your Log Drain will receive exactly what the end user is seeing. This has two benefits:

* You see the user's input as well.
* If you’re prompting the user for a password using a safe password prompt that does not write back anything, nothing will be sent to the Log Drain either. That prevents you from leaking your passwords to your logging provider.

## Metadata

For Log Drains that support embedding metadata in the payload ([HTTPS Log Drains](/core-concepts/observability/logs/log-drains/https-log-drains) and [Self-Hosted Elasticsearch Log Drains](/core-concepts/observability/logs/log-drains/elasticsearch-log-drains)), the following keys are included:

* `operation_id`: The ID of the Operation that resulted in the creation of this Ephemeral Session.
* `operation_user_name`: The name of the user that created the Operation.
* `operation_user_email`: The email of the user that created the Operation.
* `APTIBLE_USER_DOCUMENT`: An expired JWT object with user information.

For Log Drains that don't support embedding metadata (i.e., [Syslog Log Drains](/core-concepts/observability/logs/log-drains/syslog-log-drains)), the ID of the Operation that created the session is included in the logs.
