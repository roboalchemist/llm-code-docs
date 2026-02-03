# Source: https://docs.vespa.ai/en/operations/kubernetes/architecture.html.md

# Architecture

 

 ![Vespa Operator Architecture](/assets/img/vespa-operator-architecture.png)

The Vespa Operator is an implementation of the [Operator Pattern](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/) that extends Kubernetes with custom orchestration capabilities for Vespa. It relies on a [Custom Resource Definition](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) called a `VespaSet`, which represents a quorum of [ConfigServers](https://docs.vespa.ai/en/operations/self-managed/configuration-server.html) in a Kubernetes namespace. The Vespa Operator is responsible for the deployment and lifecycle of the `VespaSet` resource and its ConfigServers, which collectively entails the infrastructure for Vespa on Kubernetes.

[Application Packages](https://docs.vespa.ai/en/basics/applications.html) are deployed to the [ConfigServers](https://docs.vespa.ai/en/operations/self-managed/configuration-server.html) to create Vespa applications. The ConfigServers will dynamically instantiate the services as individual Pods based on the settings provided in the Application Package. After an Application Package is deployed, the ConfigServers will remain responsible for the management and lifecycle of the Vespa application.

 Copyright © 2026 - [Cookie Preferences](#)

