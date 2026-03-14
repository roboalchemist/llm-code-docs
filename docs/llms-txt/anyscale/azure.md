# Source: https://docs.anyscale.com/azure.md

# Anyscale on Azure

[View Markdown](/azure.md)

# Anyscale on Azure

Anyscale on Azure is an [Azure Native Integration](https://learn.microsoft.com/en-us/azure/partner-solutions/overview) in Private Preview. Anyscale and Microsoft develop this product in partnership. It includes a control plane hosted in Azure and unifies deployment, management, and monitoring in the Azure portal. To enroll, contact [Anyscale support](mailto:support@anyscale.com).

You configure an Anyscale cloud on top of your AKS cluster to create your Anyscale organization. Anyscale integrates with Entra ID to provide SSO for your Azure tenant.

note

Anyscale also supports configuring cloud resources using AKS in the AWS control plane. If you're participating in the private preview, you must deploy all Anyscale clouds and cloud resources through the Azure portal.

Anyscale on Azure doesn't support the virtual machine (VM) stack. All cloud resources on Azure use Kubernetes.

## Configure your first Anyscale cloud on AKS[​](#configure-your-first-anyscale-cloud-on-aks "Direct link to Configure your first Anyscale cloud on AKS")

When you enroll in the private preview, Azure adds the Anyscale resource provider to your Azure tenant. You use the resource provider to configure an Anyscale cloud on top of an existing AKS cluster. For details, see [Deploy Anyscale on Azure](/azure/deploy.md).

## Manage permissions in your AKS cloud resource[​](#manage-permissions "Direct link to Manage permissions in your AKS cloud resource")

Anyscale integrates with Azure managed identities to govern permissions for your cloud resources. You can configure default permissions shared by all workloads in your Anyscale cloud, or use cloud IAM mapping to scope managed identities to users, projects, or workload types. See [Configure managed identities for clusters on Anyscale on AKS](/admin/azure/aks-iam.md).

## Customize your Anyscale operator[​](#customize-operator "Direct link to Customize your Anyscale operator")

Once you've configured AKS as an Anyscale cloud resource, you customize your deployment by editing the Helm chart and upgrading the Anyscale operator. See [Configure the Helm chart for the Anyscale operator](/k8s/configure-helm.md).

## Integrate with Azure services[​](#integrate-with-azure-services "Direct link to Integrate with Azure services")

You configure most integrations with Azure services to support Anyscale workloads using some combination of Anyscale operator configuration, AKS configurations, and updates to Azure managed identities. The following pages provide instructions for integrating with common Azure services to support your Anyscale workloads:

note

The linked pages provide configuration instructions that are general for the Azure and AWS control planes. Contact [Anyscale support](mailto:support@anyscale.com) if you encounter non-functioning instructions or code examples in the Anyscale docs.

* [Configure managed identities for clusters on Anyscale on AKS](/admin/azure/aks-iam.md)
* [Access blob storage and ADLS](/admin/azure/storage.md)
* [Configure shared storage with Azure blob PVC for AKS](/admin/azure/pvc.md)
* [Configure Azure Container Registry](/admin/azure/container-registry.md)
* [Use secrets from Azure Key Vault](/admin/azure/key-vault.md)

Administrator and ops personas can also integrate with other Azure services directly through AKS. See [Azure documentation](https://learn.microsoft.com/azure/) or contact [Anyscale support](mailto:support@anyscale.com) to configure and troubleshoot custom AKS configurations and integrations.

## Access Anyscale on Azure[​](#access-anyscale-on-azure "Direct link to Access Anyscale on Azure")

After you've created an Anyscale organization on Azure, you can access your organization by visiting the following URL: <https://console.azure.anyscale.com>.

You can also view Anyscale clouds in your Azure tenant in the Azure portal and follow links to access these clouds.

## Interact with the Azure control plane[​](#interact-with-the-azure-control-plane "Direct link to Interact with the Azure control plane")

By default, the Anyscale CLI and SDK connect to an Anyscale control plane hosted in AWS. To interact with the Azure control plane, follow these steps to configure your local environment:

note

The following instructions are the recommended flow for the current state of the private preview. Store API keys securely when using them as environment variables.

Anyscale plans to add CLI support for direct authentication to the Azure control plane.

1. Run the following command to set a target host as an environment variable for your current session:

   ```
   export ANYSCALE_HOST=https://console.azure.anyscale.com
   ```

2. Run the following command to authenticate to Anyscale on Azure:

   ```
   anyscale login
   ```

3. Run a command to confirm access. The following command lists all Anyscale clouds you have at least read-only permissions to view:

   ```
   anyscale cloud list
   ```

important

Use the Azure portal to create new Anyscale clouds on AKS. Once a cloud exists, you update it with the Anyscale CLI, Helm charts for the Anyscale operator, and kubectl or the Azure CLI for direct interaction with AKS.

## Deploy an additional cloud resource[​](#deploy-an-additional-cloud-resource "Direct link to Deploy an additional cloud resource")

You can optionally deploy multiple cloud resources to your Anyscale cloud.

To add a cloud resource to an existing Anyscale cloud, do the following:

1. Navigate to the [Anyscale clouds list](https://aka.ms/anyscaleprivatepreview) in the Azure portal.
2. Click the name of your cloud.
3. Click **Cloud resources**.
4. Click **Create**.

The cloud resource flow is nearly identical to the flow for creating your first cloud, except that you have multiple cloud resources in your cloud config. See [Deploy Anyscale on Azure](/azure/deploy.md).

## Limitations[​](#limitations "Direct link to Limitations")

* You must create and delete Anyscale clouds and cloud resources using the Anyscale resource provider in the Azure portal. The following commands aren't supported:

  <!-- -->

  * `anyscale cloud setup`
  * `anyscale cloud register`
  * `anyscale cloud delete`

* The following CLI commands aren't supported:

  <!-- -->

  * `anyscale workspace_v2 ssh`
  * `anyscale workspace_v2 pull`
  * All `anyscale image` commands

* Anyscale on Azure only supports cloud resources backed by AKS. You can't deploy clouds from other cloud providers or on-prem.

* Anyscale platform features that require the VM stack aren't supported. Anyscale on Azure only uses Kubernetes.

* Anyscale-hosted clouds aren't available for Anyscale on Azure.
