# Source: https://archivedocs.stackstate.com/5.1/use/problem-analysis/problem_investigation.md

# Investigate a problem

## Overview

Unhealthy components in a view are grouped into [problems](https://archivedocs.stackstate.com/5.1/use/problem-analysis/about-problems) based on how they're connected in the topology. When StackState identifies a problem, this will be reported in the right panel under **Problems**.

* The **View summary** and **Subview summary** tabs list all problems that impact components in the current view or subview.
* The **Component details** tab lists all problems that involve the selected component.
* The **Direct relation details** tab lists all problems that involve the selected direct relation, its source component or its target component.

You will find the most recently updated problem at the top of the list and the problem with the oldest update at the bottom. Whenever a problem is created or updated, it will move to the top of the list. Within each problem, the involved components are listed in order of the timestamp of their last health state change, from the most recent at the top to the oldest at the bottom.

➡️ [Learn more about the problem lifecycle](https://archivedocs.stackstate.com/5.1/use/problem-analysis/problem-lifecycle)

## Detailed information about a problem

Select a problem to open detailed information about it in the right panel details tab - **Problem details**.

![View summary](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-6121e8858b32344adc1653d817403b7f6d94a527%2Fv51_problem_details_tab.png?alt=media)

The **Problem details** tab gathers together all the information you need to get started investigating a problem in your landscape:

* All [unhealthy components](https://archivedocs.stackstate.com/5.1/use/about-problems#topology-elements-in-a-problem) in the problem (the root cause and contributing causes).
* The [Probable Causes](#probable-causes) of unhealthy components - events that may have triggered the unhealthy state changes in the problem.

Click **INVESTIGATE IN SUBVIEW** to open all components in a problem in a dedicated, temporary [problem subview](#problem-subview).

## Probable causes

For each reported problem, StackState will list all events that are likely to have contributed to unhealthy state changes in the problem. These could be events of type **Anomaly**, **Element properties changed** or **Version changed** that occurred within the [problem time window](https://archivedocs.stackstate.com/5.1/use/about-problems#time-window-of-a-problem) and relate to components in the problem. If no relevant probable cause events are available in StackState, the list will be empty.

### Anomaly events

Anomaly events are generated whenever an anomaly is detected by the [Autonomous Anomaly Detector](https://archivedocs.stackstate.com/5.1/stackpacks/add-ons/aad). For metric stream anomalies, details of the metric stream where the anomaly was found are provided.

1. Select a `Metric stream anomaly` event in the Events Perspective.
   * Detailed information about the event is displayed in the right panel details tab - **Event details**.
   * The affected stream is displayed highlighting the detected anomaly.
2. Click on the metric stream graph or select **inspect** from its menu (**...**) to open the [telemetry inspector](https://archivedocs.stackstate.com/5.1/use/metrics/browse-telemetry) and inspect the stream in more detail.

![Metric stream anomaly detailed event information](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-953200d10168ddf549b5750cf5fbce519e9f87ac%2Fv51_event_metric_stream_anomaly.png?alt=media)

### Element properties changed events

Element properties changed events are generated whenever relevant properties of a component are updated at the synchronization source. For example, if AWS security rules are changed or a load balancer has increased its capacity. Exact details of the change are provided.

1. Select an `Element properties changed` event in the Events Perspective.
   * Detailed information about the event is displayed in the right panel details tab - **Event details**.
2. Click **Show all changes** in the right panel details tab.
   * A diff of the old and new properties is displayed.

![View all changes](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-77f4c19b7d0c192298a14323ac90392b59a1ce74%2Fv51_event_view_all_changes.png?alt=media)

### Version changed events

Version changed events are generated whenever the `version` property of a component is updated.

## Problem subview

A problem subview is a temporary StackState view. The filters applied to a problem subview return all components related to the problem root cause and any contributing causes within the [problem time window](https://archivedocs.stackstate.com/5.1/use/about-problems#time-window-of-a-problem). This is a larger set of components than would be shown by selecting to show the [full root cause tree](https://archivedocs.stackstate.com/5.1/stackstate-ui/perspectives/topology-perspective#show-root-cause). The following components will be included:

* **Root cause** - Each problem has a single root cause. This is the unhealthy component at the bottom of the dependency chain.
* **Contributing cause** - A problem can contain any number of contributing causes. These are all of the unhealthy components in the problem, other than the root cause.
* **Healthy components** - A number of healthy components are also included in a problem:
  * Upstream healthy dependencies of the root cause or one of the contributing causes.
  * Downstream healthy components with an unhealthy [propagated state](https://archivedocs.stackstate.com/5.1/concepts/health-state#element-propagated-health-state) that originates from either the root cause or one of the contributing causes.

Within a problem subview, you have access to all perspectives containing data specific to the problem time window and the involved components. The applied filters can be adjusted, but it isn't possible to save the subview. You can share the problem subview with other StackState users, including any modifications you have made, as a link.

To exit the Problem Subview, click the view name in the top bar of the StackState UI.

![Breadcrumbs with view name](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-8987e909165943f4a135b6f2622c22ce646099ad%2Fv51_problem_subview_breadcrumb.png?alt=media)

## See also

* [What is a problem?](https://archivedocs.stackstate.com/5.1/use/problem-analysis/about-problems)
* [Problem lifecycle](https://archivedocs.stackstate.com/5.1/use/problem-analysis/problem-lifecycle)
* [Problem notifications](https://archivedocs.stackstate.com/5.1/use/problem-analysis/problem_notifications)
* [Anomaly detection](https://archivedocs.stackstate.com/5.1/use/concepts/anomaly-detection)
