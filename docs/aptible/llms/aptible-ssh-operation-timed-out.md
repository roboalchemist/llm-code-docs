# Source: https://www.aptible.com/docs/how-to-guides/troubleshooting/common-errors-issues/aptible-ssh-operation-timed-out.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# aptible ssh Operation Timed Out

When connecting using [`aptible ssh`](/reference/aptible-cli/cli-commands/cli-ssh), you might encounter this error:

```
ssh: connect to host bastion-layer-$NAME.aptible.in port 1022: Operation timed out
```

## Cause

This issue is often caused by a firewall blocking traffic on port `1022` from your workstation to Aptible.

## Resolution

Try connecting from a different network or using a VPN (we suggest using [Cloak](https://www.getcloak.com/) if you need to quickly set up an ad-hoc VPN).

If that does not resolve your issue, contact [Aptible Support](/how-to-guides/troubleshooting/aptible-support).
