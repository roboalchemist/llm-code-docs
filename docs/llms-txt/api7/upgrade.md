# Source: https://docs.api7.ai/enterprise/upgrade-guides/upgrade.md

# Source: https://docs.api7.ai/enterprise/3.8.x/upgrade-guides/upgrade.md

# Source: https://docs.api7.ai/enterprise/3.7.x/upgrade-guides/upgrade.md

# Upgrade to API7 Enterprise 3.7.x

This guide walks you through the recommended process to upgrade from an older version to 3.7.x of API7 Enterprise. To minimize the risk of operation disruption, comprehensive preparation and impact assessment are crucial before initiating the upgrade. Please contact API7 with any inquiries or for upgrade guidance.

API7 Enterprise utilizes a structured versioning scheme that differentiates between major, minor, and patch releases. The latest version is generally recommended, as it incorporates fixes for known issues and minimizes risks. Alternatively, consider the latest Long-Term Support (LTS) version, currently 3.7.x.

note

The most suitable upgrade strategy depends heavily on factors such as deployment mode, custom plugins, specific plugin usage, technical capabilities, hardware capacity, SLAs, and more. Therefore, a thorough discussion with API7 is essential before proceeding with any upgrade.

## Overview[â](#overview "Direct link to Overview")

Upgrading API7 Enterprise involves three phases: preparation, testing and validation, and production deployment.

