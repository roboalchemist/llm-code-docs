# Source: https://docs.gitguardian.com/self-hosting/installation/installation-existing-cluster-kots.md

# Install on an Existing Cluster using KOTS

> [Deprecated] Install GitGuardian on an existing Kubernetes cluster using KOTS (Kubernetes Off-The-Shelf).

## Introduction

:::danger Deprecation Notice
This installation method will be deprecated and unsupported after the June 2026 release (version 2026.6.0). Please use the [Helm installation on an existing cluster](./installation-existing-cluster-helm) instead.
:::

**â ï¸ Use the [Helm installation on an existing cluster](./installation-existing-cluster-helm) unless instructed otherwise.**

GitGuardian can be installed on your existing Kubernetes cluster using [KOTS](https://kots.io),
a kubectl plugin and KOTS Admin Console to help manage Kubernetes Off-The-Shelf software.

GitGuardian supports deployment on bare metal, private, or public clouds.

## Prerequisites

### Required Infrastructure

1. **Kubernetes Cluster**: A running Kubernetes cluster. See [system requirements](../system-requirements#kubernetes-for-existing-clusters) for details. For OpenShift clusters, refer to the [OpenShift installation guidelines](./openshift).

2. **PostgreSQL Database**: An external PostgreSQL instance with required extensions installed. See [database configuration](./databases/database-config) for setup details.

3. **Redis Instance**: A dedicated Redis instance. See [system requirements](../system-requirements#redis) for configuration details.

### Additional Requirements

4. **License File**: Download your GitGuardian license from the portal. See [license management](../license-management#kots-existing-cluster-installation) for instructions.

5. **Network Access**: Ensure your cluster meets the [network requirements](../network-requirements).

6. **Domain Name**: A Fully Qualified Domain Name (FQDN) for accessing the application. See [system requirements](../system-requirements#domain-name-requirements).

:::caution Requirements
Review the complete **[system](../system-requirements)** and **[network](../network-requirements)** requirements before proceeding.
:::

## Installation

### KOTS plugin

First, you need to install the KOTS plugin for `kubectl`. You can do this with
this command:

```bash
curl https://kots.io/install | bash
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

And proceed with the KOTS Admin Console step.

### KOTS Admin Console

Once you have the plugin installed, you can install the KOTS Admin Console.

If you are `cluster-admin`:

```bash
kubectl kots install gitguardian
```

If not:

```bash
kubectl kots install --ensure-rbac=false gitguardian
```

You will be prompted to choose a namespace to deploy the application and a
password to access the KOTS Admin Console.

![Namespace and password prompt](/img/self-hosting/installation/replicated_choose_namespace_and_password.png)

Once the installation of the KOTS Admin Console is finished, a port forward will be
set up, and you will be able to access the KOTS Admin Console on
http://localhost:8800.

:::tip

**KOTS Admin Console**

By default, this is accessed on http://localhost:8800 using this command
`kubectl kots admin-console --namespace=<namespace>`, which is a wrapper
around `kubectl port-forward`. You can configure an ingress if you want a public
endpoint.
:::

Launch

![End of existing cluster installation](/img/self-hosting/installation/replicated_end_existing_install.png)

### Application

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

GitGuardian encrypts all sensitive information in the database using an
encryption key (aka Django Secret Key). In case of disaster recovery, this key
will be needed to restore your data.

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
