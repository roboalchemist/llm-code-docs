# Deploy Mattermost on Kubernetes

.. If used with include::, note the paths for images

<div class="mm-badge mm-badge--note">

[\|plans-img-yellow\|](##SUBST##|plans-img-yellow|) Available on [Entry,
Enterprise, and Enterprise Advanced
plans](https://mattermost.com/pricing/) (not available on Professional)

</div>

Mattermost server can be deployed on various Kubernetes platforms,
providing a scalable and robust infrastructure for your team
communication needs. This guide covers deployment options for major
cloud providers and general Kubernetes installations.

:::: tip
::: title
Tip
:::

To learn how to safely upgrade your deployment in Kubernetes for High
Availability with Active/Active support, see the
`Upgrading Mattermost in Kubernetes and High Availability Environments </administration-guide/upgrade/upgrade-mattermost-kubernetes-ha>`{.interpreted-text
role="doc"} documenation.
::::

## Platform

Choose your preferred platform below for specific deployment
instructions:

:::::::::: {#install-mattermost-operator}
::::::::: {.tab parse-titles=""}
Mattermost Operator

You can use the Mattermost Kubernetes Operator to deploy Mattermost on
Kubernetes using S3-compatible storage and a managed database service.
While the operator supports a range of configurations, we strongly
recommend using a cloud-native approach for production environments.

### Prerequisites

Before you begin, ensure you have the following:

- A functioning Kubernetes cluster (see the [Kubernetes setup
  guide](https://kubernetes.io/docs/setup/)). Your cluster should be
  running a [supported Kubernetes
  version](https://kubernetes.io/releases/).
- The [kubectl]{.title-ref} command-line tool installed on your local
  machine (see the [kubectl installation
  guide](https://kubernetes.io/docs/reference/kubectl/)).
- A fundamental understanding of Kubernetes concepts, such as
  deployments, pods, and applying manifests.
- Sufficient Kubernetes resources allocated based on your expected user
  load. Consult the
  `scaling for Enterprise <administration-guide/scale/scaling-for-enterprise:available reference architectures>`{.interpreted-text
  role="ref"} documentation for resource requirements at different
  scales.

### Installation steps

The installation process involves setting up necessary operators and
then deploying Mattermost itself.

#### Step 1: Install the NGINX Ingress Controller

Follow the instructions in the [Kubernetes deployment
documentation](https://kubernetes.github.io/ingress-nginx/deploy/) to
install the NGINX ingress controller on your Kubernetes cluster.
Mattermost recommends installing the Nginx Operator via helm, regardless
of platform you are installing to.

#### Step 2: Install the Mattermost Operator

The Mattermost Kubernetes Operator can be installed using Helm.

1. Install Helm (version 3.13.0 or later). See the [Helm quickstart
    documentation](https://helm.sh/docs/using_helm/) for installation
    instructions.
2. Add the Mattermost Helm repository:

> ``` sh
> helm repo add mattermost https://helm.mattermost.com
> ```

1. Create a file named `config.yaml` and populate it with the contents
    of the [Mattermost operator values
    file](https://github.com/mattermost/mattermost-helm/blob/master/charts/mattermost-operator/values.yaml).
    This file allows for customization of the operator.
2. Create a namespace for the Mattermost Operator:

> ``` sh
> kubectl create ns mattermost-operator
> ```

1. Install the Mattermost Operator. If you don\'t specify a version,
    the latest version of the Mattermost Operator will be installed. We
    recommend using the latest version of the Mattermost Operator.

> ``` sh
> helm install <your-release-name> mattermost/mattermost-operator -n <namespace_name>
> ```
>
> For example:
>
> ``` sh
> helm install mattermost-operator mattermost/mattermost-operator -n mattermost-operator
> ```
>
> To use your custom `config.yaml` file:
>
> ``` sh
> helm install mattermost-operator mattermost/mattermost-operator -n mattermost-operator -f config.yaml
> ```

#### Step 3: Deploy Mattermost

:::: note
::: title
Note
:::

- A Mattermost Enterprise license is required for multi-server
  deployments.
- For single-server deployments without an Enterprise license, add
  `Replicas: 1` to the `spec` section in step 2 below. See the
  `high availability documentation </administration-guide/scale/high-availability-cluster-based-deployment>`{.interpreted-text
  role="doc"} for more on highly-available deployments.
::::

1. **(Mattermost Enterprise only)** Create a Mattermost license secret.
    Create a file named `mattermost-license-secret.yaml` with the
    following content, replacing `[LICENSE_FILE_CONTENTS]` with your
    actual license:

> ``` yaml
> apiVersion: v1
> kind: Secret
> metadata:
>   name: my-mattermost-license
> type: Opaque
> stringData:
>   license: <LICENSE_FILE_CONTENTS>
> ```

1. Create a Mattermost installation manifest file named
    `mattermost-installation.yaml`. File names in this guide are
    suggestions; you can use different names. Use the following
    template, adjusting the values as needed:

> ``` yaml
> apiVersion: installation.mattermost.com/v1beta1
> kind: Mattermost
> metadata:
>   name: <INSTALLATION_NAME_HERE>        # Example: mm-example-full
> spec:
>   size: <SIZE_VALUE_HERE>               # Example: 5000users
>   ingress:
>     enabled: true
>     host: <FULL_DOMAIN_NAME_HERE>       # Example: example.mattermost-example.com
>     annotations:
>       kubernetes.io/ingress.class: nginx
> version: <VERSION_HERE>               # Example: 9.3.0
> licenseSecret: ""                     # If you created a license secret, put the name here
> ```
>
> Key fields in the manifest include:
>
> - `metadata.name`: The name of your Mattermost deployment in
>   Kubernetes.
> - `spec.size`: The size of your installation (e.g., \"100users\",
>   \"1000users\", etc.).
> - `spec.ingress.host`: The DNS name for your Mattermost installation.
> - `spec.version`: The Mattermost version. See the
>   `server version archive </product-overview/version-archive>`{.interpreted-text
>   role="doc"} for available versions. You should use a
>   `supported version </product-overview/release-policy>`{.interpreted-text
>   role="doc"} of Mattermost in conjunction with the latest version of
>   the Mattermost Operator.
> - `spec.licenseSecret`: The name of the Kubernetes secret containing
>   your license (required for Enterprise).
>
> For a full list of configurable fields, see the [example
> manifest](https://github.com/mattermost/mattermost-operator/blob/master/docs/examples/mattermost_full.yaml)
> and the [Custom Resource
> Definition](https://github.com/mattermost/mattermost-operator/blob/master/config/crd/bases/installation.mattermost.com_mattermosts.yaml).

1. Create a file named `mattermost-database-secret.yaml` for database
    credentials. This secret must be in the same namespace as the
    Mattermost installation.

> ``` yaml
> apiVersion: v1
> data:
>   DB_CONNECTION_CHECK_URL: <DB_CONNECTION_CHECK_URL>
>   DB_CONNECTION_STRING: <DB_CONNECTION_STRING>
>   MM_SQLSETTINGS_DATASOURCEREPLICAS: <MM_SQLSETTINGS_DATASOURCEREPLICAS>
> kind: Secret
> metadata:
>   name: my-postgres-connection
> type: Opaque
> ```
>
> Example for AWS Aurora with PostgreSQL:
>
> ``` yaml
> apiVersion: v1
> data:
>   DB_CONNECTION_CHECK_URL: cG9zdGdyZXM6Ly91c2VyOnN1cGVyX3NlY3JldF9wYXNzd29yZEBteS1kYXRhYmFzZS5jbHVzdGVyLWFiY2QudXMtZWFzdC0xLnJkcy5hbWF6b25hd3MuY29tOjU0MzIvbWF0dGVybW9zdD9jb25uZWN0X3RpbWVvdXQ9MTAK
>   DB_CONNECTION_STRING: cG9zdGdyZXM6Ly91c2VyOnN1cGVyX3NlY3JldF9wYXNzd29yZEBteS1kYXRhYmFzZS5jbHVzdGVyLWFiY2QudXMtZWFzdC0xLnJkcy5hbWF6b25hd3MuY29tOjU0MzIvbWF0dGVybW9zdD9jb25uZWN0X3RpbWVvdXQ9MTAK
>   MM_SQLSETTINGS_DATASOURCEREPLICAS: cG9zdGdyZXM6Ly91c2VyOnN1cGVyX3NlY3JldF9wYXNzd29yZEBteS1kYXRhYmFzZS5jbHVzdGVyLXJvLWFiY2QudXMtZWFzdC0xLnJkcy5hbWF6b25hd3MuY29tOjU0MzIvbWF0dGVybW9zdD9jb25uZWN0X3RpbWVvdXQ9MTAK
> kind: Secret
> metadata:
>   name: my-postgres-connection
> type: Opaque
> ```

#### Step 4: Create the Filestore Secret

Create a file named `mattermost-filestore-secret.yaml` to store the
credentials for your object storage service (e.g., AWS S3 or any
S3-compatible service). This secret must be created in the same
namespace where you intend to install Mattermost. The file should
contain the following YAML structure:

``` yaml
apiVersion: v1
kind: Secret
metadata:
  name: <secret-name>  # Choose a descriptive name (e.g., my-s3-credentials)
type: Opaque
data:
  accesskey: <base64-encoded-access-key>
  secretkey: <base64-encoded-secret-key>
```

  Key             Description                                           Required
  --------------- ----------------------------------------------------- ----------
  accesskey       Base64-encoded access key for your storage service.   Yes
  secretkey       Base64-encoded secret key for your storage service.   Yes
  metadata.name   The name of the Kubernetes secret.                    Yes

:::: important
::: title
Important
:::

The `accesskey` and `secretkey` values must be **base64-encoded**. Do
not enter the raw keys directly. Use a command-line tool or online
encoder to generate the base64 strings.

**Example (AWS S3):**

``` yaml
apiVersion: v1
kind: Secret
metadata:
  name: my-s3-credentials
type: Opaque
data:
  accesskey: QUNDRVNTX0tFWQo=  # Example: Replace with your actual encoded key
  secretkey: U1VQRVJfU0VDUkVUX0tFWQo=  # Example: Replace with your actual encoded key
```

::::

#### Step 5: Configure the Mattermost Installation Manifest

1. Modify the `mattermost-installation.yaml` file (created in step 2)
    to connect Mattermost to your external database and object storage.
    Refer to the supported fields for guidance on where to add these
    configurations within the YAML structure.
2. Connect to the database:

> a.  Add the following to the `spec` section of your manifest:
>
> > ``` yaml
> > spec:
> >   database:
> >     external:
> >       secret: <database-secret-name>  # The name of the database secret (e.g., my-postgres-connection)
> > ```

1. Connect to Object Storage:

> a.  Add the following to the `spec` section of your manifest:
>
> > ``` yaml
> > spec:
> >   fileStore:
> >     external:
> >       url: <storage-service-url>  # The URL of your storage service (e.g., s3.amazonaws.com)
> >       bucket: <bucket-name>      # The name of your storage bucket
> >       secret: <filestore-secret-name> # The name of the filestore secret (e.g., my-s3-credentials)
> > ```

1. If you are using Amazon S3, it\'s recommended to enable server-side
    encryption (SSE) and SSL. Add the following environment variables to
    the `mattermostEnv` section:

> ``` yaml
> spec:
>   mattermostEnv:
>     MM_FILESETTINGS_AMAZONS3SSL: true
>     MM_FILESETTINGS_AMAZONS3SSE: true
> ```

### Review Mattermost Resource Status

After a Mattermost installation has been created with the Operator, you
can review its status with the following:

``` sh
kubectl -n [namespace] get mattermost
```

The `kubectl describe` command can be used to obtain more information
about the Mattermost server pods:

``` sh
kubectl -n [namespace] describe pod
```

**Follow logs**

The following command can be used to follow logs on any kubernetes pod:

``` sh
kubectl -n [namespace] logs -f [pod name]
```

If the `-n [namespace]` is omitted, then the default namespace of the
current context is used. We recommend specifying the namespace based on
your deployment.

This command can be used to review the Mattermost Operator or Mattermost
server logs as needed.

:::: note
::: title
Note
:::

- If you\'re new to Kubernetes or prefer a managed solution, consider
  using a service like [Amazon EKS](https://aws.amazon.com/eks/), [Azure
  Kubernetes
  Service](https://azure.microsoft.com/en-ca/products/kubernetes-service/),
  [Google Kubernetes
  Engine](https://cloud.google.com/kubernetes-engine/), or [DigitalOcean
  Kubernetes](https://www.digitalocean.com/products/kubernetes/). While
  this guidance focuses on using external, managed services for your
  database and file storage, the Mattermost Operator *does* offer the
  flexibility to use other solutions. For example, you could choose to
  deploy a PostgreSQL database within your Kubernetes cluster using the
  CloudNative PG operator (or externally however you wish), or use any
  self-hosted S3-compatible storage service.
- While using managed cloud services is generally simpler to maintain
  and our recommended approach for production deployments, using
  self-managed S3-compatible storage services and CloudNative PG for
  PostgreSQL are also valid options if you have the expertise to manage
  them.
- If you choose to use self-managed components, you\'ll need to adapt
  the instructions accordingly, pointing to your internal services
  instead.
- To customize your production deployment, refer to the
  `configuration settings documentation </administration-guide/configure/configuration-settings>`{.interpreted-text
  role="doc"}.
- If you encounter issues during deployment, consult the
  `deployment troubleshooting guide </deployment-guide/deployment-troubleshooting>`{.interpreted-text
  role="doc"}.
::::

### Frequently Asked Questions

#### What is the Operator\'s version compatibility with Mattermost Server?

While generally speaking, the Operator should be compatible with most,
or all versions of Mattermost Server, we recommend always using the
latest version of the Operator in conjunction with a
`supported version </product-overview/release-policy>`{.interpreted-text
role="doc"} of Mattermost Server.
:::::::::
::::::::::

::::: {.tab parse-titles=""}
Azure

You can use a supported [Azure Marketplace Container
Offer](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/mattermost.mattermost-operator)
to install Mattermost on your existing Azure infrastructure.

### Before you begin

Before deploying, make sure you have the following:

- **An AKS cluster**: with the [Application Gateway Ingress Controller
  (AGIC)
  add-on](https://learn.microsoft.com/en-us/azure/application-gateway/tutorial-ingress-controller-add-on-new)
  enabled or another Ingress controller deployed.
- **PostgreSQL v13.0+ database**: [Azure Database for PostgreSQL -
  Flexible Server with Private
  Access](https://learn.microsoft.com/en-us/azure/postgresql/) is
  recommended. Deploy one by following [this Microsoft quick start
  guide](https://learn.microsoft.com/en-us/azure/postgresql/flexible-server/quickstart-create-server-portal).
- **Private Network Connectivity**: Verify that there is network
  connectivity between your AKS cluster and the PostgreSQL database.
- **Valid DNS name and TLS certificate**: You must have access to a DNS
  zone and provide a valid TLS key and certificate for the Ingress
  Controller.
- **Node Capacity**: At least 2 AKS nodes for high availability when
  deploying for 100 users or more.
- **License Key**: Trial or Enterprise license to test high availability
  and other Enterprise features.

### Installation steps

The installation process includes deploying Mattermost and updating the
server.

#### Step 1: Deploy Mattermost

1. Deploy Mattermost from the [Azure Marketplace Container
    Offer](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/mattermost.mattermost-operator)
    and select **Get it now**.

> Alternatively, you can go to the `Extensions + Applications` section
> of your AKS cluster and install the Mattermost offering from there.
> Visit the [Microsoft cluster extensions
> documentation](https://learn.microsoft.com/en-gb/azure/aks/cluster-extensions?tabs=azure-cli)
> to learn more.

1. Choose the **Resource Group** and the **Region** of your installed
    AKS and PostgreSQL database.

> ![An example of the Azure AKS Project details screen.](/_static/images/azure/basics.png)

1. Choose your AKS cluster.

> ![An example of the Azure AKS cluster setup screen.](/_static/images/azure/aks-cluster.png)

1. Fill in the details for your PostgreSQL database. Ensure the user
    specified has full access.

> ![An example of the Azure AKS Database setup screen.](/_static/images/azure/postgreSQL.png)

1. Specify Deployment Details including Deployment Name and Deployment
    Size. You will need to configure file storage for your Mattermost
    instance. We recommend using an S3-compatible storage service or an
    NFS-compatible server.

> ![An example of the Azure AKS Deployment Details setup screen.](/_static/images/azure/deployment-details.png)

1. Configure Mattermost installation hostname and Ingress details. The
    AGIC add-on is used in the following example to show the ingress
    annotations required.

> You can use any pre-installed Ingress Controller in your cluster as
> long as it supports Kubernetes Ingress and TLS termination.
>
> ``` yaml
> kubernetes.io/ingress.class: azure/application-gateway
> appgw.ingress.kubernetes.io/ssl-redirect: "true"
> ```

1. Additionally, we recommend considering:

> a.  Enforcing a minimum TLS version (e.g., TLS 1.2).
> b.  Deploying a Web Application Firewall (WAF) for additional
> protection, if supported by your ingress controller.
> c.  Limiting access using Kubernetes Network Policies.
>
> ![An example of the Azure AKS Networking Details setup screen.](/_static/images/azure/networking-details.png)

1. Ensure that everything is running. You should be able to check the
    installed plugin from the **AKS Extensions + Applications** page
    under the **Settings** menu.

> When the deployment is complete, obtain the hostname or IP address of
> your Mattermost deployment using the following command:
>
> ``` sh
> kubectl -n mattermost-operator get ingress
> ```

1. Use your IP address from the `ADDRESS` column, and create a DNS
    record in your domain registration service.
2. Access your working Mattermost installation at the URL you've
    determined in your DNS record.

Learn more about administrating your Mattermost server by visiting the
`Administration Guide </administration-guide/administration-guide-index>`{.interpreted-text
role="doc"}.

#### Step 2: Upgrade Mattermost via your AKS cluster

1. Visit the `Extensions + Applications` section of your AKS cluster
    where your Mattermost installation is deployed.
2. You can enable minor version auto upgrades since these are not
    updating Mattermost version
3. Expand the `Configuration Settings` table and add the below
    configuration and the version you want to install as a value.

> ```text
> global.azure.mattermost.version
>
> .. image:: /_static/images/global-azure-mattermost-version.png
> :alt: An example of using custom Mattermost version.
> ```

1. Select **Save** and wait for the upgrade.

### Looking for a sovereign deployment on Azure Local?

For organizations requiring on-premises deployments with data
sovereignty, **Azure Local** (formerly Azure Stack HCI) provides a
hybrid cloud platform that enables you to run Mattermost on-premises
while maintaining integration with Microsoft Teams and M365.

We recommend engaging **Mattermost Professional Services** for Azure
Local deployments to ensure optimal configuration and compliance with
your security requirements. [Talk to an
Expert](https://mattermost.com/contact-sales/) to discuss your Azure
Local deployment needs.

:::: important
::: title
Important
:::

You are responsible for Azure costs associated with any infrastructure
you spin up to host a Mattermost server, and Azure credits cannot be
applied towards the purchase of a Mattermost license.
::::
:::::

::::::: {.tab parse-titles=""}
Oracle

You can use the supported [Oracle Cloud Marketplace
listing](https://cloudmarketplace.oracle.com/marketplace/en_US/listing/188386963)
to install Mattermost Enterprise Edition on Oracle Cloud Infrastructure
(OCI) using Oracle Kubernetes Engine (OKE).

### Before you begin

Before deploying, make sure you have the following:

- **Oracle Cloud Account** with appropriate permissions
- **Permissions** to create/manage OKE, Compute, Networking, Database,
  Resource Manager, and Secrets
- **Compartment** for deployment
- **Domain Name and TLS Certificate** for secure access
- **Mattermost License Key** (Trial or Enterprise)
- **Node Capacity**: At least 2 OKE nodes for high availability when
  deploying for 100 users or more

### Installation steps

The installation process includes deploying Mattermost and configuring
the necessary components.

#### Step 1: Start from Oracle Cloud Marketplace

Go to the Mattermost listing and select **Launch Stack**.

![Oracle Cloud Marketplace listing for Mattermost](/images/oracle/marketplace-listing.png)

#### Step 2: Stack Information

On the **Create stack** page, review the information, and then set the
name, compartment, and Terraform version.

![Stack information page](/images/oracle/stack-info.png)

#### Step 3: Configure Variables

Set all the details for your Mattermost deployment. Each section is
important for a successful and secure installation.

##### OKE Cluster Configuration

- **Create new OKE Cluster:**
  - Check this if you want to create a new Kubernetes cluster.
  - If you already have a cluster, you can uncheck and select your
    existing one.
- **Kubernetes Version:**
  - Choose the latest stable version unless you have a specific
    requirement.
- **Node Pool Shape (Flex/Fixed):**
  - Select a shape that fits your workload. For production, use at least
    2 OCPUs and 16GB RAM per node.
- **Number of Nodes:**
  - Minimum 2 for high availability. For testing, 1 is enough. For
    production environments, always use at least 2 nodes and enable high
    availability.
- **Operating System:**
  - Oracle Linux 8 is recommended for best compatibility.

##### OKE Network Configuration

- **Worker Node Visibility:**
  - Private is more secure for production. Public is easier for testing.
    For production environments, use private nodes and restrict access
    to the API endpoint.
- **API Endpoint Visibility:**
  - Public allows you to manage the cluster from anywhere. Private is
    more secure but requires VPN or bastion.
- **Create new Virtual Cloud Network (VCN):**
  - Check this to create a new network, or uncheck to use an existing
    one.
- **VCN CIDR Block:**
  - Set a unique network range (e.g., `10.20.0.0/16`). Avoid overlap
    with other networks.

##### OKE Worker Nodes

- **Enable Cluster Autoscaler:**
  - Allows the cluster to automatically add or remove nodes based on
    usage.
- **Initial/Min Number of Worker Nodes:**
  - Set the minimum number of nodes. For high availability, use at
    least 2. Autoscaling helps manage costs and performance
    automatically.
- **Node Shape:**
  - Choose a shape (e.g., `VM.Standard.E4.Flex`) and set OCPUs and
    memory.
- **Auto Generate SSH Key:**
  - Enable this if you do not have your own SSH key for node access.
- **Image OS and Version:**
  - Oracle Linux 8 is recommended.

##### PostgreSQL Configuration

- **Admin Username:**
  - The main user for your PostgreSQL database (e.g., `admin1`).
- **Password Type:**
  - `PLAIN_TEXT` for testing, `SECRET` for production (uses Oracle
    Vault). Always use Oracle Vault for production passwords.
- **Password/Secret Name:**
  - Enter a strong password or the name of a secret in Oracle Vault.
- **Database Password:**
  - Required if not using a secret.

##### General Configuration

- **Cluster Name Prefix:**
  - Used to identify all resources (e.g., `mm-oke`).
- **Show Advanced Options:**
  - Enable for more control (encryption keys, SSH keys, etc.). Use
    advanced options if you need custom encryption or want to manage
    your own SSH keys.
- **PostgreSQL Deployment Strategy:**
  - Use \"Database For PostgreSQL\" for managed service.
- **Object Storage for File Storage:**
  - Enable to use OCI Object Storage for Mattermost files.
- **Mattermost Version:**
  - Use the latest stable version.
- **Namespace:**
  - Default is `mattermost`.
- **License Key:**
  - Upload or paste your Mattermost license.
- **Helm Repository:**
  - Default is `https://helm.mattermost.com`.

#### Step 4: Review and Apply

Check all your settings and select **Create** to start the deployment.
Monitor the Resource Manager job and logs.

![Resource Manager job monitor](/images/oracle/job-monitor.png)

#### Step 5: After Deployment

When the job is finished, your OKE cluster, PostgreSQL database, and
Mattermost will be ready. To find the Mattermost web address, run:

``` sh
kubectl -n mattermost-operator get ingress
```

Copy the address and create a DNS record for your domain. Open your
browser and go to your Mattermost URL.

#### Step 6: Upgrade Mattermost

To upgrade your Mattermost installation:

1. Access your OKE cluster through the Oracle Cloud Console
2. Navigate to the Mattermost operator deployment
3. Update the Mattermost version in the configuration
4. Apply the changes and wait for the upgrade to complete

:::: tip
::: title
Tip
:::

**Tips for Success**

- Make sure you have all the permissions you need before you start.
- Use Oracle Vault to store passwords and sensitive data.
- Use private nodes and secure your network for production.
- Always monitor logs from the Resource Manager and pods using
  `kubectl logs` for more specific error messages.
- For more details, see the official [OCI Database with PostgreSQL
  documentation](https://www.oracle.com/cloud/postgresql/) and [OKE
  documentation](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengoverview.htm).
::::

### Common Errors and How to Avoid Them

- **Error: Kubernetes API not reachable**
  - *Cause:* API endpoint is private and you\'re not connected to the
    VCN via VPN or Bastion.
  - *Solution:* Ensure you have access to the network or make the
    endpoint public for testing.
- **Error: Stack creation fails with missing permissions**
  - *Cause:* IAM policies are not set properly for the user or group.
  - *Solution:* Ensure you have permissions for Resource Manager, OKE,
    Networking, and Secrets.
- **Error: No ingress returned by kubectl**
  - *Cause:* Mattermost Ingress might not be ready or was misconfigured.
  - *Solution:* Check with `kubectl describe ingress` and validate DNS,
    TLS, and Helm values.
- **Error: PostgreSQL password rejected**
  - *Cause:* Password not set or mismatched with Oracle Vault.
  - *Solution:* Re-check the password value or Vault secret used during
    setup.

:::: important
::: title
Important
:::

You are responsible for Oracle Cloud Infrastructure costs for the
resources you create. Oracle Cloud credits cannot be used to buy a
Mattermost license.
::::

Learn more about managing your Mattermost server by visiting the
`Administration Guide </administration-guide/administration-guide-index>`{.interpreted-text
role="doc"}.
:::::::

## Frequently Asked Questions

### Why are my pods failing with a `CrashLoopBackOff` error after adding a custom CA certificate to my Docker image?

You may see a `CrashLoopBackOff` error after adding a custom CA
certificate to your Docker image\'s `/etc/ssl/certs` directory and
deploying it to your Kubernetes environment via the Mattermost
Enterprise Edition Helm Chart. This issue typically arises because the
custom CA certificate is not being recognized by the system\'s
certificate trust store, leading to TLS handshake failures when the
application attempts to connect to services that require the custom CA.

While core functionality may remain operational, you may notice the
following symptoms:

- Pods stuck in a crashloop with the error message: backoff - restarting
  failed container in pod.
- Debugging commands like `kubectl describe` and `kubectl logs` provide
  little to no valuable information.
- Integrations may be blocked.

### Can I resolve this issue without rebuilding the Docker image?

Yes. We recommend using Kubernetes-native solutions to manage custom CA
certificates to simplify deployment processes and minimize disruptions
caused by image rebuilds. You can inject the certificate directly into
the pod using Kubernetes resources instead of modifying the Docker image
to manage custom CA certificates dynamically without needing to rebuild
and redeploy your Docker image every time the certificate changes.

Use a Kubernetes secret to store your custom CA certificate and then
mount it into the pod:

1. Create a Kubernetes secret with your custom CA certificate.
2. Mount the certificate into the pod using the Helm chart's
    configuration options. This method simplifies management and avoids
    the need to rebuild your Docker image for future certificate
    updates.

Alternatively, to dynamically inject certificates without modifying the
Docker image, use an `initContainer` to copy the certificate into the
pod\'s filesystem and update the certificate trust store before the main
container starts.

### How to troubleshoot the root cause of the `CrashLoopBackOff` error?

Use `kubectl describe pods` to check detailed event logs.

Consider logging tools like Grafana to aggregate and analyze logs for
additional insights.

### Where is data stored in a self-hosted Kubernetes deployment?

Where data is stored depends on the backend database (such as RDS, Azure
Postgres, self-hosted PostgreSQL), and the backend filestore (such as
AWS S3, other S3-compatible services, or a mounted volume) configured
during deployment.

For volume mounts, we recommend using an NFS volume to provide
filestores as a \"local\" directory to the Mattermost server.

Not all types of [Kubernetes persistent
volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#types-of-persistent-volumes)
have been tested with Mattermost, and some may have limitations or
specific configurations that may require additional setup to ensure
proper permissions and access. We recommend system admins review
documentation for their preferred persistent volume types and test to
ensure compatibility with Mattermost.
