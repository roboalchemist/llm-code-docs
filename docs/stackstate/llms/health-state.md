# Source: https://archivedocs.stackstate.com/5.1/use/concepts/health-state.md

# Health state

## Overview

StackState calculates and reports the health state for elements (components and relations) and views. The following health state types are reported:

* [Element own health state](#element-own-health-state) - indicates the current health state of an element based on configured health sources.
* [Element propagated health state](#element-propagated-health-state) - highlights potential impact resulting from other unhealthy elements in the topology.
* [View health state](#view-health-state) - summarizes the health states and propagated health states of all elements in a view.

Changes to a health state will generate [events](https://archivedocs.stackstate.com/5.1/use/events/about_events) that can be used to trigger [event notifications](https://archivedocs.stackstate.com/5.1/use/events/event-notifications).

## Health sources

Health data in StackState can be derived from a number of health sources.

### StackState health checks

StackState health checks calculate a health state based on the telemetry or log streams that are defined for a topology element. This approach opens up the possibility to use the Autonomous Anomaly Detector (AAD) for anomaly health checks.

Existing StackPacks offer StackState health checks out of the box.

* [How to add a health check](https://archivedocs.stackstate.com/5.1/use/checks-and-monitors/add-a-health-check)
* [How to set up anomaly health checks](https://archivedocs.stackstate.com/5.1/use/checks-and-monitors/anomaly-health-checks)
* [About StackState checks](https://archivedocs.stackstate.com/5.1/use/checks-and-monitors/checks)

### StackState monitors

StackState monitors compute a health state based on a configured algorithm that combines and processes the 4T data collected by StackState. Health states computed this way are bound to topology elements using health synchronization.

Existing StackPacks will offer StackState monitors out of the box.

* [How to manage monitors](https://archivedocs.stackstate.com/5.1/use/checks-and-monitors/manage-monitors)
* [About StackState monitors](https://archivedocs.stackstate.com/5.1/use/checks-and-monitors/monitors)

### External monitoring systems

Health data from external monitoring systems can be sent to StackState using health synchronization. In this case, the health state is calculated by an external system based on its own rules. The calculated health state is then sent to StackState as a health stream and bound to the associated topology element. This approach is useful if you have existing health calculations defined externally, or if it isn't viable to send telemetry or events data to StackState and translate the health calculation rules.

Existing StackPacks offer health synchronization out of the box.

{% hint style="success" %}
You can set up a [custom health synchronization](https://archivedocs.stackstate.com/5.1/configure/health/health-synchronization) to integrate with external monitoring systems that aren't supported out of the box.
{% endhint %}

## Health state types

### Element own health state

StackState tracks a single own health state for each topology element (components, component groups and relations) based on information available from all of the [health sources](#health-sources) attached to it. The own health state is calculated as the most severe state reported by all health sources configured the element. If no health sources are present, an `UNKNOWN` health state will be reported.

In the StackState UI, the color of an element represents its own health state. A topology element can have any of the following health states:

* Green - `CLEAR` - There is nothing to worry about.
* Orange - `DEVIATING` - Something may require your attention. A badge on the component shows the number of health checks that are currently failing.
* Red - `CRITICAL` - Attention is needed right now, because something is broken. A badge on the component shows the number of health checks that are currently failing.
* Gray - `UNKNOWN` - No health state available.

![Health states](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-2711dc39608fbd7f0431d600c18eafd72d7a2c71%2Fv51_element-health-states.png?alt=media)

The element will also have an outer color if it has an unhealthy [propagated health state](#element-propagated-health-state).

You can find details of the calculated element own health state and all configured monitors and health checks in the StackState UI right panel details tab when information about a topology element is displayed - [Component details](https://archivedocs.stackstate.com/5.1/use/components#component-details) or [Direct relation details](https://archivedocs.stackstate.com/5.1/use/relations#relation-details) depending on the element type that you selected.

![Health states](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-766892677b7bb250bf6d00dc0a497916de23c3f1%2Fv51_element-health-details-panel.png?alt=media)

### Element propagated health state

In addition to the own health state, StackState calculates a propagated health state for each topology element (components, component groups and relations). The propagated health state is derived from the own health state of components and relations that the element depends upon.

➡️ [Learn how health state propagates in StackState](#propagation)

A topology element can have any of the propagated health states listed below:

* Orange - `DEVIATING` - Potential impact from another `DEVIATING` topology element. May require your attention.
* Red - `CRITICAL` - Potential impact from another `CRITICAL` topology element. May require your attention.
* `UNKNOWN` - No propagated health state. There is nothing to worry about.

In the StackState UI, an outer color will be shown when an element's propagated health state is calculated as unhealthy - orange for `DEVIATING` or red for `CRITICAL`.

The color of the element itself (the inner color) represents the [element own health state](#element-own-health-state).

![](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-b1098b1fe492d4914b1fe132eb906deead72da9e%2Fv51_propagated-health-states.png?alt=media)

The propagated health state of an element can also be found in the following places:

* In the right panel details tab when information about a topology element is displayed - [Component details](https://archivedocs.stackstate.com/5.1/use/components#component-details) or [Direct relation details](https://archivedocs.stackstate.com/5.1/use/relations#relation-details) depending on the element type that you selected.
* In the [component context menu](https://archivedocs.stackstate.com/5.1/stackstate-ui/perspectives/topology-perspective#component-context-menu) when you hover the mouse pointer over a component in the topology visualization.

![](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-71cf0b9653700c90be9ca6401ee13172cb8eaaee%2Fv51_stackstate-ui-propagated-health-state.png?alt=media)

### View health state

When **view health state** is enabled for a view, it will report a health state. The view health state is calculated based on the health of components and relations within in the view.

In the StackState UI, the view health state is reported as a one of four colors:

* Green - `CLEAR` - There is nothing to worry about.
* Orange - `DEVIATING` - Something may require your attention.
* Red - `CRITICAL` - Attention is needed right now, because something is broken.
* Gray - `UNKNOWN` - View health state reporting is disabled.

![Health states](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-7764072cf5ad025a87d19e039bcadbb1b2bf2c79%2Fv51_view_health_states.svg?alt=media)

➡️ [Learn how to configure view health state reporting](https://archivedocs.stackstate.com/5.1/use/stackstate-ui/views/configure-view-health)

You can check the view health state in the following places in the StackState UI:

* **Current view** - The health state of the current view is visible in the top bar of the StackState UI and also next to the view name in the right panel **View summary** tab. Historical health state information for a view can be seen in the [timeline Health](https://archivedocs.stackstate.com/5.1/stackstate-ui/timeline-time-travel#health) line at the bottom of the screen.
* **Starred views** - Starred views are listed in the StackState main menu together with their health state.
* **All views** - The health state of all views is visible on the view overview screen. Click **Views** from the StackState main menu.

![View health state in main menu](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-ded8bb620ca805d3d44646de46d3a595cc337746%2Fv51_view_health_main_menu.png?alt=media)

## Run state

Some components in StackState will report a **Run state**, for example, AWS EC2 instances. This is different to the [health state](https://archivedocs.stackstate.com/5.1/use/concepts/health-state) and indicates the component’s operational state. The run state can be `DEPLOYING`, `DEPLOYED`, `STARTING`, `STARTED`, `STOPPING`, `STOPPED` or `UNKNOWN`. It isn't used in the calculation of a component's health state.

For every change in run state, a `Run state changed` event is generated. These events are visible in the [Events Perspective](https://archivedocs.stackstate.com/5.1/use/stackstate-ui/perspectives/events_perspective) and can help to correlate changes in the deployment state of components with problems in an environment.

## Propagation

The propagated health state of an element is calculated using a propagation function. Health state will propagate from one element to the next, from dependencies to dependent elements. Note that this is the opposite direction to the arrows shown on relations in the topology visualization. A `CLEAR` (green) or `UNKNOWN` (gray) health state won't propagate.

| Dependency and propagated state                                                                                                                                                                                        | Description                                                                                                                         |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| ![](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-309dbabbbd80af1be306aa79d240aea1b88f9fb7%2Fv51_propagation_b_to_a.png?alt=media)  | Component A depends on component B. Health state will propagate from B to A.                                                        |
| ![](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-f67b698bef727334d2e09a78761f86140ec5ef41%2Fv51_propagation_a_to_b.png?alt=media)  | Component B depends on component A. Health state will propagate from A to B.                                                        |
| ![](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-a1821b313c1aa8679e19044920c091e33adb313d%2Fv51_propagation_a_and_b.png?alt=media) | Dependency in both directions. Health state will propagate from A to B and from B to A. In other words, it's a circular dependency. |
| ![](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-5f8da7aab42586b538dc03a72e6e9428e9b2df8e%2Fv51_no_propagation.png?alt=media)      | No dependency. Health state doesn't propagate.                                                                                      |

{% hint style="success" %}
You can configure [custom propagation functions](https://archivedocs.stackstate.com/5.1/develop/developer-guides/custom-functions/propagation-functions) to customize how health state affects the overall health of your systems.
{% endhint %}

## See also

* [Add a health check based on telemetry streams available in StackState](https://archivedocs.stackstate.com/5.1/use/checks-and-monitors/add-a-health-check)
* [Manage monitors](https://archivedocs.stackstate.com/5.1/use/checks-and-monitors/manage-monitors)
* [Add Static Health from a CSV file](https://archivedocs.stackstate.com/5.1/stackpacks/integrations/static_health)
* [Set up a health synchronization](https://archivedocs.stackstate.com/5.1/configure/health/health-synchronization)
* [Configure the view health](https://archivedocs.stackstate.com/5.1/use/stackstate-ui/views/configure-view-health)
