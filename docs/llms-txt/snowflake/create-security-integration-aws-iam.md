# Source: https://docs.snowflake.com/en/sql-reference/sql/create-security-integration-aws-iam.md

# CREATE SECURITY INTEGRATION (AWS IAM Authentication)

Creates a new security integration for external authentication using Amazon Web Services (AWS) Identity and Access Management (IAM).

For information about creating other types of security integrations (e.g. External OAuth), see [CREATE SECURITY INTEGRATION](create-security-integration.md).

See also:
:   [ALTER SECURITY INTEGRATION (AWS IAM Authentication)](alter-security-integration-aws-iam.md) , [DESCRIBE INTEGRATION](desc-integration.md) ,
    [DROP INTEGRATION](drop-integration.md) , [SHOW INTEGRATIONS](show-integrations.md)

## Syntax

```sqlsyntax
CREATE SECURITY INTEGRATION <name>
  TYPE = API_AUTHENTICATION
  AUTH_TYPE = AWS_IAM
  AWS_ROLE_ARN = '<iam_role_arn>'
  ENABLED = { TRUE | FALSE }
  [ COMMENT = '<string_literal>' ]
```

## Required parameters

`name`
:   Specifies the identifier (i.e. name) for the integration. This value must be unique in your account.

    For more details, see [Identifier requirements](../identifiers-syntax.md).

`TYPE = API_AUTHENTICATION`
:   Specifies that the security integration is an interface between Snowflake and one or more AWS services that use OAuth 2.0 or AWS IAM
    credentials.

`AUTH_TYPE = AWS_IAM`
:   Specifies that the integration uses AWS IAM to authenticate to one or more AWS services.

`AWS_ROLE_ARN = 'iam_role_arn'`
:   Specifies the Amazon Resource Name (ARN) of the AWS identity and access management (IAM) role that grants privileges for AWS resources.

`ENABLED = { TRUE | FALSE }`
:   Specifies whether this security integration is enabled or disabled.

    `TRUE`
    :   Allows the integration to run based on the parameters specified in the integration definition.

    `FALSE`
    :   Suspends the integration for maintenance. Any integration between Snowflake and a third-party service fails to work.

    The value is case-insensitive.

    The default is `TRUE`.

## Optional parameters

`COMMENT = 'string_literal'`
:   Specifies a comment for the integration.

    Default: No value

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| CREATE INTEGRATION | Account | Only the ACCOUNTADMIN role has this privilege by default. The privilege can be granted to additional roles as needed. |

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* Regarding metadata:

  > **Attention:**
  >
  > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).
* CREATE OR REPLACE *<object>* statements are atomic. That is, when an object is replaced, the old object is deleted and the new object is created in a single transaction.

## Examples

Create a security integration to connect Snowflake to AWS as the role named in AWS as `arn:aws:iam::001234567890:role/myrole`.

> ```sqlexample
> CREATE SECURITY INTEGRATION aws_iam
>   TYPE = API_AUTHENTICATION
>   AUTH_TYPE = AWS_IAM
>   AWS_ROLE_ARN = 'arn:aws:iam::001234567890:role/myrole'
>   ENABLED = true;
> ```
