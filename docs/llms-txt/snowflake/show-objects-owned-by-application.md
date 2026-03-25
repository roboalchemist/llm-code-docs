# Source: https://docs.snowflake.com/en/sql-reference/sql/show-objects-owned-by-application.md

# SHOW OBJECTS OWNED BY APPLICATION

Lists the objects owned by an app that exists outside the app.

See also:
:   [SHOW APPLICATIONS](show-applications.md)

## Syntax

```sqlsyntax
SHOW OBJECTS OWNED BY APPLICATION <app_name>
```

## Parameters

`app_name`
:   The name of the app whose objects you want to list.

## Access control requirements

| Privilege | Object | Notes |
| --- | --- | --- |
| OWNERSHIP or MANAGE GRANTS | App | One of these privileges is required to view the objects owned by the app. |

## Output

| Column | Description |
| --- | --- |
| `created_on` | The timestamp when the object was created. |
| `name` | The name of the object owned by the app |
| `type` | The type of object, for example COMPUTE_POOL. |

## Examples

```sqlexample
SHOW OBJECTS OWNED BY APPLICATION hello_snowflake_app;
```

```output
+---------------------------------+----------------------+---------------------+
| created_on                      | name                 | object_type         |
|---------------------------------|----------------------|---------------------|
| 2024-11-20 17:56:08.887 -0800   | HELLO_SNOWFLAKE_APP  | COMPUTE_POOL        |
+---------------------------------+----------------------+---------------------+
```
