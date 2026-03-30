# Package org.h2.expression.condition

---

package org.h2.expression.condition

Condition expressions.

- 

Related Packages

Package
Description
org.h2.expression

Expressions include mathematical operations, simple values, and others.

org.h2.expression.aggregate

Aggregate functions.

org.h2.expression.analysis

Base classes for data analysis operations and implementations of window
 functions.

org.h2.expression.function

Functions.

- 

Class
Description
BetweenPredicate

BETWEEN predicate.

BooleanTest

Boolean test (IS [NOT] { TRUE | FALSE | UNKNOWN }).

CompareLike

Pattern matching comparison expression: WHERE NAME LIKE ?

CompareLike.LikeType

The type of comparison.

Comparison

Example comparison expressions are ID=1, NAME=NAME, NAME IS NULL.

ConditionAndOr

An 'and' or 'or' condition as in WHERE ID=1 AND NAME=?

ConditionAndOrN

An 'and' or 'or' condition as in WHERE ID=1 AND NAME=? with N operands.

ConditionInArray

Quantified comparison predicate with array.

ConditionInConstantSet

Used for optimised IN(...) queries where the contents of the IN list are all
 constant and of the same type.

ConditionInList

An 'in' condition with a list of values, as in WHERE NAME IN(...)

ConditionInQuery

An IN() condition with a subquery, as in WHERE ID IN(SELECT ...)

ConditionLocalAndGlobal

A global condition or combination of local and global conditions.

ConditionNot

A NOT condition.

ExistsPredicate

Exists predicate as in EXISTS(SELECT ...)

IsJsonPredicate

IS JSON predicate.

NullPredicate

Null predicate (IS [NOT] NULL).

SimplePredicate

Base class for simple predicates.

TypePredicate

Type predicate (IS [NOT] OF).

UniquePredicate

Unique predicate as in UNIQUE(SELECT ...)