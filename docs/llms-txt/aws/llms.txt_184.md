# Source: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/llms.txt

# AWS Clean Rooms SQL Reference

> Provides detailed information about the SQL commands that can be used with AWS Clean Rooms.

- [Querying nested data](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/query-nested-data.html)
- [Document history](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/doc-history-sql-ref.html)

## [Overview](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/sql-reference.html)

- [Conventions](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/sql-ref-conventions.html): Learn about the SQL reference conventions in AWS Clean Rooms.
- [Naming rules](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/sql-ref-naming.html): Learn about the SQL naming rules for AWS Clean Rooms.
- [Data type support by SQL engine](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/sql-reference-supported-data-types-dialect.html): Learn about the supported data types across AWS Clean Rooms SQL, Snowflake SQL, and Spark SQL, including numeric, boolean, date/time, character, and structured data types with their corresponding descriptions and compatibility.


## [AWS Clean Rooms Spark SQL](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/sql-reference-spark.html)

- [Literals](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/sql-ref-literals-spark.html): Learn about literals in AWS Clean Rooms Spark SQL.

### [Data types](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/s_Supported_data_types.html)

Learn about the rules for working with database data types that are supported by AWS Clean Rooms Spark SQL.

### [Numeric types](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/Numeric_types.html)

Learn about the rules for working with numeric types that are supported by AWS Clean Rooms Spark SQL.

- [Integer types](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/Numeric_types-integer-types.html): Learn about the rules for working with integer types that are supported by AWS Clean Rooms Spark SQL.
- [DECIMAL or NUMERIC type](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/Numeric_types-decimal-or-numeric-type.html): Learn about the rules for working with DECIMAL or NUMERIC types that are supported by AWS Clean Rooms Spark SQL.
- [Floating-point types](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/Numeric_types-floating-point-types.html): Learn about the rules for working with Floating-point types that are supported by AWS Clean Rooms Spark SQL.
- [Computations with numeric values](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/Numeric_computations.html): Learn about the rules for performing computations with numeric values that are supported by AWS Clean Rooms Spark SQL.

### [Character types](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/Character_types.html)

Learn about the rules for working with character types that are supported by AWS Clean Rooms.

- [CHAR or CHARACTER](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/Character_types-char-or-character.html): Learn about the rules for working with CHAR or CHARACTER types that are supported by AWS Clean Rooms Spark SQL.
- [VARCHAR or CHARACTER VARYING](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/Character_types-varchar-or-character-varying.html): Learn about the rules for working with VARCHAR or CHARACTER VARYING types that are supported by AWS Clean Rooms Spark SQL.

### [Datetime types](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/Datetime_types.html)

Learn about the rules for working with datetime types that are supported by AWS Clean Rooms Spark SQL.

- [DATE](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/Datetime_types-date.html): Learn about the rules for working with DATE types that are supported by AWS Clean Rooms Spark SQL.
- [TIMESTAMP_LTZ](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/Datetime_types-timestamp_LTZ.html): Learn about the rules for working with TIMESTAMP_LTZ types that are supported by AWS Clean Rooms Spark SQL.
- [TIMESTAMP_NTZ](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/Datetime_types-TIMESTAMP_NTZ.html): Learn about the rules for working with TIMESTAMP_NTZ types that are supported by AWS Clean Rooms Spark SQL.
- [Examples with datetime types](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/Examples_with_datetime_types.html): Learn about examples with datetime data types in AWS Clean Rooms SQL.
- [Date, time, and timestamp literals](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/Date_and_time_literals.html): Find rules for working with date, time, and timestamp literals that are supported by AWS Clean Rooms Spark SQL.
- [Interval literals](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/Interval_literals.html): Find rules for working with interval literals that are supported by AWS Clean Rooms Spark SQL.

### [Interval data types and literals](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/interval_data_types_spark.html)

Find rules for working with interval data types and literals supported by AWS Clean Rooms.

- [Examples of interval literals without qualifier syntax](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/interval_literals_examples.html): Shows examples of using interval literals without qualifier syntax.

### [Boolean type](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/s_Boolean_type.html)

Learn about the rules for working with Boolean data types that are supported by AWS Clean Rooms.

- [Boolean literals](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/Boolean_literals-spark.html): Find rules for working with Boolean literals that are supported by AWS Clean Rooms Spark SQL.
- [Binary type](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/binary-data-type.html): Learn about the Binary data type that is supported by AWS Clean Rooms Spark SQL.

