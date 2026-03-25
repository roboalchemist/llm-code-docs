# Source: https://docs.gitguardian.com/platform/enterprise-administration/ip-allowlist.md

# IP allowlist for workspace access

> Restrict access to your GitGuardian workspace to specific IP addresses or CIDR ranges.

The IP Allowlist enables customers to restrict access to their workspace, including both the dashboard and the public API, to trusted IP addresses or IP ranges. This feature is designed to enhance security by ensuring that only approved IPs can interact with your GitGuardian resources.

:::info Business accounts only
This feature is reserved to workspaces with Business access (Business or Business trial plans). After the end of a Business trial, any IP restriction will be lifted.
:::

:::info Not available on self-hosted environments
This feature is not supported on self-hosted environments, as there are alternative methods to restrict access in those scenarios.
:::

## Configuring the IP allowlist

Configuring and enabling the allowlist can be done only by workspace managers.

1. Navigate to Settings > Authentication > IP allowlist
2. Add IP addresses or ranges: in the IP Allowlist management section, enter the IP addresses or IP ranges (in CIDR notation) that you wish to allow, and enter a description. Note that only IPv4 addresses are supported. 
3. Enable IP Allowlist: once the necessary IP addresses or ranges are added, toggle the IP restriction option to enable it.

Workspace managers can subsequently edit or delete IP addresses or IP ranges through the same settings section.

![ip-allowlist-setting](/img/platform/enterprise-administration/auth-ip-allowlist.png)

## Blocked Resources

Once the IP Allowlist is enabled, the restriction applies to all resources within your GitGuardian workspace:

- **UI:** Users without an allowed IP address will be blocked from accessing the dashboard.
- **API and ggshield:** The API, and as a consequence the ggshield cli that relies on it, will be subject to the same IP restrictions.

:::caution
If you are using ggshield in CI/CD pipelines or in pre-receive hooks, you must ensure that the IPs from your version control system (VCS) or CI/CD runners are added to the allowlist to avoid any disruptions.
:::
