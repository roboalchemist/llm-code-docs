# Source: https://docs.snowflake.com/en/sql-reference/sql/alter-dynamic-table.md

# ALTER DYNAMIC TABLE

Modifies the properties of a [dynamic table](../../user-guide/dynamic-tables-about.md).

See also:
:   [CREATE DYNAMIC TABLE](create-dynamic-table.md), [DESCRIBE DYNAMIC TABLE](desc-dynamic-table.md), [DROP DYNAMIC TABLE](drop-dynamic-table.md), [SHOW DYNAMIC TABLES](show-dynamic-tables.md)

## Syntax

```sqlsyntax
ALTER DYNAMIC TABLE [ IF EXISTS ] <name> { SUSPEND | RESUME }

ALTER DYNAMIC TABLE [ IF EXISTS ] <name> RENAME TO <new_name>

ALTER DYNAMIC TABLE [ IF EXISTS ] <name> SWAP WITH <target_dynamic_table_name>

ALTER DYNAMIC TABLE [ IF EXISTS ] <name> REFRESH [ COPY SESSION ]

ALTER DYNAMIC TABLE [ IF EXISTS ] <name> { clusteringAction }

ALTER DYNAMIC TABLE [ IF EXISTS ] <name> { tableColumnCommentAction }

ALTER DYNAMIC TABLE <name> { SET | UNSET } COMMENT = '<string_literal>'

ALTER DYNAMIC TABLE [ IF EXISTS ] <name> dataGovnPolicyTagAction

ALTER DYNAMIC TABLE [ IF EXISTS ] <name> searchOptimizationAction

ALTER DYNAMIC TABLE [ IF EXISTS ] <name> SET
  [ TARGET_LAG = { '<num> { seconds | minutes | hours | days }'  | DOWNSTREAM } ],
  [ WAREHOUSE = <warehouse_name> ],
  [ INITIALIZATION_WAREHOUSE = <warehouse_name> ],
  [ DATA_RETENTION_TIME_IN_DAYS = <integer> ],
  [ MAX_DATA_EXTENSION_TIME_IN_DAYS = <integer> ]
  [ DEFAULT_DDL_COLLATION = '<collation_specification>' ],
  [ LOG_LEVEL = '<log_level>' ],
  [ CONTACT ( <purpose> = <contact_name> [ , <purpose> = <contact_name> ... ] ) ],
  [ IMMUTABLE WHERE ( <expr> ) ],
  [ EXECUTE AS USER <user_name>
    [ USE SECONDARY ROLES { ALL | NONE | <role> [ , ... ] } ]
  ]
  [ ROW_TIMESTAMP = { TRUE | FALSE } ]

ALTER DYNAMIC TABLE [ IF EXISTS ] <name> UNSET
  [ INITIALIZATION_WAREHOUSE ],
  [ DATA_RETENTION_TIME_IN_DAYS ],
  [ MAX_DATA_EXTENSION_TIME_IN_DAYS ],
  [ DEFAULT_DDL_COLLATION ],
  [ LOG_LEVEL ],
  [ CONTACT <purpose> ],
  [ IMMUTABLE WHERE ],
  [ EXECUTE AS USER ],
  [ ROW_TIMESTAMP ]
```

Where:

