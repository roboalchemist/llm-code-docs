# Source: https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/llms.txt

# Amazon Kinesis Data Analytics SQL Reference SQL Reference

> SQL Reference Documentation for Amazon Kinesis Data Analytics

- [SQL Reference](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/analytics-sql-reference.html)
- [Kinesis Data Analytics Developer Guide](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/analytics-sql-reference-dg.html)
- [Document History](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/doc-history.html)

## [Streaming SQL Language Elements](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-basic-building-blocks.html)

- [Identifiers](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-identifiers.html): Rules for valid identifiers in Kinesis Data Analytics

### [Data Types](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-data-types.html)

SQL data types supported by Kinesis Data Analytics

- [Numeric Types and Precision](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-numeric-types-precision.html): Supported numeric data types and precision for Kinesis Data Analytics

### [Streaming SQL Operators](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-streaming-operators.html)

Supported operator types for Kinesis Data Analytics

- [String Operators](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-string-operators.html): String operators in Kinesis Data Analytics
- [Logical Operators](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-logical-operators.html): Logical Operators in Kinesis Data Analytics
- [Expressions and Literals](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-expressions.html)
- [Monotonic Expressions and Operators](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-monotonic-expressions-operators.html): Since Amazon Kinesis Data Analytics queries operate on infinite streams of rows, some operations are only possible if something is known about those streams.
- [Condition Clause](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-conditions.html): Referenced by:
- [Temporal Predicates](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-temporal-predicate.html): This topic describes extensions to the Amazon Kinesis Data Analytics SQL dialect that let users express temporal relationships simply and elegantly.
- [Reserved Words and Keywords](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-reserved-words-keywords.html)


## [Standard SQL Operators](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-standard-sql-operators.html)

### [CREATE statements](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-create-statements.html)

You can use the following CREATE statements with Amazon Kinesis Data Analytics:

- [CREATE STREAM](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-create-stream.html): The CREATE STREAM statement creates a (local) stream.
- [CREATE FUNCTION](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-create-function.html): Amazon Kinesis Data Analytics provides a number of , and also allows users to extend its capabilities by means of user-defined functions (UDFs).
- [CREATE PUMP](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-create-pump.html): A pump is an Amazon Kinesis Data Analytics Repository Object (an extension of the SQL standard) that provides a continuously running INSERT INTO stream SELECT ...
- [INSERT](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-insert.html): INSERT is used to insert rows into a stream.
- [Query](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-query.html)

### [SELECT statement](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-select.html)

SELECT retrieves rows from streams.

- [SELECT ALL and SELECT DISTINCT](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-select-all-distinct.html): If the ALL keyword is specified, the query does not eliminate duplicate rows.
- [SELECT clause](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-select-clause.html): The <select-clause> uses the following items after the STREAM keyword:
- [FROM clause](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-from-clause.html): The FROM clause is the source of rows for a query.
- [JOIN clause](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-join-clause.html): The JOIN clause in a SELECT statement combines columns from one or more streams or reference tables.
- [HAVING clause](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-having-clause.html): The HAVING clause in a SELECT specifies a condition to apply within a group or aggregate.
- [GROUP BY clause](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-group-by-clause.html)
- [WHERE clause](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-where-clause.html): The WHERE clause extracts records that meet a specified condition.

### [WINDOW Clause (Sliding Windows)](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-window-clause.html)

The WINDOW clause for a sliding windowed query specifies the rows over which analytic functions are computed across a group of rows in relation to the current row.

- [Allowed and Disallowed Window Specifications](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-allowed-disallowed-window.html): Amazon Kinesis Data Analytics supports nearly all windows that end with the current row.
- [Window examples](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-window-examples.html): The following examples show a sample input data set, the definitions for several windows, and the contents of those windows at various times after 10:00, the time data starts to arrive for this example.

### [ORDER BY clause](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-order-by-clause.html)

A streaming query can use ORDER BY if its leading expression is time-based and monotonic.

- [T-sorting Stream Input](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sqlrf_T-sorting_Stream_Input.html): Amazon Kinesis Data Analytics real-time analytics use the fact that arriving data is ordered by ROWTIME.
- [ROWTIME](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-rowtime.html): ROWTIME is an operator and system column that returns the time at which a particular row of a stream was created.


## [Functions](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-functions.html)

