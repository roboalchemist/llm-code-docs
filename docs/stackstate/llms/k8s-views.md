# Source: https://archivedocs.stackstate.com/views/k8s-views.md

# Kubernetes views

## Overview

StackState has deep knowledge of Kubernetes and its components. After installation of the StackState agent in your cluster, it will then automatically detect and visualize the topology of your Kubernetes applications. This includes the Kubernetes resources that make up your application, such as deployments, pods, services, and ingress. It will also automatically detect and visualize the topology of your Kubernetes infrastructure that makes up your cluster, such as nodes, namespaces, and persistent volumes.

StackState has dedicated overviews and highlights pages for the following Kubernetes native resources:

![Kubernetes views](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-6a656a9b73bf6babe65af49fbbadc699e95de16e%2Fk8s-menu.png?alt=media)

All other Kubernetes resources are recognized and visualized in the topology views.

## Overview pages

The overview pages provide a high-level overview of specific Kubernetes resources in your environment. These overviews highlight the most important information about the resource, including its health, age, namespace, cluster and more.

![Overview pages](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-a4ef27705721b68a02275b0939af7abce8643fa5%2Fk8s-service-overview.png?alt=media)

From an overview page, you can click on one of the Kubernetes resources to navigate to the highlights page for that resource.

## Highlights pages

The highlights page shows an overview of the most important information about a specific Kubernetes resource. Here you can see the health of the resource, the monitors that are active on the resource, and the events that have occurred on the resource. Also we display the key metrics for the resource.

![Highlights pages](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-ebfd5f97b615eedd1e40b884e1e240fd9148e85e%2Fk8s-pod-highlights.png?alt=media)
