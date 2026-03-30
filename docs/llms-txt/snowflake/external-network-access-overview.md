# Source: https://docs.snowflake.com/en/developer-guide/external-network-access/external-network-access-overview.md

# External network access overview

You can create secure access to specific network locations external to Snowflake, then use that access from within the handler code for
user-defined functions (UDFs) and stored procedures. You can enable this access through an external access integration.

With an external access integration, you can:

* Write UDF and procedure handlers that access external locations.
* Allow or block access to locations on a network external to Snowflake.
* Use secrets that represent stored credentials, rather than using literal values, within handler code to authenticate with external
  network locations.
* Specify which secrets are allowed for use with external network locations.
* Choose whether your connectivity to the external network location uses the public internet or a private network, such as by using
  Azure Private Link, AWS PrivateLink, or Google Cloud Private Service Connect.

  If you choose to use private connectivity, your Snowflake account must be Business Critical Edition (or later).

  For more information, see the following topics:

  * [External network access and private connectivity on Microsoft Azure](creating-using-private-azure.md)
  * [External network access and private connectivity on AWS](creating-using-private-aws.md)
  * [External network access and private connectivity on Google Cloud](creating-using-private-gcp.md)

## Get started

For an introduction to external network access, including code examples, refer to
[External network access examples](external-network-access-examples.md).

## References

* [CREATE EXTERNAL ACCESS INTEGRATION](../../sql-reference/sql/create-external-access-integration.md)
* [ALTER EXTERNAL ACCESS INTEGRATION](../../sql-reference/sql/alter-external-access-integration.md)
* [DESCRIBE INTEGRATION](../../sql-reference/sql/desc-integration.md)
* [DROP INTEGRATION](../../sql-reference/sql/drop-integration.md)
* [SHOW INTEGRATIONS](../../sql-reference/sql/show-integrations.md)
