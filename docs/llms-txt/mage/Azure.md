# Source: https://docs.mage.ai/production/deploying-to-cloud/secrets/Azure.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Azure Key Vault

### YAML

To use secrets in YAML files (e.g. in data integration pipelines):

1. Add the following keys and values to your environment variables so that
   Mage can access the Azure Key Vault:
   1. `AZURE_KEY_VAULT_URL`: The Azure Key Vault URI.
   2. `AZURE_CLIENT_ID`: Azure Active Directory [client ID](https://learn.microsoft.com/en-us/azure/active-directory/develop/msal-client-application-configuration#client-id).
   3. `AZURE_CLIENT_SECRET`: Azure Active Directory [client secret](https://learn.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app#add-a-client-secret).
   4. `AZURE_TENANT_ID`: Azure Active Directory [tenant ID](https://learn.microsoft.com/en-us/azure/azure-portal/get-subscription-tenant-id#find-your-azure-ad-tenant).
2. Store a secret in Azure Key Vault.
3. Use the following syntax in your YAML file to interpolate secret values from Azure Key Vault:

   ```yaml  theme={"system"}
   "{{ azure_secret_var('secret_name') }}"
   ```

   For example:

   ```yaml  theme={"system"}
   api_key: "{{ azure_secret_var('API_KEY') }}"
   access_token: "{{ azure_secret_var('ACCESS_TOKEN') }}"
   ```

### Python

Here is the example python code to get secrets from Azure Key Vault:

```python  theme={"system"}
from mage_ai.services.azure.key_vault.key_vault import get_secret

get_secret('secret_name')
```


Built with [Mintlify](https://mintlify.com).