> ```sqlsyntax
> clusteringAction ::=
>   {
>     CLUSTER BY ( <expr> [ , <expr> , ... ] )
>     | { SUSPEND | RESUME } RECLUSTER
>     | DROP CLUSTERING KEY
>   }
> ```
>
> For more information, see [Clustering Keys & Clustered Tables](../../user-guide/tables-clustering-keys.md).
>
> ```sqlsyntax
> tableCommentAction ::=
>   {
>     ALTER | MODIFY [ ( ]
>                            [ COLUMN ] <col1_name> COMMENT '<string>'
>                          , [ COLUMN ] <col1_name> UNSET COMMENT
>                        [ , ... ]
>                    [ ) ]
>   }
> ```
>
> ```sqlsyntax
> dataGovnPolicyTagAction ::=
>   {
>       ADD ROW ACCESS POLICY <policy_name> ON ( <col_name> [ , ... ] )
>     | DROP ROW ACCESS POLICY <policy_name>
>     | DROP ROW ACCESS POLICY <policy_name> ,
>         ADD ROW ACCESS POLICY <policy_name> ON ( <col_name> [ , ... ] )
>     | DROP ALL ROW ACCESS POLICIES
>   }
>   |
>   {
>     SET AGGREGATION POLICY <policy_name>
>       [ ENTITY KEY ( <col_name> [, ... ] ) ]
>       [ FORCE ]
>   | UNSET AGGREGATION POLICY
>   }
>   |
>   {
>     { ALTER | MODIFY } [ COLUMN ] <col1_name>
>         SET MASKING POLICY <policy_name>
>           [ USING ( <col1_name> , <cond_col_1> , ... ) ] [ FORCE ]
>       | UNSET MASKING POLICY
>   }
>   |
>   { ALTER | MODIFY } [ COLUMN ] <col1_name> SET TAG
>       <tag_name> = '<tag_value>' [ , <tag_name> = '<tag_value>' ... ]
>       , [ COLUMN ] <col2_name> SET TAG
>           <tag_name> = '<tag_value>' [ , <tag_name> = '<tag_value>' ... ]
>   |
>   {
>     { ALTER | MODIFY } [ COLUMN ] <col1_name>
>         SET PROJECTION POLICY <policy_name>
>           [ FORCE ]
>       | UNSET PROJECTION POLICY
> }
> |
>   { ALTER | MODIFY } [ COLUMN ] <col1_name> UNSET TAG <tag_name> [ , <tag_name> ... ]
>                   , [ COLUMN ] <col2_name> UNSET TAG <tag_name> [ , <tag_name> ... ]
>   }
>   |
>   {
>       SET TAG <tag_name> = '<tag_value>' [ , <tag_name> = '<tag_value>' ... ]
>     | UNSET TAG <tag_name> [ , <tag_name> ... ]
>   }
> ```
>
> ```sqlsyntax
> searchOptimizationAction ::=
>   {
>     ADD SEARCH OPTIMIZATION [
>       ON <search_method_with_target> [ , <search_method_with_target> ... ]
>         [ EQUALITY ]
>       ]
>
>     | DROP SEARCH OPTIMIZATION [
>       ON { <search_method_with_target> | <column_name> | <expression_id> }
>         [ EQUALITY ]
>         [ , ... ]
>       ]
>
>     | SUSPEND SEARCH OPTIMIZATION [
>        ON { <search_method_with_target> | <column_name> | <expression_id> }
>           [ , ... ]
>      ]
>
>     | RESUME SEARCH OPTIMIZATION [
>        ON { <search_method_with_target> | <column_name> | <expression_id> }
>           [ , ... ]
>      ]
>   }
> ```
>
> For details, see [Search optimization actions (searchOptimizationAction)](alter-table.md).

## Parameters

`name`
:   Identifier for the dynamic table to alter.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

`SUSPEND | RESUME`
:   Specifies the action to perform on the dynamic table:

    * `SUSPEND` suspends refreshes on the dynamic table. If the dynamic table is used
      by other dynamic tables, they are also suspended.
    * `RESUME` resumes refreshes on the dynamic table. Resume operations cascade
      downstream to all downstream dynamic tables not manually suspended.

`RENAME TO new_name`
:   Renames the specified dynamic table with a new identifier that is not currently used by
    any other dynamic tables in the schema.

    Renaming a dynamic table requires the CREATE DYNAMIC TABLE privilege on the schema for
    the dynamic table.

    You can also move the dynamic table to a different database and/or schema while
    optionally renaming the dynamic table. To do so, specify a qualified `new_name`
    value that includes the new database and/or schema name in the form
    `db_name.schema_name.new_name` or `schema_name.new_name`,
    respectively.

    The following restrictions apply:

    * The destination database and/or schema must already exist. In addition, an object
      with the same name cannot already exist in the new location; otherwise, the
      statement returns an error.
    * You can’t move an object to a managed access schema unless the object owner
      (that is, the role that has the OWNERSHIP privilege on the object) also owns the
      target schema.
    * When an object (table, column, etc.) is renamed, other objects that reference it
      must be updated with the new name.

`SWAP WITH target_dynamic_table_name`
:   Swaps two dynamic tables in a single transaction. The role used to perform this
    operation must have OWNERSHIP privileges on both dynamic tables.

    The following restrictions apply:

    * You can only swap a dynamic table with another dynamic table.

