# Source: https://docs.anyscale.com/admin/azure/create-aks-cloud.md

# Deploy Anyscale on Azure Kubernetes Service (AKS)

[View Markdown](/admin/azure/create-aks-cloud.md)

## 1. Install Anyscale's python client package[​](#1-install-anyscales-python-client-package "Direct link to 1. Install Anyscale's python client package")

```
pip install -U anyscale
anyscale login # authenticate
```

## 2. Configure your Cloud Provider account[​](#2-configure-your-cloud-provider-account "Direct link to 2. Configure your Cloud Provider account")

```
az login
```

## 3. Terraform your Azure Account to create an AKS cluster[​](#3-terraform-your-azure-account-to-create-an-aks-cluster "Direct link to 3. Terraform your Azure Account to create an AKS cluster")

**Enter information about where you want to deploy your AKS cluster.**

Anyscale Cloud Namemy-aks-cloud

Azure Subscription IDxxxx-xxxx-xxxx

Azure RegionWest US

AKS Cluster Namemy-aks-cluster

Azure Tenant IDxxxx-xxxx-xxxx

Run the following commands to create an Anyscale Cloud with a basic AKS cluster.

```
git clone https://github.com/anyscale/terraform-kubernetes-anyscale-foundation-modules
cd terraform-kubernetes-anyscale-foundation-modules/examples/azure/aks-new_cluster/
```

Create and populate the Terraform variable file.

```
cat <<EOF > terraform.tfvars
aks_cluster_name = "<your_aks_cluster_name>"
azure_subscription_id = "<your_subscription_id>"
azure_tenant_id = "<your_tenant_id>"
azure_location = "<your_azure_region>"
EOF
```

note

The Terraform example enables GPU node pools (T4 and A100) by default. To customize or disable GPU pools, set `gpu_pool_configs` in `variables.tf` or in your `terraform.tfvars` (for example, use an empty map `{}` to disable GPU pools).

Apply the Terraform and wait for resources to be created. This may take a couple minutes.

```
terraform init
terraform plan
terraform apply
```

note

The Terraform output provides an example cloud registration command. Take note of the following outputs:

* Operator IAM principal ID (for `anyscale cloud register`)
* Operator IAM client ID (for the Helm install)
* Storage account name
* Container name

Provide information from the Terraform output:

Operator IAM Principal IDprincipal-id-from-terraform-output

Operator IAM Client IDanyscale-operator-client-id

Container Nameanyscale-container

Storage Account Nameanyscale-storage

## 4. Install additional AKS components[​](#4-install-additional-aks-components "Direct link to 4. Install additional AKS components")

note

Ensure that you are authenticated to the AKS cluster

Azure Resource Group Namemy-resource-group

```
az aks get-credentials --resource-group <azure_resource_group_name> --name <your_aks_cluster_name> --overwrite-existing
```

Install the Nginx ingress controller. The Terraform example repo includes a sample values file `sample-values_nginx.yaml`; use it or supply your own.

note

The Anyscale operator chart can optionally install the NGINX Ingress Controller as a dependency (`ingress-nginx.enabled: true` in Helm values). This guide follows the Terraform example and installs Nginx manually so you can use the example's values file.

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

(Optional) Install the Nvidia device plugin.

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

## 5. Register the Anyscale Cloud resources[​](#5-register-the-anyscale-cloud-resources "Direct link to 5. Register the Anyscale Cloud resources")

Run the command produced by the Terraform script. The command should look similar to the commands below. Verify all variables are entered correctly.

```
anyscale cloud register \
  --name <your_cloud_name> \
  --region <your_azure_region> \
  --provider azure \
  --compute-stack k8s \
  --azure-tenant-id <your_tenant_id> \
  --anyscale-operator-iam-identity <anyscale_operator_principal_id> \
  --cloud-storage-bucket-name 'abfss://<blob_storage_name>@<storage_account>.dfs.core.windows.net'
```

note

Take note of the Cloud Deployment ID in the output.

Cloud Resource IDcldrsrc\_1234

## 6. Install and deploy the Anyscale operator on your AKS cluster[​](#operator-helm-chart "Direct link to 6. Install and deploy the Anyscale operator on your AKS cluster")

In this step, you add the Anyscale operator Helm chart to your AKS cluster, create a `values.yaml` file that describes your cloud and Azure identity, and install the operator with Helm.

### Add the Anyscale operator Helm chart[​](#add-the-anyscale-operator-helm-chart "Direct link to Add the Anyscale operator Helm chart")

Run the following command to add the Anyscale operator Helm chart:

```
helm repo add anyscale https://anyscale.github.io/helm-charts
helm repo update anyscale
```

### Create a values YAML file[​](#create-a-values-yaml-file "Direct link to Create a values YAML file")

Create a `values.yaml` file. The following example uses the values you provided in earlier steps for a minimal Azure configuration.

```
global:
  cloudDeploymentId: <your_cloud_deployment_id>
  controlPlaneURL: https://console.azure.anyscale.com
  cloudProvider: azure
  auth:
    iamIdentity: <anyscale_operator_client_id>
    audience: api://086bc555-6989-4362-ba30-fded273e432b/.default

workloads:
  serviceAccount:
    name: anyscale-operator
```

If you want to customize the Helm chart to add custom Patches or additional pod shapes, see [Configure the Helm chart for the Anyscale operator](/k8s/configure-helm.md).

### Install the Anyscale operator on AKS[​](#install-the-anyscale-operator-on-aks "Direct link to Install the Anyscale operator on AKS")

Run the following command to install the Anyscale operator with Helm using your `values.yaml` file. Ensure you've added the Anyscale Helm repo (see [section 5](#operator-helm-chart)).

```
helm upgrade anyscale-operator anyscale/anyscale-operator \
  --namespace anyscale-operator \
  -f values.yaml \
  --create-namespace \
  --wait \
  -i
```

It may take several minutes for your Anyscale Cloud to be ready to use. You can watch the deployment status using the following command.

```
kubectl get deployments anyscale-operator -n anyscale-operator -w
```

## 8. Verify your Anyscale Cloud[​](#8-verify-your-anyscale-cloud "Direct link to 8. Verify your Anyscale Cloud")

After the operator is ready, verify that your cloud is registered and functional:

```
anyscale cloud verify --name <your_cloud_name>
```
