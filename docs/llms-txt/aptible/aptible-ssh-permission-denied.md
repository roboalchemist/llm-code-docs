# Source: https://www.aptible.com/docs/how-to-guides/troubleshooting/common-errors-issues/aptible-ssh-permission-denied.md

# aptible ssh Permission Denied

If you get an error indicating `Permission denied (publickey)` when using [`aptible ssh`](/reference/aptible-cli/cli-commands/cli-ssh) (or [`aptible db:tunnel`](/reference/aptible-cli/cli-commands/cli-db-tunnel), [`aptible logs`](/reference/aptible-cli/cli-commands/cli-logs)), follow the instructions below.

This issue is caused by a bug in OpenSSH 7.8 that broke support for client certificates, which Aptible uses to authenticate [Ephemeral SSH Sessions](/core-concepts/apps/connecting-to-apps/ssh-sessions) sessions.

This only happens if you installed the [Aptible CLI](/reference/aptible-cli/cli-commands/overview) from source (as opposed to using the Aptible Toolbelt).

To fix the issue, follow the [Aptible CLI installation instructions](/reference/aptible-cli/cli-commands/overview) and make sure to install the CLI using the Aptible Toolbelt package download.
