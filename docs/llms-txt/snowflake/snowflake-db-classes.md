# Source: https://docs.snowflake.com/en/sql-reference/snowflake-db-classes.md

# Snowflake classes

The SNOWFLAKE database also includes Classes provided by Snowflake.

## Concepts

A *Class* is similar to a class in object oriented programming and serves as a blueprint for creating instances. An *Instance* is an
object created from a Class. Classes and instances are schema-level objects in Snowflake. You can think of a class as an extensible
Snowflake object type and an instance as a Snowflake object.

A class provides a public API through stored procedures and functions. Collectively they are referred to as *class methods*. A
class also provides *class roles* that enable fine-grained privileges on class methods. In addition to its public API, a class
includes private state and private procedures and functions, similar to private properties and methods in object oriented programming.
The implementation of a class can evolve over time through new *class versions*. Instances are upgraded to the latest class version
automatically by Snowflake.

For example, Snowflake provides the [ANOMALY_DETECTION class](classes/anomaly_detection.md) in the SNOWFLAKE.ML
schema. You can create an instance of a class using a CREATE command just as you would create an object of a specific object type.

The example below creates an instance of a class and calls an instance method.

1. Update your search path to include `SNOWFLAKE.ML`:

   ```sqlexample
   ALTER SESSION SET SEARCH_PATH = '$current, $public, snowflake.ml';
   ```

2. Create an instance of ANOMALY_DETECTION class:

   ```sqlexample
   CREATE ANOMALY_DETECTION mydatabase.myschema.my_anomaly_detector(...);
   ```

3. After you create an instance of the ANOMALY_DETECTION class, you can call instance methods:

   ```sqlexample
   mydatabase.myschema.my_anomaly_detector!DETECT_ANOMALIES(...);
   ```

> **Note:**
>
> Currently, classes are only provided by Snowflake and cannot be created by users.

## List available classes

You can find available classes and learn more about each class using SHOW commands. These commands allow you to:

* Find all available classes in the SNOWFLAKE database.
* List class methods.
* List class roles.

### Find all classes

List all the available Snowflake classes by executing the [SHOW CLASSES](sql/show-classes.md) command:

```sqlexample
SHOW CLASSES IN DATABASE SNOWFLAKE;
```

The results of this statement include the database and schema name for each class.

### Update your search path

Classes are objects in a schema in the SNOWFLAKE database. You must use the fully qualified class name (for example,
SNOWFLAKE.ML.ANOMALY_DETECTION) to execute the SQL commands that follow in this topic. Alternatively, you can update the
[search path](name-resolution.md) to include the database and schema for a class, then refer to
the class by its unqualified name (for example, ANOMALY_DETECTION).

> **Note:**
>
> If you update the search path for a particular class, functions that have the same name but that are part of
> a different class will no longer be accessible. For example, if you add `SNOWFLAKE.CORTEX` to your search path,
> the string function [TRANSLATE](functions/translate.md) won’t be accessible since the
> [SNOWFLAKE.CORTEX.TRANSLATE](functions/translate-snowflake-cortex.md) function exists.

You can modify the search path using ALTER SESSION, ALTER USER, or ALTER ACCOUNT.

| Command | Notes |
| --- | --- |
| [ALTER SESSION](sql/alter-session.md) | Modifies the search path for the current session only. You can modify your own search path at the session level. A session-level change overrides the account-level or user-level setting. |
| [ALTER USER](sql/alter-user.md) | Modifies the search path persistently for the current or specified user. You can modify your own search path at the user level. An administrator can modify another user’s search path. A user-level change overrides the account-level or session-level setting. |
| [ALTER ACCOUNT](sql/alter-account.md) | Modifies the search path persistently for all users in the account. An administrator must modify the search path at the account level. |

1. Execute the following statement and copy your current search path from the `value` column:

   ```sqlexample
   SHOW PARAMETERS LIKE 'search_path';
   ```

