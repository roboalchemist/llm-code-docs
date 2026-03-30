# Source: https://docs.gitguardian.com/self-hosting/installation/installation-existing-cluster-helm.md

# Install on an Existing Cluster using Helm

> Install GitGuardian self-hosted on an existing Kubernetes cluster using Helm, the recommended installation method.

## Introduction

GitGuardian can be installed on your existing Kubernetes cluster using [Helm](https://helm.sh/), a package manager for Kubernetes. GitGuardian supports deployment on bare metal, private, or public clouds.

## Prerequisites

### Required Infrastructure

1. **Kubernetes Cluster**: A running Kubernetes cluster. See [system requirements](../system-requirements#kubernetes-for-existing-clusters) for details. For OpenShift clusters, refer to the [OpenShift installation guidelines](./openshift).

2. **PostgreSQL Database**: An external PostgreSQL instance with required extensions installed. See [database configuration](./databases/database-config) for setup details.

3. **Redis Instance**: A dedicated Redis instance. See [system requirements](../system-requirements#redis) for configuration details.

### Additional Requirements

4. **Helm**: Helm version 3.13+ installed. See [system requirements](../system-requirements#helm) for version compatibility. Currently, deployment of the app using Helm charts supports only **Helm CLI**, **[ArgoCD](https://argo-cd.readthedocs.io/en/stable/getting_started/)**, and **[FluxCD](https://fluxcd.io/flux/installation/)**. Helm installations support both AMD64 and ARM64 clusters; see [architecture](../system-requirements#architecture).

5. **Network Access**: Ensure your cluster meets the [network requirements](../network-requirements).

6. **Domain Name**: A Fully Qualified Domain Name (FQDN) for accessing the application. See [system requirements](../system-requirements#domain-name-requirements).

:::caution Requirements
Review the complete **[system](../system-requirements)** and **[network](../network-requirements)** requirements before proceeding.
:::

## Installation

:::note
Only the following methods are supported to deploy the app using Helm charts: **Helm CLI** and **ArgoCD**.

For GitGuardian installation in an Airgap environment, utilize a private image repository.
Detailed instructions are available on the **[Install on Airgap](./airgap-installation-existing-cluster-helm)** page.
:::

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

### Accessing the Helm Chart Registry

â ï¸ Ensure you're using the latest version of [helm](https://helm.sh/docs/helm/helm_install/).

The GitGuardian Helm chart is available in the Replicated private registry. The license is included directly in the Helm chart, so no separate license file download is required.

Contact the GitGuardian team at support@gitguardian.com to obtain the password.

To log in, use the command below, replacing the email with the one provided by the GitGuardian team:

```bash
helm registry login registry.replicated.com --username your.name@yourcompany.com
```

### Customize the local values file

This installation offers multiple customization options. Use a local values file (named `local-values.yaml`)
for customizations when installing any Helm application.

Ensure your values file configures these essential elements:

At the minimum, your values must configure the following elements:

- `hostname`
- `postgres`
- `redis`
- `onPrem.adminUser`

Below is an example values file covering these elements:

```yaml
hostname: gitguardian.internal.yourcompany.com # Hostname where the instance will be accessed

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

When FIPS is enabled, the installation will use FIPS-compliant versions of the application images that include specialized cryptographic modules meeting Federal Information Processing Standards, ensuring top-tier encryption of sensitive data, both at rest and in transit.

For more information about FIPS compliance and security considerations, see the [Security Recommendations](../security/recommendations) page.

### Configure network access to the application

The application front end is behind a Service object named `nginx`.
You can configure access to the application in different ways:

1. Configure the service as a `LoadBalancer` using `front.service.type` value. See
   [Load-balancer](../management/infrastructure-management/load-balancer) for
   more details.
2. Add an Ingress object routing to the `nginx` service. See
   [Ingress](../management/infrastructure-management/ingress) for more
   details.
3. If your cluster has `istio` service mesh, activate it with the
   `istio.enabled` value. This will enable the proper Gateway and VirtualService
   objects.

Please note that the `nginx` service is not configured with SSL support. You must configure it
and manage your TLS certificate through your Load-Balancer, Ingress or Service Mesh.

### Run preflight checks ð¦

:::caution Requirements
Preflight checks are critical for a successful installation. The following rules apply:

- :x: **Preflight Check Failures**: If preflight checks fail, the installation must not continue until the targeted environment meets all requirements. Please reach out to our **[support team](mailto:support@gitguardian.com)** if needed.
- :warning: **Preflight Check Warnings**: If preflight checks return warnings, the installation can proceed, but it is recommended that you address these warnings to comply with our **[recommendations](../system-requirements)**.

:::

We strongly advise you to run our preflight script to ensure your existing cluster meets GitGuardian's requirements. Retrieve the script from our public repository [here](https://github.com/GitGuardian/ggtools/tree/main/helm-preflights).

Specify an existing Kubernetes namespace using the `-n` option. If not specified, the script will run in your default namespace.
Replace `<release-name>` with your desired [helm release name](https://helm.sh/docs/intro/using_helm/#helm-install-installing-a-package).

```bash
./preflights.sh -r <release-name> -n <namespace> oci://registry.replicated.com/gitguardian/gitguardian -f local-values.yaml
```

### Install the application

Use the following command to install the application using your `local-values.yaml` file.
Replace `<release-name>` with your desired [helm release name](https://helm.sh/docs/intro/using_helm/#helm-install-installing-a-package).

Specify an existing kubernetes namespace with the `-n` option. If not specified, Helm installs GitGuardian in your default namespace.
Use the `--create-namespace` option to create the namespace if it doesn't exist.

```bash
helm install <release-name> --timeout 30m -n <namespace> --create-namespace oci://registry.replicated.com/gitguardian/gitguardian -f local-values.yaml
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

GitGuardian encrypts all sensitive information in the database using an
encryption key (aka Django Secret Key). In case of disaster recovery, this key
will be needed to restore your data.

:::

When you don't specify it either using inline parameter `miscEncryption.djangoSecretKey` or using an existing secret with `miscEncryption.existingSecret`, the data encryption key is automatically generated by the Helm chart. You should save it and keep it in **a secure location**. Use the following command
to display the key:

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

You can access the application using the hostname you provided, using the login
with the email provided in the `onPrem.adminUser.email` and the temporary
password.

### Troubleshooting

If you encounter issues during the installation process, you can generate a support bundle for the GitGuardian team to diagnose and resolve problems more efficiently. See the [support bundle documentation](../troubleshoot/support#helm-based-installation) for detailed instructions.

## Next Steps

After successful installation:
- Access your GitGuardian instance using the hostname you configured
- Log in with the administrator credentials you set up (change the temporary password on first login)
- Configure [email settings](../management/application-management/email-configuration) for notifications
- Set up [SSO](../../platform/enterprise-administration/saml-sso-configuration) and [SCIM](../../platform/enterprise-administration/scim-configuration) integration (optional)
- [Integrate your first repositories](/platform/getting-started/integrate) to begin secret detection
