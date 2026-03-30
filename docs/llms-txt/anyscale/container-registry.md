# Source: https://docs.anyscale.com/admin/azure/container-registry.md

# Configure Azure Container Registry

[View Markdown](/admin/azure/container-registry.md)

# Configure Azure Container Registry

This page provides an overview of configuring Azure Container Registry (ACR) for use with Anyscale cloud resources deployed on Azure Kubernetes Services (AKS).

## How does Anyscale integrate with Azure Container Registry?[​](#how-does-anyscale-integrate-with-azure-container-registry "Direct link to How does Anyscale integrate with Azure Container Registry?")

You configure a trust relationship between your AKS cluster and ACR using the kubelet managed identity. The kubelet uses these permissions to pull images to deploy Ray nodes using pods in your AKS cluster.

The Anyscale control plane and Anyscale operator don't have permissions to interact with ACR. You build and push images using tooling of your choice, such as Azure DevOps. You configure your AKS with read-only permissions to use ACR images.

## Add ACR permissions to an AKS cluster[​](#add-acr-permissions-to-an-aks-cluster "Direct link to Add ACR permissions to an AKS cluster")

You must have the Owner, Azure account administrator, or Azure co-administrator role in your Azure subscription to configure ACR for your AKS cluster.

Anyscale recommends using the following Azure CLI command to grant access to ACR from your AKS cluster:

```
az aks update --name <aks-cluster-name> --resource-group <acr-resource-group> --attach-acr <acr-name>
```

This command uses your credentials to add the `AcrPull` role to kubelet managed identity for your AKS cluster. All users that can deploy workloads on your Anyscale cloud can use the registry.

important

You must run this command again after updating your AKS cluster to make sure the newly created kubelet for the managed identity has permissions to pull from ACR.

## Use a custom image from ACR[​](#use-a-custom-image-from-acr "Direct link to Use a custom image from ACR")

Pass the fully qualified image URI using the `image_uri` field or `image-uri` parameter when configuring a workspace, job, or service.

ACR uses the following format for image URIs:

```
<registry-name>.azurecr.io/<repository-name>:<tag>
```

The following example uses the `--image-uri` flag to use an ACR image with an Anyscale job:

```
anyscale job submit -f job.yaml --image-uri myregistry.azurecr.io/ml/prod/recommender:v2 --ray-version 2.52.0
```
