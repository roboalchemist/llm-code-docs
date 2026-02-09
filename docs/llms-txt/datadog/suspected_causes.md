# Source: https://docs.datadoghq.com/error_tracking/suspected_causes.md

---
title: Suspected Causes
description: Learn about suspected causes in backend Error Tracking.
breadcrumbs: Docs > Error Tracking > Suspected Causes
---

# Suspected Causes

## Overview{% #overview %}

Datadog assigns a suspected cause label to issues at creation time. The suspected cause label represents the first hypothesis a developer may have about the root cause of an error. This initial classification helps teams streamline their troubleshooting efforts and enhance their understanding of recurring problems.

The suspected cause can be one of the following categories:

- **Code Exception**: An error was caused by a flaw in the code.
- **Failed Request**: An API endpoint responded with an error status code.
- **Illegal Object Access**: The code accessed an object that was null or undefined.
- **Invalid Argument**: A function was called with an invalid argument.
- **Network**: A server took long to respond, or the network was slow.

Suspected causes can be used as filters in search, enabling you to locate relevant issues.

{% image
   source="https://datadog-docs.imgix.net/images/error_tracking/suspected-cause.aade69fc1863e5cb8eeb04260bae7ca8.png?auto=format"
   alt="Filter your search by the suspected cause." /%}

### Updating suspected cause labels{% #updating-suspected-cause-labels %}

Suspected causes can be manually edited if they are deemed incorrect, allowing for continuous improvement of the labeling process.

To update the suspected cause, click the label and select a different one.

{% image
   source="https://datadog-docs.imgix.net/images/error_tracking/suspected-cause-labels.37c0e20f3bd6781d17b1497ef2a03520.png?auto=format"
   alt="Update the suspected cause label." /%}

## Further Reading{% #further-reading %}

- [Learn about Error Tracking Monitors](https://docs.datadoghq.com/error_tracking/monitors)