`REFRESH [ COPY SESSION ]`
:   Specifies that the dynamic table should be manually refreshed.

    Both user-suspended and auto-suspended dynamic tables can be manually refreshed.
    Manually refreshed dynamic tables return MANUAL as the output for `refresh_trigger`
    in the DYNAMIC_TABLE_REFRESH_HISTORY function.

    Note that refreshing a dynamic table also refreshes all upstream dynamic tables as
    of the same data timestamp. For more information, see [Alter the warehouse or target lag for dynamic tables](../../user-guide/dynamic-tables-alter.md).

    For information on dynamic table refresh status, see [DYNAMIC_TABLE_REFRESH_HISTORY](../functions/dynamic_table_refresh_history.md).

    `COPY SESSION`

    > Runs the refresh operation in a copy of the current session using the current user and
    > warehouse.
    >
    > This only applies to a single manual refresh; it does not permanently update the credentials for the dynamic table.
    > Use the [GRANT OWNERSHIP](grant-ownership.md) command to transfer the ownership for scheduled
    > refreshes. For more information, see [Transfer ownership](../../user-guide/dynamic-tables-privileges.md).
    >
    > The primary role is the role that owns the dynamic table and secondary roles will match
    > the DEFAULT_SECONDARY_ROLES property of the user.

`SET ...`
:   Specifies one or more properties/parameters to set for the table (separated by blank
    spaces, commas, or new lines):

    `TARGET_LAG = { num { seconds | minutes | hours | days } | DOWNSTREAM }`
    :   > Specifies the target lag for the dynamic table:

        `'num seconds | minutes | hours | days'`
        :   Specifies the maximum amount of time that the dynamic table’s content should lag
            behind updates to the base tables.

            For example:

            * If the data in the dynamic table should lag by no more than 5 minutes, specify `5 minutes`.
            * If the data in the dynamic table should lag by no more than 5 hours, specify `5 hours`.

            The minimum value is 1 minute. If a dynamic table A depends on another dynamic
            table B, the minimum lag for A must be greater than or equal to the lag for B.

        `DOWNSTREAM`
        :   > Specifies that the dynamic table should be refreshed if any dynamic table
            > downstream of it is refreshed.

            For information on how target lag affects refresh frequency and costs, see [Identify the right target lag](../../user-guide/dynamic-tables-performance-optimize.md).

    `WAREHOUSE = warehouse_name`
    :   Specifies the name of the warehouse that provides the compute resources for
        refreshing the dynamic table.

        You must use a role that has the USAGE privilege on this warehouse. For more information, see [Privileges to create a dynamic table](../../user-guide/dynamic-tables-privileges.md).

        For guidance on choosing a warehouse for optimal refresh performance, see [Adjust your warehouse configuration](../../user-guide/dynamic-tables-performance-optimize.md).

    `INITIALIZATION_WAREHOUSE = warehouse_name`
    :   Specifies a warehouse to use for all dynamic table [initializations and reinitializations](../../user-guide/dynamic-tables-refresh.md).

        When this parameter is set, the specified warehouse is used for all initializations and reinitializations; otherwise, the dynamic
        table uses the warehouse that is specified by the required WAREHOUSE parameter for all refreshes.

        You must use a role that has the USAGE privilege on this warehouse. For more information, see [Privileges to create a dynamic table](../../user-guide/dynamic-tables-privileges.md).

    `DATA_RETENTION_TIME_IN_DAYS = integer`
    :   Object-level parameter that modifies the retention period for the dynamic table for
        Time Travel. For more details, see [Understanding & using Time Travel](../../user-guide/data-time-travel.md) and
        [Working with Temporary and Transient Tables](../../user-guide/tables-temp-transient.md).

        For a detailed description of this parameter and more information about object
        parameters, see [Parameters](../parameters.md).

        Values:

        > * Standard Edition: `0` or `1`
        > * Enterprise Edition:
        >
        >   + `0` to `90` for permanent dynamic tables
        >   + `0` or `1` for transient dynamic tables

        > **Note:**
        >
        > A value of `0` effectively disables Time Travel for the dynamic table.

    `MAX_DATA_EXTENSION_TIME_IN_DAYS = integer`
    :   Object parameter that specifies the maximum number of days Snowflake can extend the
        data retention period to prevent streams on the dynamic table from becoming stale.

        For a detailed description of this parameter, see
        [MAX_DATA_EXTENSION_TIME_IN_DAYS](../parameters.md).

    `DEFAULT_DDL_COLLATION = 'collation_specification'`
    :   Specifies a default [collation specification](../collation.md)
        for any new columns added to the dynamic table.

        Setting this parameter does not change the collation specification for any
        existing columns.

        For more information, see [DEFAULT_DDL_COLLATION](../parameters.md).

    `LOG_LEVEL = 'log_level'`
    :   Specifies the severity level of [events for this dynamic table](../../user-guide/dynamic-tables-monitor-event-table-alerts.md) that are
        ingested and made available in the active event table. Events at the specified level (and at more severe levels) are
        ingested.

        For more information about levels, see [LOG_LEVEL](../parameters.md). For information about setting the log level, see
        [Setting levels for logging, metrics, and tracing](../../developer-guide/logging-tracing/telemetry-levels.md).

    `CONTACT purpose = contact [ , purpose = contact ... ]`
    :   Associate the existing object with one or more [contacts](../../user-guide/contacts-using.md).

        You cannot set the CONTACT property with other properties in the same statement.

    `IMMUTABLE WHERE`
    :   Specifies a condition that defines the immutable portion of the dynamic table. For more
        information, see [Understanding immutability constraints](../../user-guide/dynamic-tables-immutability-constraints.md).

    `EXECUTE AS USER user_name`
    :   Refreshes the dynamic table as the specified user, rather than as the SYSTEM user.

        To specify EXECUTE AS USER, you must use a role that has been granted the IMPERSONATE privilege on the `user_name` user. To grant this privilege,
        run the [GRANT <privileges> … TO ROLE](grant-privilege.md) command.

        `USE SECONDARY ROLES { ALL | NONE | role [ , ... ] }`
        :   Specifies the secondary roles to use on the dynamic table. Can be used to override the default secondary roles that are otherwise used in execution.

            Can only be used with the EXECUTE AS USER option.

        For more information, see [Refresh dynamic tables with specific user privileges and secondary roles](../../user-guide/dynamic-tables-privileges.md).

    `ROW_TIMESTAMP = { TRUE | FALSE }`
    :   Adds or removes row timestamps on the table.

        * `TRUE` adds row timestamps on the table.
        * `FALSE` removes row timestamps on the table. This parameter setting permanently deletes all stored METADATA$ROW_LAST_COMMIT_TIME values.
          Reenabling it will not restore these values and Time Travel queries will return nothing.

