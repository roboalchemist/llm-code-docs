# Dependabot Documentation

Source: https://docs.github.com/en/code-security/dependabot

Dependabot is GitHub's automated dependency management tool that helps you maintain secure and up-to-date project dependencies. This documentation covers setup, configuration, and best practices for using Dependabot.

## Contents

1. **[Overview & Getting Started](01-overview.md)** - Introduction to Dependabot and its three core features
2. **[Quickstart Guide](02-quickstart.md)** - Step-by-step setup instructions
3. **[Version Updates](03-version-updates.md)** - Keeping dependencies current
4. **[Security Updates](04-security-updates.md)** - Automatic vulnerability patching
5. **[Configuration Reference](05-configuration-reference.md)** - Complete dependabot.yml options
6. **[Managing Pull Requests](06-managing-pull-requests.md)** - PR handling and commands
7. **[Best Practices](07-best-practices.md)** - Recommended usage patterns

## Quick Summary

Dependabot automates three key security and maintenance tasks:

- **Alerts**: Inform you about vulnerabilities in your dependencies
- **Security Updates**: Automatically fix known vulnerabilities
- **Version Updates**: Keep dependencies current with latest releases

Dependabot supports 20+ package ecosystems including Python (pip), Node.js (npm), Ruby, Java, Go, Rust, and many others.

## Key Features

- Automatic pull requests for dependency updates
- Vulnerability detection and alerting
- Configurable schedules (daily, weekly, monthly, or cron)
- Multi-ecosystem support
- Customizable commit messages and labels
- Private package registry support
- Automatic commit signing
- Integration with GitHub Actions and CI/CD