### [Nested type](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/s_Nested-data-type.html)

Learn about the rules for working with nested types that are supported by AWS Clean Rooms.

- [ARRAY type](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/array_type.html): Learn about the ARRAY data type that is supported by AWS Clean Rooms Spark SQL.
- [MAP type](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/map_type.html): Learn about the MAP data type that is supported by AWS Clean Rooms Spark SQL.
- [STRUCT type](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/struct_type.html): Learn about the STRUCT data type that is supported by AWS Clean Rooms Spark SQL.
- [Examples of nested data types](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/s_nested-data-type-examples.html): View examples of nested data types that are supported by AWS Clean Rooms Spark SQL.
- [Type compatibility and conversion](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/s_Type_conversion.html): Learn about data type compatibility and conversion in AWS Clean Rooms Spark SQL.

### [SQL commands](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/sql-commands-topic-spark.html)

Learn about the SQL commands that are supported in AWS Clean Rooms Spark SQL.

- [CACHE TABLE](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/sql-commands-cache-table.html): Learn how to use the CACHE TABLE SQL command in AWS Clean Rooms Spark SQL to cache existing tables or create new cached tables from query results.
- [Hints](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/sql-commands-hints-spark.html): Learn how to use SQL hints in AWS Clean Rooms Spark SQL to optimize query performance and reduce compute costs.

### [SELECT](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/sql-commands-select-spark.html)

Learn about the SELECT SQL command in AWS Clean Rooms Spark SQL.

- [SELECT list](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/sql-function-select-list-spark.html): Learn how to use the SELECT list function in AWS Clean Rooms Spark SQL.
- [WITH clause](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/WITH_clause.html): Defines one or more subqueries.
- [FROM clause](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/FROM_clause30.html): Lists the table references (tables, views, and subqueries) in a query to show where the data is selected from.

### [JOIN clause](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/join-clause.html)

Learn about the JOIN clause in AWS Clean Rooms.

- [Join types](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/join-types.html): Learn about the different JOIN types supported in AWS Clean Rooms.
- [WHERE clause](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/WHERE_clause.html): Contains the conditions that either join tables or apply predicates to columns in tables.
- [VALUES clause](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/VALUES.html): Learn about the VALUES clause in AWS Clean Rooms Spark SQL.

### [GROUP BY clause](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/GROUP_BY_clause.html)

Identifies the grouping columns for the query.

- [Aggregation extensions](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/GROUP_BY_aggregation-extensions.html): AWS Clean Rooms supports aggregation extensions to do the work of multiple GROUP BY operations in a single statement.
- [HAVING clause](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/HAVING_clause.html): Applies a condition to the intermediate grouped result set that a query returns.

### [Set operators](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/UNION.html)

Compare and merge the results of two separate query expressions.

- [Example UNION queries](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/example_union_query.html): Provides examples of how to use UNION queries.
- [Example UNION ALL query](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/example_unionall_query.html): Provides examples of how to use a UNION ALL query.
- [Example INTERSECT queries](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/example_intersect_query.html): Provides examples of how to use INTERSECT queries.
- [Example EXCEPT query](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/Example_EXCEPT_query.html): Provides an example of how to use the EXCEPT query.

### [ORDER BY clause](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/ORDER_BY_clause.html)

Sorts the result set of a query.

- [Examples with ORDER BY](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/Examples_with_ORDER_BY.html): Provides examples of how to use the ORDER BY clause.
- [Subquery examples](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/Subquery_examples.html): Provides examples of subqueries that fit into SELECT and WHERE.
- [Correlated subqueries](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/correlated_subqueries.html): Provides examples of how to use correlated subqueries in the WHERE clause.

### [SQL functions](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/sql-functions-topic-spark.html)

Learn about the SQL functions that are supported in AWS Clean Rooms Spark SQL.

### [Aggregate functions](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/sql-functions-agg-spark.html)

Work with the aggregate functions for SQL that AWS Clean Rooms supports to access and manipulate arrays.

