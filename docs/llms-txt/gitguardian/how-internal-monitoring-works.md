# Source: https://docs.gitguardian.com/internal-monitoring/core-concepts/how-internal-monitoring-works.md

# How Internal Monitoring works

> How Internal Monitoring integrates with sources via APIs, webhooks, and native integrations to detect secrets in real-time and historically.

GitGuardian scans your internal sources to detect secrets in real-time, preventing credentials from being exposed across your organization's infrastructure. This includes version control repositories, container registries, documentation platforms, messaging systems, and more.

## How it works

GitGuardian integrates with your internal sources through various methods depending on the platform:

- **APIs**: Direct integration with platform APIs for comprehensive scanning
- **Webhooks**: Real-time event notifications for immediate scanning
- **Native integrations**: Platform-specific apps and connectors

When content is created or modified, GitGuardian immediately scans it using our comprehensive [library of secrets detectors](../../secrets-detection/secrets-detection-engine/detectors/introduction).

If a secret is detected:
1. An incident is created in your dashboard instantly
2. You receive real-time alerts
3. Your team can respond immediately to prevent exposure

### VCS integration specifics

GitGuardian's internal repository monitoring product integrates natively with your VCS (Version Control System), hence on the **server
side**. This is done through a GitHub app or a webhook for GitLab, Bitbucket and Azure repos. GitGuardian "listens" to all the events reaching the **post-receive hook stage**.

GitGuardian integrates directly with your VCS at the server level through native integrations:

- **GitHub**: GitHub App
- **GitLab, Bitbucket, Azure Repos**: Webhooks

This server-side approach means GitGuardian monitors all events that reach the **post-receive hook stage**âafter code is pushed but before it's fully committed to your repository.

Read our [blog article](https://blog.gitguardian.com/git-hooks-automated-secrets-detection/) to learn more about git hooks and why they're essential for automated secrets detection.

## Real-time vs historical scanning

### Real-time scanning
GitGuardian continuously monitors your internal sources for new content and changes. When new data is detected, it's immediately scanned for secrets, ensuring rapid response to potential exposures.

### Historical scanning
Beyond real-time monitoring, GitGuardian can scan existing content that was created before you installed GitGuardian. This comprehensive audit ensures no legacy secrets remain hidden across your systems.

We encourage running historical scans to get complete visibility into your security posture.
