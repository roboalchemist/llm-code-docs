# Source: https://docs.salad.com/container-engine/explanation/container-groups/container-groups.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Container Groups

*Last Updated: October 15, 2024*

Container Groups are fundamental to the deployment process within the SaladCloud Environment (SCE). They consist of a
container image, hardware requirements, and a replica count, playing a crucial role in deploying your application on the
SaladCloud network. As the owner of the Container Group, you have the responsibility to manage it, while SCE takes care
of running the group and maintaining the desired replica count.

## Container Group Components

* **[Container Registry and Image](/container-engine/explanation/infrastructure-platform/container-registries)**:
  Specify the container image you want to run in the Container Group. Use public or private images from most container
  registries.
* **Resource Requirements**:
  * **Replica Count**: Replicas are the desired number of instances for your container group deployment. We recommend
    that you deploy with 3+ replicas during testing, and 5+ replicas in production to ensure the uptime of your
    deployment.
    * **Why multiple replicas?**: For enhanced reliability and smoother operation, we strongly recommend deploying with
      a minimum of 3 replicas. This ensures your applications remain resilient and maintain performance, even when a
      node becomes temporarily unavailable. Scaling beyond a single node not only increases fault tolerance but also
      optimizes resource allocation and load balancing across our distributed cloud infrastructure. Start with 3 or more
      replicas to unlock the full potential of our platform and experience seamless scaling and improved uptime for your
      containers.
  * **Number of vCPUs (1-16)**: \*Define the desired number of virtual CPUs for your container.
  * **Memory (RAM) (1-60GB)**: Specify the amount of RAM required for your container.
  * **GPU Class**: Define the type of GPU to be used. Each container instance will have 1 GPU attached. If you select
    multiple GPU classes, the system will assign the first available GPU class to new container instances.

<img src="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-select-hardware.png?fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=84e9756027f3692b9444ef53dc1d4e5d" data-og-width="566" width="566" data-og-height="1134" height="1134" data-path="container-engine/images/portal-select-hardware.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-select-hardware.png?w=280&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=5c676c13a38427b3fb0d7e9ef45c758b 280w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-select-hardware.png?w=560&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=892b67f26ef553ec2a4d707ce87ea34b 560w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-select-hardware.png?w=840&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=9f1ed6185d13444a60eef0a64e5d2ad1 840w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-select-hardware.png?w=1100&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=927505d92e92af60414872e37bed1d0b 1100w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-select-hardware.png?w=1650&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=634a96c81df8d41ef8be2a6ed16d5b62 1650w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-select-hardware.png?w=2500&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=07bac022f2518a226917b3564f33a838 2500w" />

## Additional Configuration

* **[Environment Variables](/container-engine/how-to-guides/environment-variables)**: Define environment variables to
  customize your container's environment. You can do this via the key-value editor, or via the bulk editor.
  <img src="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-environment-variables-key-value-edit.png?fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=106d8d158c940dfe95de7a0009fe230b" alt="" data-og-width="665" width="665" data-og-height="269" height="269" data-path="container-engine/images/portal-environment-variables-key-value-edit.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-environment-variables-key-value-edit.png?w=280&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=ac399d2ff2aab2271a92b7949e88d805 280w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-environment-variables-key-value-edit.png?w=560&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=0ad6592321bd6319b63b455944ef513c 560w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-environment-variables-key-value-edit.png?w=840&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=a9e0a4c794543d4fe8d3262549885760 840w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-environment-variables-key-value-edit.png?w=1100&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=4a944dd7173e4b9224e821ef99d40689 1100w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-environment-variables-key-value-edit.png?w=1650&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=67c6f1183749a0af65fb4baeef5b9692 1650w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-environment-variables-key-value-edit.png?w=2500&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=89c6396fc49551580a2ee27cd27c97ef 2500w" />
  <img src="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-environment-variables-bulk-edit.png?fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=3f8d33fbd3cb22829edc5f3212755718" alt="" data-og-width="664" width="664" data-og-height="408" height="408" data-path="container-engine/images/portal-environment-variables-bulk-edit.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-environment-variables-bulk-edit.png?w=280&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=c2f80cc96bb2f83fbf5a4cb82f438a48 280w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-environment-variables-bulk-edit.png?w=560&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=6f28ebd739876a586dc9592f6863a3da 560w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-environment-variables-bulk-edit.png?w=840&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=10d2169a6f5bcda8e68d0de3f8b95ded 840w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-environment-variables-bulk-edit.png?w=1100&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=e0a83764266556920ab012bf794600c0 1100w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-environment-variables-bulk-edit.png?w=1650&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=e9499ab60724363ca45cbcfa6ff1f696 1650w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-environment-variables-bulk-edit.png?w=2500&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=e6d4b610e783014018a04eb27e9d7966 2500w" />
* **[Command](/container-engine/how-to-guides/specifying-a-command)**: Specify the command to run when the container
  starts. This command will override the default command and entrypoint specified in the container image.