2. Update your search path.

   > **Note:**
   >
   > The examples below use the default search path, `$current, $public`. If your search path in the `value`
   > column from the previous step does not match the default value, edit the example statements below to include your actual
   > search path.

   For example, to add SNOWFLAKE.ML to your search path for your current session, execute the following statement:

   ```sqlexample
   ALTER SESSION SET SEARCH_PATH = '$current, $public, SNOWFLAKE.ML';
   ```

   To add SNOWFLAKE.ML to your own search path at the user level, execute the following statement:

   ```sqlexample
   ALTER USER SET SEARCH_PATH = '$current, $public, SNOWFLAKE.ML';
   ```

   A user with the ACCOUNTADMIN role can update the search path for the account by executing the following statement:

   ```sqlexample
   ALTER ACCOUNT SET SEARCH_PATH = '$current, $public, SNOWFLAKE.ML';
   ```

For more information on how Snowflake resolves names, see [Object name resolution](name-resolution.md).

### Class methods

A class provides a public API through stored procedures and functions. Collectively they are referred to as class *methods*. To list
all the methods for a class, including the arguments required for each method, execute the
[SHOW FUNCTIONS IN CLASS](sql/show-functions.md) and
[SHOW PROCEDURES IN CLASS](sql/show-procedures.md) commands. A class might include multiple methods with the same name
but different signatures (that is to say, a different number of arguments or argument data types).

> **Note:**
>
> The example statements in this topic use the non-qualified class name ANOMALY_DETECTION. If you have not
> updated your search path to include SNOWFLAKE.ML, use the fully qualified
> name for the SNOWFLAKE.ML.ANOMALY_DETECTION class.

For example, to list all the functions available in the SNOWFLAKE.ML.ANOMALY_DETECTION class, execute the following statement:

```sqlexample
SHOW FUNCTIONS IN CLASS ANOMALY_DETECTION;
```

```output
+-----------------------+-------------------+-------------------+--------------------------------------------------------------------------+--------------+----------+
| name                  | min_num_arguments | max_num_arguments | arguments                                                                | descriptions | language |
|-----------------------+-------------------+-------------------+--------------------------------------------------------------------------+--------------+----------|
| _DETECT_ANOMALIES_1_1 |                 5 |                 5 | (MODEL BINARY, TS TIMESTAMP_NTZ, Y FLOAT, FEATURES ARRAY, CONFIG OBJECT) | NULL         | Python   |
| _FIT                  |                 3 |                 3 | (TS TIMESTAMP_NTZ, Y FLOAT, FEATURES ARRAY)                              | NULL         | Python   |
| _FIT                  |                 4 |                 4 | (TS TIMESTAMP_NTZ, Y FLOAT, LABEL BOOLEAN, FEATURES ARRAY)               | NULL         | Python   |
+-----------------------+-------------------+-------------------+--------------------------------------------------------------------------+--------------+----------+
```

To list all the stored procedures in the SNOWFLAKE.ML.ANOMALY_DETECTION class, execute the following statement:

```sqlexample
SHOW PROCEDURES IN CLASS ANOMALY_DETECTION;
```

The results below include the stored procedures in the class for which the current role in the session has been granted
access privileges:

