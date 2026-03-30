# Source: https://docs.snowflake.com/en/user-guide/classify-ui-trust-center.md

# Use the Trust Center to set up sensitive data classification

Trust Center lets you set up [sensitive data classification](classify-intro.md) in the Snowsight user interface, so you
don’t have to write any SQL code. After it is set up, sensitive data classification automatically identifies which data in a database is sensitive and needs to be protected.

## Get started

> **Note:**
>
> The following steps apply only to the first user who accesses the Data Security tab in the Trust Center. If you aren’t the first
> user and want to set up classification, see Set up classification with advanced settings.

To use a web interface to set up sensitive data classification, complete the following steps:

1. Sign in to [Snowsight](ui-snowsight-gs.md) as a user with the required privileges.
2. In the navigation menu, select Governance & security » Trust Center.
3. Select the Data Security tab.
4. Select Get started.
5. In the Set up auto-classification dialog, do the following:

   1. Select the databases that you want to classify.
   2. Specify whether you want to auto-apply tags instead of just recommending them. For more information about tags and categories, see [Core concepts of sensitive data classification](classify-intro.md).
6. Select Enable.
7. Select Close.

Based on this default set up, sensitive data classification has the following behavior:

* Reclassifies previously classified objects every 30 days.
* Scans data for all [native semantic categories](classify-native.md).
* Excludes views from classification.
* Bases classification on a sample of up to 10,000 randomly selected rows per table.

When the classification process is complete, you are ready to [view the results](classify-results.md).

## Set up classification with advanced settings

To set up sensitive data classification with advanced settings, complete the following steps:

1. Sign in to [Snowsight](ui-snowsight-gs.md) as a user with the required privileges.
2. In the navigation menu, select Governance & security » Trust Center.
3. Select the Data Security tab.
4. Select Settings.
5. Do one of the following:

   * If you’re fine-tuning existing classification settings, find the classification profile that contains the settings and
     select  » Edit. If the first person to set up classification chose the default settings during
     setup, the profile is `Default Snowflake profile`.
   * If you are creating a new [classification profile](classify-intro.md) so different databases can be
     classified with different settings, select Create New.
6. Select the databases that you want to scan for sensitive data.

   If a database is greyed out, it’s associated with an existing
   classification profile and is already being classified. You’ll need to edit the existing classification profile to remove the database
   before you can classify it with the settings of a new profile.
7. Select Next.
8. If your account classifies sensitive data into [custom categories](classify-custom.md), select the ones that you want to use.
9. Select Next.
10. If you don’t want tags automatically applied to columns containing sensitive data, deselect Auto-apply tags.
11. If you want to apply a user-defined tag in addition to a system tag on matching columns, do the following:

    1. In the Tag to apply column, select the user-defined tag/value pair that you want applied to sensitive data.
    2. In the Detected semantic categories column, select values of the `SNOWFLAKE.CORE.SEMANTIC_CATEGORY` tag. These can be
       native and custom semantic categories.

    For example, if you select `PII = CONFIDENTIAL` as the user-defined tag/value pair in Tag to apply, and
    then select the `NAME` semantic category in Detected semantic categories, when Snowflake assigns the
    `SNOWFLAKE.CORE.SEMANTIC_CATEGORY = NAME` system tag to a column, it also applies the `PII = CONFIDENTIAL` tag.
12. Select Next.
13. Specify the database, schema, and name of the [classification profile](classify-intro.md) where all of your
    settings will be saved.
14. Select the cadence at which previously classified objects are re-classified.
15. Specify if you want to exclude certain objects from the classification process. For information about excluding specific objects, see [Excluding data from sensitive data classification](classify-auto-exclude.md).
16. Select Enable.

## Classify additional databases

You can classify additional databases with the same classification settings by editing an existing classification profile. To edit a classification profile:

1. Sign in to [Snowsight](ui-snowsight-gs.md) as a user with the required privileges.
2. In the navigation menu, select Governance & security » Trust Center.
3. Select the Data Security tab.
4. Select Settings.
5. Find the classification profile in the list and select  » Edit. If the first person to set up classification used the default settings, the classification profile is `Default Snowflake profile`.
6. On the first page that appears, select the additional databases.
7. Complete the setup.

## Next steps

To view the results of sensitive data classification, see [Use the Trust Center to view results](classify-results.md).

## Access control requirements

> **Note:**
>
> The `DATA_SECURITY_*` application roles alone are not sufficient to access the Trust Center Data Security tab. You must have the
> SNOWFLAKE.TRUST_CENTER_VIEWER or SNOWFLAKE.TRUST_CENTER_ADMIN application role to use the Trust Center UI for classification. If your
> account previously relied on `DATA_SECURITY_*` roles, update your role grants accordingly.

| Task | Required privileges/roles | Notes |
| --- | --- | --- |
| Set up classification for a database | One of the following:   *SNOWFLAKE.TRUST_CENTER_VIEWER application role* SNOWFLAKE.TRUST_CENTER_ADMIN application role |  |
|  | EXECUTE AUTO CLASSIFICATION privilege on ACCOUNT |  |
|  | APPLY TAG privilege on ACCOUNT |  |
|  | USAGE on the database | More powerful privileges on the database meet this requirement. |
| Review classification insights and classified objects | One of the following:   *SNOWFLAKE.TRUST_CENTER_VIEWER application role* SNOWFLAKE.TRUST_CENTER_ADMIN application role |  |

**Example: Allow a user to set up classification**

To allow user `mary` to set up sensitive data classification and review classification findings, run the following commands:

```sqlexample
USE ROLE ACCOUNTADMIN;
CREATE ROLE trust_center_admin_role;

GRANT APPLICATION ROLE SNOWFLAKE.TRUST_CENTER_ADMIN TO ROLE trust_center_admin_role;
GRANT EXECUTE AUTO CLASSIFICATION ON ACCOUNT TO ROLE trust_center_admin_role;
GRANT APPLY TAG ON ACCOUNT TO ROLE trust_center_admin_role;
GRANT USAGE ON DATABASE mydb TO ROLE trust_center_admin_role;

GRANT ROLE trust_center_admin_role TO USER mary;
```

**Example: Allow user to review classification findings**

If you want user `joe` to be able to review classification findings, but not be able to set up classification, run the following commands:

```sqlexample
USE ROLE ACCOUNTADMIN;
CREATE ROLE trust_center_viewer_role;

GRANT APPLICATION ROLE SNOWFLAKE.TRUST_CENTER_VIEWER TO ROLE trust_center_viewer_role;

GRANT ROLE trust_center_viewer_role TO USER joe;
```
