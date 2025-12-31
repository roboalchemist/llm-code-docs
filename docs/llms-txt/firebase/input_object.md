# Source: https://firebase.google.com/docs/reference/data-connect/gql/input_object.md.txt

This reference doc is generated based on this[example schema](https://firebase.google.com/docs/reference/data-connect#graphql_schema).

Input Object types define structured inputs that can be used as arguments in a GraphQL schema.

Data Connect generates input types to work with built in scalars and developer defined[`@table`](https://firebase.google.com/docs/reference/data-connect/gql/directive#table)types.

## Data Connect Defined

### input Any_Filter

Query filter criteria for[`Any`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Any)scalar fields.

|   Field   |                                           Type                                            |                                      Description                                       |
|-----------|-------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| `isNull`  | [`Boolean`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean)   | When true, match if field`IS NULL`. When false, match if field is`NOT NULL`.           |
| `eq`      | [`Any`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Any)           | Match if field is exactly equal to provided value.                                     |
| `eq_expr` | [`Any_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Any_Expr) | Match if field is exactly equal to the result of the provided server value expression. |
| `ne`      | [`Any`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Any)           | Match if field is not equal to provided value.                                         |
| `ne_expr` | [`Any_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Any_Expr) | Match if field is not equal to the result of the provided server value expression.     |
| `in`      | [`[Any!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Any)        | Match if field value is among the provided list of values.                             |
| `nin`     | [`[Any!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Any)        | Match if field value is not among the provided list of values.                         |

### input Any_ListFilter

Query filter criteria for[`[Any!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Any)scalar fields.

|     Field     |                                        Type                                        |                                 Description                                 |
|---------------|------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| `includes`    | [`Any`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Any)    | Match if list field contains the provided value as a member.                |
| `excludes`    | [`Any`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Any)    | Match if list field does not contain the provided value as a member.        |
| `includesAll` | [`[Any!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Any) | Match if list field contains all of the provided values as members.         |
| `excludesAll` | [`[Any!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Any) | Match if list field does not contain any of the provided values as members. |

### input Any_ListUpdate

Update input of an[`Any`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Any)list value. Only one of`append`,`prepend`,`add`, or`remove`may be specified.

|   Field   |                                        Type                                        |                        Description                        |
|-----------|------------------------------------------------------------------------------------|-----------------------------------------------------------|
| `append`  | [`[Any!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Any) | Append the provided list of values to the existing list.  |
| `prepend` | [`[Any!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Any) | Prepend the provided list of values to the existing list. |
| `add`     | [`[Any!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Any) | Append values that do not already exist to the list.      |
| `remove`  | [`[Any!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Any) | Remove all occurrences of each value from the list.       |

### input Boolean_Filter

Query filter criteria for[`Boolean`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean)scalar fields.

|   Field   |                                               Type                                                |                                 Description                                  |
|-----------|---------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| `isNull`  | [`Boolean`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean)           | When true, match if field`IS NULL`. When false, match if field is`NOT NULL`. |
| `eq`      | [`Boolean`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean)           | Match if field is exactly equal to provided value.                           |
| `eq_expr` | [`Boolean_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean_Expr) | Match if field is equal to the result of the provided expression.            |
| `ne`      | [`Boolean`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean)           | Match if field is not equal to provided value.                               |
| `ne_expr` | [`Boolean_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean_Expr) | Match if field does not match the result of the provided expression.         |
| `in`      | [`[Boolean!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean)        | Match if field value is among the provided list of values.                   |
| `nin`     | [`[Boolean!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean)        | Match if field value is not among the provided list of values.               |

### input Boolean_ListFilter

Query filter criteria for[`[Boolean!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean)scalar fields.

|     Field     |                                            Type                                            |                                 Description                                 |
|---------------|--------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| `includes`    | [`Boolean`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean)    | Match if list field contains the provided value as a member.                |
| `excludes`    | [`Boolean`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean)    | Match if list field does not contain the provided value as a member.        |
| `includesAll` | [`[Boolean!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean) | Match if list field contains all of the provided values as members.         |
| `excludesAll` | [`[Boolean!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean) | Match if list field does not contain any of the provided values as members. |

### input Boolean_ListUpdate

Update input of a[`Boolean`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean)list value. Only one of`append`,`prepend`,`add`, or`remove`may be specified.

|   Field   |                                            Type                                            |                        Description                        |
|-----------|--------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| `append`  | [`[Boolean!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean) | Append the provided list of values to the existing list.  |
| `prepend` | [`[Boolean!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean) | Prepend the provided list of values to the existing list. |
| `add`     | [`[Boolean!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean) | Append values that do not already exist to the list.      |
| `remove`  | [`[Boolean!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean) | Remove all occurrences of each value from the list.       |

### input Date_Duration

|  Field   |                                       Type                                       |              Description               |
|----------|----------------------------------------------------------------------------------|----------------------------------------|
| `days`   | [`Int!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int) | The number of days for the duration.   |
| `weeks`  | [`Int!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int) | The number of weeks for the duration.  |
| `months` | [`Int!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int) | The number of months for the duration. |
| `years`  | [`Int!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int) | The number of years for the duration.  |

### input Date_Filter

Conditions on a[`Date`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Date)value.

|   Field   |                                                   Type                                                    |                                    Description                                    |
|-----------|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| `isNull`  | [`Boolean`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean)                   | Match if the field`IS NULL`.                                                      |
| `eq`      | [`Date`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Date)                         | Match if the field is exactly equal to the provided value.                        |
| `eq_expr` | [`Date_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Date_Expr)               | Match if the field equals the provided CEL expression.                            |
| `eq_date` | [`Date_Relative`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Date_Relative) | Match if the field equals the provided relative date.                             |
| `ne`      | [`Date`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Date)                         | Match if the field is not equal to the provided value.                            |
| `ne_expr` | [`Date_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Date_Expr)               | Match if the field is not equal to the provided CEL expression.                   |
| `ne_date` | [`Date_Relative`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Date_Relative) | Match if the field is not equal to the provided relative date.                    |
| `in`      | [`[Date!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Date)                      | Match if the field value is among the provided list of values.                    |
| `nin`     | [`[Date!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Date)                      | Match if the field value is not among the provided list of values.                |
| `gt`      | [`Date`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Date)                         | Match if the field value is greater than the provided value.                      |
| `gt_expr` | [`Date_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Date_Expr)               | Match if the field value is greater than the provided CEL expression.             |
| `gt_date` | [`Date_Relative`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Date_Relative) | Match if the field value is greater than the provided relative date.              |
| `ge`      | [`Date`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Date)                         | Match if the field value is greater than or equal to the provided value.          |
| `ge_expr` | [`Date_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Date_Expr)               | Match if the field value is greater than or equal to the provided CEL expression. |
| `ge_date` | [`Date_Relative`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Date_Relative) | Match if the field value is greater than or equal to the provided relative date.  |
| `lt`      | [`Date`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Date)                         | Match if the field value is less than the provided value.                         |
| `lt_expr` | [`Date_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Date_Expr)               | Match if the field value is less than the provided CEL expression.                |
| `lt_date` | [`Date_Relative`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Date_Relative) | Match if the field value is less than the provided relative date.                 |
| `le`      | [`Date`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Date)                         | Match if the field value is less than or equal to the provided value.             |
| `le_expr` | [`Date_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Date_Expr)               | Match if the field value is less than or equal to the provided CEL expression.    |
| `le_date` | [`Date_Relative`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Date_Relative) | Match if the field value is less than or equal to the provided relative date.     |

### input Date_ListFilter

Conditions on a[`Date`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Date)list.

|      Field      |                                                   Type                                                    |                             Description                              |
|-----------------|-----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| `includes`      | [`Date`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Date)                         | Match if the list contains the provided date.                        |
| `includes_expr` | [`Date_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Date_Expr)               | Match if the list contains the provided date CEL expression.         |
| `includes_date` | [`Date_Relative`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Date_Relative) | Match if the list contains the provided relative date.               |
| `excludes`      | [`Date`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Date)                         | Match if the list does not contain the provided date.                |
| `excludes_expr` | [`Date_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Date_Expr)               | Match if the list does not contain the provided date CEL expression. |
| `excludes_date` | [`Date_Relative`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Date_Relative) | Match if the list does not contain the provided relative date.       |
| `includesAll`   | [`[Date!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Date)                      | Match if the list contains all the provided dates.                   |
| `excludesAll`   | [`[Date!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Date)                      | Match if the list contains none of the provided dates.               |

### input Date_ListUpdate

Update input of a[`Date`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Date)list value. Only one of`append`,`prepend`,`add`, or`remove`may be specified.

|   Field   |                                         Type                                         |                                                               Description                                                                |
|-----------|--------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| `append`  | [`[Date!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Date) | Append the provided[`Date`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Date)values to the existing list.         |
| `prepend` | [`[Date!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Date) | Prepend the provided[`Date`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Date)values to the existing list.        |
| `add`     | [`[Date!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Date) | Append any[`Date`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Date)values that do not already exist to the list. |
| `remove`  | [`[Date!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Date) | Remove all occurrences of each[`Date`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Date)from the list.            |

### input Date_Relative

A runtime-calculated Date value relative to`today`or`on`.

|    Field     |                                                   Type                                                    |                    Description                     |
|--------------|-----------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| `today`      | [`True`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#True)                         | Match for today's date.                            |
| `on`         | [`Date`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Date)                         | A specific date for matching.                      |
| `add`        | [`Date_Duration`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Date_Duration) | Add the provided duration to the base date.        |
| `sub`        | [`Date_Duration`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Date_Duration) | Subtract the provided duration from the base date. |
| `truncateTo` | [`Date_Interval`](https://firebase.google.com/docs/reference/data-connect/gql/enum#Date_Interval)         | Truncate the date to the provided interval.        |

### input Date_Update

Update input of a[`Date`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Date)value. Only one of`inc`or`dec`may be specified.

| Field |                                                   Type                                                    |                 Description                 |
|-------|-----------------------------------------------------------------------------------------------------------|---------------------------------------------|
| `inc` | [`Date_Duration`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Date_Duration) | Increment the field by a provided duration. |
| `dec` | [`Date_Duration`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Date_Duration) | Decrement the field by a provided duration. |

### input Float_Filter

Query filter criteria for[`Float`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Float)scalar fields.

|   Field   |                                             Type                                              |                                             Description                                              |
|-----------|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| `isNull`  | [`Boolean`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean)       | When true, match if field`IS NULL`. When false, match if field is`NOT NULL`.                         |
| `eq`      | [`Float`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Float)           | Match if field is exactly equal to provided value.                                                   |
| `eq_expr` | [`Float_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Float_Expr) | Match if field is exactly equal to the result of the provided server value expression.               |
| `ne`      | [`Float`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Float)           | Match if field is not equal to provided value.                                                       |
| `ne_expr` | [`Float_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Float_Expr) | Match if field is not equal to the result of the provided server value expression.                   |
| `in`      | [`[Float!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Float)        | Match if field value is among the provided list of values.                                           |
| `nin`     | [`[Float!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Float)        | Match if field value is not among the provided list of values.                                       |
| `gt`      | [`Float`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Float)           | Match if field value is greater than the provided value.                                             |
| `gt_expr` | [`Float_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Float_Expr) | Match if field value is greater than the result of the provided server value expression.             |
| `ge`      | [`Float`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Float)           | Match if field value is greater than or equal to the provided value.                                 |
| `ge_expr` | [`Float_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Float_Expr) | Match if field value is greater than or equal to the result of the provided server value expression. |
| `lt`      | [`Float`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Float)           | Match if field value is less than the provided value.                                                |
| `lt_expr` | [`Float_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Float_Expr) | Match if field value is less than the result of the provided server value expression.                |
| `le`      | [`Float`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Float)           | Match if field value is less than or equal to the provided value.                                    |
| `le_expr` | [`Float_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Float_Expr) | Match if field value is less than or equal to the result of the provided server value expression.    |

### input Float_ListFilter

Query filter criteria for[`[Float!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Float)scalar fields.

|     Field     |                                          Type                                          |                                 Description                                 |
|---------------|----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| `includes`    | [`Float`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Float)    | Match if list field contains the provided value as a member.                |
| `excludes`    | [`Float`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Float)    | Match if list field does not contain the provided value as a member.        |
| `includesAll` | [`[Float!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Float) | Match if list field contains all of the provided values as members.         |
| `excludesAll` | [`[Float!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Float) | Match if list field does not contain any of the provided values as members. |

### input Float_ListUpdate

Update input of a[`Float`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Float)list value. Only one of`append`,`prepend`,`add`, or`remove`may be specified.

|   Field   |                                          Type                                          |                        Description                        |
|-----------|----------------------------------------------------------------------------------------|-----------------------------------------------------------|
| `append`  | [`[Float!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Float) | Append the provided list of values to the existing list.  |
| `prepend` | [`[Float!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Float) | Prepend the provided list of values to the existing list. |
| `add`     | [`[Float!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Float) | Append values that do not already exist to the list.      |
| `remove`  | [`[Float!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Float) | Remove all occurrences of each value from the list.       |

### input Float_Update

Update input of a[`Float`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Float)value. Only one of`inc`or`dec`may be specified.

| Field |                                        Type                                         |               Description                |
|-------|-------------------------------------------------------------------------------------|------------------------------------------|
| `inc` | [`Float`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Float) | Increment the field by a provided value. |
| `dec` | [`Float`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Float) | Decrement the field by a provided value. |

### input Int64_Filter

Query filter criteria for[`Int64`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int64)scalar fields.

|   Field   |                                             Type                                              |                                             Description                                              |
|-----------|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| `isNull`  | [`Boolean`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean)       | When true, match if field`IS NULL`. When false, match if field is`NOT NULL`.                         |
| `eq`      | [`Int64`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int64)           | Match if field is exactly equal to provided value.                                                   |
| `eq_expr` | [`Int64_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int64_Expr) | Match if field is exactly equal to the result of the provided server value expression.               |
| `ne`      | [`Int64`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int64)           | Match if field is not equal to provided value.                                                       |
| `ne_expr` | [`Int64_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int64_Expr) | Match if field is not equal to the result of the provided server value expression.                   |
| `in`      | [`[Int64!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int64)        | Match if field value is among the provided list of values.                                           |
| `nin`     | [`[Int64!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int64)        | Match if field value is not among the provided list of values.                                       |
| `gt`      | [`Int64`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int64)           | Match if field value is greater than the provided value.                                             |
| `gt_expr` | [`Int64_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int64_Expr) | Match if field value is greater than the result of the provided server value expression.             |
| `ge`      | [`Int64`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int64)           | Match if field value is greater than or equal to the provided value.                                 |
| `ge_expr` | [`Int64_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int64_Expr) | Match if field value is greater than or equal to the result of the provided server value expression. |
| `lt`      | [`Int64`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int64)           | Match if field value is less than the provided value.                                                |
| `lt_expr` | [`Int64_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int64_Expr) | Match if field value is less than the result of the provided server value expression.                |
| `le`      | [`Int64`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int64)           | Match if field value is less than or equal to the provided value.                                    |
| `le_expr` | [`Int64_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int64_Expr) | Match if field value is less than or equal to the result of the provided server value expression.    |

### input Int64_ListFilter

Query filter criteria for[`[Int64!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int64)scalar fields.

|     Field     |                                          Type                                          |                                 Description                                 |
|---------------|----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| `includes`    | [`Int64`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int64)    | Match if list field contains the provided value as a member.                |
| `excludes`    | [`Int64`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int64)    | Match if list field does not contain the provided value as a member.        |
| `includesAll` | [`[Int64!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int64) | Match if list field contains all of the provided values as members.         |
| `excludesAll` | [`[Int64!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int64) | Match if list field does not contain any of the provided values as members. |

### input Int64_ListUpdate

Update input of an[`Int64`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int64)list value. Only one of`append`,`prepend`,`add`, or`remove`may be specified.

|   Field   |                                          Type                                          |                        Description                        |
|-----------|----------------------------------------------------------------------------------------|-----------------------------------------------------------|
| `append`  | [`[Int64!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int64) | Append the provided list of values to the existing list.  |
| `prepend` | [`[Int64!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int64) | Prepend the provided list of values to the existing list. |
| `add`     | [`[Int64!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int64) | Append values that do not already exist to the list.      |
| `remove`  | [`[Int64!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int64) | Remove all occurrences of each value from the list.       |

### input Int64_Update

Update input of an[`Int64`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int64)value. Only one of`inc`or`dec`may be specified.

| Field |                                        Type                                         |               Description                |
|-------|-------------------------------------------------------------------------------------|------------------------------------------|
| `inc` | [`Int64`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int64) | Increment the field by a provided value. |
| `dec` | [`Int64`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int64) | Decrement the field by a provided value. |

### input Int_Filter

Query filter criteria for[`Int`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int)scalar fields.

|   Field   |                                           Type                                            |                                             Description                                              |
|-----------|-------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| `isNull`  | [`Boolean`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean)   | When true, match if field`IS NULL`. When false, match if field is`NOT NULL`.                         |
| `eq`      | [`Int`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int)           | Match if field is exactly equal to provided value.                                                   |
| `eq_expr` | [`Int_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int_Expr) | Match if field is exactly equal to the result of the provided server value expression.               |
| `ne`      | [`Int`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int)           | Match if field is not equal to provided value.                                                       |
| `ne_expr` | [`Int_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int_Expr) | Match if field is not equal to the result of the provided server value expression.                   |
| `in`      | [`[Int!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int)        | Match if field value is among the provided list of values.                                           |
| `nin`     | [`[Int!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int)        | Match if field value is not among the provided list of values.                                       |
| `gt`      | [`Int`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int)           | Match if field value is greater than the provided value.                                             |
| `gt_expr` | [`Int_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int_Expr) | Match if field value is greater than the result of the provided server value expression.             |
| `ge`      | [`Int`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int)           | Match if field value is greater than or equal to the provided value.                                 |
| `ge_expr` | [`Int_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int_Expr) | Match if field value is greater than or equal to the result of the provided server value expression. |
| `lt`      | [`Int`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int)           | Match if field value is less than the provided value.                                                |
| `lt_expr` | [`Int_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int_Expr) | Match if field value is less than the result of the provided server value expression.                |
| `le`      | [`Int`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int)           | Match if field value is less than or equal to the provided value.                                    |
| `le_expr` | [`Int_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int_Expr) | Match if field value is less than or equal to the result of the provided server value expression.    |

### input Int_ListFilter

Query filter criteris for[`[Int!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int)scalar fields.

|     Field     |                                        Type                                        |                                 Description                                 |
|---------------|------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| `includes`    | [`Int`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int)    | Match if list field contains the provided value as a member.                |
| `excludes`    | [`Int`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int)    | Match if list field does not contain the provided value as a member.        |
| `includesAll` | [`[Int!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int) | Match if list field contains all of the provided values as members.         |
| `excludesAll` | [`[Int!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int) | Match if list field does not contain any of the provided values as members. |

### input Int_ListUpdate

Update input of an[`Int`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int)list value. Only one of`append`,`prepend`,`add`, or`remove`may be specified.

|   Field   |                                        Type                                        |                        Description                        |
|-----------|------------------------------------------------------------------------------------|-----------------------------------------------------------|
| `append`  | [`[Int!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int) | Append the provided list of values to the existing list.  |
| `prepend` | [`[Int!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int) | Prepend the provided list of values to the existing list. |
| `add`     | [`[Int!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int) | Append values that do not already exist to the list.      |
| `remove`  | [`[Int!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int) | Remove all occurrences of each value from the list.       |

### input Int_Update

Update input of an[`Int`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int)value. Only one of`inc`or`dec`may be specified.

| Field |                                      Type                                       |               Description                |
|-------|---------------------------------------------------------------------------------|------------------------------------------|
| `inc` | [`Int`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int) | Increment the field by a provided value. |
| `dec` | [`Int`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int) | Decrement the field by a provided value. |

### input String_Filter

Query filter criteria for[`String`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String)scalar fields.

|    Field     |                                              Type                                               |                                                                  Description                                                                  |
|--------------|-------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| `isNull`     | [`Boolean`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean)         | When true, match if field`IS NULL`. When false, match if field is`NOT NULL`.                                                                  |
| `eq`         | [`String`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String)           | Match if field is exactly equal to provided value.                                                                                            |
| `eq_expr`    | [`String_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String_Expr) | Match if field is exactly equal to the result of the provided server value expression. Currently only`auth.uid`is supported as an expression. |
| `ne`         | [`String`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String)           | Match if field is not equal to provided value.                                                                                                |
| `ne_expr`    | [`String_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String_Expr) | Match if field is not equal to the result of the provided server value expression. Currently only`auth.uid`is supported as an expression.     |
| `in`         | [`[String!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String)        | Match if field value is among the provided list of values.                                                                                    |
| `nin`        | [`[String!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String)        | Match if field value is not among the provided list of values.                                                                                |
| `gt`         | [`String`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String)           | Match if field value is greater than the provided value.                                                                                      |
| `ge`         | [`String`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String)           | Match if field value is greater than or equal to the provided value.                                                                          |
| `lt`         | [`String`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String)           | Match if field value is less than the provided value.                                                                                         |
| `le`         | [`String`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String)           | Match if field value is less than or equal to the provided value.                                                                             |
| `contains`   | [`String`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String)           | Match if field value contains the provided value as a substring. Equivalent to`LIKE '%value%'`                                                |
| `startsWith` | [`String`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String)           | Match if field value starts with the provided value. Equivalent to`LIKE 'value%'`                                                             |
| `endsWith`   | [`String`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String)           | Match if field value ends with the provided value. Equivalent to`LIKE '%value'`                                                               |

### input String_ListFilter

Query filter criteris for[`[String!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String)scalar fields.

|     Field     |                                           Type                                           |                                 Description                                 |
|---------------|------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| `includes`    | [`String`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String)    | Match if list field contains the provided value as a member.                |
| `excludes`    | [`String`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String)    | Match if list field does not contain the provided value as a member.        |
| `includesAll` | [`[String!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String) | Match if list field contains all of the provided values as members.         |
| `excludesAll` | [`[String!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String) | Match if list field does not contain any of the provided values as members. |

### input String_ListUpdate

Update input of a[`String`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String)list value. Only one of`append`,`prepend`,`add`, or`remove`may be specified.

|   Field   |                                           Type                                           |                     Description                      |
|-----------|------------------------------------------------------------------------------------------|------------------------------------------------------|
| `append`  | [`[String!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String) | Append the provided values to the existing list.     |
| `prepend` | [`[String!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String) | Prepend the provided values to the existing list.    |
| `add`     | [`[String!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String) | Append values that do not already exist to the list. |
| `remove`  | [`[String!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String) | Remove all occurrences of each value from the list.  |

### input Timestamp_Duration

|     Field      |                                       Type                                       |                 Description                  |
|----------------|----------------------------------------------------------------------------------|----------------------------------------------|
| `milliseconds` | [`Int!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int) | The number of milliseconds for the duration. |
| `seconds`      | [`Int!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int) | The number of seconds for the duration.      |
| `minutes`      | [`Int!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int) | The number of minutes for the duration.      |
| `hours`        | [`Int!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int) | The number of hours for the duration.        |
| `days`         | [`Int!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int) | The number of days for the duration.         |
| `weeks`        | [`Int!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int) | The number of weeks for the duration.        |
| `months`       | [`Int!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int) | The number of months for the duration.       |
| `years`        | [`Int!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int) | The number of years for the duration.        |

### input Timestamp_Filter

Conditions on a[`Timestamp`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Timestamp)value.

|   Field   |                                                        Type                                                         |                                    Description                                    |
|-----------|---------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| `isNull`  | [`Boolean`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean)                             | Match if the field`IS NULL`.                                                      |
| `eq`      | [`Timestamp`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Timestamp)                         | Match if the field is exactly equal to the provided value.                        |
| `eq_expr` | [`Timestamp_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Timestamp_Expr)               | Match if the field equals the provided CEL expression.                            |
| `eq_time` | [`Timestamp_Relative`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Timestamp_Relative) | Match if the field equals the provided relative time.                             |
| `ne`      | [`Timestamp`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Timestamp)                         | Match if the field is not equal to the provided value.                            |
| `ne_expr` | [`Timestamp_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Timestamp_Expr)               | Match if the field is not equal to the provided CEL expression.                   |
| `ne_time` | [`Timestamp_Relative`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Timestamp_Relative) | Match if the field is not equal to the provided relative time.                    |
| `in`      | [`[Timestamp!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Timestamp)                      | Match if the field value is among the provided list of values.                    |
| `nin`     | [`[Timestamp!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Timestamp)                      | Match if the field value is not among the provided list of values.                |
| `gt`      | [`Timestamp`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Timestamp)                         | Match if the field value is greater than the provided value.                      |
| `gt_expr` | [`Timestamp_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Timestamp_Expr)               | Match if the field value is greater than the provided CEL expression.             |
| `gt_time` | [`Timestamp_Relative`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Timestamp_Relative) | Match if the field value is greater than the provided relative time.              |
| `ge`      | [`Timestamp`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Timestamp)                         | Match if the field value is greater than or equal to the provided value.          |
| `ge_expr` | [`Timestamp_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Timestamp_Expr)               | Match if the field value is greater than or equal to the provided CEL expression. |
| `ge_time` | [`Timestamp_Relative`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Timestamp_Relative) | Match if the field value is greater than or equal to the provided relative time.  |
| `lt`      | [`Timestamp`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Timestamp)                         | Match if the field value is less than the provided value.                         |
| `lt_expr` | [`Timestamp_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Timestamp_Expr)               | Match if the field value is less than the provided CEL expression.                |
| `lt_time` | [`Timestamp_Relative`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Timestamp_Relative) | Match if the field value is less than the provided relative time.                 |
| `le`      | [`Timestamp`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Timestamp)                         | Match if the field value is less than or equal to the provided value.             |
| `le_expr` | [`Timestamp_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Timestamp_Expr)               | Match if the field value is less than or equal to the provided CEL expression.    |
| `le_time` | [`Timestamp_Relative`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Timestamp_Relative) | Match if the field value is less than or equal to the provided relative time.     |

### input Timestamp_ListFilter

Conditions on a[`Timestamp`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Timestamp)list.

|      Field      |                                                        Type                                                         |                                Description                                |
|-----------------|---------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| `includes`      | [`Timestamp`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Timestamp)                         | Match if the list contains the provided timestamp.                        |
| `includes_expr` | [`Timestamp_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Timestamp_Expr)               | Match if the list contains the provided timestamp CEL expression.         |
| `includes_time` | [`Timestamp_Relative`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Timestamp_Relative) | Match if the list contains the provided relative timestamp.               |
| `excludes`      | [`Timestamp`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Timestamp)                         | Match if the list does not contain the provided timestamp.                |
| `excludes_expr` | [`Timestamp_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Timestamp_Expr)               | Match if the list does not contain the provided timestamp CEL expression. |
| `excludes_time` | [`Timestamp_Relative`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Timestamp_Relative) | Match if the list does not contain the provided relative timestamp.       |
| `includesAll`   | [`[Timestamp!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Timestamp)                      | Match if the list contains all the provided timestamps.                   |
| `excludesAll`   | [`[Timestamp!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Timestamp)                      | Match if the list contains none of the provided timestamps.               |

### input Timestamp_ListUpdate

Update input of an[`Timestamp`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Timestamp)list value. Only one of`append`,`prepend`,`add`, or`remove`may be specified.

|   Field   |                                              Type                                              |                                                                    Description                                                                     |
|-----------|------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| `append`  | [`[Timestamp!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Timestamp) | Append the provided[`Timestamp`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Timestamp)values to the existing list.         |
| `prepend` | [`[Timestamp!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Timestamp) | Prepend the provided[`Timestamp`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Timestamp)values to the existing list.        |
| `add`     | [`[Timestamp!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Timestamp) | Append any[`Timestamp`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Timestamp)values that do not already exist to the list. |
| `remove`  | [`[Timestamp!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Timestamp) | Remove all occurrences of each[`Timestamp`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Timestamp)from the list.            |

### input Timestamp_Relative

A runtime-calculated[`Timestamp`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Timestamp)value relative to`now`or`at`.

|    Field     |                                                        Type                                                         |                       Description                       |
|--------------|---------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| `now`        | [`True`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#True)                                   | Match for the current time.                             |
| `at`         | [`Timestamp`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Timestamp)                         | A specific timestamp for matching.                      |
| `add`        | [`Timestamp_Duration`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Timestamp_Duration) | Add the provided duration to the base timestamp.        |
| `sub`        | [`Timestamp_Duration`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Timestamp_Duration) | Subtract the provided duration from the base timestamp. |
| `truncateTo` | [`Timestamp_Interval`](https://firebase.google.com/docs/reference/data-connect/gql/enum#Timestamp_Interval)         | Truncate the timestamp to the provided interval.        |

### input Timestamp_Update

Update input of a[`Timestamp`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Timestamp)value. Only one of`inc`or`dec`may be specified.

| Field |                                                        Type                                                         |                 Description                 |
|-------|---------------------------------------------------------------------------------------------------------------------|---------------------------------------------|
| `inc` | [`Timestamp_Duration`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Timestamp_Duration) | Increment the field by a provided duration. |
| `dec` | [`Timestamp_Duration`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Timestamp_Duration) | Decrement the field by a provided duration. |

### input UUID_Filter

Query filter criteria for[`UUID`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)scalar fields.

|   Field   |                                            Type                                             |                                      Description                                       |
|-----------|---------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| `isNull`  | [`Boolean`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean)     | When true, match if field`IS NULL`. When false, match if field is`NOT NULL`.           |
| `eq`      | [`UUID`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)           | Match if field is exactly equal to provided value.                                     |
| `eq_expr` | [`UUID_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID_Expr) | Match if field is exactly equal to the result of the provided server value expression. |
| `ne`      | [`UUID`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)           | Match if field is not equal to provided value.                                         |
| `ne_expr` | [`UUID_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID_Expr) | Match if field is not equal to the result of the provided server value expression.     |
| `in`      | [`[UUID!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)        | Match if field value is among the provided list of values.                             |
| `nin`     | [`[UUID!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)        | Match if field value is not among the provided list of values.                         |

### input UUID_ListFilter

Query filter criteris for[`[UUID!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)scalar fields.

|     Field     |                                         Type                                         |                                 Description                                 |
|---------------|--------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| `includes`    | [`UUID`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)    | Match if list field contains the provided value as a member.                |
| `excludes`    | [`UUID`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)    | Match if list field does not contain the provided value as a member.        |
| `includesAll` | [`[UUID!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID) | Match if list field contains all of the provided values as members.         |
| `excludesAll` | [`[UUID!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID) | Match if list field does not contain any of the provided values as members. |

### input UUID_ListUpdate

Update input of an[`ID`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#ID)list value. Only one of`append`,`prepend`,`add`, or`remove`may be specified.

|   Field   |                                         Type                                         |                     Description                      |
|-----------|--------------------------------------------------------------------------------------|------------------------------------------------------|
| `append`  | [`[UUID!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID) | Append the provided UUIDs to the existing list.      |
| `prepend` | [`[UUID!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID) | Prepend the provided UUIDs to the existing list.     |
| `add`     | [`[UUID!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID) | Append values that do not already exist to the list. |
| `remove`  | [`[UUID!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID) | Remove all occurrences of each value from the list.  |

### input Vector_Embed

Create a vector embedding of text using the given model on Vertex AI.

Cloud SQL for Postgresql natively integrates with[Vertex AI Text embeddings API](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/text-embeddings-api)to effectively generate text embeddings.

If you uses[](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Vector)[`Vector`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Vector)in your schema, Firebase Data Connect automatically installs[`pgvector`](https://github.com/pgvector/pgvector)and[`google_ml_integration`](https://cloud.google.com/sql/docs/postgres/integrate-cloud-sql-with-vertex-ai)Postgres extensions in your Cloud SQL database.

Given a Post table with a[`Vector`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Vector)embedding field.  

    type Post @table {
      content: String!
      contentEmbedding: Vector @col(size:768)
    }

NOTE: All natively supported[`Vector_Embed_Model`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Vector_Embed_Model)generates vector of length`768`.

###### Example: Insert embedding

    mutation CreatePost($content: String!) {
      post_insert(data: {
        content: $content,
        contentEmbedding_embed: {model: "textembedding-gecko@003", text: $content},
      })
    }

###### Example: Vector similarity Search

    query SearchPost($query: String!) {
      posts_contentEmbedding_similarity(compare_embed: {model: "textembedding-gecko@003", text: $query}) {
        id
        content
      }
    }

|  Field  |                                                      Type                                                      |                                             Description                                             |
|---------|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| `model` | [`Vector_Embed_Model!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Vector_Embed_Model) | The model to use for vector embedding. Recommend the latest stable model:`textembedding-gecko@003`. |
| `text`  | [`String!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String)                         | The text to generate the vector embedding from.                                                     |

### input Vector_Filter

Conditions on a Vector value.

|  Field   |                                           Type                                           |                             Description                             |
|----------|------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| `eq`     | [`Vector`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Vector)    | Match if the field is exactly equal to the provided vector.         |
| `ne`     | [`Vector`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Vector)    | Match if the field is not equal to the provided vector.             |
| `in`     | [`[Vector!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Vector) | Match if the field value is among the provided list of vectors.     |
| `nin`    | [`[Vector!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Vector) | Match if the field value is not among the provided list of vectors. |
| `isNull` | [`Boolean`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean)  | Match if the field is`NULL`.                                        |

### input Vector_ListFilter

|     Field     |                                           Type                                           |                       Description                        |
|---------------|------------------------------------------------------------------------------------------|----------------------------------------------------------|
| `includes`    | [`Vector`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Vector)    | Match if the list includes the supplied vector.          |
| `excludes`    | [`Vector`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Vector)    | Match if the list does not include the supplied vector.  |
| `includesAll` | [`[Vector!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Vector) | Match if the list contains all the provided vectors.     |
| `excludesAll` | [`[Vector!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Vector) | Match if the list contains none of the provided vectors. |

## Data Connect Generated

### input MainTable_Data

â¨ Generated data input type for table 'MainTable'. It includes all necessary fields for creating or upserting rows into table.

|          Field          |                                                            Type                                                            |                                                                                                                                        Description                                                                                                                                        |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`                    | [`UUID`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)                                          | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`id`of type[`UUID!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)                                                                           |
| `id_expr`               | [`UUID_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID_Expr)                                | â¨`_expr`server value variant of`id`(â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`id`of type[`UUID!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID))                                      |
| `anyArray`              | [`[Any!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Any)                                         | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`anyArray`of type[`[Any]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Any)                                                                      |
| `anyArray_update`       | [`[Any_ListUpdate!]`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Any_ListUpdate)             | â¨`_update`server value variant of`anyArray`(â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`anyArray`of type[`[Any]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Any))                         |
| `anyField`              | [`Any`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Any)                                            | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`anyField`of type[`Any`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Any)                                                                        |
| `anyField_expr`         | [`Any_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Any_Expr)                                  | â¨`_expr`server value variant of`anyField`(â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`anyField`of type[`Any`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Any))                             |
| `booleanArray`          | [`[Boolean!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean)                                 | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`booleanArray`of type[`[Boolean]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean)                                                          |
| `booleanArray_update`   | [`[Boolean_ListUpdate!]`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Boolean_ListUpdate)     | â¨`_update`server value variant of`booleanArray`(â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`booleanArray`of type[`[Boolean]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean))         |
| `booleanField`          | [`Boolean`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean)                                    | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`booleanField`of type[`Boolean`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean)                                                            |
| `booleanField_expr`     | [`Boolean_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean_Expr)                          | â¨`_expr`server value variant of`booleanField`(â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`booleanField`of type[`Boolean`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean))             |
| `dateArray`             | [`[Date!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Date)                                       | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`dateArray`of type[`[Date]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Date)                                                                   |
| `dateArray_update`      | [`[Date_ListUpdate!]`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Date_ListUpdate)           | â¨`_update`server value variant of`dateArray`(â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`dateArray`of type[`[Date]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Date))                     |
| `dateField`             | [`Date`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Date)                                          | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`dateField`of type[`Date`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Date)                                                                     |
| `dateField_expr`        | [`Date_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Date_Expr)                                | â¨`_expr`server value variant of`dateField`(â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`dateField`of type[`Date`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Date))                         |
| `dateField_date`        | [`Date_Relative`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Date_Relative)                  | â¨`_date`server value variant of`dateField`(â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`dateField`of type[`Date`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Date))                         |
| `dateField_update`      | [`[Date_Update!]`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Date_Update)                   | â¨`_update`server value variant of`dateField`(â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`dateField`of type[`Date`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Date))                       |
| `floatArray`            | [`[Float!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Float)                                     | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`floatArray`of type[`[Float]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Float)                                                                |
| `floatArray_update`     | [`[Float_ListUpdate!]`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Float_ListUpdate)         | â¨`_update`server value variant of`floatArray`(â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`floatArray`of type[`[Float]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Float))                 |
| `floatField`            | [`Float`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Float)                                        | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`floatField`of type[`Float`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Float)                                                                  |
| `floatField_expr`       | [`Float_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Float_Expr)                              | â¨`_expr`server value variant of`floatField`(â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`floatField`of type[`Float`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Float))                     |
| `floatField_update`     | [`[Float_Update!]`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Float_Update)                 | â¨`_update`server value variant of`floatField`(â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`floatField`of type[`Float`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Float))                   |
| `int64Array`            | [`[Int64!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int64)                                     | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`int64Array`of type[`[Int64]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int64)                                                                |
| `int64Array_update`     | [`[Int64_ListUpdate!]`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Int64_ListUpdate)         | â¨`_update`server value variant of`int64Array`(â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`int64Array`of type[`[Int64]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int64))                 |
| `int64Field`            | [`Int64`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int64)                                        | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`int64Field`of type[`Int64`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int64)                                                                  |
| `int64Field_expr`       | [`Int64_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int64_Expr)                              | â¨`_expr`server value variant of`int64Field`(â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`int64Field`of type[`Int64`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int64))                     |
| `int64Field_update`     | [`[Int64_Update!]`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Int64_Update)                 | â¨`_update`server value variant of`int64Field`(â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`int64Field`of type[`Int64`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int64))                   |
| `intArray`              | [`[Int!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int)                                         | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`intArray`of type[`[Int]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int)                                                                      |
| `intArray_update`       | [`[Int_ListUpdate!]`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Int_ListUpdate)             | â¨`_update`server value variant of`intArray`(â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`intArray`of type[`[Int]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int))                         |
| `intField`              | [`Int`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int)                                            | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`intField`of type[`Int`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int)                                                                        |
| `intField_expr`         | [`Int_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int_Expr)                                  | â¨`_expr`server value variant of`intField`(â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`intField`of type[`Int`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int))                             |
| `intField_update`       | [`[Int_Update!]`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Int_Update)                     | â¨`_update`server value variant of`intField`(â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`intField`of type[`Int`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int))                           |
| `stringArray`           | [`[String!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String)                                   | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`stringArray`of type[`[String]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String)                                                             |
| `stringArray_update`    | [`[String_ListUpdate!]`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#String_ListUpdate)       | â¨`_update`server value variant of`stringArray`(â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`stringArray`of type[`[String]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String))             |
| `stringField`           | [`String`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String)                                      | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`stringField`of type[`String`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String)                                                               |
| `stringField_expr`      | [`String_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String_Expr)                            | â¨`_expr`server value variant of`stringField`(â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`stringField`of type[`String`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String))                 |
| `timestampArray`        | [`[Timestamp!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Timestamp)                             | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`timestampArray`of type[`[Timestamp]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Timestamp)                                                    |
| `timestampArray_update` | [`[Timestamp_ListUpdate!]`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Timestamp_ListUpdate) | â¨`_update`server value variant of`timestampArray`(â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`timestampArray`of type[`[Timestamp]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Timestamp)) |
| `timestampField`        | [`Timestamp`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Timestamp)                                | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`timestampField`of type[`Timestamp`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Timestamp)                                                      |
| `timestampField_expr`   | [`Timestamp_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Timestamp_Expr)                      | â¨`_expr`server value variant of`timestampField`(â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`timestampField`of type[`Timestamp`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Timestamp))     |
| `timestampField_time`   | [`Timestamp_Relative`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Timestamp_Relative)        | â¨`_time`server value variant of`timestampField`(â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`timestampField`of type[`Timestamp`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Timestamp))     |
| `timestampField_update` | [`[Timestamp_Update!]`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Timestamp_Update)         | â¨`_update`server value variant of`timestampField`(â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`timestampField`of type[`Timestamp`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Timestamp))   |
| `uuidArray`             | [`[UUID!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)                                       | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`uuidArray`of type[`[UUID]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)                                                                   |
| `uuidArray_update`      | [`[UUID_ListUpdate!]`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#UUID_ListUpdate)           | â¨`_update`server value variant of`uuidArray`(â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`uuidArray`of type[`[UUID]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID))                     |
| `uuidField`             | [`UUID`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)                                          | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`uuidField`of type[`UUID`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)                                                                     |
| `uuidField_expr`        | [`UUID_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID_Expr)                                | â¨`_expr`server value variant of`uuidField`(â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`uuidField`of type[`UUID`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID))                         |
| `vectorField`           | [`Vector`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Vector)                                      | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`vectorField`of type[`Vector`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Vector)                                                               |
| `vectorField_embed`     | [`Vector_Embed`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Vector_Embed)                    | â¨`_embed`server value variant of`vectorField`(â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`vectorField`of type[`Vector`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Vector))                |

### input MainTable_Filter

â¨ Generated filter input type for table 'MainTable'. This input allows filtering objects using various conditions. Use`_or`,`_and`, and`_not`to compose complex filters.

|                     Field                     |                                                                    Type                                                                     |                                                                                                                                 Description                                                                                                                                 |
|-----------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `_and`                                        | [`[MainTable_Filter!]`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#MainTable_Filter)                          | Apply multiple filter conditions using`AND`logic.                                                                                                                                                                                                                           |
| `_or`                                         | [`[MainTable_Filter!]`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#MainTable_Filter)                          | Apply multiple filter conditions using`OR`logic.                                                                                                                                                                                                                            |
| `_not`                                        | [`MainTable_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#MainTable_Filter)                             | Negate the result of the provided filter condition.                                                                                                                                                                                                                         |
| `id`                                          | [`UUID_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#UUID_Filter)                                       | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`id`of type[`UUID!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)                                                             |
| `anyArray`                                    | [`Any_ListFilter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Any_ListFilter)                                 | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`anyArray`of type[`[Any]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Any)                                                        |
| `anyField`                                    | [`Any_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Any_Filter)                                         | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`anyField`of type[`Any`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Any)                                                          |
| `booleanArray`                                | [`Boolean_ListFilter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Boolean_ListFilter)                         | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`booleanArray`of type[`[Boolean]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean)                                            |
| `booleanField`                                | [`Boolean_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Boolean_Filter)                                 | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`booleanField`of type[`Boolean`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean)                                              |
| `dateArray`                                   | [`Date_ListFilter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Date_ListFilter)                               | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`dateArray`of type[`[Date]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Date)                                                     |
| `dateField`                                   | [`Date_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Date_Filter)                                       | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`dateField`of type[`Date`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Date)                                                       |
| `floatArray`                                  | [`Float_ListFilter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Float_ListFilter)                             | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`floatArray`of type[`[Float]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Float)                                                  |
| `floatField`                                  | [`Float_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Float_Filter)                                     | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`floatField`of type[`Float`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Float)                                                    |
| `int64Array`                                  | [`Int64_ListFilter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Int64_ListFilter)                             | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`int64Array`of type[`[Int64]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int64)                                                  |
| `int64Field`                                  | [`Int64_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Int64_Filter)                                     | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`int64Field`of type[`Int64`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int64)                                                    |
| `intArray`                                    | [`Int_ListFilter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Int_ListFilter)                                 | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`intArray`of type[`[Int]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int)                                                        |
| `intField`                                    | [`Int_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Int_Filter)                                         | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`intField`of type[`Int`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int)                                                          |
| `stringArray`                                 | [`String_ListFilter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#String_ListFilter)                           | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`stringArray`of type[`[String]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String)                                               |
| `stringField`                                 | [`String_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#String_Filter)                                   | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`stringField`of type[`String`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String)                                                 |
| `timestampArray`                              | [`Timestamp_ListFilter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Timestamp_ListFilter)                     | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`timestampArray`of type[`[Timestamp]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Timestamp)                                      |
| `timestampField`                              | [`Timestamp_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Timestamp_Filter)                             | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`timestampField`of type[`Timestamp`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Timestamp)                                        |
| `uuidArray`                                   | [`UUID_ListFilter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#UUID_ListFilter)                               | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`uuidArray`of type[`[UUID]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)                                                     |
| `uuidField`                                   | [`UUID_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#UUID_Filter)                                       | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`uuidField`of type[`UUID`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)                                                       |
| `vectorField`                                 | [`Vector_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Vector_Filter)                                   | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`vectorField`of type[`Vector`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Vector)                                                 |
| `manyToManyJoinTables_on_left`                | [`ManyToManyJoinTable_ListFilter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#ManyToManyJoinTable_ListFilter) | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`manyToManyJoinTables_on_left`of type[`[ManyToManyJoinTable!]!`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToManyJoinTable)  |
| `manyToManyJoinTables_on_right`               | [`ManyToManyJoinTable_ListFilter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#ManyToManyJoinTable_ListFilter) | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`manyToManyJoinTables_on_right`of type[`[ManyToManyJoinTable!]!`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToManyJoinTable) |
| `manyToOneExamples_on_main`                   | [`ManyToOneExample_ListFilter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#ManyToOneExample_ListFilter)       | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`manyToOneExamples_on_main`of type[`[ManyToOneExample!]!`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToOneExample)           |
| `oneToOneExample_on_main`                     | [`OneToOneExample_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#OneToOneExample_Filter)                 | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`oneToOneExample_on_main`of type[`OneToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#OneToOneExample)                   |
| `mainTables_via_ManyToManyJoinTable_on_left`  | [`MainTable_ListFilter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#MainTable_ListFilter)                     | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`mainTables_via_ManyToManyJoinTable_on_left`of type[`[MainTable!]!`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable)        |
| `mainTables_via_ManyToManyJoinTable_on_right` | [`MainTable_ListFilter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#MainTable_ListFilter)                     | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`mainTables_via_ManyToManyJoinTable_on_right`of type[`[MainTable!]!`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable)       |

### input MainTable_FirstRow

â¨ Generated first-row input type for table 'MainTable'. This input selects the first row matching the filter criteria, ordered according to the specified conditions.

|   Field   |                                                       Type                                                       |                   Description                   |
|-----------|------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| `where`   | [`MainTable_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#MainTable_Filter)  | Filters rows based on the specified conditions. |
| `orderBy` | [`[MainTable_Order!]`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#MainTable_Order) | Order the result by the specified fields.       |

### input MainTable_Having

â¨ Generated having input type for table 'MainTable'. This input allows you to filter groups during aggregate queries using various conditions. Use`_or`,`_and`, and`_not`to compose complex filters.

|         Field          |                                                        Type                                                        |                                                                                                               Description                                                                                                                |
|------------------------|--------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `_and`                 | [`[MainTable_Having!]`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#MainTable_Having) | Apply multiple Having conditions using`AND`logic.                                                                                                                                                                                        |
| `_or`                  | [`[MainTable_Having!]`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#MainTable_Having) | Apply multiple Having conditions using`OR`logic.                                                                                                                                                                                         |
| `_not`                 | [`MainTable_Having`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#MainTable_Having)    | Negate the result of the provided Having condition.                                                                                                                                                                                      |
| `_distinct`            | [`Boolean`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean)                            | Whether to apply DISTINCT to the aggregate function.                                                                                                                                                                                     |
| `_count`               | [`Int_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Int_Filter)                | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`_count`of type[`Int!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int)                        |
| `anyField_count`       | [`Int_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Int_Filter)                | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`anyField_count`of type[`Int!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int)                |
| `booleanField_count`   | [`Int_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Int_Filter)                | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`booleanField_count`of type[`Int!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int)            |
| `dateField_count`      | [`Int_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Int_Filter)                | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`dateField_count`of type[`Int!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int)               |
| `floatField_count`     | [`Int_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Int_Filter)                | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`floatField_count`of type[`Int!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int)              |
| `id_count`             | [`Int_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Int_Filter)                | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`id_count`of type[`Int!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int)                      |
| `int64Field_count`     | [`Int_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Int_Filter)                | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`int64Field_count`of type[`Int!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int)              |
| `intField_count`       | [`Int_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Int_Filter)                | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`intField_count`of type[`Int!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int)                |
| `stringField_count`    | [`Int_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Int_Filter)                | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`stringField_count`of type[`Int!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int)             |
| `timestampField_count` | [`Int_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Int_Filter)                | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`timestampField_count`of type[`Int!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int)          |
| `uuidField_count`      | [`Int_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Int_Filter)                | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`uuidField_count`of type[`Int!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int)               |
| `vectorField_count`    | [`Int_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Int_Filter)                | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`vectorField_count`of type[`Int!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int)             |
| `floatField_sum`       | [`Float_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Float_Filter)            | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`floatField_sum`of type[`Float`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Float)             |
| `int64Field_sum`       | [`Int64_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Int64_Filter)            | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`int64Field_sum`of type[`Int64`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int64)             |
| `intField_sum`         | [`Int_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Int_Filter)                | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`intField_sum`of type[`Int`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int)                   |
| `floatField_avg`       | [`Float_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Float_Filter)            | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`floatField_avg`of type[`Float`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Float)             |
| `int64Field_avg`       | [`Float_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Float_Filter)            | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`int64Field_avg`of type[`Float`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Float)             |
| `intField_avg`         | [`Float_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Float_Filter)            | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`intField_avg`of type[`Float`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Float)               |
| `anyField_min`         | [`Any_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Any_Filter)                | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`anyField_min`of type[`Any`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Any)                   |
| `dateField_min`        | [`Date_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Date_Filter)              | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`dateField_min`of type[`Date`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Date)                |
| `floatField_min`       | [`Float_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Float_Filter)            | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`floatField_min`of type[`Float`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Float)             |
| `int64Field_min`       | [`Int64_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Int64_Filter)            | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`int64Field_min`of type[`Int64`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int64)             |
| `intField_min`         | [`Int_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Int_Filter)                | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`intField_min`of type[`Int`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int)                   |
| `timestampField_min`   | [`Timestamp_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Timestamp_Filter)    | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`timestampField_min`of type[`Timestamp`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Timestamp) |
| `anyField_max`         | [`Any_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Any_Filter)                | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`anyField_max`of type[`Any`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Any)                   |
| `dateField_max`        | [`Date_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Date_Filter)              | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`dateField_max`of type[`Date`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Date)                |
| `floatField_max`       | [`Float_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Float_Filter)            | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`floatField_max`of type[`Float`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Float)             |
| `int64Field_max`       | [`Int64_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Int64_Filter)            | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`int64Field_max`of type[`Int64`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int64)             |
| `intField_max`         | [`Int_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Int_Filter)                | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`intField_max`of type[`Int`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int)                   |
| `timestampField_max`   | [`Timestamp_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Timestamp_Filter)    | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`timestampField_max`of type[`Timestamp`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Timestamp) |

### input MainTable_Key

â¨ Generated key input type for table 'MainTable'. It represents the primary key fields used to uniquely identify a row in the table.

|   Field   |                                            Type                                             |                                                                                                                     Description                                                                                                                      |
|-----------|---------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`      | [`UUID`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)           | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`id`of type[`UUID!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)                                      |
| `id_expr` | [`UUID_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID_Expr) | â¨`_expr`server value variant of`id`(â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`id`of type[`UUID!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)) |

### input MainTable_ListFilter

â¨ Generated list filter input type for table 'MainTable'. This input applies filtering logic based on the count or existence of related objects that matches certain criteria.

|  Field  |                                                      Type                                                       |                                    Description                                     |
|---------|-----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| `count` | [`Int_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Int_Filter)             | The desired number of objects that match the condition (defaults to at least one). |
| `exist` | [`MainTable_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#MainTable_Filter) | Condition of the related objects to filter for.                                    |

### input MainTable_Order

â¨ Generated order input type for table 'MainTable'. This input defines the sorting order of rows in query results based on one or more fields.

|      Field       |                                                Type                                                 |                                                                                                             Description                                                                                                              |
|------------------|-----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`             | [`OrderDirection`](https://firebase.google.com/docs/reference/data-connect/gql/enum#OrderDirection) | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`id`of type[`UUID!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)                      |
| `anyField`       | [`OrderDirection`](https://firebase.google.com/docs/reference/data-connect/gql/enum#OrderDirection) | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`anyField`of type[`Any`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Any)                   |
| `booleanField`   | [`OrderDirection`](https://firebase.google.com/docs/reference/data-connect/gql/enum#OrderDirection) | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`booleanField`of type[`Boolean`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean)       |
| `dateField`      | [`OrderDirection`](https://firebase.google.com/docs/reference/data-connect/gql/enum#OrderDirection) | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`dateField`of type[`Date`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Date)                |
| `floatField`     | [`OrderDirection`](https://firebase.google.com/docs/reference/data-connect/gql/enum#OrderDirection) | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`floatField`of type[`Float`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Float)             |
| `int64Field`     | [`OrderDirection`](https://firebase.google.com/docs/reference/data-connect/gql/enum#OrderDirection) | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`int64Field`of type[`Int64`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int64)             |
| `intField`       | [`OrderDirection`](https://firebase.google.com/docs/reference/data-connect/gql/enum#OrderDirection) | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`intField`of type[`Int`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int)                   |
| `stringField`    | [`OrderDirection`](https://firebase.google.com/docs/reference/data-connect/gql/enum#OrderDirection) | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`stringField`of type[`String`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String)          |
| `timestampField` | [`OrderDirection`](https://firebase.google.com/docs/reference/data-connect/gql/enum#OrderDirection) | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`timestampField`of type[`Timestamp`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Timestamp) |
| `uuidField`      | [`OrderDirection`](https://firebase.google.com/docs/reference/data-connect/gql/enum#OrderDirection) | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`uuidField`of type[`UUID`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)                |
| `vectorField`    | [`OrderDirection`](https://firebase.google.com/docs/reference/data-connect/gql/enum#OrderDirection) | â¨ Generated from Field[`MainTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable).`vectorField`of type[`Vector`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Vector)          |

### input ManyToManyJoinTable_Data

â¨ Generated data input type for table 'ManyToManyJoinTable'. It includes all necessary fields for creating or upserting rows into table.

|     Field      |                                                   Type                                                    |                                                                                                                                    Description                                                                                                                                     |
|----------------|-----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `leftId`       | [`UUID`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)                         | â¨ Generated from Field[`ManyToManyJoinTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToManyJoinTable).`leftId`of type[`UUID!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)                                            |
| `leftId_expr`  | [`UUID_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID_Expr)               | â¨`_expr`server value variant of`leftId`(â¨ Generated from Field[`ManyToManyJoinTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToManyJoinTable).`leftId`of type[`UUID!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID))   |
| `rightId`      | [`UUID`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)                         | â¨ Generated from Field[`ManyToManyJoinTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToManyJoinTable).`rightId`of type[`UUID!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)                                           |
| `rightId_expr` | [`UUID_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID_Expr)               | â¨`_expr`server value variant of`rightId`(â¨ Generated from Field[`ManyToManyJoinTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToManyJoinTable).`rightId`of type[`UUID!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)) |
| `left`         | [`MainTable_Key`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#MainTable_Key) | â¨ Generated from Field[`ManyToManyJoinTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToManyJoinTable).`left`of type[`MainTable!`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable)                                    |
| `right`        | [`MainTable_Key`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#MainTable_Key) | â¨ Generated from Field[`ManyToManyJoinTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToManyJoinTable).`right`of type[`MainTable!`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable)                                   |

### input ManyToManyJoinTable_Filter

â¨ Generated filter input type for table 'ManyToManyJoinTable'. This input allows filtering objects using various conditions. Use`_or`,`_and`, and`_not`to compose complex filters.

|   Field   |                                                                  Type                                                                  |                                                                                                                   Description                                                                                                                    |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `_and`    | [`[ManyToManyJoinTable_Filter!]`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#ManyToManyJoinTable_Filter) | Apply multiple filter conditions using`AND`logic.                                                                                                                                                                                                |
| `_or`     | [`[ManyToManyJoinTable_Filter!]`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#ManyToManyJoinTable_Filter) | Apply multiple filter conditions using`OR`logic.                                                                                                                                                                                                 |
| `_not`    | [`ManyToManyJoinTable_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#ManyToManyJoinTable_Filter)    | Negate the result of the provided filter condition.                                                                                                                                                                                              |
| `leftId`  | [`UUID_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#UUID_Filter)                                  | â¨ Generated from Field[`ManyToManyJoinTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToManyJoinTable).`leftId`of type[`UUID!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)          |
| `rightId` | [`UUID_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#UUID_Filter)                                  | â¨ Generated from Field[`ManyToManyJoinTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToManyJoinTable).`rightId`of type[`UUID!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)         |
| `left`    | [`MainTable_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#MainTable_Filter)                        | â¨ Generated from Field[`ManyToManyJoinTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToManyJoinTable).`left`of type[`MainTable!`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable)  |
| `right`   | [`MainTable_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#MainTable_Filter)                        | â¨ Generated from Field[`ManyToManyJoinTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToManyJoinTable).`right`of type[`MainTable!`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable) |

### input ManyToManyJoinTable_FirstRow

â¨ Generated first-row input type for table 'ManyToManyJoinTable'. This input selects the first row matching the filter criteria, ordered according to the specified conditions.

|   Field   |                                                                 Type                                                                 |                   Description                   |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| `where`   | [`ManyToManyJoinTable_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#ManyToManyJoinTable_Filter)  | Filters rows based on the specified conditions. |
| `orderBy` | [`[ManyToManyJoinTable_Order!]`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#ManyToManyJoinTable_Order) | Order the result by the specified fields.       |

### input ManyToManyJoinTable_Having

â¨ Generated having input type for table 'ManyToManyJoinTable'. This input allows you to filter groups during aggregate queries using various conditions. Use`_or`,`_and`, and`_not`to compose complex filters.

|      Field      |                                                                  Type                                                                  |                                                                                                                 Description                                                                                                                  |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `_and`          | [`[ManyToManyJoinTable_Having!]`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#ManyToManyJoinTable_Having) | Apply multiple Having conditions using`AND`logic.                                                                                                                                                                                            |
| `_or`           | [`[ManyToManyJoinTable_Having!]`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#ManyToManyJoinTable_Having) | Apply multiple Having conditions using`OR`logic.                                                                                                                                                                                             |
| `_not`          | [`ManyToManyJoinTable_Having`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#ManyToManyJoinTable_Having)    | Negate the result of the provided Having condition.                                                                                                                                                                                          |
| `_distinct`     | [`Boolean`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean)                                                | Whether to apply DISTINCT to the aggregate function.                                                                                                                                                                                         |
| `_count`        | [`Int_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Int_Filter)                                    | â¨ Generated from Field[`ManyToManyJoinTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToManyJoinTable).`_count`of type[`Int!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int)        |
| `leftId_count`  | [`Int_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Int_Filter)                                    | â¨ Generated from Field[`ManyToManyJoinTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToManyJoinTable).`leftId_count`of type[`Int!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int)  |
| `rightId_count` | [`Int_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Int_Filter)                                    | â¨ Generated from Field[`ManyToManyJoinTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToManyJoinTable).`rightId_count`of type[`Int!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int) |

### input ManyToManyJoinTable_Key

â¨ Generated key input type for table 'ManyToManyJoinTable'. It represents the primary key fields used to uniquely identify a row in the table.

|     Field      |                                            Type                                             |                                                                                                                                    Description                                                                                                                                     |
|----------------|---------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `leftId`       | [`UUID`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)           | â¨ Generated from Field[`ManyToManyJoinTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToManyJoinTable).`leftId`of type[`UUID!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)                                            |
| `leftId_expr`  | [`UUID_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID_Expr) | â¨`_expr`server value variant of`leftId`(â¨ Generated from Field[`ManyToManyJoinTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToManyJoinTable).`leftId`of type[`UUID!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID))   |
| `rightId`      | [`UUID`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)           | â¨ Generated from Field[`ManyToManyJoinTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToManyJoinTable).`rightId`of type[`UUID!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)                                           |
| `rightId_expr` | [`UUID_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID_Expr) | â¨`_expr`server value variant of`rightId`(â¨ Generated from Field[`ManyToManyJoinTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToManyJoinTable).`rightId`of type[`UUID!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)) |

### input ManyToManyJoinTable_ListFilter

â¨ Generated list filter input type for table 'ManyToManyJoinTable'. This input applies filtering logic based on the count or existence of related objects that matches certain criteria.

|  Field  |                                                                Type                                                                 |                                    Description                                     |
|---------|-------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| `count` | [`Int_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Int_Filter)                                 | The desired number of objects that match the condition (defaults to at least one). |
| `exist` | [`ManyToManyJoinTable_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#ManyToManyJoinTable_Filter) | Condition of the related objects to filter for.                                    |

### input ManyToManyJoinTable_Order

â¨ Generated order input type for table 'ManyToManyJoinTable'. This input defines the sorting order of rows in query results based on one or more fields.

|   Field   |                                                     Type                                                      |                                                                                                                   Description                                                                                                                    |
|-----------|---------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `leftId`  | [`OrderDirection`](https://firebase.google.com/docs/reference/data-connect/gql/enum#OrderDirection)           | â¨ Generated from Field[`ManyToManyJoinTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToManyJoinTable).`leftId`of type[`UUID!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)          |
| `rightId` | [`OrderDirection`](https://firebase.google.com/docs/reference/data-connect/gql/enum#OrderDirection)           | â¨ Generated from Field[`ManyToManyJoinTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToManyJoinTable).`rightId`of type[`UUID!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)         |
| `left`    | [`MainTable_Order`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#MainTable_Order) | â¨ Generated from Field[`ManyToManyJoinTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToManyJoinTable).`left`of type[`MainTable!`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable)  |
| `right`   | [`MainTable_Order`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#MainTable_Order) | â¨ Generated from Field[`ManyToManyJoinTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToManyJoinTable).`right`of type[`MainTable!`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable) |

### input ManyToOneExample_Data

â¨ Generated data input type for table 'ManyToOneExample'. It includes all necessary fields for creating or upserting rows into table.

|      Field       |                                                   Type                                                    |                                                                                                                                  Description                                                                                                                                  |
|------------------|-----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`             | [`UUID`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)                         | â¨ Generated from Field[`ManyToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToOneExample).`id`of type[`UUID!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)                                                 |
| `id_expr`        | [`UUID_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID_Expr)               | â¨`_expr`server value variant of`id`(â¨ Generated from Field[`ManyToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToOneExample).`id`of type[`UUID!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID))            |
| `mainId`         | [`UUID`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)                         | â¨ Generated from Field[`ManyToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToOneExample).`mainId`of type[`UUID!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)                                             |
| `mainId_expr`    | [`UUID_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID_Expr)               | â¨`_expr`server value variant of`mainId`(â¨ Generated from Field[`ManyToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToOneExample).`mainId`of type[`UUID!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID))    |
| `main`           | [`MainTable_Key`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#MainTable_Key) | â¨ Generated from Field[`ManyToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToOneExample).`main`of type[`MainTable!`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable)                                     |
| `someField`      | [`Any`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Any)                           | â¨ Generated from Field[`ManyToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToOneExample).`someField`of type[`Any`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Any)                                             |
| `someField_expr` | [`Any_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Any_Expr)                 | â¨`_expr`server value variant of`someField`(â¨ Generated from Field[`ManyToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToOneExample).`someField`of type[`Any`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Any)) |

### input ManyToOneExample_Filter

â¨ Generated filter input type for table 'ManyToOneExample'. This input allows filtering objects using various conditions. Use`_or`,`_and`, and`_not`to compose complex filters.

|    Field    |                                                               Type                                                               |                                                                                                                Description                                                                                                                |
|-------------|----------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `_and`      | [`[ManyToOneExample_Filter!]`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#ManyToOneExample_Filter) | Apply multiple filter conditions using`AND`logic.                                                                                                                                                                                         |
| `_or`       | [`[ManyToOneExample_Filter!]`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#ManyToOneExample_Filter) | Apply multiple filter conditions using`OR`logic.                                                                                                                                                                                          |
| `_not`      | [`ManyToOneExample_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#ManyToOneExample_Filter)    | Negate the result of the provided filter condition.                                                                                                                                                                                       |
| `id`        | [`UUID_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#UUID_Filter)                            | â¨ Generated from Field[`ManyToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToOneExample).`id`of type[`UUID!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)             |
| `mainId`    | [`UUID_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#UUID_Filter)                            | â¨ Generated from Field[`ManyToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToOneExample).`mainId`of type[`UUID!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)         |
| `main`      | [`MainTable_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#MainTable_Filter)                  | â¨ Generated from Field[`ManyToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToOneExample).`main`of type[`MainTable!`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable) |
| `someField` | [`Any_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Any_Filter)                              | â¨ Generated from Field[`ManyToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToOneExample).`someField`of type[`Any`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Any)         |

### input ManyToOneExample_FirstRow

â¨ Generated first-row input type for table 'ManyToOneExample'. This input selects the first row matching the filter criteria, ordered according to the specified conditions.

|   Field   |                                                              Type                                                              |                   Description                   |
|-----------|--------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| `where`   | [`ManyToOneExample_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#ManyToOneExample_Filter)  | Filters rows based on the specified conditions. |
| `orderBy` | [`[ManyToOneExample_Order!]`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#ManyToOneExample_Order) | Order the result by the specified fields.       |

### input ManyToOneExample_Having

â¨ Generated having input type for table 'ManyToOneExample'. This input allows you to filter groups during aggregate queries using various conditions. Use`_or`,`_and`, and`_not`to compose complex filters.

|       Field       |                                                               Type                                                               |                                                                                                               Description                                                                                                                |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `_and`            | [`[ManyToOneExample_Having!]`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#ManyToOneExample_Having) | Apply multiple Having conditions using`AND`logic.                                                                                                                                                                                        |
| `_or`             | [`[ManyToOneExample_Having!]`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#ManyToOneExample_Having) | Apply multiple Having conditions using`OR`logic.                                                                                                                                                                                         |
| `_not`            | [`ManyToOneExample_Having`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#ManyToOneExample_Having)    | Negate the result of the provided Having condition.                                                                                                                                                                                      |
| `_distinct`       | [`Boolean`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean)                                          | Whether to apply DISTINCT to the aggregate function.                                                                                                                                                                                     |
| `_count`          | [`Int_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Int_Filter)                              | â¨ Generated from Field[`ManyToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToOneExample).`_count`of type[`Int!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int)          |
| `id_count`        | [`Int_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Int_Filter)                              | â¨ Generated from Field[`ManyToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToOneExample).`id_count`of type[`Int!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int)        |
| `mainId_count`    | [`Int_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Int_Filter)                              | â¨ Generated from Field[`ManyToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToOneExample).`mainId_count`of type[`Int!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int)    |
| `someField_count` | [`Int_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Int_Filter)                              | â¨ Generated from Field[`ManyToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToOneExample).`someField_count`of type[`Int!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int) |
| `someField_min`   | [`Any_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Any_Filter)                              | â¨ Generated from Field[`ManyToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToOneExample).`someField_min`of type[`Any`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Any)    |
| `someField_max`   | [`Any_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Any_Filter)                              | â¨ Generated from Field[`ManyToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToOneExample).`someField_max`of type[`Any`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Any)    |

### input ManyToOneExample_Key

â¨ Generated key input type for table 'ManyToOneExample'. It represents the primary key fields used to uniquely identify a row in the table.

|   Field   |                                            Type                                             |                                                                                                                            Description                                                                                                                             |
|-----------|---------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`      | [`UUID`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)           | â¨ Generated from Field[`ManyToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToOneExample).`id`of type[`UUID!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)                                      |
| `id_expr` | [`UUID_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID_Expr) | â¨`_expr`server value variant of`id`(â¨ Generated from Field[`ManyToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToOneExample).`id`of type[`UUID!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)) |

### input ManyToOneExample_ListFilter

â¨ Generated list filter input type for table 'ManyToOneExample'. This input applies filtering logic based on the count or existence of related objects that matches certain criteria.

|  Field  |                                                             Type                                                              |                                    Description                                     |
|---------|-------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| `count` | [`Int_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Int_Filter)                           | The desired number of objects that match the condition (defaults to at least one). |
| `exist` | [`ManyToOneExample_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#ManyToOneExample_Filter) | Condition of the related objects to filter for.                                    |

### input ManyToOneExample_Order

â¨ Generated order input type for table 'ManyToOneExample'. This input defines the sorting order of rows in query results based on one or more fields.

|    Field    |                                                     Type                                                      |                                                                                                                Description                                                                                                                |
|-------------|---------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`        | [`OrderDirection`](https://firebase.google.com/docs/reference/data-connect/gql/enum#OrderDirection)           | â¨ Generated from Field[`ManyToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToOneExample).`id`of type[`UUID!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)             |
| `mainId`    | [`OrderDirection`](https://firebase.google.com/docs/reference/data-connect/gql/enum#OrderDirection)           | â¨ Generated from Field[`ManyToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToOneExample).`mainId`of type[`UUID!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)         |
| `main`      | [`MainTable_Order`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#MainTable_Order) | â¨ Generated from Field[`ManyToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToOneExample).`main`of type[`MainTable!`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable) |
| `someField` | [`OrderDirection`](https://firebase.google.com/docs/reference/data-connect/gql/enum#OrderDirection)           | â¨ Generated from Field[`ManyToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#ManyToOneExample).`someField`of type[`Any`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Any)         |

### input OneToOneExample_Data

â¨ Generated data input type for table 'OneToOneExample'. It includes all necessary fields for creating or upserting rows into table.

|      Field       |                                                   Type                                                    |                                                                                                                                 Description                                                                                                                                 |
|------------------|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`             | [`UUID`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)                         | â¨ Generated from Field[`OneToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#OneToOneExample).`id`of type[`UUID!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)                                                 |
| `id_expr`        | [`UUID_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID_Expr)               | â¨`_expr`server value variant of`id`(â¨ Generated from Field[`OneToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#OneToOneExample).`id`of type[`UUID!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID))            |
| `mainId`         | [`UUID`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)                         | â¨ Generated from Field[`OneToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#OneToOneExample).`mainId`of type[`UUID!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)                                             |
| `mainId_expr`    | [`UUID_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID_Expr)               | â¨`_expr`server value variant of`mainId`(â¨ Generated from Field[`OneToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#OneToOneExample).`mainId`of type[`UUID!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID))    |
| `main`           | [`MainTable_Key`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#MainTable_Key) | â¨ Generated from Field[`OneToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#OneToOneExample).`main`of type[`MainTable!`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable)                                     |
| `someField`      | [`Any`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Any)                           | â¨ Generated from Field[`OneToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#OneToOneExample).`someField`of type[`Any`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Any)                                             |
| `someField_expr` | [`Any_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Any_Expr)                 | â¨`_expr`server value variant of`someField`(â¨ Generated from Field[`OneToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#OneToOneExample).`someField`of type[`Any`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Any)) |

### input OneToOneExample_Filter

â¨ Generated filter input type for table 'OneToOneExample'. This input allows filtering objects using various conditions. Use`_or`,`_and`, and`_not`to compose complex filters.

|    Field    |                                                              Type                                                              |                                                                                                               Description                                                                                                               |
|-------------|--------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `_and`      | [`[OneToOneExample_Filter!]`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#OneToOneExample_Filter) | Apply multiple filter conditions using`AND`logic.                                                                                                                                                                                       |
| `_or`       | [`[OneToOneExample_Filter!]`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#OneToOneExample_Filter) | Apply multiple filter conditions using`OR`logic.                                                                                                                                                                                        |
| `_not`      | [`OneToOneExample_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#OneToOneExample_Filter)    | Negate the result of the provided filter condition.                                                                                                                                                                                     |
| `id`        | [`UUID_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#UUID_Filter)                          | â¨ Generated from Field[`OneToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#OneToOneExample).`id`of type[`UUID!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)             |
| `mainId`    | [`UUID_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#UUID_Filter)                          | â¨ Generated from Field[`OneToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#OneToOneExample).`mainId`of type[`UUID!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)         |
| `main`      | [`MainTable_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#MainTable_Filter)                | â¨ Generated from Field[`OneToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#OneToOneExample).`main`of type[`MainTable!`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable) |
| `someField` | [`Any_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Any_Filter)                            | â¨ Generated from Field[`OneToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#OneToOneExample).`someField`of type[`Any`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Any)         |

### input OneToOneExample_FirstRow

â¨ Generated first-row input type for table 'OneToOneExample'. This input selects the first row matching the filter criteria, ordered according to the specified conditions.

|   Field   |                                                             Type                                                             |                   Description                   |
|-----------|------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| `where`   | [`OneToOneExample_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#OneToOneExample_Filter)  | Filters rows based on the specified conditions. |
| `orderBy` | [`[OneToOneExample_Order!]`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#OneToOneExample_Order) | Order the result by the specified fields.       |

### input OneToOneExample_Having

â¨ Generated having input type for table 'OneToOneExample'. This input allows you to filter groups during aggregate queries using various conditions. Use`_or`,`_and`, and`_not`to compose complex filters.

|       Field       |                                                              Type                                                              |                                                                                                              Description                                                                                                               |
|-------------------|--------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `_and`            | [`[OneToOneExample_Having!]`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#OneToOneExample_Having) | Apply multiple Having conditions using`AND`logic.                                                                                                                                                                                      |
| `_or`             | [`[OneToOneExample_Having!]`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#OneToOneExample_Having) | Apply multiple Having conditions using`OR`logic.                                                                                                                                                                                       |
| `_not`            | [`OneToOneExample_Having`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#OneToOneExample_Having)    | Negate the result of the provided Having condition.                                                                                                                                                                                    |
| `_distinct`       | [`Boolean`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean)                                        | Whether to apply DISTINCT to the aggregate function.                                                                                                                                                                                   |
| `_count`          | [`Int_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Int_Filter)                            | â¨ Generated from Field[`OneToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#OneToOneExample).`_count`of type[`Int!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int)          |
| `id_count`        | [`Int_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Int_Filter)                            | â¨ Generated from Field[`OneToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#OneToOneExample).`id_count`of type[`Int!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int)        |
| `mainId_count`    | [`Int_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Int_Filter)                            | â¨ Generated from Field[`OneToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#OneToOneExample).`mainId_count`of type[`Int!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int)    |
| `someField_count` | [`Int_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Int_Filter)                            | â¨ Generated from Field[`OneToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#OneToOneExample).`someField_count`of type[`Int!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int) |
| `someField_min`   | [`Any_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Any_Filter)                            | â¨ Generated from Field[`OneToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#OneToOneExample).`someField_min`of type[`Any`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Any)    |
| `someField_max`   | [`Any_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Any_Filter)                            | â¨ Generated from Field[`OneToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#OneToOneExample).`someField_max`of type[`Any`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Any)    |

### input OneToOneExample_Key

â¨ Generated key input type for table 'OneToOneExample'. It represents the primary key fields used to uniquely identify a row in the table.

|   Field   |                                            Type                                             |                                                                                                                           Description                                                                                                                            |
|-----------|---------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`      | [`UUID`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)           | â¨ Generated from Field[`OneToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#OneToOneExample).`id`of type[`UUID!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)                                      |
| `id_expr` | [`UUID_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID_Expr) | â¨`_expr`server value variant of`id`(â¨ Generated from Field[`OneToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#OneToOneExample).`id`of type[`UUID!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)) |

### input OneToOneExample_ListFilter

â¨ Generated list filter input type for table 'OneToOneExample'. This input applies filtering logic based on the count or existence of related objects that matches certain criteria.

|  Field  |                                                            Type                                                             |                                    Description                                     |
|---------|-----------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| `count` | [`Int_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Int_Filter)                         | The desired number of objects that match the condition (defaults to at least one). |
| `exist` | [`OneToOneExample_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#OneToOneExample_Filter) | Condition of the related objects to filter for.                                    |

### input OneToOneExample_Order

â¨ Generated order input type for table 'OneToOneExample'. This input defines the sorting order of rows in query results based on one or more fields.

|    Field    |                                                     Type                                                      |                                                                                                               Description                                                                                                               |
|-------------|---------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`        | [`OrderDirection`](https://firebase.google.com/docs/reference/data-connect/gql/enum#OrderDirection)           | â¨ Generated from Field[`OneToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#OneToOneExample).`id`of type[`UUID!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)             |
| `mainId`    | [`OrderDirection`](https://firebase.google.com/docs/reference/data-connect/gql/enum#OrderDirection)           | â¨ Generated from Field[`OneToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#OneToOneExample).`mainId`of type[`UUID!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)         |
| `main`      | [`MainTable_Order`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#MainTable_Order) | â¨ Generated from Field[`OneToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#OneToOneExample).`main`of type[`MainTable!`](https://firebase.google.com/docs/reference/data-connect/gql/object#MainTable) |
| `someField` | [`OrderDirection`](https://firebase.google.com/docs/reference/data-connect/gql/enum#OrderDirection)           | â¨ Generated from Field[`OneToOneExample`](https://firebase.google.com/docs/reference/data-connect/gql/object#OneToOneExample).`someField`of type[`Any`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Any)         |

### input StringTable_Data

â¨ Generated data input type for table 'StringTable'. It includes all necessary fields for creating or upserting rows into table.

|               Field                |                                                         Type                                                         |                                                                                                                                                   Description                                                                                                                                                   |
|------------------------------------|----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`                               | [`UUID`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)                                    | â¨ Generated from Field[`StringTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#StringTable).`id`of type[`UUID!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)                                                                                             |
| `id_expr`                          | [`UUID_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID_Expr)                          | â¨`_expr`server value variant of`id`(â¨ Generated from Field[`StringTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#StringTable).`id`of type[`UUID!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID))                                                        |
| `nonNullStringArray`               | [`[String!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String)                             | â¨ Generated from Field[`StringTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#StringTable).`nonNullStringArray`of type[`[String!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String)                                                                       |
| `nonNullStringArray_update`        | [`[String_ListUpdate!]`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#String_ListUpdate) | â¨`_update`server value variant of`nonNullStringArray`(â¨ Generated from Field[`StringTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#StringTable).`nonNullStringArray`of type[`[String!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String))                |
| `nonNullStringField`               | [`String`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String)                                | â¨ Generated from Field[`StringTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#StringTable).`nonNullStringField`of type[`String!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String)                                                                         |
| `nonNullStringField_expr`          | [`String_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String_Expr)                      | â¨`_expr`server value variant of`nonNullStringField`(â¨ Generated from Field[`StringTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#StringTable).`nonNullStringField`of type[`String!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String))                    |
| `nonNullStringNonnullArray`        | [`[String!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String)                             | â¨ Generated from Field[`StringTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#StringTable).`nonNullStringNonnullArray`of type[`[String!]!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String)                                                               |
| `nonNullStringNonnullArray_update` | [`[String_ListUpdate!]`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#String_ListUpdate) | â¨`_update`server value variant of`nonNullStringNonnullArray`(â¨ Generated from Field[`StringTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#StringTable).`nonNullStringNonnullArray`of type[`[String!]!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String)) |
| `stringArray`                      | [`[String!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String)                             | â¨ Generated from Field[`StringTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#StringTable).`stringArray`of type[`[String]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String)                                                                               |
| `stringArray_update`               | [`[String_ListUpdate!]`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#String_ListUpdate) | â¨`_update`server value variant of`stringArray`(â¨ Generated from Field[`StringTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#StringTable).`stringArray`of type[`[String]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String))                               |
| `stringField`                      | [`String`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String)                                | â¨ Generated from Field[`StringTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#StringTable).`stringField`of type[`String`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String)                                                                                 |
| `stringField_expr`                 | [`String_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String_Expr)                      | â¨`_expr`server value variant of`stringField`(â¨ Generated from Field[`StringTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#StringTable).`stringField`of type[`String`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String))                                   |
| `stringNonnullArray`               | [`[String!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String)                             | â¨ Generated from Field[`StringTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#StringTable).`stringNonnullArray`of type[`[String]!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String)                                                                       |
| `stringNonnullArray_update`        | [`[String_ListUpdate!]`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#String_ListUpdate) | â¨`_update`server value variant of`stringNonnullArray`(â¨ Generated from Field[`StringTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#StringTable).`stringNonnullArray`of type[`[String]!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String))                |

### input StringTable_Filter

â¨ Generated filter input type for table 'StringTable'. This input allows filtering objects using various conditions. Use`_or`,`_and`, and`_not`to compose complex filters.

|            Field            |                                                          Type                                                          |                                                                                                                    Description                                                                                                                    |
|-----------------------------|------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `_and`                      | [`[StringTable_Filter!]`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#StringTable_Filter) | Apply multiple filter conditions using`AND`logic.                                                                                                                                                                                                 |
| `_or`                       | [`[StringTable_Filter!]`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#StringTable_Filter) | Apply multiple filter conditions using`OR`logic.                                                                                                                                                                                                  |
| `_not`                      | [`StringTable_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#StringTable_Filter)    | Negate the result of the provided filter condition.                                                                                                                                                                                               |
| `id`                        | [`UUID_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#UUID_Filter)                  | â¨ Generated from Field[`StringTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#StringTable).`id`of type[`UUID!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)                               |
| `nonNullStringArray`        | [`String_ListFilter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#String_ListFilter)      | â¨ Generated from Field[`StringTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#StringTable).`nonNullStringArray`of type[`[String!]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String)         |
| `nonNullStringField`        | [`String_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#String_Filter)              | â¨ Generated from Field[`StringTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#StringTable).`nonNullStringField`of type[`String!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String)           |
| `nonNullStringNonnullArray` | [`String_ListFilter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#String_ListFilter)      | â¨ Generated from Field[`StringTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#StringTable).`nonNullStringNonnullArray`of type[`[String!]!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String) |
| `stringArray`               | [`String_ListFilter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#String_ListFilter)      | â¨ Generated from Field[`StringTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#StringTable).`stringArray`of type[`[String]`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String)                 |
| `stringField`               | [`String_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#String_Filter)              | â¨ Generated from Field[`StringTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#StringTable).`stringField`of type[`String`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String)                   |
| `stringNonnullArray`        | [`String_ListFilter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#String_ListFilter)      | â¨ Generated from Field[`StringTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#StringTable).`stringNonnullArray`of type[`[String]!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String)         |

### input StringTable_FirstRow

â¨ Generated first-row input type for table 'StringTable'. This input selects the first row matching the filter criteria, ordered according to the specified conditions.

|   Field   |                                                         Type                                                         |                   Description                   |
|-----------|----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| `where`   | [`StringTable_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#StringTable_Filter)  | Filters rows based on the specified conditions. |
| `orderBy` | [`[StringTable_Order!]`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#StringTable_Order) | Order the result by the specified fields.       |

### input StringTable_Having

â¨ Generated having input type for table 'StringTable'. This input allows you to filter groups during aggregate queries using various conditions. Use`_or`,`_and`, and`_not`to compose complex filters.

|           Field            |                                                          Type                                                          |                                                                                                               Description                                                                                                               |
|----------------------------|------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `_and`                     | [`[StringTable_Having!]`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#StringTable_Having) | Apply multiple Having conditions using`AND`logic.                                                                                                                                                                                       |
| `_or`                      | [`[StringTable_Having!]`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#StringTable_Having) | Apply multiple Having conditions using`OR`logic.                                                                                                                                                                                        |
| `_not`                     | [`StringTable_Having`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#StringTable_Having)    | Negate the result of the provided Having condition.                                                                                                                                                                                     |
| `_distinct`                | [`Boolean`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Boolean)                                | Whether to apply DISTINCT to the aggregate function.                                                                                                                                                                                    |
| `_count`                   | [`Int_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Int_Filter)                    | â¨ Generated from Field[`StringTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#StringTable).`_count`of type[`Int!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int)                   |
| `id_count`                 | [`Int_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Int_Filter)                    | â¨ Generated from Field[`StringTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#StringTable).`id_count`of type[`Int!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int)                 |
| `nonNullStringField_count` | [`Int_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Int_Filter)                    | â¨ Generated from Field[`StringTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#StringTable).`nonNullStringField_count`of type[`Int!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int) |
| `stringField_count`        | [`Int_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Int_Filter)                    | â¨ Generated from Field[`StringTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#StringTable).`stringField_count`of type[`Int!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#Int)        |

### input StringTable_Key

â¨ Generated key input type for table 'StringTable'. It represents the primary key fields used to uniquely identify a row in the table.

|   Field   |                                            Type                                             |                                                                                                                       Description                                                                                                                        |
|-----------|---------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`      | [`UUID`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)           | â¨ Generated from Field[`StringTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#StringTable).`id`of type[`UUID!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)                                      |
| `id_expr` | [`UUID_Expr`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID_Expr) | â¨`_expr`server value variant of`id`(â¨ Generated from Field[`StringTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#StringTable).`id`of type[`UUID!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)) |

### input StringTable_ListFilter

â¨ Generated list filter input type for table 'StringTable'. This input applies filtering logic based on the count or existence of related objects that matches certain criteria.

|  Field  |                                                        Type                                                         |                                    Description                                     |
|---------|---------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| `count` | [`Int_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#Int_Filter)                 | The desired number of objects that match the condition (defaults to at least one). |
| `exist` | [`StringTable_Filter`](https://firebase.google.com/docs/reference/data-connect/gql/input_object#StringTable_Filter) | Condition of the related objects to filter for.                                    |

### input StringTable_Order

â¨ Generated order input type for table 'StringTable'. This input defines the sorting order of rows in query results based on one or more fields.

|        Field         |                                                Type                                                 |                                                                                                               Description                                                                                                               |
|----------------------|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`                 | [`OrderDirection`](https://firebase.google.com/docs/reference/data-connect/gql/enum#OrderDirection) | â¨ Generated from Field[`StringTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#StringTable).`id`of type[`UUID!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#UUID)                     |
| `nonNullStringField` | [`OrderDirection`](https://firebase.google.com/docs/reference/data-connect/gql/enum#OrderDirection) | â¨ Generated from Field[`StringTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#StringTable).`nonNullStringField`of type[`String!`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String) |
| `stringField`        | [`OrderDirection`](https://firebase.google.com/docs/reference/data-connect/gql/enum#OrderDirection) | â¨ Generated from Field[`StringTable`](https://firebase.google.com/docs/reference/data-connect/gql/object#StringTable).`stringField`of type[`String`](https://firebase.google.com/docs/reference/data-connect/gql/scalar#String)         |