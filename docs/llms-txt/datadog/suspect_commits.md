# Source: https://docs.datadoghq.com/error_tracking/suspect_commits.md

# Source: https://docs.datadoghq.com/tracing/error_tracking/suspect_commits.md

---
title: Suspect Commits
description: >-
  Identify and analyze suspect commits that may be causing errors in your
  application using Error Tracking's commit analysis features.
breadcrumbs: Docs > APM > Error Tracking for Backend Services > Suspect Commits
---

# Suspect Commits

## Overview{% #overview %}

Error Tracking can identify suspect commits, helping you pinpoint the root cause of your errors and expedite resolution. This feature is automatically enabled on issues when the setup requirements are met.

{% image
   source="https://datadog-docs.imgix.net/images/logs/error_tracking/suspect_commit.3a3ca6fb06e957d30feca75fb08d6ccd.png?auto=format"
   alt="A suspect commit as it is displayed in the Datadog UI" /%}

Once a suspect commit has been identified, it is displayed on the issue panel, as shown in the highlighted area of the image below.

{% image
   source="https://datadog-docs.imgix.net/images/logs/error_tracking/suspect_commit_in_context.8964956d72c3ea7c0da61a0da83fada3.png?auto=format"
   alt="A suspect commit shown in the context of the issue panel" /%}

To view a suspect commit on GitHub, click the **View Commit** button.

### Suspect commit criteria{% #suspect-commit-criteria %}

A commit becomes a suspect commit if:

- It modifies one of the lines in the stack trace.
- It was authored before the first error occurrence.
- It was authored no more than 90 days before the first error occurrence.
- It is the most recent commit that meets the above criteria.

For a suspect commit to be displayed on an issue, at least one candidate commit must have been found.

## Setup{% #setup %}

Once the setup requirements are met, suspect commits automatically appear on issues where available. Commits made before the setup requirements were met are not displayed.

### Enable Source Code Integration{% #enable-source-code-integration %}

The Suspect Commits feature requires [Source Code Integration](https://docs.datadoghq.com/integrations/guide/source-code-integration). To enable Source Code Integration:

1. On the [**Integrations** page](https://app.datadoghq.com/integrations) in Datadog, choose **Link Source Code** in the top navbar.
1. Follow the steps to associate a commit with your telemetry and configure your GitHub repository.

### Install the GitHub integration{% #install-the-github-integration %}

Install [the GitHub integration](https://docs.datadoghq.com/integrations/github/), enabling read permissions for pull requests and contents.

## Further reading{% #further-reading %}

- [Troubleshoot root causes with GitHub commit and ownership data in Error Tracking](https://www.datadoghq.com/blog/error-tracking-and-github/)
