# Source: https://archivedocs.stackstate.com/5.1/use/metrics/top-metrics.md

# Top metrics

## Overview

When you hover the mouse pointer over a component in the Topology Perspective, the component context menu is displayed. Here you will find a list of the three top metrics for the component, together with the most recently retrieved metric value. Click the metric name to open the associated metric stream in the [telemetry inspector](https://archivedocs.stackstate.com/5.1/use/metrics/browse-telemetry).

![Top metrics](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-0a8d9c3b247a7c588d50c75359846ce66bf1daed%2Fv51_component_context_menu.png?alt=media)

## Change the displayed metrics

The metrics displayed are taken from the three metric streams displayed at the top of the **Telemetry** list. The order of the **Telemetry** list is defined by the **Priority** assigned to each telemetry stream and then by the name of the telemetry stream. To change the top metrics displayed in the component context menu, [set the telemetry stream priority](https://archivedocs.stackstate.com/5.1/use/metrics/set-telemetry-stream-priority) to fit the desired order of the **Telemetry** list.

![Top metrics and telemetry streams](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-a418c3189efc3612d6e9a05038f3d1ecce6ef4e5%2Fv51_top_metrics_streams.png?alt=media)

## Reported metric values

The metric values displayed are the current metric value of the associated metric stream. If no value is available, or the last received metric is more than a few seconds old, `n/a` will be displayed. Click the metric name to open the stream in the [telemetry inspector](https://archivedocs.stackstate.com/5.1/use/metrics/browse-telemetry) and browse all retrieved values.

## See also

* [Component context menu](https://archivedocs.stackstate.com/5.1/stackstate-ui/perspectives/topology-perspective#component-context-menu)
* [Telemetry inspector](https://archivedocs.stackstate.com/5.1/use/metrics/browse-telemetry)
* [Set telemetry stream priority](https://archivedocs.stackstate.com/5.1/use/metrics/set-telemetry-stream-priority)
