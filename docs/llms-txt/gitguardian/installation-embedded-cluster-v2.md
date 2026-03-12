# Source: https://docs.gitguardian.com/self-hosting/installation/installation-embedded-cluster-v2.md

# Install on an Embedded cluster

> Install GitGuardian self-hosted using the Replicated Embedded Cluster v2 method for a simplified single-node deployment.

## Introduction

**â ï¸ Note that embedded installations are not recommended for production use and are better suited for trial or Proof of Concept (PoC) purposes. More information [here](./choose-embedded-existing#how-to-choose-between-these-options).**

GitGuardian can be installed with an embedded Kubernetes distribution packaged with it and supports deployment on bare metal, private, or public clouds.

## Prerequisites

### Required Infrastructure

1. **Linux Virtual Machine**: See [system requirements](../system-requirements#embedded-kubernetes-cluster-installation) for detailed hardware and OS specifications.

   **Example VM instances that meet minimum requirements:**
   - **AWS**: `m7a.2xlarge` (8 vCPUs, 32 GiB RAM)
   - **GCP**: `n2-standard-8` (8 vCPUs, 32 GB RAM)
   - **Azure**: `Standard_D8s_v5` (8 vCPUs, 32 GiB RAM)

### Additional Requirements

2. **License File**: Download your GitGuardian license from the portal. See [license management](../license-management) for instructions.

3. **Network Access**: Ensure your cluster meets the [network requirements](../network-requirements).

4. **Domain Name**: A Fully Qualified Domain Name (FQDN) for accessing the application. See [system requirements](../system-requirements#domain-name-requirements).

:::caution Requirements
Review the complete **[system](../system-requirements)** and **[network](../network-requirements)** requirements before proceeding.
:::

## Installation

### Embedded cluster

Contact the GitGuardian team at support@gitguardian.com to obtain your license ID. The license is embedded directly in the installer bundle, eliminating the need for a separate license file download.

To begin the installation, execute the following commands on your host system. The installation process takes approximately 5 minutes to complete. Consider using a terminal multiplexer like `screen` or `tmux` to prevent interruption due to connection loss. Replace `your_license` with the license ID provided by the GitGuardian team.

```bash
LICENSE_ID=your_license
curl -f "https://replicated.app/embedded/gitguardian/stable?airgap=true" -H "Authorization: $LICENSE_ID" -o gitguardian.tgz
tar -xvzf gitguardian.tgz
sudo ./gitguardian install --license license.yaml
```

:::info

**Airgap**

To use in airgap mode, use this instead:

```bash
LICENSE_ID=your_license
curl -f https://replicated.app/embedded/gitguardian/stable?airgap=true -H "Authorization: $LICENSE_ID" -o gitguardian.tgz
tar -xvzf gitguardian.tgz
sudo ./gitguardian install --license license.yaml --airgap-bundle gitguardian.airgap
```

**HTTP Proxy**

To use an HTTP proxy, use this instead:

```bash
LICENSE_ID=your_license
curl -f https://replicated.app/embedded/gitguardian/stable -H "Authorization: $LICENSE_ID" -o gitguardian.tgz
tar -xvzf gitguardian.tgz
sudo ./gitguardian install --license license.yaml \
  --http-proxy http://proxy.example.com:8080 \
  --https-proxy http://proxy.example.com:8080
```

For proxies with authentication, include credentials in the URL:

```bash
sudo ./gitguardian install --license license.yaml \
  --http-proxy http://username:password@proxy.example.com:8080 \
  --https-proxy http://username:password@proxy.example.com:8080
```

For detailed proxy configuration instructions, including troubleshooting authenticated proxies, see the [HTTP Proxy documentation](../management/infrastructure-management/proxy-server#embedded-cluster-specific).
:::

You will be prompted to enter the Admin console password. This password is used to manage the GitGuardian application and is different from the GitGuardian dashboard password that you will configure later.

If you are prompted to select from multiple network interfaces, choose the one connected to your private network.

This will install a single node-managed Kubernetes cluster with everything it
needs to run the GitGuardian application.

Once the installation is completed, instructions will appear on how to access the Admin Console.

![Installation's end screenshot](/img/self-hosting/installation/replicated_embedded_v2_end.png)

:::note
The deployment namespace for KOTS (and GitGuardian) cannot be changed at this time.
:::

### Application

With the embedded Kubernetes cluster now set up, let's move on to installing the GitGuardian application.

1. Access the **Admin Console** with the link provided and configure TLS.
   You have the option to upload your TLS certificates or use self-signed ones.

![Admin console TLS setup](/img/self-hosting/installation/replicated_tls_setup.png)

2. Enter the password provided at the end of the cluster installation.

![Admin console password](/img/self-hosting/installation/replicated_password_form.png)

3. You can see cluster status (with one node currently). Then click continue.

![Cluster management](/img/self-hosting/installation/replicated_embedded_v2_cluster_view.png)

4. Configure the application by completing all the required fields:

   - **Application Hostname**: Enter the Fully Qualified Domain Name (FQDN) for the GitGuardian application.
   - **Admin User Fields**: These fields are used to create the first GitGuardian user. You'll need to change the password upon the first login.

![Admin Console Application Configuration](/img/self-hosting/installation/replicated_configure_app.png)

Additional configuration options include:

- **Scaling**: Adjust the number of replicas for each application component. For more details, visit the [Scaling](../management/infrastructure-management/scaling) page.
- **Prometheus**: Activate an exporter for [Prometheus](../management/application-management/metrics).
- **TLS Certificate**: This is for the GitGuardian Application. You can either use auto-generated self-signed certificates or upload your own. For self-signed or private CA certificates, disable SSL verification for the GitHub webhook. Learn more on the [Configure TLS certificates](../security/tls-certificates) page.
- **Custom Certificate Authority**: Provide a [custom CA](../security/custom-ca) if necessary.
- **HTTP(s) Proxy**: Refer to the [proxy](../management/infrastructure-management/proxy-server) section if needed.
- **Databases/Datastores**: Choose between using embedded PostgreSQL/Redis or an external one. For more information, see [Configure your database](./databases/database-config).
- **Load balancer considerations**: To use the embedded cluster behind a load balancer, please read [Configure your instance to work behind a load balancer](../management/infrastructure-management/load-balancer#embedded-clusters).

5. Check if preflight checks pass.

:::caution Requirements
Preflight checks are critical for a successful installation. The following rules apply:

- :x: **Preflight Check Failures**: If preflight checks fail, the installation **must not continue** until the targeted environment meets all requirements. Please reach out to our **[support team](mailto:support@gitguardian.com)** if needed.
- :warning: **Preflight Check Warnings**: If preflight checks return warnings, the installation can proceed, but it is recommended that you address these warnings to comply with our **[recommendations](../system-requirements)**.

:::

![Admin console preflights](/img/self-hosting/installation/replicated_preflights.png)

6. Launch

The first installation of the GitGuardian application requires a few minutes to create all
database objects.
Once the process is completed, you will be able to log in to the dashboard using
the administrator user you defined.

### Save the Data Encryption Key

:::caution

GitGuardian encrypts all sensitive information in the database using an
encryption key (aka Django Secret Key). In case of disaster recovery, this key
will be needed to restore your data.

:::
You should save it and keep it in **a secure location**. Use the following command to display the key:

```shell
sudo ./gitguardian shell
kubectl get secrets gim-secrets -o jsonpath='{.data.DJANGO_SECRET_KEY}' | base64 -d
```

### Troubleshooting

If you encounter issues during the installation process, you can generate a support bundle for the GitGuardian team to diagnose and resolve problems more efficiently. See the [support bundle documentation](../troubleshoot/support#kots-based-installation) for detailed instructions.

## Next Steps

After successful installation:
- Access your GitGuardian instance using the hostname you configured
- Log in with the administrator credentials you set up (change the temporary password on first login)
- Configure [email settings](../management/application-management/email-configuration) for notifications
- Set up [SSO](../../platform/enterprise-administration/saml-sso-configuration) and [SCIM](../../platform/enterprise-administration/scim-configuration) integration (optional)
- [Integrate your first repositories](/platform/getting-started/integrate) to begin secret detection
