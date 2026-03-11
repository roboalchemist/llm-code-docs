# Source: https://archivedocs.stackstate.com/5.1/configure/anomaly-detection.md

# Source: https://archivedocs.stackstate.com/5.1/use/concepts/anomaly-detection.md

# Anomaly detection

## Overview

StackState can detect anomalies in your IT infrastructure by monitoring the metric streams attached to elements.

## Autonomous anomaly detection

The StackState Autonomous Anomaly Detector (AAD) StackPack works fully autonomously to identify anomalies in your IT environment. When installed and enabled, it will determine for itself the best configuration of its machine learning models and the metric streams that should be prioritized for anomaly detection. The AAD doesn't require configuration, although you can influence the selection of telemetry streams by giving them a higher priority.

Once the anomalies are identified, they're displayed in the MetricStream charts as in the example below:

![Anomaly example](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-1d38a28d94b895962673aa6ecd81ca30d609509c%2Fv51_anomaly_severity.png?alt=media)

Additionally, identified anomalies are available as StackState Events and can be viewed in the [Events Perspective](https://archivedocs.stackstate.com/5.1/use/stackstate-ui/perspectives/events_perspective) when event category `Anomalies` is selected in the filter.

![Anomaly events](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-953200d10168ddf549b5750cf5fbce519e9f87ac%2Fv51_event_metric_stream_anomaly.png?alt=media)

Finally, [anomaly health checks](https://archivedocs.stackstate.com/5.1/use/checks-and-monitors/anomaly-health-checks) can be configured for the most important metric streams to alert on problems before they occur.

➡️ [Learn more about the Autonomous Anomaly Detector](https://archivedocs.stackstate.com/5.1/stackpacks/add-ons/aad)
