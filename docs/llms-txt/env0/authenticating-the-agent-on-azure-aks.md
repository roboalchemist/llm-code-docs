# Source: https://docs.envzero.com/guides/admin-guide/self-hosted-kubernetes-agent/authenticating-the-agent-on-azure-aks.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Authenticating the Agent On Azure AKS

> Authenticate env zero self-hosted agents on Azure AKS using workload identity and federated tokens

If your agent runs on an Azure AKS cluster, you can leverage the following method to assign an Azure AD identity to your env zero deployments.

## Using workload identity

You can associate an IAM role with a Kubernetes Service Account (KSA). The KSA that will be used by env zero is the `default` KSA under the `env0-agent` namespace.

You'll need to follow the Azure guide - [Deploy and configure workload identity on an Azure Kubernetes Service (AKS) cluster](https://learn.microsoft.com/en-us/azure/aks/workload-identity-deploy-cluster)  . The `SERVICE_ACCOUNT_NAMESPACE` will be `env0-agent` and the `SERVICE_ACCOUNT_NAME` will be `default`.

If you override these parameters in your installation, please make sure to use the correct values, i.e. pass the correct name of the service account to `deploymentJobServiceAccountName` within the agent's helm values.

Now, in order for the pods to use the identity, they should be labeled with `azure.workload.identity/use: "true"`. To achieve this, you need to add into the `podAdditionalLabels` field of your agent's helm values those field and value.

e.g.

```yaml values.customer.yaml theme={null}
"podAdditionalLabels": 
  "azure.workload.identity/use": "\"true\""
```

### Configuring Terraform Provider to use an AKS workload identity

Follow this official azurerm provider guide - [terraform registry documentation](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/aks_workload_identity#configuring-terraform-to-use-an-aks-workload-identity).

### Configuring Azure Backend to use an AKS workload identity

When configuring the Azure Backend, you need to make sure that the Client ID, Tenant ID, and OIDC are configured. You have to make sure to have the backend is configured as using OIDC, and with the OIDC token taken from the `AZURE_FEDERATED_TOKEN_FILE`

The are a couple of ways to do that:

1. In the backend configuration itself, make sure to set the following values:

```hcl  theme={null}
terraform {
  backend "azurerm" {
    resource_group_name  = "StorageAccount-ResourceGroup"                 # Can be passed via `-backend-config=`"resource_group_name=<resource group name>"` in the `init` command.
    storage_account_name = "abcd1234"                                     # Can be passed via `-backend-config=`"storage_account_name=<storage account name>"` in the `init` command.
    container_name       = "tfstate"                                      # Can be passed via `-backend-config=`"container_name=<container name>"` in the `init` command.
    key                  = "prod.terraform.tfstate"                       # Can be passed via `-backend-config=`"key=<blob key name>"` in the `init` command.
    use_oidc             = true                                           # Can also be set via `ARM_USE_OIDC` environment variable.
    oidc_token_file_path = "/var/run/secrets/azure/tokens/azure-identity-token" # Should be set to the value of AZURE_FEDERATED_TOKEN_FILE, usually "/var/run/secrets/azure/tokens/azure-identity-token"
    client_id            = "00000000-0000-0000-0000-000000000000"               # Can also be set via `ARM_CLIENT_ID` environment variable.
    subscription_id      = "00000000-0000-0000-0000-000000000000"          # Can also be set via `ARM_SUBSCRIPTION_ID` environment variable.
    tenant_id            = "00000000-0000-0000-0000-000000000000"          # Can also be set via `ARM_TENANT_ID` environment variable.
  }
}


```

1. Use environment variables to set `ARM_CLIENT_ID`to the client ID, `ARM_TENANT_ID` to the tenant ID, `ARM_USE_OIDC` to true, and `ARM_OIDC_TOKEN_FILE_PATH` to the value of `AZURE_FEDERATED_TOKEN_FILE` (usually "/var/run/secrets/azure/tokens/azure-identity-token")

Follow the official azure backend guide - [azure backend documentation](https://developer.hashicorp.com/terraform/language/settings/backends/azurerm#backend-azure-ad-service-principal-or-user-assigned-managed-identity-via-oidc-workload-identity-federation)

<Warning>
  You must set oidc\_token\_file\_path

  he official guide does not mention it, but if you do not provide the OIDC token explicitly, then the backend will ignore the `use_oidc` configuration. Unlike the azurerm Terraform Provider, which automatically picks up the token from `AZURE_FEDERATED_TOKEN_FILE`
</Warning>

### Access Key Vault secrets

If accessing sensitive values stored in Azure Key Vault is required during your deployments, you should also accomplish this optional step from the AKS guide - [Grant permissions to access Azure Key Vault](https://learn.microsoft.com/en-us/azure/aks/workload-identity-deploy-cluster#optional---grant-permissions-to-access-azure-key-vault)

### Verifying the cluster is configured properly

Once the cluster is configured for using the workload identity, you can run this command from a pod on it to validate all the correct parameters are exported correctly: `az login --service-principal -u $AZURE_CLIENT_ID -t $AZURE_TENANT_ID --federated-token $(cat $AZURE_FEDERATED_TOKEN_FILE)`.

The pod will need the correct labels for the namespace, service account, and `azure.workload.identity/use: "true"`.

If the command ran without error, you may also check the Key Vault access with the following command `az keyvault secret list --vault-name <YOUR VALUT NAME>`

Built with [Mintlify](https://mintlify.com).
