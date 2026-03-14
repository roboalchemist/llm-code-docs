# Source: https://docs.gitguardian.com/self-hosting/installation/airgap-installation-existing-cluster-kots.md

# Install airgap using KOTS existing cluster

> [Deprecated] Install GitGuardian in air-gapped environments using KOTS on an existing Kubernetes cluster.

## Introduction

:::danger Deprecation Notice
This installation method will be deprecated and unsupported after the June 2026 release (version 2026.6.0). Please use the [Helm installation on an existing cluster](./airgap-installation-existing-cluster-helm) instead.
:::

**â ï¸ Use the [Helm installation on an existing cluster](./airgap-installation-existing-cluster-helm) unless instructed otherwise.**

This guide covers installing GitGuardian in air-gapped environments using KOTS (Kubernetes Off-The-Shelf) on an existing Kubernetes cluster. In air-gapped environments, there is no direct internet connectivity, so this installation method requires downloading GitGuardian bundles from the internet on a separate machine, then transferring them to your isolated environment.

## Prerequisites

### Required Infrastructure

1. **Kubernetes Cluster**: A running Kubernetes cluster in your isolated environment. See [system requirements](../system-requirements#kubernetes-for-existing-clusters) for details. For OpenShift clusters, refer to the [OpenShift installation guidelines](./openshift).

2. **PostgreSQL Database**: An external PostgreSQL instance with required extensions installed. See [database configuration](./databases/database-config) for setup details.

3. **Redis Instance**: A dedicated Redis instance. See [system requirements](../system-requirements#redis) for configuration details.

4. **Private Image Registry**: A private container registry accessible from your Kubernetes cluster to host GitGuardian images.

### Additional Requirements

1. **License File** (for KOTS installation): Download your GitGuardian license from the portal. See [license management](../license-management) for instructions.

2. **Network Access**: Ensure your isolated environment meets the [network requirements](../network-requirements#isolated-network).

3. **Domain Name**: A Fully Qualified Domain Name (FQDN) for accessing the application. See [system requirements](../system-requirements#domain-name-requirements).

:::caution Requirements
Before starting the installation, ensure to review the **[system](../system-requirements)** and **[network](../network-requirements#isolated-network)** requirements, and **[download your license](../license-management)**.
:::

## Installation

### Download and Install the KOTS Admin Console

First, install the `kubectl` KOTS plugin on your machine:

```
curl https://kots.io/install | bash
```

Then, you need to download the latest bundle for the KOTS Admin Console. There
are two places to download it. The first and recommended one is the download
portal where you can also download your license and the application bundle. The
second one is the
[release assets on GitHub](https://github.com/replicatedhq/kots/releases). In
both cases, make sure to match your locally installed KOTS plugin version. You
can check it by running:

```
kubectl kots version
```

### Kubernetes Application RBAC

The KOTS Admin Console will have full control over all resources across all namespaces in the cluster.
More information in [Replicated documentation](https://docs.replicated.com/vendor/packaging-rbac#about-cluster-scoped-rbac).

If you are not `cluster-admin` in your Kubernetes cluster or do not want to
grant the KOTS Admin Console such wide permissions, you will need to apply the
below configuration in your targeted namespace `<gitguardian_namespace>`:

<details>
<summary>RBAC Roles KOTS install</summary>

```yaml
---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: kotsadm
  namespace: <gitguardian_namespace>
  labels:
    kots.io/backup: velero
    kots.io/kotsadm: 'true'

---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: kotsadm-role
  namespace: <gitguardian_namespace>
  labels:
    kots.io/backup: velero
    kots.io/kotsadm: 'true'
rules:
  - apiGroups: ['']
    resources:
      [
        'configmaps',
        'persistentvolumeclaims',
        'pods',
        'secrets',
        'services',
        'limitranges',
        'serviceaccounts',
      ]
    verbs: ['get', 'list', 'watch', 'create', 'update', 'patch', 'delete']
  - apiGroups: ['apps']
    resources:
      [
        'daemonsets',
        'deployments',
        'deployments/scale',
        'replicasets',
        'statefulsets',
      ]
    verbs: ['get', 'list', 'watch', 'create', 'update', 'patch', 'delete']
  - apiGroups: ['batch']
    resources: ['jobs', 'cronjobs']
    verbs: ['get', 'list', 'watch', 'create', 'update', 'patch', 'delete']
  - apiGroups: ['networking.k8s.io', 'extensions']
    resources: ['ingresses', 'networkpolicies']
    verbs: ['get', 'list', 'watch', 'create', 'update', 'patch', 'delete']
  - apiGroups: ['policy']
    resources: ['poddisruptionbudgets']
    verbs: ['get', 'list', 'watch', 'create', 'update', 'patch', 'delete']
  - apiGroups: ['']
    resources: ['namespaces', 'endpoints']
    verbs: ['get']
  - apiGroups: ['authorization.k8s.io']
    resources: ['selfsubjectaccessreviews', 'selfsubjectrulesreviews']
    verbs: ['create']
  - apiGroups: ['rbac.authorization.k8s.io']
    resources: ['roles', 'rolebindings']
    verbs: ['get', 'list', 'watch', 'create', 'update', 'patch', 'delete']
  - apiGroups: ['']
    resources: ['pods/log', 'pods/exec']
    verbs: ['get', 'list', 'watch', 'create']
  - apiGroups: ['batch']
    resources: ['jobs/status']
    verbs: ['get', 'list', 'watch']
  - apiGroups: ['monitoring.coreos.com']
    resources: ['servicemonitors']
    verbs: ['get', 'list', 'watch', 'create', 'update', 'patch', 'delete']
  - apiGroups: ['']
    resources: ['events']
    verbs: ['list']

---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: kotsadm-rolebinding
  namespace: <gitguardian_namespace>
  labels:
    kots.io/backup: velero
    kots.io/kotsadm: 'true'
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: kotsadm-role
subjects:
  - kind: ServiceAccount
    name: kotsadm
```
</details>

### Upload Admin Console Images to Private Registry

Now you need to upload these images to your registry using a user with write
access to your internal registry:

```bash
kubectl kots admin-console push-images ./kotsadm.tar.gz \
  ${private.registry.host}/gitguardian \
  --registry-username ${rw-username} \
  --registry-password ${rw-password}
```

The username and password for the registry are not stored anywhere.

### Install the KOTS Admin Console

Finally, you can run the install command for the KOTS Admin Console.

If you are `cluster-admin`:

```bash
kubectl kots install gitguardian \
  --kotsadm-namespace gitguardian \
  --kotsadm-registry ${private.registry.host} \
  --registry-username ${ro-username} \
  --registry-password ${ro-password}
```

If you are not `cluster-admin` (and applied the RBAC configuration above):

```bash
kubectl kots install --ensure-rbac=false gitguardian \
  --kotsadm-namespace gitguardian \
  --kotsadm-registry ${private.registry.host} \
  --registry-username ${ro-username} \
  --registry-password ${ro-password}
```

A Kubernetes secret will be used to store these credentials.

You will be prompted to choose a password to access the KOTS Admin Console if one wasn't provided during installation.

An automatic port-forward is launched, you can now access the KOTS Admin Console on http://localhost:8800.

:::tip

**KOTS Admin Console**

By default, this is accessed on http://localhost:8800 using this command `kubectl kots admin-console --namespace=<namespace>`, which is a wrapper around `kubectl port-forward`. You can configure an ingress if you want a public endpoint.

:::

### Download Application Bundle

First, you will need to download the license and the application bundle from the download portal. The application bundle filename should end with `.airgap`.

![Download portal airgap embedded](/img/self-hosting/installation/replicated_download_portal_airgap_existing.png)

Transfer both the license file and the application bundle to your airgap environment where you can access the KOTS Admin Console.

## Application Configuration

Once the KOTS Admin Console is running and you have uploaded the admin console bundle, you can proceed with the application configuration:

1. Enter the password provided at the end of the cluster installation.

![Admin console password](/img/self-hosting/installation/replicated_password_form.png)

2. Upload the license downloaded on the portal ([see instructions on how to download the license file](../license-management#download)).

![License upload](/img/self-hosting/installation/replicated_license_upload.png)

3. Configure the application. You need to fill in all the required fields:

   - **Application Hostname**: Enter the Fully Qualified Domain Name (FQDN) for the GitGuardian application.
   - **Admin User Fields**: These fields are used to create the first GitGuardian user. You'll need to change the password upon the first login.
   - **Databases**: You must select an external PostgreSQL and Redis, see [Configure your database](./databases/database-config). When utilizing Redis Sentinel for high availability, ensure that the Redis master password matches with the Redis sentinel's password and that you're using the correct Sentinel port (default: 26379).

![Admin console application configuration](/img/self-hosting/installation/replicated_configure_app.png)

Additional configuration options include:

- **Scaling**: Adjust the number of replicas for each application component. For more details, visit the [Scaling](../management/infrastructure-management/scaling) page.
- **Prometheus**: Activate an exporter for [Prometheus](../management/application-management/metrics).
- **Ingress TLS Certificate**: This is for the GitGuardian Application. You can either use auto-generated self-signed certificates or upload your own. For self-signed or private CA certificates, disable SSL verification for the GitHub webhook. Learn more on the [Configure TLS certificates](../security/tls-certificates) page.
- **Load Balancer**: Change the Service type can be changed from ClusterIP to [LoadBalancer](../management/infrastructure-management/load-balancer) if needed.
- **Custom Certificate Authority**: Provide a [custom CA](../security/custom-ca) if necessary.
- **HTTP(s) Proxy**: Refer to the [proxy](../management/infrastructure-management/proxy-server) section if needed.

4. Check if preflight checks pass.

:::caution Requirements
Preflight checks are critical for a successful installation. The following rules apply:

- :x: **Preflight Check Failures**: If preflight checks fail, the installation **must not continue** until the targeted environment meets all requirements. Please reach out to our **[support team](mailto:support@gitguardian.com)** if needed.
- :warning: **Preflight Check Warnings**: If preflight checks return warnings, the installation can proceed, but it is recommended that you address these warnings to comply with our **[recommendations](../system-requirements)**.

:::

![Admin console preflights](/img/self-hosting/installation/replicated_preflights.png)

5. Launch

The first installation of the application requires a few minutes to create all
database objects.
Once the process is completed, you will be able to log in to the dashboard
using the administrator user you defined.

### Save the Data Encryption Key

:::caution

GitGuardian encrypts all sensitive information in the database using an encryption key (aka Django Secret Key). In case of disaster recovery, this key will be needed to restore your data.

:::

You should save it and keep it in **a secure location**. Use the following command to display the key:

```shell
kubectl get secrets gim-secrets --namespace=<namespace> -o jsonpath='{.data.DJANGO_SECRET_KEY}' | base64 -d
```

If needed, specify the Kubernetes namespace with `--namespace` (default namespace is used if not specified).

### Troubleshooting

If you encounter issues during the installation process, you can generate a support bundle for the GitGuardian team to diagnose and resolve problems more efficiently. See the [support bundle documentation](../troubleshoot/support#kots-based-installation) for detailed instructions.

## Next Steps

After successful installation:
- Access your GitGuardian instance using the hostname you configured
- Log in with the administrator credentials you set up (change the temporary password on first login)
- Configure [email settings](../management/application-management/email-configuration) for notifications
- Set up [SSO](../../platform/enterprise-administration/saml-sso-configuration) and [SCIM](../../platform/enterprise-administration/scim-configuration) integration (optional)
- [Integrate your first repositories](/platform/getting-started/integrate) to begin secret detection
