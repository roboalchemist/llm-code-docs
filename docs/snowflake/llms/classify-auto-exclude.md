# Source: https://docs.snowflake.com/en/user-guide/classify-auto-exclude.md

# Excluding data from sensitive data classification

With sensitive data classification, Snowflake classifies data as sensitive at regular intervals without user intervention. You can
use settings and system tags to exclude certain data from this classification process.

For example, suppose a database `my_db` has three tables, `t1`, `t2`, and `t3`. By default, when you classify
`my_db`, all three tables are automatically classified. You can configure Snowflake to skip `t2` during classification so only
tables `t1` and `t3` are classified.

## Workflow

Excluding data from sensitive data classification is a two-step process:

1. Apply the SNOWFLAKE.CORE.SKIP_SENSITIVE_DATA_CLASSIFICATION tag to every object that you want
   excluded from sensitive data classification.
2. Enable the exclusion setting for tag-based sensitive data exclusion.

## Set tag on data objects

An [object tag](object-tagging/introduction.md) is an object that can be set on another object. Snowflake
provides a system-defined tag, SNOWFLAKE.CORE.SKIP_SENSITIVE_DATA_CLASSIFICATION, that you can set on objects that you want excluded from
sensitive data classification. When the value of this tag is `TRUE`, then Snowflake skips the object during classification.

You can set the SNOWFLAKE.CORE.SKIP_SENSITIVE_DATA_CLASSIFICATION tag on a schema, table, or column to control which data is excluded from
sensitive data classification.

Exclude a schema
:   You can set the SNOWFLAKE.CORE.SKIP_SENSITIVE_DATA_CLASSIFICATION tag on a schema in the database to exclude the schema from the
    classification process. For example:

    ```sqlexample
    ALTER SCHEMA my_schema SET TAG SNOWFLAKE.CORE.SKIP_SENSITIVE_DATA_CLASSIFICATION = 'TRUE';
    ```

Exclude a table
:   You can set the SNOWFLAKE.CORE.SKIP_SENSITIVE_DATA_CLASSIFICATION tag on a table in the database or schema to exclude the
    table from the classification process. For example:

    ```sqlexample
    ALTER TABLE my_table SET TAG SNOWFLAKE.CORE.SKIP_SENSITIVE_DATA_CLASSIFICATION = 'TRUE';
    ```

Exclude a column
:   You can set the SNOWFLAKE.CORE.SKIP_SENSITIVE_DATA_CLASSIFICATION tag on a column so that Snowflake skips it when classifying the
    table. If you exclude a column, the classification result contains an empty value for the column, even if it contains sensitive data.

    For example, suppose you want to automatically classify all columns in a table except the column `employee_id`. You can run the
    [ALTER TABLE … ALTER COLUMN](../sql-reference/sql/alter-table-column.md) command to set the system-defined tag on the column:

    ```sqlexample
    ALTER TABLE my_table ALTER COLUMN employee_id
      SET TAG SNOWFLAKE.CORE.SKIP_SENSITIVE_DATA_CLASSIFICATION = 'TRUE';
    ```

    When Snowflake automatically classifies data in the table, the `employee_id` field in the JSON result is empty.

For the access control requirements for setting the SNOWFLAKE.CORE.SKIP_SENSITIVE_DATA_CLASSIFICATION tag, see
Access control requirements.

## Enable the exclusion setting

Setting the SNOWFLAKE.CORE.SKIP_SENSITIVE_DATA_CLASSIFICATION tag on
objects has no effect until you enable the setting for tag-based sensitive data exclusion.

You can enable this setting using the Trust Center user interface or using SQL commands.

### Use the Trust Center to enable tag-based sensitive data exclusion

1. Sign in to [Snowsight](ui-snowsight-gs.md) as a user with the [required privileges](classify-ui-trust-center.md).
2. In the navigation menu, select Governance & security » Trust Center.
3. Select the Data Security tab.
4. Select the Settings tab.
5. Do one of the following:

   * If you are enabling the setting for an existing classification profile, find the profile and select  » Edit.
   * If you are setting up an advanced classification profile for the first time, select Create New.
6. Go through the classification settings until you get to the Define classification criteria page.
7. In the Exclusion criteria section, select Exclude SKIP_SENSITIVE_DATA_CLASSIFICATION tagged objects.

### Use SQL to enable tag-based sensitive data exclusion

A classification profile contains the settings that control how Snowflake automatically classifies data in a database. These
settings are specified using key-value pairs in an [OBJECT](../sql-reference/data-types-semistructured.md).

You must define the `enable_tag_based_sensitive_data_exclusion` key of the classification profile if you want data excluded from
sensitive data classification.

The following is an example of a classification profile that, when set on a database, excludes properly tagged objects from
sensitive data classification:

```sqlexample
CREATE OR REPLACE SNOWFLAKE.DATA_PRIVACY.CLASSIFICATION_PROFILE
  my_classification_profile(
    {
      'minimum_object_age_for_classification_days': 0,
      'maximum_classification_validity_days': 30,
      'auto_tag': true,
      'enable_tag_based_sensitive_data_exclusion': true
    });
```

You can also execute the [SET_ENABLE_TAG_BASED_SENSITIVE_DATA_EXCLUSION](../sql-reference/classes/classification_profile/methods/set_enable_tag_based_sensitive_data_exclusion.md) method to enable the setting for an existing classification profile.

## Access control requirements

By default, a user with the ability to enable or disable classification settings can set the
SNOWFLAKE.CORE.SKIP_SENSITIVE_DATA_CLASSIFICATION system tag only on their own schemas and tables.

If you want a user to be able to set the system tag on all objects, not just the ones they own, run the following command:

```sqlexample
GRANT APPLY TAG ON ACCOUNT TO ROLE <classify_user>;
```
