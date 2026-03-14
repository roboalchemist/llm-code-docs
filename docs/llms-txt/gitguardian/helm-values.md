# Source: https://docs.gitguardian.com/self-hosting/management/infrastructure-management/helm-values.md

# Helm Chart Values Changelog

> Index of Helm chart values references for all GitGuardian self-hosted versions.

# Helm Chart Values Changelog

Track changes in GitGuardian's Helm chart values across releases.

**Latest Version**: [2026.2.0](./helm-values/2026.2.0)

**Resources**: [Helm installation guide](../../installation/installation-existing-cluster-helm) | [Upgrade procedures](./upgrade-helm)

## 2026.2.0 vs 2026.1.0

**New:**
- Added `hookMethod` parameter to handle `helm` and `argocd` hooks annotations.
- Added `replicated.replicaCount` coming with Replicated SDK HA feature.
- Added `replicated.highAvailability.podAntiAffinityPreset` coming with Replicated SDK HA feature.
- Added `replicated.highAvailability.podDisruptionBudget.enabled` coming with Replicated SDK HA feature.
- Added `replicated.highAvailability.podDisruptionBudget.minAvailable` coming with Replicated SDK HA feature.
- Introduced new `celeryWorkers.check-runs` worker type dedicated to Check Run tasks (default: 0 replicas).

**Updated:**
- Updated `loki.loki.compactor.retention_delete_delay` from `168h` to `2h` to better reflect Loki configuration.
- Added `sources_default`, `incidents_default` and `individual_validity_check` to `celeryWorkers.worker.queues`.
- Added `individual_validity_check` to `celeryWorkers.worker.autoscaling.metrics`.
- Added `code_fixing` to `celeryWorkers.scanners.queues`.
- Added `hmsl`, `sources_long` and `incidents_long` to `celeryWorkers.long.queues`.

## 2026.1.0 (Required) vs 2025.12.0

**New:**
- Added `webappDefaults` and `celeryWorkerDefaults` sections to centralize common configuration (e.g., `nodeSelector`, `tolerations`, `priorityClassName`). Individual webapp/worker configurations are still fully supported and take priority over defaults - you can override any default value by specifying it directly under `webapps.[name]` or `celeryWorkers.[name]`, even if not explicitly listed in the values reference.
- Added new Celery queues: `core_default` and `core_long`.

**Removed:**
- Removed `apacheTika.javaOpts` parameter.

## 2025.12.0 vs 2025.11.0

**New:**
- Added `extra_hostnames` parameter to allow additional hostnames on Nginx proxy.
- Added `network.ipFamily` parameter to select IP class (IPv4/IPv6) for `Service` resources. [Learn more](./ipv6-networking).
- Introduced new worker type `business-contribution` under `celeryWorkers` key value.
- Added new global `podDisruptionBudget.enabled` parameter to deploy PDB globally.
- Introduced section `inAppAnalytics` parameter to configure the In App Analytics feature (in beta).
- Added new `podDisruptionBudget` parameter to control PDB globally.

**Updated:**
- Tagged `experimental.ingressRoutes` explicitly as deprecated feature.

## 2025.11.0 vs 2025.10.0

**New:**
- Added default `RuntimeDefault` value to MinIO pod security `loki-minio.containerSecurityContext.seccompProfile.type`.
- Introduced `update_sources_state` and `nhi_ingestion` parameters to `celeryWorkers.long.autoscaling.metrics`.
- Added `replicatedRbac` section to control replicated RBAC.

**Updated:**
- replicated-sdk now inherits from `global.imagePullSecrets`, removing the need to use `replicated.imagePullSecrets` if secret is defined globally.
- Default `logCollector.supportBundle.since` changed from `6h` to `12h`.
- Changed `celeryWorkers.long.queues` value to add `update_sources_state` and `nhi_ingestion`.

**Removed:**

- Deleted `replicatedSdk` key as it is enabled by default now.

## 2025.10.0 (Required) vs 2025.9.0

