# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/streamlit-commands/describe.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/stage-commands/describe.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/spcs-commands/service-commands/describe.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/spcs-commands/compute-pool-commands/describe.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/snowpark-commands/describe.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/object-commands/describe.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/git-commands/describe.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/dbt-commands/describe.md

# Source: https://docs.snowflake.com/en/sql-reference/classes/classification_profile/methods/describe.md

# <classification_profile_name>!DESCRIBE

Describes the properties of an instance of the CLASSIFICATION_PROFILE class.

## Syntax

```sqlsyntax
<classification_profile_name>!DESCRIBE()
```

## Output

The output includes the criteria you specified when [creating](../commands/create-classification-profile.md) the instance and is formatted as
follows:

```output
{
   "auto_tag": true | false ,
   "maximum_classification_validity_days": <integer>,
   "minimum_object_age_for_classification_days": <integer>
   "column_tag_map": <object>
   "custom_classifiers": <object>,
}
```

## Access control requirements

A [role](../../../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../../../user-guide/security-access-control-overview.md) at a minimum:

| Instance role | Object | Notes |
| --- | --- | --- |
| `classification_profile`!PRIVACY_USER | The classification profile instance. | The account role that calls this method must be granted this instance role on the classification profile. The role used to create the instance is automatically granted this instance role. |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../../../user-guide/security-access-control-overview.md).

## Usage notes

Calling this method does not return the object. Because of this, you can’t use method chaining to call another method on the
return value of this method. Instead, call each method in a separate SQL statement.

## Examples

Describe the classification profile:

```sqlexample
SELECT my_classification_profile!DESCRIBE();
```

```output
+--------------------------------------------------------+
|         MY_CLASSIFICATION_PROFILE!DESCRIBE()           |
+--------------------------------------------------------+
|   {                                                    |
|     "auto_tag": true,                                  |
|     "maximum_classification_validity_days": 30,        |
|     "column_tag_map": [                                |
|       {                                                |
|         "semantic_categories": [                       |
|           "NAME"                                       |
|         ],                                             |
|         "tag_name": "test_cc_db.test_cc_schema.pii_r3",|
|         "tag_value": "important"                       |
|       },                                               |
|      "custom_classifiers": {                           |
|        "PII": {                                        |
|          "SC1": {                                      |
|            "col_name_regex": "my_name",                |
|             "description": "a new semantic category",  |
|             "privacy_category": "IDENTIFIER",          |
|             "threshold": 0.8,                          |
|             "value_regex": "\\\\d{{2}}-\\\\d{{2}}"     |
|          },                                            |
|          "SC2": {                                      |
|            "privacy_category": "IDENTIFIER",           |
|            "threshold": 0.8,                           |
|            "value_regex": "\\\\d{{3}}-\\\\d{{3}}|\\\\d"|
|          }                                             |
|        }                                               |
|      },                                                |
       "minimum_object_age_for_classification_days": 1   |
|   }                                                    |
+--------------------------------------------------------+
```
