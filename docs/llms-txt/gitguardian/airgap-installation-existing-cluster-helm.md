# Source: https://docs.gitguardian.com/self-hosting/installation/airgap-installation-existing-cluster-helm.md

# Install on an Existing Cluster using Helm (airgap)

> Install GitGuardian self-hosted in air-gapped environments using Helm on an existing Kubernetes cluster.

## Introduction

This guide covers installing GitGuardian in air-gapped environments using Helm on an existing Kubernetes cluster. In air-gapped environments, there is no direct internet connectivity, so this installation method requires downloading GitGuardian Helm charts and images from the internet on a separate machine, then transferring them to your isolated environment.

## Prerequisites

### Required Infrastructure

1. **Kubernetes Cluster**: A running Kubernetes cluster in your isolated environment. See [system requirements](../system-requirements#kubernetes-for-existing-clusters) for details. For OpenShift clusters, refer to the [OpenShift installation guidelines](./openshift).

2. **PostgreSQL Database**: An external PostgreSQL instance with required extensions installed. See [database configuration](./databases/database-config) for setup details.

3. **Redis Instance**: A dedicated Redis instance. See [system requirements](../system-requirements#redis) for configuration details.

4. **Private Image Registry**: A private container registry accessible from your Kubernetes cluster to host GitGuardian images.

### Additional Requirements

5. **Helm**: Helm version 3.13+ installed. See [system requirements](../system-requirements#helm) for version compatibility. Currently, deployment of the app using Helm charts supports only **Helm CLI**, **[ArgoCD](https://argo-cd.readthedocs.io/en/stable/getting_started/)**, and **[FluxCD](https://fluxcd.io/flux/installation/)**.

6. **Domain Name**: A Fully Qualified Domain Name (FQDN) for accessing the application. See [system requirements](../system-requirements#domain-name-requirements).

7. **Image Transfer Tools**: Tools like [Docker](https://docs.docker.com/) or [Skopeo](https://github.com/containers/skopeo) to transfer images to your private registry.

8. **Network Access**: Ensure your isolated environment meets the [network requirements](../network-requirements#isolated-network).

:::caution Requirements
Before starting the installation, ensure to review the **[system](../system-requirements)** and **[network](../network-requirements#isolated-network)** requirements.
:::

## Installation

### Accessing and Downloading the GitGuardian Helm Chart

â ï¸ Ensure you're using the latest version of [helm](https://helm.sh/docs/helm/helm_install/).

The GitGuardian Helm chart is available in the Replicated private registry. The license is included directly in the Helm chart, so no separate license file download is required.

1. **Login to Helm chart registry**: Contact the GitGuardian team at support@gitguardian.com to obtain the password. Log in with this command (replace email with the one provided by GitGuardian):

```bash
helm registry login registry.replicated.com --username your.name@yourcompany.com
```

2. **Download Helm chart locally**: After logging in, download and extract the GitGuardian Helm chart
   into a local directory (e.g., `/home/user`) using:

```bash
cd /home/user
helm fetch oci://registry.replicated.com/gitguardian/gitguardian
```

### Download GitGuardian Images

:::tip
GitGuardian images are accessible through the Replicated proxy registry. To learn how to connect it to a Harbor or JFrog Container Registry instance for pull-through image caching, visit [Using a Registry Proxy for Helm Air Gap Installations](https://docs.replicated.com/vendor/using-third-party-registry-proxy).
:::

You may get current versions in [values reference documentation](/self-hosting/management/infrastructure-management/helm-values).

Below is a list of images to download and upload to your private image registry:

| Image Type         | Repository and Image Name                                                                    | 2026.2         |
| ------------------ | -------------------------------------------------------------------------------------------- | -------------- |
| Front              | proxy.replicated.com/proxy/gitguardian/docker.io/gitguardian/prm-static-chainguard           | 2026.2.0       |
| Backend            | proxy.replicated.com/proxy/gitguardian/docker.io/gitguardian/prm-app-chainguard              | 2026.2.0       |
| Helm Tooling       | proxy.replicated.com/proxy/gitguardian/docker.io/gitguardian/prm-helm-tooling                | 2026.2.0       |
| Machine Learning   | proxy.replicated.com/proxy/gitguardian/docker.io/gitguardian/ml-secret-engine-app-chainguard | 0.4.3          |
| File Scanner       | proxy.replicated.com/proxy/gitguardian/ghcr.io/gitguardian/wolfi/apache-tika                 | 3.2            |
| Replicated SDK     | proxy.replicated.com/proxy/gitguardian/docker.io/replicated/replicated-sdk                   | 1.16.0         |
| Used for Custom CA | proxy.replicated.com/proxy/gitguardian/ghcr.io/gitguardian/wolfi/bash                        | latest         |
| ggscout            | proxy.replicated.com/proxy/gitguardian/ghcr.io/gitguardian/ggscout/chainguard                | 0.24.0         |
| fluent-bit         | proxy.replicated.com/proxy/gitguardian/ghcr.io/gitguardian/wolfi/fluent-bit                  | 4.2.2          |
| loki               | proxy.replicated.com/proxy/gitguardian/ghcr.io/gitguardian/wolfi/loki                        | 3.6.5          |
| minio              | proxy.replicated.com/proxy/gitguardian/ghcr.io/gitguardian/wolfi/minio                       | 0.20251015     |
| analytics          | proxy.replicated.com/proxy/gitguardian/docker.io/gitguardian/basalt-onprem-analytics         | 0.1.1          |

<details>
<summary>Previous release image versions and tags</summary>

| Image Type         | 2026.1       | 2025.12     | 2025.11     |
| ------------------ | ------------ | ----------- | ----------- |
| Front              | 2026.1.0     | 2025.12.0   | 2025.11.1   |
| Backend            | 2026.1.0     | 2025.12.0   | 2025.11.1   |
| Helm Tooling       | 2026.1.0     | 2025.12.0   | 2025.11.1   | 
| Machine Learning   | 20260127     | 20251212    | 20251212    |
| File Scanner       | 3.2          | 3.2         | 3.2         |
| Replicated SDK     | 1.12.2       | 1.12.1      | 1.11.1      |
| Used for Custom CA | latest       | latest      | latest      |
| ggscout            | 0.22.0       | 0.22.0      | 0.20.0      |
| fluent-bit         | 4.2.2        | 4.0.3       | 4.0.3       |
| loki               | 3.6.3        | 3.6.2       | 3.5.8       |
| minio              | 0.20251015   | 0.20251015  | 0.20251015  |
| analytics          | 20260122     | 20251211    | N/A         |

</details>

Contact the GitGuardian team at support@gitguardian.com to obtain your license ID.

Use this ID to authenticate with the GitGuardian image repository by executing the command below. Replace `<your_licenseID>` with your actual License ID.

```sh
LICENSE_ID="<your_licenseID>";
echo "{\"auths\": {\"proxy.replicated.com\": {\"auth\": \"$(echo -n "${LICENSE_ID}:${LICENSE_ID}" | base64)\"}, \"registry.replicated.com\": {\"auth\": \"$(echo -n "${LICENSE_ID}:${LICENSE_ID}" | base64)\"}}}" > ~/.docker/config.json
```

Example on how to download the images with docker pull with the latest release:

::::info Image architecture
All GitGuardian images are published as multi-architecture (multi-arch) manifests. The correct image variant is automatically selected based on the Docker engine host architecture.
::::

```bash
docker pull proxy.replicated.com/proxy/gitguardian/docker.io/gitguardian/prm-static-chainguard:2026.2.0
docker pull proxy.replicated.com/proxy/gitguardian/docker.io/gitguardian/prm-app-chainguard:2026.2.0
docker pull proxy.replicated.com/proxy/gitguardian/docker.io/gitguardian/prm-helm-tooling:2026.2.0
docker pull proxy.replicated.com/proxy/gitguardian/docker.io/gitguardian/ml-secret-engine-app-chainguard:0.4.3
docker pull proxy.replicated.com/proxy/gitguardian/ghcr.io/gitguardian/wolfi/apache-tika:3.2
docker pull proxy.replicated.com/proxy/gitguardian/docker.io/replicated/replicated-sdk:1.16.0
docker pull proxy.replicated.com/proxy/gitguardian/ghcr.io/gitguardian/wolfi/bash:latest
docker pull proxy.replicated.com/proxy/gitguardian/ghcr.io/gitguardian/ggscout/chainguard:0.24.0
docker pull proxy.replicated.com/proxy/gitguardian/ghcr.io/gitguardian/ggscout/chainguard-bash:0.24.0
docker pull proxy.replicated.com/proxy/gitguardian/ghcr.io/gitguardian/wolfi/fluent-bit:4.2.2
docker pull proxy.replicated.com/proxy/gitguardian/ghcr.io/gitguardian/wolfi/loki:3.6.5
docker pull proxy.replicated.com/proxy/gitguardian/ghcr.io/gitguardian/wolfi/minio:0.20251015
docker pull proxy.replicated.com/proxy/gitguardian/docker.io/gitguardian/basalt-onprem-analytics:0.1.1
```

You can verify that the images have been correctly downloaded and upload them to your private image registry.

```bash
docker images | grep replicated
```

:::info
For this process, you can utilize a tool like [Skopeo](https://github.com/containers/skopeo) to handle image transfers. Additionally, if you need to set up a proxy to access the replicated registry, refer to the [Docker documentation](https://docs.docker.com/network/proxy/#configure-the-docker-client).
:::

### Upload GitGuardian Images

Ensure the following directory structure is respected in your **private registry**:

| Path and image name                                 |
| --------------------------------------------------- |
| `/gitguardian/prm-static-chainguard`                |
| `/gitguardian/prm-static-chainguard-fips`           |
| `/gitguardian/prm-app-chainguard`                   |
| `/gitguardian/prm-app-chainguard-fips`              |
| `/gitguardian/prm-helm-tooling`                     |
| `/gitguardian/ml-secret-engine-app-chainguard`      |
| `/gitguardian/ml-secret-engine-app-chainguard-fips` |
| `/gitguardian/wolfi/apache-tika`                    |
| `/gitguardian/ggscout/chainguard`                   |
| `/gitguardian/ggscout/chainguard-bash`              |
| `/gitguardian/wolfi/fluent-bit`                     |
| `/gitguardian/wolfi/loki`                           |
| `/gitguardian/wolfi/minio-bitnami`                  |
| `/gitguardian/wolfi/bash`                           |
| `/replicated/replicated-sdk`                        |

#### FIPS Compliance for Airgap Installations

:::info
FIPS (Federal Information Processing Standards) compliance is available for airgap Helm installations with additional steps.
:::

If you require FIPS-compliant cryptographic modules for your air gap installation, download the FIPS images (with `-fips` suffix):
  - `proxy.replicated.com/proxy/gitguardian/docker.io/gitguardian/prm-static-chainguard-fips`
  - `proxy.replicated.com/proxy/gitguardian/docker.io/gitguardian/prm-app-chainguard-fips`
  - `proxy.replicated.com/proxy/gitguardian/docker.io/gitguardian/ml-secret-engine-app-chainguard-fips`

### Kubernetes Application RBAC

The following RBAC roles are required for the proper functioning of the application, enabling the Replicated SDK to validate customer license entitlements and ensuring non-skippable versions are not bypassed during upgrades.

If you are not a `cluster-admin` in your Kubernetes cluster, you will need to apply the configuration below in your targeted namespace `<gitguardian_namespace>`:

<details>
<summary>RBAC Roles Helm install</summary>

```yaml
# GitGuardian Role
---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: gim-role
rules:
- apiGroups:
  - ''
  resources:
  - configmaps
  - secrets
  verbs:
  - get
  - list
  - watch

# GitGuardian RoleBinding
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: gim-rolebinding
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: gim-role
subjects:
- kind: ServiceAccount
  name: gim-migration
- kind: ServiceAccount
  name: gim

# Upgrade-path-check Role
---
kind: Role
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: upgrade-path-check
rules:
- apiGroups:
  - ''
  resources:
  - configmaps
  verbs:
  - get
  - list

# Upgrade-path-check RoleBindng
---
kind: RoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: upgrade-path-check
roleRef:
  kind: Role
  name: upgrade-path-check
  apiGroup: rbac.authorization.k8s.io
subjects:
  - kind: ServiceAccount
    name: upgrade-path-check

# Replicated SDK Role
---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: replicated-role
rules:
- apiGroups:
  - ''
  resources:
  - configmaps
  - persistentvolumeclaims
  - pods
  - secrets
  - services
  verbs:
  - get
  - list
  - watch
- apiGroups:
  - apps
  resources:
  - daemonsets
  - deployments
  - replicasets
  - statefulsets
  verbs:
  - get
  - list
  - watch
- apiGroups:
  - networking.k8s.io
  - extensions
  resources:
  - ingresses
  verbs:
  - get
  - list
  - watch
- apiGroups:
  - ''
  resources:
  - secrets
  verbs:
  - create
- apiGroups:
  - ''
  resources:
  - secrets
  verbs:
  - update
  resourceNames:
  - replicated
  - replicated-instance-report
  - replicated-custom-app-metrics-report
  - replicated-meta-data

# Replicated SDK RoleBinding
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: replicated-rolebinding
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: replicated-role
subjects:
- kind: ServiceAccount
  name: replicated

# Support Bundle
# Below role is mandatory
---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: support-bundle
  namespace: <gitguardian_namespace>
rules:
- apiGroups: ['*']
  resources: ['*']
  verbs: ['get', 'list', 'watch']
- apiGroups: ['']
  resources: ['pods/exec']
  verbs: ['create']
# This role is optional and is used to retrieve cluster-scoped information, which can be useful for troubleshooting
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: support-bundle
rules:
- apiGroups: ['']
    resources: ['namespaces', 'nodes']
    verbs: ['get', 'list', 'watch']
- apiGroups: ['apiextensions.k8s.io']
  resources: ['customresourcedefinitions']
  verbs: ['get', 'list', 'watch']
- apiGroups: ['storage.k8s.io']
  resources: ['storageclasses']
  verbs: ['get', 'list', 'watch']
```

</details>

### Customize the local values file

This installation offers multiple customization options. Use a local values file (named `local-values.yaml`) for customizations when installing any Helm application.

Ensure your values file configures these essential elements:

At the minimum, your values must configure the following elements:

- `hostname`
- `postgres`
- `redis`
- `onPrem.adminUser`

Below is an example values file covering these elements, **adapted for airgap installation**:

```yaml
hostname: gitguardian.internal.yourcompany.com # Hostname where the instance will be accessed

# Airgap-specific configuration
global:
  imageRegistry: docker.internal/example/path # Location of the GitGuardian images in your private registry
  image:
    registry:  docker.internal/example/path # Location of the GitGuardian images (same as imageRegistry)
  imagePullSecrets:
    - name: pull-secret # Existing docker secret used to pull images from your private registry

proxy:
  noProxyHostNames:
    - 127.0.0.1
    - 10.0.0.0/8
  existingSecret: 'gim-proxy'
  existingSecretKeys:
    httpProxyUrl: 'http_proxy'   # Secret should contain: http://username:password@proxy.company.com:8080
    httpsProxyUrl: 'https_proxy' # Secret should contain: https://username:password@proxy.company.com:8080

replicated:
  isAirgap: false # Set to true only for environments without Internet access and no HTTP proxy configured
  privateCASecret: # optional if you are using a custom CA
    name: custom-ca-secret-name
    key: 'custom-ca.pem'
  extraEnv:
    - name: NO_PROXY
      valueFrom:
        configMapKeyRef:
          name: gim-config
          key: 'NO_PROXY'
    - name: HTTP_PROXY
      valueFrom:
        secretKeyRef:
          name: 'gim-proxy'
          key: 'http_proxy'        # Example: http://username:password@proxy.company.com:8080
    - name: HTTPS_PROXY
      valueFrom:
        secretKeyRef:
          name: 'gim-proxy'
          key: 'https_proxy'       # Example: https://username:password@proxy.company.com:8080

postgresql:
  host: gitguardian-postgres # PostgreSQL host
  username: postgres # PostgreSQL username
  database: gitguardian # PostgreSQL database name
  existingSecret: gitguardian-postgresql-secret # Kubernetes secret where to check the PostgreSQL password
  existingSecretKeys:
    password: postgres-password # Name of the key containing password in the secret

redis:
  main:
    host: gitguardian-redis # Redis host
    tls:
      enabled: false # Set TLS encryption for Redis
    existingSecret: gitguardian-redis-secret # Kubernetes secret where to check the Redis password
    existingSecretKeys:
      url: redis-url # Name of the key containing redis url in the secret

onPrem:
  adminUser:
    email: your.name@yourcompany.com # email of the instance admin user
    firstname: YourName # name of the instance admin user
```

**Important Airgap Configuration Notes:**

Replace `docker.internal/example/path` with your private registry and the appropriate path where the images are stored in your registry. Ensure you maintain the specified directory structure outlined in the "Upload GitGuardian Images" section.

For detailed guidance on:

- configurable parameters, refer to the [Helm Chart Values Reference](../management/infrastructure-management/helm-values) page.
- `existingSecret` parameter and its setup process, visit the [Helm Sensitive Information Management](./helm-secrets) page.
- database configuration, see [Configure Your Database](./databases/database-config).
- scaling options, consult the [Scaling Documentation](../management/infrastructure-management/scaling).
- HTTP proxy, see [Configure a proxy server](../management/infrastructure-management/proxy-server).

### Enable FIPS Compliance (Optional)

If you require FIPS-compliant cryptographic modules, you can enable them by adding the following to your `local-values.yaml` file:

```yaml
global:
  fips:
    enabled: true
```

When FIPS is enabled in airgap environments, ensure you have downloaded and uploaded the FIPS images as outlined in the [FIPS Compliance for Airgap Installations](#fips-compliance-for-airgap-installations) section above. The installation will automatically use FIPS-compliant versions of the application images that include specialized cryptographic modules meeting Federal Information Processing Standards.

For more information about FIPS compliance and security considerations, see the [Security Recommendations](../security/recommendations) page.

### Configure network access to the application

The application front end is behind a Service object named `nginx`. You can configure access to the application in different ways:

1. Configure the service as a `LoadBalancer` using `front.service.type` value. See [Load-balancer](../management/infrastructure-management/load-balancer) for more details.
2. Add an Ingress object routing to the `nginx` service. See [Ingress](../management/infrastructure-management/ingress) for more details.
3. If your cluster has `istio` service mesh, activate it with the `istio.enabled` value. This will enable the proper Gateway and VirtualService objects.

Please note that the `nginx` service is not configured with SSL support. You must configure it and manage your TLS certificate through your Load-Balancer, Ingress or Service Mesh.

### Run preflight checks ð¦

:::caution Requirements
Preflight checks are critical for a successful installation. The following rules apply:

- :x: **Preflight Check Failures**: If preflight checks fail, the installation must not continue until the targeted environment meets all requirements. Please reach out to our **[support team](mailto:support@gitguardian.com)** if needed.
- :warning: **Preflight Check Warnings**: If preflight checks return warnings, the installation can proceed, but it is recommended that you address these warnings to comply with our **[recommendations](../system-requirements)**.

:::

We strongly advise you to run our preflight script to ensure your existing cluster meets GitGuardian's requirements. Retrieve the script from our public repository [here](https://github.com/GitGuardian/ggtools/tree/main/helm-preflights).

Specify an existing Kubernetes namespace using the `-n` option. If not specified, the script will run in your default namespace.
Replace `<release-name>` with your desired [helm release name](https://helm.sh/docs/intro/using_helm/#helm-install-installing-a-package).

**For airgap installations**, use the local Helm chart file:

```bash
./preflights.sh -r <release-name> -n <namespace> gitguardian-<version>.tgz -f local-values.yaml
```

### Install the application

Use the following command to install the application using your `local-values.yaml` file.
Replace `<release-name>` with your desired [helm release name](https://helm.sh/docs/intro/using_helm/#helm-install-installing-a-package).

Specify an existing kubernetes namespace with the `-n` option. If not specified, Helm installs GitGuardian in your default namespace.
Use the `--create-namespace` option to create the namespace if it doesn't exist.

**For airgap installations**, use the local Helm chart file instead of the remote repository:

```bash
helm install <release-name> --timeout 30m -n <namespace> --create-namespace gitguardian-<version>.tgz -f local-values.yaml
```

**Note**: The installation may take a few minutes due to database migrations.

### Verify the installation

Upon successful installation, you should see the following output:

```shell
NAME: <release-name>
LAST DEPLOYED: Mon May 15 16:15:56 2023
NAMESPACE: <namespace>
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
Thank you for installing GitGuardian Internal Monitoring.
```

These notes can later be retrieved with `helm get notes <release-name>`

### Save the Data Encryption Key

:::caution

GitGuardian encrypts all sensitive information in the database using an encryption key (aka Django Secret Key). In case of disaster recovery, this key will be needed to restore your data.

:::

When you don't specify it either using inline parameter `miscEncryption.djangoSecretKey` or using an existing secret with `miscEncryption.existingSecret`, the data encryption key is automatically generated by the Helm chart. You should save it and keep it in **a secure location**. Use the following command to display the key:

```shell
kubectl get secrets gim-secrets --namespace=<namespace> -o jsonpath='{.data.DJANGO_SECRET_KEY}' | base64 -d
```

If needed, specify the Kubernetes namespace with `--namespace` (default namespace is used if not specified).

### Application login

Upon successful installation, you will need to get your temporary admin password. Use the following command:

```bash
kubectl get secrets gim-secrets --namespace=<namespace> -o jsonpath='{.data.ADMIN_PASSWORD}'| base64 -d
```

If needed, specify the Kubernetes namespace with `--namespace` (default namespace is used if not specified).

You can access the application using the hostname you provided, using the login with the email provided in the `onPrem.adminUser.email` and the temporary password.

### Troubleshooting

If you encounter issues during the installation process, you can generate a support bundle for the GitGuardian team to diagnose and resolve problems more efficiently. See the [support bundle documentation](../troubleshoot/support#helm-based-installation) for detailed instructions.

## Next Steps

After successful installation:
- Access your GitGuardian instance using the hostname you configured
- Log in with the administrator credentials you set up (change the temporary password on first login)
- Configure [email settings](../management/application-management/email-configuration) for notifications
- Set up [SSO](../../platform/enterprise-administration/saml-sso-configuration) and [SCIM](../../platform/enterprise-administration/scim-configuration) integration (optional)
- [Integrate your first repositories](/platform/getting-started/integrate) to begin secret detection
