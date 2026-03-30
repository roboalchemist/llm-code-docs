# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/cassandra-input/options-cassandra-input/where-clause.md

# WHERE Clause

When terms appear on both sides of a relational operator, the filter is applied to an indexed column. With column index filters, the term on the left of the operator is the name, and the term on the right is the value to filter on. When filtering on indexed columns, at least one equality operator must be present. Using inequality operators will result in ranges that are inclusive of the terms (for example, > is the same as >=, and < is the same as <=).

A `WHERE` clause may be used to filter rows that appear in the results.

```
SELECT ... WHERE KEY = keyname AND name1 = value1
SELECT ... WHERE KEY >= startkey and KEY =< endkey AND name1 = value1
SELECT ... WHERE KEY IN ('<key>', '<key>', '<key>', ...)
```