`UNSET ...`
:   Specifies one or more properties/parameters to unset for the dynamic table, which
    resets them back to their defaults:

    * `INITIALIZATION_WAREHOUSE`
    * `DATA_RETENTION_TIME_IN_DAYS`
    * `MAX_DATA_EXTENSION_TIME_IN_DAYS`
    * `DEFAULT_DDL_COLLATION`
    * `LOG_LEVEL`
    * `CONTACT purposes`
    * `IMMUTABLE WHERE`
    * `EXECUTE AS USER`
    * `ROW_TIMESTAMP`

## Clustering actions (`clusteringAction`)

`CLUSTER BY ( expr [ , expr , ... ] )`
:   Specifies (or modifies) one or more table columns or column expressions as the
    clustering key for the dynamic table. These are the columns/expressions for which
    clustering is maintained by Automatic Clustering. Before you specify a clustering key
    for a dynamic table, you should understand micro-partitions. For more information, see
    [Understanding Snowflake Table Structures](../../user-guide/tables-micro-partitions.md).

    Note the following when using clustering keys with dynamic tables:

    * Column definitions are required and must be explicitly specified in the statement.
    * Clustering keys are not intended or recommended for all tables; they
      typically benefit very large (for example, multi-terabyte) tables.

`SUSPEND | RESUME RECLUSTER`
:   Enables or disables [Automatic Clustering](../../user-guide/tables-auto-reclustering.md) for the dynamic table.

`DROP CLUSTERING KEY`
:   Drops the clustering key for the dynamic table.

For more information about clustering keys and reclustering, see [Understanding Snowflake Table Structures](../../user-guide/tables-micro-partitions.md).

## Table comment actions (`tableCommentAction`)

`ALTER | MODIFY [ ( ]` . `[ COLUMN ] <col1_name> COMMENT '<string>'` . `, [ COLUMN ] <col1_name> UNSET COMMENT` . `[ , ... ]` . `[ ) ]`
:   Alters a comment or overwrites the existing comment for a column in the dynamic table.

