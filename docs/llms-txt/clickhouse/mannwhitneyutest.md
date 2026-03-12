# Source: https://clickhouse.ferndocs.com/reference/sql-reference/aggregate-functions/reference/mannwhitneyutest.md

---

description: Applies the Mann-Whitney rank test to samples from two populations.
sidebar_label: mannWhitneyUTest
sidebar_position: 161
slug: /sql-reference/aggregate-functions/reference/mannwhitneyutest
title: mannWhitneyUTest
doc_type: reference
---

Applies the Mann-Whitney rank test to samples from two populations.

**Syntax**

```sql
mannWhitneyUTest[(alternative[, continuity_correction])](sample_data, sample_index)
```

Values of both samples are in the `sample_data` column. If `sample_index` equals to 0 then the value in that row belongs to the sample from the first population. Otherwise it belongs to the sample from the second population.
The null hypothesis is that two populations are stochastically equal. Also one-sided hypothesises can be tested. This test does not assume that data have normal distribution.

**Arguments**

- `sample_data` — sample data. [Integer](../../../sql-reference/data-types/int-uint.md), [Float](../../../sql-reference/data-types/float.md) or [Decimal](../../../sql-reference/data-types/decimal.md).
- `sample_index` — sample index. [Integer](../../../sql-reference/data-types/int-uint.md).

**Parameters**

- `alternative` — alternative hypothesis. (Optional, default: `'two-sided'`.) [String](../../../sql-reference/data-types/string.md).
  - `'two-sided'`;
  - `'greater'`;
  - `'less'`.
- `continuity_correction` — if not 0 then continuity correction in the normal approximation for the p-value is applied. (Optional, default: 1.) [UInt64](../../../sql-reference/data-types/int-uint.md).

**Returned values**

[Tuple](../../../sql-reference/data-types/tuple.md) with two elements:

- calculated U-statistic. [Float64](../../../sql-reference/data-types/float.md).
- calculated p-value. [Float64](../../../sql-reference/data-types/float.md).

**Example**

Input table:

```text
┌─sample_data─┬─sample_index─┐
│          10 │            0 │
│          11 │            0 │
│          12 │            0 │
│           1 │            1 │
│           2 │            1 │
│           3 │            1 │
└─────────────┴──────────────┘
```

Query:

```sql
SELECT mannWhitneyUTest('greater')(sample_data, sample_index) FROM mww_ttest;
```

Result:

```text
┌─mannWhitneyUTest('greater')(sample_data, sample_index)─┐
│ (9,0.04042779918503192)                                │
└────────────────────────────────────────────────────────┘
```

**See Also**

- [Mann–Whitney U test](https://en.wikipedia.org/wiki/Mann%E2%80%93Whitney_U_test)
- [Stochastic ordering](https://en.wikipedia.org/wiki/Stochastic_ordering)