- [ANY_VALUE](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/ANY_VALUE.html): Returns any value from the input expression values nondeterministically.
- [APPROX COUNT_DISTINCT](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/approx-count-distinct.html): Learn how to use the approx_count_distinct function in AWS Clean Rooms Spark SQL.
- [APPROX PERCENTILE](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/approx-percentile.html): Learn how to use the APPROX PERCENTILE function in AWS Clean Rooms Spark SQL.
- [AVG](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/avg-function.html): Learn how to use the AVG_ function in AWS Clean Rooms Spark SQL.
- [BOOL_AND](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/BOOL_AND.html): Work with the syntax and arguments used in the BOOL_AND function for AWS Clean Rooms Spark SQL.
- [BOOL_OR](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/BOOL_OR.html): Work with the syntax and arguments used in the BOOL_OR function for AWS Clean Rooms Spark SQL.
- [CARDINALITY](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/CARDINALITY.html): Learn how to use the CARDINALITY function in AWS Clean Rooms Spark SQL.
- [COLLECT_LIST](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/COLLECT_LIST.html): Learn how to use the COLLECT_LIST function in AWS Clean Rooms Spark SQL.
- [COLLECT_SET](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/COLLECT_SET.html): Learn how to use the COLLECT_SET function in AWS Clean Rooms Spark SQL.
- [COUNT and COUNT DISTINCT functions](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/count-function.html): Learn how to use the COUNT and COUNT DISTINCT function in AWS Clean Rooms Spark SQL.
- [COUNT](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/COUNT.html): Counts the rows defined by the expression.
- [MAX](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/MAX.html): Returns the maximum value in a set of rows.
- [MEDIAN](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/MEDIAN.html): Calculates the median value for the range of values.
- [MIN](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/MIN.html): Returns the minimum value in a set of rows.
- [PERCENTILE](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/percentile.html): Learn how to use the PERCENTILE function in AWS Clean Rooms Spark SQL.
- [SKEWNESS](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/SKEWNESS.html): Learn how to use the SKEWNESS function in AWS Clean Rooms Spark SQL.
- [STDDEV_SAMP and STDDEV_POP](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/STDDEV_functions.html): Returns the sample and population standard deviation of a set of numeric values (integer, decimal, or floating-point).
- [SUM and SUM DISTINCT](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/sum-function.html): The SUM function returns the sum of the input column or expression values.
- [VAR_SAMP and VAR_POP](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/VARIANCE_functions.html): Returns the sample and population variance of a set of numeric values (integer, decimal, or floating-point).

### [Array functions](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/Array_Functions.html)

Work with the array functions for SQL that AWS Clean Rooms supports to access and manipulate arrays.

- [ARRAY](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/array.html): Creates an array with the given elements.
- [ARRAY_CONTAINS](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/array_contains.html): Learn how to use the array_contains function in AWS Clean Rooms.
- [ARRAY_DISTINCT](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/array_distinct.html): Learn how to use the array_distinct function in AWS Clean Rooms.
- [ARRAY_EXCEPT](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/array_except.html): Learn how to use the ARRAY_EXCEPT function in AWS Clean Rooms.
- [ARRAY_INTERSECT](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/array_intersect.html): Learn how to use the ARRAY_INTERSECT function in AWS Clean Rooms.
- [ARRAY_JOIN](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/array_join.html): Learn how to use the array_join function in AWS Clean Rooms.
- [ARRAY_REMOVE](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/array_remove.html): Learn how to use the ARRAY_REMOVE function in AWS Clean Rooms.
- [ARRAY_UNION](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/array_union.html): Learn how to use the ARRAY_UNION function in AWS Clean Rooms.
- [EXPLODE](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/explode.html): Learn how to use the EXPLODE function in AWS Clean Rooms.
- [FLATTEN](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/flatten.html): Learn how to use the FLATTEN function in AWS Clean Rooms.

### [Conditional expressions](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/sql-functions-conditional-expressions-spark.html)

Learn about conditional expressions in AWS Clean Rooms Spark SQL.

- [CASE](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/CASE_function.html): Specifies a result when there are multiple conditions.
- [COALESCE expression](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/coalesce-function.html): A COALESCE expression returns the value of the first expression in the list that is not null.
- [GREATEST and LEAST](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/GREATEST_LEAST.html): Returns the largest or smallest value from a list of expressions.
- [IF](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/IF.html): Learn how to use the IF expression in AWS Clean Rooms.
- [IS_NULL](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/IS_NULL.html): Learn how to use the IS_NULL expression in AWS Clean Rooms.
- [IS_NOT_NULL](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/IS_NOT_NULL.html): Learn how to use the IS_NOT_NULL expression in AWS Clean Rooms.
- [NVL and COALESCE](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/NVL_function.html): Returns the value of the first expression that isn't null in a series of expressions.
- [NVL2](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/NVL2.html): Returns one of two values based on whether a specified expression evaluates to NULL or NOT NULL.
- [NULLIF](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/NULLIF_function.html): Compares two arguments and returns null if the arguments are equal.

