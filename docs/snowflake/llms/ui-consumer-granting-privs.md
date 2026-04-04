# Source: https://docs.snowflake.com/en/developer-guide/native-apps/ui-consumer-granting-privs.md

# Allow access to a consumer account

This topic describes how a consumer can allow a Snowflake Native App to create and access objects in
their account. This includes granting the privileges requested by an app or enabling access to existing
objects by using references. It also describes how to allow an app to use external and Apache Iceberg™
tables that a provider shares in the app.

## Privileges and references requested by an app

In a simple Snowflake Native App, all of the objects required by the app are created inside the
application object when the setup script runs during installation. All of the objects
required by the app are created in and accessed within the installed app.
The consumer does not need to perform any actions in their account.

However, some apps might ask the consumer to perform the following types of actions in their account:

* Create a database or warehouse.
* Execute tasks.
* Access existing objects such as tables.

There are two types of access that a Snowflake Native App can request:

* Privileges that allow the app to perform some account-level operations. An app can request the
  following global privileges:

  * EXECUTE TASK
  * EXECUTE MANAGED TASK
  * CREATE WAREHOUSE
  * MANAGE WAREHOUSES
  * CREATE DATABASE
  * CREATE COMPUTE POOL
  * BIND SERVICE ENDPOINT
  * READ SESSION

  Some apps might also request the IMPORTED PRIVILEGES privilege on the SNOWFLAKE database.
  See Grant the IMPORTED PRIVILEGES privilege on the SNOWFLAKE database.
* References that allow the app to access objects that already exist in the consumer
  account and are outside the application object. A provider defines the references required by the
  app in the manifest file.

  After installing the app, the consumer can authorize access on an object by creating a
  [reference](../../sql-reference/references.md) that associates the object to the app.

  An app can request access to the following types of objects and their corresponding privileges:

  | Object Type | Privileges Allowed |
  | --- | --- |
  | TABLE | SELECT, INSERT, UPDATE, DELETE, TRUNCATE, REFERENCES |
  | VIEW | SELECT, REFERENCES |
  | EXTERNAL TABLE | SELECT, REFERENCES |
  | FUNCTION | USAGE |
  | PROCEDURE | USAGE |
  | WAREHOUSE | MODIFY, MONITOR, USAGE, OPERATE |
  | API INTEGRATION | USAGE |

A consumer can approve these requests using [Snowsight](../../user-guide/ui-snowsight-gs.md) or by running the SQL commands.

> **Note:**
>
> If you do not grant the requested privileges or associate references on the requested object to the
> app, parts of the app may not function correctly.

## Manage access requests using Snowsight

If a provider implements a user interface in a Snowflake Native App, a consumer may perform the following using
[Snowsight](../../user-guide/ui-snowsight-gs.md).

* View and grant global privileges.
* Authorize access to existing objects in the consumer account.

### Grant global privileges

1. Sign in to [Snowsight](../../user-guide/ui-snowsight-gs.md).
2. In the navigation menu, select Catalog » Apps.
3. Select an app.
4. Select the Settings icon in the toolbar.
5. Select the Privileges tab.

   The account level permissions requested by the app appear under
   Account level privileges
6. In the Account level privileges pane, select the Edit icon and then move the slider for each privilege that you want to grant.
7. Select Update Privileges.

### Authorize access to specific objects

If a provider implements a user interface for a Snowflake Native App, a consumer can use [Snowsight](../../user-guide/ui-snowsight-gs.md)
to authorize access on objects in their account.

1. Sign in to [Snowsight](../../user-guide/ui-snowsight-gs.md).
2. In the navigation menu, select Catalog » Apps.
3. Select an app.
4. Select the Settings icon in the toolbar.
5. Select the Privileges tab.
6. In the Object access privileges pane, select Add next to the object to which
   you want to authorize access.
7. Select Select Data and choose the data product to which you want to authorize access.
8. Select Save.

### Revoke privileges and access to objects

Revoking privileges or removing access from objects can cause the application to become unstable or stop working.

