# Dependabot Security Updates

Source: https://docs.github.com/en/code-security/dependabot/dependabot-security-updates

## Overview

Dependabot security updates automate the process of fixing vulnerable dependencies by raising pull requests when vulnerabilities are detected.

## Vulnerability Detection

Dependabot identifies vulnerabilities through the dependency graph. As the documentation states: "If you enable Dependabot security updates, when a Dependabot alert is raised for a vulnerable dependency in the dependency graph of your repository, Dependabot automatically tries to fix it."

The system alerts users to every vulnerable dependency in the full dependency graph, though security updates are only triggered for dependencies explicitly listed in manifest or lock files.

## How Security Updates Work

### Automatic Response

When vulnerabilities are identified, "Dependabot checks whether it's possible to upgrade the vulnerable dependency to a fixed version without disrupting the dependency graph for the repository. Then Dependabot raises a pull request to update the dependency to the minimum version that includes the patch."

This process is automatic—when a security update PR is available, Dependabot will create it without waiting for user action.

### Alert Resolution

Upon merging a security update pull request, the corresponding alert is automatically marked as resolved.

### Comprehensive Coverage

The system attempts to address every available vulnerability: "When Dependabot security updates are enabled for a repository, Dependabot will automatically try to open pull requests to resolve **every** open Dependabot alert that has an available patch."

## Key Features

### Grouped Updates

Multiple vulnerable dependencies can be grouped into single pull requests to reduce notification volume. This is controlled via the `groups` configuration option.

### Compatibility Scoring

Updates include compatibility metrics showing potential breaking changes, helping you assess the impact of security patches.

### Automatic Deactivation

If maintainers ignore pull requests, the system temporarily pauses updates. Specifically, if you don't interact with Dependabot pull requests for a repository during a 90-day time period, Dependabot considers your repository as inactive and will pause updates.

## Dependabot Alerts

Dependabot alerts inform you about vulnerabilities in your dependencies. These alerts:

- Appear in the Security tab of your repository
- Show severity levels (critical, high, moderate, low)
- Include CVE and GHSA identifiers
- Link to vulnerability databases and security advisories
- Provide patch availability information

### Alert Management

You can:
- Review detailed vulnerability information
- Merge Dependabot's proposed security update PRs
- Dismiss alerts with reasons (not affected, tolerable risk, no bandwidth, inaccurate)
- Add comments to explain dismissals
- Track alert status over time

## Configuration

Security updates are enabled separately from version updates. In your `dependabot.yml`:

```yaml
version: 2
updates:
  - package-ecosystem: "pip"
    directory: "/"
    schedule:
      interval: "daily"
    # Security updates run on their own schedule (realtime)
```

Security updates run independently and trigger immediately when vulnerabilities are detected, regardless of the version update schedule.

## Best Practices

1. **Enable both features**: Use security updates for urgent fixes and version updates for maintenance
2. **Monitor alerts regularly**: Check your Security tab weekly
3. **Merge security PRs promptly**: Prioritize security patches over other work
4. **Review the patches**: Understand what's being changed before merging
5. **Keep repository active**: Interact with PRs to prevent automatic deactivation
6. **Configure notifications**: Set up alerts to notify your team immediately

## Supported Ecosystems

Security updates work with all supported package ecosystems:
- Python (pip)
- Node.js (npm, yarn, pnpm)
- Ruby (bundler)
- Java (Maven, Gradle)
- Go (go modules)
- Rust (Cargo)
- PHP (Composer)
- .NET (NuGet)
- Docker
- Terraform
- Helm
- And others