**Updated:**

- Containers are now using readOnlyRootFilesystem by default (`containerSecurityContext`).
- Updated `loki-minio.image.repository` from `gitguardian/wolfi/minio-bitnami` to `gitguardian/wolfi/minio`.
- Updated `loki-minio.image.tag` from `0.20250723` to `0.20250907`.
- The parameter `loki-minio.image.pullPolicy` has been renamed to `loki-minio.image.imagePullPolicy`.
- Added `automatic_severities` to `celeryWorkers.long.queues` to allow long-running tasks to complete gracefully before the 24-hour timeout.
- Added `NO_PROXY` to `replicated.extraEnv` default to fix license verification when using a proxy.

**Removed:**

- `loki-minio.podSecurityContext.enabled` boolean has been removed. To disable `podSecurityContext` you now need to use empty object such as `podSecurityContext: {}`.
- `loki-minio.containerSecurityContext.enabled` boolean has been removed. To disable `containerSecurityContext` you now need to use empty object such as `containerSecurityContext: {}`.
- `loki-minio.networkPolicy` section has been removed since it is not supported anymore.
- `loki-minio.console` section has been removed since it is not relevant anymore.
- `loki-minio.ServiceAccount` section has been removed since it is now enabled by default.

## 2025.9.0 vs 2025.8.0

**New:**

- Introduced `apacheTika` parameter to configure the new file scanner service for Non-VCS sources (disabled by default).
- Introduced `celeryWorkers.scanners-ods-highdisk` parameter to configure workers dedicated to high storage tasks like Microsoft OneDrive and SharePoint scanning (default: 0).

[Learn more about Non-VCS Sources](../application-management/non-vcs-sources.md).

**Updated:**

- Updated `logCollector.supportBundle.since` default value from `3d` to `6h` to make support bundle lighter.

**Removed:**

