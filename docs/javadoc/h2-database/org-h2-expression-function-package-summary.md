# Package org.h2.expression.function

---

package org.h2.expression.function

Functions.

- 

Related Packages

Package
Description
org.h2.expression

Expressions include mathematical operations, simple values, and others.

org.h2.expression.function.table

Table value functions.

org.h2.expression.aggregate

Aggregate functions.

org.h2.expression.analysis

Base classes for data analysis operations and implementations of window
 functions.

org.h2.expression.condition

Condition expressions.

- 

Class
Description
ArrayFunction

An array function.

BitFunction

A bitwise function.

BuiltinFunctions

Maintains the list of built-in functions.

CardinalityExpression

Cardinality expression.

CastSpecification

A cast specification.

CoalesceFunction

A COALESCE, GREATEST, or LEAST function.

CompatibilitySequenceValueFunction

NEXTVAL() and CURRVAL() compatibility functions.

CompressFunction

A COMPRESS or EXPAND function.

ConcatFunction

A CONCAT or CONCAT_WS function.

CryptFunction

An ENCRYPT or DECRYPT function.

CSVWriteFunction

A CSVWRITE function.

CurrentDateTimeValueFunction

Current datetime value function.

CurrentGeneralValueSpecification

Simple general value specifications.

DataTypeSQLFunction

DATA_TYPE_SQL() function.

DateTimeFormatFunction

A date-time format function.

DateTimeFunction

A date-time function.

DayMonthNameFunction

A DAYNAME() or MONTHNAME() function.

DBObjectFunction

DB_OBJECT_ID() and DB_OBJECT_SQL() functions.

FileFunction

A FILE_READ or FILE_WRITE function.

Function0_1

Function with one optional argument.

Function1

Function with one argument.

Function1_2

Function with two arguments.

Function2

Function with two arguments.

FunctionN

Function with many arguments.

GCDFunction

GCD and LCM functions.

HashFunction

A HASH or ORA_HASH function.

JavaFunction

This class wraps a user-defined function.

JsonConstructorFunction

JSON constructor function.

LengthFunction

CHAR_LENGTH(), or OCTET_LENGTH() function.

MathFunction

A math function.

MathFunction1

A math function with one argument and DOUBLE PRECISION result.

MathFunction2

A math function with two arguments and DOUBLE PRECISION result.

NamedExpression

A function-like expression with a name.

NullIfFunction

A NULLIF function.

RandFunction

A RAND, SECURE_RAND, or RANDOM_UUID function.

RegexpFunction

A regular expression function.

SessionControlFunction

An ABORT_SESSION() or CANCEL_SESSION() function.

SetFunction

A SET function.

SignalFunction

A SIGNAL function.

SoundexFunction

A SOUNDEX or DIFFERENCE function.

StringFunction

An string function with multiple arguments.

StringFunction1

A string function with one argument.

StringFunction2

A string function with two arguments.

SubstringFunction

A SUBSTRING function.

SysInfoFunction

Database or session information function.

TableInfoFunction

A table information function.

ToCharFunction

Emulates Oracle's TO_CHAR function.

ToCharFunction.Capitalization

Represents a capitalization / casing strategy.

TrimFunction

A TRIM, LTRIM, RTRIM, or BTRIM function.

TruncateValueFunction

A TRUNCATE_VALUE function.

XMLFunction

An XML function.