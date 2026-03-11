# Source: https://docs.anyscale.com/admin/azure/aks-iam.md

# Configure managed identities for clusters on Anyscale on AKS

[View Markdown](/admin/azure/aks-iam.md)

# Configure managed identities for clusters on Anyscale on AKS

This page describes how to use and manage service accounts with user-assigned managed identities for Anyscale cloud resources configured on Azure Kubernetes Service (AKS).

## What is the IAM model for Anyscale on AKS?[​](#what-is-the-iam-model-for-anyscale-on-aks "Direct link to What is the IAM model for Anyscale on AKS?")

The Anyscale control plane interacts with AKS service accounts through the Anyscale operator. You manage all identity and access management (IAM) for Anyscale workloads on AKS through service accounts.

AKS supports integration with Entra ID using many possible configurations. For the best performance on Anyscale, Anyscale recommends the following:

* Configure your AKS cluster to use workload identity and OIDC.
* Create user-assigned managed identities to manage role and permission assignments.
* Map a single user-assigned managed identity to each Kubernetes service account in your AKS cluster used by Anyscale.

See Azure docs for [Deploy and configure workload identity on an AKS cluster](https://learn.microsoft.com/en-us/azure/aks/workload-identity-deploy-cluster#update-an-existing-aks-cluster).

note

Anyscale also uses Entra ID to establish the trust relationship between the Anyscale control plane and your AKS cluster through your Anyscale operator.

When you register your AKS cloud resource to the Anyscale control plane, you include the Azure tenant ID and principal ID for the managed identity used by the Anyscale operator. Anyscale and the Anyscale operator use these credentials to validate a JSON Web Token (JWT) vended by Entra ID, then use the JWT to authenticate communication between the control plane and Anyscale operator.

## AKS service accounts and managed identities used by Anyscale[​](#aks-service-accounts-and-managed-identities-used-by-anyscale "Direct link to AKS service accounts and managed identities used by Anyscale")

You create and annotate AKS service accounts to add a trust relationship with a user-assigned managed identity. This annotation provides Ray nodes in your Anyscale cluster access to resources in your cloud provider account, such as the default Azure storage container configured during your cloud deployment.

The following table describes the managed identities you need to configure for Anyscale:

| Term                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Anyscale operator managed identity | When you deploy an Anyscale cloud on AKS, you configure a Kubernetes service account for the Anyscale operator that maps to an Azure user-assigned managed identity.The permissions in this managed identity govern all actions that the Anyscale operator can take in your Azure account. The Anyscale operator is responsible for processing all instructions from the Anyscale control plane to deploy nodes for Ray clusters in your AKS cluster.                                                                                                                                                     |
| Cluster managed identity           | When you configure the Anyscale operator for your Anyscale cloud on AKS, you configure a default Kubernetes service account that maps to an Azure user-assigned managed identity. When the Anyscale operator deploys a new cluster or autoscales to add worker nodes, the Pods use this service account and assume the managed identity to gain access to necessary resources in your cloud provider account.You must define a Kubernetes service account and managed identity for each unique set of IAM permissions you want to assign to a given user, workload, or project through cloud IAM mapping. |

## View cluster service account and managed identity[​](#view-cluster-service-account-and-managed-identity "Direct link to View cluster service account and managed identity")

Run the following commands to find the Kubernetes service account in use for Pods in your Anyscale cluster:

```
# Define your AKS namespace.
NAMESPACE="<your-anyscale-namespace>"

# Get all Pods and manually identify your Pod.
kubectl get pods -n ${NAMESPACE} | grep k-

# Define a variable for your Pod name.
POD_NAME="<your-pod-name>"

# Get the Kubernetes service account name used by your Pod.
kubectl get pod ${POD_NAME} -n ${NAMESPACE} -o jsonpath='{.spec.serviceAccountName}'
```

To see the Azure managed identity used by your Kubernetes service account, run the following command:

```
kubectl get serviceaccount "<your-kubernetes-service-account>" -n "${NAMESPACE}" \
  -o jsonpath='{.metadata.annotations.azure\.workload\.identity/client-id}{"\n"}'
```

## Create and map an AKS cluster managed identity[​](#create-and-map-an-aks-cluster-managed-identity "Direct link to Create and map an AKS cluster managed identity")

To create a new cluster managed identity, you annotate a Kubernetes service account with an Azure user-assigned managed identity. You add roles and permissions to the managed identity to grant access to additional resources in your cloud provider account, such as blob storage containers.

note

Use cloud IAM mapping to control how Anyscale assigns cluster managed identities based on user identity, workload type, or project.

You must create and annotate a Kubernetes service account for each unique managed identity you need to assign to Anyscale clusters. See [Anyscale cloud IAM mapping](/iam/cloud-iam-mapping.md).

Complete the following steps to annotate an AKS service account.

### Requirements[​](#requirements "Direct link to Requirements")

The following instructions assume the following:

* You have created an AKS cluster and registered it as an Anyscale cloud resource.
* You have installed and authenticated the Azure CLI.
* You have installed and configured `kubectl` for your AKS cluster.
* You have enabled workload identity and the OIDC issuer on your AKS cluster.

### Step 0: Identify or create a managed identity[​](#step-0-identify-or-create-a-managed-identity "Direct link to Step 0: Identify or create a managed identity")

Identify or create the user-assigned managed identity you need to attach to your AKS cluster.

For Anyscale to operate correctly, your managed identity must have the Storage Blob Data Contributor role on the storage account configured as default storage for your Anyscale cloud resource.

important

You use the client ID for the managed identity to configure the trust relationship with AKS.

You define your managed identity name as a variable in the next step and use the Azure CLI to get the client ID.

### Step 1: Configure variables[​](#step-1-configure-variables "Direct link to Step 1: Configure variables")

The following commands configure variables that describe your Azure account, AKS cluster, and Anyscale account. Replace the variables denoted with `<>` before running these commands. For example, replace `<your-aks-cluster-name>` with the name of your AKS cluster.

note

You can save and run these commands as a `.sh` script, or run each command sequentially from the command line.

```
#!/bin/bash

# Specify the namespace for Anyscale in your AKS cluster.
# Anyscale uses 'anyscale-operator' as the default AKS namespace.
export NAMESPACE="<your-anyscale-namespace>"

# Specify the name of your AKS cluster and the Azure resource group containing it.
export AKS_CLUSTER_NAME="<your-aks-cluster-name>"
export RESOURCE_GROUP_NAME="<your-resource-group-name>"

# Define the name for a new service account.
export SERVICE_ACCOUNT_NAME="<your-service-account-name>"

# Specify the name of managed identity to use with the service account.
export MANAGED_IDENTITY_NAME="<your-managed-identity-name>"
 
# Specify the client ID for the managed identity.
export MANAGED_IDENTITY_CLIENT_ID=az identity show \
  --resource-group "${RESOURCE_GROUP_NAME}" \
  --name "${MANAGED_IDENTITY_NAME}" \
  --query 'clientId' \
  --output tsv
```

### Step 2: Show current service accounts[​](#step-2-show-current-service-accounts "Direct link to Step 2: Show current service accounts")

Run the following commands to list all service accounts present in your namespace:

```
az aks get-credentials --resource-group $RESOURCE_GROUP_NAME --name $AKS_CLUSTER_NAME;
kubectl get serviceaccounts -n ${NAMESPACE}
```

note

You can review service accounts currently registered for Anyscale cloud IAM mapping in the Anyscale console or using the CLI. See [Anyscale cloud IAM mapping](/iam/cloud-iam-mapping.md).

### Step 3: Create a Kubernetes service account[​](#step-3-create-a-kubernetes-service-account "Direct link to Step 3: Create a Kubernetes service account")

Run the following command to create a Kubernetes service account in the namespace of your AKS cluster:

```
kubectl create serviceaccount "${SERVICE_ACCOUNT_NAME}" -n "${NAMESPACE}" \
  --dry-run=client -o yaml | kubectl apply -f -
```

### Step 4: Annotate the Kubernetes service account[​](#step-4-annotate-the-kubernetes-service-account "Direct link to Step 4: Annotate the Kubernetes service account")

Run the following command to annotate the AKS service account with the managed identity client ID:

```
kubectl annotate serviceaccount "${SERVICE_ACCOUNT_NAME}" -n "${NAMESPACE}" \
  azure.workload.identity/client-id="${MANAGED_IDENTITY_CLIENT_ID}" --overwrite
```

### Step 5: Establish the federated trust relationship[​](#step-5-establish-the-federated-trust-relationship "Direct link to Step 5: Establish the federated trust relationship")

Create a federated identity credential between the user-assigned managed identity and Microsoft Entra ID, linking it to the Kubernetes service account.

Start by getting the OIDC issuer URL for your AKS cluster:

```
export AKS_OIDC_ISSUER="$(az aks show --name "${AKS_CLUSTER_NAME}" \
    --resource-group "${RESOURCE_GROUP_NAME}" \
    --query "oidcIssuerProfile.issuerUrl" \
    --output tsv)"
```

Then run the following command to link your managed identity with the AKS service account in Entra ID:

```
export FEDERATED_IDENTITY_CREDENTIAL_NAME="${SERVICE_ACCOUNT_NAME}-fc"
az identity federated-credential create \
    --name "${FEDERATED_IDENTITY_CREDENTIAL_NAME}" \
    --identity-name "${MANAGED_IDENTITY_NAME}" \
    --resource-group "${RESOURCE_GROUP_NAME}" \
    --issuer "${AKS_OIDC_ISSUER}" \
    --subject system:serviceaccount:"${NAMESPACE}":"${SERVICE_ACCOUNT_NAME}" \
    --audience api://AzureADTokenExchange
```

### Step 6: Verify the annotation[​](#step-6-verify-the-annotation "Direct link to Step 6: Verify the annotation")

Run the following command to display the annotation field of your service account:

```
kubectl get serviceaccount "${SERVICE_ACCOUNT_NAME}" -n "${NAMESPACE}" \
  -o jsonpath='{.metadata.annotations.azure\.workload\.identity/client-id}{"\n"}'
```

The managed identity client ID you assigned to the service account displays.

### Step 7: Register the service account with Anyscale[​](#step-7-register-the-service-account-with-anyscale "Direct link to Step 7: Register the service account with Anyscale")

Each Anyscale cloud resource has a default service account used by all clusters. To use your new service account as the default, update the `workloads.serviceAccount.name` setting in your Helm chart with name of your service account and update your Anyscale operator.

Anyscale recommends using cloud IAM mapping to scope service accounts to users, projects, and workloads for more fine-grained access controls. Cloud owners can define cloud IAM mapping rules in the Anyscale console or using the CLI. See [Anyscale cloud IAM mapping](/iam/cloud-iam-mapping.md).
