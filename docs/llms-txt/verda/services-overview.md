# Source: https://docs.verda.com/resources/services-overview.md

# Services Overview

Verda offers a variety of services for our customers. We offer on-demand access, as well as direct and long-term access, to high-end GPU compute, CPU compute, Storage, Serverless Containers, and Managed Inference. Below is an outline of each of our services and supporting materials.

## Bare Metal

**Bare metal** contracts provide the customer with sole access to an entire physical server on a contract-only basis. These can be in an arrangement of clusters or singular full servers. For instance, a customer may book a 128-GPU H200 cluster for six months. This would be specifically prepared for the client based on their requirements and can include adjustments to some hardware specifications and additional support services.

These bare metal servers are non-virtual devices and are fully assigned to the customer. Bare Metal customers do not share their device with any other customers and are the sole tenant within the physical server. Verda is responsible for maintaining the power, networking, and physical operation of the server.

### Instant Clusters

[**Instant Clusters**](#instant-clusters) are virtualized on-demand clusters. In this arrangement, Verda is responsible for the power, networking, physical operation of the hardware, and software operation of the host machines, as well as the initial setup of the virtual machine instances comprising the cluster. However, software updates and internal configuration changes inside the virtual machine instances are the customer's responsibility.

### GPU and CPU Instances

On-demand [**GPU and CPU instances**](#gpu-and-cpu-instances) are available via the cloud console. These are available in numerous configurations with multiple GPU models, numbers of GPUs, and CPU-core counts. These instances are available as on-demand (pay per usage) or as long-term deployments (one month to two years). On-demand instances are available as:

1. Uninterruptible fixed or dynamically-priced instances,
2. Interruptible spot instances, offered at a discounted rate.

{% hint style="info" %}
Spot instances may be discontinued at any point and allocated to on-demand or other services. This may mean that a spot instance is removed even a few seconds after creation.
{% endhint %}

In contract agreements, it is possible to arrange a credit limit or outline a specific arrangement of instances instead of pre-paying for services, as is the case with our self-service agreements.

### Storage

We offer two types of **Storage** solutions, [**Block Volumes**](https://docs.verda.com/storage/block-volumes) and a [**Shared File System**](https://docs.verda.com/storage/shared-filesystems-sfs). The Block Volumes are required for the operation of an instance, as these are the OS drives. The shared file system can be accessed by multiple instances simultaneously.

### Serverless Containers

[**Serverless Containers**](https://docs.datacrunch.io/containers/overview) are a managed service in which Verda hosts and scales customers' containers. A unique endpoint with bearer-token authentication is created for each container that the customer hosts with Verda. The customer is expected to build their own services that make requests to the container endpoints.

Customers are responsible only for the internal operation of their containers. They may send traffic to the endpoint through our systems or through their services hosted elsewhere.

### Managed endpoints

The [**Inference**](#managed-endpoints) service provides API access to different models via managed endpoints that are run by Verda. Here, the customer is only responsible for the inputs they provide to such endpoints. Managed endpoints may at times rely on 3rd party APIs, which will be clearly stated in relation to each respective endpoint.