```output
+---------------------------------+-------------------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------+--------------+------------+
| name                            | min_num_arguments | max_num_arguments | arguments                                                                                                                                | descriptions | language   |
|---------------------------------+-------------------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------+--------------+------------|
| __CONSTRUCT                     |                 4 |                 4 | (INPUT_DATA VARCHAR, TIMESTAMP_COLNAME VARCHAR, TARGET_COLNAME VARCHAR, LABEL_COLNAME VARCHAR)                                           | NULL         | Javascript |
| __CONSTRUCT                     |                 5 |                 5 | (INPUT_DATA VARCHAR, SERIES_COLNAME VARCHAR, TIMESTAMP_COLNAME VARCHAR, TARGET_COLNAME VARCHAR, LABEL_COLNAME VARCHAR)                   | NULL         | Javascript |
| DETECT_ANOMALIES                |                 4 |                 4 | (INPUT_DATA VARCHAR, SERIES_COLNAME VARCHAR, TIMESTAMP_COLNAME VARCHAR, TARGET_COLNAME VARCHAR)                                          | NULL         | SQL        |
| DETECT_ANOMALIES                |                 5 |                 5 | (INPUT_DATA VARCHAR, SERIES_COLNAME VARCHAR, TIMESTAMP_COLNAME VARCHAR, TARGET_COLNAME VARCHAR, CONFIG_OBJECT OBJECT)                    | NULL         | SQL        |
| DETECT_ANOMALIES                |                 3 |                 3 | (INPUT_DATA VARCHAR, TIMESTAMP_COLNAME VARCHAR, TARGET_COLNAME VARCHAR)                                                                  | NULL         | SQL        |
| DETECT_ANOMALIES                |                 4 |                 4 | (INPUT_DATA VARCHAR, TIMESTAMP_COLNAME VARCHAR, TARGET_COLNAME VARCHAR, CONFIG_OBJECT OBJECT)                                            | NULL         | SQL        |
| EXPLAIN_FEATURE_IMPORTANCE      |                 0 |                 0 | ()                                                                                                                                       | NULL         | SQL        |
| _CONSTRUCTFEATUREINPUT          |                 6 |                 6 | (INPUT_REF VARCHAR, SERIES_COLNAME VARCHAR, TIMESTAMP_COLNAME VARCHAR, TARGET_COLNAME VARCHAR, LABEL_COLNAME VARCHAR, REF_ALIAS VARCHAR) | NULL         | Javascript |
| _CONSTRUCTINFERENCEFUNCTIONNAME |                 0 |                 0 | ()                                                                                                                                       | NULL         | SQL        |
| _CONSTRUCTINFERENCERESULTAPI    |                 0 |                 0 | ()                                                                                                                                       | NULL         | SQL        |
| _SETTRAININGINFO                |                 0 |                 0 | ()                                                                                                                                       | NULL         | SQL        |
+---------------------------------+-------------------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------+--------------+------------+
```

### Class roles

A class might have one or more roles that are granted the USAGE privilege on some or all class methods. You can list the available roles in
a class using the [SHOW ROLES IN CLASS](sql/show-roles.md) command.

List all the roles in the SNOWFLAKE.ML.ANOMALY_DETECTION class:

```sqlexample
SHOW ROLES IN CLASS ANOMALY_DETECTION;
```

```output
+-------------------------------+------+---------+
| created_on                    | name | comment |
|-------------------------------+------+---------|
| 2023-06-06 01:06:42.808 +0000 | USER | NULL    |
+-------------------------------+------+---------+
```

#### Instance roles

Roles are defined in the class and instantiated in the instance as an *instance role*. An instance role can be granted to a role in your
account to enable access to instance methods.

For example, if you have an ANOMALY_DETECTION instance `my_anomaly_detector` in schema `my_db.my_schema`, you can view
the privileges granted to the instance role USER using the following statement:

```sqlexample
SHOW GRANTS TO SNOWFLAKE.ML.ANOMALY_DETECTION ROLE my_db.my_schema.my_anomaly_detector!USER;
```

To grant the instance role to role `my_role` in your account, execute the following statement:

```sqlexample
GRANT SNOWFLAKE.ML.ANOMALY_DETECTION ROLE my_db.my_schema.my_anomaly_detector!USER
  TO ROLE my_role;
```

The above statement enables the role `my_role` to execute methods of the ANOMALY_DETECTOR instance `my_anomaly_detector`.

> **Note:**
>
> The role `my_role` must also have the USAGE privilege on database `my_db` and schema `my_schema`.
> Role `my_role` must also have the appropriate privileges on objects passed to instance methods.

## Grant the privilege to create class instances

In order to create an instance of a class, a role must be granted the CREATE *<class_name>* privilege.

For example, to enable the `ml_admin` role to create SNOWFLAKE.ML.ANOMALY_DETECTION instances in the `mydb.myschema`
schema, execute the following statement:

```sqlexample
GRANT CREATE ANOMALY_DETECTION ON SCHEMA mydb.myschema TO ROLE ml_admin;
```

## Create an instance

You can create an instance of a class using the CREATE *<object>* command and the class constructor method.

