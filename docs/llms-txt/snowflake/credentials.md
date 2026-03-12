# Source: https://docs.snowflake.com/en/sql-reference/account-usage/credentials.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# CREDENTIALS view

This Account Usage view includes a row for each credential used as a first or
[second factor](../../user-guide/security-mfa-second-factor.md) for authentication. This view includes rows for the following types
of credentials:

* [Programmatic access tokens](../../user-guide/programmatic-access-tokens.md)
* [Passkeys](../../user-guide/security-mfa-second-factor.md)
* [Time-based one-time passcodes (TOTPs)](../../user-guide/security-mfa-second-factor.md)
* [Workload identity federation](../../user-guide/workload-identity-federation.md)

> **Note:**
>
> This view does not include information about [Duo authenticators](../../user-guide/security-mfa-duo.md) (Duo push and passcodes).
>
> To determine if a user has configured Duo as a second factor for authentication, you can run the
> [SHOW MFA METHODS](../sql/show-mfa-methods.md) command.

This view does not include credentials that have been deleted.

## Columns

| Column | Data type | Description |
| --- | --- | --- |
| CREDENTIAL_ID | NUMBER | Internal/system-generated identifier for the credential. |
| NAME | VARCHAR | Name of the credential. |
| USER_NAME | VARCHAR | Name of the user associated with the credential. |
| TYPE | VARCHAR | Type of the credential. These types include:   *`PASSKEY`: [Passkey](../../user-guide/security-mfa-second-factor.md).* `PAT`: [Programmatic access token](../../user-guide/programmatic-access-tokens.md). *`TOTP`: [Time-based one-time passcode](../../user-guide/security-mfa-second-factor.md).* `AWS`: AWS Identity and Access Management (AWS IAM) is the identity provider, which indicates the workload is running on AWS. See   [Workload identity federation](../../user-guide/workload-identity-federation.md). *`AZURE`: Microsoft Entra ID is the identity provider, which indicates the workload is running on Microsoft Azure. See   [Workload identity federation](../../user-guide/workload-identity-federation.md).* `GCP`: Google Accounts is the identity provider, which indicates the workload is running on Google Cloud. See   [Workload identity federation](../../user-guide/workload-identity-federation.md). * `OIDC`: An OpenID Connect (OIDC) provider is the identity provider. See [Workload identity federation](../../user-guide/workload-identity-federation.md). |
| DOMAIN | VARCHAR | Domain of the credential. The domains include:   *`MFA_METHOD`: The credential is used as a   [second factor of authentication](../../user-guide/security-mfa-second-factor.md).* `PROGRAMMATIC_ACCESS_TOKEN`: [Programmatic access token](../../user-guide/programmatic-access-tokens.md). * `WORKLOAD_IDENTITY_FEDERATION_METHOD`: [Workload identity federation](../../user-guide/workload-identity-federation.md).   A given domain can have one or more possible types (specified in the TYPE column). |
| COMMENT | VARCHAR | Comment about the credential. |
| STATUS | VARCHAR | Status of the credential. The status depends on the value in the TYPE column:   *For `TYPE = 'PAT'` ([programmatic access tokens](../../user-guide/programmatic-access-tokens.md)), the status can be one   of the following:    + `ACTIVE`: The programmatic access token can be used to authenticate and has not expired yet.   + `EXPIRED`: The programmatic access token cannot be used to authenticate because the expiration date has passed.   + `DISABLED`: The programmatic access token is [disabled](../../user-guide/programmatic-access-tokens.md) because user login access is disabled or     the user is locked out of logging in.* For other types of credentials, the status can be one of the following:    + `PENDING`: The user started the enrollment process for an MFA method but has not completed the process. For example,     the user started registering an authenticator but never finished the setup process for the authenticator. As a result,     the MFA method is not considered to be valid yet.   + `ENROLLED`: The user has completed the enrollment process for the MFA method, and the MFA method can be used for     second-factor authentication. |
| ADDITIONAL_DETAILS | OBJECT | Additional details about the credential. The additional details depend on the type of the credential (the value in the TYPE column):   *For `TYPE = 'PAT'` ([programmatic access tokens](../../user-guide/programmatic-access-tokens.md)), the column contains   an [OBJECT](../data-types-semistructured.md) value with the following key-value pairs:    + For the `MINS_TO_BYPASS_NETWORK_POLICY_REQUIREMENT` key, the value is an integer representing the number of minutes     during which the [requirement of having a network policy](../../user-guide/programmatic-access-tokens.md) is bypassed. You can     specify this value when [generating the token](../../user-guide/programmatic-access-tokens.md).   + For the `ROLE_RESTRICTION` key, the value is an array of the roles that are used for privilege evaluation and     object creation during the session authenticated with this token. You can specify these roles when     [generating the token](../../user-guide/programmatic-access-tokens.md).   + For the `ROTATED_TO` key, the value is the name of the newer token that this token was replaced by during     [rotation](../../user-guide/programmatic-access-tokens.md). These key-value pairs are present only if the corresponding properties are set in the token. For example:  ```json   {     "MINS_TO_BYPASS_NETWORK_POLICY_REQUIREMENT":       60,     "ROLE_RESTRICTION": [       "MY_ROLE"     ],     "ROTATED_TO": "MY_PAT_NAME"   }```  If none of these are specified for the token, the column contains an empty object (`{}`).* For `TYPE = 'PASSKEY'` ([passkey](../../user-guide/security-mfa-second-factor.md)), the column contains   an [OBJECT](../data-types-semistructured.md) value with the key-value pair `aaguid`. For example:  ```json   {     "aaguid": "a12345678-..."   }``` *For `TYPE = 'TOTP'` ([time-based one-time passcode](../../user-guide/security-mfa-second-factor.md)), the column contains NULL.* For `TYPE = 'AWS'` ([workload identity federation](../../user-guide/workload-identity-federation.md)), the column contains   an [OBJECT](../data-types-semistructured.md) value with the following key-value pairs:    + For the `aws_partition` key, the value is the AWS partition for the federated identity.   + For the `aws_account` key, the value is the AWS account identifier for the federated identity.   + For the `type` key, the value is the type of the federated identity. This can be `IAM_USER` or `IAM_ROLE`.   + For the `iam_role` key, the value is the name of the federated IAM role or user. *For `TYPE = 'AZURE'` ([workload identity federation](../../user-guide/workload-identity-federation.md)), the column contains   an [OBJECT](../data-types-semistructured.md) value with the following key-value pairs:    + For the `issuer` key, the value is the Entra ID tenant’s Authority URL.   + For the `subject` key, the value is the Object ID (Principal ID) assigned to the Azure workload that is using a     managed identity.* For `TYPE = 'GCP'` ([workload identity federation](../../user-guide/workload-identity-federation.md)), the column contains   an [OBJECT](../data-types-semistructured.md) value with the following key-value pairs:    + For the `subject` key, the value is the `uniqueId` property of the Google Cloud service account associated with the     federated workload. * For `TYPE = 'OIDC'` ([workload identity federation](../../user-guide/workload-identity-federation.md)), the column contains   an [OBJECT](../data-types-semistructured.md) value with the following key-value pairs:    + For the `issuer` key, the value is the issuer URL of the OpenID Connect (OIDC) provider.   + For the `subject` key, the value is the identifier of the federated workload.   + For the `audience_list` key, the value is the custom audiences that are allowed in an OIDC ID token. An empty value means     the default audience `snowflakecomputing.com` is required. |
| CREATED_BY | VARCHAR | Name of the user who created the credential. |
| LAST_ALTERED_BY | VARCHAR | Name of the user who last modified the credential. |
| CREATED_ON | TIMESTAMP_LTZ | Date and time when the credential was created. |
| LAST_USED_ON | TIMESTAMP_LTZ | Date and time when the credential was last used for authentication. |
| LAST_ALTERED | TIMESTAMP_LTZ | Date and time when the credential was last modified. |
| EXPIRATION_DATE | TIMESTAMP_LTZ | Date and time when the credential expires. |

