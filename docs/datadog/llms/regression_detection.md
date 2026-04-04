# Source: https://docs.datadoghq.com/error_tracking/regression_detection.md

---
title: Regression Detection
description: >-
  Learn how a resolved error gets automatically re-opened through regression
  detection.
breadcrumbs: Docs > Error Tracking > Regression Detection
---

# Regression Detection

## Overview{% #overview %}

A regression refers to the unintended reappearance of a bug or issue that was previously fixed. In Datadog, resolved issues are automatically re-opened through regression detection so that you can see all the context of the issues without duplicating information.

## Automatic re-opening through regression detection{% #automatic-re-opening-through-regression-detection %}

If a **RESOLVED** error recurs in a newer version of the code, or the error occurs again in code without versions, Error Tracking triggers a regression. The issue moves to the **FOR REVIEW** state, and is tagged with a **Regression** tag:

{% image
   source="https://datadog-docs.imgix.net/images/error_tracking/regression-detection.991413da4ebb5c0f191276c9e1f74321.png?auto=format"
   alt="The details of regression in Error Tracking" /%}

Regressions take into account the versions of your service where the error is known to occur, and only trigger on new versions after an issue is marked as **RESOLVED**. Configure your services with version tags (see instructions for [APM](https://docs.datadoghq.com/tracing/services/deployment_tracking), [RUM](https://docs.datadoghq.com/real_user_monitoring/guide/setup-rum-deployment-tracking/?tab=npm), and [Logs](https://docs.datadoghq.com/getting_started/tagging/unified_service_tagging/)) to ensure that issues automatically resolve only if the same errors occur on newer versions of your services.

If you don't have version tags set up, issues are tagged with **Regression** when an error occurs on an issue marked as **RESOLVED**.

You can also set up [monitors](https://docs.datadoghq.com/monitors/types/error_tracking/) to alert you when regressions occur.

## Updating the issue status{% #updating-the-issue-status %}

The issue status appears anywhere the issue can be viewed, such as in the issues list or on the details panel for a given issue. To manually update the status of an issue, click the status and choose a different one in the dropdown menu.

{% image
   source="https://datadog-docs.imgix.net/images/error_tracking/updating-issue-status.bfc2a7a35dcf0f75e1ac3353b05e0492.png?auto=format"
   alt="The Activity Timeline in the Error Tracking Issue" /%}

## Issue history{% #issue-history %}

View a history of your issue activity with the **Activity Timeline**. On the details panel of any Error Tracking issue, view the Activity Timeline by clicking the **Activity** tab.

{% image
   source="https://datadog-docs.imgix.net/images/error_tracking/issue-status-history.595f50475978f402b31d31ec4610e6df.png?auto=format"
   alt="The Activity Timeline in the Error Tracking Issue" /%}

## Further Reading{% #further-reading %}

- [Issue States in Error Tracking](https://docs.datadoghq.com/error_tracking/issue_states/)