## Monitoring and Observability

* **[Startup Probe](/container-engine/explanation/infrastructure-platform/startup-probes)**: Set up a startup probe to
  check if the container has started as expected. Recommended for all applications using the Container Gateway.
* **[Liveness Probe](/container-engine/explanation/infrastructure-platform/liveness-probes)**: Configure a liveness
  probe to check if the container is healthy. Recommended for all applications using the Container Gateway.
* **[Readiness Probe](/container-engine/explanation/infrastructure-platform/readiness-probes)**: Set up a readiness
  probe to check if the container is ready to accept traffic. Recommended for all applications using the Container
  Gateway.
* **[Container Gateway](/container-engine/explanation/infrastructure-platform/networking)**: Choose between
  authentication or no authentication for external requests and port number for enabling networking inside of container.
* **[External Logging Service](/container-engine/explanation/infrastructure-platform/external-logging)**: Optionally
  configure an external logging service for container logs. Recommended for production deployments.

<img src="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-monitoring-config.png?fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=cea0b0cd5c96083d2a137caa5ea043ec" data-og-width="611" width="611" data-og-height="837" height="837" data-path="container-engine/images/portal-monitoring-config.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-monitoring-config.png?w=280&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=0c7df7cf7639a6b85cf288fece6fb273 280w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-monitoring-config.png?w=560&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=8d1f1ce7b4bf5cbdcfa8711324d5e2af 560w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-monitoring-config.png?w=840&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=2de83a70630508f8c26d239d040161be 840w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-monitoring-config.png?w=1100&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=cf0425c83c59383d41b26f2db0268988 1100w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-monitoring-config.png?w=1650&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=309466edf40501466df692c747ac596e 1650w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-monitoring-config.png?w=2500&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=9413ba544a4a23068d9704b45077bf13 2500w" />

## Auto-Start Feature

The container deployment screen offers an auto-start feature. By default, this feature is enabled, and it automatically
starts the container group when the image is pulled. If you disable this feature, you will need to manually start the
container group after it is done pulling the image.

## Container Group Actions

Container Group actions allow you to create, manage, and modify your container deployments effectively. To access the
container group actions you first need to deploy a container.

* **Create** : Create a new Container Group. When created, it is not yet running on nodes.
* **Start** : Initiate a deployment of the Container Group on the SaladCloud network.
* **Stop**: Stop the current deployment, terminating all active Container Instances. Stopped Container Groups can be
  started again, but the deployment will be of new container group instances, not the same ones that were stopped.
* **Duplicate**: Create a copy of an existing Container Group, allowing for easy replication of settings and
  configurations.
* **Edit**: Update the display name, replica count, image source, resource requirements, and other configuration
  settings of a Container Group once it has been created.
* **Delete**: Delete a Container Group and all associated information. This action is irreversible.

<img src="https://mintcdn.com/salad/yZinoDalrD_wLP9i/container-engine/images/portal-container-group-actions.png?fit=max&auto=format&n=yZinoDalrD_wLP9i&q=85&s=eadb5b090577b0088017880ae89f1a58" data-og-width="807" width="807" data-og-height="266" height="266" data-path="container-engine/images/portal-container-group-actions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/yZinoDalrD_wLP9i/container-engine/images/portal-container-group-actions.png?w=280&fit=max&auto=format&n=yZinoDalrD_wLP9i&q=85&s=3d09d27bb9c8ce524a078a4fc61bf1eb 280w, https://mintcdn.com/salad/yZinoDalrD_wLP9i/container-engine/images/portal-container-group-actions.png?w=560&fit=max&auto=format&n=yZinoDalrD_wLP9i&q=85&s=5ba96ab6eae878ade6190fe9a4e29af3 560w, https://mintcdn.com/salad/yZinoDalrD_wLP9i/container-engine/images/portal-container-group-actions.png?w=840&fit=max&auto=format&n=yZinoDalrD_wLP9i&q=85&s=c108f48f0bc8527359b3fb4ace4275c4 840w, https://mintcdn.com/salad/yZinoDalrD_wLP9i/container-engine/images/portal-container-group-actions.png?w=1100&fit=max&auto=format&n=yZinoDalrD_wLP9i&q=85&s=775fe4563d479011dccc749af4382cd3 1100w, https://mintcdn.com/salad/yZinoDalrD_wLP9i/container-engine/images/portal-container-group-actions.png?w=1650&fit=max&auto=format&n=yZinoDalrD_wLP9i&q=85&s=c24bea655bd139cdb1f30f595625a6bd 1650w, https://mintcdn.com/salad/yZinoDalrD_wLP9i/container-engine/images/portal-container-group-actions.png?w=2500&fit=max&auto=format&n=yZinoDalrD_wLP9i&q=85&s=50cc453b8b79d004043dd14b7891697e 2500w" />
