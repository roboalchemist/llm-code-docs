# Source: https://developer.1password.com/docs/sdks

On this page

# 1Password SDKs

1Password SDKs allow you to build secrets management integrations that can programmatically access secrets stored in 1Password using Go, JavaScript, or Python. With 1Password SDKs, you can:

- [Securely load secrets](/docs/sdks/load-secrets/) from 1Password into your code with secret references.
- [Read, write, and update secrets](/docs/sdks/manage-items/) stored in 1Password, including passwords, API keys, and one-time passwords.
- [List items and vaults](/docs/sdks/list-vaults-items/) in a 1Password account.
- [Integrate with AI agents](/docs/sdks/ai-agent/).

## Supported languages[â€‹](#supported-languages "Direct link to Supported languages") 

[![Go SDK](/img/logos/go.png)![Go SDK](/img/logos/go.png) [Golang](https://github.com/1Password/onepassword-sdk-go)]

[![JS SDK](/img/logos/node.png)![JS SDK](/img/logos/node.png) [JavaScript](https://github.com/1Password/onepassword-sdk-js/)]

[![Python SDK](/img/logos/python.png)![Python SDK](/img/logos/python.png) [Python](https://github.com/1Password/onepassword-sdk-python/)]

## Supported functionality[â€‹](#supported-functionality "Direct link to Supported functionality") 

+-----------------------+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| Feature               | Supported functionality                                                           | Notes                                                                                   |
+=======================+===================================================================================+=========================================================================================+
| Secret references     | - [Load secrets](/docs/sdks/load-secrets)                                         | You can retrieve secrets from [supported field types](/docs/sdks/concepts#field-types). |
+-----------------------+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| Item management       | - [Create items](/docs/sdks/manage-items#create-an-item)                          | You can perform operations on [supported field types](/docs/sdks/concepts#field-types). |
|                       | - [Retrieve field values](/docs/sdks/manage-items#get-a-one-time-password)        |                                                                                         |
|                       | - [Retrieve items](/docs/sdks/manage-items#get-an-item)                           |                                                                                         |
|                       | - [Update items](/docs/sdks/manage-items#update-an-item)                          |                                                                                         |
|                       | - [Delete items](/docs/sdks/manage-items#delete-an-item)                          |                                                                                         |
|                       | - [Archive items](/docs/sdks/manage-items#archive-an-item)                        |                                                                                         |
|                       | - [Add & update tags](/docs/sdks/manage-items#create-an-item)                     |                                                                                         |
|                       | - [Manage autofill websites and behavior](/docs/sdks/manage-items#create-an-item) |                                                                                         |
|                       | - [Generate passwords](/docs/sdks/manage-items#generate-a-password)               |                                                                                         |
|                       | - [List items](/docs/sdks/list-vaults-items#list-items)                           |                                                                                         |
|                       | - [Share items](/docs/sdks/share-items/)                                          |                                                                                         |
|                       | - [Manage files](/docs/sdks/files/)                                               |                                                                                         |
+-----------------------+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| Vault management      | - [List vaults](/docs/sdks/list-vaults-items#list-vaults)                         |                                                                                         |
+-----------------------+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| Authentication        | - [1Password Service Accounts](/docs/service-accounts/get-started)                |                                                                                         |
+-----------------------+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+

## About the current version[â€‹](#about-the-current-version "Direct link to About the current version") 

1Password SDKs are currently in version 0, which means they can meet the stability and scalability requirements of production use cases. During version 0, expect more frequent releases as we add additional features and languages.

- There is a possibility of breaking changes when you upgrade from one version 0 release to another, for example 0.1.X to 0.2.0. Minor releases (0.1.X to 0.1.Y) will not include breaking changes.
- Integration authors may need to update their code when updating the SDK version. Existing code and integrations wonâ€™t be affected, as these will have the SDK pinned at a specific version via package.json (JS), requirements.txt (Python), or go.mod (Go).
- We will provide three months of support and security patches for version 0, so you can upgrade when it makes sense for your workflows and teams.

You can find information about the latest releases in the [1Password SDK release notes](https://releases.1password.com/developers/sdks/).

## Example integrations[â€‹](#example-integrations "Direct link to Example integrations") 

See examples of how our partners have used SDKs to build integrations with 1Password:

###  

**[![Go SDK](/img/logos/postman.svg)![Go SDK](/img/logos/postman.svg) [Postman](https://go.pstmn.io/1password)]**

Securely load API keys and other secrets stored in 1Password into Postman without exposing any secrets in plaintext.

[Learn more ](https://go.pstmn.io/1password)