# Source: https://docs.anyscale.com/services/deploy.md

# Source: https://docs.anyscale.com/azure/deploy.md

# Deploy Anyscale on Azure

[View Markdown](/azure/deploy.md)

# Deploy Anyscale on Azure

This page provides an overview of deploying Anyscale on Azure.

This flow uses the Anyscale Terraform module to register a new AKS cluster and supporting Azure resources. See [Anyscale Terraform module for AKS](https://github.com/anyscale/terraform-kubernetes-anyscale-foundation-modules/tree/main/examples/azure/aks-new_cluster).

The Anyscale resource provider assumes that your AKS cluster and other Azure resources are in the same resource group and cloud region. The Anyscale Terraform module deploys an AKS cluster and resources fulfilling this expectation.

note

If you already have an AKS cluster you want to use, you can use the Anyscale resource provider to register an Anyscale cloud resource on top of your AKS deployment. Installing on an existing AKS deployment might require additional configuration. Contact [Anyscale support](mailto:support@anyscale.com) for assistance.

## Enroll in the private preview[​](#enroll-in-the-private-preview "Direct link to Enroll in the private preview")

Anyscale on Azure is an [Azure Native Integration](https://learn.microsoft.com/en-us/azure/partner-solutions/overview) in Private Preview. Anyscale and Microsoft develop this product in partnership. It includes a control plane hosted in Azure and unifies deployment, management, and monitoring in the Azure portal. To enroll, contact [Anyscale support](mailto:support@anyscale.com).

You provide the following details to Anyscale during enrollment:

* Your Azure subscription ID.
* The Azure regions where you want to deploy AKS.

important

Anyscale also supports configuring cloud resources using AKS in the AWS control plane. See [Deploy Anyscale on Azure Kubernetes Service (AKS)](/admin/azure/create-aks-cloud.md).

## Step 0: Configure Azure subscription for Anyscale[​](#configure-azure-subscription "Direct link to Step 0: Configure Azure subscription for Anyscale")

Before you can use the Anyscale resource provider, an Azure subscription owner must configure a trust relationship with the Anyscale control plane application and register Azure resource providers.

### Step 0a: Create an Azure service principal for Anyscale authentication[​](#azure-service-principal "Direct link to Step 0a: Create an Azure service principal for Anyscale authentication")

Anyscale uses Entra ID to sign tokens to validate the connection between your AKS deployment and the Anyscale control plane. Run the following command to create a trust relationship between your Azure subscription and the Anyscale application using an Azure service principal:

note

You need permission to create service principals for applications from other Entra tenants to do this. Many organizations restrict this role to the Azure subscription owner.

```
az ad sp create --id 086bc555-6989-4362-ba30-fded273e432b
```

See [Application and service principal objects in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity-platform/app-objects-and-service-principals).

### Step 0b: Register Azure resource providers[​](#register-resource-providers "Direct link to Step 0b: Register Azure resource providers")

Depending on how you choose to deploy and manage your Azure infrastructure, you might need to register Azure resource providers. Anyscale introduces the resource provider `Anyscale.Platform`, but all other resource providers might already be in use for your subscription if you're actively using AKS, Entra ID, and other Azure products.

You can see currently registered resource providers with the following query:

```
az provider list --query "[?registrationState=='Registered']" --output table
```

If you're using Terraform to manage your Azure infrastructure, run the following command to ensure all required resource providers are registered:

```
for provider in \
  Microsoft.Storage \
  Microsoft.ManagedIdentity \
  Microsoft.Authorization\
  Microsoft.Resources \
  Microsoft.Network \
  Microsoft.ContainerService\;
do
    az provider register --namespace "$provider"
done
```

note

You can choose to configure underlying Azure infrastructure using the Azure CLI, Azure portal, or other tools. These tools also require permissions to use these resource providers.

## Step 1: Use the Anyscale Terraform module[​](#terraform-module "Direct link to Step 1: Use the Anyscale Terraform module")

Anyscale provides a [Terraform module](https://github.com/anyscale/terraform-kubernetes-anyscale-foundation-modules/tree/main/examples/azure/aks-new_cluster) to complete a basic installation of AKS and other Azure resources needed to get started working with Anyscale. Anyscale recommends using this module to deploy your first Anyscale cloud resource on AKS.

### Step 1a: Authenticate the Azure CLI[​](#authenticate-azure-cli "Direct link to Step 1a: Authenticate the Azure CLI")

The Anyscale Terraform module uses your Entra ID privileges to deploy and configure resources in your Azure account. You need elevated privileges on the target Azure subscription to complete this step. Anyscale recommends one of the following roles on the target Azure subscription:

* Owner
* Azure account administrator
* Azure co-administrator

Azure resources created include the following:

* A resource group
* An AKS cluster
* A user-assigned managed identity
* A storage account and blob storage container

important

If you use an Azure service principal to deploy your Anyscale organization, you might not have any Azure users that can interact with the Anyscale console to invite additional users. Contact [Anyscale support](mailto:support@anyscale.com) and provide a list of users you need to add, indicating who should be the organization owner. The organization owner can add users from the Anyscale console. See [Manage users](/administration/organization/user-management.md).

As an admin user with the Azure CLI installed, run the following command from your local machine:

```
az login
```

note

Contact [Anyscale support](mailto:support@anyscale.com) if you need a full list of required privileges and resources created by the Terraform module.

### Step 1b: Clone the Terraform module[​](#clone-terraform-module "Direct link to Step 1b: Clone the Terraform module")

Create a directory on your local machine to contain all configuration assets related to your Anyscale cloud, such as Helm chart `values.yaml` files and the Terraform module. Use your local terminal to navigate to that directory and run the following command to clone the Anyscale Terraform module:

```
git clone https://github.com/anyscale/terraform-kubernetes-anyscale-foundation-modules
cd terraform-kubernetes-anyscale-foundation-modules/examples/azure/aks-new_cluster/
```

### Step 1c: Populate the Terraform variable file[​](#terraform-variable-file "Direct link to Step 1c: Populate the Terraform variable file")

In this step, you specify the desired name for AKS cluster, as well as your Azure subscription ID and the Azure region where you want to deploy your resources.

note

Provide the programmatic name for your desired region. See the [Azure regions list](https://learn.microsoft.com/en-us/azure/reliability/regions-list).

Run the following command to display your Azure tenant ID:

```
az account show --query tenantId -o tsv
```

The Terraform module uses the AKS cluster name you provide to programmatically create unique names for the resource group, storage account, and other Azure resources. Provide a name less than 40 characters in length. AKS names support alphanumeric characters, hyphens, and underscores.

Azure Subscription IDxxxx-xxxx-xxxx

Azure regionWest US 2

AKS cluster namemy-aks-cluster

Azure Tenant IDxxxx-xxxx-xxxx

Run the following command to create and populate a Terraform variable file:

```
cat <<EOF > terraform.tfvars
aks_cluster_name = "<your_aks_cluster_name>"
azure_subscription_id = "<your_subscription_id>"
azure_tenant_id = "<your_tenant_id>"
azure_location = "<your_azure_region>"
EOF
```

note

The Terraform example enables GPU node pools (T4 and A100) by default. To customize or disable GPU pools, set `gpu_pool_configs` in `variables.tf` or in your `terraform.tfvars`. For example, use an empty map `{}` to disable GPU pools.

### Step 1d: Apply the Terraform to create Azure resources[​](#apply-terraform "Direct link to Step 1d: Apply the Terraform to create Azure resources")

Run the following commands to use the variable file and your Azure credentials to deploy the resources needed for Anyscale on AKS:

```
terraform init
terraform plan
terraform apply
```

This command might take several minutes to complete.

Collect and enter the following values from your Terraform output:

Operator IAM Principal IDprincipal-id-from-terraform-output

Operator IAM Client IDclient-id-from-terraform-output

Container namemy-container

Storage account namemystorageaccount

Azure resource group namemy-resource-group

## Step 2: Use the Anyscale resource provider to configure an Anyscale cloud resource[​](#create-cloud-portal "Direct link to Step 2: Use the Anyscale resource provider to configure an Anyscale cloud resource")

In this step, you use the Anyscale resource provider in the Azure portal to configure an Anyscale cloud resource on AKS.

note

Anyscale recommends that the same admin user that ran the Terraform module completes the following steps.

### Step 2a: Navigate to the Private Preview UI in the Azure portal[​](#portal-private-preview-ui "Direct link to Step 2a: Navigate to the Private Preview UI in the Azure portal")

Navigate to the following URL to access the Private Preview for the Anyscale resource provider in the Azure portal: <https://aka.ms/anyscaleprivatepreview>.

A page with the title **Anyscale clouds** displays.

note

If you don't have access to this resource provider, your selected Azure tenant needs the Private Preview enabled. Contact [Anyscale support](mailto:support@anyscale.com).

### Step 2b: Create an Anyscale cloud resource[​](#create-cloud-resource "Direct link to Step 2b: Create an Anyscale cloud resource")

Complete the following steps to use the Azure portal to create an Anyscale cloud resource:

1. Click **Create**. The **Create Anyscale cloud** page appears with the **Basics** tab selected.

2. Confirm that the **Subscription** field matches the subscription you provided to Terraform.

3. In the **Resource group** field, enter the name of the resource group created by Terraform.

4. Enter a name for your Anyscale cloud in the **Cloud name** field.

   Anyscale cloud names must be unique in your Anyscale organization. Cloud names can only contain alphanumeric characters.

5. In the **Region** field, select the region you provided to Terraform.

6. Click **Next**. The **Cloud storage settings** tab appears.

7. In the **Cloud storage bucket endpoint** field, enter the following URI:

   ```
   https://<storage-account-name>.blob.core.windows.net
   ```

8. In the **Cloud storage bucket name** field, enter the following URI:

   ```
   abfss://<blob-container-name>@<storage-account-name>.dfs.core.windows.net
   ```

9. Click **Review + Create**. The **Review + Create** tab appears and validation on your provided information runs.

10. Click **Create**.

## Step 3: Update your Anyscale cloud configuration[​](#update-cloud-configuration "Direct link to Step 3: Update your Anyscale cloud configuration")

In this step, you authenticate to Anyscale, get details about your Anyscale cloud resource, and update your Anyscale cloud deployment to establish the auth relationship between the Anyscale control plane and the Anyscale operator deployed on your AKS cluster.

### Step 3a: Log in to Anyscale[​](#step-3a-log-in-to-anyscale "Direct link to Step 3a: Log in to Anyscale")

Use the Anyscale CLI to configure an API key for programmatic access. Anyscale uses Entra ID to manage all SSO for Anyscale on Azure.

1. Run the following command to install the Anyscale CLI:

   ```
   pip install anyscale
   ```

2. Run the following command to set the Azure control plane as the target for CLI operations in your current shell session:

   ```
   export ANYSCALE_HOST=https://console.azure.anyscale.com
   ```

3. Run the following commands to start the authentication flow:

   ```
   anyscale login
   ```

4. Complete the following steps to authenticate. Your authentication flow might differ slightly depending on your browser, terminal settings, and active Microsoft credentials.

   * Running `anyscale login` prints a URL starting with `https://console.azure.anyscale.com/otp/otp_` and a time-sensitive authorization hash. Your browser might automatically open a new tab. If not, open the URL in a browser tab.

   * Anyscale attempts to use the active Microsoft login for your browser session to authenticate.
     <!-- -->
     * If your screen displays **Log in to Anyscale command line interface**, click **Approve** and continue to [find your Anyscale cloud ID](#find-cloud-resource-id).

   * If prompted, click **Continue with Microsoft** and log in using the identity you used to deploy Anyscale from the Azure portal.

     <!-- -->

     * If you use multiple Microsoft logins, open a private browser window to sign in with the correct identity.
     * When you reach the Anyscale console homepage, you've successfully authenticated to Anyscale with Entra ID SSO, but you haven't authenticated the CLI.

   * Return to your terminal. Open the displayed URL. A page that displays **Log in to Anyscale command line interface** appears. Click **Approve**.

Login credentials last for seven days. You must set the environment variable `ANYSCALE_HOST=https://console.azure.anyscale.com` to target the Azure control plane. If you only use the Azure control plane for Anyscale, you can add this to your `.bashrc` or similar environment management file for all future sessions.

### Step 3b: Find your Anyscale cloud ID[​](#cloud-id "Direct link to Step 3b: Find your Anyscale cloud ID")

Use the Anyscale CLI to find the ID for your Anyscale cloud. Run the following command:

```
anyscale cloud list
```

Clouds in your Anyscale organization display with the newest first. Your cloud name includes the name of the Azure resource group and the value you provided to the **Cloud name** field while deploying your cloud with the Azure portal. Record the ID of your cloud:

Anyscale cloud IDcld\_12345

### Step 3c: Download and edit your cloud configuration[​](#step-3c-download-and-edit-your-cloud-configuration "Direct link to Step 3c: Download and edit your cloud configuration")

Run the following command to download your Anyscale cloud configuration:

```
anyscale cloud get --id <your_cloud_id> > cloud-config.yaml
```

Open the file. Record the cloud resource ID in the following field:

important

Cloud IDs start with `cld_` and cloud resource IDs start with `cldrsrc_`. Make sure you have recorded values correctly.

Cloud resource IDcldrsrc\_xxxxxx

Edit your cloud config YAML to add the service principal ID configured for the Anyscale operator. The following example is a cloud config with the required two lines added at the end:

```
name: <cloud-name>   # Your cloud name displays.
id: <your_cloud_id>
resources:
- cloud_resource_id: <anyscale-cloud-resource-id>
  name: default
  provider: AZURE
  compute_stack: K8S
  region: <your_azure_region>
  object_storage:
    bucket_name: abfss://<blob-container-name>@<storage-account-name>.dfs.core.windows.net
    endpoint: https://<storage-account-name>.blob.core.windows.net
  azure_config:
    tenant_id: <your_tenant_id>
kubernetes_config:
    anyscale_operator_iam_identity: <anyscale_operator_principal_id>
```

Save the file and run the following command to update your cloud:

```
anyscale cloud update --id <your_cloud_id> -f cloud-config.yaml
```

The console prints confirmation of the resources and fields the command updated.

note

If no update occurs, confirm that you edited and saved the file, then try again.

## Step 4: Deploy the Anyscale operator[​](#deploy-operator "Direct link to Step 4: Deploy the Anyscale operator")

In this step, you configure Helm chart values and install the Anyscale operator to your AKS cluster.

### Step 4a: Set up your local environment[​](#set-up-local-environment "Direct link to Step 4a: Set up your local environment")

You use Helm charts to install the Anyscale operator to your AKS cluster. You must have the following tools configured on your local machine:

* Azure CLI
* `kubectl`
* Helm

Run the following command to get credentials for your AKS cluster:

```
az aks get-credentials --resource-group <azure_resource_group_name> --name <your_aks_cluster_name> --overwrite-existing
```

Run the following command to install the Anyscale operator Helm chart:

```
helm repo add anyscale https://anyscale.github.io/helm-charts
helm repo update anyscale
```

### Step 4b: Install nginx-ingress[​](#install-nginx-ingress "Direct link to Step 4b: Install nginx-ingress")

Install the Nginx ingress controller. The Terraform example repo includes a sample values file `sample-values_nginx.yaml`. You can use this file or supply your own.

```
helm repo add nginx https://kubernetes.github.io/ingress-nginx
```

```
helm upgrade ingress-nginx nginx/ingress-nginx \
  --version 4.12.1 \
  --namespace ingress-nginx \
  --values sample-values_nginx.yaml \
  --create-namespace \
  --install
```

### Step 4c: Install the NVIDIA device plugin (optional)[​](#step-4c-install-the-nvidia-device-plugin-optional "Direct link to Step 4c: Install the NVIDIA device plugin (optional)")

If you intend to use NVIDIA GPUs in your Anyscale workloads, run the following commands:

```
helm repo add nvdp https://nvidia.github.io/k8s-device-plugin
```

```
helm upgrade nvdp nvdp/nvidia-device-plugin \
  --namespace nvidia-device-plugin \
  --version 0.17.1 \
  --values values_nvdp.yaml \
  --create-namespace \
  --install
```

### Step 4c: Define your Helm values YAML[​](#helm-values-yaml "Direct link to Step 4c: Define your Helm values YAML")

Create a `values.yaml` file on your local machine. Populate the file with the following:

```
global:
  auth:
    iamIdentity: <anyscale_operator_client_id>
    audience: api://086bc555-6989-4362-ba30-fded273e432b/.default
  cloudDeploymentId: <anyscale-cloud-resource-id>
  cloudProvider: azure
  controlPlaneURL: https://console.azure.anyscale.com
workloads:
  serviceAccount:
    name: anyscale-operator
```

### Step 4d: Install the Anyscale operator[​](#install-anyscale-operator "Direct link to Step 4d: Install the Anyscale operator")

Use the following field to provide a unique release name for your Anyscale operator.

Anyscale recommends using the name of your Anyscale cloud resource for the release name. This helps differentiate configurations when you're managing multiple Anyscale operators from the same local machine.

Helm release nameanyscale-operator

Run the following command to install the Anyscale operator:

```
helm install <release-name> anyscale/anyscale-operator \
  --namespace anyscale-operator \
  --create-namespace \
  --values values.yaml \
  --wait
```
