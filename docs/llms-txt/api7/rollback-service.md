# Source: https://docs.api7.ai/enterprise/getting-started/rollback-service.md

# Source: https://docs.api7.ai/enterprise/3.2.16.7/getting-started/rollback-service.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/getting-started/rollback-service.md

# Source: https://docs.api7.ai/enterprise/3.2.16.5/getting-started/rollback-service.md

# Source: https://docs.api7.ai/enterprise/3.2.16.4.1/getting-started/rollback-service.md

# Source: https://docs.api7.ai/enterprise/3.2.15.2.1/getting-started/rollback-service.md

# Source: https://docs.api7.ai/enterprise/3.2.14.6/getting-started/rollback-service.md

# Source: https://docs.api7.ai/enterprise/3.8.x/getting-started/rollback-service.md

# Source: https://docs.api7.ai/enterprise/3.7.x/getting-started/rollback-service.md

# Source: https://docs.api7.ai/enterprise/3.6.x/getting-started/rollback-service.md

# Source: https://docs.api7.ai/enterprise/3.5.x/getting-started/rollback-service.md

# Source: https://docs.api7.ai/enterprise/3.4.x/getting-started/rollback-service.md

# Source: https://docs.api7.ai/enterprise/3.3.x/getting-started/rollback-service.md

# Roll Back a Service

Rollbacks allow you to revert a [service](https://docs.api7.ai/enterprise/3.3.x/key-concepts/services.md) to an older version published on this [gateway group](https://docs.api7.ai/enterprise/3.3.x/key-concepts/gateway-groups.md), if the new version has issues.

note

* Older service versions do not contain any [service runtime configurations](https://docs.api7.ai/enterprise/3.3.x/key-concepts/services.md#service-runtime-configurations). Instead, the current configurations will still be used after rolling back.

* You can only roll back to a service version published on the same gateway group.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

1. [Install API7 Enterprise](https://docs.api7.ai/enterprise/3.3.x/getting-started/install-api7-ee.md).
2. [Have a historical version of the service on the gateway group](https://docs.api7.ai/enterprise/3.3.x/getting-started/publish-service.md).

## Steps[â](#steps "Direct link to Steps")

1. Select **Published Services** of your gateway group from the side navigation bar, then click the service version you want to roll back, for example, `httpbin` with version `1.2.0`.
2. Click the button next to **Enable/Disable** at the page header, then select **View History Versions**.
3. Choose version `1.0.0` and then click **Rollback**.

## Additional Resources[â](#additional-resources "Direct link to Additional Resources")

* Key Concepts

  <!-- -->

  * [Services](https://docs.api7.ai/enterprise/3.3.x/key-concepts/services.md)
  * [Gateway Groups](https://docs.api7.ai/enterprise/3.3.x/key-concepts/gateway-groups.md)

* Getting Started

  <!-- -->

  * [Publish Service Version](https://docs.api7.ai/enterprise/3.3.x/getting-started/publish-service.md)
  * [Synchronize Published Service Version between Gateway Groups](https://docs.api7.ai/enterprise/3.3.x/getting-started/sync-service.md)

* Best Practices
  <!-- -->
  * [API Version Control](https://docs.api7.ai/enterprise/3.3.x/best-practices/api-version-control.md)
