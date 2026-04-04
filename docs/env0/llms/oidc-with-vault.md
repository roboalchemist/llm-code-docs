# Source: https://docs.envzero.com/guides/integrations/oidc-integrations/oidc-with-vault.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# OIDC for Vault

> Connect env zero to HashiCorp Vault using OIDC with JWT Authentication for secure secret retrieval

This guide is to help you connect to [Vault](https://www.vaultproject.io/) with OIDC.

## Overview

This guide will show you how to create a JWT Authentication Method, and how to configure env zero to utilize OIDC to authenticate to your vault cluster to retrieve secrets. Refer to [env zero's OIDC configuration](/guides/integrations/oidc-integrations).

We are going to follow the Vault documentation on how to create a [JWT Authentication](https://developer.hashicorp.com/vault/docs/auth/jwt#jwt-authentication)

## JWT Authentication Method

1. Login to your vault cluster
2. In the side navigation bar click on `Access`
3. Choose `Authentication Methods` in the left side menu
4. Click on the `Enable new method` button and it will open the Authentication method creation wizard
5. Choose `JWT`
6. Expand `Method Options` add a description and the relevant configuration and click on the `Enabled Method` button
7. In the `Configure JWT` page under the `Jwks url` enter `https://login.app.env0.com/.well-known/jwks.json`
8. Expand `JWT Options` and set the `Bound issuer` to be `https://login.app.env0.com/`
9. Click on the `Save` button

<Frame caption="Configure JWT">
  <img src="https://mintcdn.com/envzero-b61043c8/f50k_bxcw7fbjToJ/images/guides/integrations/oidc-integrations/configure_jwt.png?fit=max&auto=format&n=f50k_bxcw7fbjToJ&q=85&s=5d88b1ee6749d501a1115f71394e6f5b" alt="Vault JWT configuration interface showing OIDC authentication setup" width="1920" height="976" data-path="images/guides/integrations/oidc-integrations/configure_jwt.png" />
</Frame>

## Setup Secrets Store and Create Policy

Create a KV store in vault to save and fetch secrets.

```shell  theme={null}
vault secrets enable -path=secrets-for-env0/ kv
```

A policy needs to be created to define which secrets can be accessed. Here's an example:

```shell  theme={null}
vault policy write env0-access - <<EOF
path "secrets-for-env0/*" {
    capabilities = ["read", "create", "update"]
}
EOF
```

## Create Login Role

To create the role that binds the policy, `sub`, `aud` and env0 custom claims we will use the vault CLI. Make sure you have it installed on your machine and that you have access to vault. Export the following environment variables:

```shell  theme={null}
export ENV0_ORG_ID="your_env_zero_org_id"
export VAULT_ROLE_NAME="your_vault_role_name"
export VAULT_ADDR="your_vault_address_url"
export VAULT_NAMESPACE="your_vault_namespace" (optional)
export VAULT_TOKEN="your_vault_token"
```

Vault CLI uses the `VAULT_TOKEN` environment variable to authenticate but if you prefer, you can skip it and use `vault login` instead.

Now execute the following command to create the role:

```shell  theme={null}
vault write auth/jwt/role/$VAULT_ROLE_NAME - <<EOF
{
  "user_claim": "sub",
  "role_type": "jwt",
  "policies": ["env0-access"],
  "bound_audiences": ["https://prod.env0.com"],
  "bound_claims": {
    "organizationId": "$ENV0_ORG_ID",
    "apiKeyType": "oidc"
  }
}
EOF
```

<Note>
  More Claims

  In this example we only set the `aud`, the `organizationId` and the `apiKeyType` claims, however you can also set any additional claims you would like from the list of claims we support. The list is located [here](/guides/integrations/oidc-integrations/#format-of-the-openid-connect-id-token)
</Note>

## Authenticating to Vault with env zero Credential

Go to the organization's credentials page and create a new deployment credential. Select `Vault OIDC` type and enter the following fields:

* `Address` - The vault address, including port
* `Version`- The vault version to use
* `Role Name` - Vault role name
* `JWT Auth Backend Path` - Path to the new authentication method
* `Namespace`- Optional, the vault namespace

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/f50k_bxcw7fbjToJ/images/guides/integrations/oidc-integrations/d86ded4-image.png?fit=max&auto=format&n=f50k_bxcw7fbjToJ&q=85&s=6e8f53a71518bd48a8fffe13c0f562f6" alt="Interface screenshot showing configuration options" width="1126" height="1750" data-path="images/guides/integrations/oidc-integrations/d86ded4-image.png" />
</Frame>

After creating the credential you will need to go to the relevant project and assign that credential to the project in the project's credentials page. Now all environments within the project will have the relevant environment variables available.

## Authenticating to Vault with Terraform Provider

To configure the vault terraform provider all you need is the vault provider block and the `VAULT OIDC` deployment credentials set on the project. Example:

```hcl  theme={null}
provider "vault" {
  address          = var.vault_address
  skip_child_token = true # (depends on your role vault policy)
}
```

The `VAULT OIDC` deployment credentials are used to authenticate with the vault server along with the `ENV0_OIDC_TOKEN` JWT token which then sets the `VAULT_TOKEN` variable with the actual session token that is returned from the vault server used for authentication/authorization.

Built with [Mintlify](https://mintlify.com).