### [Aggregate Functions](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-aggregate-functions.html)

Instead of returning a result calculated from a single row, an aggregate function returns a result calculated from aggregated data contained in a finite set of rows, or from information about a finite set of rows.

- [Windowed Aggregation on Streams](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-windowed-aggregation-stream.html): To illustrate how windowed aggregation works on Amazon Kinesis data streams, assume that the data in the following table is flowing through a stream called WEATHERSTREAM.
- [AVG](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-avg.html): Returns the average of a group of values from a windowed query.
- [COUNT](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-count.html): Returns the number of qualifying rows of a group of values from a windowed query.
- [COUNT_DISTINCT_ITEMS_TUMBLING Function](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/count-distinct-items.html): Returns a count of the number of distinct items in the specified in-application stream column over a tumbling window.
- [EXP_AVG](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-exp-avg.html)
- [FIRST_VALUE](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-first-value.html)
- [LAST_VALUE](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-last-value.html)
- [MAX](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-max.html): Returns the maximum value among the values of the qualifying rows from a windowed query.
- [MIN](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-min.html): Returns the minimum value among the values of the qualifying rows from a windowed query.
- [SUM](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-sum.html): Returns the sum of a group of values from a windowed query
- [TOP_K_ITEMS_TUMBLING Function](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/top-k.html): Returns the most frequently occurring values in the specified in-application stream column over a tumbling window.
- [Analytic Functions](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-analytic-functions.html): Analytic functions for Kinesis Data Analytics

### [Boolean Functions](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-boolean-functions.html)

Boolean functions for Kinesis Data Analytics streaming SQL.

- [ANY](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-any.html): ANY function
- [EVERY](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-every.html)

### [Conversion Functions](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-conversion-functions.html)

Conversion functions for Kinesis Data Analytics streaming SQL.

- [CAST](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-cast.html): CAST lets you convert one value expression or data type to another value expression or data type.

### [Date and Time Functions](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-date-time-functions.html)

Built-in functions relating to dates and time

### [Datetime Conversion Functions](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-datetime-conversion-functions.html)

Datetime Conversion Functions for Kinesis Data Analytics

### [Char To Timestamp(Sys)](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-char-to-timestamp.html)

Char To Timestamp(Sys) function

- [Template Strings to Create Specific Output Timestamps](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-template-strings-create-output-timestamps.html)
- [CHAR_TO_DATE](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-char-to-date.html): Converts a string to a date, according to the specified format string.
- [CHAR_TO_TIME](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-char-to-time.html): Converts a string to a date
- [DATE_TO_CHAR](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-date-to-char.html): The DATE_TO_CHAR converts a date to a string.
- [TIME_TO_CHAR](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-time-to-char.html): Uses a format string to format a time.
- [TIMESTAMP_TO_CHAR](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-timestamp-to-char.html): TIMESTAMP_TO_CHAR function
- [TO_TIMESTAMP](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-to-timestamp.html): TO_TIMESTAMP function
- [UNIX_TIMESTAMP](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-unix-timestamp.html): Converts a SQL timestamp to a Unix timestamp that is expressed in milliseconds since '1970-01-01 00:00:00' UTC and that is a BIGINT.
- [Date, Timestamp, and Interval Operators](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-date-timestamp-interval.html): Date, Timestamp, and Interval Operators for Kinesis Data Analytics
- [Date and Time Patterns](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-parse-timestamp-format.html): Date and time formats are specified by date and time pattern strings.
- [CURRENT_DATE](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-current-date.html): Returns the current Amazon Kinesis Data Analytics system date when the query executes as YYYY-MM-DD when the query executes.
- [CURRENT_ROW_TIMESTAMP](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-current-row-timestamp.html): CURRENT_ROW_TIMESTAMP is an Amazon Kinesis Data Analytics extension to the SQL:2008 specification.
- [CURRENT_TIME](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-current-time.html): Returns the current Amazon Kinesis Data Analytics system time when the query executes.
- [CURRENT_TIMESTAMP](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-current-timestamp.html): Returns the current database system timestamp (as defined on the environment on which Amazon Kinesis Data Analytics is running) as a datetime value.
- [EXTRACT](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-extract.html)
- [LOCALTIME](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-localtime.html): Returns the current time when the query executes as defined by the environment on which Amazon Kinesis Data Analytics is running.
- [LOCALTIMESTAMP](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-local-timestamp.html): Returns the current timestamp as defined by the environment on Amazon Kinesis Data Analytics application is running.
- [TSDIFF](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-tsdiff.html): TSDIFF function

