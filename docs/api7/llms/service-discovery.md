# Source: https://docs.api7.ai/enterprise/best-practices/service-discovery.md

# Source: https://docs.api7.ai/enterprise/3.2.16.7/best-practice/service-discovery.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/best-practice/service-discovery.md

# Source: https://docs.api7.ai/enterprise/3.2.16.5/best-practice/service-discovery.md

# Source: https://docs.api7.ai/enterprise/3.2.16.4.1/best-practice/service-discovery.md

# Source: https://docs.api7.ai/enterprise/3.2.15.2.1/best-practice/service-discovery.md

# Source: https://docs.api7.ai/enterprise/3.2.14.6/best-practice/service-discovery.md

# Source: https://docs.api7.ai/enterprise/3.8.x/best-practices/service-discovery.md

# Source: https://docs.api7.ai/enterprise/3.7.x/best-practices/service-discovery.md

# Source: https://docs.api7.ai/enterprise/3.6.x/best-practices/service-discovery.md

# Source: https://docs.api7.ai/enterprise/3.5.x/best-practices/service-discovery.md

# Source: https://docs.api7.ai/enterprise/3.4.x/best-practices/service-discovery.md

# Source: https://docs.api7.ai/enterprise/3.3.x/best-practices/service-discovery.md

# Use Service Discovery for Upstream

Instead of configuring the upstream directly, service discovery mechanisms like Consul, Eureka, Nacos, or Kubernetes Service Discovery can be used to dynamically detect upstream nodes.

info

Once published, a service cannot directly switch between configured upstream nodes and service discovery. Instead, you have to configure this through a [canary deployment](https://docs.api7.ai/enterprise/3.3.x/getting-started/canary-upstream.md).

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

1. [Install API7 Enterprise](https://docs.api7.ai/enterprise/3.3.x/getting-started/install-api7-ee.md).
2. [Have at least one gateway instance](https://docs.api7.ai/enterprise/3.3.x/getting-started/add-gateway-instance.md) in your gateway group.

## Kubernetes[â](#kubernetes "Direct link to Kubernetes")

### Add Service Registry Connection[â](#add-service-registry-connection "Direct link to Add Service Registry Connection")

1. Select **Service Registries** of your gateway group from the side navigation bar, then click **Add Service Registry Connection**.
2. From the dialog box, do the following:

* In the **Name** field, enter `Registry for Test`.
* In the **Discovery Type** field, choose `Kubernetes`.
* Fill in the **API Server Address** and **Token Value** fields.
* Click **Add**.

3. Wait to make sure the status of the service registry is `Healthy`.

### Configure Upstream[â](#configure-upstream "Direct link to Configure Upstream")

1. Select **Published Services** under your gateway group from the side navigation bar and then click **Add Service**.

2. Select **Add Manually**.

3. From the **Add Service** dialog box, do the following:

   * In the **Name** field, enter `httpbin`.
   * In the **Service Type** field, choose `HTTP (Layer 7 Proxy)`.
   * In the **Upstream Scheme** field, choose `HTTP`.
   * In the **How to find the upstream** field, choose `Use Service Discovery`.
   * In the **Service Registry** field, choose `Registry for Test`, then choose the **Namespace** and **Service Name**.

4. Click **Add**. This will create a new service in the 'No Version' state.

Below is an interactive demo that provides a hands-on introduction to connecting Kubernetes service discovery. You will gain a better understanding of how to use it in API7 Gateway by clicking and following the steps.

## Nacos[â](#nacos "Direct link to Nacos")

### Add Service Registry Connection[â](#add-service-registry-connection-1 "Direct link to Add Service Registry Connection")

1. Select **Service Registries** of your gateway group from the side navigation bar, then click **Add Service Registry Connection**.
2. From the dialog box, do the following:

* In the **Name** field, enter `Registry for Test`.
* In the **Discovery Type** field, choose `Nacos`.
* In the **Hosts** field, fill in the host address and port.
* In the **How to Get Token** field, choose a way to get the token and configure related parameters.
* Click **Add**.

3. Wait to make sure the status of the service registry is `Healthy`.

### Configure Upstream[â](#configure-upstream-1 "Direct link to Configure Upstream")

1. Select **Published Services** under your gateway group from the side navigation bar and then click **Add Service**.

2. Select **Add Manually**.

3. From the **Add Service** dialog box, do the following:

   * In the **Name** field, enter `httpbin`.
   * In the **Service Type** field, choose `HTTP (Layer 7 Proxy)`.
   * In the **Upstream Scheme** field, choose `HTTP`.
   * In the **How to find the upstream** field, choose `Use Service Discovery`.
   * In the **Service Registry** field, choose `Registry for Test`, then choose the **Namespace**, **Group**, and **Service Name**.

4. Click **Add**. This will create a new service in the 'No Version' state.

Below is an interactive demo that provides a hands-on introduction to connecting Nacos service discovery. You will gain a better understanding of how to use it in API7 Gateway by clicking and following the steps.

## Additional Resources[â](#additional-resources "Direct link to Additional Resources")

* Key Concepts

  <!-- -->

  * [Services](https://docs.api7.ai/enterprise/3.3.x/key-concepts/services.md)
  * [Upstreams](https://docs.api7.ai/enterprise/3.3.x/key-concepts/upstreams.md)
