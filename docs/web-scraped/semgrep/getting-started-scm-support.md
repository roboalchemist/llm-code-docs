# Supported source code managers

Source: https://semgrep.dev/docs/getting-started/scm-support

- [](/docs/)- [Scan](/docs/getting-started/quickstart)- Get started- Supported source code managers- [SCM](/docs/tags/scm)- [Deployment](/docs/tags/deployment)Supported source code managers
Semgrep supports the following source code managers (SCM) and plans to varying degrees. Please review the information for your specific SCM and plan to see what Semgrep features are available to you.

If any of the following conditions apply to you, you may need to add [Semgrep&#x27;s IP addresses](/docs/deployment/checklist#ip-addresses) to your ingress and egress allowlists, or you can use the [Network Broker](/docs/semgrep-ci/network-broker):

- Your SCM offers security features that limit access to your resources
- Your SCM is behind a firewall or protected by network restrictions regarding access
- You are using a virtual private network (VPN)

PlanUnsupported Semgrep featuresAzure DevOps Cloud- Query console- Auto PRs for Supply Chain findingsAzure DevOps Server- Semgrep Assistant- Semgrep Managed Scans- Pull request comments- Query console- Diff-aware scans- Sending findings to Semgrep AppSec Platform- Default branch identification- Auto PRs for Supply Chain findings- Generic secrets (requires Semgrep Assistant)Bitbucket Cloud Free- Semgrep Assistant†-  Semgrep Managed Scan†-  Query console- Auto PRs for Supply Chain findings- Generic secrets (requires Semgrep Assistant)Bitbucket Cloud Standard- Semgrep Assistant†- Semgrep Managed Scan†-  Query console- Auto PRs for Supply Chain findings- Generic secrets (requires Semgrep Assistant)Bitbucket Cloud Premium- Query console- Auto PRs for Supply Chain findingsBitbucket Data Center- Query console- Diff-aware scans require Bitbucket Data Center version 8.8 or later.- Auto PRs for Supply Chain findingsGitHub Free-GitHub Pro-GitHub Team-GitHub Enterprise Cloud-GitHub Enterprise Server- Auto PRs for Supply Chain findingsGitLab Free- Semgrep Managed Scans*-  Query console- Auto PRs for Supply Chain findingsGitLab Premium- Query console- Auto PRs for Supply Chain findingsGitLab Ultimate- Query console- Auto PRs for Supply Chain findingsGitLab Dedicated / Dedicated for Government- Query console- Auto PRs for Supply Chain findingsGitLab Self-Managed Free- Semgrep Managed Scans*** Query console- Auto PRs for Supply Chain findingsGitLab Self-Managed Premium- Query console- Auto PRs for Supply Chain findingsGitLab Self-Managed Ultimate- Query console- Auto PRs for Supply Chain findings
**†**Semgrep Assistant and Managed Scans require a workspace access token, which is only available to users with Bitbucket Cloud Premium.

*****Semgrep Managed Scans requires access to group webhooks, which is unavailable to GitLab Free users.

Not finding what you need in this doc? Ask questions in our [Community Slack group](https://go.semgrep.dev/slack), or see [Support](/docs/support/) for other ways to get help.

Tags:**- [SCM](/docs/tags/scm)- [Deployment](/docs/tags/deployment)[Edit this page](https://github.com/semgrep/semgrep-docs/edit/main/docs/getting-started/scm-support.md)Last updated on **Jun 23, 2025**