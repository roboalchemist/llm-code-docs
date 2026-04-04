# Integrate Postman Vault with external vaults

**[Postman Vault integrations are available with Postman Enterprise plans with the Advanced Security Administration add-on.](https://www.postman.com/pricing/)**

You can integrate your [Postman Vault](/docs/sending-requests/postman-vault/postman-vault-secrets/) with external vaults, such as Azure Key Vault. This enables you to link vault secrets with secrets stored in an external vault. You can then reference vault secrets in your Postman team, and retrieve the value of secrets stored in external vaults when you send HTTP requests.

You can create Postman Vault integrations from the [Postman desktop app](/docs/getting-started/installation/installation-and-updates/).

Before you integrate your Postman Vault with external vaults, make sure you understand how to [add vault secrets to your Postman Vault](/docs/sending-requests/postman-vault/manage-vault-secrets/#add-sensitive-data-as-vault-secrets), and [reference vault secrets in Postman](/docs/sending-requests/postman-vault/manage-vault-secrets/#use-vault-secrets).

You can't create an integration that links [vault secrets created using Guided Auth](/docs/sending-requests/postman-vault/manage-vault-secrets-using-guided-auth/) with external vaults.

## About Postman Vault integrations

Postman Vault integrations enable you to link vault secrets with secrets that are stored in an external vault. You can then reference vault secrets in your Postman team, and retrieve the value of external vault secrets using end-to-end encryption when you send HTTP requests. Postman supports Postman Vault integrations with [1Password](https://1password.com/), [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/), [Azure Key Vault](https://azure.microsoft.com/en-us/products/key-vault/), and [HashiCorp Vault](https://www.hashicorp.com/en/products/vault).

Postman retrieves authentication credentials that enable you to authenticate with your external vault, such as a user access token. The type of authentication credentials that Postman retrieves can vary depending on the external vault you're authenticating with. Postman must authenticate with your external vault to retrieve secrets from it when you send HTTP requests.

Authentication credentials and retrieved secrets aren't stored in your local instance of Postman or the Postman cloud. Postman removes authentication credentials from your working memory and local storage when you close Postman or your authentication credentials expire.

You'll need to [reauthenticate with external vaults](/docs/sending-requests/postman-vault/manage-postman-vault-integrations/#reauthenticate-with-an-external-vault) each time you open Postman or when your authentication credentials expire in Postman. You'll need to create the integration again if you sign out and back in to Postman.

You can only integrate your Postman Vault with one organization in an external vault provider at a time. If you want to integrate with a different organization in your external vault provider, you must [disconnect the integration](/docs/sending-requests/postman-vault/manage-postman-vault-integrations/#disconnect-an-integration), then create a new integration that authenticates with a different organization. See the following details about creating and managing integrations with external vault providers:

* **1Password, AWS Secrets Manager, and Azure Key Vault** - You create and manage the integration with your Postman Vault. This means you and your team members can integrate with different organizations in 1Password, AWS Secrets Manager, and Azure Key Vault.
* **HashiCorp Vault** - Only a Postman [Team Admin or Super Admin](/docs/administration/roles-and-permissions/#team-roles) can create and manage the integration with your Postman Vault. This means that you and your team members must integrate with the same organization in HashiCorp.

External partners assigned the [Partner role](/docs/administration/roles-and-permissions/#partner-team-and-partner-workspace-roles) can't access Postman Vault integrations.

## Supported integrations

Postman supports the following Postman Vault integrations:

* [1Password](/docs/sending-requests/postman-vault/1password/)
* [AWS Secrets Manager](/docs/sending-requests/postman-vault/aws-secrets-manager/)
* [Azure Key Vault](/docs/sending-requests/postman-vault/azure-key-vault/)
* [HashiCorp Vault](/docs/sending-requests/postman-vault/hashicorp-vault/)

## Manage integrations

You can [manage and update your Postman Vault integrations](/docs/sending-requests/postman-vault/manage-postman-vault-integrations/). Set the expiration duration for cached secrets, change linked secrets, reauthenticate with your external vaults, and disconnect your integrations.

## Troubleshoot vault secrets

To learn how to troubleshoot vault secrets, see [Troubleshoot vault secrets](/docs/sending-requests/postman-vault/troubleshoot-vault-secrets/).