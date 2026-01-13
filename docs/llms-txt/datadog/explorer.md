# Source: https://docs.datadoghq.com/continuous_integration/explorer.md

# Source: https://docs.datadoghq.com/continuous_delivery/explorer.md

# Source: https://docs.datadoghq.com/cloud_cost_management/reporting/explorer.md

# Source: https://docs.datadoghq.com/tracing/error_tracking/explorer.md

---
title: Error Tracking Explorer
description: Learn about the Error Tracking Explorer.
breadcrumbs: Docs > APM > Error Tracking for Backend Services > Error Tracking Explorer
source_url: https://docs.datadoghq.com/error_tracking/explorer/index.html
---

# Error Tracking Explorer

## Overview{% #overview %}

{% image
   source="https://datadog-docs.imgix.net/images/error_tracking/error-tracking-overview-2.aa2160eb75631cb79d8401f9448cc71f.png?auto=format"
   alt="The details of an issue in the Error Tracking Explorer" /%}

The Error Tracking Explorer allows you to view, filter, and investigate issues. An issue is a group of similar errors related to the same bug. Datadog creates issues by computing a fingerprint for each error using some of its attributes such as the error type, the error message, or the stack trace. Errors with the same fingerprint are grouped together in the same issue.

## Explore your issues{% #explore-your-issues %}

Each item listed in the Error Tracking Explorer is an issue that contains high-level information about the error, including the following:

- The error type and the error message
- The path to the file in which underlying errors are fired
- Important information about the issue's lifetime:
  - When it was first and last seen
  - Graph of occurrences over time
  - Number of occurrences in the selected time period

Issue are also tagged as:

- `New` if the issue was first seen less than two days ago and is in state **FOR REVIEW** (see [Issue States](https://docs.datadoghq.com/error_tracking/issue_states))
- `Regression` if the issue was **RESOLVED** and occurred again in a newer version (see [Regression Detection](https://docs.datadoghq.com/error_tracking/regression_detection))
- `Crash` if the application crashed
- Having a [Suspected Cause](https://docs.datadoghq.com/error_tracking/suspected_causes)

### Time range{% #time-range %}

{% image
   source="https://datadog-docs.imgix.net/images/real_user_monitoring/error_tracking/time_range.f4fd26f0076aefc5cfb1f0baf31e1bcb.png?auto=format"
   alt="Error Tracking Time Range" /%}

The time range appears on the top right of the Explorer as a timeline. This feature allows you to display issues having error occurrences within the selected time period. Change the time range by selecting a preset range from the dropdown.

### Sorting{% #sorting %}

Order issues in the list using one of these options:

- **Relevance** combines multiple issue features to prioritize code related, recent, or spiking issues. Error Tracking analyzes how old issues are, occurrences over the last day, notable increase over the past hour, or if they triggered an application crash.
- **Count** sorts issues based on the total count of occurrences over the selected time range.
- **Newest** orders issues by when they were first seen.
- **Impacted Sessions** sorts issues by the number of impacted [RUM sessions](https://docs.datadoghq.com/real_user_monitoring/explorer/search/#event-types).

### Facets{% #facets %}

{% image
   source="https://datadog-docs.imgix.net/images/error_tracking/facets-panel.ce8f6bca3d77131e90d542e4d67e7355.png?auto=format"
   alt="Error Tracking Facets" /%}

Error Tracking automatically indexes a predefined list of attributes from your issues and creates facets out of it. A facet displays all the distinct members of an attribute for the selected time period and provides some basic analytics, such as the number of issues represented. Facets allow you to pivot or filter your issues based on the given attribute.

Some commonly used error attributes include:

| Attribute        | Description                                                                                                                                                                                                                                                                                 |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `error.message`  | The message associated with the error.                                                                                                                                                                                                                                                      |
| `error.type`     | The type or class of the error.                                                                                                                                                                                                                                                             |
| `error.stack`    | The stack trace associated with the error.                                                                                                                                                                                                                                                  |
| `error.handling` | Indicates whether the error was handled. APM errors are considered `handled` if a parent span reports a successful operation (`HTTP 200`, `gRPC OK`) or successful error handling (`HTTP 400`, `gRPC NOT_FOUND`). RUM errors are `unhandled` if they are not captured manually in the code. |

Click the Edit icon to see the list of available facets that you can show or hide from view.

{% image
   source="https://datadog-docs.imgix.net/images/error_tracking/error-tracking-facets.795e793715c6f18a031d70c3782dfb1e.png?auto=format"
   alt="Click the pencil icon to hide or show available Error Tracking facets from view." /%}

### Issue level filters{% #issue-level-filters %}

In addition to error events, Error Tracking offers issue level filters to refine the list of displayed issues.

{% image
   source="https://datadog-docs.imgix.net/images/error_tracking/issue-level-filters.748f86bee032ee6e4d9de2a5bf4dae3a.png?auto=format"
   alt="Issue level filters in Error Tracking" /%}

#### Sources{% #sources %}

Error Tracking consolidates errors from multiple Datadog products (Rum, Logs, APM) into a unified view, allowing you to watch and troubleshoot errors across your entire stack. You can choose to display **All**, **Browser**, **Mobile**, or **Backend** issues in the explorer.

For more granular filtering, you can narrow down issues by specific log sources or by SDK and scope to a programming language.

#### Fix available{% #fix-available %}

Display only issues that have an AI generated fix available to quickly remediate problems.

#### Teams filters{% #teams-filters %}

[Issue Team Ownership](https://docs.datadoghq.com/error_tracking/issue_team_ownership) helps you quickly identify issues relevant to your team by using Git `CODEOWNERS` and service owners.

#### Assigned to{% #assigned-to %}

Track and assign issues to yourself or the most knowledgeable team members, and easily refine the issue list by assignee.

#### Suspected Cause{% #suspected-cause %}

[Suspected Cause](https://docs.datadoghq.com/error_tracking/suspected_causes) enables quicker filtering and prioritization of errors, empowering teams to address potential root causes more effectively.

## Inspect an issue{% #inspect-an-issue %}

Click on any issue to open the issue panel and see more information about it.

{% image
   source="https://datadog-docs.imgix.net/images/real_user_monitoring/error_tracking/issue_summary.92d2c1becbf74ec0a501c2d000347b21.png?auto=format"
   alt="Upper part of the Error Tracking issue panel offering a summarized view of the issue" /%}

The high-level details you need when troubleshooting an issue can be found in the upper part of the panel. From here, you can understand its lifecycle: first and last occurrence dates, total count, as well as the count over time for the given issue.

{% image
   source="https://datadog-docs.imgix.net/images/real_user_monitoring/error_tracking/error_sample.ea9f7fe4d03b1dc6e8d6db8e77f2bf67.png?auto=format"
   alt="Lower part of the Error Tracking issue panel offering error samples" /%}

The information shown in the issue panel varies depending on the error source. For example, an issue created from APM errors shows the error span tags, such as the resource or operation name, with direct access to the related trace or to logs that are linked to it.

The lower part of the issue panel gives you the ability to navigate error samples from the related issue. Each error sample gives you troubleshooting information such as the stack trace of the error, and the characteristics of impacted users.

## Get alerted on new or impactful errors{% #get-alerted-on-new-or-impactful-errors %}

Seeing a new issue as soon as it happens gives you the chance to proactively identify and fix it before it becomes critical. Error Tracking monitors allow you to track any new issue or issues that have a high impact in your systems or on your users (see [Error Tracking Monitors](https://docs.datadoghq.com/monitors/types/error_tracking))

You can directly export your search query from the explorer to create an Error Tracking Monitor on the related scope:

{% video
   url="https://datadog-docs.imgix.net/images//error_tracking/create-monitor.mp4" /%}

## Further Reading{% #further-reading %}

- [Learn about Error Tracking Monitors](https://docs.datadoghq.com/monitors/types/error_tracking)