### [Constructor functions](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/sql-functions-constructor.html)

Learn about constructor expressions in AWS Clean Rooms.

- [MAP](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/map_function.html): Learn how to use the MAP constructor function in AWS Clean Rooms.
- [NAMED_STRUCT](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/named-struct_function.html): Learn how to use the NAMED_STRUCT constructor function in AWS Clean Rooms.
- [STRUCT](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/struct_function.html): Learn how to use the MAP constructor function in AWS Clean Rooms.

### [Data type formatting functions](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/Data_type_formatting.html)

Work with the data type formatting functions for SQL that AWS Clean Rooms supports.

- [BASE64](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/base64.html): Learn how to use the BASE64 in AWS Clean Rooms.
- [CAST](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/CAST_function.html): Perform runtime conversions between compatible data types by using the CAST function.
- [DECODE](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/DECODE.html): Learn how to use the DECODE function in AWS Clean Rooms.
- [ENCODE](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/ENCODE.html): Learn how to use the ENCODE function in AWS Clean Rooms.
- [HEX](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/HEX.html): Learn how to use the HEX function in AWS Clean Rooms.
- [STR_TO_MAP](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/STR_TO_MAP.html): Learn how to use the STR_TO_MAP function in AWS Clean Rooms.
- [TO_CHAR](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/TO_CHAR.html): Converts a timestamp or numeric expression to a character-string data format.
- [TO_DATE](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/TO_DATE_function.html): Converts a date represented in a character string to a DATE data type.
- [TO_NUMBER](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/TO_NUMBER.html): Converts a string to a numeric (decimal) value.
- [UNBASE64](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/unbase64.html): Learn how to use the unbase64 function in AWS Clean Rooms.
- [UNHEX](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/UNHEX.html): Learn how to use the UNHEX function in AWS Clean Rooms.
- [Datetime format strings](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/FORMAT_strings.html): Provides a reference for datetime format strings.
- [Numeric format strings](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/Numeric_formating.html): Provides a reference for numeric format strings.

### [Date and time functions](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/date-time-functions-spark.html)

Work with the data and time functions for SQL that AWS Clean Rooms supports.

- [ADD_MONTHS](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/ADD_MONTHS.html): Adds the specified number of months to a date or timestamp value or expression.
- [CONVERT_TIMEZONE](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/s_CONVERT_TIMEZONE.html): Converts a time from one time zone to another.
- [CURRENT_DATE](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/CURRENT_DATE_function.html): CURRENT_DATE returns a date in the current session time zone (UTC by default) in the default format: YYYY-MM-DD.
- [CURRENT_TIMESTAMP](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/CURRENT_TIMESTAMP.html): Learn how to use the CURRENT_TIMESTAMP function in AWS Clean Rooms.
- [DATE_ADD](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/DATE_ADD_function.html): Returns the date that is num_days after start_date.
- [DATE_DIFF](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/DATE_DIFF_function.html): DATE_DIFF returns the difference between the date parts of two date or time expressions.
- [DATE_PART](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/DATE_PART_function.html): Extracts date part values from an expression.
- [DATE_TRUNC](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/DATE_TRUNC.html): Truncates any timestamp expression or literal based on the time interval that you specify, such as hour, day, or month.
- [DAY](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/DAY.html): Learn how to use the DAY function in AWS Clean Rooms Spark SQL.
- [DAYOFMONTH](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/DAYOFMONTH.html): Learn how to use the DAYOFMONTH function in AWS Clean Rooms Spark SQL.
- [DAYOFWEEK](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/DAYOFWEEK.html): Learn how to use the DAYOFWEEK function in AWS Clean Rooms Spark SQL.
- [DAYOFYEAR](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/DAYOFYEAR.html): Learn how to use the DAYOFYEAR function in AWS Clean Rooms Spark SQL.
- [EXTRACT](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/EXTRACT_function.html): Returns a date or time part from a TIMESTAMP, TIMESTAMPTZ, TIME, or TIMETZ value.
- [FROM_UTC_TIMESTAMP](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/FROM_UTC_TIMESTAMP.html): Learn how to use the FROM_UTC_TIMESTAMP function in AWS Clean Rooms Spark SQL.
- [HOUR](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/HOUR.html): Learn how to use the HOUR function in AWS Clean Rooms Spark SQL.
- [MINUTE](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/MINUTE.html): Learn how to use the MINUTE function in AWS Clean Rooms Spark SQL.
- [MONTH](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/MONTH.html): Learn how to use the MONTH function in AWS Clean Rooms Spark SQL.
- [SECOND](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/SECOND.html): Learn how to use the SECOND function in AWS Clean Rooms Spark SQL.
- [TIMESTAMP](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/TIMESTAMP.html): Learn how to use the TIMESTAMP function in AWS Clean Rooms Spark SQL.
- [TO_TIMESTAMP](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/TO_TIMESTAMP.html): TO_TIMESTAMP converts a TIMESTAMP string to TIMESTAMPTZ.
- [YEAR](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/YEAR.html): Learn how to use the YEAR function in AWS Clean Rooms Spark SQL.
- [Date parts for date or timestamp functions](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/Dateparts_for_datetime_functions.html): Find the date part and time part names and abbreviations that are accepted as arguments for date and time functions in AWS Clean Rooms Spark SQL.

