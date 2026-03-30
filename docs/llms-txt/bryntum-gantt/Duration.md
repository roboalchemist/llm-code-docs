# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/data/Duration.md

# [Duration](https://bryntum.com/docs/gantt/api/Core/data/Duration)

Class which represents a duration object. A duration consists of a `magnitude` and a `unit`.

```
{
   unit      : String,
   magnitude : Number
}
```

Valid values are:

* "millisecond" - Milliseconds
* "second" - Seconds
* "minute" - Minutes
* "hour" - Hours
* "day" - Days
* "week" - Weeks
* "month" - Months
* "quarter" - Quarters
* "year"- Years

## Properties

Properties are getters/setters or publicly accessible variables on this class

[magnitude](https://bryntum.com/docs/gantt/api/Core/data/Duration#property-magnitude)
Get/Set numeric magnitude `value`.

[unit](https://bryntum.com/docs/gantt/api/Core/data/Duration#property-unit)
Get/set duration unit to use with the current magnitude value. Valid values are:

* "millisecond" - Milliseconds
* "second" - Seconds
* "minute" - Minutes
* "hour" - Hours
* "day" - Days
* "week" - Weeks
* "month" - Months
* "quarter" - Quarters
* "year"- Years

[milliseconds](https://bryntum.com/docs/gantt/api/Core/data/Duration#property-milliseconds)
The `milliseconds` property is a read only property which returns the number of milliseconds in this Duration

## Functions

Functions are methods available for calling on the class

[constructor](https://bryntum.com/docs/gantt/api/Core/data/Duration#function-constructor)
Duration constructor.

[from](https://bryntum.com/docs/gantt/api/Core/data/Duration#function-from-static)
Converts the passed parameter converted to a [Duration](https://bryntum.com/docs/gantt/api/#Core/data/Duration) object if possible, or `null` if `null` or `undefined` passed.

[negate](https://bryntum.com/docs/gantt/api/Core/data/Duration#function-negate)
Returns a negated copy of this Duration.

[isEqual](https://bryntum.com/docs/gantt/api/Core/data/Duration#function-isEqual)
Returns truthy value if this Duration equals the passed value.

[toString](https://bryntum.com/docs/gantt/api/Core/data/Duration#function-toString)
Returns a readable localized representation of this Duration (e.g. 5 days).

[add](https://bryntum.com/docs/gantt/api/Core/data/Duration#function-add)
Returns a new Duration which is the sum of this Duration and the passed Duration. The returned Duration unit is the same as this Duration's unit.

[diff](https://bryntum.com/docs/gantt/api/Core/data/Duration#function-diff)
Returns a new Duration which is the difference between this Duration and the passed Duration. The returned Duration unit is the same as this Duration's unit.

## Typedefs

Typedefs are type definitions for the class

[DurationConfig](https://bryntum.com/docs/gantt/api/Core/data/Duration#typedef-DurationConfig)
Object describing a duration.
