# Source: https://docs.oxla.com/sql-reference/sql-functions/math-functions/exp.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxla.com/llms.txt
> Use this file to discover all available pages before exploring further.

# EXP

## Overview

The `EXP()` function returns the exponential value of a number specified in the argument.

## Syntax

The syntax for the `EXP()` is:

```sql  theme={null}
EXP(number);
```

Where:

* `number`: The number for which you want to calculate the exponential value. Equivalent to the formula `e^number`.

## Examples

Let's explore examples to see how the `EXP()` function works.

### Case #1: Basic Usage

In this case, we use the `EXP()` function with positive and negative values.

```sql  theme={null}
SELECT EXP(0) AS "EXP of 0", 
      EXP(1) AS "EXP of 1",
      EXP(2) AS "EXP of 2",
      EXP(-1) AS "EXP of -1",
      EXP(-2) AS "EXP of -2";
```

You will get the following result:

```sql  theme={null}
EXP of 0  |     EXP of 1      |     EXP of 2     |      EXP of -1      |     EXP of -2      
----------+-------------------+------------------+---------------------+--------------------
        1 | 2.718281828459045 | 7.38905609893065 | 0.36787944117144233 | 0.1353352832366127
```

### Case #2: Using `EXP()` with Fractions

This case uses the `EXP()` function with a fractional argument.

```sql  theme={null}
SELECT EXP(3.2);
```

Here is the result:

```sql  theme={null}
        exp         
--------------------
 24.532531366911574
```

### Case #3: Using `EXP()` with Expressions

Here, we use the `EXP()` function with expressions.

```sql  theme={null}
SELECT EXP(5 * 5);
```

See the result below:

```sql  theme={null}
        exp        
-------------------
 72004899337.38588
```