### [Encryption and decryption functions](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/encryption-decryption-functions.html)

Work with the encryption and decryption functions for SQL that AWS Clean Rooms Spark SQL supports.

- [AES_ENCRYPT](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/AES_ENCRYPT.html): Learn how to use the AES_ENCRYPT function in AWS Clean Rooms Spark SQL.
- [AES_DECRYPT](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/AES_DECRYPT.html): Learn how to use the AES_DECRYPT function in AWS Clean Rooms Spark SQL.

### [Hash functions](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/s_hash-functions.html)

Work with the HASH functions for SQL that AWS Clean Rooms Spark SQL supports.

- [MD5](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/s_MD5.html): Uses the MD5 cryptographic hash function to convert a variable-length string into a 32-character string.
- [SHA](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/s_SHA.html): Synonym of SHA1 function
- [SHA1](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/s_SHA1.html): Uses the SHA1 cryptographic hash function to convert a variable-length string into a 40-character string.
- [SHA2](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/s_SHA2.html): The SHA2 function uses the SHA cryptographic hash function to convert a variable-length string into a character string.
- [xxhash64](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/xxhash64.html): Learn how to use the xxHASH64 function in AWS Clean Rooms.

### [Hyperloglog functions](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/hyperloglog-functions.html)

Work with the HLL functions for SQL that AWS Clean Rooms supports.

- [HLL_SKETCH_AGG](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/HLL_SKETCH_AGG.html): Work with the HLL_SKETCH_AGG function for AWS Clean Rooms.
- [HLL_SKETCH_ESTIMATE](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/HLL_SKETCH_ESTIMATE.html): Work with the HLL_SKETCH_ESTIMATE function for AWS Clean Rooms.
- [HLL_UNION](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/HLL_UNION.html): Work with the HLL_UNION function for AWS Clean Rooms.
- [HLL_UNION_AGG](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/HLL_UNION_AGG.html): Work with the HLL_UNION_AGG function for AWS Clean Rooms.

### [JSON functions](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/json-functions-spark.html)

Work with the JSON functions for SQL that AWS Clean Rooms Spark SQL supports.

- [GET_JSON_OBJECT](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/GET_JSON_OBJECT.html): Learn how to use the GET_JSON_OBJECT function in AWS Clean Rooms.
- [TO_JSON](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/TO_JSON.html): Learn how to use the TO_JSON function in AWS Clean Rooms.

### [Math functions](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/Math_functions-spark.html)

Work with the mathematical operators and functions for SQL that AWS Clean Rooms supports.

