# Source: https://firebase.google.com/docs/reference/rules/rules.math.md.txt

# Namespace: math

# [rules](https://firebase.google.com/docs/reference/rules/rules).math

namespace static

Globally available mathematical functions. These functions are accessed
using the `math.` prefix and operate on numerical values.

## Methods

### abs

static

abs(num) returns number

Absolute value of a numeric value.

|       #### Parameter       ||
|-----|-----------------------|
| num | number Numeric value. |

Returns

:   `non-null number` the absolute numeric value of the input.

#### Example

    math.abs(-1) == 1
    math.abs(1) == 1

### ceil

static

ceil(num) returns [rules.Integer](https://firebase.google.com/docs/reference/rules/rules.Integer)

Ceiling of the numeric value.

|       #### Parameter       ||
|-----|-----------------------|
| num | number Numeric value. |

Returns

:   `non-null `[rules.Integer](https://firebase.google.com/docs/reference/rules/rules.Integer) the ceiling of the given value.

#### Example

    math.ceil(2.0) == 2
    math.ceil(2.1) == 3
    math.ceil(2.7) == 3

### floor

static

floor(num) returns [rules.Integer](https://firebase.google.com/docs/reference/rules/rules.Integer)

Floor of the numeric value.

|       #### Parameter       ||
|-----|-----------------------|
| num | number Numeric value. |

Returns

:   `non-null `[rules.Integer](https://firebase.google.com/docs/reference/rules/rules.Integer) the floor of the given value.

#### Example

    math.floor(1.9) == 1
    math.floor(2.0) == 2
    math.floor(2.7) == 2

### isInfinite

static

isInfinite(num) returns [rules.Boolean](https://firebase.google.com/docs/reference/rules/rules.Boolean)

Test whether the value is Â±â.

|       #### Parameter       ||
|-----|-----------------------|
| num | number Numeric value. |

Returns

:   `non-null `[rules.Boolean](https://firebase.google.com/docs/reference/rules/rules.Boolean) true if the number is positive or negative
    infinity.

#### Example

    math.isInfinite(â) == true
    math.isInfinite(100) == false

### isNaN

static

isNaN(num) returns [rules.Boolean](https://firebase.google.com/docs/reference/rules/rules.Boolean)

Test whether the value is Â±â.

|       #### Parameter       ||
|-----|-----------------------|
| num | number Numeric value. |

Returns

:   `non-null `[rules.Boolean](https://firebase.google.com/docs/reference/rules/rules.Boolean) true if the value is not a number.

#### Example

    math.isNaN(NaN) == true
    math.isNaN(100) == false

### pow

static

pow(base, exponent) returns [rules.Float](https://firebase.google.com/docs/reference/rules/rules.Float)

Return the value of the first argument raised to the power of the second
argument.

|              #### Parameter              ||
|----------|--------------------------------|
| base     | number Numeric base value.     |
| exponent | number Numeric exponent value. |

Returns

:   `non-null `[rules.Float](https://firebase.google.com/docs/reference/rules/rules.Float) the value of the first argument raised to the power
    of the second argument.

#### Example

    math.pow(2, 2) == 4
    math.pow(1.5, 2) == 2.25
    math.pow(4, 0.5) == 2

### round

static

round(num) returns [rules.Integer](https://firebase.google.com/docs/reference/rules/rules.Integer)

Round the input value to the nearest int.

|       #### Parameter       ||
|-----|-----------------------|
| num | number Numeric value. |

Returns

:   `non-null `[rules.Integer](https://firebase.google.com/docs/reference/rules/rules.Integer) the nearest int to the given value.

#### Example

    math.round(1.9) == 2
    math.round(2.4) == 2
    math.round(2.5) == 3

### sqrt

static

sqrt(num) returns [rules.Float](https://firebase.google.com/docs/reference/rules/rules.Float)

Square root of the input value.

|       #### Parameter       ||
|-----|-----------------------|
| num | number Numeric value. |

Returns

:   `non-null `[rules.Float](https://firebase.google.com/docs/reference/rules/rules.Float) the square root of the input value.

#### Example

    math.sqrt(4) == 2.0
    math.sqrt(2.25) == 1.5