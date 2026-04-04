# Source: https://firebase.google.com/docs/reference/rules/rules.Duration.md.txt

# Interface: Duration

# [rules](https://firebase.google.com/docs/reference/rules/rules).Duration

interface static

Duration with nanosecond accuracy.

## Methods

### nanos

nanos() returns [rules.Integer](https://firebase.google.com/docs/reference/rules/rules.Integer)

Get the nanoseconds portion (signed) of the duration
from -999,999,999 to +999,999,999 inclusive.

Returns

:   `non-null `[rules.Integer](https://firebase.google.com/docs/reference/rules/rules.Integer) nanoseconds portion of the dutation.

### seconds

seconds() returns [rules.Integer](https://firebase.google.com/docs/reference/rules/rules.Integer)

Get the seconds portion (signed) of the duration
from -315,576,000,000 to +315,576,000,000 inclusive.

Returns

:   `non-null `[rules.Integer](https://firebase.google.com/docs/reference/rules/rules.Integer) seconds portion of the dutation.