# Source: https://docs.snowflake.com/en/release-notes/bcr-bundles/un-bundled/bcr-add-unversioned-status.md

# Snowflake Native App Framework Changes to the version output for the SHOW APPLICATIONS and DESC APPLICATION commands

For applications [created using staged files](../../../developer-guide/native-apps/installing-testing-application.md),
the output of the [SHOW APPLICATIONS](../../../sql-reference/sql/show-applications.md) and
[DESCRIBE APPLICATION](../../../sql-reference/sql/desc-application.md) will change as follows:

Before the change:
:   The value of the `version` column of the [SHOW APPLICATIONS](../../../sql-reference/sql/show-applications.md) command
    is `dev_stage`.

    The value of the `version` row of the [DESCRIBE APPLICATION](../../../sql-reference/sql/desc-application.md) command
    is `dev_stage`.

After the change:
:   The value of the `version` column of the [SHOW APPLICATIONS](../../../sql-reference/sql/show-applications.md) command
    will be `UNVERSIONED`.

    The value of the `version` row of the [DESCRIBE APPLICATION](../../../sql-reference/sql/desc-application.md) command
    is `UNVERSIONED`.

Ref: n/a
