# Source: https://docs.snowflake.com/en/sql-reference/functions/system_get_snowflake_egress_ip_ranges.md

Categories:
:   [System functions](../functions-system.md) (System Information)

# SYSTEM$GET_SNOWFLAKE_EGRESS_IP_RANGES

Support for this feature is available only for external access on AWS.

Returns a list of egress IP address ranges (as Classless Inter-Domain Routing (CIDR) IP addresses) that you can use to represent
Snowflake in a server’s IP allowlist.

Use this function to obtain a list of egress IP address ranges with which to allow Snowflake traffic on external servers. You
can add IP addresses from the list to the allowlist on an external server from which Snowflake makes requests.

For example, you can allow requests by user-defined functions (UDFs) deployed on Snowflake to access resources on an external server.
To do this, you add Snowflake egress IP addresses to the network firewall for your server.

Addresses in the returned list expire. You can automate refreshes from the list as described in
[Securing ingress of Snowflake requests with egress IP addresses](../../user-guide/egress-ip/network-egress.md).

## Syntax

```sqlsyntax
SYSTEM$GET_SNOWFLAKE_EGRESS_IP_RANGES()
```

## Returns

Returns JSON containing a list of CIDR IP addresses, effective date, and an expiration date for each address. The following example shows what the
return value looks like:

```sqlexample
SELECT SYSTEM$GET_SNOWFLAKE_EGRESS_IP_RANGES();
```

```json
{
  "ipv4_prefix": "153.45.151.0/24",
  "effective": "2025-06-30T23:59:59Z",
  "expires": "2026-08-30T23:59:59Z"
}
```

## Usage notes

Keep in mind the following about the returned list of CIDR IP address ranges:

* Each IP address expires. The returned list includes both the IP address and its expiration date and time. To allow continued access
  from Snowflake, automate refreshing your allowlist with addresses that have not yet expired.

  For more information, see [Securing ingress of Snowflake requests with egress IP addresses](../../user-guide/egress-ip/network-egress.md).
* Addresses are scoped to the region of your Snowflake deployment. Addresses for one region differ from those for another region.
* Addresses are shared among Snowflake accounts in the region. In other words, they’re not unique to a Snowflake account.
