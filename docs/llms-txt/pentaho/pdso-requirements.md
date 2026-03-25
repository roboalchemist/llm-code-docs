# Source: https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-install-landing-page/pdso-requirements.md

# Requirements

Data Optimizer requires specific external components and applications to operate optimally. This section provides a list of those components and applications along with details of their use and the versions Data Optimizer supports.

## Environment considerations

To ensure proper software development and deployment practices, it is a best practice to have two separate environments:

* Development or Staging
* Production

## System requirements

The software, hardware, and access requirements you should have before you install Data Optimizer are outlined below.

### Checklist for infrastructure requests

Perform the following tasks as needed to prepare your environment for Data Storage Optimizer:

* Request a Virtual Machine (VM) on Azure, AWS, or on-premises.
* Request IDs with remote access permissions to the VM on your cloud or on-premises.
* Request necessary access to systems, applications, and data sources.
* Request VDI or VPN access for Data Storage Optimizer data engineers to enable remote access to the VM.
* Request a database user account (service account) or logins for connecting to the data sources.
* Make sure the database user account has read-only permissions for the database objects.
* Make sure that your system owner or Database Administrator (DBA) has copied or extracted any required data or files.
* Obtain an SSL certificate from a certificate authority. If required by your organization's security policy, raise an infrastructure support request for an SSL certificate. The certificate authority will give you a key file and a certificate file.

### Hardware requirements

Your server and network must meet the following requirements:

<table><thead><tr><th width="178">Category</th><th>Description</th></tr></thead><tbody><tr><td>CPU</td><td><p>16 cores (minimum)</p><p>32 cores (recommended)</p></td></tr><tr><td>RAM</td><td><p>64 GB (minimum)</p><p>128 GB (recommended)</p></td></tr><tr><td>Disk storage</td><td>1 TB (minimum)</td></tr><tr><td>Network</td><td>1 Gbps</td></tr></tbody></table>

If the server is running on AWS, review the following requirements.

#### AWS EC2 details

An AWS EC2 virtual machine has the following requirements:

<table><thead><tr><th width="122">Category</th><th>Minimum Requirements</th><th>Preferred Requirements</th></tr></thead><tbody><tr><td>Size</td><td>m5.4xlarge</td><td>m2.8xlarge</td></tr><tr><td>vCPU</td><td>16 cores</td><td>32 cores</td></tr><tr><td>Memory</td><td>64 GB</td><td>128 GB</td></tr></tbody></table>

{% hint style="info" %}
You can attach Amazon Elastic Block Store (EBS) to these VMs.
{% endhint %}

#### Azure VM details

An Azure VM has the following requirements:

<table><thead><tr><th width="146">Category</th><th>Minimum Requirements</th><th>Preferred Requirements</th></tr></thead><tbody><tr><td>Size</td><td>B_16s_v2</td><td>B_32s_v2</td></tr><tr><td>vCPU</td><td>16 cores</td><td>32 cores</td></tr><tr><td>Memory</td><td>64GB</td><td>128 GB</td></tr></tbody></table>

{% hint style="info" %}
You can attach standard SSDs, standard HDDs, and premium SSDs disk storage to these VMs.
{% endhint %}

#### Server storage requirements

The server file systems and storage must meet the following requirements:

* At least 10 GB of storage should be allocated for the root file system.
* Ample storage should be mounted in the designated Docker storage area (typically the default on Linux servers).

{% hint style="info" %}
Any POSIX-compliant file system can be used, but XFS, the standard file system in RHEL, is well-tested.
{% endhint %}

## Operating system requirements

You must deploy Data Optimizer to a dedicated server, which can be either a physical server or a virtual machine. The hosting environment can be on-premises or on the cloud using platforms such as Azure or AWS.

For optimal compatibility and performance, the server must run a modern Linux operating system based on 64-bit (x86\_64/amd64) architecture.

