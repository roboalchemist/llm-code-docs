# Source: https://docs.datadoghq.com/error_tracking/issue_team_ownership.md

---
title: Issue Team Ownership
description: Automatically assign issues to teams based on Git CODEOWNERS files.
breadcrumbs: Docs > Error Tracking > Issue Team Ownership
---

# Issue Team Ownership

## Overview{% #overview %}

Issue Team Ownership automates your triaging work by assigning issues to the right teams. Your team owns an issue if it is either:

- code owner of the top-level stack frame of the issue according to GitHub `CODEOWNERS`.
- owner of the service where the issue happens.

**Note**: Stack frames of third-party files are not taken into account. Only the top-most stack frame related to a file present in your repository is considered.

## Leverage team ownership{% #leverage-team-ownership %}

Team ownership information appears on the issue details panel when available:

{% image
   source="https://datadog-docs.imgix.net/images/error_tracking/ownership-details.2b7b7cdf7b5732ee5a9b1fd2f46d1995.png?auto=format"
   alt="Team ownership information on issue details" /%}

You can also use issue team ownership to filter issues by teams in the Error Tracking Explorer.

{% image
   source="https://datadog-docs.imgix.net/images/error_tracking/ownership-search-bar.6a2dd60f602b40f2e65a3b4e7e2cac2d.png?auto=format"
   alt="Team owner filtering in the search bar" /%}

## Setup{% #setup %}

### Configure Source Code Integration{% #configure-source-code-integration %}

1. Ensure [Source Code Integration](https://docs.datadoghq.com/integrations/guide/source-code-integration) is set up.
1. Install [the GitHub integration](https://docs.datadoghq.com/integrations/github/).
1. Make sure all requested permissions (Contents, Members) are granted for the GitHub integration.

### Set up a CODEOWNERS file{% #set-up-a-codeowners-file %}

Create a valid `CODEOWNERS` file in your repository following [GitHub's CODEOWNERS standards](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners).

### Link GitHub teams to Datadog teams{% #link-github-teams-to-datadog-teams %}

In Datadog, go to [**Teams**](https://app.datadoghq.com/teams) > Select your team > **Settings** > **GitHub Connection** to map your Datadog teams to the corresponding GitHub teams defined in your `CODEOWNERS` file.

{% image
   source="https://datadog-docs.imgix.net/images/error_tracking/team-github-connection.d8c5563ad175b7f8980e51a1649af8dc.jpg?auto=format"
   alt="Linking GitHub teams to Datadog teams" /%}

**Note**: Issue Team Ownership only supports GitHub.

## Configuration{% #configuration %}

Issue Team Ownership is enabled by default for all services once the setup requirements are met. You can control this feature at both global and service levels through the [Error Tracking settings page](https://app.datadoghq.com/error-tracking/settings/issues/ownership).

{% image
   source="https://datadog-docs.imgix.net/images/error_tracking/ownership-config.b97af0e33fab662e98c1a3464ab9a58c.png?auto=format"
   alt="Issue Team Ownership configuration settings" /%}

## Further Reading{% #further-reading %}

- [Auto Assign](https://docs.datadoghq.com/error_tracking/auto_assign/)
- [Suspected Causes](https://docs.datadoghq.com/error_tracking/suspected_causes/)
