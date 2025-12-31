# Source: https://firebase.google.com/docs/reference/rules/rules.Timestamp_.md.txt

# Interface: Timestamp

# [rules](https://firebase.google.com/docs/reference/rules/rules).Timestamp

interface static

A timestamp in UTC with nanosecond accuracy.

## Methods

### date

date() returns [rules.Timestamp](https://firebase.google.com/docs/reference/rules/rules.Timestamp_)

Timestamp value containing year, month, and day only.

Returns

:   `non-null `[rules.Timestamp](https://firebase.google.com/docs/reference/rules/rules.Timestamp_) The timestamp.

### day

day() returns [rules.Integer](https://firebase.google.com/docs/reference/rules/rules.Integer)

Get the day value of the timestamp.

Returns

:   `non-null `[rules.Integer](https://firebase.google.com/docs/reference/rules/rules.Integer) day value.

### dayOfWeek

dayOfWeek() returns [rules.Integer](https://firebase.google.com/docs/reference/rules/rules.Integer)

Get the day of the week as a value from 1 to 7.

Returns

:   `non-null `[rules.Integer](https://firebase.google.com/docs/reference/rules/rules.Integer) the day of the week.

### dayOfYear

dayOfYear() returns [rules.Integer](https://firebase.google.com/docs/reference/rules/rules.Integer)

Get the day of the year as a value from 1 to 366.

Returns

:   `non-null `[rules.Integer](https://firebase.google.com/docs/reference/rules/rules.Integer) the day of the year.

### hours

hours() returns [rules.Integer](https://firebase.google.com/docs/reference/rules/rules.Integer)

Get the hours value of the timestamp.

Returns

:   `non-null `[rules.Integer](https://firebase.google.com/docs/reference/rules/rules.Integer) hours value.

### minutes

minutes() returns [rules.Integer](https://firebase.google.com/docs/reference/rules/rules.Integer)

Get the minutes value of the timestamp.

Returns

:   `non-null `[rules.Integer](https://firebase.google.com/docs/reference/rules/rules.Integer) minutes value.

### month

month() returns [rules.Integer](https://firebase.google.com/docs/reference/rules/rules.Integer)

Get the month value of the timestamp.

Returns

:   `non-null `[rules.Integer](https://firebase.google.com/docs/reference/rules/rules.Integer) month value.

### nanos

nanos() returns [rules.Integer](https://firebase.google.com/docs/reference/rules/rules.Integer)

Get the nanos value of the timestamp.

Returns

:   `non-null `[rules.Integer](https://firebase.google.com/docs/reference/rules/rules.Integer) nanos value.

### seconds

seconds() returns [rules.Integer](https://firebase.google.com/docs/reference/rules/rules.Integer)

Get the seconds value of the timestamp.

Returns

:   `non-null `[rules.Integer](https://firebase.google.com/docs/reference/rules/rules.Integer) seconds value.

### time

time() returns [rules.Duration](https://firebase.google.com/docs/reference/rules/rules.Duration)

Get the duration value from the time portion of the timestamp.

Returns

:   `non-null `[rules.Duration](https://firebase.google.com/docs/reference/rules/rules.Duration) duration value.

### toMillis

toMillis() returns [rules.Integer](https://firebase.google.com/docs/reference/rules/rules.Integer)

Get the time in milliseconds since the epoch.

Returns

:   `non-null `[rules.Integer](https://firebase.google.com/docs/reference/rules/rules.Integer) time in milliseconds.

### year

year() returns [rules.Integer](https://firebase.google.com/docs/reference/rules/rules.Integer)

Get the year value of the timestamp.

Returns

:   `non-null `[rules.Integer](https://firebase.google.com/docs/reference/rules/rules.Integer) year value.