# Source: https://docs.snowflake.com/en/sql-reference/sql/create-network-policy.md

# CREATE NETWORK POLICY

Creates a network policy or replaces an existing network policy.

> **Note:**
>
> Only security administrators (i.e. users with the SECURITYADMIN role) or higher or a role with the global CREATE NETWORK POLICY
> privilege can create network policies.

See also:
:   [ALTER NETWORK POLICY](alter-network-policy.md) , [DROP NETWORK POLICY](drop-network-policy.md) , [SHOW NETWORK POLICIES](show-network-policies.md) , [DESCRIBE NETWORK POLICY](desc-network-policy.md)

    [ALTER ACCOUNT](alter-account.md)

## Syntax

```sqlsyntax
CREATE [ OR REPLACE ] NETWORK POLICY [ IF NOT EXISTS ] <name>
  [ ALLOWED_NETWORK_RULE_LIST = ( '<network_rule>' [ , '<network_rule>' , ... ] ) ]
  [ BLOCKED_NETWORK_RULE_LIST = ( '<network_rule>' [ , '<network_rule>' , ... ] ) ]
  [ ALLOWED_IP_LIST = ( [ '<ip_address>' ] [ , '<ip_address>' , ... ] ) ]
  [ BLOCKED_IP_LIST = ( [ '<ip_address>' ] [ , '<ip_address>' , ... ] ) ]
  [ COMMENT = '<string_literal>' ]
```

## Required parameters

`name`
:   Identifier for the network policy; must be unique for your account.

    The identifier value must start with an alphabetic character and cannot contain spaces or special characters unless the entire identifier
    string is enclosed in double quotes (for example, `"My object"`). Identifiers enclosed in double quotes are also case-sensitive.

    For more details, see [Identifier requirements](../identifiers-syntax.md).

## Optional parameters

`ALLOWED_NETWORK_RULE_LIST = ( 'network_rule' [ , 'network_rule' , ... ] )`
:   Specifies a list of [network rules](../../user-guide/network-rules.md) that contain the network identifiers that are allowed access to
    Snowflake. There is no limit on the number of network rules in the list.

`BLOCKED_NETWORK_RULE_LIST = ( 'network_rule' [ , 'network_rule' , ... ] )`
:   Specifies a list of network rules that contain the network identifiers that are denied access to Snowflake. There is no limit on the
    number of network rules in the list.

`ALLOWED_IP_LIST = ( [ ip_address ] [ , ip_address , ... ] )`
:   Specifies a list of IPv4 addresses that are allowed access to your Snowflake account. This is referred to as the *allowed list*.

    Snowflake recommends using network rules in conjunction with network policies rather than using this property. Use the
    `ALLOWED_NETWORK_RULE_LIST` property to specify network rules that contain IPv4 addresses.

    If you are not yet using network rules, specify at least one IPv4 address or CIDR block range to allow access to your Snowflake
    account. Additionally, if you are not using network rules and this property is specified with an empty list, no IPv4 addresses are
    allowed to access your Snowflake account.

`BLOCKED_IP_LIST = ( [ ip_address ] [ , ip_address , ... ] )`
:   Specifies a list of IPv4 addresses that are denied access to your Snowflake account. This is referred to as the *blocked list*.
    To unset this parameter, specify a different CIDR block range, a series of IPv4 addresses, or a single IPv4 address.

    Snowflake recommends using network rules in conjunction with network policies rather than using this parameter. Use the
    `BLOCKED_NETWORK_RULE_LIST` property to specify network rules that contain IPv4 addresses.

    To block public access, use a network rule and add the network rule to the `BLOCKED_NETWORK_RULE_LIST` property. The result is
    that only IP addresses that use private connectivity, such as AWS PrivateLink, can access your Snowflake account.

    Default: No value; no IP addresses in `ALLOWED_IP_LIST` property are blocked.

`COMMENT = 'string_literal'`
:   Specifies a comment for the network policy.

    Default: No value

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| CREATE NETWORK POLICY | Account | Only the SECURITYADMIN role, or a higher role, has this privilege by default. The privilege can be granted to additional roles as needed. |

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* Use network rules in conjunction with the network policy to manage access to your Snowflake account.
* You cannot execute a CREATE OR REPLACE NETWORK POLICY command to replace an existing network policy if that policy is currently assigned
  to an account, security integration, or user.
* Each `ip_address` can cover a range of addresses using Classless Inter-Domain Routing (CIDR) notation:

  > `ip_address[/optional_prefix_length]`

  For example:

  > `192.168.1.0/24`
* When a network policy includes values for both `ALLOWED_IP_LIST` and `BLOCKED_IP_LIST`, Snowflake applies the
  blocked list first.
* The maximum number of characters for the `ALLOWED_IP_LIST` list is 100,000. Snowflake returns an error message when this
  character limit is exceeded.
* After creating a network policy, you must associate it with your account before Snowflake enforces the policy. You can associate a
  policy with your account through the [ALTER ACCOUNT](alter-account.md) command, which must be run by a user with the SECURITYADMIN
  role (or higher).

  For example:

  > ```sqlexample
  > USE ROLE SECURITYADMIN;
  >
  > ALTER ACCOUNT SET NETWORK_POLICY = <policy_name>;
  > ```

  For more details, see [Parameter management](../../user-guide/admin-account-management.md). Note that [NETWORK_POLICY](../parameters.md) is currently the only account
  parameter that can be set by users with the SECURITYADMIN role.
* Before associating a network policy with your account, your current IP address must be included in `ALLOWED_IP_LIST`; otherwise,
  the ALTER ACCOUNT command returns an error. In addition, your current IP address cannot be included in `BLOCKED_IP_LIST`.
* Regarding metadata:

  > **Attention:**
  >
  > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).

* The OR REPLACE and IF NOT EXISTS clauses are mutually exclusive. They can’t both be used in the same statement.
* CREATE OR REPLACE *<object>* statements are atomic. That is, when an object is replaced, the old object is deleted and the new object is created in a single transaction.

## Example

Create a network policy named `allow_vpceid_block_public_policy` based on two network rules, one that allows a VPCE ID and one that
blocks public network traffic, as described in [Interaction between allowed lists and blocked lists](../../user-guide/network-policies.md).

```sqlexample
CREATE NETWORK POLICY allow_vpceid_block_public_policy
  ALLOWED_NETWORK_RULE_LIST = ('allow_vpceid_access')
  BLOCKED_NETWORK_RULE_LIST = ('block_public_access');

DESC NETWORK POLICY rule_based_policy;
```

```output
+---------------------------+---------------------+
| name                      | value               |
|---------------------------+---------------------|
| ALLOWED_NETWORK_RULE_LIST | ALLOW_VPCEID_ACCESS |
+---------------------------+---------------------+
| BLOCKED_NETWORK_RULE_LIST | BLOCK_PUBLIC_ACCESS |
+---------------------------+---------------------+
```
