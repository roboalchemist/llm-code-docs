# Source: https://docs.snowflake.com/en/sql-reference/sql/create-network-rule.md

# CREATE NETWORK RULE

Creates a network rule or replaces an existing network rule.

See also:
:   [ALTER NETWORK RULE](alter-network-rule.md) , [DROP NETWORK RULE](drop-network-rule.md) , [SHOW NETWORK RULES](show-network-rules.md) ,
    [DESCRIBE NETWORK RULE](desc-network-rule.md)

## Syntax

```sqlsyntax
CREATE [ OR REPLACE ] NETWORK RULE <name>
   TYPE = { IPV4 | AWSVPCEID | AZURELINKID | GCPPSCID | HOST_PORT | PRIVATE_HOST_PORT }
   VALUE_LIST = ( '<value>' [, '<value>', ... ] )
   MODE = { INGRESS | INTERNAL_STAGE | EGRESS }
   [ COMMENT = '<string_literal>' ]
```

## Required parameters

`name`
:   Identifier for the network rule.

    The identifier value must start with an alphabetic character and cannot contain spaces or special characters unless the entire identifier
    string is enclosed in double quotes (e.g. `"My object"`). Identifiers enclosed in double quotes are case-sensitive.

    For more details, see [Identifier requirements](../identifiers-syntax.md).

