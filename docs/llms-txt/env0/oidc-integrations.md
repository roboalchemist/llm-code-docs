# Source: https://docs.envzero.com/guides/integrations/oidc-integrations.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# General OIDC Integrations

> Configure OpenID Connect (OIDC) in env zero for short-lived token authentication with cloud providers

## Using OpenID Connect Tokens

[OpenID Connect](https://openid.net/connect/) (OIDC) allows your deployments to exchange short-lived tokens directly from your cloud provider. env zero provides an OIDC token (JWT) as an environment variable. A deployment can use this to access compatible cloud services without a long-lived credential stored in env zero.

## Enabling OIDC Token Availability

A JWT token could be available during deployment as an environment variable called `ENV0_OIDC_TOKEN`.

This feature can be enabled by selecting an OIDC credential when creating a credential in the organization's credentials page.\
In addition, organization admins can enable this feature by toggling the related checkbox in the organization's policies tab.

<img src="https://mintcdn.com/envzero-b61043c8/A22trGA9OCusm4S6/images/guides/integrations/0cce374-screen_shot_2022-08-05_at_13.png?fit=max&auto=format&n=A22trGA9OCusm4S6&q=85&s=da8c31ccf1a493144a16a05b2aa47c12" alt="" width="1405" height="503" data-path="images/guides/integrations/0cce374-screen_shot_2022-08-05_at_13.png" />

## Setting Up Your 3rd Party Service Integration

Consult your 3rd party service’s documentation for how to add an identity provider.\
For example, Vault’s [JWT Authentication](https://www.vaultproject.io/docs/auth/jwt#jwt-authentication), or [AWS’s Creating OpenID Connect (OIDC) identity providers](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html).

The OIDC token is unique to your organization. The custom claims attached to the token contain your organization ID. You can find your env zero organization ID by navigating to the Organization Settings page in our web app and copying the UUID from the URL.

In addition, the OpenID Connect ID tokens issued by env zero have a fixed audience (see `aud` in the table below).

## Format of the OpenID Connect ID token

The OpenID Connect ID token contains the following standard [claims](https://openid.net/specs/openid-connect-core-1_0.html#IDToken).

| Claims | Description                                                                                                                                                 |
| ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `iss`  | The issuer. The issuer is specific to env zero and the value is: `https://login.app.env0.com/`                                                              |
| `sub`  | The subject. It contains the user ID that represents your organization's OIDC user. If you like to get this ID please [contact us](mailto:support@env0.com) |
| `aud`  | The audience. This is a fixed string array value, containing URLs that identify env zero app domain: `https://prod.env0.com`                                |
| `iat`  | The time of issuance. This is when the token was created, which is shortly before the deployment starts.                                                    |
| `exp`  | The expiration time. Its value is 24 hours after the time of issuance.                                                                                      |

The OpenID Connect ID token also contains some additional custom claims that you should validate:

| Additional Claims | Description                                                                                                   |
| :---------------- | :------------------------------------------------------------------------------------------------------------ |
| `apiKeyType`      | The value should be `oidc`. Claim that the provided JWT should be from type `oidc` only                       |
| `organizationId`  | Unique organization ID                                                                                        |
| `projectId`       | Unique project ID                                                                                             |
| `projectName`     | Project name                                                                                                  |
| `templateId`      | Unique template ID                                                                                            |
| `templateName`    | Template name                                                                                                 |
| `environmentId`   | Unique environment ID                                                                                         |
| `environmentName` | Environment name                                                                                              |
| `workspaceName`   | Workspace name                                                                                                |
| `deploymentLogId` | Unique deployment ID                                                                                          |
| `deploymentType`  | Deployment type such as `deploy/destroy/prPlan/task` [etc](/api-reference/getting-started/authentication)'... |
| `deployerEmail`   | Email of the person that triggered the deployment                                                             |
| `env0Tag`         | Custom tag value (when `ENV0_OIDC_TAG` environment variable is set)                                           |

<Warning>
  Deprecated Additional Claims

  In addition to all the Custom Claims that are mentioned above, we also have all those claims with a prefix of `https://env0.com/` (for example: `https://env0.com/organizationId`)\
  Those claims are deprecated and will be removed in the future.
</Warning>

### Specific AWS Session Tags

In addition to the claims mentioned above, there is also a specific section for AWS tags inside a `https://aws.amazon.com/tags` and inside `principal_tags`:

| Additional Claims                                             | Description                                       |
| :------------------------------------------------------------ | :------------------------------------------------ |
| `https://aws.amazon.com/tags[principal_tags][organizationId]` | Unique organization ID                            |
| `https://aws.amazon.com/tags[principal_tags][projectId]`      | Unique project ID                                 |
| `https://aws.amazon.com/tags[principal_tags][templateId]`     | Unique template ID                                |
| `https://aws.amazon.com/tags[principal_tags][environmentId]`  | Unique environment ID                             |
| `https://aws.amazon.com/tags[principal_tags][deployerEmail]`  | Email of the person that triggered the deployment |
| `https://aws.amazon.com/tags[principal_tags][deploymentType]` | Deployment Type                                   |

Here is an example of a full JWT Token example:

```json  theme={null}
{
  "https://aws.amazon.com/tags": {
    "principal_tags": {
      "organizationId": [ "66a38abf-69bc-4cb7-ad73-7f61e389079f" ],
      "projectId": [ "5b44fa6d-ecfd-40ab-8e69-14d6fe7c638c" ],
      "templateId": [ "dc9808e2-44d3-48dd-b12a-31a08927ee6e" ],
      "environmentId": [ "9c3ca3cf-870d-4db4-9c60-5adf37faab45" ],
      "deployerEmail": [ "test@test.com" ],
      "deploymentType": [ "deploy" ],
      "env0Tag": [ "production-workload" ]
    }
  },
  "apiKeyType": "oidc",
  "organization": "66a38abf-69bc-4cb7-ad73-7f61e389079f",
  "organizationId": "66a38abf-69bc-4cb7-ad73-7f61e389079f",
  "projectId": "5b44fa6d-ecfd-40ab-8e69-14d6fe7c638c",
  "projectName": "Test Project",
  "templateId": "dc9808e2-44d3-48dd-b12a-31a08927ee6e",
  "templateName": "Test Tempalte",
  "environmentId": "9c3ca3cf-870d-4db4-9c60-5adf37faab45",
  "environmentName": "Dev Test Environment",   
  "workspaceName": "env09c3ca3",
  "deployerEmail": "test@test.com",
  "deploymentLogId": "96e2b169-5e4a-44a4-876b-4a5d26f4412c",  
  "deploymentType": "deploy",  
  "https://env0.com/apiKeyType": "oidc",
  "https://env0.com/organization": "66a38abf-69bc-4cb7-ad73-7f61e389079f",
  "https://env0.com/organizationId": "66a38abf-69bc-4cb7-ad73-7f61e389079f",
  "https://env0.com/projectId": "5b44fa6d-ecfd-40ab-8e69-14d6fe7c638c",
  "https://env0.com/projectName": "Test Project",
  "https://env0.com/templateId": "dc9808e2-44d3-48dd-b12a-31a08927ee6e",
  "https://env0.com/templateName": "Test Tempalte",
  "https://env0.com/environmentId": "9c3ca3cf-870d-4db4-9c60-5adf37faab45",
  "https://env0.com/environmentName": "Dev Test Environment",
  "https://env0.com/workspaceName": "env09c3ca3",  
  "https://env0.com/deploymentLogId": "96e2b169-5e4a-44a4-876b-4a5d26f4412c",
  "https://env0.com/deploymentType": "deploy",
  "https://env0.com/deployerEmail": "test@test.com",
  "https://env0.com/env0Tag": "production-workload",
  "env0Tag": "production-workload",
  "iss": "https://login.app.env0.com/",
  "sub": "auth0|63021f2ce98a11d0678ed6fe",
  "aud": "https://app.env0.com",
  "iat": 1685696926,
  "exp": 1685783326,
  "azp": "hoMiq9PdkRh9LUvVpH4wIErWg50VSG1b",
  "gty": "password"
}
```

### Custom Claims

You can add custom claims to the OIDC token by setting the `ENV0_OIDC_TAG` environment variable in env zero.

**Usage:**

* Set `ENV0_OIDC_TAG` as an environment variable in env zero
* The value will be included in the token as both `env0Tag` and `https://env0.com/env0Tag` claims
* For AWS integrations, it will also be included in the `https://aws.amazon.com/tags` principal\_tags

  **Example:**\
  If you set `ENV0_OIDC_TAG=production-workload`, the token will include:

```json  theme={null}
{
  "env0Tag": "production-workload",
  "https://env0.com/env0Tag": "production-workload",
  "https://aws.amazon.com/tags": {
    "principal_tags": {
      "env0Tag": ["production-workload"]
    }
  }
}
```

## JWT Verification

JWT signatures will be verified against public keys from the issuer.\
A *JSON Web Key Set* (**JWKS**) URL should be configured on your 3rd party service side.\
Keys will be fetched from this endpoint during authentication.\
Our **JWKS** URL is: `https://login.app.env0.com/.well-known/jwks.json`

Built with [Mintlify](https://mintlify.com).
