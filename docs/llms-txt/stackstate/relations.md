# Source: https://archivedocs.stackstate.com/5.1/stackpacks/integrations/opentelemetry/manual-instrumentation/relations.md

# Source: https://archivedocs.stackstate.com/5.1/use/concepts/relations.md

# Relations

## Overview

A relation connects two [components or groups of components](https://archivedocs.stackstate.com/5.1/use/concepts/components). Relations have some similarities with components. Just like a component, they can have a health state and a propagated health state. In the StackState topology perspective, relations are shown as lines connecting components or component groups.

## Relation types

Relations in StackState can be either direct or indirect. The type of relation is indicated by the type of line connecting the components. Relations that connect to a component group are represented as grouped relations, these can contain a combination of direct and indirect relations and may connect to all or only some components included in the group. Select a relation in the topology visualizer to display detailed information about it in the right panel details tab - **Direct relation details**, **Indirect relation details** or **Grouped relation details** depending on the relation type that you selected.

You can customize the types of relations displayed in the [visualization settings](https://archivedocs.stackstate.com/5.1/use/stackstate-ui/views/visualization_settings).

### Direct relations

![](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-b3e059058fe8f47161a4d5ada4d5a242df15a4dd%2Fv51_relation_comp_comp.png?alt=media)

Direct relations link two components that have a direct connection to each other. A **direct relation** between two components is indicated by a solid line. The direction of the arrowhead shows the direction of the dependency. Select a direct relation to detailed information about the relation in the right panel details tab - **Direct relation details**.

#### Direct relation details

![Direct relation details](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-e1bf0cdf8dd856b72c87744b424324a0cb0f3fcc%2Fv51_direct_relation_details.png?alt=media)

The **Direct relation details** tab is shown in the StackState UI right panel when a direct relation is selected in the topology visualizer. This includes:

* **Properties** - metadata, such as the relation type and any labels. Click SHOW ALL PROPERTIES to open a pop-up with all details of the relation.
* **Components** - the source component and target component that the relation connects.
* **Health** - reports the relation [health state](https://archivedocs.stackstate.com/5.1/use/concepts/health-state) as calculated by StackState. Expand to see all [health checks](https://archivedocs.stackstate.com/5.1/use/checks-and-monitors/checks) and [monitors](https://archivedocs.stackstate.com/5.1/use/checks-and-monitors/monitors) attached to the component.
* **Propagated health** - reports the relation's [propagated health state](https://archivedocs.stackstate.com/5.1/use/health-state#element-propagated-health-state). This is derived from the health state of the components and relations that the relation depends upon.
* **Problems** - lists all [problems](https://archivedocs.stackstate.com/5.1/use/problem-analysis/about-problems) that involve the selected relation.
* **Events** - the latest 10 [events](https://archivedocs.stackstate.com/5.1/use/events/about_events) that relate to the selected relation. Click VIEW ALL to open the Events perspective in a [subview](https://archivedocs.stackstate.com/5.1/stackstate-ui/views/about_views#subview) containing only the relation component.
* **Telemetry** - all [telemetry streams](https://archivedocs.stackstate.com/5.1/use/metrics/telemetry_streams) linked to the relation.

### Indirect relations

![](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-3cd673a1173d77e59ff8e591d77ff9489aca9f4a%2Fv51_indirect_relation_comp_comp.png?alt=media)

Indirect relations link two components that are connected together via a path of invisible components. Indirect relations in a view will be displayed when **Show all indirect relations** is enabled in the [visualization settings](https://archivedocs.stackstate.com/5.1/use/stackstate-ui/views/visualization_settings). An **indirect relation** between two components is shown as a dashed line. The direction of the arrowhead shows the direction of the dependency. Select an indirect relation to view the full path between the components in the right panel details tab - **Indirect relation details**.

#### Indirect relation details

![Indirect relation details](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-0bdab45f036e5ddeb287a4f140b4e84fc79d8b4b%2Fv51_indirect_relation_details.png?alt=media)

Select an indirect relation in the topology visualizer to display detailed information about it in the right panel **Indirect relation details** tab. The full path, including all components that connect the source and the target component, is shown. From here, you can click on a component, or a relation between components, to open its associated details tab - **Component details** or **Direct relation details**.

### Grouped relations

![](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-c8c916a4c3d406c8015a0bee0d9b3130fa6b6d56%2Fv51_relation_group_comp.png?alt=media)

Relations between a component group and a component or component group are shown in the topology visualizer as a combination of a solid and a dashed line. This type of relation is called a grouped relation and could contain a combination of direct relations and indirect relations and could connect to one or more components in the component group. Select a grouped relation to display full details of the included relations in the right panel details tab - **Grouped relation details**.

#### Grouped relation details

![Grouped relation details](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-0c9b33a4f1d958d5e2f23914d0bb639520f8c56d%2Fv51_grouped_relation_details.png?alt=media)

Select a grouped relation in the topology visualizer to display detailed information about it in the right panel details tab - **Grouped relation details**. This shows all direct and indirect relations included in the group. From here, you can click on a component, or a relation between components, to open its associated details tab - **Component details**, **Direct relation details** or **Indirect relation details**.

## Relation details

![Relation details](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-e1bf0cdf8dd856b72c87744b424324a0cb0f3fcc%2Fv51_direct_relation_details.png?alt=media)

Select a relation in the visualizer to display detailed information about it in the right panel. The right panel details tab will be named **Direct relation details**, **Indirect relation details** or **Grouped relation details**, depending on the type of relation that you selected. For details of the tab content, see the relation types [direct relations](#direct-relations), [indirect relations](#indirect-relations) and [grouped relations](#grouped-relations).

## Dependencies and propagation

If a relation indicates a dependency, the line will have an arrowhead showing the direction of the dependency. A dependency could be in one direction or in both directions, indicating that two components depend on each other. For example, a network device talking to another networking device that has a bidirectional connection.

[Health state will propagate](https://archivedocs.stackstate.com/5.1/use/health-state#element-propagated-health-state) from one component to the next upwards along a chain of dependencies. If the relation doesn't show a dependency between the components it connects (no arrowhead), it can be considered as merely a line in the visualizer or a connection in the stack topology.

## See also

* [Topology perspective](https://archivedocs.stackstate.com/5.1/use/stackstate-ui/perspectives/topology-perspective)
* [Components](https://archivedocs.stackstate.com/5.1/use/concepts/components)
* [Health state propagation](https://archivedocs.stackstate.com/5.1/use/health-state#element-propagated-health-state)
* [View visualization settings](https://archivedocs.stackstate.com/5.1/use/stackstate-ui/views/visualization_settings)
