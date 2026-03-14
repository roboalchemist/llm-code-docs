# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/helper/DateHelper.md

# [DateHelper](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper)

A static class offering date manipulation, comparison, parsing and formatting helper methods.

Parsing strings
---------------

Use `DateHelper.parse()` to parse strings into dates. It accepts a date string and a format specifier. The format specifier is string built up using the following tokens:

Unit

Token

Description

Year

YYYY

4-digits year, like: 2018

Y

numeric, any number of digits

YY

< 68 -> 2000, > 68 -> 1900

Month

MM

01 - 12

Month

MMM

Short name of the month

Date

DD

01 - 31

Hour

HH

00 - 23 or 1 - 12

Minute

mm

00 - 59

Second

ss

00 - 59

Millisecond

S

0 - 9 \[000, 100, 200 .. 900 \]

SS

00 - 99 \[000, 010, 020 .. 990 \]

SSS

000 - 999 \[000, 001, 002 .. 999 \]

AM/PM

A

AM or PM

a

am or pm

TimeZone

Z

Z for UTC or +-HH:mm. Local timezone if left out

Predefined

L

Long date, MM/DD/YYYY

LT

Long time, HH:mm A

Default parse format is: `'YYYY-MM-DDTHH:mm:ss.SSSZ'` see [defaultParseFormat](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper#property-defaultParseFormat-static).

For example:

```
DateHelper.parse('2018-11-06', 'YYYY-MM-DD');
DateHelper.parse('13:14', 'HH:mm');
DateHelper.parse('6/11/18', 'DD/MM/YY');
```

Note that date strings without timezone information ('Z' or '+-HH:mm') will be in the local timezone. Eg. '2024-05-14' -> local time, '2024-05-14Z' -> UTC

Formatting dates
----------------

Use `DateHelper.format()` to create a string from a date using a format specifier. The format specifier is similar to that used when parsing strings. It can use the following tokens (input used for output below is `new Date(2018,8,9,18,7,8,145)`):

Unit

Token

Description & output

Year

YYYY

2018

YY

18

Y

2018

Quarter

Q

3

Qo

3rd

Month

MMMM

September

MMM

Sep

MM

09

Mo

9th

M

9

Week (iso)

WW

37 (2 digit, zero padded)

Wo

37th

W

37

WWp

Week 37 (localized prefix, zero pad)

Wp

Week 37 (localized prefix)

WWp0

W37 (localized prefix)

Wp0

W37 (localized prefix)

Date

DDDD

Day of year, 3 digits

DDDo

Day of year, ordinal

DDD

Day of year

DD

09

Do

9th

D

9

Weekday

dddd

Sunday

ddd

Sun

dd

Su

d1

S

do

0th

d

0

Hour

HH

18 (00 - 23)

H

18 (0 - 23)

hh

06 (00 - 12)

h

6 (0 - 12)

KK

19 (01 - 24)

K

19 (1 - 24)

kk

06 or 18, locale determines

k

6 or 18, locale determines

Minute

mm

07

m

7

Second

ss

08

s

8

Millisecond

S

1 (100ms)

SS

14 (140ms)

SSS

145 (145ms)

AM/PM

A

AM or PM

a

am or pm

Predefined

LT

H: 2-digit (2d), m: 2d

(uses browser locale)

LTS

H: 2d, m: 2d, s : 2d

LST

Depends on 12 or 24 hour clock

12h, H : 1d, m : 0 or 2d

24h, H : 2d, m : 2d

L

Y: numeric (n), M : 2d, D : 2d

l

Y: n, M : n, D : n

LL

Y: n, M : long (l), D : n

ll

Y: n, M : short (s), D : n

LLL

Y: n, M : l, D : n, H: n, m: 2d

lll

Y: n, M : s, D : n, H: n, m: 2d

LLLL

Y: n, M : l, D : n, H: n, m: 2d, d: l

llll

Y: n, M : s, D : n, H: n, m: 2d, d: s

u

YYYYMMDDZ in UTC zone

uu

YYYYMMDDTHHMMSSZ in UTC zone

Default format is: `'YYYY-MM-DDTHH:mm:ssZ'` see [defaultFormat](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper#property-defaultFormat-static)

For example:

```
DateHelper.format(new Date(2018,10,6), 'YYYY-MM-DD'); // 2018-11-06
DateHelper.format(new Date(2018,10,6), 'M/D/YY'); // 11/6/18
```

### Using embedded text inside format string

Arbitrary text can be embedded in the format string by wrapping it with {}:

```
DateHelper.format(new Date(2019, 7, 16), '{It is }dddd{, yay!}') -> It is Friday, yay!
```

Overriding Formatters
---------------------

To override formatters, you need to configure the locale.

Here is a sample code snippet demonstrating how to override formatters using a custom locale.

```
const customLocale = {
    DateHelper : {
        formats : {
            ll : date => {
                return DateHelper.format(date, 'DD.MM.YYYY');
            },
            L : date => {
                return DateHelper.format(date, 'DD--MM--YYYY')
            },
            LT : date => {
                return DateHelper.format(date, 'HH-mm');
            },
            LTS : date => {
                return DateHelper.format(date, 'HH-mm-ss');
            }
        }
    }
};

// Extend the English locale with the custom locale
LocaleHelper.publishLocale('En', locale);
```

Once the custom locale is published, you can use the overridden formatters with `DateHelper.format()`.

```
DateHelper.format(new Date(2024, 0, 12, 12, 4, 5), 'll') // Output: 12.01.2024
DateHelper.format(new Date(2024, 0, 12, 12, 4, 5), 'L') // Output: 12--01--2024
DateHelper.format(new Date(2024, 0, 12, 12, 4, 5), 'LT') // Output: 12-04
DateHelper.format(new Date(2024, 0, 12, 12, 4, 5), 'LTS') // Output: 12-04-05
```

Unit names
----------

Many DateHelper functions (for example add, as, set) accepts a unit among their params. The following units are available:

Unit

Aliases

millisecond

millisecond, milliseconds, ms

second

second, seconds, s

minute

minute, minutes, m

hour

hour, hours, h

day

day, days, d

week

week, weeks, w

month

month, months, mon, mo, M

quarter

quarter, quarters, q

year

year, years, y

decade

decade, decades, dec

For example:

```
DateHelper.add(date, 2, 'days');
DateHelper.as('hour', 7200, 'seconds');
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[defaultFormat](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#property-defaultFormat-static)
Get/set the default format used by `format()` and `parse()`. Defaults to `'YYYY-MM-DDTHH:mm:ssZ'` (~ISO 8601 Date and time, `'1962-06-17T09:21:34Z'`).

[defaultParseFormat](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#property-defaultParseFormat-static)
Get/set the default format used by `parse()`. Defaults to `'YYYY-MM-DDTHH:mm:ss.SSSZ'` or [defaultFormat](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper#property-defaultFormat-static) (~ISO 8601 Date and time, `'1962-06-17T09:21:34.123Z'`).

[amIndicator](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#property-amIndicator-static)
Get the local AM indicator string.

[pmIndicator](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#property-pmIndicator-static)
Get the local PM indicator string.

[weekStartDay](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#property-weekStartDay-static)
Get the first day of week, 0-6 (Sunday-Saturday). This is determined by the current locale's `DateHelper.weekStartDay` parameter.

[nonWorkingDays](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#property-nonWorkingDays-static)
Get non-working days as an object where keys are day indices, 0-6 (Sunday-Saturday), and the value is `true`. This is determined by the current locale's `DateHelper.nonWorkingDays` parameter.

For example:

```
{
    0 : true, // Sunday
    6 : true  // Saturday
}
```

[nonWorkingDaysAsArray](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#property-nonWorkingDaysAsArray-static)
Get non-working days as an array of day indices, 0-6 (Sunday-Saturday). This is determined by the current locale's `DateHelper.nonWorkingDays` parameter.

For example:

```
[ 0, 6 ] // Sunday & Saturday
```

[weekends](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#property-weekends-static)
Get weekend days as an object where keys are day indices, 0-6 (Sunday-Saturday), and the value is `true`. Weekends are days which are declared as weekend days by the selected country and defined by the current locale's `DateHelper.weekends` parameter. To get non-working days see [nonWorkingDays](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper#property-nonWorkingDays-static).

For example:

```
{
    0 : true, // Sunday
    6 : true  // Saturday
}
```

## Functions

Functions are methods available for calling on the class

[makeKey](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-makeKey-static)
A utility function to create a sortable string key for the passed date or ms timestamp using the `'YYYY-MM-DD'` format.

[parseKey](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-parseKey-static)
A utility function to parse a sortable string to a date using the `'YYYY-MM-DD'` format.

[parse](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-parse-static)
Returns a date created from the supplied string using the specified format. Will try to create even if format is left out, by first using the default format (see [defaultFormat](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper#property-defaultFormat-static), by default `YYYY-MM-DDTHH:mm:ssZ`) and then using `new Date(dateString)`. Supported tokens:

Unit

Token

Description

Year

YYYY

4-digits year, like: 2018

Y

numeric, any number of digits

YY

< 68 -> 2000, > 68 -> 1900

Month

MM

01 - 12

Month

MMM

Short name of the month

Date

DD

01 - 31

Hour

HH

00 - 23 or 1 - 12

Minute

mm

00 - 59

Second

ss

00 - 59

Millisecond

S

0 - 9 \[000, 100, 200 .. 900 \]

SS

00 - 99 \[000, 010, 020 .. 990 \]

SSS

000 - 999 \[000, 001, 002 .. 999 \]

AM/PM

A

AM or PM

a

am or pm

TimeZone

Z

Z for UTC or +-HH:mm. Local timezone if left out

Predefined

L

Long date, MM/DD/YYYY

LT

Long time, HH:mm A

Predefined formats and functions used to parse tokens can be localized, see for example the swedish locale `SvSE.js`.

NOTE: If no date parameters are provided then `Jan 01 2020` is used as a default date.

Note that date strings without timezone information ('Z' or '+-HH:mm') will be in the local timezone. Eg. '2024-05-14' -> local time, '2024-05-14Z' -> UTC

[create](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-create-static)
Creates a date from a date definition object. The object can have the following properties:

* year
* month
* date (day in month)
* hours
* minutes
* seconds
* milliseconds
* amPm : 'am' or 'pm', implies 12-hour clock
* timeZone : offset from UTC in minutes

[format](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-format-static)
Converts a date to string with the specified format. Formats heavily inspired by https://momentjs.com. Available formats (input used for output below is `new Date(2018,8,9,18,7,8,145)`):

Unit

Token

Description & output

Decade

DC

2010s

Year

YYYY

2018

YY

18

Y

2018

Quarter

Q

3

Qo

3rd

Month

MMMM

September

MMM

Sep

MM

09

Mo

9th

M

9

Week (iso)

WW

37 (2 digit, zero padded)

Wo

37th

W

37

WWp

Week 37 (localized prefix, zero pad)

Wp

Week 37 (localized prefix)

WWp0

W37 (localized prefix)

Wp0

W37 (localized prefix)

Date

DDDD

Day of year, 3 digits

DDDo

Day of year, ordinal

DDD

Day of year

DD

09

Do

9th

D

9

Weekday

dddd

Sunday

ddd

Sun

dd

Su

d1

S

do

0th

d

0

Hour

HH

18 (00 - 23)

H

18 (0 - 23)

hh

06 (00 - 12)

h

6 (0 - 12)

KK

19 (01 - 24)

K

19 (1 - 24)

kk

06 or 18, locale determines

k

6 or 18, locale determines

Minute

mm

07

m

7

Second

ss

08

s

8

Millisecond

S

1 (100ms)

SS

14 (140ms)

SSS

145 (145ms)

AM/PM

A

AM or PM

a

am or pm

Predefined

LT

H: 2-digit (2d), m: 2d

(uses browser locale)

LTS

H: 2d, m: 2d, s : 2d

LST

Depends on 12 or 24 hour clock

12h, H : 1d, m : 0 or 2d

24h, H : 2d, m : 2d

L

Y: numeric (n), M : 2d, D : 2d

l

Y: n, M : n, D : n

LL

Y: n, M : long (l), D : n

ll

Y: n, M : short (s), D : n

LLL

Y: n, M : l, D : n, H: n, m: 2d

lll

Y: n, M : s, D : n, H: n, m: 2d

LLLL

Y: n, M : l, D : n, H: n, m: 2d, d: l

llll

Y: n, M : s, D : n, H: n, m: 2d, d: s

Some examples:

```
DateHelper.format(new Date(2019, 7, 16), 'dddd') -> Friday
DateHelper.format(new Date(2019, 7, 16, 14, 27), 'HH:mm') --> 14:27
DateHelper.format(new Date(2019, 7, 16, 14, 27), 'L HH') --> 2019-07-16 14
```

### Using embedded text inside format string

Arbitrary text can be embedded in the format string by wrapping it with {}:

```
DateHelper.format(new Date(2019, 7, 16), '{It is }dddd{, yay!}') -> It is Friday, yay!
```

[formatRange](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-formatRange-static)
Formats a range of `dates` using the specified `format`. Because two dates are involved, the `format` specifier uses the tokens `S{}` and `E{}`. The text contained between the `{}` is the [format](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper#function-format-static) for the start date or end date, respectively. Text not inside these tokens is retained verbatim.

For example:

```
 DateHelper.formatRange(dates, 'S{DD MMM YYYY} - E{DD MMM YYYY}');
```

The above will format `dates[0]` based on the `S{DD MMM YYYY}` segment and `dates[1] using` E{DD MMM YYYY}`. The` ' - '\` between these will remain between the two formatted dates.

[asMilliseconds](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-asMilliseconds-static)
Converts the specified amount of desired unit into milliseconds. Can be called by only specifying a unit as the first argument, it then uses `amount = 1`.

For example:

```
asMilliseconds('hour') == asMilliseconds(1, 'hour')
```

[asMonths](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-asMonths-static)
Converts the passed Date to an accurate number of months passed since the epoch start.

[formatDelta](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-formatDelta-static)
Converts a millisecond time delta to a human-readable form. For example `1000 * 60 * 60 * 50` milliseconds would be rendered as `'2 days, 2 hours'`.

[getDelta](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-getDelta-static)
Converts a millisecond time delta to an object structure. For example `1000 * 60 * 60 * 50` milliseconds the result would be as:

```
{
    day  : 2,
    hour : 2
}
```

[as](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-as-static)
Converts the specified amount of one unit (`fromUnit`) into an amount of another unit (`toUnit`).

[is24HourFormat](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-is24HourFormat-static)
Returns `true` for 24-hour format.

[add](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-add-static)
Add days, hours etc. to a date. Always clones the date, original will be left unaffected.

[diff](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-diff-static)
Calculates the difference between two dates, in the specified unit.

[startOf](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-startOf-static)
Sets the date to the start of the specified unit, by default returning a clone of the date instead of changing it in place.

[endOf](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-endOf-static)
Returns the end point of the passed date, that is 00:00:00 of the day after the passed date.

[clone](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-clone-static)
Creates a clone of the specified date

[clearTime](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-clearTime-static)
Removes time from a date (same as calling [startOf(date)](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper#function-startOf-static)).

[getTimeOfDay](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-getTimeOfDay-static)
Returns the elapsed milliseconds from the start of the specified date.

[set](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-set-static)
Sets a part of a date (in place).

[constrain](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-constrain-static)
Constrains the date within a min and a max date.

[getTime](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-getTime-static)
Returns time with default year, month, and day (Jan 1, 2020).

[copyTimeValues](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-copyTimeValues-static)
Copies hours, minutes, seconds, milliseconds from one date to another.

[combineDateAndTime](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-combineDateAndTime-static)
Combines the hours, minutes, seconds, milliseconds from one date with the year, month, and date of another. The result is returned in a new `Date` instance

[isToday](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-isToday-static)
Determines if a date is today's date.

[isBefore](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-isBefore-static)
Determines if a date precedes another.

[isAfter](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-isAfter-static)
Determines if a date succeeds another.

[isEqual](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-isEqual-static)
Checks if two dates are equal.

[compare](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-compare-static)
Compares two dates using the specified precision.

[clamp](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-clamp-static)
Coerces the passed Date between the passed minimum and maximum values.

[isStartOf](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-isStartOf-static)
Checks if date is the start of specified unit.

[betweenLesser](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-betweenLesser-static)
Checks if this date is `>= start` and `< end`.

[betweenLesserEqual](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-betweenLesserEqual-static)
Checks if this date is `>= start` and `<= end`.

[intersectSpans](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-intersectSpans-static)
Returns `true` if date ranges intersect.

[compareUnits](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-compareUnits-static)
Compare two units. Returns `1` if first param is a greater unit than second param, `-1` if the opposite is true or `0` if they're equal.

[timeSpanContains](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-timeSpanContains-static)
Returns `true` if the first time span completely 'covers' the second time span.

```
DateHelper.timeSpanContains(
    new Date(2010, 1, 2),
    new Date(2010, 1, 5),
    new Date(2010, 1, 3),
    new Date(2010, 1, 4)
) ==> true
DateHelper.timeSpanContains(
  new Date(2010, 1, 2),
  new Date(2010, 1, 5),
  new Date(2010, 1, 3),
  new Date(2010, 1, 6)
) ==> false
```

[get](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-get-static)
Get the specified part of a date.

[daysInYear](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-daysInYear-static)
Get number of days in the current year for the supplied date.

[daysInMonth](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-daysInMonth-static)
Get number of days in the current month for the supplied date.

[hoursInDay](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-hoursInDay-static)
Get number of hours in the current day for the supplied date.

[getNormalizedUnitDuration](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-getNormalizedUnitDuration-static)
Converts unit related to the date to actual amount of milliseconds in it. Takes into account leap years and different duration of months.

[getFirstDateOfMonth](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-getFirstDateOfMonth-static)
Get the first date of the month for the supplied date.

[getLastDateOfMonth](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-getLastDateOfMonth-static)
Get the last date of the month for the supplied date.

[min](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-min-static)
Get the earliest of two dates.

[max](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-max-static)
Get the latest of two dates.

[getNext](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-getNext-static)
Get an incremented date. Incrementation based on specified unit and optional amount.

[isValidDate](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-isValidDate-static)
Checks if date object is valid.

For example:

```
date = new Date('foo')
date instanceof Date // true
date.toString() // Invalid Date
isNaN(date) // true
DateHelper.isValidDate(date) // false

date = new Date()
date instanceof Date // true
date.toString() // Mon Jan 13 2020 18:27:38 GMT+0300 (GMT+03:00)
isNaN(date) // false
DateHelper.isValidDate(date) // true
```

[isDate](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-isDate-static)
Checks if value is a date object. Allows to recognize date object even from another context, like the top frame when used in an iframe.

[getStartOfNextDay](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-getStartOfNextDay-static)
Get the start of the next day.

[getEndOfPreviousDay](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-getEndOfPreviousDay-static)
Get the end of previous day.

[getWeekDescription](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-getWeekDescription-static)
Returns a string describing the specified week. For example, `'39, September 2020'` or `'40, Sep - Oct 2020'`.

[getWeekNumber](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-getWeekNumber-static)
Get week number for the date.

[formatCount](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-formatCount-static)
Turns `(10, 'day')` into `'10 days'` etc.

[getUnitToBaseUnitRatio](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-getUnitToBaseUnitRatio-static)
Get the ratio between two units ( year, month -> 1/12 ).

[getShortNameOfUnit](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-getShortNameOfUnit-static)
Returns a localized abbreviated form of the name of the duration unit. For example in the `EN` locale, for `'qrt'` it will return `'q'`.

[getLocalizedNameOfUnit](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-getLocalizedNameOfUnit-static)
Returns a localized full name of the duration unit.

For example in the `EN` locale, for `'d'` it will return either `'day'` or `'days'`, depending on the `plural` argument

Preserves casing of first letter.

[normalizeUnit](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-normalizeUnit-static)
Normalizes a unit for easier usage in conditionals. For example `'year'`, `'years'`, `'y'` -> `'year'`.

[getDurationInUnit](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-getDurationInUnit-static)
Returns a duration of the timeframe in the given unit.

[doesUnitsAlign](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-doesUnitsAlign-static)
Checks if two date units align.

[round](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-round-static)
Rounds the passed Date value to the nearest `increment` value.

Optionally may round relative to a certain base time point.

For example `DH.round(new Date('2020-01-01T09:35'), '30 min', new Date('2020-01-01T09:15'))` would round to 9:45 because that's the nearest integer number of 30 minute increments from the base.

Note that `base` is ignored when rounding to weeks. The configured [weekStartDay](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper#property-weekStartDay-static) dictates what the base of a week is.

[floor](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-floor-static)
Floor the passed Date value to the nearest `increment` value.

Optionally may floor relative to a certain base time point.

For example `DH.floor(new Date('2020-01-01T09:35'), '30 min', new Date('2020-01-01T09:15'))` would floor to 9:15 because that's the closest lower integer number of 30 minute increments from the base.

Note that `base` is ignored when flooring to weeks. The configured [weekStartDay](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper#property-weekStartDay-static) dictates what the base of a week is.

[ceil](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-ceil-static)
Ceils the passed Date value to the nearest `increment` value.

Optionally may ceil relative to a certain base time point.

For example `DH.ceil(new Date('2020-01-01T09:35'), '30 min', new Date('2020-01-01T09:15'))` would ceil to 9:45 because that's the closest higher integer number of 30 minute increments from the base.

Note that `base` is ignored when ceiling to weeks. Use weekStartDay argument which default to the configured [weekStartDay](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper#property-weekStartDay-static) dictates what the base of a week is

[snap](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-snap-static)
Implementation for round, floor and ceil.

[parseDuration](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-parseDuration-static)
Parses a typed duration value according to locale rules.

The value is taken to be a string consisting of the numeric magnitude and the units:

* The numeric magnitude can be either an integer or a float value. Both `','` and `'.'` are valid decimal separators.
* The units may be a recognised unit abbreviation of this locale or the full local unit name.

For example: `'2d'`, `'2 d'`, `'2 day'`, `'2 days'` will be turned into `{ magnitude : 2, unit : 'day' }` `'2.5d'`, `'2,5 d'`, `'2.5 day'`, `'2,5 days'` will be turned into `{ magnitude : 2.5, unit : 'day' }`

**NOTE:** Doesn't work with complex values like `'2 days, 2 hours'`

[parseTimeUnit](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#function-parseTimeUnit-static)
Parses a typed unit name, for example `'ms'` or `'hr'` or `'yr'` into the canonical form of the unit name which may be passed to [add](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper#function-add-static) or [diff](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper#function-diff-static).

## Typedefs

Typedefs are type definitions for the class

[DurationUnit](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#typedef-DurationUnit)
A string defining a duration unit. Valid values are:

* "millisecond" - Milliseconds
* "second" - Seconds
* "minute" - Minutes
* "hour" - Hours
* "day" - Days
* "week" - Weeks
* "month" - Months
* "quarter" - Quarters
* "year"- Years

[DurationUnitShort](https://bryntum.com/docs/gantt/api/Core/helper/DateHelper#typedef-DurationUnitShort)
A string defining an abbreviated duration unit. Valid values are:

* "ms" - Milliseconds
* "s" - Seconds
* "m" - Minutes
* "h" - Hours
* "d" - Days
* "w" - Weeks
* "M" - Months
* "q" - Quarters
* "y"- Years
