# Source: https://archivedocs.stackstate.com/views/k8s-view-structure.md

# View structure

## Overview

A view in StackState allows you to monitor and inspect a subset of your IT environment. The structure of a view is tailored towards filtering and visualizing the data in that subset (view) in an efficient way.

### Filters

The **Filters** menu on the top right corner of the view UI allows you to filter the components (topology), events and traces displayed in a view. Once applied, the filters will affect the content of all the perspectives in a view.

* [Filters](https://archivedocs.stackstate.com/views/k8s-view-structure/k8s-filters) - Filter the components (topology), events and traces in your view

### Perspectives

The **Perspectives** of a view are displayed as tabs on the top left corner of the view UI and allow you to visualize all the data in a view through different lenses:

* [Overview perspective](https://archivedocs.stackstate.com/views/k8s-view-structure/k8s-overview-perspective) or [Highlights perspective](https://archivedocs.stackstate.com/views/k8s-view-structure/k8s-highlights-perspective) - depending on the type of view you are in
* [Topology perspective](https://archivedocs.stackstate.com/views/k8s-view-structure/k8s-topology-perspective) - the dependency map of the view components
* [Events perspective](https://archivedocs.stackstate.com/views/k8s-view-structure/k8s-events-perspective) - all the events happening on the topology
* [Metrics perspective](https://archivedocs.stackstate.com/views/k8s-view-structure/k8s-metrics-perspective) - key metrics for the most relevant components
* [Traces perspective](https://archivedocs.stackstate.com/views/k8s-view-structure/k8s-traces-perspective) - the tracing information running on the topology

{% hint style="info" %}
**All the perspectives** will update their content based on the [timeline](https://archivedocs.stackstate.com/views/k8sts-timeline-time-travel) configuration.
{% endhint %}

![Overview cards layout](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-6fddd5b0f2d8d4dc45641c2360bf605f3cc4c6f6%2Fk8s-overview-perspective-cards-layout.png?alt=media)