`SET | UNSET COMMENT = '<string_literal>'`
:   Adds a comment or overwrites the existing comment for the dynamic table.

## Data Governance policy and tag actions (`dataGovnPolicyTagAction`)

`TAG tag_name = 'tag_value' [ , tag_name = 'tag_value' , ... ]`
:   Specifies the [tag](../../user-guide/object-tagging/introduction.md) name and the tag string value.

    The tag value is always a string, and the maximum number of characters for the tag value is 256.

    For information about specifying tags in a statement, see [Tag quotas](../../user-guide/object-tagging/introduction.md).

`policy_name`
:   Identifier for the policy; must be unique for your schema.

    `ADD ROW ACCESS POLICY policy_name ON (col_name [ , ... ])`
    :   Adds a row access policy to the dynamic table.

        At least one column name must be specified. Additional columns can be specified
        with a comma separating each column name.

    `DROP ROW ACCESS POLICY policy_name`
    :   Drops a row access policy from the dynamic table.

    `DROP ROW ACCESS POLICY policy_name, ADD ROW ACCESS POLICY policy_name ON ( col_name [ , ... ] )`
    :   Drops the row access policy that is set on the dynamic table and adds a row access
        policy to the same dynamic table in a single SQL statement.

    `DROP ALL ROW ACCESS POLICIES`
    :   Drops all [row access policy](../../user-guide/security-row-using.md) associations from the dynamic table.

        You must also use this clause to access a dynamic table that you restore from a [backup](../../user-guide/backups.md), if a
        row access policy applied to the table when the backup was created and the policy was later dropped. After the dynamic table
        is restored, you can’t query it until you run an ALTER TABLE command with the DROP ALL ROW ACCESS POLICIES clause.

    `{ ALTER | MODIFY } [ COLUMN ] ...`
    :   `USING ( col_name , cond_col_1 ... )`
        :   Specifies the arguments to pass into the conditional masking policy.

            The first column in the list specifies the data to be masked or tokenized based on
            policy conditions and must match the column to which the masking policy
            is applied.

            The additional columns specify which data to evaluate for masking or tokenization
            in each row of the query result when selecting from the first column.

            If the USING clause is omitted, Snowflake treats the conditional masking policy as a
            normal [masking policy](../../user-guide/security-column-intro.md).

    `SET AGGREGATION POLICY {policy_name}`
    :   `[ ENTITY KEY ({col_name} [ , ... ]) ] [ FORCE ]`
        :   Assigns an [aggregation policy](../../user-guide/aggregation-policies.md) to the dynamic table.

            Use the optional ENTITY KEY parameter to define which columns uniquely identity an entity within the dynamic table. For
            more information, see [Implementing entity-level privacy with aggregation policies](../../user-guide/aggregation-policies-entity-privacy.md).

            Use the optional FORCE parameter to atomically replace an existing aggregation policy with the new aggregation policy.

    `UNSET AGGREGATION POLICY`
    :   Detaches an aggregation policy from the dynamic table.

    `FORCE`
    :   Replaces a masking or projection policy that is currently set on a column with a
        different policy in a single statement.

        Note that using the `FORCE` keyword with a masking policy requires the
        [data type](../../sql-reference-data-types.md) of the policy in the ALTER DYNAMIC
        TABLE statement (i.e. STRING) to match the data type of the masking policy currently
        set on the column (i.e. STRING).

        If a masking policy is not currently set on the column, specifying this keyword has
        no effect.

        For details, see: [Replace a masking policy on a column](../../user-guide/security-column-intro.md) or
        [Replace a projection policy](../../user-guide/projection-policies.md).

## Search optimization actions (`searchOptimizationAction`)

`ADD SEARCH OPTIMIZATION`
:   Adds [search optimization](../../user-guide/search-optimization-service.md) for the
    entire dynamic table or, if you specify the optional `ON` clause, for specific
    columns.

    Search optimization can be expensive to maintain, especially if the data in the table
    changes frequently. For more information, see
    [Search optimization cost estimation and management](../../user-guide/search-optimization/cost-estimation.md).