1. Sign in to [Snowsight](../../user-guide/ui-snowsight-gs.md).
2. In the navigation menu, select Catalog » Apps.
3. Select an app.
4. Select the Settings icon in the toolbar.
5. Select the Privileges tab.
6. In the Account level privileges pane, select the Edit icon and then move the slider for the privilege you want to revoke.
7. Select Update Privileges.

## Manage privileges for an app by using SQL commands

If your provider does not implement an interface for granting privileges, you must
use SQL commands to manage application access requests.

### View the privileges requested by an app

When a provider specifies the privileges required by the app, the privilege request is
included as part of the installed app. You can view these privileges after installing
the app.

To view the privileges required by an app, run the
[SHOW PRIVILEGES](../../sql-reference/sql/show-privileges.md) command as shown
in the following example:

```sqlexample
SHOW PRIVILEGES IN APPLICATION hello_snowflake_app;
```

### Grant privileges to a Snowflake Native App

After a consumer determines the privileges requested by an app, they can grant those privileges to
the app.

For example, to grant the EXECUTE TASK privilege to an app, run the
[GRANT <privileges> … TO ROLE](../../sql-reference/sql/grant-privilege.md) command as shown
in the following example:

```sqlexample
GRANT EXECUTE TASK ON ACCOUNT TO APPLICATION hello_snowflake_app;
```

### Grant the MANAGE WAREHOUSES privilege to a Snowflake Native App

The [MANAGE WAREHOUSES privilege](../../user-guide/warehouses-tasks.md)
allows an app to create, modify, and use warehouses within the consumer account. To grant the
MANAGE WAREHOUSES privilege to an app, use the [GRANT <privileges> … TO ROLE](../../sql-reference/sql/grant-privilege.md)
as shown in the following example:

```sqlexample
GRANT MANAGE WAREHOUSES ON ACCOUNT TO APPLICATION hello_snowflake_app;
```

### Grant the IMPORTED PRIVILEGES privilege on the SNOWFLAKE database

Some apps might request that a consumer grants the IMPORTED PRIVILEGES privilege on the
SNOWFLAKE database in their account. This privilege can only be granted using SQL commands. It cannot
be granted using [Snowsight](../../user-guide/ui-snowsight-gs.md). If an app requires this privilege, the provider should
communicate this requirement to the consumer, for example, in the README file of the app.

To grant the IMPORT privilege on the SNOWFLAKE database, run the following command:

```sqlexample
GRANT IMPORTED PRIVILEGES ON DATABASE SNOWFLAKE TO APPLICATION hello_snowflake_app;
```

> **Note:**
>
> The IMPORTED PRIVILEGES privilege allows the app to access information about usage and costs associated with
> the consumer account. A consumer should ensure that they want to share this information with the
> app before granting this privilege.

## Manually authorize access to objects

When a provider defines a reference to an object in the manifest file, this reference
definition is included as part of the installed app. A consumer can create a reference to an object
in their account to authorize the app to access the object. If the provider did not create a user
interface for allowing access to objects in the consumer account, the consumer can authorize access
manually.

The consumer can create a reference for an object to associate with the app if they have the requested
privileges on the object. For example, if SELECT and INSERT privileges are required for an object, for
example a table, the consumer must create the reference using a role that has the SELECT and INSERT privileges
on the table. To view the object types and the specific required privilege grants for each object,
see View the References Requested by an App.

> **Note:**
>
> A reference does not grant any privileges on the object. If the role used to create the reference loses
> privileges on the object, the reference is no longer valid. The consumer must do one of the following:
>
> * Restore the required privileges to the role that created the reference.
> * Recreate the reference using a role with the required privileges on the object.

### View the references requested by an app

A consumer can view the references requested by an app by running the
[SHOW REFERENCES](../../sql-reference/sql/show-references.md) command as shown in
the following example:

```sqlexample
SHOW REFERENCES IN APPLICATION hello_snowflake_app;
```

This command displays a list of all the references defined in the app. It also displays the privileges
that the consumer role must have on the object in order to create the reference.

### Create the reference and associate the reference to the app

After viewing the references requested by the app,
a consumer can create the reference by running the [SYSTEM$REFERENCE](../../sql-reference/functions/system_reference.md) system
function as shown in the following example:

