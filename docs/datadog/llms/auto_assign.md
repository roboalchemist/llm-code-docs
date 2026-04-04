# Source: https://docs.datadoghq.com/error_tracking/auto_assign.md

---
title: Auto Assign
description: Learn about Auto Assign in Error Tracking.
breadcrumbs: Docs > Error Tracking > Auto Assign
---

# Auto Assign

## Overview{% #overview %}

Auto Assign automates triaging by assigning issues to the author of their [suspect commit](https://docs.datadoghq.com/error_tracking/suspect_commits/).

This feature enables faster issue resolution by automatically assigning issues to developers most familiar with the relevant code, while reducing manual triage work. You are immediately notified when issues arise from your code.

## Setup{% #setup %}

Once configured and enabled, issues are automatically assigned to developers based on suspect commit analysis.

### Configure Source Code Integration{% #configure-source-code-integration %}

1. Ensure [Source Code Integration](https://docs.datadoghq.com/integrations/guide/source-code-integration/) is enabled and set up.
1. Install [the GitHub integration](https://docs.datadoghq.com/integrations/github/).
1. Make sure all requested permissions (Contents, Members) are granted for the GitHub integration.

**Note**: Auto Assign requires linking your Datadog account to your GitHub account. This connection is established when you first load a stack trace code snippet.

## How it works{% #how-it-works %}

When an error occurs, Auto Assign:

1. Analyzes the stack trace to identify a suspect commit.
1. Finds the author of this commit.
1. Assigns the issue to that developer and sends a notification.

## Managing assignments{% #managing-assignments %}

You can view assigned developers directly within each issue in Datadog. If needed, manual reassignment is always possible to override the automatic assignment.

{% image
   source="https://datadog-docs.imgix.net/images/error_tracking/ownership-details.2b7b7cdf7b5732ee5a9b1fd2f46d1995.png?auto=format"
   alt="Team ownership information on issue details" /%}

# Configuration{% #configuration %}

Navigate to the [Error Tracking settings page](https://app.datadoghq.com/error-tracking/settings/issues/ownership) in Datadog to manage Auto Assign settings. You can enable or disable Auto Assign globally for your entire organization, or configure it on a per-service basis for more granular control.

{% image
   source="https://datadog-docs.imgix.net/images/error_tracking/ownership-config.b97af0e33fab662e98c1a3464ab9a58c.png?auto=format"
   alt="Issue Team Ownership configuration settings" /%}

## Further Reading{% #further-reading %}

- [Suspect Commits](https://docs.datadoghq.com/error_tracking/suspect_commits/)
- [Issue Team Ownership](https://docs.datadoghq.com/error_tracking/issue_team_ownership/)
