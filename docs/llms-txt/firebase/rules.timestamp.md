# Source: https://firebase.google.com/docs/reference/rules/rules.timestamp.md.txt

# Namespace: timestamp

# [rules](https://firebase.google.com/docs/reference/rules/rules).timestamp

namespace static

Globally available timestamp functions. These functions are accessed
using the `timestamp.` prefix.

## Methods

### date

static

date(year, month, day) returns [rules.Timestamp](https://firebase.google.com/docs/reference/rules/rules.Timestamp_)

Make a timestamp from a year, month, and day.

|                                                      #### Parameter                                                       ||
|-------|--------------------------------------------------------------------------------------------------------------------|
| year  | [rules.Integer](https://firebase.google.com/docs/reference/rules/rules.Integer) The year. Value must not be null.  |
| month | [rules.Integer](https://firebase.google.com/docs/reference/rules/rules.Integer) The month. Value must not be null. |
| day   | [rules.Integer](https://firebase.google.com/docs/reference/rules/rules.Integer) The day. Value must not be null.   |

Returns

:   `non-null `[rules.Timestamp](https://firebase.google.com/docs/reference/rules/rules.Timestamp_) a timestamp.

#### Example

    // Timestamp for 1984-01-02T00:00:00Z
    timestamp.date(1984, 1, 2);

### value

static

value(epochMillis) returns [rules.Timestamp](https://firebase.google.com/docs/reference/rules/rules.Timestamp_)

Make a timestamp from an epoch time in milliseconds.

|                                                                  #### Parameter                                                                  ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------|
| epochMillis | [rules.Integer](https://firebase.google.com/docs/reference/rules/rules.Integer) Time since the epoch in ms. Value must not be null. |

Returns

:   `non-null `[rules.Timestamp](https://firebase.google.com/docs/reference/rules/rules.Timestamp_) a timestamp.