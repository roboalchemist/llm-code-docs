# Source: https://archivedocs.stackstate.com/5.1/getting_started.md

# Getting Started

Hi! So, you've just installed StackState and you are ready to get started.

## StackPacks

The first step to take is integrating StackState with your IT systems. This can be done by installing one or more [StackPacks](https://archivedocs.stackstate.com/5.1/stackpacks/about-stackpacks).

![StackPacks overview](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-82251bc9fd09baef670f38bb4afa3ef17fc55810%2Fv51_stackpacks.png?alt=media)

## Explore topology

After setting up an [integration](https://archivedocs.stackstate.com/5.1/stackpacks/integrations), you can go to the [Explore Mode](https://archivedocs.stackstate.com/5.1/use/stackstate-ui/explore_mode) to explore your IT landscape or visit a specific [view](https://archivedocs.stackstate.com/5.1/use/stackstate-ui/views/about_views) from your installed StackPacks.

StackState visualizes components in the Topology Perspective by the layer and domain that they're placed in. These are logical groupings of components. Layers are displayed on the vertical axis. Domains are displayed on the horizontal axis.

You can change which part of the landscape you are viewing (for example, layers and domains) with the [view filters](https://archivedocs.stackstate.com/5.1/use/stackstate-ui/filters) on the left bar, or by [hovering over a component](https://archivedocs.stackstate.com/5.1/use/stackstate-ui/perspectives/topology-perspective#component-context-menu).

➡️ [Learn more about the Topology Perspective](https://archivedocs.stackstate.com/5.1/use/stackstate-ui/perspectives/topology-perspective)

![Explore topology](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-5d790c4ec25efa8cd916c20583c97fb0c06feff7%2Fv51_topology.png?alt=media)

## Topology elements

A topology consists of components and relations combined with their health state. Because topologies can get very large, StackState automatically groups the components.

The health state of a component is indicated by two colors:

* The component color indicates the health state calculated for the component itself.
* The outer color indicates there is potential impact from unhealthy components or relations that this component depends upon.

The direction of a relation's arrow indicates dependency. For example, `app -> db` means: `app` depends on `db`. Health propagates in the opposite direction to the arrows. So if the `db` component turns red, the outer color of the `app` component will turn red too.

➡️ Learn more about [components](https://archivedocs.stackstate.com/5.1/use/concepts/components), [relations](https://archivedocs.stackstate.com/5.1/use/concepts/relations) and [health state](https://archivedocs.stackstate.com/5.1/use/concepts/health-state)

![Component](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-fe8fd3a959b634ea1397a94249f77183ce0488cc%2Fv51_topology_elements.png?alt=media)

## Timeline

The [timeline](https://archivedocs.stackstate.com/5.1/use/stackstate-ui/timeline-time-travel) at the bottom of the screen gives you the ability to go to any point in time. All the information that you see (component details, metric streams, etc.) is relative to the topology that existed at the currently selected topology time. Normally, StackState is in **live mode**, this means that StackState automatically displays the latest state of the stack.

➡️ [Learn more about the timeline and time travel](https://archivedocs.stackstate.com/5.1/use/stackstate-ui/timeline-time-travel)

![Timeline](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-e3fcd32d013c0f05707d982e36fd6b2681a0f1b9%2Fv51_timeline.png?alt=media)

## Detailed information about components and relations

Select a component or a relation to display detailed information about it in the right panel details tab - the tab will be named according to the element type that you selected. For example, **Component details** when you select a component or **Direct relation details** when you select a relation that links two components with no hidden components in between. Click **SHOW ALL PROPERTIES** to open a popup with all details of a component or direct relation.

![Detailed component information](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-b7a010ea524fd780d92aa5608414a9335b284168%2Fv51_component_details.png?alt=media)

## Telemetry inspector

Both components and relations can have one or multiple telemetry streams. The most common type is a metric stream also known as time series. If you click on a metric stream, you can see the metric stream in a popup.

![Telemetry inspector](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-cf41e4a1621af43850ea67ad1033ed5d928d5bb8%2Fv51_component_details_inspect_metric_stream.png?alt=media)

If you click on a log stream, you can see the log stream in a popup. Again, there are a number of drill-down capabilities available on the left of the popup.

![Telemetry inspector](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-e33113f9b5ee15eeee0424ce0f8d0b79e855915a%2Fv51_component_details_inspect_log_stream.png?alt=media)

## Problems

![Detailed component information](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-3abbb7283184a64b683e094910af9f78cc02532d%2Fv51_problem_summary.png?alt=media)

To quickly find the cause of any DEVIATING component, head to the right panel in the StackState UI where you can find the **Problems** section. It provides an immediate understanding of ongoing problems in your IT environment clustered by their root cause and will show you the probable cause of current problems.

* The **View summary** and **Subview summary** tabs give an overview of problems based on the components impacted in the current view or subview.
* The **Component details** lists all problems that involve the selected component.
* The **Direct relation details** tab lists all problems that involve the selected direct relation, its source component or its target component.

Problems and issues are displayed in order of the last problem update with the most recently updated problem at the top of the list and the oldest update at the bottom. Within each problem, component-specific issues are displayed in order of the timestamp of the last health state change, from the most recent at the top of the list to the oldest at the bottom.

Note that some components listed in the problem panel might not be visible in the current topology view. You can open a dedicated problem subview to focus on all of the topology elements involved in a specific problem.

➡️ [Learn more about problems](https://archivedocs.stackstate.com/5.1/use/problem-analysis/about-problems)

## Events

To show all events for the selected Topology, select the Events Perspective from the top of the screen. Examples of important events that may appear here are health state changes and changes to the components themselves, like version changes. With [event handlers](https://archivedocs.stackstate.com/5.1/use/events/event-notifications), you can configure StackState to react to any events, for example, by automatically creating a ticket or triggering some automation.

![Events Perspective](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-1fc60b6e12206fee18e7b7e47bb143bd06b1a55d%2Fv51_events-perspective.png?alt=media)

The Events Perspective isn't the only place you can find events; you can find the latest events in the Events section in the right panel **View summary** tab and in the details tabs - **Component details** and **Direct relation details**.

![Events section](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-3d4e87212164d52066ce577bf036874a8e32f2e2%2Fv51_events-section.png?alt=media)

➡️ [Learn more about the Events Perspective](https://archivedocs.stackstate.com/5.1/use/stackstate-ui/perspectives/events_perspective)