`ON search_method_with_target [, search_method_with_target ... ]`
:   Specifies that you want to configure search optimization for specific columns or
    VARIANT fields (rather than the entire dynamic table).

    For `search_method_with_target`, use an expression with the following syntax:

    ```sqlsyntax
    <search_method>(<target> [, ...])
    ```

    Where:

    * `search_method` specifies one of the following methods that optimizes
      queries for a particular type of predicate:

      + `GEO`: Predicates that use GEOGRAPHY types.
      + `SUBSTRING`: Predicates that match substrings and regular expressions (for
        example, [[ NOT ] LIKE](../functions/like.md), [[ NOT ] ILIKE](../functions/ilike.md),
        [[ NOT ] RLIKE](../functions/rlike.md), [REGEXP_LIKE](../functions/regexp_like.md),
        etc.)
      + `EQUALITY`: Equality and IN predicates.
    * `target` specifies the column, VARIANT field, or an asterisk (\*).

      Depending on the value of `search_method`, you can specify a column or
      VARIANT field of one of the following types:

      + `GEO`: Columns of the GEOGRAPHY data type.
      + `SUBSTRING`: Columns of string or VARIANT data types, including paths to
        fields in VARIANTs. Specify paths to fields as described under `EQUALITY`;
        searches on nested fields are improved in the same way.
      + `EQUALITY`: Columns of numeric, string, binary, and VARIANT data types,
        including paths to fields in VARIANT columns.

        To specify a VARIANT field, use
        [dot or bracket notation](../../user-guide/querying-semistructured.md). For
        example:

        - `my_column:my_field_name.my_nested_field_name`
        - `my_column['my_field_name']['my_nested_field_name']`

        You may also use a colon-delimited path to the field. For example:

        - `my_column:my_field_name:my_nested_field_name`

        When you specify a VARIANT field, the configuration applies to all nested fields
        under that field.

        For example, if you specify `ON EQUALITY(src:a.b)`:

        - This configuration can improve queries `on src:a.b` and on any nested fields
          (for example, `src:a.b.c`, `src:a.b.c.d`, etc.).
        - This configuration only affects queries that use the `src:a.b` prefix (for
          example, `src:a`, `src:z`, etc.).

    To specify all applicable columns in the table as targets, use an asterisk (`*`).

    Note that you can’t specify both an asterisk and specific column names for a
    given search method. However, you can specify an asterisk in different search methods.

    For example, you can specify the following expressions:

    ```sqlexample
    ON SUBSTRING(*)
    ON EQUALITY(*), SUBSTRING(*), GEO(*)
    ```

    You can’t specify the following expressions:

    ```sqlexample
    ON EQUALITY(*, c1)
    ON EQUALITY(c1, *)
    ON EQUALITY(v1:path, *)
    ON EQUALITY(c1), EQUALITY(*)
    ```

    To specify more than one search method on a target, use a comma to separate each
    subsequent method and target:

    ```sqlexample
    ALTER DYNAMIC TABLE my_dynamic_table ADD SEARCH OPTIMIZATION ON EQUALITY(c1), EQUALITY(c2, c3);
    ```

    If you run the ALTER DYNAMIC TABLE … ADD SEARCH OPTIMIZATION ON … command multiple
    times on the same table, each subsequent command adds to the existing configuration
    for the table. For instance, suppose that you run the following commands:

    ```sqlexample
    ALTER DYNAMIC TABLE my_dynamic_table ADD SEARCH OPTIMIZATION ON EQUALITY(c1, c2);
    ALTER DYNAMIC TABLE my_dynamic_table ADD SEARCH OPTIMIZATION ON EQUALITY(c3, c4);
    ```

    This adds equality predicates for the columns `c1`, `c2`, `c3`, and `c4` to
    the configuration for the table. This is equivalent to running the command:

    ```sqlexample
    ALTER DYNAMIC TABLE my_dynamic_table ADD SEARCH OPTIMIZATION ON EQUALITY(c1, c2, c3, c4);
    ```

    For examples, see [Enabling search optimization for specific columns](../../user-guide/search-optimization/enabling.md).

`DROP SEARCH OPTIMIZATION`
:   Removes [search optimization](../../user-guide/search-optimization-service.md) for the
    entire dynamic table or, if you specify the optional `ON` clause, from specific
    columns.

    The following restrictions apply:

    * If a dynamic table has the search optimization property, then dropping the dynamic
      table and undropping it preserves the search optimization property.
    * Removing the search optimization property from a dynamic table and then adding it
      back incurs the same cost as adding it the first time.

