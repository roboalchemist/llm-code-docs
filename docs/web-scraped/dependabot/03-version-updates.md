# Dependabot Version Updates

Source: https://docs.github.com/en/code-security/dependabot/dependabot-version-updates

## Overview

Dependabot version updates is a feature that "takes the effort out of maintaining your dependencies" by automatically keeping packages current with their latest releases.

## How It Works

The system operates through a `dependabot.yml` configuration file checked into your repository. Dependabot uses semantic versioning to determine when updates are available, then automatically raises pull requests to update manifests to the latest dependency versions.

For vendored (cached) dependencies stored directly in repositories rather than referenced in manifests, Dependabot can replace outdated versions directly.

## Availability

This feature is available for all repositories on GitHub across free, pro, and team plans.

## Update Frequency

Users specify check schedules in their configuration using intervals:
- `daily`
- `weekly` (default)
- `monthly`
- `quarterly`
- `semiannually`
- `yearly`
- Custom `cron` expressions

When first enabled, Dependabot may generate pull requests within minutes, depending on how many manifest files need updates.

### Pull Request Limits

To manage volume, Dependabot initially raises a maximum of five pull requests. Users can adjust this limit using the `open-pull-requests-limit` configuration option. The `groups` option further consolidates multiple dependency updates into single pull requests.

## Key Features

- **Automatic commit signing** for signed commits
- **Integration with GitHub Actions workflows** for CI/CD automation
- **Support for security updates** (separate from version updates)
- **Customizable notifications** that can be filtered to show only Dependabot pull requests
- **Dependency grouping** to consolidate updates into single PRs
- **Rebase strategy configuration** for conflict resolution
- **Private package registry support** for internal dependencies

## Configuration

Version updates are configured in `.github/dependabot.yml`:

```yaml
version: 2
updates:
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "weekly"
      day: "monday"
      time: "03:00"
```

## Supported Package Ecosystems

Dependabot version updates supports 20+ package management systems:

- **Python**: pip, pip-tools
- **JavaScript/TypeScript**: npm, yarn, pnpm
- **Ruby**: bundler
- **Java**: Maven, Gradle
- **Go**: go modules
- **Rust**: Cargo
- **PHP**: Composer
- **.NET**: NuGet
- **Elm**: Elm
- **Elixir**: Mix
- **Erlang**: Rebar3
- **Dart**: Pub
- **Deno**: Deno
- **Docker**: Docker
- **Terraform**: Terraform
- **Helm**: Helm
- **And others**

## Automatic Deactivation

When repository maintainers stop engaging with Dependabot pull requests, the system temporarily pauses updates and notifies users. Specifically, if you don't interact with Dependabot pull requests for a repository during a 90-day time period, Dependabot considers your repository as inactive and will automatically pause Dependabot updates.

To reactivate:

1. Engage with Dependabot PRs by merging or closing them
2. Manually re-enable in repository settings if needed

## Managing Updates

Users can:
- Set specific dependencies to always or never update
- Filter by dependency type (direct, indirect, production, development)
- Group multiple updates into single PRs
- Customize commit messages and PR labels
- Configure different schedules per package ecosystem
- Set target branches for updates
