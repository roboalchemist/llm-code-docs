# Source: https://archivedocs.stackstate.com/get-started/k8s-getting-started.md

# StackState walk-through

Hi! So, you've integrated your Kubernetes or OpenShift clusters and you are ready to get started.

After setting up your [integration with Kubernetes](https://archivedocs.stackstate.com/get-started/k8s-quick-start-guide), you can go open the Main menu to explore your resources. You can for example start with the Services.

## Explore your Kubernetes resources

![Main menu](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-19fe937807bace4e776906381983b93d930ca9ec%2Fk8s-quick-start-menu.png?alt=media)

This brings you to the service overview which shows all services running in your clusters. If you click any of the other items underneath Kubernetes you will go to the overview page of that type of resource. It will show all resources of that type in all clusters and all namespaces at first.

![Services overview](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-2d3ea34ee6dec527c570f5f1c7d01257df8fd418%2Fk8s-quick-start-services.png?alt=media)

At the right top, you have the option to filter your selection to a certain cluster and/ or namespace to see the resources for which you are responsible.

At the bottom left, you find two inputs.

1. The time-range selector. This selects the time range for all metrics, logs and events you see throughout the product.
2. The topology-time selector. This is used to travel back to a certain moment in time to see the exact state of your systems as observed at that moment in time.

You can for example filter on a certain namespace, in this case, I filter the services down to 'sock-shop' which is a demo application using different microservices written in different programming languages and using different ways of communication to act as a nice example for troubleshooting an issue. If you now click on Topology you will see the topology of the currently selected components (in this case the services of the sock-shop).

![Services topology](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-81c15d963107cc62715ca570af2445ac2e26aefd%2Fk8s-quick-start-service-topology.png?alt=media)

In the topology, you see all resources, in this case services.

* If you click a component (in this case a service) it shows you the details of a service including the most important metrics, in the case of a service, for example, the latency, throughput and error rate. Next to the most important metrics the health of the component is shown and expanded if there is anything going wrong.
* If you click a relation you will see the detail of the relation including all components part of it. In the case of a service map you will see all components involved in the service-to-service communication. If you want to open a component to see all details of that resource (e.g. the details of this service a certain service) you can click on the 'Open Component' button from a selected component (which you then see in the Right Hand Side panel) or you can open the component by clicking on the name of the component in the overview page tab.

![Service overview](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-2440c81ff92c653056456fb50502526eaed599d5%2Fk8s-quick-start-service.png?alt=media)

After opening a Kubernetes resource you will get a Highlight perspective showing you all the highlights of that component.

1. The component meta-data
2. The actions available on the component, in the case of a service, it gives you the ability to show the Status and/ or Configuration information. If you want to see the logs you can open the pods via the related resources which give you access to the Logs.
3. Related resources. This section shows all related resources to this resource in this case 2 other services to which it communicates and 1 pod which backs this services.
4. The monitors sections shows you all monitors applied to this Resource including their state a the selected topology-time.
5. The metrics section shows you all the important metrics for this service. The metrics include the selected telemetry-time interval.
6. A health time-line for a service shows the health of this resource over time.
7. A event time-line showing all events happening on this service over time.

Let's now explore a triggered monitor by clicking on the 'HTTP - 5xx error ratio' one.

![HTTP - 5xx error ratio triggered monitor](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-43737f4415cd4c6dc455deeaa87059d33f84f361%2Fk8s-quick-start-service-5xx-error-triggered-monitor.png?alt=media)
