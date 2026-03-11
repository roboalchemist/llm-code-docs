# Source: https://docs.anyscale.com/admin/azure/key-vault.md

# Use secrets from Azure Key Vault

[View Markdown](/admin/azure/key-vault.md)

# Use secrets from Azure Key Vault

This page provides an overview of configuring access to use secrets stored in Azure Key Vault.

note

AKS also supports using Key Vault as a Kubernetes secret store. See Azure docs [Use the Azure Key Vault provider for Secrets Store CSI Driver in an AKS cluster](https://learn.microsoft.com/en-us/azure/aks/csi-secrets-store-driver).

## Configure access to Azure Key Vault[​](#configure-access-to-azure-key-vault "Direct link to Configure access to Azure Key Vault")

Configure access to Azure Key Vault by adding roles to the managed identity used by your cluster. See [Configure managed identities for clusters on Anyscale on AKS](/admin/azure/aks-iam.md).

You must have sufficient privileges in your Azure account to assign roles to managed identities. Azure provides many tools for managing resources, including the [Azure Portal](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal) and [CLI](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-cli).

The following example demonstrates configuring read-only access to an Azure Key Vault from a managed identity.

### Requirements[​](#requirements "Direct link to Requirements")

This example has the following requirements:

* You have permission to assign roles in the target resource group, such as Role Based Access Control Administrator.
* You have created a managed identity configured as a service account in your AKS cluster and configured this for use with your Anyscale clusters. See [Configure managed identities for clusters on Anyscale on AKS](/admin/azure/aks-iam.md).
* You have created an Azure Key Vault and defined a secret.
* You have configured the Azure CLI on your machine.

### Step 1: Configure variables[​](#step-1-configure-variables "Direct link to Step 1: Configure variables")

Define the following variables for the Azure resources you need to configure relationships between.

```
export SUBSCRIPTION_ID="<your-subscription-id>"
export RESOURCE_GROUP="<your-resource-group-name>"
export MANAGED_ID_NAME="<your-user-assigned-managed-identity-name>"
export KEYVAULT_NAME="<your-keyvault-name>"
export SECRET_NAME="<your-secret-name>"
```

note

This example assumes your Key Vault and managed identity are in the same resource group.

Run the following command to validate that your secret exists:

```
az keyvault secret show --name "${SECRET_NAME}" --vault-name "${KEYVAULT_NAME}" --query value -o tsv
```

### Step 2: Get identifiers for Azure resources[​](#step-2-get-identifiers-for-azure-resources "Direct link to Step 2: Get identifiers for Azure resources")

Run the following command to set the resource ID for your Key Vault as an environment variable:

```
export KEYVAULT_RESOURCE_ID=$(az keyvault show \
    --resource-group "${RESOURCE_GROUP}" \
    --name "${KEYVAULT_NAME}" \
    --query id \
    --output tsv)
```

Run the following command to set the principal ID for your managed identity as an environment variable:

```
export PRINCIPAL_ID=$(az identity show \
  --name "${MANAGED_ID_NAME}" \
  --resource-group "${RESOURCE_GROUP}" \
  --query principalId \
  --output tsv)
```

#### Step 3: Assign the role to your managed identity[​](#step-3-assign-the-role-to-your-managed-identity "Direct link to Step 3: Assign the role to your managed identity")

Run the following command to assign the Key Vault Secrets User role to your managed identity for the specified Key Vault:

```
az role assignment create \
    --assignee-object-id "${PRINCIPAL_ID}" \
    --role "Key Vault Secrets User" \
    --scope "${KEYVAULT_RESOURCE_ID}" \
    --assignee-principal-type ServicePrincipal
```

## Use secrets from Azure Key Vault in Python[​](#use-secrets "Direct link to Use secrets from Azure Key Vault in Python")

Azure provides a Python SDK for interaction with Key Vault. Install the `azure-keyvault-secrets` package to use it on Anyscale.

important

Your Anyscale cluster must use a managed identity with sufficient privileges to connect to the target Azure Key Vault. See [Configure managed identities for clusters on Anyscale on AKS](/admin/azure/aks-iam.md).

You start by authenticating a client to your Key Vault, as in the following example:

```
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

key_vault_name = "my-key-vault"

kv_uri = f"https://{key_vault_name}.vault.azure.net"

credential = DefaultAzureCredential()
client = SecretClient(vault_url=kv_uri, credential=credential)
```

You then use the client to get secrets by name. Returned objects contain the value as a string stored using the `value` class variable. The following code demonstrates getting a secret and printing the value:

```
retrieved_secret = client.get_secret("secret-name")

print(retrieved_secret.value)
```
