# Source: https://docs.snowflake.com/en/release-notes/2025/other/2025-07-28-object-descriptions.md

# Jul 28, 2025: Cortex Powered Object Descriptions

## Ability to generate descriptions without being the owner

You can now use Snowflake Cortex to generate descriptions for Snowflake objects if you have the SELECT privilege on the object. Previously, you needed the OWNERSHIP privilege on the object. You still need the OWNERSHIP privilege if you want to save the generated description.

For the steps you take in Snowsight to generate a description, see [Generate descriptions without saving](../../../user-guide/ui-snowsight-cortex-descriptions.md).

For a complete list of roles and privileges you need to generate object descriptions, see [Cortex descriptions access control requirements](../../../user-guide/ui-snowsight-cortex-descriptions.md).
