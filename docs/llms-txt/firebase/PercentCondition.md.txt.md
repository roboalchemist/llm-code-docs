# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/PercentCondition.md.txt

# PercentCondition

public final class **PercentCondition** extends Object  
Represents a condition that compares the instance pseudo-random percentile to a given limit.

### Public Method Summary

|---|---|
| int | [getMicroPercent](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/PercentCondition#getMicroPercent())() Gets the limit of percentiles to target in micro-percents when using the LESS_OR_EQUAL and GREATER_THAN operators. |
| MicroPercentRange | [getMicroPercentRange](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/PercentCondition#getMicroPercentRange())() Gets micro-percent interval to be used with the BETWEEN operator. |
| [PercentConditionOperator](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/PercentConditionOperator) | [getPercentConditionOperator](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/PercentCondition#getPercentConditionOperator())() Gets choice of percent operator to determine how to compare targets to percent(s). |
| String | [getSeed](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/PercentCondition#getSeed())() The seed used when evaluating the hash function to map an instance to a value in the hash space. |

### Inherited Method Summary

From class java.lang.Object

|---|---|
| Object | clone() |
| boolean | equals(Object arg0) |
| void | finalize() |
| final Class\<?\> | getClass() |
| int | hashCode() |
| final void | notify() |
| final void | notifyAll() |
| String | toString() |
| final void | wait(long arg0, int arg1) |
| final void | wait(long arg0) |
| final void | wait() |

## Public Methods

#### public int
**getMicroPercent**
()

Gets the limit of percentiles to target in micro-percents when using the LESS_OR_EQUAL and
GREATER_THAN operators. The value must be in the range \[0 and 100000000\].

##### Returns

- micro percent.

#### public MicroPercentRange
**getMicroPercentRange**
()

Gets micro-percent interval to be used with the BETWEEN operator.

##### Returns

- micro percent range.

#### public [PercentConditionOperator](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/PercentConditionOperator)
**getPercentConditionOperator**
()

Gets choice of percent operator to determine how to compare targets to percent(s).

##### Returns

- operator.

#### public String
**getSeed**
()

The seed used when evaluating the hash function to map an instance to a value in the hash
space. This is a string which can have 0 - 32 characters and can contain ASCII characters
\[-_.0-9a-zA-Z\].The string is case-sensitive.

##### Returns

- seed.