> **Note:**
>
> Instance names in a schema must be unique irrespective of the class they were created from. For example, if you have
> an instance of the [BUDGET (SNOWFLAKE.CORE)](classes/budget.md) class named `foo`, you can’t create an instance of the
> [ANOMALY_DETECTION (SNOWFLAKE.ML)](classes/anomaly_detection.md) class named `foo` in the same schema.

For example, to create an anomaly detector `my_anomaly_detector` instance, execute the following statement:

```sqlexample
CREATE ANOMALY_DETECTION my_anomaly_detector(
  INPUT_DATA => SYSTEM$REFERENCE('VIEW', 'my_view'),
  TIMESTAMP_COLUMN => 'my_timestamp_column'
  TARGET_COLNAME => 'my_target_column',
  LABEL_COLNAME => ''
);
```

## Use an instance

After you create an instance of a class, you can call the instance methods that the class
provides. Calling a method requires the exclamation point (`!`) character. The `!` character is used to dereference
the instance.

For example, to call the DETECT_ANOMALIES method of the anomaly detector `my_anomaly_detector`, execute the following
statement:

```sqlexample
CALL my_anomaly_detector!DETECT_ANOMALIES(
  INPUT_DATA => SYSTEM$REFERENCE('VIEW', 'my_view'),
  TIMESTAMP_COLNAME =>'my_timestamp_column',
  TARGET_COLNAME => 'my_target_column'
);
```

## Selecting columns from SQL class instance methods that return tabular data

Some methods return tabular data (for example, methods in the [ANOMALY_DETECTION](classes/anomaly_detection.md)
and [FORECAST](classes/forecast.md) classes). To select and manipulate this tabular data, you can call these
methods in the [FROM](constructs/from.md) clause of a SELECT statement.

When calling the method, omit the [CALL](sql/call.md) command. Instead, put the call in parentheses, preceded by the
TABLE keyword:

```sqlsyntax
SELECT ... FROM TABLE( <method_name>( <arg> [ , ... <arg> ] ) );
```

For example, to select the `ts`, `forecast`, and `is_anomaly` columns from the tabular data returned by the
[DETECT_ANOMALIES](classes/anomaly-detection/methods/detect_anomalies.md) method of the anomaly detector
`my_anomaly_detector`:

```sqlexample
SELECT ts, forecast, is_anomaly FROM TABLE(
  my_anomaly_detector!DETECT_ANOMALIES(
    INPUT_DATA => TABLE('my_view'),
    TIMESTAMP_COLNAME =>'my_timestamp_column',
    TARGET_COLNAME => 'my_target_column'
  )
);
```

If you pass in a reference to a query, the query cannot refer to any [common table expressions](../user-guide/queries-cte.md)
defined outside of the reference. For example, executing the following statement results in an error because the query reference
refers to `my_data`, which is defined in the outer [WITH](constructs/with.md) clause:

```sqlexample
WITH my_data AS (
  SELECT * FROM my_view
)
SELECT ts, forecast FROM TABLE(
  my_anomaly_detector!DETECT_ANOMALIES(
    INPUT_DATA => TABLE('SELECT * FROM my_data'),
    TIMESTAMP_COLNAME =>'my_timestamp_column',
    TARGET_COLNAME => 'my_target_column'
  )
);
```

To work around this limitation, move the WITH clause inside the query reference:

```sqlexample
SELECT ts, forecast FROM TABLE(
  my_anomaly_detector!DETECT_ANOMALIES(
    INPUT_DATA => TABLE('
      WITH my_data AS (
        SELECT * FROM my_view
      )
      SELECT * FROM my_data
    '),
    TIMESTAMP_COLNAME =>'my_timestamp_column',
    TARGET_COLNAME => 'my_target_column'
  )
);
```

## Available classes

For a list of available Snowflake classes, see [SQL class reference](../sql-reference-classes.md).

## Limitations

[Replication](../user-guide/account-replication-intro.md) is supported only for instances
of the [CUSTOM_CLASSIFIER](classes/custom_classifier.md) class.
