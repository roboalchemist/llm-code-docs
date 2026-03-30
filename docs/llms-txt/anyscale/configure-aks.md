# Source: https://docs.anyscale.com/admin/azure/configure-aks.md

# Anyscale on AKS

[View Markdown](/admin/azure/configure-aks.md)

# Anyscale on AKS

important

Anyscale on Azure is an [Azure Native Integration](https://learn.microsoft.com/en-us/azure/partner-solutions/overview) in Private Preview. Anyscale and Microsoft develop this product in partnership. It includes a control plane hosted in Azure and unifies deployment, management, and monitoring in the Azure portal. To enroll, contact [Anyscale support](mailto:support@anyscale.com).

You can also get started building on AKS today using Anyscale on the AWS control plane, which has general availability for cloud resources backed by AKS. Use the following interactive page to configure a new Anyscale cloud resource on AKS: [Deploy Anyscale on AKS](/admin/azure/create-aks-cloud.md).

For more details on configuring and deploying Anyscale cloud resources on AKS, see [Deploy Anyscale on Kubernetes](/admin/cloud/kubernetes.md).

## Manage permissions in your AKS cloud resource[​](#manage-permissions-in-your-aks-cloud-resource "Direct link to Manage permissions in your AKS cloud resource")

Anyscale integrates with Azure managed identities to govern permissions for your cloud resources. You can configure default permissions shared by all workloads in your Anyscale cloud, or use cloud IAM mapping to scope managed identities to users, projects, or workload types. See [Configure managed identities for clusters on Anyscale on AKS](/admin/azure/aks-iam.md).

## Customize your Anyscale operator[​](#customize-your-anyscale-operator "Direct link to Customize your Anyscale operator")

Once you've configured AKS as an Anyscale cloud resource, you customize your deployment by editing the Helm chart and upgrading the Anyscale operator. See [Configure the Helm chart for the Anyscale operator](/k8s/configure-helm.md).

## Integrate with Azure services[​](#integrate-with-azure-services "Direct link to Integrate with Azure services")

The following articles focus mostly on integrating Azure services so developers can use them in their workflows and production jobs. These integrations leverage managed identities assigned to Anyscale clusters.

* [Access blob storage and ADLS](/admin/azure/storage.md)
* [Configure shared storage with Azure blob PVC for AKS](/admin/azure/pvc.md)
* [Use secrets from Azure Key Vault](/admin/azure/key-vault.md)
* [Configure Azure Container Registry](/admin/azure/container-registry.md)

Administrator and ops personas can also integrate with other Azure services directly through AKS. See Azure docs or reach out to Anyscale support to configure and troubleshoot custom AKS configurations and integrations.