- [Mathematical operator symbols](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/OPERATOR_SYMBOLS.html): Lists the mathematical operators supported by AWS Clean Rooms Spark SQL.
- [ABS](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/ABS.html): Calculates the absolute value of a number, where that number can be a literal or an expression that evaluates to a number.
- [ACOS](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/ACOS.html): Returns the arc cosine of a number.
- [ASIN](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/ASIN.html): Returns the arc sine of a number.
- [ATAN](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/ATAN.html): Returns the arc tangent of a number.
- [ATAN2](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/ATAN2.html): Returns the arc tangent of one number divided by another number.
- [CBRT](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/CBRT.html): Calculates the cube root of a number.
- [CEILING (or CEIL)](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/CEILING_FLOOR.html): Rounds a number up to the next whole number.
- [COS](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/COS.html): Returns the cosine of a number.
- [COT](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/COT.html): Returns the cotangent of a number.
- [DEGREES](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/DEGREES.html): Converts an angle in radians to its equivalent in degrees.
- [DIV](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/DIV.html): Returns the integral part of the division of dividend by divisor.
- [EXP](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/EXP.html): Returns the exponential value in double precision for a numeric expression.
- [FLOOR](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/FLOOR.html): Rounds a number down to the next whole number.
- [LN](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/LN.html): Returns the natural logarithm of the input parameter.
- [LOG](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/LOG.html): Returns the logarithm of expr with base.
- [MOD](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/MOD.html): Returns the remainder after a number is divided by another.
- [PI](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/PI.html): Returns the value of pi to 14 decimal places.
- [POWER](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/POWER.html): Raises a numeric expression to the power of a second numeric expression.
- [RADIANS](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/RADIANS.html): Converts an angle in degrees to its equivalent in radians.
- [RAND](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/RAND.html): Learn how to use the RAND function in AWS Clean Rooms.
- [RANDOM](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/RANDOM.html): Generates a random value greater than or equal to 0.0 and less than 1.0.
- [ROUND](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/ROUND.html): Rounds numbers to the nearest integer or decimal.
- [SIGN](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/SIGN.html): Returns the sign (positive or negative) of a number.
- [SIN](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/SIN.html): Returns the sine of a number.
- [SQRT](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/SQRT.html): Returns the square root of a numeric value.
- [TRUNC](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/TRUNC.html): Truncates a number and right-fills it with zeros from the position specified.

### [Scalar functions](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/scalar_functions.html)

Work with the scalar functions for SQL that AWS Clean Rooms supports to analyze arrays, maps, and strings.

- [SIZE](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/size.html): Learn how to use the size function for arrays in AWS Clean Rooms.

### [String functions](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/String_functions_spark.html)

Work with the string functions that process and manipulate character strings or expressions that evaluate to character strings.

- [|| (Concatenation) Operator](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/concat_op.html): Concatenates two expressions on either side of the || symbol and returns the concatenated expression.
- [BTRIM](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/BTRIM.html): Trims a string by removing leading and trailing blanks or by removing leading and trailing characters that match an optional specified string.
- [CONCAT](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/CONCAT.html): Concatenates two expressions and returns the resulting expression.
- [FORMAT_STRING](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/FORMAT_STRING.html): Learn how to use the FORMAT_STRING function in AWS Clean Rooms.
- [LEFT and RIGHT](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/LEFT.html): Returns the specified number of leftmost or rightmost characters from a character string.
- [LENGTH](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/LENGTH.html): Learn about the LENGTH function.
- [LOWER](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/LOWER.html): Converts a string to lowercase.
- [LPAD and RPAD](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/LPAD.html): Prepend or append characters to a string, based on a specified length.
- [LTRIM](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/LTRIM.html): The LTRIM function trims a specified set of characters from the beginning of a string.
- [POSITION](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/POSITION.html): Returns the location of the specified substring within a string.
- [REGEXP_COUNT](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/REGEXP_COUNT.html): Searches a string for a regular expression pattern and returns an integer that indicates the number of times the pattern occurs in the string.
- [REGEXP_INSTR](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/REGEXP_INSTR.html): Returns the characters extracted from a string by searching for a regular expression pattern.
- [REGEXP_REPLACE](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/REGEXP_REPLACE.html): Searches a string for a regular expression pattern and replaces every occurrence of the pattern with the specified string.
- [REGEXP_SUBSTR](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/REGEXP_SUBSTR.html): Returns the characters extracted from a string by searching for a regular expression pattern.
- [REPEAT](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/REPEAT.html): Repeats a string the specified number of times.
- [REPLACE](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/REPLACE.html): Replaces all occurrences of a set of characters within an existing string with other specified characters.
- [REVERSE](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/REVERSE.html): Operates on a string and returns the characters in reverse order.
- [RTRIM](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/RTRIM.html): Trims a specified set of characters from the end of a string.
- [SPLIT](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/split.html): Learn how to use the SPLIT function in AWS Clean Rooms.
- [SPLIT_PART](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/SPLIT_PART.html): Splits a string on the specified delimiter and returns the part at the specified position.
- [SUBSTRING](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/SUBSTRING.html): Returns the subset of a string based on the specified start position.
- [TRANSLATE](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/TRANSLATE.html): For a given expression, replaces all occurrences of specified characters with specified substitutes.
- [TRIM](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/TRIM.html): Trims a string by removing leading and trailing blanks or by removing leading and trailing characters that match an optional specified string.
- [UPPER](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/UPPER.html): Converts a string to uppercase.
- [UUID](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/UUID.html): Learn how to use the UUID function in AWS Clean Rooms.

