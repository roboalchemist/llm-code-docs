# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/streamlit-commands/list.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/stage-commands/list.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/spcs-commands/service-commands/list.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/spcs-commands/image-repository-commands/list.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/spcs-commands/compute-pool-commands/list.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/snowpark-commands/list.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/object-commands/list.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/git-commands/list.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/dbt-commands/list.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/native-apps-commands/release-directive/list.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/native-apps-commands/release-channel/list.md

# Source: https://docs.snowflake.com/en/sql-reference/sql/list.md

# Source: https://docs.snowflake.com/en/sql-reference/classes/custom_classifier/methods/list.md

# `custom_classifier`!LIST

Lists each custom classification semantic category system tag with its associated regular expressions for the column name and values in the
column, the description, and the privacy category tag.

See also:
:   [Using custom classifiers to implement custom semantic categories](../../../../user-guide/classify-custom-using.md)

## Syntax

```sqlsyntax
<custom_classifier>!LIST()
```

## Arguments

None.

## Output

Returns a JSON object with the following structure:

```sqljson
{
  "semantic_category_name": {
    "col_name_regex": "string",
    "description": "string",
    "privacy_category": "string",
    "threshold": number,
    "value_regex": "string"
   }
}
```

Each field value corresponds to the value that you specify when calling the
[custom_classifier!ADD_REGEX](add_regex.md) method.

## Access control requirements

A [role](../../../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../../../user-guide/security-access-control-overview.md) at a minimum:

| Instance role | Object | Notes |
| --- | --- | --- |
| `custom_classifier`!PRIVACY_USER | The custom classifier instance. | The role that calls this method must be granted the instance role.  By default, the account role used to create the instance can call this method. |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../../../user-guide/security-access-control-overview.md).

## Usage notes

Call each method in a separate SQL statement (no method chaining).

## Examples

```sqlexample
SELECT medical_codes!LIST();
```

Returns:

```output
+--------------------------------------------------------------------------------+
| MEDICAL_CODES!LIST()                                                           |
+--------------------------------------------------------------------------------+
| {                                                                              |
|   "ICD-10-CODES": {                                                            |
|     "col_name_regex": "ICD.*",                                                 |
|     "description": "Add a regex to identify ICD-10 medical codes in a column", |
|     "privacy_category": "IDENTIFIER",                                          |
|     "threshold": 0.8,                                                          |
|     "value_regex": "[A-TV-Z][0-9][0-9AB]\.?[0-9A-TV-Z]{0,4}"                   |
|   }                                                                            |
| }                                                                              |
+--------------------------------------------------------------------------------+
```
