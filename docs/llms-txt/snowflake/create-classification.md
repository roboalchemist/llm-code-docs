# Source: https://docs.snowflake.com/en/sql-reference/classes/classification/commands/create-classification.md

# CREATE SNOWFLAKE.ML.CLASSIFICATION

Creates a new classification model or replaces an existing model in the current or specified schema.

See also:
:   [DROP SNOWFLAKE.ML.CLASSIFICATION](drop-classification.md)

## Syntax

```sqlsyntax
CREATE [ OR REPLACE ] SNOWFLAKE.ML.CLASSIFICATION [ IF NOT EXISTS ] <model_name> (
    INPUT_DATA => <input_data>,
    TARGET_COLNAME => '<target_colname>',
    [CONFIG_OBJECT => <config_object>],
)
[ [ WITH ] TAG ( <tag_name> = '<tag_value>' [ , <tag_name> = '<tag_value>' , ... ] ) ]
[ COMMENT = '<string_literal>' ]
```

## Parameters

*Required*

`input_data`
:   A [reference](../../../../developer-guide/stored-procedure/stored-procedures-calling-references.md) to the training data.
    Using a reference allows the training process, which runs with limited privileges, to use your active role’s
    privileges to access the data. You can use a reference to a table or a view if your data is already in that form, or
    you can use a [query reference](../../../../developer-guide/stored-procedure/stored-procedures-calling-references.md) to provide the query to be executed
    to obtain the data.

    INPUT_DATA must contain the entire training data to be consumed by the classification model. Any columns that are
    not named in the TARGET_COLNAME arguments are considered training variables (features). The order of the columns in
    the input data is not important.

    Feature columns must be STRING, NUMERIC, or BOOLEAN. STRING and BOOLEAN columns are treated as categorical features,
    while NUMERIC columns are considered continuous features. To treat a numeric column as categorical, cast it to STRING.

`target_colname`
:   Name of the column containing the label (target value) for each row in the training data. The target column may be
    BOOLEAN, NUMERIC, or STRING.

*Optional*

`config_object`
:   An [OBJECT](../../../data-types-semistructured.md) whose key-value pairs specify additional training options.

    | Key | Type | Default | Description |
    | --- | --- | --- | --- |
    | evaluate | [BOOLEAN](../../../data-types-logical.md) | TRUE | Whether evaluation metrics should be generated. If TRUE, then additional model is trained for evaluation using the parameters in the `evaluation_config`. |
    | on_error | STRING | ‘ABORT’ | String constant that specifies the error handling method for the model training task. Supported values are:   * `'ABORT'`: Abort the entire training operation if any row results in an error. * `'SKIP'`: Skip rows that result in an error. The error is shown instead of the results. |
    | evaluation_config | [OBJECT](../../../data-types-semistructured.md) | NULL | A optional configuration object to specify how out-of-sample evaluation metrics should be generated. Currently, there is only one such option.   * `test_fraction` (FLOAT): The fraction of the dataset that should be used as test (evaluation) data.   If evaluation configuration is not specified, the default behavior is to try to include a minimum of 500 instances of the minority class in the evaluation set and to limit the total test fraction of 20% of the dataset. This approach maintains balance in model evaluation and training, particularly for minority classes. |

## Access control requirements

A [role](../../../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege / Role | Object | Notes |
| --- | --- | --- |
| CREATE SNOWFLAKE.ML.CLASSIFICATION | Schema | The role used to create a budget must be granted this privilege on the schema in which the budget is created. |
| OWNERSHIP | Schema | A role must be granted or inherit the OWNERSHIP privilege on the object to create a temporary object that has the same name as the object that already exists in the schema. |
| `model_name`!mladmin | SNOWFLAKE.ML.CLASSIFICATION instance | This role, scoped to the model itself, is initially granted to the owner, who can grant it to others to allow them to call all of the model’s methods. See [Model Roles and Usage Privileges](../../../../user-guide/ml-functions/classification.md). |
| `model_name`!mlconsumer | SNOWFLAKE.ML.CLASSIFICATION instance | This role, scoped to the model itself, is initially granted to the owner, who can grant it to others to allow them to call the model’s prediction methods (such as `PREDICT`). See [Model Roles and Usage Privileges](../../../../user-guide/ml-functions/classification.md). |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../../../user-guide/security-access-control-overview.md).

## Example

See [Examples](../../../../user-guide/ml-functions/classification.md).
