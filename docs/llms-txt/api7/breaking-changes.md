# Source: https://docs.api7.ai/enterprise/upgrade-guides/breaking-changes.md

# Source: https://docs.api7.ai/enterprise/3.8.x/upgrade-guides/breaking-changes.md

# Source: https://docs.api7.ai/enterprise/3.7.x/upgrade-guides/breaking-changes.md

# Historic Breaking Changes

This document outlines the breaking changes introduced in API7 Enterprise across different versions. These changes may affect your existing configurations and workflows. Please review the changes for your target version before upgrading to ensure a smooth transition.

## 3.6.0[â](#360 "Direct link to 3.6.0")

**Release Date**: 2025-02-26

* Removed [service runtime configurations](https://docs.api7.ai/enterprise/3.7.x/key-concepts/services.md#service-runtime-configurations) in service templates, for better template reuse across gateway groups. **Existing service runtime configurations within service templates will be removed, but your published service configurations will remain unchanged.** Furthermore, the publishing process is simplified and streamlined, with no service runtime configurations allowed during the process. See the updated guide to [publish service](https://docs.api7.ai/enterprise/3.7.x/getting-started/publish-service.md).

warning

**ADC Version Compatibility**: Starting from this version, API7 Enterprise is no longer compatible with ADC versions before **0.18.0**. Please ensure you are using ADC **0.18.0** or higher to avoid compatibility issues.

## 3.5.0[â](#350 "Direct link to 3.5.0")

**Release Date**: 2025-01-27

* **Multiple Upstreams in a Service**: For advanced scenarios such as canary deployments, blue-green deployments, or managing multiple clusters, a service can now utilize multiple upstreams. In such cases, a default upstream serves as the primary target for most requests, while other upstreams can be used for specific purposes, such as routing traffic to a canary deployment or a secondary cluster. See the renewed [Configure Canary Traffic Shifting](https://docs.api7.ai/enterprise/3.7.x/getting-started/canary-upstream.md) for details.

info

The old **Canary Rule** function is no longer available.
