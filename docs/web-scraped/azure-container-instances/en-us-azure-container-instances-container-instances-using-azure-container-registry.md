# Source: https://learn.microsoft.com/en-us/azure/container-instances/container-instances-using-azure-container-registry

Title: Deploy container image from Azure Container Registry using a service principal - Azure Container Instances

URL Source: https://learn.microsoft.com/en-us/azure/container-instances/container-instances-using-azure-container-registry

Published Time: Thu, 11 Dec 2025 06:03:39 GMT

Markdown Content:
Deploy container image from Azure Container Registry using a service principal - Azure Container Instances | Microsoft Learn
===============

[Skip to main content](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-using-azure-container-registry#main)[Skip to Ask Learn chat experience](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-using-azure-container-registry#)

Go deep on real code and real systems at Microsoft Build 2026, June 2-3 in San Francisco and online[Get started](https://aka.ms/MSBuild_FY26_BN_MSLearn_Txt)Dismiss alert

This browser is no longer supported.

Upgrade to Microsoft Edge to take advantage of the latest features, security updates, and technical support.

[Download Microsoft Edge](https://go.microsoft.com/fwlink/p/?LinkID=2092881)[More info about Internet Explorer and Microsoft Edge](https://learn.microsoft.com/en-us/lifecycle/faq/internet-explorer-microsoft-edge)

[Learn](https://learn.microsoft.com/en-us/)[](https://www.microsoft.com/)

 Suggestions will filter as you type

[Sign in](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-using-azure-container-registry#)

![Image 4](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-using-azure-container-registry)

![Image 5](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-using-azure-container-registry)

* [Profile](https://learn.microsoft.com/en-us/users/me/activity/)
* [Settings](https://learn.microsoft.com/en-us/users/me/settings/)

[Sign out](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-using-azure-container-registry#)

[](https://www.microsoft.com/)[Learn](https://learn.microsoft.com/en-us/)

* Documentation

  * [All product documentation](https://learn.microsoft.com/en-us/docs/)
  * [Azure documentation](https://learn.microsoft.com/en-us/azure/?product=popular)
  * [Dynamics 365 documentation](https://learn.microsoft.com/en-us/dynamics365/)
  * [Microsoft Copilot documentation](https://learn.microsoft.com/en-us/copilot/)
  * [Microsoft 365 documentation](https://learn.microsoft.com/en-us/microsoft-365/)
  * [Power Platform documentation](https://learn.microsoft.com/en-us/power-platform/)
  * [Code samples](https://learn.microsoft.com/en-us/samples/)
  * [Troubleshooting documentation](https://learn.microsoft.com/en-us/troubleshoot/)

Free to join. Request to attend.

[Microsoft AI Tour](https://aitour.microsoft.com/?wt.mc_id=itour26_learnmarketingspot_wwl)
Take your business to the AI frontier.

* Training & Labs

  * [All training](https://learn.microsoft.com/en-us/training/)
  * [Azure training](https://learn.microsoft.com/en-us/training/browse/?products=azure)
  * [Dynamics 365 training](https://learn.microsoft.com/en-us/training/browse/?products=dynamics-365)
  * [Microsoft Copilot training](https://learn.microsoft.com/en-us/training/browse/?products=ms-copilot)
  * [Microsoft 365 training](https://learn.microsoft.com/en-us/training/browse/?products=m365)
  * [Microsoft Power Platform training](https://learn.microsoft.com/en-us/training/browse/?products=power-platform)
  * [Labs](https://learn.microsoft.com/en-us/labs/)
  * [Credentials](https://learn.microsoft.com/en-us/credentials/)
  * [Career paths](https://learn.microsoft.com/en-us/training/career-paths/)

Free to join. Request to attend.

[Microsoft AI Tour](https://aitour.microsoft.com/?wt.mc_id=itour26_learnmarketingspot_wwl)
Take your business to the AI frontier.

* Q&A

  * [Ask a question](https://learn.microsoft.com/en-us/answers/questions/ask/)
  * [Azure questions](https://learn.microsoft.com/en-us/answers/tags/133/azure/)
  * [Windows questions](https://learn.microsoft.com/en-us/answers/tags/60/windows/)
  * [Microsoft 365 questions](https://learn.microsoft.com/en-us/answers/tags/9/m365/)
  * [Microsoft Outlook questions](https://learn.microsoft.com/en-us/answers/tags/131/office-outlook/)
  * [Microsoft Teams questions](https://learn.microsoft.com/en-us/answers/tags/108/office-teams/)
  * [Popular tags](https://learn.microsoft.com/en-us/answers/tags/)
  * [All questions](https://learn.microsoft.com/en-us/answers/questions/)

Free to join. Request to attend.

[Microsoft AI Tour](https://aitour.microsoft.com/?wt.mc_id=itour26_learnmarketingspot_wwl)
Take your business to the AI frontier.

* Topics

  * [Artificial intelligence](https://learn.microsoft.com/en-us/ai/)
Learning hub to build AI skills
  * [Compliance](https://learn.microsoft.com/en-us/compliance/)
Compliance resources you need to get started with your business
  * [DevOps](https://learn.microsoft.com/en-us/devops/)
DevOps practices, Git version control and Agile methods
  * [Learn for Organizations](https://learn.microsoft.com/en-us/training/organizations/)
Curated offerings from Microsoft to boost your team’s technical skills
  * [Platform engineering](https://learn.microsoft.com/en-us/platform-engineering/)
Tools from Microsoft and others to build personalized developer experiences
  * [Security](https://learn.microsoft.com/en-us/security/)
Guidance to help you tackle security challenges
  * [Assessments](https://learn.microsoft.com/en-us/assessments/)
Interactive guidance with custom recommendations
  * [Student hub](https://learn.microsoft.com/en-us/training/student-hub/)
Self-paced and interactive training for students
  * [Educator center](https://learn.microsoft.com/en-us/training/educator-center/)
Resources for educators to bring technical innovation in their classroom

Free to join. Request to attend.

[Microsoft AI Tour](https://aitour.microsoft.com/?wt.mc_id=itour26_learnmarketingspot_wwl)
Take your business to the AI frontier.

 Suggestions will filter as you type

[Sign in](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-using-azure-container-registry#)

![Image 6](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-using-azure-container-registry)

![Image 7](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-using-azure-container-registry)

* [Profile](https://learn.microsoft.com/en-us/users/me/activity/)
* [Settings](https://learn.microsoft.com/en-us/users/me/settings/)

[Sign out](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-using-azure-container-registry#)

[Azure](https://learn.microsoft.com/en-us/azure/)

* Products
  * Popular products
    * [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/)
    * [Azure App Service](https://learn.microsoft.com/en-us/azure/app-service/)
    * [Azure Databricks](https://learn.microsoft.com/en-us/azure/databricks/)
    * [Azure DevOps](https://learn.microsoft.com/en-us/azure/devops/)
    * [Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/)
    * [Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/)
    * [Azure Virtual Machines](https://learn.microsoft.com/en-us/azure/virtual-machines/)

  * Popular categories
    * [Compute](https://learn.microsoft.com/en-us/azure/?product=compute)
    * [Networking](https://learn.microsoft.com/en-us/azure/?product=networking)
    * [Storage](https://learn.microsoft.com/en-us/azure/?product=storage)
    * [AI & machine learning](https://learn.microsoft.com/en-us/azure/?product=ai-machine-learning)
    * [Analytics](https://learn.microsoft.com/en-us/azure/?product=analytics)
    * [Databases](https://learn.microsoft.com/en-us/azure/?product=databases)
    * [Security](https://learn.microsoft.com/en-us/azure/?product=security)

  * [View all products](https://learn.microsoft.com/en-us/azure/)

* Architecture
  * [Cloud Adoption Framework](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/)
  * [Well-Architected Framework](https://learn.microsoft.com/en-us/azure/well-architected/)
  * [Azure Architecture Center](https://learn.microsoft.com/en-us/azure/architecture/)

* Develop
  * [Python](https://learn.microsoft.com/en-us/azure/developer/python/)
  * [.NET](https://learn.microsoft.com/en-us/dotnet/azure/)
  * [JavaScript](https://learn.microsoft.com/en-us/azure/developer/javascript/)
  * [Java](https://learn.microsoft.com/en-us/azure/developer/java/)
  * [PowerShell](https://learn.microsoft.com/en-us/powershell/azure/)
  * [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/)
  * [View all developer resources](https://learn.microsoft.com/en-us/azure/developer/)

* Learn Azure
  * [Start your AI learning assessment](https://learn.microsoft.com/en-us/assessments/1c032171-8ca0-4032-8962-a38a5cc424a8/)
  * Top learning paths
    * [Cloud concepts](https://learn.microsoft.com/en-us/training/paths/microsoft-azure-fundamentals-describe-cloud-concepts/)
    * [AI fundamentals](https://learn.microsoft.com/en-us/training/paths/get-started-with-artificial-intelligence-on-azure/)
    * [Intro to generative AI](https://learn.microsoft.com/en-us/training/paths/introduction-generative-ai/)
    * [Azure Architecture fundamentals](https://learn.microsoft.com/en-us/training/paths/azure-fundamentals-describe-azure-architecture-services/)

  * [Earn credentials](https://learn.microsoft.com/en-us/credentials/browse/?products=azure)
  * [Instructor-led courses](https://learn.microsoft.com/en-us/training/browse/?products=azure&resource_type=course)
  * [View all training](https://learn.microsoft.com/en-us/training/azure/)

* [Troubleshooting](https://learn.microsoft.com/en-us/troubleshoot/azure/)
* Resources
  * [Product overview](https://azure.microsoft.com/get-started)
  * [Azure updates](https://azure.microsoft.com/updates)
  * [Pricing information](https://azure.microsoft.com/pricing/)
  * [Cost management & billing](https://learn.microsoft.com/en-us/azure/cost-management-billing/)
  * [Latest blog posts](https://azure.microsoft.com/blog/)
  * [Support options](https://azure.microsoft.com/support/options/)

* More
  * Products
    * Popular products
      * [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/)
      * [Azure App Service](https://learn.microsoft.com/en-us/azure/app-service/)
      * [Azure Databricks](https://learn.microsoft.com/en-us/azure/databricks/)
      * [Azure DevOps](https://learn.microsoft.com/en-us/azure/devops/)
      * [Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/)
      * [Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/)
      * [Azure Virtual Machines](https://learn.microsoft.com/en-us/azure/virtual-machines/)

    * Popular categories
      * [Compute](https://learn.microsoft.com/en-us/azure/?product=compute)
      * [Networking](https://learn.microsoft.com/en-us/azure/?product=networking)
      * [Storage](https://learn.microsoft.com/en-us/azure/?product=storage)
      * [AI & machine learning](https://learn.microsoft.com/en-us/azure/?product=ai-machine-learning)
      * [Analytics](https://learn.microsoft.com/en-us/azure/?product=analytics)
      * [Databases](https://learn.microsoft.com/en-us/azure/?product=databases)
      * [Security](https://learn.microsoft.com/en-us/azure/?product=security)

    * [View all products](https://learn.microsoft.com/en-us/azure/)

  * Architecture
    * [Cloud Adoption Framework](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/)
    * [Well-Architected Framework](https://learn.microsoft.com/en-us/azure/well-architected/)
    * [Azure Architecture Center](https://learn.microsoft.com/en-us/azure/architecture/)

  * Develop
    * [Python](https://learn.microsoft.com/en-us/azure/developer/python/)
    * [.NET](https://learn.microsoft.com/en-us/dotnet/azure/)
    * [JavaScript](https://learn.microsoft.com/en-us/azure/developer/javascript/)
    * [Java](https://learn.microsoft.com/en-us/azure/developer/java/)
    * [PowerShell](https://learn.microsoft.com/en-us/powershell/azure/)
    * [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/)
    * [View all developer resources](https://learn.microsoft.com/en-us/azure/developer/)

  * Learn Azure
    * [Start your AI learning assessment](https://learn.microsoft.com/en-us/assessments/1c032171-8ca0-4032-8962-a38a5cc424a8/)
    * Top learning paths
      * [Cloud concepts](https://learn.microsoft.com/en-us/training/paths/microsoft-azure-fundamentals-describe-cloud-concepts/)
      * [AI fundamentals](https://learn.microsoft.com/en-us/training/paths/get-started-with-artificial-intelligence-on-azure/)
      * [Intro to generative AI](https://learn.microsoft.com/en-us/training/paths/introduction-generative-ai/)
      * [Azure Architecture fundamentals](https://learn.microsoft.com/en-us/training/paths/azure-fundamentals-describe-azure-architecture-services/)

    * [Earn credentials](https://learn.microsoft.com/en-us/credentials/browse/?products=azure)
    * [Instructor-led courses](https://learn.microsoft.com/en-us/training/browse/?products=azure&resource_type=course)
    * [View all training](https://learn.microsoft.com/en-us/training/azure/)

  * [Troubleshooting](https://learn.microsoft.com/en-us/troubleshoot/azure/)
  * Resources
    * [Product overview](https://azure.microsoft.com/get-started)
    * [Azure updates](https://azure.microsoft.com/updates)
    * [Pricing information](https://azure.microsoft.com/pricing/)
    * [Cost management & billing](https://learn.microsoft.com/en-us/azure/cost-management-billing/)
    * [Latest blog posts](https://azure.microsoft.com/blog/)
    * [Support options](https://azure.microsoft.com/support/options/)

[Portal](https://portal.azure.com/)[Get started with Azure](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn)

Search

 Suggestions will filter as you type

* [Container Instances documentation](https://learn.microsoft.com/en-us/azure/container-instances/)
* Overview
* Quickstarts
  * [Deploy a container instance - CLI](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-quickstart)
  * [Deploy a container instance - Portal](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-quickstart-portal)
  * [Deploy a container instance - PowerShell](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-quickstart-powershell)
  * [Deploy a container instance - Bicep](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-quickstart-bicep)
  * [Deploy a container instance - ARM template](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-quickstart-template)
  * [Deploy a container instance - Terraform](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-quickstart-terraform)

* Tutorials
* Samples
* Concepts
* How-to guides
  * Deploy
    * [Deploy in a virtual network](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-vnet)
    * Deploy from Azure Container Registry
      * [Deploy using a service principal](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-using-azure-container-registry)
      * [Deploy using a managed identity](https://learn.microsoft.com/en-us/azure/container-instances/using-azure-container-registry-mi)

    * [Deploy with GitHub Actions](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-github-action)
    * [Encrypt deployment data](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-encrypt-data)
    * [Availability zones and disaster recovery](https://learn.microsoft.com/en-us/azure/reliability/reliability-container-instances?toc=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fazure%2Fcontainer-instances%2Ftoc.json&bc=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fazure%2Fbreadcrumb%2Fazure-compute%2Ftoc.json)
    * [Configure DNS name reuse](https://learn.microsoft.com/en-us/azure/container-instances/how-to-reuse-dns-names)
    * [Use Logic Apps connector](https://learn.microsoft.com/en-us/azure/connectors/connectors-create-api-container-instances?toc=/azure/container-instances/toc.json&bc=/azure/container-instances/breadcrumb/toc.json)
    * [Deploy confidential containers using the Azure portal](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-tutorial-deploy-confidential-container-default-portal)
    * [Deploy confidential containers using ARM](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-tutorial-deploy-confidential-containers-cce-arm)

  * Container scenarios
  * Mount data volumes
  * Manage running containers
  * Manage a standby pool
  * Monitor and log
  * Troubleshoot

* Reference
* Resources
* [Support and troubleshooting](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-support-help)

Download PDF

 Table of contents Exit editor mode

1. [Learn](https://learn.microsoft.com/en-us/)
2. [Azure](https://learn.microsoft.com/en-us/azure/)
3. [Container Instances](https://learn.microsoft.com/en-us/azure/container-instances/)

4. [Learn](https://learn.microsoft.com/en-us/)
5. [Azure](https://learn.microsoft.com/en-us/azure/)
6. [Container Instances](https://learn.microsoft.com/en-us/azure/container-instances/)

Ask Learn Ask Learn Focus mode

Table of contents[Read in English](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-using-azure-container-registry)Add to Collections Add to plan[Edit](https://github.com/MicrosoftDocs/azure-compute-docs/blob/main/articles/container-instances/container-instances-using-azure-container-registry.md)

* * *

#### Share via

[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fazure%2Fcontainer-instances%2Fcontainer-instances-using-azure-container-registry%3FWT.mc_id%3Dfacebook)[x.com](https://twitter.com/intent/tweet?original_referer=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fazure%2Fcontainer-instances%2Fcontainer-instances-using-azure-container-registry%3FWT.mc_id%3Dtwitter&tw_p=tweetbutton&url=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fazure%2Fcontainer-instances%2Fcontainer-instances-using-azure-container-registry%3FWT.mc_id%3Dtwitter)[LinkedIn](https://www.linkedin.com/feed/?shareActive=true&text=%0A%0D%0Ahttps%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fazure%2Fcontainer-instances%2Fcontainer-instances-using-azure-container-registry%3FWT.mc_id%3Dlinkedin)[Email](mailto:?subject=%5BShared%20Article%5D%20Deploy%20container%20image%20from%20Azure%20Container%20Registry%20using%20a%20service%20principal%20-%20Azure%20Container%20Instances%20%7C%20Microsoft%20Learn&body=%0A%0D%0Ahttps%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fazure%2Fcontainer-instances%2Fcontainer-instances-using-azure-container-registry%3FWT.mc_id%3Demail)

* * *

Copy Markdown Print

* * *

Note

Access to this page requires authorization. You can try [signing in](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-using-azure-container-registry#) or [changing directories](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-using-azure-container-registry).

Access to this page requires authorization. You can try [changing directories](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-using-azure-container-registry).

Deploy to Azure Container Instances from Azure Container Registry using a service principal
===========================================================================================

Feedback

 Summarize this article for me

In this article
---------------

1. [Prerequisites](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-using-azure-container-registry#prerequisites)
2. [Limitations](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-using-azure-container-registry#limitations)
3. [Configure registry authentication](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-using-azure-container-registry#configure-registry-authentication)
4. [Deploy container with Azure CLI](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-using-azure-container-registry#deploy-container-with-azure-cli)
5. [Deploy with Azure Resource Manager template](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-using-azure-container-registry#deploy-with-azure-resource-manager-template)
6. [Deploy with Azure portal](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-using-azure-container-registry#deploy-with-azure-portal)
7. [Next steps](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-using-azure-container-registry#next-steps)

Show 3 more

[Azure Container Registry](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-intro) is an Azure-based, managed container registry service used to store private Docker container images. This article describes how to pull container images stored in an Azure container registry when deploying to Azure Container Instances. One way to configure registry access is to create a Microsoft Entra service principal and password, and store the sign-in credentials in an Azure key vault.

[](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-using-azure-container-registry#prerequisites)
Prerequisites
-------------

**Azure container registry**: You need an Azure container registry--and at least one container image in the registry--to complete the steps in this article. If you need a registry, see [Create a container registry using the Azure CLI](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-get-started-azure-cli).

**Azure CLI**: The command-line examples in this article use the [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/) and are formatted for the Bash shell. You can [install the Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli) locally, or use the [Azure Cloud Shell](https://shell.azure.com/bash).

[](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-using-azure-container-registry#limitations)
Limitations
-----------

* Windows containers don't support system-assigned managed identity-authenticated image pulls with ACR, only user-assigned.

[](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-using-azure-container-registry#configure-registry-authentication)
Configure registry authentication
---------------------------------

In a production scenario where you provide access to "headless" services and applications, we recommend you configure registry access by using a [service principal](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-auth-service-principal). A service principal allows you to provide [Azure role-based access control (Azure RBAC)](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-roles) to your container images. For example, you can configure a service principal with pull-only access to a registry.

Azure Container Registry provides more [authentication options](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-authentication).

In the following section, you create an Azure key vault and a service principal, and store the service principal's credentials in the vault.

[](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-using-azure-container-registry#create-key-vault)

### Create key vault

If you don't already have a vault in [Azure Key Vault](https://learn.microsoft.com/en-us/azure/key-vault/general/overview), create one with the Azure CLI using the following commands.

Update the `RES_GROUP` variable with the name of an existing resource group in which to create the key vault, and `ACR_NAME` with the name of your container registry. For brevity, commands in this article assume that your registry, key vault, and container instances are all created in the same resource group.

Specify a name for your new key vault in `AKV_NAME`. The vault name must be unique within Azure and must be 3-24 alphanumeric characters in length, begin with a letter, end with a letter or digit, and can't contain consecutive hyphens.

 Azure CLI

Copy

```azurecli
RES_GROUP=myresourcegroup # Resource Group name
ACR_NAME=myregistry       # Azure Container Registry registry name
AKV_NAME=mykeyvault       # Azure Key Vault vault name

az keyvault create -g $RES_GROUP -n $AKV_NAME
```

[](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-using-azure-container-registry#create-service-principal-and-store-credentials)

### Create service principal and store credentials

Now create a service principal and store its credentials in your key vault.

The following commands use [az ad sp create-for-rbac](https://learn.microsoft.com/en-us/cli/azure/ad/sp#az_ad_sp_create_for_rbac) to create the service principal, and [az keyvault secret set](https://learn.microsoft.com/en-us/cli/azure/keyvault/secret#az_keyvault_secret_set) to store the service principal's **password** in the vault. Be sure to take note of the service principal's **appId** upon creation.

 Azure CLI

Copy

```azurecli
# Create service principal
az ad sp create-for-rbac \
  --name http://$ACR_NAME-pull \
  --scopes $(az acr show --name $ACR_NAME --query id --output tsv) \
  --role acrpull

SP_ID=xxxx # Replace with your service principal's appId

# Store the registry *password* in the vault
az keyvault secret set \
  --vault-name $AKV_NAME \
  --name $ACR_NAME-pull-pwd \
  --value $(az ad sp show --id $SP_ID --query password --output tsv)
```

The `--role` argument in the preceding command configures the service principal with the _acrpull_ role, which grants it pull-only access to the registry. To grant both push and pull access, change the `--role` argument to _acrpush_.

Next, store the service principal's _appId_ in the vault, which is the **username** you pass to Azure Container Registry for authentication.

 Azure CLI

Copy

```azurecli
# Store service principal ID in vault (the registry *username*)
az keyvault secret set \
    --vault-name $AKV_NAME \
    --name $ACR_NAME-pull-usr \
    --value $(az ad sp show --id $SP_ID --query appId --output tsv)
```

You created an Azure key vault and stored two secrets in it:

* `$ACR_NAME-pull-usr`: The service principal ID, for use as the container registry **username**.
* `$ACR_NAME-pull-pwd`: The service principal password, for use as the container registry **password**.

You can now reference these secrets by name when you or your applications and services pull images from the registry.

[](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-using-azure-container-registry#deploy-container-with-azure-cli)
Deploy container with Azure CLI
-------------------------------

Now that the service principal credentials are stored in Azure Key Vault secrets, your applications and services can use them to access your private registry.

First get the registry's login server name by using the [az acr show](https://learn.microsoft.com/en-us/cli/azure/acr#az_acr_show) command. The login server name is all lowercase and similar to `myregistry.azurecr.io`.

 Azure CLI

Copy

```azurecli
ACR_LOGIN_SERVER=$(az acr show --name $ACR_NAME --resource-group $RES_GROUP --query "loginServer" --output tsv)
```

Execute the following [az container create](https://learn.microsoft.com/en-us/cli/azure/container#az_container_create) command to deploy a container instance. The command uses the service principal's credentials stored in Azure Key Vault to authenticate to your container registry, and assumes you previously pushed the [aci-helloworld](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-quickstart) image to your registry. Update the `--image` value if you'd like to use a different image from your registry.

 Azure CLI

Copy

```azurecli
az container create \
    --name aci-demo \
    --resource-group $RES_GROUP \
    --image $ACR_LOGIN_SERVER/aci-helloworld:v1 \
    --registry-login-server $ACR_LOGIN_SERVER \
    --registry-username $(az keyvault secret show --vault-name $AKV_NAME -n $ACR_NAME-pull-usr --query value -o tsv) \
    --registry-password $(az keyvault secret show --vault-name $AKV_NAME -n $ACR_NAME-pull-pwd --query value -o tsv) \
    --dns-name-label aci-demo-$RANDOM \
    --query ipAddress.fqdn
```

The `--dns-name-label` value must be unique within Azure, so the preceding command appends a random number to the container's DNS name label. The output from the command displays the container's fully qualified domain name (FQDN), for example:

 Output

Copy

```output
"aci-demo-25007.eastus.azurecontainer.io"
```

Once the container starts successfully, you can navigate to its FQDN in your browser to verify the application is running successfully.

[](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-using-azure-container-registry#deploy-with-azure-resource-manager-template)
Deploy with Azure Resource Manager template
-------------------------------------------

You can specify the properties of your Azure container registry in an Azure Resource Manager template by including the `imageRegistryCredentials` property in the container group definition. For example, you can specify the registry credentials directly:

 JSON

Copy

```JSON
[...]
"imageRegistryCredentials": [
  {
    "server": "imageRegistryLoginServer",
    "username": "imageRegistryUsername",
    "password": "imageRegistryPassword"
  }
]
[...]
```

For complete container group settings, see the [Resource Manager template reference](https://learn.microsoft.com/en-us/azure/templates/Microsoft.ContainerInstance/2019-12-01/containerGroups).

For details on referencing Azure Key Vault secrets in a Resource Manager template, see [Use Azure Key Vault to pass secure parameter value during deployment](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/key-vault-parameter).

[](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-using-azure-container-registry#deploy-with-azure-portal)
Deploy with Azure portal
------------------------

If you maintain container images in an Azure container registry, you can easily create a container in Azure Container Instances using the Azure portal. When using the portal to deploy a container instance from a container registry, you must enable the registry's [admin account](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-authentication#admin-account). The admin account is designed for a single user to access the registry, mainly for testing purposes.

1. In the Azure portal, navigate to your container registry.

2. To confirm that the admin account is enabled, select **Access keys**, and under **Admin user** select **Enable**.

3. Select **Repositories**, then select the repository that you want to deploy from, right-click the tag for the container image you want to deploy, and select **Run instance**.

![Image 8: "Run instance" in Azure Container Registry in the Azure portal](https://learn.microsoft.com/en-us/azure/container-instances/media/container-instances-using-azure-container-registry/acr-runinstance-contextmenu.png)

1. Enter a name for the container and a name for the resource group. You can also change the default values if you wish.

![Image 9: Create menu for Azure Container Instances](https://learn.microsoft.com/en-us/azure/container-instances/media/container-instances-using-azure-container-registry/acr-create-deeplink.png)

1. Once the deployment completes, you can navigate to the container group from the notifications pane to find its IP address and other properties.

![Image 10: Details view for Azure Container Instances container group](https://learn.microsoft.com/en-us/azure/container-instances/media/container-instances-using-azure-container-registry/aci-detailsview.png)

[](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-using-azure-container-registry#next-steps)
Next steps
----------

For more information about Azure Container Registry authentication, see [Authenticate with an Azure container registry](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-authentication).

* * *

Feedback
--------

Was this page helpful?

Yes No

No

Need help with this topic?

Want to try using Ask Learn to clarify or guide you through this topic?

Ask Learn Ask Learn

 Suggest a fix?

* * *

Additional resources
--------------------

Training

Module

[Deploy and use Azure Container Registry - Training](https://learn.microsoft.com/en-us/training/modules/deploy-use-azure-container-registry/?source=recommendations)

Learn how to create a private registry service for building, storing, and managing container images and related artifacts.

Certification

[Microsoft Certified: Azure Administrator Associate - Certifications](https://learn.microsoft.com/en-us/credentials/certifications/azure-administrator/?source=recommendations)

Demonstrate key skills to configure, manage, secure, and administer key professional functions in Microsoft Azure.

* * *

* Last updated on 11/17/2025

In this article
---------------

1. [Prerequisites](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-using-azure-container-registry#prerequisites)
2. [Limitations](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-using-azure-container-registry#limitations)
3. [Configure registry authentication](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-using-azure-container-registry#configure-registry-authentication)
4. [Deploy container with Azure CLI](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-using-azure-container-registry#deploy-container-with-azure-cli)
5. [Deploy with Azure Resource Manager template](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-using-azure-container-registry#deploy-with-azure-resource-manager-template)
6. [Deploy with Azure portal](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-using-azure-container-registry#deploy-with-azure-portal)
7. [Next steps](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-using-azure-container-registry#next-steps)

Was this page helpful?

Yes No

No

Need help with this topic?

Want to try using Ask Learn to clarify or guide you through this topic?

Ask Learn Ask Learn

 Suggest a fix?

Ask Learn
---------

Preview

Ask Learn is an AI assistant that can answer questions, clarify concepts, and define terms using trusted Microsoft documentation.

Please sign in to use Ask Learn.

[Sign in](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-using-azure-container-registry#)

[English (United States)](https://learn.microsoft.com/en-us/locale?target=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fazure%2Fcontainer-instances%2Fcontainer-instances-using-azure-container-registry)

[Your Privacy Choices](https://aka.ms/yourcaliforniaprivacychoices)

Theme

* Light
* Dark
* High contrast

* [AI Disclaimer](https://learn.microsoft.com/en-us/principles-for-ai-generated-content)
* [Previous Versions](https://learn.microsoft.com/en-us/previous-versions/)
* [Blog](https://techcommunity.microsoft.com/t5/microsoft-learn-blog/bg-p/MicrosoftLearnBlog)
* [Contribute](https://learn.microsoft.com/en-us/contribute)
* [Privacy](https://go.microsoft.com/fwlink/?LinkId=521839)
* [Consumer Health Privacy](https://go.microsoft.com/fwlink/?linkid=2259814)
* [Terms of Use](https://learn.microsoft.com/en-us/legal/termsofuse)
* [Trademarks](https://www.microsoft.com/legal/intellectualproperty/Trademarks/)
* © Microsoft 2026
