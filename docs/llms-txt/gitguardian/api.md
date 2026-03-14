# Source: https://docs.gitguardian.com/platform/gitguardian-suite/api.md

# API

> Overview of the GitGuardian API for programmatically managing dashboard data and running secrets detection scans.

GitGuardian Internal Monitoring has a public API for teams to:

- Programmatically manage their GitGuardian workspace and handle their incidents lifecycle
- Scan additional data sources for hardcoded secrets (e.g., Slack, MS Teams, Jira, Confluence by Atlassian)

## Resources

- [**API documentation**](../../api-docs/introduction.md)
- [**API reference**](https://api.gitguardian.com/docs)

> Please note that if you are using a GitGuardian self-hosted instance, the base url of the API routes will be `https://dashboard.gitguardian.mycorp.local/exposed/` instead of `https://api.gitguardian.com/`.  For example, the scan route will be: `https://dashboard.gitguardian.mycorp.local/exposed/v1/scan`

Examples are provided in all supported programming languages (e.g. Python and Go).