{% hint style="info" %}
For an updated list of compatible Linux distributions, visit the [Support Portal](https://support.pentaho.com/hc/en-us).
{% endhint %}

### Linux kernel version

Version 4.0 or higher of the Linux kernel is required. For RHEL, use version 3.10.0-514 of the kernel or a higher version.

**Note:** The `overlay` and `overlay2` drivers are supported on XFS backing file systems with the **d\_type=true** option enabled.

* To ensure that the **ftype** option is set to 1, use the command **xfs\_info** and verify the output. To format an XFS file system correctly, use the flag **-n ftype=1**.
* If the dedicated server is restarted, make sure to enable auto start-up for Docker by executing the following commands:
  * `sudo systemctl enable docker.service`
  * `sudo systemctl enable containerd.service`

## Network security and firewall requirements

The network security and firewall must meet the following requirements:

* Ports `80` and `443` should be open to inbound traffic.
* The application server must have network connectivity to the database server and port.

{% hint style="info" %}
The default installation includes a signed certificate for HTTPS enablement on port `443`. However, if desired, you can obtain an SSL certificate from a certificate authority.
{% endhint %}

## User account

The server user account used for the installation must either be the root user or have appropriate permissions to run Docker. To set up Docker permissions for non-root users, see the official Docker documentation at <https://docs.docker.com/engine/install/linux-postinstall/>.

## Software requirements

Before you install Data Optimizer, make sure that Docker is installed on your server and configured to automatically start on boot. See the [official Docker documentation](https://docs.docker.com/) for instructions on installing Docker.

<table><thead><tr><th width="175">Name</th><th>Requirements</th></tr></thead><tbody><tr><td>Docker</td><td>Version 20.10+</td></tr><tr><td>Docker Compose</td><td>Use the latest version of Docker Compose supported by your OS platform.</td></tr></tbody></table>

### Additional software

For seamless SSH connectivity and secure file transfer between your machine and the server, it is a best practice that you install the following software on your machine:

* An SSH client such as PuTTY (recommended).
* WinSCP for a graphical user interface to securely transfer files between the client and the server using SSH.

## Data source connectivity

The following table contains the supported data sources and respective requirements to connect with Data Optimizer.

<table><thead><tr><th width="196">Data source</th><th>Requirements</th></tr></thead><tbody><tr><td>AWS S3</td><td><ul><li>AWS region where the S3 bucket was created</li><li>Access key and secret access key</li><li>Read-only permissions to the S3 bucket</li></ul></td></tr><tr><td>Azure Blob Storage</td><td><ul><li>Account Fully Qualified Domain Name (FQDN)</li><li>Client ID and client key</li><li>authTokenEndpoint</li></ul></td></tr><tr><td>HCP</td><td><ul><li>AWS region where the S3 bucket was created</li><li>Access key and secret access key</li><li>Read-only permissions to the S3 bucket</li></ul></td></tr><tr><td>HDFS</td><td><ul><li>Hadoop version 2.7.2 and later</li><li>URI should provide a hostname and share folder details</li><li>Path of the directory that needs to be scanned</li><li>Read-only access to the directory</li></ul></td></tr><tr><td>SharePoint and OneDrive</td><td><ul><li>Application (client) ID, Directory (tenant ID), and clientSecret from a registered app on the Azure portal</li><li>Delegated permissions and Application permissions in the registered app</li><li>Read-only permissions to the SharePoint and OneDrive sites</li></ul></td></tr><tr><td>SMB/CIFS</td><td><ul><li>URI should provide host name and share folder details</li><li>Username and password to access the SMB/CIFS share directory</li><li>Path of directory that needs to be scanned</li><li>Read-only access is required</li></ul></td></tr></tbody></table>

## (Optional) Client Virtual Device Interface

The following table contains the client’s Virtual Device Interface (VDI) requirements.

<table><thead><tr><th width="198">Category</th><th>Requirements</th></tr></thead><tbody><tr><td>Server configuration</td><td><ul><li>Windows operating system</li><li>16 GB RAM</li></ul></td></tr><tr><td>Disk or storage</td><td>100 GB minimum</td></tr><tr><td>Others</td><td><ul><li>Internet connectivity</li><li>Google Chrome browser</li><li>Permission to download files from the FTP server (secure FTP access)</li></ul></td></tr></tbody></table>
