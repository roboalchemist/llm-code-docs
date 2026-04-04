# Source: https://huggingface.co/docs/hub/enterprise-hub-tokens-management.md

# Tokens Management

> [!WARNING]
> This feature is part of the Team & Enterprise plans.

Tokens Management enables organization administrators to oversee access tokens within their organization, ensuring secure access to organization resources.

## Viewing and Managing Access Tokens

The token listing feature displays all access tokens within your organization. Administrators can:

- Monitor token usage and identify or prevent potential security risks:
  - Unauthorized access to private resources ("leaks")
  - Overly broad access scopes
  - Suboptimal token hygiene (e.g., tokens that have not been rotated in a long time)
- Identify and revoke inactive or unused tokens

    
    

Fine-grained tokens display their specific permissions:

    
    

## Token Policy

Enterprise organization administrators can enforce the following policies:

| **Policy**                                        | **Unscoped (Read/Write) Access Tokens** | **Fine-Grained Tokens**                                     |
| ------------------------------------------------- | --------------------------------------- | ----------------------------------------------------------- |
| **Allow access via User Access Tokens (default)** | Authorized                              | Authorized                                                  |
| **Only access via fine-grained tokens**           | Unauthorized                            | Authorized                                                  |
| **Do not require administrator approval**         | Unauthorized                            | Authorized                                                  |
| **Require administrator approval**                | Unauthorized                            | Unauthorized without an approval (except for admin-created) |

    
    

## Reviewing Token Authorization

When token policy is set to "Require administrator approval", organization administrators can review details of all fine-grained tokens accessing organization-owned resources and revoke access if needed. Administrators receive email notifications for token authorization requests.

When a token is revoked or denied, the user who created the token receives an email notification.

    
    

