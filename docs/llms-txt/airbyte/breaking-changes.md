# Source: https://docs.airbyte.com/release_notes/breaking-changes.md

# Breaking change list

Copy Page

CoreStandardPlusProEnterprise FlexSelf-Managed Enterprise[ Compare](https://airbyte.com/product/features)

Occasionally, new versions of Airbyte introduce breaking changes. This page inventories breaking changes between versions and any necessary steps to mitigate the change.

When you upgrade your Self-Managed instance of Airbyte to a version with a breaking change, you may need to take mitigating action. If you are upgrading multiple versions at once, complete the mitigaton steps for the versions you are skipping as well.

## Core[​](#core "Direct link to Core")

### 1.8.x to 2.0.x[​](#18x-to-20x "Direct link to 1.8.x to 2.0.x")

* If you deploy with abctl, version 2.0 requires abctl version 0.30.2 or later. [Upgrade to version 0.30.2 or later](/platform/operator-guides/upgrading-airbyte.md#upgrade-abctl) before deploying Airbyte version 2.0.

### 1.7.x to 1.8.x[​](#17x-to-18x "Direct link to 1.7.x to 1.8.x")

* Airbyte no longer publishes a `webapp` image and it's no longer independently deployable. To mitigate this, complete 1.7 ingress update.

### 1.6.x to 1.7.x[​](#16x-to-17x "Direct link to 1.6.x to 1.7.x")

* Airbyte began removing the `webapp` service and moving its functions to `server`. To mitigate this, [update your ingress](/platform/deploying-airbyte/integrations/ingress-1-7.md)

## Self-Managed Enterprise[​](#self-managed-enterprise "Direct link to Self-Managed Enterprise")

### 1.7.x to 1.8.x[​](#17x-to-18x-1 "Direct link to 1.7.x to 1.8.x")

* Airbyte no longer publishes a `webapp` image and it's no longer independently deployable. To mitigate this, complete 1.7 ingress update.

### 1.6.x to 1.7.x[​](#16x-to-17x-1 "Direct link to 1.6.x to 1.7.x")

* Airbyte began removing the `webapp` service and moving its functions to `server`. To mitigate this, [update your ingress](/platform/deploying-airbyte/integrations/ingress-1-7.md).

### 1.5.x to 1.6.x[​](#15x-to-16x "Direct link to 1.5.x to 1.6.x")

* Service accounts require a new permission. [Update your service account](/platform/enterprise-setup/upgrade-service-account.md)
