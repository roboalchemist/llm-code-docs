# Source: https://archivedocs.stackstate.com/5.1/use/concepts/components.md

# Components

## Overview

A component is anything that has a run-time state and some relation with other components. Some component examples are a load balancer, a database server, a network switch, or a business service. It's possible to define custom components, and they can be anything - the granularity and range can be defined according to the needs. Each component is of a specific type. Types can be configured.

A component consists of:

1. The name of the component.
2. An icon in the middle that represents either the component itself or the component type.
3. The component color represents the component's [own health state](https://archivedocs.stackstate.com/5.1/use/health-state#element-own-health-state).
4. An outer color indicates an unhealthy [propagated health state](https://archivedocs.stackstate.com/5.1/use/health-state#element-propagated-health-state) (`DEVIATING` or `CRITICAL`). The propagated health state is calculated based on the health state of components or relations that the component depends upon.

![](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-fe8fd3a959b634ea1397a94249f77183ce0488cc%2Fv51_topology_elements.png?alt=media)

## Component details

![Component details](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-b7a010ea524fd780d92aa5608414a9335b284168%2Fv51_component_details.png?alt=media)

Select a component in the visualizer to display detailed information about it in the right panel details tab - **Component details**. This includes:

* **Properties** - metadata, such as the component name, type and any labels. Click SHOW ALL PROPERTIES to open a pop-up with all details of the component, including the YAML definition.
* **Relations** - the number of other components that the component is connected to, note that this will also include any connections the component has with components that sit outside the current view. Expand to see details of each [relation](https://archivedocs.stackstate.com/5.1/use/concepts/relations).
* **Actions** - the available [actions](https://archivedocs.stackstate.com/5.1/stackstate-ui/perspectives/topology-perspective#actions) for the component.
* **Health** - reports the component [health state](https://archivedocs.stackstate.com/5.1/use/concepts/health-state) as calculated by StackState. Expand to see all [health checks](https://archivedocs.stackstate.com/5.1/use/checks-and-monitors/checks) and [monitors](https://archivedocs.stackstate.com/5.1/use/checks-and-monitors/monitors) attached to the component.
* **Propagated health** - reports the component's [propagated health state](https://archivedocs.stackstate.com/5.1/use/health-state#element-propagated-health-state). This is derived from the health state of the components and relations that the component depends upon.
* **Run state** - the [run state](https://archivedocs.stackstate.com/5.1/use/health-state#run-state) of the component (when available).
* **Problems** - lists all [problems](https://archivedocs.stackstate.com/5.1/use/problem-analysis/about-problems) that involve the selected component.
* **Events** - the latest 10 [events](https://archivedocs.stackstate.com/5.1/use/events/about_events) that relate to the selected component. Click VIEW ALL to open the Events perspective in a [subview](https://archivedocs.stackstate.com/5.1/stackstate-ui/views/about_views#subview) containing only the selected component.
* **Telemetry** - all [telemetry streams](https://archivedocs.stackstate.com/5.1/use/metrics/telemetry_streams) linked to the component.

## Grouping

Components of the same type or state can optionally be grouped together into a single element. Grouped components are represented by a circle in the topology visualization. The component group will be named `<COMPONENT_TYPE> group`. For example a group of components with type `pod` will be named `pod group`.

The size of the component group's circle in the topology visualization represents the number of components in the group:

* Less than 100 components = small circle
* 100 to 150 components = medium circle
* More than 150 components = large circle

The way in which components are grouped can be customized in the [view visualization settings](https://archivedocs.stackstate.com/5.1/stackstate-ui/views/visualization_settings#components-grouping).

## See also

* [Topology perspective](https://archivedocs.stackstate.com/5.1/use/stackstate-ui/perspectives/topology-perspective)
* [Relations](https://archivedocs.stackstate.com/5.1/use/concepts/relations)
* [View visualization settings](https://archivedocs.stackstate.com/5.1/use/stackstate-ui/views/visualization_settings)
