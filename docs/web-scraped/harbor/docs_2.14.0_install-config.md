# Harbor docs | Harbor Installation and Configuration

**Source:** https://goharbor.io/docs/2.14.0/install-config/

Harbor Installation and Configuration

[Harbor version 2.14.0](/docs/2.14.0)

[Harbor Installation and Configuration](/docs/2.14.0/install-config/)

* [Test Harbor with the Demo Server](/docs/2.14.0/install-config/demo-server/)
* [Harbor Compatibility List](/docs/2.14.0/install-config/harbor-compatibility-list/)
* [Harbor Installation Prerequisites](/docs/2.14.0/install-config/installation-prereqs/)
* [Download the Harbor Installer](/docs/2.14.0/install-config/download-installer/)
* [Configure HTTPS Access to Harbor](/docs/2.14.0/install-config/configure-https/)
* [Configure Internal TLS communication between Harbor Component](/docs/2.14.0/install-config/configure-internal-tls/)
* [Configure the Harbor YML File](/docs/2.14.0/install-config/configure-yml-file/)
* [Run the Installer Script](/docs/2.14.0/install-config/run-installer-script/)
* [Deploying Harbor with High Availability via Helm](/docs/2.14.0/install-config/harbor-ha-helm/)
* [Troubleshooting Harbor Installation](/docs/2.14.0/install-config/troubleshoot-installation/)
* [Reconfigure Harbor and Manage the Harbor Lifecycle](/docs/2.14.0/install-config/reconfigure-manage-lifecycle/)
* [Customize the Harbor Token Service](/docs/2.14.0/install-config/customize-token-service/)
* [Harbor Configuration](/docs/2.14.0/install-config/configure-system-settings-cli/)

[Harbor Administration](/docs/2.14.0/administration/)

[Working with Projects](/docs/2.14.0/working-with-projects/)

[Building, Customizing, and Contributing to Harbor](/docs/2.14.0/build-customize-contribute/)

This section describes how to perform a new installation of Harbor.

If you are upgrading from a previous version of Harbor, you might need to update the configuration file and migrate your data to fit the database schema of the later version. For information about upgrading, see
[Upgrading Harbor](/docs/2.14.0/administration/upgrade/).

Before you install Harbor, you can test the latest version of Harbor on a demo environment maintained by the Harbor team. For information, see
[Test Harbor with the Demo Server](/docs/2.14.0/install-config/demo-server/).

Harbor supports integration with different 3rd-party replication adapters for replicating data, OIDC adapters for authN/authZ, and scanner adapters for vulnerability scanning of container images. For information about the supported adapters, see the
[Harbor Compatibility List](/docs/2.14.0/install-config/harbor-compatibility-list/).

## Installation Process

The standard Harbor installation process involves the following stages:

1. Make sure that your target host meets the
   [Harbor Installation Prerequisites](/docs/2.14.0/install-config/installation-prereqs/).
2. [Download the Harbor Installer](/docs/2.14.0/install-config/download-installer/)
3. [Configure HTTPS Access to Harbor](/docs/2.14.0/install-config/configure-https/)
4. [Configure the Harbor YML File](/docs/2.14.0/install-config/configure-yml-file/)
5. [Configure Enabling Internal TLS](/docs/2.14.0/install-config/configure-internal-tls/)
6. [Run the Installer Script](/docs/2.14.0/install-config/run-installer-script/)

If installation fails, see
[Troubleshooting Harbor Installation](/docs/2.14.0/install-config/troubleshoot-installation/).

## Deploy Harbor on Kubernetes

You can also use Helm to install Harbor on a Kubernetes cluster, to make Harbor highly available. For information about installing Harbor with Helm on a Kubernetes cluster, see
[Deploying Harbor with High Availability via Helm](/docs/2.14.0/install-config/harbor-ha-helm/).

## Post-Installation Configuration

For information about how to manage your deployed Harbor instance, see
[Reconfigure Harbor and Manage the Harbor Lifecycle](/docs/2.14.0/install-config/reconfigure-manage-lifecycle/).

By default, Harbor uses its own private key and certificate to authenticate with Docker. For information about how to optionally customize your configuration to use your own key and certificate, see
[Customize the Harbor Token Service](/docs/2.14.0/install-config/customize-token-service/).

After installation, log into your Harbor via the web console to configure the instance under ‘configuration’. Harbor also provides a command line interface (CLI) that allows you to
[Configure Harbor System Settings at the Command Line](/docs/2.14.0/install-config/configure-system-settings-cli/).

## Harbor Components

The table below lists the some of the key components that are deployed when you deploy Harbor.

| Component | Version |
| --- | --- |
| Postgresql | 15.12 |
| Redis | 7.2.6 |
| Beego | 2.3.4 |
| Distribution/Distribution | 2.8.3 |
| Helm | 2.9.1 |
| Swagger-ui | 5.9.1 |

* The postgresql and redis version might be updated in the minor patch.

---

## Pages in this section

* [Test Harbor with the Demo Server](/docs/2.14.0/install-config/demo-server/)
* [Harbor Compatibility List](/docs/2.14.0/install-config/harbor-compatibility-list/)
* [Harbor Installation Prerequisites](/docs/2.14.0/install-config/installation-prereqs/)
* [Download the Harbor Installer](/docs/2.14.0/install-config/download-installer/)
* [Configure HTTPS Access to Harbor](/docs/2.14.0/install-config/configure-https/)
* [Configure Internal TLS communication between Harbor Component](/docs/2.14.0/install-config/configure-internal-tls/)
* [Configure the Harbor YML File](/docs/2.14.0/install-config/configure-yml-file/)
* [Run the Installer Script](/docs/2.14.0/install-config/run-installer-script/)
* [Deploying Harbor with High Availability via Helm](/docs/2.14.0/install-config/harbor-ha-helm/)
* [Troubleshooting Harbor Installation](/docs/2.14.0/install-config/troubleshoot-installation/)
* [Reconfigure Harbor and Manage the Harbor Lifecycle](/docs/2.14.0/install-config/reconfigure-manage-lifecycle/)
* [Customize the Harbor Token Service](/docs/2.14.0/install-config/customize-token-service/)
* [Harbor Configuration](/docs/2.14.0/install-config/configure-system-settings-cli/)

On this page

Contributing

[Page source](https://github.com/goharbor/website/blob/release-2.14.0/docs/install-config/_index.md)
[Create issue](https://github.com/goharbor/harbor/issues)
