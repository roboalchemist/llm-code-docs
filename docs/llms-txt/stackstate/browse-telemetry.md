# Source: https://archivedocs.stackstate.com/5.1/use/metrics/browse-telemetry.md

# Browse telemetry

## Overview

The StackState UI displays a visualization of filtered data for each configured telemetry stream.

Telemetry streams are added to elements automatically when they're imported to StackState or you can manually [add a single telemetry stream](https://archivedocs.stackstate.com/5.1/use/metrics/add-telemetry-to-element) to a single component.

## Telemetry inspector

Click on any of the telemetry stream charts, or select **Inspect stream** from its context menu, to open the telemetry inspector.

![Telemetry inspector](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-3a15c71291d219bed06260e1e7a716ee931855ea%2Fv51_telemetry-inspector.png?alt=media)

Within the telemetry inspector you can adjust the selected metric as well as the filters, time window and aggregation applied to the data source.

{% hint style="info" %}
Changes made here won't be saved to the telemetry stream attached to the element.
{% endhint %}

### Anomaly feedback

When anomaly detection is enabled for a metric stream, users can give feedback on reported anomalies in the form of a thumbs-up (meaning "well spotted!") or thumbs-down (meaning "false positive"). For more elaborate feedback, it's also possible to add comments. Feedback added to anomalies will be used by the StackState team to further develop and improve the AAD. **It isn't used to train the local instance of the AAD.**

{% hint style="success" %}
In a self-hosted installation, feedback must be [exported and sent to StackState](https://archivedocs.stackstate.com/5.1/configure/anomaly-detection/export-anomaly-feedback) for the StackState team to be able to access it.
{% endhint %}

{% hint style="warning" %}
**Take care not to include sensitive data in comments.**

Comments added to an anomaly will be included in any anomaly feedback data sent to StackState.
{% endhint %}

## See also

* [Add a single telemetry stream to a component](https://archivedocs.stackstate.com/5.1/use/metrics/add-telemetry-to-element)
* [Monitor a telemetry stream with a health check](https://archivedocs.stackstate.com/5.1/use/checks-and-monitors/add-a-health-check)
* [Use templates to add telemetry streams to your own integrations](https://archivedocs.stackstate.com/5.1/configure/telemetry/telemetry_synchronized_topology)