### [Privacy-related functions](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/privacy-related-functions.html)

Learn about privacy-related functions in AWS Clean Rooms.

- [consent_gpp_v1_decode](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/consent_gpp_v1_decode.html): Learn how to use the consent_tcf_v2_decode function in AWS Clean Rooms.
- [consent_tcf_v2_decode](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/consent_tcf_v2_decode.html): Learn how to use the consent_tcf_v2_decode function in AWS Clean Rooms.

### [Window functions](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/Window_functions.html)

Create analytic business queries more efficiently using the window functions for SQL that AWS Clean Rooms Spark SQL supports.

- [CUME_DIST](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/WF_CUME_DIST.html): An inverse distribution function that assumes a continuous distribution model.
- [DENSE_RANK](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/WF_DENSE_RANK.html): Determines the rank of a value in a group of values, based on the ORDER BY expression in the OVER clause.
- [FIRST](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/WF_FIRST.html): Returns the value of the specified expression with respect to the first row in the window frame given an ordered set of rows.
- [FIRST_VALUE](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/WF_first_value.html): Returns the value of the specified expression with respect to the first row in the window frame given an ordered set of rows.
- [LAG](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/WF_LAG.html): Returns the values for a row at a given offset above (before) the current row in the partition.
- [LAST](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/WF-LAST.html): Returns the value of the specified expression with respect to the first row in the window frame given an ordered set of rows.
- [LAST_VALUE](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/WF_last_value.html): Returns the value of the specified expression with respect to the first row in the window frame given an ordered set of rows.
- [LEAD](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/WF_LEAD.html): Returns the values for a row at a given offset below (after) the current row in the partition.
- [PERCENT_RANK](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/WF_PERCENT_RANK.html): Calculates the percent rank of a given row.
- [RANK](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/WF_RANK.html): Determines the rank of a value in a group of values, based on the ORDER BY expression in the OVER clause.
- [ROW_NUMBER](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/WF_ROW_NUMBER.html): Determines the row number of the current row within a group of rows, based on the ORDER BY expression in the OVER clause.

### [SQL conditions](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/sql-conditions-topic-spark.html)

Learn about the SQL conditions that are supported in AWS Clean Rooms.

- [Comparison operators](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/comparison-operators.html): Learn about how to use comparison operators in AWS Clean Rooms SQL.
- [Logical conditions](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/logical-conditions-spark.html): Logical conditions combine the result of two conditions to produce a single result.

### [Pattern-matching conditions](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/sql-contitions-pattern-matching-spark.html)

A pattern-matching operator searches a string for a pattern specified in the conditional expression and returns true or false depending on whether it finds a match.

- [LIKE](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/patternmatching_condition_like.html): Describes the pattern-matching condition LIKE operator supported by AWS Clean Rooms.
- [RLIKE](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/RLIKE.html): Describes the pattern-matching condition RLIKE operator supported by AWS Clean Rooms.
- [BETWEEN range condition](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/range_condition-spark.html): Tests expressions for inclusion in a range of values, using the keywords BETWEEN and AND.
- [Null condition](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/null_condition-spark.html): Tests for nulls, when a value is missing or unknown.
- [EXISTS condition](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/exists_condition.html): Tests for the existence of rows in a subquery, and return true if a subquery returns at least one row.
- [IN condition](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/in_condition-spark.html): Tests a value for membership in a set of values or in a subquery.
