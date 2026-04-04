# Source: https://docs.prefect.io/v3/api-ref/python/prefect-utilities-math.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# math

# `prefect.utilities.math`

## Functions

### `poisson_interval` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/math.py#L5" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
poisson_interval(average_interval: float, lower: float = 0, upper: float = 1) -> float
```

Generates an "inter-arrival time" for a Poisson process.

Draws a random variable from an exponential distribution using the inverse-CDF
method. Can optionally be passed a lower and upper bound between (0, 1] to clamp
the potential output values.

### `exponential_cdf` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/math.py#L21" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
exponential_cdf(x: float, average_interval: float) -> float
```

### `lower_clamp_multiple` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/math.py#L26" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
lower_clamp_multiple(k: float) -> float
```

Computes a lower clamp multiple that can be used to bound a random variate drawn
from an exponential distribution.

Given an upper clamp multiple `k` (and corresponding upper bound k \* average\_interval),
this function computes a lower clamp multiple `c` (corresponding to a lower bound
c \* average\_interval) where the probability mass between the lower bound and the
median is equal to the probability mass between the median and the upper bound.

### `clamped_poisson_interval` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/math.py#L43" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
clamped_poisson_interval(average_interval: float, clamping_factor: float = 0.3) -> float
```

Bounds Poisson "inter-arrival times" to a range defined by the clamping factor.

The upper bound for this random variate is: average\_interval \* (1 + clamping\_factor).
A lower bound is picked so that the average interval remains approximately fixed.

### `bounded_poisson_interval` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/utilities/math.py#L64" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
bounded_poisson_interval(lower_bound: float, upper_bound: float) -> float
```

Bounds Poisson "inter-arrival times" to a range.

Unlike `clamped_poisson_interval` this does not take a target average interval.
Instead, the interval is predetermined and the average is calculated as their
midpoint. This allows Poisson intervals to be used in cases where a lower bound
must be enforced.


Built with [Mintlify](https://mintlify.com).