### [Null Functions](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-null-functions.html)

Null functions for Kinesis Data Analytics streaming SQL.

- [COALESCE](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-coalesce.html)
- [NULLIF](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-nullif.html)

### [Numeric Functions](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-numeric-functions.html)

Numeric functions for Kinesis Data Analytics streaming SQL.

- [ABS](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-abs.html): ABS returns the absolute value of the input argument.
- [CEIL / CEILING](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-ceil.html): CEIL returns the smallest integer equal to or larger than the input argument.
- [EXP](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-exp.html)
- [FLOOR](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-floor.html)
- [LN](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-ln.html)
- [LOG10](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-log10.html)
- [MOD](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-mod.html)
- [POWER](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-power.html)
- [STEP](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-step.html)

### [Log Parsing Functions](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-pattern-matching-functions.html)

Amazon Kinesis Data Analytics features the following functions for log parsing:

- [FAST_REGEX_LOG_PARSER](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-fast-regex-log-parser.html)
- [FIXED_COLUMN_LOG_PARSE](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-fixed-column-log-parse.html): Parses fixed-width fields and automatically converts them to the given SQL types.
- [REGEX_LOG_PARSE](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-regex-log-parse.html): Returns regex matches from a source string in columnar format.
- [SYS_LOG_PARSE](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-sys-log-parse.html): Parses the standard syslog format:
- [VARIABLE_COLUMN_LOG_PARSE](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-variable-column-log-parse.html)
- [W3C_LOG_PARSE](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-w3c-log-parse.html)

### [Sorting Functions](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-sorting-functions.html)

Sorting functions for Kinesis Data Analytics streaming SQL.

- [Group Rank](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-group-rank-udx.html): Group Rank function

### [Statistical Variance and Deviation Functions](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-statistical-variance-deviation-functions.html)

Each of these functions takes a set of numbers, ignores nulls, and can be used as either an aggregate function or an analytical function.

- [HOTSPOTS](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sqlrf-hotspots.html): Overview of Kinesis Data Analytics HOTSPOTS SQL function
- [RANDOM_CUT_FOREST](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sqlrf-random-cut-forest.html): Detects anomalies in your data stream.Â  A record is an anomaly if it is distant from other records.Â  To detect anomalies in individual record columns, see .
- [RANDOM_CUT_FOREST_WITH_EXPLANATION](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sqlrf-random-cut-forest-with-explanation.html): Computes an anomaly score and explains it for each record in your data stream.
- [STDDEV_POP](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-STDDEVPOP.html): Returns the square root of the population variance for <number expression>, evaluated for each row remaining in the group.
- [STDDEV_SAMP](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-STDDEVSAMP.html): Returns the statistical standard deviation of all values in <number-expression>, evaluated for each row remaining in the group and defined as the square root of the .
- [VAR_POP](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-VARPOP.html): Returns the population variance of a non-null set of numbers (nulls being ignored)
- [VAR_SAMP](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-VARSAMP.html): Returns the sample variance of a non-null set of numbers (nulls being ignored).

### [Streaming SQL Functions](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-streaming-sql-functions.html)

Functions that operate on streaming properties for Kinesis Data Analytics streaming SQL.

- [LAG](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-lag.html): LAG returns the evaluation of the expression (such as the name of a column) for the record that is N records before the current record in a given window.
- [Monotonic Function](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-monotonic.html)
- [NTH_VALUE](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-nth-value.html)

### [String and Search Functions](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-string-and-search-functions.html)

String and search functions for Kinesis Data Analytics streaming SQL.

- [CHAR_LENGTH / CHARACTER_LENGTH](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-char-length.html): Returns the length in characters of the string passed as the input argument.
- [INITCAP](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-initcap.html)
- [LOWER](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-lower.html)
- [OVERLAY](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-overlay.html)
- [POSITION](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-position.html)
- [REGEX_REPLACE](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-regex-replace.html): REGEX_REPLACE replaces a substring with an alternative substring.
- [SUBSTRING](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-substring.html)
- [TRIM](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-trim.html)
- [UPPER](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-upper.html)
