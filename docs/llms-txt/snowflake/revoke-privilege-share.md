# Source: https://docs.snowflake.com/en/sql-reference/sql/revoke-privilege-share.md

# REVOKE *<privilege>* … FROM SHARE

Revokes access privileges for databases and other supported database objects (schemas, tables, and views) from a share. Revoking
privileges on these objects effectively removes the objects from the share, disabling access to the objects granted via the database
role in all consumer accounts that have created a database from the share.

For more details, see [About Secure Data Sharing](../../user-guide/data-sharing-intro.md) and [Create and configure shares](../../user-guide/data-sharing-provider.md).

See also:
:   [GRANT <privilege> … TO SHARE](grant-privilege-share.md)

    [REVOKE <privileges> … FROM ROLE](revoke-privilege.md)

## Syntax

```sqlsyntax
REVOKE objectPrivilege ON
     {  DATABASE <name>
      | SCHEMA <name>
      | SEMANTIC VIEW <name>
      | { TABLE <name> | ALL TABLES IN SCHEMA <schema_name> }
      | { EXTERNAL TABLE <name> | ALL EXTERNAL TABLES IN SCHEMA <schema_name> }
      | { ICEBERG TABLE <name> | ALL ICEBERG TABLES IN SCHEMA <schema_name> }
      | { DYNAMIC TABLE <name> | ALL DYNAMIC TABLES IN SCHEMA <schema_name> }
      | { VIEW <name> | ALL VIEWS IN SCHEMA <schema_name> }  }
  FROM SHARE <share_name>
```

Where:

```sqlsyntax
objectPrivilege ::=
-- For DATABASE
   REFERENCE_USAGE [ , ... ]
-- For DATABASE, FUNCTION, or SCHEMA
   USAGE [ , ... ]
-- For SEMANTIC VIEW
   { REFERENCES | SELECT } [ , ... ]
-- For TABLE
   EVOLVE SCHEMA [ , ... ]
-- For EXTERNAL TABLE, ICEBERG TABLE, TABLE, or VIEW
   SELECT [ , ... ]
-- For TAG
   READ
```

## Parameters

`name`
:   Specifies the identifier for the object (database, schema, table, or secure view) for which the specified privilege is revoked.

`schema_name`
:   Specifies the identifier for the schema for which the specified privilege is revoked for all tables or views.

`share_name`
:   Specifies the identifier for the share for which the specified privilege is revoked.

## Usage notes

* Each object privilege must be revoked individually from a role, except for tables, Apache Iceberg™ tables, and views.
  Using an `ALL` clause, you can revoke the SELECT privilege from all the tables or views in the specified schema from a role.
* If you specify a `TABLE` object that is an *Iceberg* table, the command revokes the privilege from that Iceberg table.

## Examples

> ```sqlexample
> REVOKE SELECT ON VIEW mydb.shared_schema.view1 FROM SHARE share1;
>
> REVOKE SELECT ON VIEW mydb.shared_schema.view3 FROM SHARE share1;
>
> REVOKE USAGE ON SCHEMA mydb.shared_schema FROM SHARE share1;
>
> REVOKE SELECT ON ALL TABLES IN SCHEMA mydb.public FROM SHARE share1;
>
> REVOKE SELECT ON ALL ICEBERG TABLES IN SCHEMA mydb.public FROM SHARE share1;
>
> REVOKE SELECT ON ALL DYNAMIC TABLES IN SCHEMA mydb.public FROM SHARE share1;
>
> REVOKE SELECT ON ICEBERG TABLE mydb.shared_schema.iceberg_table_1 FROM SHARE share1;
>
> REVOKE SELECT ON DYNAMIC TABLE mydb TO SHARE share1;
>
> REVOKE USAGE ON SCHEMA mydb.public FROM SHARE share1;
>
> REVOKE USAGE ON DATABASE mydb FROM SHARE share1;
> ```

This example disallows a shared secure view to reference objects from a different database:

> ```sqlexample
> REVOKE REFERENCE_USAGE ON DATABASE database2 FROM SHARE share1;
> ```
