# Source: https://docs.datadoghq.com/error_tracking/issue_states.md

# Source: https://docs.datadoghq.com/tracing/error_tracking/issue_states.md

---
title: Issue States in Error Tracking
description: >-
  Learn about the different issue states available in Error Tracking and how to
  manage error lifecycle with state transitions.
breadcrumbs: >-
  Docs > APM > Error Tracking for Backend Services > Issue States in Error
  Tracking
---

# Issue States in Error Tracking

## Overview{% #overview %}

All issues in Error Tracking have a status to help you triage and prioritize issues or dismiss noise. There are five statuses:

- **FOR REVIEW**: New or regressed issues that need attention.
- **REVIEWED**: Triaged issues that need to be fixed, now or later.
- **RESOLVED**: Issues that have been fixed and are no longer occurring.
- **IGNORED**: Issues that require no further investigation or action.
- **EXCLUDED**: Issues that require no further investigation, stops collecting new errors, and no longer count towards usage or billing

All issues start with a FOR REVIEW status. Error Tracking automatically updates the status in the cases described below, or you can manually update the status. You can also view the history of a given error's state changes.

The diagram below shows how the Error Tracking states are updated automatically and manually:

{% image
   source="https://datadog-docs.imgix.net/images/error_tracking/issue-states-diagram.5fffeb362efc2ceb4ab98070c5c295b2.png?auto=format"
   alt="Error Tracking Issue States" /%}



## Automatic review{% #automatic-review %}

Error Tracking automatically marks issues as **REVIEWED** if one of the following actions has been taken:

- The issue has been assigned
- A case has been created from the issue

{% image
   source="https://datadog-docs.imgix.net/images/error_tracking/auto-review-actions-2.724e53c17d92445c58bb9b25a6d4dc85.png?auto=format"
   alt="Error Tracking automatic review actions" /%}

## Automatic resolution{% #automatic-resolution %}

Error Tracking automatically marks issues as **RESOLVED** that appear to be inactive or resolved due to a lack of recent error occurrences:

- If the issue was last reported in a version that is more than 14 days old, and a newer version has been released but does not report the same error, Error Tracking automatically resolves the issue. Configure your services with version tags (see instructions for [APM](https://docs.datadoghq.com/tracing/services/deployment_tracking), [RUM](https://docs.datadoghq.com/real_user_monitoring/guide/setup-rum-deployment-tracking/?tab=npm), and [Logs](https://docs.datadoghq.com/getting_started/tagging/unified_service_tagging/)) to ensure that automatic resolution accounts for versions of your services.
- If `version` tags are not set up, Error Tracking automatically resolves an issue if there have been no new errors reported for that issue within the last 14 days.

**Note**: The auto-resolution logic does not take `version` into account.

## Automatic re-opening through regression detection{% #automatic-re-opening-through-regression-detection %}

See [Regression Detection](https://docs.datadoghq.com/error_tracking/regression_detection/).

## Updating the issue status{% #updating-the-issue-status %}

The issue status appears anywhere the issue can be viewed, such as in the issues list or on the details panel for a given issue. To manually update the status of an issue, click the status and choose a different one in the dropdown menu.

{% image
   source="https://datadog-docs.imgix.net/images/error_tracking/updating-issue-status.bfc2a7a35dcf0f75e1ac3353b05e0492.png?auto=format"
   alt="The Activity Timeline in the Error Tracking Issue" /%}

## Excluding an issue{% #excluding-an-issue %}

The `EXCLUDED` status lets you prevent specific errors from being tracked, ensuring they are not collected or counted toward billing. This helps you remove non-actionable errors or issues caused by expected failures without needing complex exclusion rules.

To exclude an issue, click its status and choose **EXCLUDED** in the dropdown menu. Excluded issues are still accessible in the **IGNORED** tab. You can review their history at any time.

{% image
   source="https://datadog-docs.imgix.net/images/error_tracking/issue-states-excluded.f471cbb29df20f0cef201a84d4bb2d19.png?auto=format"
   alt="Excluded in issue status dropdown" /%}

To resume collecting errors for an excluded issue, select any status other than **EXCLUDED**.

## Issue history{% #issue-history %}

View a history of your issue activity with the **Activity Timeline**. On the details panel of any Error Tracking issue, view the Activity Timeline by clicking the **Activity** tab.

{% image
   source="https://datadog-docs.imgix.net/images/error_tracking/issue-status-history.595f50475978f402b31d31ec4610e6df.png?auto=format"
   alt="The Activity Timeline in the Error Tracking Issue" /%}

## Further Reading{% #further-reading %}

- [Regression Detection](https://docs.datadoghq.com/error_tracking/regression_detection/)