`ON search_method_with_target | column_name | expression_id [, ... ]`
:   Specifies that you want to drop the search optimization configuration for specific
    columns or VARIANT fields (rather than dropping search optimization for the entire
    dynamic table).

    To identify the column configuration to drop, specify one of the following:

    * For `search_method_with_target`, specify a method for optimizing queries for
      one or more specific targets, which can be columns or VARIANT fields. Use the
      syntax described earlier.
    * For `column_name`, specify the name of the column configured for search
      optimization. Specifying the column name drops all expressions for that column,
      including expressions that use VARIANT fields in the column.
    * For `expression_id`, specify the ID for an expression listed in the output
      of the [DESCRIBE SEARCH OPTIMIZATION](../../user-guide/search-optimization/enabling.md)
      command.

    You can specify any combination of search methods with targets, column names, and
    expression IDs using a comma between items.

    For examples, see [Dropping search optimization for specific columns](../../user-guide/search-optimization/enabling.md).

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| OWNERSHIP or OPERATE | The dynamic table you want to alter. | Some actions are only supported with the OWNERSHIP privilege. For more information, see [Privileges to alter a dynamic table](../../user-guide/dynamic-tables-privileges.md). |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* To alter a dynamic table, you must be using a role that has OPERATE privilege on that
  dynamic table. For general information, see [Privileges to view a dynamic table’s metadata](../../user-guide/dynamic-tables-privileges.md).
* Making changes to masking policies on a base table causes a [reinitialization](../../user-guide/dynamic-tables-refresh.md).
* If you want to update an existing dynamic table and need to see its current definition,
  call the [GET_DDL](../functions/get_ddl.md) function.
* You can use data metric functions with dynamic tables by executing an [ALTER TABLE](alter-table.md)
  command. For more information, see [Use SQL to set up data metric functions](../../user-guide/data-quality-working.md).
* You cannot use [IDENTIFIER()](../identifier-literal.md) to specify the
  name of the dynamic table to alter. For example, the following statement isn’t supported:

  ```sqlexample
  ALTER DYNAMIC TABLE IDENTIFIER(my_dynamic_table) SUSPEND;
  ```

* After a reinitialization or full refresh, search indexes on dynamic tables are rebuilt.
  This process involves dropping the existing indexes and rebuilding them from scratch,
  which might incur higher costs. For more information, see [Search optimization cost estimation and management](../../user-guide/search-optimization/cost-estimation.md).
* Regarding metadata:

  > **Attention:**
  >
  > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).

## Examples

Change the target lag time of a dynamic table named `my_dynamic_table` to 1 hour:

```sqlexample
ALTER DYNAMIC TABLE my_dynamic_table SET
  TARGET_LAG = '1 hour';
```

Specify downstream target lag for `my_dynamic_table`:

```sqlexample
ALTER DYNAMIC TABLE my_dynamic_table SET TARGET_LAG = DOWNSTREAM;
```

Suspend a dynamic table:

```sqlexample
ALTER DYNAMIC TABLE my_dynamic_table SUSPEND;
```

Resume a dynamic table:

```sqlexample
ALTER DYNAMIC TABLE my_dynamic_table RESUME;
```

Rename `my_dynamic_table`:

```sqlexample
ALTER DYNAMIC TABLE my_dynamic_table RENAME TO my_updated_dynamic_table;
```

Swap `my_dynamic_table` with `my_new_dynamic_table`:

```sqlexample
ALTER DYNAMIC TABLE my_dynamic_table SWAP WITH my_new_dynamic_table;
```

Change the clustering key for a dynamic table:

```sqlexample
ALTER DYNAMIC TABLE my_dynamic_table CLUSTER BY (date);
```

Remove clustering from a dynamic table:

```sqlexample
ALTER DYNAMIC TABLE my_dynamic_table DROP CLUSTERING KEY;
```

Perform a manual refresh of `my_dynamic_table` using the user, secondary roles, and warehouse settings
from the current session. This ensures that the refresh operation runs with the exact context
of the user session.

```sqlexample
ALTER DYNAMIC TABLE my_dynamic_table REFRESH COPY SESSION
```

To modify or remove an existing constraint, you can replace a predicate:

```sqlexample
ALTER DYNAMIC TABLE my_dynamic_table SET IMMUTABLE WHERE ( <new_expr> );
```

Alternatively, remove an immutability predicate:

```sqlexample
ALTER DYNAMIC TABLE my_dynamic_table UNSET IMMUTABLE WHERE;
```
