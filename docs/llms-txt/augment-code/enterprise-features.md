# Source: https://docs.augmentcode.com/codereview/enterprise-features.md

# Code Review Enterprise Features

> Advanced features and capabilities available to Enterprise plan customers for Augment Code Review.

## Overview

Augment Code Review Enterprise provides advanced features designed for organizations that need greater control, deeper integrations, and comprehensive analytics. This page outlines the key differences between self-serve and Enterprise plans.

## Feature Comparison

| Feature                | Self-Serve                 | Enterprise                                                         |
| ---------------------- | -------------------------- | ------------------------------------------------------------------ |
| **Advanced Analytics** | Total reviews performed    | Full dashboard with reviews, comments addressed, and team insights |
| **User Allowlist**     | All repo users get reviews | Control exactly which users receive PR reviews                     |
| **MCP Integration**    | Not available              | Connect to Jira, Linear, Notion, feature flags, and more           |
| **Multi-Org Support**  | Single GitHub organization | Multiple GitHub organizations per tenant                           |
| **Seats**              | Up to 20 seats             | Unlimited seats                                                    |
| **Connected Repos**    | Limited                    | Unlimited repositories                                             |

## Available Enterprise Features

### Advanced Analytics

Enterprise customers have access to a comprehensive analytics dashboard that goes beyond basic metrics:

* **Reviews Performed**: Track the total number of reviews completed by Augment Code Review
* **Comments Addressed**: See how many review comments were acted upon by developers
* **Engagement Metrics**: Understand how your team interacts with Code Review feedback

Self-serve users see only the total number of reviews performed.

<Note>
  Access the analytics dashboard at [Code Review Analytics](https://app.augmentcode.com/code-review/analytics).
</Note>

### User Allowlist

Enterprise administrators can specify exactly which GitHub users can trigger Augment Code Review. This provides fine-grained control over feature access within your organization.

When Allowlist Mode is active:

* Only users in the allowlist can trigger Augment Code Review
* Automatic and manual reviews are disabled for all other users
* Useful for phased rollouts or restricting access to specific teams

<Note>
  Manage your allowlist at [User Access Settings](https://app.augmentcode.com/settings/code-review/user-access).
</Note>

### MCP Integration

Connect Augment Code Review to your existing tools through Model Context Protocol (MCP). This enables the code review agent to gather additional context from your organization's systems:

* **Ticketing Systems**: Jira, Linear, and other issue trackers
* **Documentation**: Notion, Confluence, and internal wikis
* **Feature Flags**: LaunchDarkly, Split, and other feature management tools
* **Other Systems**: Any MCP-compatible tool relevant to your development workflow

This additional context allows Code Review to provide more informed and relevant feedback based on your team's specific requirements and documentation.

<Note>
  Configure MCP servers at [MCP Settings](https://app.augmentcode.com/settings/code-review/mcp).
</Note>

### Multi-Organization Support

Enterprise customers can install the Augment Code Review GitHub bot across multiple GitHub organizations or accounts. This is essential for:

* Organizations with separate GitHub orgs for different products or teams
* Companies that have acquired other organizations with existing GitHub structures
* Enterprises with strict organizational boundaries between business units

All organizations connect to a single Augment Enterprise tenant for unified management and billing.

### Unlimited Seats

Enterprise plans provide access to Augment Code Review for your entire organization without seat limitations. Self-serve plans are limited to 20 seats.

### Unlimited Connected Repositories

Enterprise customers can enable Code Review on an unlimited number of repositories. Self-serve plans have a cap on the number of repositories that can be connected.

## Getting Started with Enterprise

To upgrade to Enterprise or learn more about Enterprise features, visit [augmentcode.com/pricing](https://augmentcode.com/pricing) or contact our sales team.

If you're already an Enterprise customer, visit your [Code Review Settings](https://app.augmentcode.com/settings/code-review) to configure these features.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.augmentcode.com/llms.txt