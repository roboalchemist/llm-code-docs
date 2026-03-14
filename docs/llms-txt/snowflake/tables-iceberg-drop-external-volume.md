# Source: https://docs.snowflake.com/en/user-guide/tables-iceberg-drop-external-volume.md

# Drop an external volume by using Snowsight

Dropping an external volume removes the [external volume](tables-iceberg.md) from the account, but retains a version of the
external volume so that it can be recovered using [UNDROP EXTERNAL VOLUME](../sql-reference/sql/undrop-external-volume.md). For more information, see [Usage Notes for DROP EXTERNAL VOLUME](../sql-reference/sql/drop-external-volume.md).

> **Note:**
>
> To drop an external volume by using SQL, use the [DROP EXTERNAL VOLUME](../sql-reference/sql/drop-external-volume.md) command.

1. Sign in to [Snowsight](ui-snowsight-gs.md).
2. Switch to a role that has OWNERSHIP privilege on the external volume you want to drop.

   For instructions, see [Switch your primary role](ui-snowsight-gs.md).
3. In the navigation menu, select Catalog » External data.
4. Select the External volumes tab.
5. Select the external volume you want to drop.
6. Select … » Drop external volume.
7. Select Drop external volume again.