```sqlexample
SELECT SYSTEM$REFERENCE('table', 'db1.schema1.table1', 'persistent', 'select', 'insert');
```

This command creates the reference and returns an identifier for the object. The identifier looks
similar to the following example:

```output
ENT_REF_TABLE_16617302895522_2CDD20F5C047A5B87B2CE36F6837715786AF9F2D
```

The consumer passes this identifier to a callback stored procedure to associate the reference to the app.

> **Note:**
>
> The consumer must run this command for each reference requested by the app.

To associate a reference to an app, the consumer must pass the identifier returned by calling
the [SYSTEM$REFERENCE](../../sql-reference/functions/system_reference.md)
system function to a callback stored procedure. A callback procedure is a stored procedure that the
provider creates in the Snowflake Native App to associates a reference to the app.

To use a callback procedure, run the following command:

```sqlexample
CALL app.config.register_single_reference(
  'consumer_table', 'ADD', 'ENT_REF_TABLE_16617302895522_2CDD20F5C047A5B87B2CE36F6837715786AF9F2D');
```

In this example, the `register_single_reference()` stored procedure associates the reference with the
identifier `ENT_REF_TABLE_16617302895522_2CDD20F5C047A5B87B2CE36F6837715786AF9F2D` to the app.

> **Note:**
>
> A provider can include different callback procedures in an app. These should be specified in the
> README file of the app.

### Create and associate the reference to the app in a single step

After viewing the references requested by the application,
a consumer can create the reference and associate it to the app by passing the SYSTEM$REFERENCE
system function as an argument to a callback stored procedure.

The following example shows the syntax for passing the SYSTEM$REFERENCE system function as an argument to
a callback stored procedure:

```sqlexample
CALL app.config.register_single_reference(
 'consumer_table', 'ADD', SYSTEM$REFERENCE('table', 'db1.schema1.table1',
 'PERSISTENT', 'SELECT', 'INSERT'));
```

This example creates the reference and passes the identifier to the callback function to associate the
reference to the app.

## Enable external and Apache Iceberg™ tables

The Snowflake Native App Framework allows providers to share external and Apache Iceberg™ tables in the provider shares with consumers
in the app. However, consumers must give the app permission to access these tables.

### Security and cost considerations

When allowing an app to accesses an external or Iceberg table, consumers
should be aware of the following:

* External and Iceberg tables may pose data exfiltration risks to the consumer. For example, if an
  app exposes a view that contains an external table, a provider may be able to determine the types of
  queries the consumer makes by using their cloud provider access logs.
* External and Iceberg tables may incur additional costs related to egress and ingress usage if the
  object store containing the table is not in the same region where the app is published.

### Enable external and Iceberg tables using Snowsight

Providers can configure the app to display a dialog to all consumers to allow an app to access
an external or Iceberg tables.

To allow an app to access to an external or Iceberg table:

1. Sign in to [Snowsight](../../user-guide/ui-snowsight-gs.md).
2. In the navigation menu, select Catalog » Apps.
3. Select the app.
4. In the toolbar, select Settings.
5. Select the Privileges tab.
6. Under External data access, select Review.
7. Select Enable.

### Enable external and Iceberg tables using SQL

To enable access to external and Iceberg tables by using SQL use the
SET_APPLICATION_RESTRICTED_FEATURE_ACCESS system function as shown in the following
example:

```sqlexample
SELECT SYSTEM$SET_APPLICATION_RESTRICTED_FEATURE_ACCESS(hello_snowflake_app, 'external_data', '{"allowed_cloud_providers" : "all"}');
```

This command allows the `hello_snowflake_app` app to access the external or Iceberg tables in the
that the app uses.

To determine if external and Iceberg tables have been enabled for an app, use the
LIST_APPLICATION_RESTRICTED_FEATURES system function as shown in the following example:

```sqlexample
SYSTEM$LIST_APPLICATION_RESTRICTED_FEATURES('hello_snowflake_app')
```

This system function returns a JSON object that indicates if external and Iceberg tables are allowed
the for the `hello_snowflake_app`.
