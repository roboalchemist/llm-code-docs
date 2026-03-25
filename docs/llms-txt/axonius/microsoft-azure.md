# Source: https://docs.axonius.com/docs/microsoft-azure.md

# Microsoft Azure

## Overview

Microsoft Azure is a cloud computing service created by Microsoft for building, testing, deploying, and managing applications and services through a global network of Microsoft-managed data. The Microsoft Azure adapter fetches devices from the Microsoft Azure Cloud Environment.

### Use cases the adapter solves

The Azure adapter allows Axonius users to evaluate their public cloud resources to ensure that they are correctly configured and managed, even across multiple tenants. Users can also leverage data from this adapter to modify software update deployments (including security agents).

## Types of Assets Fetched

![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Devices.svg) Devices | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Vulnerabilities.svg) Vulnerabilities | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Roles.svg) Roles | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Groups.svg) Groups | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/SaaS_Application.svg) SaaS Applications | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Compute_Services.svg) Compute Services | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Application_Services.svg) Application Services | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Networks.svg) Networks | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Load_Balancers.svg) Load Balancers | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Databases.svg) Databases | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Containers.svg) Containers | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Object_Storage.svg) Object Storage | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Network_Services.svg) Network Services | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Accounts_Tenants.svg) Accounts/Tenants | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Serverless_Functions.svg) Serverless Functions | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Disks.svg) Disks | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Compute_Image.svg) Compute Images | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Secrets.svg) Secrets | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Certificates.svg) Certificates | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Network_Firewall_Rules.svg) Network/Firewall Rules | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Alerts_Incidents.svg) Alerts/Incidents | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Application_resources.svg) Application Resources | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Configurations.svg) Configurations

For the full list of asset types and services this adapter fetches, see [Microsoft Azure Services Fetched as Assets](/docs/microsoft-azure-services-fetched-as-assets).

## Data Retrieved from Microsoft Azure

The Microsoft Azure adapter collects a broad range of cloud asset and configuration data from Azure. By default, the adapter retrieves information from the following resource types and their associated child objects:

* **Virtual Machines (VMs)** – metadata, instance details, OS information, networking configuration, attached disks
* **Virtual Networks (VNets) & Network Security Groups (NSGs)** – subnets, IP configurations, security rules, associations
* **Azure SQL Servers & Databases** – server properties, database configurations, network and security settings
* **Load Balancers** – front-end IP configurations, backend pools, health probes, rules
* **Storage Accounts** – account properties, encryption settings, network access configurations
* **Key Vaults** – vault metadata, access policies, networking restrictions
* **Azure Cache for Redis** – instance properties, networking, configuration settings
* **Azure Kubernetes Service (AKS)** – cluster properties, node pools, configurations, pods (fetched as Containers)

## Before You Begin

### Authentication Methods

You can connect the adapter using one of the following authentication methods:

* **Enterprise Application (Client ID / Client Secret)** – Recommended for most scenarios.
* **Enterprise Application (Certificate)** – Provides certificate-based authentication.
* **Managed Identity** - Enables running your Axonius instance on Azure virtual machines with managed identities to authenticate without storing client secrets or certificates.

### Required Permissions

The following roles are mandatory for all authentication methods:

* Reader (Management Group and/or Subscription level)
* Directory Reader

### Additional Permissions

These roles and permissions are required only if you want to fetch specific Azure services.

<Tabs>
  <Tab title="Keys From Key Vaults">
    <Columns layout="auto">
      <Column>
        **Roles:**

        * Key Vault Crypto Officer
      </Column>

      <Column>
        **Permissions:**

        * `Microsoft.KeyVault/vaults/keys/read`
        * `Microsoft.KeyVault/vaults/keys/update/action`
        * `Microsoft.KeyVault/vaults/keys/create/action`
        * `Microsoft.KeyVault/vaults/keys/import/action`
        * `Microsoft.KeyVault/vaults/keys/recover/action`
        * `Microsoft.KeyVault/vaults/keys/restore/action`
        * `Microsoft.KeyVault/vaults/keys/delete`
        * `Microsoft.KeyVault/vaults/keys/backup/action`
        * `Microsoft.KeyVault/vaults/keys/purge/action`
        * `Microsoft.KeyVault/vaults/keys/encrypt/action`
        * `Microsoft.KeyVault/vaults/keys/decrypt/action`
        * `Microsoft.KeyVault/vaults/keys/wrap/action`
        * `Microsoft.KeyVault/vaults/keys/unwrap/action`
        * `Microsoft.KeyVault/vaults/keys/sign/action`
        * `Microsoft.KeyVault/vaults/keys/verify/action`
        * `Microsoft.KeyVault/vaults/keys/release/action`
        * `Microsoft.KeyVault/vaults/keys/rotate/action`
      </Column>
    </Columns>
  </Tab>

  <Tab title="Certificates from Key Vaults">
    <Columns layout="auto">
      <Column>
        **Roles:**

        * Key Vault Certificates Reader
      </Column>

      <Column>
        **Permissions:**

        * `Microsoft.KeyVault/vaults/certificates/read`
        * `Microsoft.KeyVault/vaults/certificates/list`
      </Column>
    </Columns>
  </Tab>
</Tabs>

## More Information About This Adapter

* [Deploying the Azure Adapter](/docs/azure-deploying-the-adapter)
* [Advanced Settings](/docs/azure-advanced-settings)
* [Microsoft Azure Services Fetched as Assets](/docs/microsoft-azure-services-fetched-as-assets)
* [Related Enforcement Actions](/docs/azure-related-enforcement-actions)

<br />