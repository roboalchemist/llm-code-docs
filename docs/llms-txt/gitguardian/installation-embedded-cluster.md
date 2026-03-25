# Source: https://docs.gitguardian.com/self-hosting/installation/installation-embedded-cluster.md

# Install on an Embedded cluster (kURL)

> Install GitGuardian self-hosted using the KOTS embedded cluster method for an all-in-one single-node deployment.

## Introduction

**â ï¸ Use the new [Embedded Installation](./installation-embedded-cluster-v2) unless instructed otherwise.**

GitGuardian can be installed with an embedded Kubernetes distribution packaged with it and supports deployment on bare metal, private, or public clouds.

This installation uses [KOTS](https://kots.io), a kubectl plugin and KOTS Admin Console to help manage Kubernetes Off-The-Shelf software.

:::caution Requirements
Before starting the installation, ensure to review the **[system](../system-requirements)** and **[network](../network-requirements)** requirements, and **[download your license](../license-management)**.
:::

## Installation

### Embedded cluster

To start the installation, run the following command on your host as root. This command
will run for 10-20 minutes, putting in a screen or a `tmux` session can prevent
an interruption due to a loss of connection.

```bash
sudo -i
curl -sSL https://kurl.sh/gitguardian | bash
```

If prompted to select from multiple network interfaces, opt for the one connected to your private network.

This will install a single node-managed Kubernetes cluster with everything it needs to run the GitGuardian application.

Once the installation is completed, instructions will appear on how to access the KOTS Admin Console.
Use provided **IP address** on port **8800**.

![Installation's end screenshot](/img/self-hosting/installation/replicated_installation_end.png)

Save this information, especially passwords, they will be useful later.

### Application

With the embedded Kubernetes cluster now set up, let's move on to installing the GitGuardian application.

1. Access the **KOTS Admin Console** at `https://<ip_address>:8800` and configure TLS.
   You have the option to upload your TLS certificates or use self-signed ones.

![Admin console TLS setup](/img/self-hosting/installation/replicated_tls_setup.png)

2. Enter the password provided at the end of the cluster installation.

![Admin console password](/img/self-hosting/installation/replicated_password_form.png)

3. Upload the license downloaded on the portal. Refer to the [download your license](../license-management) page.

![License upload](/img/self-hosting/installation/replicated_license_upload.png)

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
kubectl get secrets gim-secrets -o jsonpath='{.data.DJANGO_SECRET_KEY}' | base64 -d
```

If needed, specify the Kubernetes namespace with `--namespace` (default namespace is used if not specified).

### Network and storage configuration

#### Configuring proxy settings

If a proxy is required for outgoing access to the internet, please create a
`patch.yaml`:

```yaml
apiVersion: 'cluster.kurl.sh/v1beta1'
kind: 'Installer'
metadata:
  name: 'patch'
spec:
  kurl:
    proxyAddress: http://<IP>:<PORT>
    noProxy: false
```

And run the installer with `-installer-spec-file=patch.yaml` as root:

```bash
sudo -i
curl -sSL https://kurl.sh/gitguardian | bash -s installer-spec-file=patch.yaml
```

#### Managing disk space

The kURL Embedded cluster will create a [MinIO](https://min.io/) Persistent
Volume mounted on `/mnt/data`. You can use a specific disk for this volume and,
in this case, it must have at least 200GB of free space.

The kURL installer will look for the existence of the `/var` directory as well
as all the core directories mentioned in its documentation.

Otherwise, the root storage **should not be partitioned**. You can read more
about the disk space requirements in the
[kURL documentation](https://kurl.sh/docs/install-with-kurl/system-requirements#disk-space-requirements).

Note that if your disk is **not** a SCSI device, you will need to patch the
install script following
[these guidelines](https://kurl.sh/docs/install-with-kurl/#modifying-an-install-using-a-yaml-patch-file-at-runtime):

1. Create a YAML file and add the following parameters (this is an example for a `nvme` device):

```yaml
kind: Installer
metadata:
  name: patch
spec:
  rook:
    blockDeviceFilter: nvme1n[0-1]
```

2. Run the install script with that patch as root:

```bash
sudo -i
curl -sSL https://kurl.sh/gitguardian | bash -s installer-spec-file=[path of the above YAML patch file]
```

### Troubleshooting

If you encounter issues during the installation process, you can generate a support bundle for the GitGuardian team to diagnose and resolve problems more efficiently. See the [support bundle documentation](../troubleshoot/support#kots-based-installation) for detailed instructions.
