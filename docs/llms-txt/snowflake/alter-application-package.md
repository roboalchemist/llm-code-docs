# Source: https://docs.snowflake.com/en/sql-reference/sql/alter-application-package.md

# ALTER APPLICATION PACKAGE

Modifies the properties of an existing application package.

See also:
:   [CREATE APPLICATION PACKAGE](create-application-package.md), [DROP APPLICATION PACKAGE](drop-application-package.md), [SHOW APPLICATION PACKAGES](show-application-packages.md),
    [SHOW VERSIONS IN APPLICATION PACKAGE](show-versions.md), [SHOW RELEASE DIRECTIVES](show-release-directives.md)

## Syntax

```sqlsyntax
ALTER APPLICATION PACKAGE [ IF EXISTS ] <name> SET
  [ DATA_RETENTION_TIME_IN_DAYS = <integer> ]
  [ MAX_DATA_EXTENSION_TIME_IN_DAYS = <integer> ]
  [ DEFAULT_DDL_COLLATION = '<collation_specification>' ]
  [ COMMENT = <string-literal> ]
  [ DISTRIBUTION = { INTERNAL | EXTERNAL } ]
  [ MULTIPLE_INSTANCES = TRUE ]
  [ ENABLE_RELEASE_CHANNELS = TRUE ]
  [ SET LISTING_AUTO_REFRESH = { TRUE | FALSE } ]

ALTER APPLICATION PACKAGE [ IF EXISTS ] <name> UNSET
  [ DATA_RETENTION_TIME_IN_DAYS ]
  [ MAX_DATA_EXTENSION_TIME_IN_DAYS ]
  [ DEFAULT_DDL_COLLATION ]
  [ COMMENT  = <string-literal> ]
  [ DISTRIBUTION = { INTERNAL | EXTERNAL } ]

ALTER APPLICATION PACKAGE <name> SET TAG <tag_name> = '<tag_value>' [ , <tag_name> = '<tag_value>' ... ]

ALTER APPLICATION PACKAGE <name> UNSET TAG <tag_name> [ , <tag_name> ... ]
```

## Parameters

`name`
:   Specifies the identifier for the application package to alter. If the identifier contains
    spaces, special characters, or mixed-case characters, the entire string must be enclosed
    in double quotes. Identifiers enclosed in double quotes are also case-sensitive.

`SET ...`
:   Specifies one (or more) properties to set for the application package (separated by blank spaces, commas, or new lines):

    `DATA_RETENTION_TIME_IN_DAYS = num`
    :   Specifies the number of days for which Time Travel actions (CLONE and UNDROP) can be performed on the database, as well as specifying the
        default Time Travel retention time for all schemas created in the database.

        The value you can specify depends on the Snowflake Edition you are using:

        * Standard Edition: `0` or `1`
        * Enterprise Edition (or higher): `0` to `90`

    `MAX_DATA_EXTENSION_TIME_IN_DAYS = integer`
    :   Object parameter that specifies the maximum number of days for which Snowflake can extend the data retention period for tables in the database
        to prevent streams on the tables from becoming stale.

        For a detailed description of this parameter, see [MAX_DATA_EXTENSION_TIME_IN_DAYS](../parameters.md).

    `DEFAULT_DDL_COLLATION = 'collation_specification'`
    :   Specifies a default [collation specification](../collation.md) for:

        * Any new columns added to existing tables in the database.
        * All columns in new tables added to the database.

        Setting the parameter does not change the collation specification for any existing columns.

        For more information about the parameter, see [DEFAULT_DDL_COLLATION](../parameters.md).

    `COMMENT = 'string_literal'`
    :   Adds a comment or overwrites an existing comment for the database.

    `DISTRIBUTION = { INTERNAL | EXTERNAL }`
    :   Specifies the type of listing a provider can create when using the application package as the data product of a listing.

        * `INTERNAL` indicates that a provider can only create a private listing within the same organization
          where the application package was created. The automated security scan is not performed
          when the DISTRIBUTION property is set to INTERNAL.
        * `EXTERNAL` indicates that a provider can create listings outside the same organization where
          the application package was created.

        See [Run the automated security scan](../../developer-guide/native-apps/security-run-scan.md) for information on setting the DISTRIBUTION property and
        the automated security scan.

        > **Note:**
        >
        > Setting the `DISTRIBUTION` parameter to `EXTERNAL` triggers an automated security review for each
        > active version and patch defined in the application package.
        >
        > The following restrictions apply until the automated security review has a status of `APPROVED`:
        >
        > * You cannot set a release directive for a version or patch.
        > * You cannot publish a listing for the application package.

    `LISTING_AUTO_REFRESH = TRUE | FALSE`
    :   When set to TRUE, initiates replication to all remote regions when there is a change to the release directive of the application package. When a release directive changes, the application package does not wait for the Cross-Cloud Auto-Fulfillment schedule.

    `MULTIPLE_INSTANCES = TRUE`
    :   Enables the consumer to install multiple instances of an app from the application package. This property cannot be
        set for application packages that are included in a trial or paid listing.

        When multiple instances are allowed, consumers can install a maximum of 10 instances of an app in their account.

        > **Caution:**
        >
        > After setting this property to true, it cannot be set to `FALSE` or unset later.

    `ENABLE_RELEASE_CHANNELS = TRUE`
    :   Enables [release channels](../../developer-guide/native-apps/release-channels.md) for the application package.

        > **Caution:**
        >
        > After setting this property to `TRUE`, it cannot be set to `FALSE` or unset later.

`UNSET ...`
:   Specifies one (or more) properties and/or parameters to unset for the application package, which resets
    them to the defaults:

    * `DATA_RETENTION_TIME_IN_DAYS`
    * `MAX_DATA_EXTENSION_TIME_IN_DAYS`
    * `EXTERNAL_VOLUME`
    * `CATALOG`
    * `DEFAULT_DDL_COLLATION`
    * `TAG tag_name [ , tag_name ... ]`
    * `COMMENT`

    You can reset multiple properties/parameters with a single ALTER statement; however, each property/parameter must be separated by a
    comma. When resetting a property/parameter, specify only the name; specifying a value for the property will return an error.

## Usage notes

* If you do not specify the values for the optional properties, the command uses the values specified in the
  manifest file of the app.

  If you specify values for the properties in the command and in the manifest file of the app, the values specified in the command take precedence.
* If two versions are active (e.g. if the current version has not finished rolling out), adding a new version results in an error.
* New versions are added with a default patch number of 0.
* Regarding metadata:

  > **Attention:**
  >
  > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).

## Examples

```sqlexample
ALTER APPLICATION PACKAGE hello_snowflake_package SET
  COMMENT = 'Altered the Hello Snowflake app.';
```

```output
+-------------------------------------------+
| status                                    |
|-------------------------------------------|
| Statement executed successfully.          |
+-------------------------------------------+
```
