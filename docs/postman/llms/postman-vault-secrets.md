# Store secrets in your Postman Vault

_Postman Vault_ enables you to store sensitive data as vault secrets in your local instance of Postman. This enables you to securely reuse sensitive data in your HTTP collections and requests. Only you can access and use values associated with your vault secrets, and they aren't synced to the Postman cloud.

![Add secrets to Postman Vault](https://assets.postman.com/postman-docs/v11/add-postman-vault-secrets-v11-1.jpg)

## Access your Postman Vault

You can open your Postman Vault from the [Postman desktop app](/docs/getting-started/installation/installation-and-updates/) or the [Postman web app](/docs/getting-started/installation/installation-and-updates/#use-the-postman-web-app). To open your Postman Vault, open a workspace then select **Vault** from the Postman footer. You can also select **Control+Shift+V** or **Ctrl+Shift+V** to open your Postman Vault.

If this is your first time opening your Postman Vault, Postman generates your vault key when you open your Postman Vault. [Save your vault key](/docs/sending-requests/postman-vault/postman-vault-key/) to open your Postman Vault when you sign in to Postman again later.

You'll need to enter your vault key each time you sign in to Postman to open your Postman Vault. You can enter your vault key in the following ways, depending on how you saved your vault key:

* If you stored your vault key in your system's password manager, Postman gets your vault key and open your Postman Vault. If you're using the Postman web app, make sure you're using the [Postman Desktop Agent](/docs/getting-started/basics/about-postman-agent/#postman-desktop-agent) so Postman can get your vault key.
* If you chose not to store your vault key in your system's password manager, open your Postman Vault, manually enter your vault key, and select **Open Vault**.

Postman recommends you [use the latest version](/docs/getting-started/basics/about-postman-agent/#update-the-postman-desktop-agent) of the Postman Desktop Agent to receive recent changes and improvements.

## Vault secrets are deleted from your Postman Vault after signing out of Postman. Your vault secrets can't be recovered with your vault key. When you sign in to Postman and open your Postman Vault, you can add vault secrets back to your Postman Vault.

Once you've opened your Postman Vault, you can [add, edit, and use your vault secrets](#add-edit-and-use-vault-secrets).

## About vault secrets

*Vault secrets* are sensitive data, such as API keys and passwords, that you store in your Postman Vault and reuse in your local instance of Postman. Only you can access and reuse values associated with your vault secrets, and they aren't synced to the Postman cloud. Also your vault secrets are encrypted using Advanced Encryption Standard (AES) with a 256-bit key length.

Collaborators can see references to your vault secrets, such as `{{vault:postman-api-key}}`, in shared workspaces, enabling secure collaboration between teammates. API consumers can also see references to your vault secrets in public workspaces, enabling you to show an example of a secret. Collaborators and API consumers can add each vault secret to their Postman Vault with their own value.

If you're on an [Enterprise plan with the Advanced Security Administration add-on](https://www.postman.com/pricing/), you can link vault secrets with sensitive data stored in an external vault. Learn more about [Postman Vault integrations](#postman-vault-integrations).

Learn about Postman Vault [features that require the Postman desktop app](#feature-availability).

### Other options for storing and reusing values

You can use [variables](/docs/sending-requests/variables/variables/) to store and reuse the same value, such as URLs, in multiple places. Variables can be shared with teammates. While Postman Vault is highly recommended for storing sensitive data, you can use the following options to store sensitive data in variables:

* You can add sensitive data as a variable's [local value](/docs/sending-requests/variables/variables/#defining-variables) and make sure to never share the value with your teammates. You can learn more about [sharing a variable value](/docs/sending-requests/variables/variables/#share-variable-values) with your teammates.
* You can set the variable as [sensitive data](/docs/sending-requests/variables/variables/#set-a-value-as-sensitive-data) in global and environment variables, masking the value. This helps prevent you from unintentionally sharing the value during screen sharing or live streaming. Teammates who can access your workspace have permission to unmask the value.

## Manage your vault key

Save your vault key to open your Postman Vault when you sign in to Postman. Save or download your vault key to a secure location. You can store your vault key in your system's password manager, enabling Postman to automatically get your vault key when you sign in to Postman. Otherwise, you must manually enter your vault key each time you sign in to Postman. Note that your vault key isn't synced to the Postman cloud. Learn how to [save and manage your vault key](/docs/sending-requests/postman-vault/postman-vault-key/).

If you stored your vault key in your system's password manager and you're using the Postman web app, use the [Postman Desktop Agent](/docs/getting-started/basics/about-postman-agent/#postman-desktop-agent) so Postman can get your vault key.

Vault secrets are deleted from your Postman Vault after signing out of Postman. Your vault secrets can't be recovered with your vault key. When you sign in to Postman and open your Postman Vault, you can add vault secrets back to your Postman Vault.

## Add, edit, and use vault secrets

[Add vault secrets](/docs/sending-requests/postman-vault/manage-vault-secrets/#add-sensitive-data-as-vault-secrets) to your Postman Vault to reuse them in your local instance of Postman. Then you can [reference vault secrets](/docs/sending-requests/postman-vault/manage-vault-secrets/#use-vault-secrets) in your HTTP collections and requests, variables, and the Collection Runner.

You can also [use Guided Auth to add vault secrets](/docs/sending-requests/postman-vault/manage-vault-secrets-using-guided-auth/#add-authorization-as-vault-secrets-using-guided-auth) that have authentication credentials for public APIs. [Reference vault secrets added using Guided Auth](/docs/sending-requests/postman-vault/manage-vault-secrets-using-guided-auth/#use-vault-secrets-added-using-guided-auth) in your HTTP requests, and reuse your authentication credentials in new HTTP requests to the same public APIs.

The following shows some high-level differences between adding vault secrets without and with Guided Auth:

| Vault secrets | Vault secrets using Guided Auth |
| --- | --- |
| Stores any type of secret, such as API keys and passwords | Stores authentication credentials for public APIs in Postman |
| You can add vault secrets directly in Postman Vault | You must use Guided Auth to add vault secrets |
| Add vault secrets at any time | API publishers must set up Guided Auth for their public APIs |
| Postman doesn't suggest specific vault secrets | Postman suggests saved vault secrets for future requests to public APIs |
| Link vault secrets with external vaults | Can't link vault secrets with external vaults |

## Postman Vault integrations

Postman Vault integrations are available with Postman Enterprise plans with the Advanced Security Administration add-on.

Postman Vault integrations enable you to link vault secrets with secrets stored in an external vault. You can then reference vault secrets in your local instance of Postman, and retrieve the value of secrets stored in external vaults when you send HTTP requests. You can also [manage and update your Postman Vault integrations](/docs/sending-requests/postman-vault/manage-postman-vault-integrations/).

Postman supports the following Postman Vault integrations:

* [1Password](/docs/sending-requests/postman-vault/1password/)
* [AWS Secrets Manager](/docs/sending-requests/postman-vault/aws-secrets-manager/)
* [Azure Key Vault](/docs/sending-requests/postman-vault/azure-key-vault/)
* [HashiCorp Vault](/docs/sending-requests/postman-vault/hashicorp-vault/)

## Feature availability

The following features require the Postman desktop app:

* **Open Postman Vault from public workspaces** - You must use the Postman desktop app to open your Postman Vault from a [public workspace](/docs/collaborating-in-postman/using-workspaces/public-workspaces/), and reference vault secrets in a public workspace. If you're using the Postman web app, you must add new vault secrets to your Postman Vault if you're opening it from a public workspace.
* **Create and manage Postman Vault integrations** ([Enterprise teams only](https://www.postman.com/pricing/)) - You must use the Postman desktop app to [create and manage Postman Vault integrations](/docs/sending-requests/postman-vault/postman-vault-integrations/). If you're using the Postman web app, Postman Vault integrations won't be available.

## Troubleshoot vault secrets

To learn how to troubleshoot empty and unresolved vault secrets, see [Troubleshoot vault secrets](/docs/sending-requests/postman-vault/troubleshoot-vault-secrets/).