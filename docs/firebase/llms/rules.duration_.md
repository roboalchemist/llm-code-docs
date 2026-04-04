# Source: https://firebase.google.com/docs/reference/rules/rules.duration_.md.txt

# Namespace: duration

# [rules](https://firebase.google.com/docs/reference/rules/rules).duration

namespace static

Globally available duration functions. These functions are accessed using the
`duration.` prefix.

## Methods

### abs

static

abs(duration) returns [rules.Duration](https://firebase.google.com/docs/reference/rules/rules.Duration)

Absolute value of a duration.

|                                                           #### Parameter                                                            ||
|----------|---------------------------------------------------------------------------------------------------------------------------|
| duration | [rules.Duration](https://firebase.google.com/docs/reference/rules/rules.Duration) Duration value. Value must not be null. |

Returns

:   `non-null `[rules.Duration](https://firebase.google.com/docs/reference/rules/rules.Duration) the absolute duration value of the input.

#### Example

    duration.abs(duration.value(-10, 's')) == duration.value(10, 's')

### time

static

time(hours, mins, secs, nanos) returns [rules.Duration](https://firebase.google.com/docs/reference/rules/rules.Duration)

Create a duration from hours, minutes, seconds, and nanoseconds.

|                                                                   #### Parameter                                                                    ||
|-------|----------------------------------------------------------------------------------------------------------------------------------------------|
| hours | [rules.Integer](https://firebase.google.com/docs/reference/rules/rules.Integer) Hours portion of the duration. Value must not be null.       |
| mins  | [rules.Integer](https://firebase.google.com/docs/reference/rules/rules.Integer) Minutes portion of the duration. Value must not be null.     |
| secs  | [rules.Integer](https://firebase.google.com/docs/reference/rules/rules.Integer) Seconds portion of the duration. Value must not be null.     |
| nanos | [rules.Integer](https://firebase.google.com/docs/reference/rules/rules.Integer) Nanoseconds portion of the duration. Value must not be null. |

Returns

:   `non-null `[rules.Duration](https://firebase.google.com/docs/reference/rules/rules.Duration) a Duration.

### value

static

value(magnitude, unit) returns [rules.Duration](https://firebase.google.com/docs/reference/rules/rules.Duration)

Create a duration from a numeric magnitude and string unit.

*** ** * ** ***

| Unit | Description  |
|------|--------------|
| w    | Weeks        |
| d    | Days         |
| h    | Hours        |
| m    | Minutes      |
| s    | Seconds      |
| ms   | Milliseconds |
| ns   | Nanoseconds  |

|                                                                     #### Parameter                                                                     ||
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------|
| magnitude | [rules.Integer](https://firebase.google.com/docs/reference/rules/rules.Integer) Unitless magnitude of the duration. Value must not be null. |
| unit      | [rules.String](https://firebase.google.com/docs/reference/rules/rules.String) Unit of the duration. Value must not be null.                 |

Returns

:   `non-null `[rules.Duration](https://firebase.google.com/docs/reference/rules/rules.Duration) a Duration.

#### Example

    duration.value(1, 'w') // Create a duration for 1 week of time.