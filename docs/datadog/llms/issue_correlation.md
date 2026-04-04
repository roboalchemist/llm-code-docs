# Source: https://docs.datadoghq.com/error_tracking/issue_correlation.md

---
title: Issue Correlation with Error Tracking
description: Understand how errors are grouped into issues.
breadcrumbs: Docs > Error Tracking > Issue Correlation with Error Tracking
---

# Issue Correlation with Error Tracking

{% callout %}
##### Join the Preview!

Issue Correlation with Error Tracking is currently in Preview, but you can easily request access! Use this form to submit your request. Once approved, you can automatically map related issues across services, helping you trace problems to their true origin.

[Request Access](https://www.datadoghq.com/product-preview/error-tracking-issue-correlation/)
{% /callout %}

## Overview{% #overview %}

{% image
   source="https://datadog-docs.imgix.net/images/error_tracking/issue-correlation-overview.6344f83d483289a86ec51b395ca60e05.png?auto=format"
   alt="The view of the correlated issues tab in the context of the Error Tracking Explorer" /%}

You use Error Tracking to simplify debugging by grouping thousands of similar errors into a single issue. Use issue correlation to determine the cause of the issue, the impact it has on other services, and if the error is a result of a downstream dependency.

Issue correlation also helps reduce noise from the issue list by identifying the most critical issues. This allows you to alert the right team and reach a quicker resolution.

## Identify correlated issues{% #identify-correlated-issues %}

To identify which issues across your services are correlated, navigate to the Error Tracking page at [**Error > Issues**](https://app.datadoghq.com/error-tracking).

{% image
   source="https://datadog-docs.imgix.net/images/error_tracking/issue-correlation-et-page.eaad33b7760ea6fd91c4eddeffb8b2b3.png?auto=format"
   alt="The issues list in the Error Tracking Explorer" /%}

Select an issue to open the issue's details side panel.

{% image
   source="https://datadog-docs.imgix.net/images/error_tracking/issue-correlation-side-panel.0e75238bcac3f4afdc6cd534f5edebc7.png?auto=format"
   alt="The details of an issue in the Error Tracking Explorer" /%}

Open the `Correlated issues` tab to see the issue correlation map.

{% image
   source="https://datadog-docs.imgix.net/images/error_tracking/issue-correlation-correlation-tab.c7ce8e3bdabe1ba865ed11e8d2ffa443.png?auto=format"
   alt="The details of an issue in the Error Tracking Explorer focusing on the issue correlation tab" /%}

The issue correlation map shows the following information about a given issue:

- **Root cause**: the services that are likely to be causing the issue
- **Current issue**: the issue selected along with whether it is assigned to a team
- **Impact**: the resources, users, and sessions that are impacted

## Further Reading{% #further-reading %}

- [Learn about Error Tracking Monitors](https://docs.datadoghq.com/monitors/types/error_tracking)
- [Issue States in Error Tracking](https://docs.datadoghq.com/error_tracking/issue_states/)