`TYPE = { IPV4 | AWSVPCEID | AZURELINKID | GCPPSCID | HOST_PORT | PRIVATE_HOST_PORT }`
:   Specifies the type of network identifiers being allowed or blocked. A network rule can have only one type.

    * `IPV4` indicates that the network rule will allow or block network traffic based on the IPv4 address of the request origin.
    * `AWSVPCEID` indicates that the network rule will allow or block network traffic over
      [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html).
    * `AZURELINKID` indicates that the network rule will allow or block network traffic over
      [Azure Private Link](https://learn.microsoft.com/en-us/azure/private-link/private-link-overview).
    * `GCPPSCID` indicates that the network rule will allow or block network traffic over
      [Google Cloud Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect#endpoints).
    * `HOST_PORT` indicates that the network rule will allow outgoing network traffic based on the domain of the request destination.

      When `TYPE = HOST_PORT`, the `MODE` parameter should be set to `EGRESS`.
    * `PRIVATE_HOST_PORT` indicates that the network rule allows outgoing network traffic to use
      [private connectivity](../../user-guide/private-connectivity-outbound.md) to an external network location.

      When `TYPE = PRIVATE_HOST_PORT`, the `MODE` parameter must be set to `EGRESS`.

`VALUE_LIST = ( 'value' [, 'value', ... ] )`
:   Specifies the network identifiers that will be allowed or blocked.

    Valid values in the list are determined by the type of network rule:

    > * When `TYPE = IPV4`, each value must be a valid IPv4 address or [range of addresses](alter-network-rule.md).
    > * When `TYPE = AWSVPCEID`, each value must be a valid VPCE ID. VPC IDs are not supported.
    > * When `TYPE = AZURELINKID`, each value must be a valid LinkID of an Azure [private endpoint](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview).
    >   Execute the [SYSTEM$GET_PRIVATELINK_AUTHORIZED_ENDPOINTS](../functions/system_get_privatelink_authorized_endpoints.md) function to retrieve the LinkID associated
    >   with an account.
    > * When `TYPE = GCPPSCID`, each value must be a valid pscConnectionID of a [Google Cloud Private Service Connect (PSC) endpoint](https://docs.cloud.google.com/vpc/docs/private-service-connect#endpoints). Run the [gcloud compute forwarding-rules describe command](https://docs.cloud.google.com/memorystore/docs/cluster/multiple-vpcs-automatically-registered-psc-connection#get_the_connection_id_1) to get the pscConnectionID for each forwarding rule.
    > * When `TYPE = HOST_PORT`, each value must resolve to a valid domain. Optionally, it can also include a port or range of ports.
    >
    >   In most cases, the valid port range is 1-65535. If you do not specify a port, it defaults to 443. If an external network location supports dynamic ports, you need to specify all possible ports.
    >
    >   To allow access to all ports, define the port as 0; for example, `example.com:0`.
    >
    >   When the value resolves to a domain, you can use a single asterisk as a wildcard character. The asterisk matches only alphanumeric
    >   characters and hyphens (`-`).
    >
    >   Wildcards are supported only for a single level of subdomains, as in the following examples:
    >
    >   + `*.google.com`
    >   + `snowflake-*.google.com` and `snowflake*abc.google.com`
    >
    >   You can allow requests to all outbound endpoints by specifying `0.0.0.0` as the domain, as in the examples below.
    >   When you specify `0.0.0.0` as the domain, you may use only 443 and 80 as port values.
    >
    >   + Allow access to all endpoints at port 80
    >
    >     ```none
    >     value_list = ('0.0.0.0:80');
    >     ```
    >   + Allow access to all endpoints at port 443
    >
    >     ```none
    >     value_list = ('0.0.0.0:443');
    >     ```
    >
    >     ```none
    >     value_list = ('0.0.0.0');
    >     ```
    >   + Allow access to all endpoints at both port 80 and 443
    >
    >     ```none
    >     value_list = ('0.0.0.0:80', '0.0.0.0:443');
    >     ```
    > * When `TYPE = PRIVATE_HOST_PORT`, specify one valid domain.
    >
    >   In most cases, the valid port range is 1-65535. If you do not specify a port, it defaults to 443. If an external network location supports dynamic ports, you need to specify all possible ports.
    >
    >   To allow access to all ports, define the port as 0; for example, `example.com:0`.

`MODE = { INGRESS | INTERNAL_STAGE | EGRESS }`
:   Specifies what is restricted by the network rule.

    `INGRESS`
    :   The behavior of the `INGRESS` mode depends on the value of the network rule’s `TYPE` property.

        * If `TYPE=IPV4`, by default the network rule controls access to the Snowflake service only.

          If the account administrator enables the [ENFORCE_NETWORK_RULES_FOR_INTERNAL_STAGES](../parameters.md) parameter, then `MODE=INGRESS` and
          `TYPE=IPV4` also protects an AWS internal stage.
        * If `TYPE=AWSVPCEID`, `TYPE=AZURELINKID`, or `TYPE=GCPPSCID`,then the network rule controls access to the Snowflake service only.

    `INTERNAL_STAGE`
    :   Allows or blocks requests to an AWS internal stage without restricting access to the Snowflake service. Using this mode requires the
        following:

        * The account administrator must enable the [ENFORCE_NETWORK_RULES_FOR_INTERNAL_STAGES](../parameters.md) parameter.
        * The `TYPE` property of the network rule must be `AWSVPCEID`.

    `EGRESS`
    :   Allows Snowflake to send requests to an external destination.

    Default: `INGRESS`

## Optional parameters

`COMMENT = 'string_literal'`
:   Specifies a comment for the network rule.

    Default: No value

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| CREATE NETWORK RULE | Schema | Only the ACCOUNTADMIN and SECURITYADMIN roles, along with the schema owner, have this privilege by default. It can be granted to additional roles as needed. |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* When specifying IP addresses for a network rule, Snowflake supports ranges of IP addresses using [Classless Inter-Domain Routing (CIDR) notation](https://tools.ietf.org/html/rfc4632).

  For example, `192.168.1.0/24` represents all IPv4 addresses in the range of `192.168.1.0` to `192.168.1.255`.
* CREATE OR REPLACE *<object>* statements are atomic. That is, when an object is replaced, the old object is deleted and the new object is created in a single transaction.
* Regarding metadata:

  > **Attention:**
  >
  > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).

## Examples

Create a network rule that is used to allow or block traffic from an AWS S3 endpoint to the internal stage:

```sqlexample
CREATE NETWORK RULE corporate_network
  TYPE = AWSVPCEID
  VALUE_LIST = ('vpce-123abc3420c1931')
  MODE = INTERNAL_STAGE
  COMMENT = 'corporate privatelink endpoint';
```

Create a network rule that is used to allow or block traffic from a range of IP addresses to the Snowflake service and internal stage:

```sqlexample
CREATE NETWORK RULE cloud_network
  TYPE = IPV4
  VALUE_LIST = ('47.88.25.32/27')
  COMMENT ='cloud egress ip range';
```

Create a network rule that is used to allow or block traffic from a Google Cloud pscConnectionId to the Snowflake service:

```sqlexample
CREATE NETWORK RULE gcp_rule
  TYPE = GCPPSCID
  MODE = INGRESS
  VALUE_LIST = ('31618973889077266');
```

Create a network rule that is used to allow a domain and domain/port combination when Snowflake is sending requests to external destinations:

```sqlexample
CREATE NETWORK RULE external_access_rule
  TYPE = HOST_PORT
  MODE = EGRESS
  VALUE_LIST = ('example.com', 'example.com:443');
```

Create a network rule to enable outbound private connectivity for
[external network access](../../developer-guide/external-network-access/external-network-access-overview.md):

```sqlexample
CREATE OR REPLACE NETWORK RULE ext_network_access_db.network_rules.azure_sql_private_rule
  MODE = EGRESS
  TYPE = PRIVATE_HOST_PORT
  VALUE_LIST = ('externalaccessdemo.database.windows.net');
```
