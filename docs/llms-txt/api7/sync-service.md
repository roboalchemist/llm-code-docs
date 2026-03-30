# Source: https://docs.api7.ai/enterprise/getting-started/sync-service.md

# Source: https://docs.api7.ai/enterprise/3.2.16.7/getting-started/sync-service.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/getting-started/sync-service.md

# Source: https://docs.api7.ai/enterprise/3.2.16.5/getting-started/sync-service.md

# Source: https://docs.api7.ai/enterprise/3.2.16.4.1/getting-started/sync-service.md

# Source: https://docs.api7.ai/enterprise/3.2.15.2.1/getting-started/sync-service.md

# Source: https://docs.api7.ai/enterprise/3.2.14.6/getting-started/sync-service.md

# Source: https://docs.api7.ai/enterprise/3.8.x/getting-started/sync-service.md

# Source: https://docs.api7.ai/enterprise/3.7.x/getting-started/sync-service.md

# Source: https://docs.api7.ai/enterprise/3.6.x/getting-started/sync-service.md

# Source: https://docs.api7.ai/enterprise/3.5.x/getting-started/sync-service.md

# Source: https://docs.api7.ai/enterprise/3.4.x/getting-started/sync-service.md

# Source: https://docs.api7.ai/enterprise/3.3.x/getting-started/sync-service.md

# Synchronize Services between Gateway Groups

Synchronizing [published service](https://docs.api7.ai/enterprise/3.3.x/key-concepts/services.md) versions between [gateway groups](https://docs.api7.ai/enterprise/3.3.x/key-concepts/gateway-groups.md) is a helpful part of API version control. For example:

1. When using gateway groups to isolate environments, such as test and production, you can synchronize a service version from test to production, after all tests are passed.
2. If you are using gateway groups to separate business segments, such as regions or teams, synchronizing a service can help distribute the service across multiple gateway groups.

note

* Synchronizing keeps the service version the same between gateway groups, while publishing creates a new service version each time.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

1. [Install API7 Enterprise](https://docs.api7.ai/enterprise/3.3.x/getting-started/install-api7-ee.md).
2. Configure two gateway groups - one for the initial test environment and another as the final destination (e.g., production environment) - [each with at least one gateway instance](https://docs.api7.ai/enterprise/3.3.x/getting-started/add-gateway-instance.md).
3. [Publish a service version](https://docs.api7.ai/enterprise/3.3.x/getting-started/publish-service.md) in the initial gateway group for test environment.

## Steps[â](#steps "Direct link to Steps")

* When publishing or synchronizing the same service version to different gateway groups, you can use different upstream addresses to correspond to the backend services in different environments.
* Service in "No Version" state can also be synchronized to other gateway groups. After synchronization, both gateway groups will have the same version number for the service.
* You can only synchronize the currently running service versions, not the older ones.

- Dashboard
- ADC

### Using Upstream Nodes[â](#using-upstream-nodes "Direct link to Using Upstream Nodes")

1. Select **Published Services** of your initial gateway group from the side navigation bar, then click the service version you want to synchronize, for example, `httpbin` with version `1.0.0`.
2. Click the button next to **Enable/Disable** at the page header, then select **Sync to Other Gateway Group**.
3. From the dialog box, do the following:

* In the **Gateway Group** field, choose your destination gateway group, for example, `Production Group`, and then click **Next**.

4. From the dialog box, do the following:

* In the **How to find the upstream** field, choose `Use Nodes`.

* Click **Add Node**. From the dialog box, do the following:

  <!-- -->

  * In the **Host** and **Port** fields, enter `httpbin.org` as the host and `80` as the port.
  * In the **Weight** field, use the default value `100`.
  * Click **Add**.

* Confirm the service information and then click **Sync**.

### Using Service Discovery[â](#using-service-discovery "Direct link to Using Service Discovery")

1. Select **Published Services** of your initial gateway group from the side navigation bar, then click the service version you want to synchronize, for example, `httpbin` with version `1.0.0`.
2. Click the button next to **Enable/Disable** at the page header, then select **Sync to Other Gateway Group**.
3. From the dialog box, do the following:

* In the **Gateway Group** field, choose your destination gateway group, for example, `Production Group`, and then click **Next**.

4. From the dialog box, do the following:

* In the **How to find the upstream** field, choose `Use Service Discovery`.
* In the **Service Registry** field, choose `Registry for Production`, as well as the Namespace and service name in the Registry.
* Confirm the service information and then click **Sync**.

To sync [the configuration](https://docs.api7.ai/enterprise/3.3.x/getting-started/publish-service.md#use-adc-to-publish-the-api) to `Production Group` with ADC, run:

```
adc sync -f adc.yaml --gateway-group "Production Group"
```

## Validate the APIs in Production Group[â](#validate-the-apis-in-production-group "Direct link to Validate the APIs in Production Group")

Send a request to validate the API:

```
# Replace with your production group address.
curl "http://127.0.0.1:9080/headers"
```

You should see the following response:

```
{
 "headers": {
   "Accept": "*/*",
   "Host": "httpbin.org",
   "User-Agent": "curl/7.74.0",
   "X-Amzn-Trace-Id": "Root=1-6650ab7e-32c90eba787abbeb4e3dbb0c",
   "X-Forwarded-Host": "127.0.0.1"
 }
}
```

## Additional Resources[â](#additional-resources "Direct link to Additional Resources")

* Key Concepts
  <!-- -->
  * [Services](https://docs.api7.ai/enterprise/3.3.x/key-concepts/services.md)

* Getting Started

  <!-- -->

  * [Publish Service Version](https://docs.api7.ai/enterprise/3.3.x/getting-started/publish-service.md)
  * [Rollback a Published Service](https://docs.api7.ai/enterprise/3.3.x/getting-started/rollback-service.md)

* Best Practices
  <!-- -->
  * [API Version Control](https://docs.api7.ai/enterprise/3.3.x/best-practices/api-version-control.md)