## Usage notes

* Latency for the view might be up to two hours.
* If a programmatic access token is generated soon after a user is created, the information about that user in this view might
  be incomplete. It might take some time for the user information to be included in the view.

## Examples

The following example returns rows for [programmatic access tokens](../../user-guide/programmatic-access-tokens.md):

```sqlexample
SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.CREDENTIALS WHERE type = 'PAT';
```

```output
+---------------+---------------+--------------+------+---------------------------+-------------------+--------+--------------------+--------------+-----------------+-------------------------+-------------------------+-------------------------+
| CREDENTIAL_ID | NAME          | USER_NAME    | TYPE | DOMAIN                    | COMMENT           | STATUS | ADDITIONAL_DETAILS | CREATED_BY   | LAST_ALTERED_BY | CREATED_ON              | LAST_USED_ON            | LAST_ALTERED            |
|---------------+---------------+--------------+------+---------------------------+-------------------+--------+--------------------+--------------+-----------------+-------------------------+-------------------------+-------------------------|
|      19464837 | EXAMPLE_TOKEN | EXAMPLE_USER | PAT  | PROGRAMMATIC_ACCESS_TOKEN | My token for APIs | ACTIVE | {}                 | EXAMPLE_USER | EXAMPLE_USER    | 2025-04-14 22:05:19.661 | 2025-04-14 22:05:19.661 | 2025-04-14 22:05:19.661 |
+---------------+---------------+--------------+------+---------------------------+-------------------+--------+--------------------+--------------+-----------------+-------------------------+-------------------------+-------------------------+
```