- `postgresql.plugins.pgvector.enabled` has been removed since it is now enabled by default, pgvector is now required. [Learn more about PostgreSQL requirements](../../system-requirements.md#postgresql).

## 2025.8.0 vs 2025.7.0

:::caution Upgrading to 2025.8
**Air gap deployment?** This release introduces a new `image.registry` parameter in Helm values to support the Log Collector system. This parameter specifies the location of the GitGuardian images for the [Log Collector](../../troubleshoot/logs#log-collector) components (Loki, MinIO, Fluent Bit) and is separate from the main `imageRegistry` parameter. Follow the [upgrade instructions](../infrastructure-management/upgrade-helm#upgrading-to-20258) to update your helm values file.
:::

**New:**

- Introduced a new `image.registry` parameter in Helm values to support the Log Collector system. This parameter specifies the location of the GitGuardian images for the [Log Collector](/self-hosting/troubleshoot/logs#log-collector) components (Loki, MinIO, Fluent Bit) and is separate from the main `imageRegistry` parameter. Follow the [upgrade instructions](/self-hosting/management/infrastructure-management/upgrade-helm#upgrading-to-20258) to update your helm values file.
- Introduced `celeryWorkers.scanners-slack` parameter to configure workers dedicated to Slack scanning (default: 0). [Learn more about Slack Scanning considerations](./scaling.md#slack-scanning-considerations).
- Added `commonTolerations` parameter that allows you to apply consistent tolerations across all workloads in the GitGuardian deployment.

**Removed:**

- `beat.replicas` has been removed and is now hardcoded in the chart to 1.

## 2025.7.0 (Required) vs 2025.6.0

**New:**

- Added `priorityClassName` parameter for ML Secret Engine and several priority class configuration. [Learn more](../application-management/machine-learning#lower-the-priority-of-ml). This is also available for other pods and as a global parameter (`global.priorityClassName`).

**Updated:**

- Changed the default value of `celeryWorkers.ml-api-priority.replicas` from `0` to `1`. [Learn more](../application-management/machine-learning#helm-based-installation).

## 2025.6.0 vs 2025.5.0

**New:**

- Added `global.fipsEnabled` parameter to enable FIPS compliant images. [Learn more about FIPS compliance](../../security/recommendations).
- Added pod anti-affinity configuration (`podAntiAffinityPreset`) and `nodeSelector` and `tolerations` parameters across all components for improved workload placement control and high availability. [Learn more about scaling](./scaling#node-affinity-scheduling).
- Enhanced logCollector with additional configuration options (`logCollector.env`, `logCollector.envFrom`, `logCollector.pipelines`). [Learn more about additional pipelines](../../troubleshoot/logs#additional-pipelines).
- Enhanced migration job resource configuration with separate specifications for pre-deploy, post-deploy, and upgrade path check jobs.

**Removed:**

- `migration.resources` has been replaced with job-specific resource configurations for better resource management.

## 2025.5.0 vs 2025.4.0

:::caution Upgrading to 2025.5
**Air gap deployment?** We've renamed images in this release. See below changes and find all image and tag names on the **[Air Gap Install page](../../installation/airgap-installation-existing-cluster-helm#download-gitguardian-images)**.
:::

**New:**

- Added support for configuring the proxy via an existing Kubernetes secret using `proxy.existingSecret` and `proxy.existingSecretKeys.*`.

**Updated:**

- **FIPS:** This release uses Chainguard images without FIPS-approved cryptographic modules. If you would like to use Chainguard images with FIPS, please contact our [support team](mailto:support@gitguardian.com). This change involves renaming the following images:
  - `gitguardian/prm-static-chainguard-fips` to `gitguardian/prm-static-chainguard`
  - `gitguardian/prm-app-fips` to `gitguardian/prm-app-chainguard`
- Use `proxy.replicated.com/proxy/gitguardian/ghcr.io/gitguardian/wolfi/bash:latest` image instead of `proxy.replicated.com/proxy/gitguardian/docker.io/nginxinc/nginx-unprivileged:stable` for Custom CA injection (See `tls.customCa.image.*`).
- The `securityContext.enabled` (bool) parameter has been replaced by a new `securityContext` (object) parameter, which now allows specifying the full Pod Security Context.

**Removed:**

- `experimental.chainguard` has been deprecated as GitGuardian images are now using Chainguard by default. [Lean more about Chainguard](../../security/recommendations).

## 2025.4.0 (Required) vs 2025.3.0

:::caution Upgrading to 2025.4
**Air gap deployment?** We've added new images in this release. Find all image and tag names on the **[Air Gap Install page](../../installation/airgap-installation-existing-cluster-helm#download-gitguardian-images)**.
:::

**New:**

- Our self-hosted deployments now include a log collection system, leveraging Loki, MinIO, and Fluent Bit under the hood. This log collection system is now enabled by default for all installation types (Helm or KOTS). [Learn more about the log collector](../../troubleshoot/logs#log-collector).
- The PostgreSQL `pgvector` extension is now required by default (`postgresql.plugins.pgvector.enabled`). Please follow the [installation instructions](../../system-requirements#postgresql) to enable vector similarity search capabilities for upcoming machine learning features.

**Updated:**

- Added default `support-bundle` Role and optional ClusterRole creation (configurable via `replicated.supportBundle.rbac.clusterRole.create`).
- Added `global.compatibility.openshift.adaptSecurityContext` configuration to support OpenShift's restricted-v2 Security Context Constraints (SCC). Values include `auto` (default), `force`, and `disabled` for flexible security context adaptation.

## 2025.3.0 vs 2025.2.0

:::caution Upgrading to 2025.3
We've updated the path and names of our images in this release. Follow the [upgrade instructions](./upgrade-helm#upgrading-to-20253) to update your tooling for downloading and uploading GitGuardian images to your private registry. Find all image and tag names on the **[Air Gap Install page](../../installation/airgap-installation-existing-cluster-helm#download-gitguardian-images)**.
:::

**Updated:**

- Change registry URL from `proxy.replicated.com/proxy/gitguardian/513715405986.dkr.ecr.us-west-2.amazonaws.com` to `proxy.replicated.com/proxy/gitguardian/docker.io` and rename paths and images name from:
  - `/prm/static-chainguard` to `/gitguardian/prm-static-chainguard-fips`
  - `/prm/app-chainguard` to `/gitguardian/prm-app-chainguard-fips`
  - `/prm/helm-tooling` to `/gitguardian/prm-helm-tooling`
  - `/services/nginx-unprivileged` to `/nginxinc/nginx-unprivileged`
  - `/ml-detector/ml-secret-engine/app-chainguard` to `/gitguardian/ml-secret-engine-app-chainguard-fips`
- Change registry URL from `registry.replicated.com` to `proxy.replicated.com/proxy/gitguardian/docker.io` and rename paths and images name from `/gitguardian/replicated-sdk` to `/replicated/replicated-sdk`.
- The `nhi-scout` parameter has been renamed to `ggscout`.
- Added `celeryWorkers.*.autoscaling.keda.idleReplicaCount` parameter to allow specifying the number of replicas when there is no activity on the Celery Worker (default: `0`).

## 2025.2.0 vs 2025.1.0

**New:**

- Enhanced the `webapps.<all>.autoscaling` settings to support both Horizontal Pod Autoscaler (HPA) and KEDA autoscaling options, including enabling/disabling and setting triggers. [Learn more](./autoscaling).
- Added `migration.podAnnotations` parameter for GitGuardian migration pods.

**Updated:**

- `nhiScout.enabled` parameter has been moved to `nhi-scout.enabled`. [Learn more](../../../ggscout-docs/self-hosted-configuration).

## 2025.1.0 (Required) vs 2024.12.0

:::caution Upgrading to 2024.12
The ReplicatedSDK image is now pulled from the Replicated registry instead of Docker Hub. For airgap installations, ensure you update your automation processes for pulling and pushing images to your private registry. For more information, refer to the [Airgap Installation page](../../installation/airgap-installation-existing-cluster-helm).
:::

**New:**

- Introduced `secretEngine` parameter to configure the new ML Secret Engine service. (Disabled by default). [Learn more](../application-management/machine-learning#helm-based-installation).
- Introduced `celeryWorkers.ml-api-priority` parameter to configure ML Secret Engine dedicated worker (Disabled by default).
- Introduced `nhiScout.enabled` parameter to enable NHI Scout deployment (Disabled by default). [Learn more](../../../ggscout-docs/self-hosted-configuration)
- Introduced `nhi-scout` parameter to configure NHI Scout.
- Added `replicated.image.registry` parameter to use the Replicated registry (`registry.replicated.com`) instead of Docker Hub by default.

**Updated:**

- Changed the default value of `replicated.image.repository` from `replicated/replicated-sdk` to `gitguardian/replicated-sdk`.

## 2024.12.0 vs 2024.11.0

:::caution Upgrading to 2024.12
This release includes breaking changes. Upgrade to **2024.12.0** using the **[upgrade notes](./upgrade-helm)**.
:::

**New:**

- Ability to deploy `Ingress` objects with the support of several Ingress controllers. For details, see the [Ingress documentation](./ingress).

**Updated:**

- `front.ingress` has been renamed to `ingress` for improved consistency and standardization across the Helm chart.
- `istio` have been moved under the `ingress`.
- The default memory value for `migration.resources` has been increased from `100Mi` to `200Mi`.

## 2024.11.0 vs 2024.10.0

:::caution Upgrading to 2024.11
This release includes breaking changes.
:::

**New:**

- Removed `settings.healthCheck.periodicInterval` parameter since health checks are now distributed over time rather than executing them simultaneously. This parameter is replaced by `spread_periodic_range_minutes` in the [admin area](../application-management/preferences#health-checks).
- Added `replicated.privateCASecret` parameter to specify a custom CA when using a proxy. [Learn more](./proxy-server#helm-based-installation).
- Replace the legacy parameter `replicated.images.replicated-sdk` with the new parameters `replicated.image.repository` and `replicated.image.tag`

## 2024.10.0 (Required) vs 2024.9.0

**New:**

- Added two new worker types `long-ods` (non-VCS sources such as Slack, Jira Cloud, Confluence, ...) and `long-ods-io` (long tasks specialized in Input/Output).
- Added the support of CRL (instead of default OCSP) for certificate-based authentication.

**Updated:**

- Decreased the default value of `celeryWorkers.realtime-ods.replicas` from `2` to `0`.

## 2024.9.0 vs 2024.8.0

**New:**

- Added a new `autoscaling` object to configure autoscaling settings.
- Enhanced the `celeryWorkers.<all>.autoscaling` settings to support both Horizontal Pod Autoscaler (HPA) and KEDA autoscaling options, including enabling/disabling and setting triggers. [Learn more](./autoscaling).
- Introduced a new setting `replicated.supportBundle.logs.maxLines` to specify the maximum number of lines included in support bundle logs.
- Added `experimental.tini`, a new option to enable `tini` for terminating zombie processes on workers.

## 2024.8.0 vs 2024.7.0

**New:**

- Introduced `tls.clientAuth` to support authentication using Common Access Card (CAC) or Personal Identity Verification (PIV). For detailed information, refer to the documentation [here](./cert-based-auth).

## 2024.7.0 (Required) vs 2024.6.0

:::caution Upgrading to 2024.7
This release includes breaking changes.
:::

**New:**

- Added `settings.healthCheck.periodicInterval` allowing you to change the frequency of [health checks](../../troubleshoot/health-check#integration-connectivity).

**Updated:**

- Renamed `front.ingress.tls.secretName` to `front.ingress.tls.existingSecret`.
- Renamed `tls.customCa.caCert` to `tls.customCa.caCrt`.
- Renamed `tls.customCa.existingSecretCaCertKey` to `tls.customCa.existingSecretKeys.caCrt` and set the Default to `""`.
- Renamed `redis.main.existingSecretKeys.sentinel.password` to `redis.main.existingSecretKeys.sentinelPassword`.
- Renamed `redis.main.existingSecretKeys.sentinel.url` to `redis.main.existingSecretKeys.sentinelUrl`.
- Updated default value `front.nginx.resources` from `{"requests":{"cpu":"200m","memory":"500Mi"}}` to `{"requests":{"cpu":"100m","memory":"200Mi"}}`

## 2024.6.0 vs 2024.5.0

**Updated:**

- Added new task `background_validity_check` to `celeryWorkers.long.queues`.

## 2024.5.0 vs 2024.4.0

:::caution Upgrading to 2024.5
This release includes breaking changes.
:::

**New:**

- Introduce `externalSecrets.refreshInterval`option to give the ability to customize the refresh interval for external secrets.
- Added `istio.gateway.enabled` parameter to be able to disable Istio Gateway handling when Istio is enabled.
- Added `redis.main.existingSecretKeys.url` and `redis.main.existingSecretKeys.password`.
- Added `redis.commitCache.existingSecretKeys.url` and `redis.commitCache.existingSecretKeys.password`.
- Added `migration.labels` and `migration.podLabels` for migrations resources.

**Updated:**

- Replaced `postgresql.existingSecretKeys.tls` with `postgresql.tls.existingSecretKeys` and set the Default to `""` for
  - `password` instead of `POSTGRES_PASSWORD`.
  - `crt` instead of ``"pg_client.crt"`.
  - `key` instead of `"pg_client.key"`.
  - `caCrt` instead of `"pg_server.ca_crt"`.
- Replaced `redis.main.existingSecretKeys.tls` with `redis.main.tls.existingSecretKeys` and set the Default values to `""` for
  - `crt` instead of ``"redis_client.crt"`.
  - `key` instead of `"redis_client.key"`.
  - `caCrt` instead of `"redis_server.ca_crt"`.
- Replaced `redis.commitCache.existingSecretKeys.tls` with `redis.commitCache.tls.existingSecretKeys` and set the Default values to `""` for
  - `crt` instead of ``"redis_client.crt"`.
  - `key` instead of `"redis_client.key"`.
  - `caCrt` instead of `"redis_server.ca_crt"`.
- Rename `celeryWorkers.realtime_ods` to `celeryWorkers.realtime-ods`.
- Set the Default for `miscEncryption.existingSecretKeys` attributes to `""` for
  - `djangoSecretKey` instead of `"DJANGO_SECRET_KEY"`.
  - `dbEncryptionKeys` instead of `"ENCRYPTION_KEYS"`.
  - `x509Cert` instead of `"SP_X509_CERT"`.
  - `x509PrivateKey` instead of `"SP_PRIVATE_KEY"`.
- Added `"existingSecret":"","existingSecretKeys":{"password":""}` in `onPrem.adminUser` offering the option to specify the admin password in a secret.
- Rename Default value for `tls.customCa.existingSecretCaCertKey ` to `"ca.crt"` instead of `"custom-ca.pem"`.
- Added `report` to `celeryWorkers.worker.queues`.

**Removed:**

- Removed `argoCd.enabled` originally used to inject Argo CD phase annotations in Kubernetes resources but, since Argo CD supports Helm hooks annotations by mapping them onto its own hook annotations, it is not used anymore in 2024.5.0.

## 2024.4.0 (Required) vs 2024.3.0

**New:**

- Added `commonLabels` to add custom labels to differentiate multiple GitGuardian deployments within the same Kubernetes cluster.
- Introduce `ephemeralStorage` option for all `celeryWorkers` to support [Generic Ephemeral Inline Volumes](./scaling#generic-ephemeral-inline-volumes).
- Introduced new `celeryWorkers.realtime-ods` worker for Other Data Sources (ODS) real time scanning.

**Updated:**

- Modified `celeryWorkers.worker.queues` and moved `realtime_ods,realtime_retry_ods` tasks into new `celeryWorkers.realtime-ods.queue`.

## 2024.3.0 vs 2024.2.0

**Updated:**

- Decreased the default value of `celeryWorkers.scanners_ods.replicas` from `2` to `0`.

## 2024.2.0 vs 2024.1.0

**New:**

- Added `redis.main.sentinel` configuration options for managing Redis Sentinel settings.
- Introduced new settings for `redis.main.existingSecretKeys.sentinel.url` and `redis.main.existingSecretKeys.sentinel.password`.
- Added `miscEncryption.dbEncryptionKeys` and `miscEncryption.existingSecretKeys.dbEncryptionKeys` for database encryption key management.
- Introduced new `celeryWorkers.scanners_ods` worker for Other Data Sources (ODS) scanning.

**Removed:**

- Removed `observability.exporters.celeryExporter`.

## 2024.1.0 (Required) vs 2023.12.0

**New:**

- Expanded `nodeSelector` and `tolerations` settings across multiple services: `front.nginx`, `webapps.internal_api`, `webapps.internal_api_long`, `webapps.public_api`, `webapps.hook`, `webapps.app_exporter`, `celeryWorkers.worker`, `celeryWorkers.email`, `celeryWorkers.scanners`, and `celeryWorkers.long`.
- New `replicated.isAirgap` setting to manage air-gapped environments.
- Introduced `tls.customCa.image` configuration for custom CA management.
- Added new settings related to Kubernetes Roles and RoleBindings: `rbac.enabled`, `serviceAccount.create`, `serviceAccount.name`, `migration.serviceAccount.create`, and `migration.serviceAccount.name`.

**Updated:**

- Added new tasks `realtime_ods,realtime_retry_ods` to `celeryWorkers.worker.queues` to support additional task types.
- Enabled `experimental.chainguard` by default, changing from `false` to `true`, to utilize Chainguard images for backend and frontend services.
