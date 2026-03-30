# Package org.h2.expression

---

package org.h2.expression

Expressions include mathematical operations, simple values, and others.

- 

Related Packages

Package
Description
org.h2

Implementation of the JDBC driver.

org.h2.expression.aggregate

Aggregate functions.

org.h2.expression.analysis

Base classes for data analysis operations and implementations of window
 functions.

org.h2.expression.condition

Condition expressions.

org.h2.expression.function

Functions.

- 

Class
Description
Alias

A column alias as in SELECT 'Hello' AS NAME ...

ArrayConstructorByQuery

Array value constructor by query.

ArrayElementReference

Array element reference.

BinaryOperation

A mathematical expression, or string concatenation.

BinaryOperation.OpType
 
CompatibilityDatePlusTimeOperation

A compatibility mathematical operation with datetime values.

ConcatenationOperation

Character string concatenation as in `'Hello' || 'World'`, binary
 string concatenation as in `X'01' || X'AB'` or an array concatenation
 as in `ARRAY[1, 2] || 3`.

DomainValueExpression

An expression representing a value for domain constraint.

Expression

An expression is a operation, a value, or a function in a query.

ExpressionColumn

A column reference expression that represents a column of a table or view.

ExpressionList

A list of expressions, as in (ID, NAME).

ExpressionVisitor

The visitor pattern is used to iterate through all expressions of a query
 to optimize a statement.

ExpressionWithFlags

Expression with flags.

ExpressionWithVariableParameters

An expression with variable number of parameters.

FieldReference

Field reference.

Format

A format clause such as FORMAT JSON.

Format.FormatEnum

Supported formats.

IntervalOperation

A mathematical operation with intervals.

IntervalOperation.IntervalOpType
 
Operation0

Operation without subexpressions.

Operation1

Operation with one argument.

Operation1_2

Operation with one or two arguments.

Operation2

Operation with two arguments.

OperationN

Operation with many arguments.

Parameter

A parameter of a prepared statement.

ParameterInterface

The interface for client side (remote) and server side parameters.

ParameterRemote

A client side (remote) parameter.

Rownum

Represents the ROWNUM function.

SearchedCase

A searched case.

SequenceValue

Wraps a sequence when used in a statement.

SimpleCase

A simple case.

SimpleCase.SimpleWhen
 
Subquery

A query returning a single value.

TimeZoneOperation

A time zone specification (AT { TIME ZONE | LOCAL }).

TypedValueExpression

An expression representing a constant value with a type cast.

UnaryOperation

Unary operation.

ValueExpression

An expression representing a constant value.

Variable

A user-defined variable, for example: @ID.

Wildcard

A wildcard expression as in SELECT * FROM TEST.