* During the preparation phase, carefully examine the [release notes](https://docs.api7.ai/enterprise/release-notes.md) between your current version and 3.7.x. Assess any [breaking changes](https://docs.api7.ai/enterprise/3.7.x/upgrade-guides/breaking-changes.md) that may require data migration or transformation.
* During the testing and validation phase, set up a test environment and deploy 3.7.x. Assess the applicability of new features and evaluate the new features. Record and verify the fixes of known issues.
* During production deployment, consider utilizing a rolling or canary upgrade strategy, and also prepare an emergency rollback plan to mitigate potential risks.

## Preparation[â](#preparation "Direct link to Preparation")

### Upgrade from 3.6.X[â](#upgrade-from-36x "Direct link to Upgrade from 3.6.X")

No breaking changes require preparation.

### Upgrade from 3.5.X[â](#upgrade-from-35x "Direct link to Upgrade from 3.5.X")

* Existing service runtime configurations within service templates will be automatically removed during upgrade.

  <!-- -->

  * Your published service configurations will remain unchanged.
  * Furthermore, the publishing process is simplified and streamlined, with no service runtime configurations allowed during the process. Follow the renewed guide to [publish service](https://docs.api7.ai/enterprise/3.7.x/getting-started/publish-service.md) after upgrade.

### Upgrade from 3.4.X[â](#upgrade-from-34x "Direct link to Upgrade from 3.4.X")

* Existing service runtime configurations within service templates will be automatically removed during upgrade.

  <!-- -->

  * Your published service configurations will remain unchanged.
  * Furthermore, the publishing process is simplified and streamlined, with no service runtime configurations allowed during the process. Follow the renewed guide to [publish service](https://docs.api7.ai/enterprise/3.7.x/getting-started/publish-service.md) after upgrade.

* The previous **Canary Rule** functionality is no longer supported.

  <!-- -->

  * Complete any ongoing canary process using the old **Canary Rule** functionality. Use the [Traffic Split](https://docs.api7.ai/hub/traffic-split.md) plugin instead after the upgrade.
  * Delete the existing [Traffic Split](https://docs.api7.ai/hub/traffic-split.md) plugin on the service or routes before upgrading. Reconfigure the plugin after the upgrade.

### Upgrade from 3.3.X[â](#upgrade-from-33x "Direct link to Upgrade from 3.3.X")

* Existing service runtime configurations within service templates will be automatically removed during upgrade.

  <!-- -->

  * Your published service configurations will remain unchanged.
  * Furthermore, the publishing process is simplified and streamlined, with no service runtime configurations allowed during the process. Follow the renewed guide to [publish service](https://docs.api7.ai/enterprise/3.7.x/getting-started/publish-service.md) after upgrade.

* The previous **Canary Rule** functionality is no longer supported.

  <!-- -->

  * Complete any ongoing canary process using the old **Canary Rule** functionality. Use the [Traffic Split](https://docs.api7.ai/hub/traffic-split.md) plugin instead after the upgrade.
  * Delete the [Traffic Split](https://docs.api7.ai/hub/traffic-split.md) plugin before upgrading. Reconfigure the plugin after the upgrade.

## Testing and Validation[â](#testing-and-validation "Direct link to Testing and Validation")

* Deploy 3.7.x in the test environment following the [Getting Started Guide](https://docs.api7.ai/enterprise/3.7.x/getting-started/install-api7-ee.md), and evaluate the new features. Refer to the [Release Notes](https://docs.api7.ai/enterprise/release-notes.md) for the feature lists.
* Perform a dry run in advance to avoid any unexpected situations.
* If you have custom plugins, review the code against release notes and test the custom plugin using the new version in the test environment.

## Production Deployment[â](#production-deployment "Direct link to Production Deployment")

The upgrade process is expected to take 80+ minutes. To facilitate effective upgrades, API7 Enterprise's [architecture](https://docs.api7.ai/enterprise/3.7.x/introduction/architecture.md) separates control plane nodes from data plane nodes (gateway instances). Consequently, the recommended upgrade process involves different strategies for control plane and data plane nodes.

**Aligning control plane and data plane nodes to the same version is strongly recommended for maximum security.** In specific scenarios or during temporary upgrade staging, checking the version and compatibility of data plane nodes is also recommended.

The separation of control and data planes facilitates API request handling by data plane nodes during control plane upgrades, achieving zero business downtime.

### Upgrade Control Plane[â](#upgrade-control-plane "Direct link to Upgrade Control Plane")

warning

A key prerequisite for upgrading is to update the control plane nodes before the data plane nodes. The control plane upgrade process is designed to avoid business downtime; however, all configuration changes are restricted during this period, including those made via the Dashboard, ADC, Admin APIs, Ingress Controller, or direct database operations.

1. Backup database(10 minutes). You can follow your own backup procedures to back up the database and generate the corresponding files or use the following process:

```
# Backup the entire database (custom format)
pg_dump -h <host> -U <username> -d <dbname> -F c -b -v -f /path/to/backup.dump

# Backup as an SQL file (output as SQL file)
pg_dump -h <host> -U <username> -d <dbname> -F p -f /path/to/backup.sql

# Correspondingly, if you encounter issues and need to restore previously backed-up data
pg_restore -h <host> -U <username> -d <new_dbname> -v /path/to/backup.dump

psql -h <host> -U <username> -d <new_dbname> -f /path/to/backup.sql
```

2. Backup configuration files, especially you have changed the default settings. (5 minutes)

```
* api7-ee/dp_manager_conf/conf.yaml
* api7-ee/dashboard_conf/conf.yaml
* api7-ee/gateway_conf/config.yaml
```

3. Upgrade control plane nodes to 3.7.x (20 minutes)

* Deploy new dashboard, DP-Manager, and related pods.
* Verify successful upgrade of the new control plane nodes.
* Perform rolling updates of existing pods.

Update the image name in the helm chart [values file](https://github.com/api7/api7-helm-chart/blob/main/charts/api7/values.yaml#L5-L13):

values.yaml

```
dashboard:
  image:
    repository: api7/api7-ee-3-integrated
    pullPolicy: Always
    # Overrides the image tag whose default is the chart appVersion.
    tag: "v3.7.3"
```

Run the helm command to update the release:

```
helm upgrade api7ee3 api7/api7ee3
```

### Upgrade Data Plane[â](#upgrade-data-plane "Direct link to Upgrade Data Plane")

note

A few error logs may be generated by data plane nodes during the upgrade process. This is expected behavior and can be safely ignored.

1. Upgrade data plane nodes to version 3.7.x (30 minutes for one gateway group)

* Deploy new gateway pods.
* Verify successful upgrade of the new data plane nodes.
* Perform rolling updates of the existing pods.
* If you have multiple Gateway groups, repeat the above steps for each Gateway group.

2. Conduct acceptance testing to ensure the upgrade is problem-free (20 minutes).

Update the image name in the helm chart [values.yaml](https://github.com/api7/api7-helm-chart/blob/main/charts/gateway/values.yaml#L99-L106):

values.yaml

```
  image:
    repository: api7/api7-ee-3-gateway
    pullPolicy: Always
    tag: 3.7.3
```

Based on the installation command generated previously in the dashboard, execute the helm command to update. Simply modify the image tag. For example:

```
helm upgrade --install -n api7 --create-namespace api7-ee-3-gateway api7/gateway \
  --set "etcd.auth.tls.enabled=true" \
  --set "etcd.auth.tls.existingSecret=api7-ee-3-gateway-tls" \
  --set "etcd.auth.tls.certFilename=tls.crt" \
  --set "etcd.auth.tls.certKeyFilename=tls.key" \
  --set "etcd.auth.tls.sni=api7ee3-dp-manager" \
  --set "etcd.auth.tls.verify=true" \
  --set "gateway.tls.existingCASecret=api7-ee-3-gateway-tls" \
  --set "gateway.tls.certCAFilename=ca.crt" \
  --set "apisix.extraEnvVars[0].name=API7_GATEWAY_GROUP_SHORT_ID" \
  --set "apisix.extraEnvVars[0].value=default" \
  --set "etcd.host[0]=https://192.168.10.101:7943" \
  --set "apisix.replicaCount=1" \
  --set "apisix.image.repository=api7/api7-ee-3-gateway" \
  --set "apisix.image.tag=3.7."
```

### Rollback Plan[â](#rollback-plan "Direct link to Rollback Plan")

1. The rolling upgrade strategy facilitates rapid rollback to the previous version in the event of verification failures or other problems.
2. Data restoration from the database backup and subsequent redeployment is a viable recovery option.

## Additional Resources[â](#additional-resources "Direct link to Additional Resources")

* Introduction
  <!-- -->
  * [API7 Enterprise Architecture](https://docs.api7.ai/enterprise/3.7.x/introduction/architecture.md)
* Upgrade Guides
  <!-- -->
  * [Breaking Changes](https://docs.api7.ai/enterprise/3.7.x/best-practices/api-version-control.md)
