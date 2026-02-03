# Source: https://docs.datadoghq.com/security/default_rules/5nr-ef7-a72.md

---
title: IAM User access keys should be created after initial setup
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > IAM User access keys should be created
  after initial setup
---

# IAM User access keys should be created after initial setup
 
## Description{% #description %}

AWS console defaults to no check boxes selected when creating a new IAM user. When creating the IAM user credentials, you have to determine what type of access they require.

**Programmatic access**: The IAM user might need to make API calls, use the AWS CLI, or use the Tools for Windows PowerShell. In that case, create an access key (access key ID and a secret access key) for that user.

**AWS Management Console access**: If the user needs to access the AWS Management Console, create a password for the user.

## Rationale{% #rationale %}

Requiring the additional steps be taken by the user for programmatic access after their profile has been created will give a stronger indication of intent that access keys are necessary for their work and once the access key is established on an account that the keys may be in use somewhere in the organization.

**Note**: Even if it is known the user will need access keys, require them to create the keys themselves or put in a support ticket to have them created as a separate step from user creation.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Log in to the AWS Management Console.
1. Click **Services**.
1. Click **IAM**.
1. Click **Users**.
1. Click **Security Credentials**.
1. As an Administrator
   - Click the **X (Delete)** for keys that were created at the same time as the user. profile but have not been used.
1. As an IAM User
   - Click the **X (Delete)** for keys that were created at the same time as the user. profile but have not been used.

### From the command line{% #from-the-command-line %}

```
aws iam delete-access-key --access-key-id <access-key-id-listed> --user-name <users-name>
```

## References{% #references %}

1. [https://docs.aws.amazon.com/cli/latest/reference/iam/delete-access-key.html](https://docs.aws.amazon.com/cli/latest/reference/iam/delete-access-key.html)
1. [https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html)

**Additional Information**: Credential report does not appear to contain "Key Creation Date".
