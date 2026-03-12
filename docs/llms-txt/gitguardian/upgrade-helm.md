# Source: https://docs.gitguardian.com/self-hosting/management/infrastructure-management/upgrade-helm.md

# Upgrade Helm

> Upgrade your GitGuardian self-hosted Helm installation, including version-specific migration instructions.

:::danger
Do not roll back or downgrade without consulting our **[support team](mailto:support@gitguardian.com)** first. Certain scenarios may necessitate restoring the database from a pre-upgrade backup due to the complexity of reversing some database migrations.
:::

:::caution
Prior to upgrading, ensure you back up your PostgreSQL database. For detailed instructions, refer to the **[Backup](./backup.md)** page.
:::

### Upgrading to 2025.10

**If you are using an air gap deployment:** This release now uses a **non-Bitnami** chart and Docker image for the MinIO subchart (which supports the [log collector feature](../../troubleshoot/logs#log-collector)). This change implies minor modifications to your `values.yaml` file:

Modify your Helm values file:

- Update `loki-minio.image.repository` from `gitguardian/wolfi/minio-bitnami` to `gitguardian/wolfi/minio`.
- Update `loki-minio.image.tag` from `0.20250723` to `0.20250907`.
- Rename parameter `loki-minio.image.pullPolicy` to `loki-minio.image.imagePullPolicy`.

### Upgrading to 2025.8

**If you are using an air gap deployment:** This release introduces a new `image.registry` parameter in Helm values to support the [Log Collector](../../troubleshoot/logs#log-collector) system. This parameter specifies the location of the GitGuardian images for the Log Collector components (Loki, MinIO, Fluent Bit) and is separate from the main `imageRegistry` parameter.

Add the `image.registry` to your Helm values file:

```yaml
global:
  imageRegistry: docker.internal/example/path # Location of the GitGuardian images
  image:
    registry:  docker.internal/example/path # Location of the GitGuardian images (same as imageRegistry)
```

Find all image and tag names on the **[Air Gap Install page](../../installation/airgap-installation-existing-cluster-helm#download-gitguardian-images)**.

### Upgrading to 2025.7

**[Machine Learning engine](../application-management/machine-learning) is now enabled by default.** Ensure your infrastructure meets the [ML requirements](../application-management/machine-learning#system-requirements).

### Upgrading to 2025.6

GitGuardian 2025.6 now requires Kubernetes 1.28 as the minimum supported version. However, **Kubernetes 1.28 is no longer receiving active or maintenance support** from the Kubernetes project (support ended in October 2024).

We strongly recommend upgrading to **Kubernetes 1.32** for optimal security and stability. Kubernetes 1.32 is actively supported until December 2025 and will receive maintenance support until February 2026.

For more information:
  - [Kubernetes end-of-life schedule](https://endoflife.date/kubernetes)
  - [GitGuardian system requirements](/self-hosting/system-requirements#kubernetes-for-existing-clusters)

### Upgrading to 2025.5

**Air gap deployment?** We've renamed images in this release. See below and find all image and tag names on the **[Air Gap Install page](../../installation/airgap-installation-existing-cluster-helm#download-gitguardian-images)**.

This change involves renaming the following images:
  - `gitguardian/prm-static-chainguard-fips` to `gitguardian/prm-static-chainguard`
  - `gitguardian/prm-app-fips` to `gitguardian/prm-app-chainguard`

### Upgrading to 2025.4

**Please install the PostgreSQL `pgvector` extension** to enable vector similarity search. This is essential for upcoming features leveraging our internal machine learning engine. Follow the [installation instructions](../../system-requirements#postgresql) to ensure compatibility.

**Air gap deployment?** We've added new images in this release. The new images are for the log collection system, which includes:
  - Fluent Bit (log collector)
  - Loki (log aggregation)
  - MinIO (object storage for logs)

Find all image and tag names on the **[Air Gap Install page](../../installation/airgap-installation-existing-cluster-helm#download-gitguardian-images)**.

### Upgrading to 2025.3

The 2025.3 release introduces a breaking change in the naming registry URL, including the path and image names. If you are downloading our images in a private registry (refer to our [air gap documentation](../../installation/airgap-installation-existing-cluster-helm)), make sure to update your tooling, as well as the image names and paths in your Helm values file.

Change registry URL
- **Old:** `proxy.replicated.com/proxy/gitguardian/513715405986.dkr.ecr.us-west-2.amazonaws.com`
- **New:** `proxy.replicated.com/proxy/gitguardian/docker.io`

Image path and name changes
- `/prm/static-chainguard` â `/gitguardian/prm-static-chainguard-fips`
- `/prm/app-chainguard` â `/gitguardian/prm-app-chainguard-fips`
- `/prm/helm-tooling` â `/gitguardian/prm-helm-tooling`
- `/services/nginx-unprivileged` â `/nginxinc/nginx-unprivileged`
- `/ml-detector/ml-secret-engine/app-chainguard` â `/gitguardian/ml-secret-engine-app-chainguard-fips`

Change registry URL
- **Old:** `registry.replicated.com`
- **New:** `proxy.replicated.com/proxy/gitguardian/docker.io`

Image path and name changes
- `/gitguardian/replicated-sdk` â `/replicated/replicated-sdk`

### Run preflight checks ð¦

:::caution Requirements
Preflight checks are critical for a successful installation. The following rules apply:

- :x: **Preflight Check Failures**: If preflight checks fail, the upgrade **must not continue** until the targeted environment meets all requirements. Please reach out to our **[support team](mailto:support@gitguardian.com)** if needed.
- :warning: **Preflight Check Warnings**: If preflight checks return warnings, the installation can proceed, but it is recommended that you address these warnings to comply with our **[recommendations](../../system-requirements)**.

:::

We strongly advise you to run our preflight script to ensure your existing cluster meets GitGuardian's requirements.

Retrieve the script from our public repository [here](https://github.com/GitGuardian/ggtools/tree/main/helm-preflights)

Specify an existing Kubernetes namespace using the `-n` option. If not specified, the script will run in your default namespace.
Replace `<release-name>` with your existing [helm release name](https://helm.sh/docs/intro/using_helm/#helm-install-installing-a-package).

```bash
./preflights.sh -r <release-name> -n <namespace> oci://registry.replicated.com/gitguardian/gitguardian -f local-values.yaml
```

### Upgrading the GitGuardian application

Log in to the registry with the following command:

```bash
helm registry login registry.replicated.com --username your.name@yourcompany.com
```

Upgrade the GitGuardian application to the latest version in the Kubernetes cluster and namespace where it's installed:

```bash
helm upgrade <release-name> -n <namespace> oci://registry.replicated.com/gitguardian/gitguardian -f local-values.yaml
```

Replace `<release-name>` with the name used during the initial installation (use `helm ls` to find it).
If needed, specify the namespace with `-n` (default namespace is used if not specified).

This will upgrade your application to the latest version. To upgrade to a specific version, use the `--version` flag:

```bash
helm upgrade <release-name> -n <namespace> oci://registry.replicated.com/gitguardian/gitguardian --version 2024.x.y -f local-values.yaml
```

### Upgrading the GitGuardian application in Airgap

Follow these steps to upgrade a Helm-based installation in an air-gapped environment:

1. Log in to the Helm registry:

   ```bash
   helm registry login registry.replicated.com --username your.name@yourcompany.com
   ```

2. Download the Helm chart locally (replace with the desired version as needed):

   ```bash
   helm fetch oci://registry.replicated.com/gitguardian/gitguardian
   # this will download a file like gitguardian-<version>.tgz
   ```

3. Authenticate Docker to the Replicated proxy to pull images (replace `<your_licenseID>`):

   ```bash
   LICENSE_ID="<your_licenseID>"; \
   echo "{\"auths\": {\"proxy.replicated.com\": {\"auth\": \"$(echo -n \"${LICENSE_ID}:${LICENSE_ID}\" | base64)\"}, \"registry.replicated.com\": {\"auth\": \"$(echo -n \"${LICENSE_ID}:${LICENSE_ID}\" | base64)\"}}}" > ~/.docker/config.json
   ```

4. Pull the required images for the target release, then upload them to your private registry. Refer to the image list on the **[Airgap Install page](../../installation/airgap-installation-existing-cluster-helm#download-gitguardian-images)**. You can use `docker` or `skopeo` to transfer images.

   :::::info Image architecture
   All GitGuardian images are multi-architecture. You do not need to pass `--platform` when pulling them; the correct variant is selected automatically based on the host architecture.
   :::::

5. Run preflight checks against the local chart archive:

   ```bash
   ./preflights.sh -r <release-name> -n <namespace> gitguardian-<version>.tgz -f local-values.yaml
   ```

6. Upgrade using the local chart archive:

   ```bash
   helm upgrade <release-name> --timeout 30m -n <namespace> gitguardian-<version>.tgz -f local-values.yaml
   ```

Replace `<release-name>`, `<namespace>`, and `<version>` accordingly. Ensure your `local-values.yaml` points to your private image registry as described in the **[Airgap Install page](../../installation/airgap-installation-existing-cluster-helm#upload-gitguardian-images)**.

### Updating application configuration

Modify the application configuration with an updated values file using the `helm upgrade` command.
Stick to the same version using the `--version` flag:

```bash
helm upgrade <release-name> -n <namespace> oci://registry.replicated.com/gitguardian/gitguardian --version 2024.x.y -f local-values.yaml
```

Replace `<release-name>` with the name used during the initial installation (use `helm ls` to find it).
If needed, specify the Kubernetes namespace with `-n` (default namespace is used if not specified).

### Additional notes

- **Pod update strategy**

The goal is to find a balance between service continuity and available resources on the cluster. You can define which [update strategy](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#strategy) to use during an upgrade / update.

This configuration is possible for celeryWorkers (`celeryWorkers.worker.updateStrategy`) and webapps (`webapps.app.updateStrategy`).

If not defined, this default strategy applies:

- If less than 3 replicas

```yaml
type: RollingUpdate
rollingUpdate:
	maxUnavailable: 50%
	maxSurge: 50%
```

- Else

```yaml
type: RollingUpdate
rollingUpdate:
	maxUnavailable: 25%
	maxSurge: 25%
```
