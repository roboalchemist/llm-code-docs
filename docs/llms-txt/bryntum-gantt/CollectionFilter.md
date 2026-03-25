# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/util/CollectionFilter.md

# [CollectionFilter](https://bryntum.com/docs/gantt/api/Core/util/CollectionFilter)

A class which encapsulates a single filter operation which may be applied to any object to decide whether to include or exclude it from a set.

A CollectionFilter generally has at least three main properties:

* `property` - The name of a property in candidate objects from which to extract the value to test
* `value` - The value which this filter uses to test against.
* `operator` - The comparison operator, eg: `'='` or `'>'` etc.

Given these three essential values, further configurations may affect how the filter is applied:

* `caseSensitive` - If configured as `false`, string comparisons are case insensitive.
* `convert` - A function which, when passed the extracted value from the candidate object, returns the value to test.

A filter may also be configured with a single `filterBy` property. This function is just passed the raw candidate object and must return `true` or `false`.

A CollectionFilter may be configured to encapsulate a single filtering function by passing that function as the sole parameter to the constructor:

```
new CollectionFilter(candidate => candidate.title.contains('search string'));
```

Logical Operators
-----------------

A CollectionFilter may instead be configured with a `children` property, which is an array of other CollectionFilters. If this is configured, the `operator` property must be set to either `'and'` or `'or'`. The `children` filters are then combined with the parent filter using the specified operator:

```
// A filter which matches any candidate object which has a duration greater than 10 or a priority of 'high'
// This is equivalent to the SQL expression: `duration > 10 OR priority = 'high'`
new CollectionFilter({
    operator : 'or',
    children : [
        { property : 'duration', operator : '>', value : 10 },
        { property : 'priority', operator : '=', value : 'high' }
    ]
});
```

Or, for nested filters which require parentheses:

```
// A filter which matches any candidates who are in Paris and are either under 18 or over 70
// This is equivalent to the SQL expression: `city = 'Paris' AND (age < 18 OR age > 70)`
new CollectionFilter({
    operator : 'and',
    children : [
        { property : 'city', operator : '=', value : 'Paris },
        {
            operator : 'or',
            children : [
                { property : 'age', operator : '<', value : 18 },
                { property : 'age', operator : '>', value : 70 }
            ]
        }
    ]
});
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[value](https://bryntum.com/docs/gantt/api/Core/util/CollectionFilter#config-value)
The value against which to compare the [property](https://bryntum.com/docs/gantt/api/#Core/util/CollectionFilter#config-property) of candidate objects.

[operator](https://bryntum.com/docs/gantt/api/Core/util/CollectionFilter#config-operator)
The operator to use when comparing a candidate object's [property](https://bryntum.com/docs/gantt/api/#Core/util/CollectionFilter#config-property) with this CollectionFilter's [value](https://bryntum.com/docs/gantt/api/#Core/util/CollectionFilter#config-value).

[filterBy](https://bryntum.com/docs/gantt/api/Core/util/CollectionFilter#config-filterBy)
May be used in place of the [property](https://bryntum.com/docs/gantt/api/#Core/util/CollectionFilter#config-property), [value](https://bryntum.com/docs/gantt/api/#Core/util/CollectionFilter#config-value) and [property](https://bryntum.com/docs/gantt/api/#Core/util/CollectionFilter#config-property) configs. A function which accepts a candidate object and returns `true` or `false`

[convert](https://bryntum.com/docs/gantt/api/Core/util/CollectionFilter#config-convert)
A function which accepts a value extracted from a candidate object using the [property](https://bryntum.com/docs/gantt/api/#Core/util/CollectionFilter#config-property) name, and returns the value which the filter should use to compare against its [value](https://bryntum.com/docs/gantt/api/#Core/util/CollectionFilter#config-value).

[caseSensitive](https://bryntum.com/docs/gantt/api/Core/util/CollectionFilter#config-caseSensitive)
Configure as `false` to have string comparisons case-insensitive.

[id](https://bryntum.com/docs/gantt/api/Core/util/CollectionFilter#config-id)
The `id` of this Filter for when used by a [Collection](https://bryntum.com/docs/gantt/api/#Core/util/Collection) Collection. By default, the `id` is the `[property](https://bryntum.com/docs/gantt/api/#Core/util/CollectionFilter#config-property)-[operator](https://bryntum.com/docs/gantt/api/#Core/util/CollectionFilter#config-operator)` value.

[internal](https://bryntum.com/docs/gantt/api/Core/util/CollectionFilter#config-internal)
Setting the `internal` config on a filter means that it is a fixed part of your store's operation.

[clearFilters](https://bryntum.com/docs/gantt/api/#Core/data/Store#function-clearFilters) does not remove `internal` filters. If you add an `internal` filter, you must explicitly remove it if it is no longer required.

Grid features which offer column-based filtering do _not_ ingest existing store filters on their data field if the filter is `internal`

[disabled](https://bryntum.com/docs/gantt/api/Core/util/CollectionFilter#config-disabled)
When `true`, the filter will not be applied.

[property](https://bryntum.com/docs/gantt/api/Core/util/CollectionFilter#config-property)
The name of a property of candidate objects which yields the value to compare against this CollectionFilter's [value](https://bryntum.com/docs/gantt/api/#Core/util/CollectionFilter#config-value).

[children](https://bryntum.com/docs/gantt/api/Core/util/CollectionFilter#config-children)
An array of child CollectionFilters which are combined with this filter using the [operator](https://bryntum.com/docs/gantt/api/#Core/util/CollectionFilter#config-operator) operator `and` or `or`.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[property](https://bryntum.com/docs/gantt/api/Core/util/CollectionFilter#property-property)
The name of a property of candidate objects which yields the value to compare against this CollectionFilter's [value](https://bryntum.com/docs/gantt/api/#Core/util/CollectionFilter#config-value).

[id](https://bryntum.com/docs/gantt/api/Core/util/CollectionFilter#property-id)
When in a Collection (A Collection holds its Filters in a Collection), we need an id.

[filterBy](https://bryntum.com/docs/gantt/api/Core/util/CollectionFilter#property-filterBy)
May be used in place of the [property](https://bryntum.com/docs/gantt/api/#Core/util/CollectionFilter#config-property), [value](https://bryntum.com/docs/gantt/api/#Core/util/CollectionFilter#config-value) and [property](https://bryntum.com/docs/gantt/api/#Core/util/CollectionFilter#config-property) configs. A function which accepts a candidate object and returns `true` or `false`

[value](https://bryntum.com/docs/gantt/api/Core/util/CollectionFilter#property-value)
The value against which to compare the [property](https://bryntum.com/docs/gantt/api/#Core/util/CollectionFilter#config-property) of candidate objects.

[operator](https://bryntum.com/docs/gantt/api/Core/util/CollectionFilter#property-operator)
The operator to use when comparing a candidate object's [property](https://bryntum.com/docs/gantt/api/#Core/util/CollectionFilter#config-property) with this CollectionFilter's [value](https://bryntum.com/docs/gantt/api/#Core/util/CollectionFilter#config-value).

## Functions

Functions are methods available for calling on the class

[generateFiltersFunction](https://bryntum.com/docs/gantt/api/Core/util/CollectionFilter#function-generateFiltersFunction-static)
Generates a filter function based on provided collection filters.

## Typedefs

Typedefs are type definitions for the class

[CollectionCompareOperator](https://bryntum.com/docs/gantt/api/Core/util/CollectionFilter#typedef-CollectionCompareOperator)
The operator to use when comparing a collection object.

### Valid Values

Following are the operators supported by CollectionFilter. **Text** is the label shown when this operator is displayed in a [FieldFilterPicker](https://bryntum.com/docs/gantt/api/#Core/widget/FieldFilterPicker). To customize the list of operators displayed in a [FieldFilterPicker](https://bryntum.com/docs/gantt/api/#Core/widget/FieldFilterPicker), see [operators](https://bryntum.com/docs/gantt/api/#Core/widget/FieldFilterPicker#config-operators).

Operator

Text

Description

`=`

equals

Match records having values exactly equal to a given value

`!=`

does not equal

Match records having values not equal to a given value

`>`

greater than

Match records having values greater than a given value

`>=`

greater or equals

Match records having values greater than or equal to a given value

`<`

less than

Match records having values less than a given value

`<=`

less or equals

Match records having values less than or equal to a given value

`*`

contains

Match records where a value includes a specified substring

`startsWith`

starts with

Match records starting with a specific string

`endsWith`

ends with

Match records ending with a specific string

`isIncludedIn`

one of

Match records where a value is included in a given set of values

`isNotIncludedIn`

not one of

Match records where a value is not included in a given set of values

`includes`

contains

Match records where a value includes a specified substring

`doesNotInclude`

does not contain

Match records where a value does not include a specified substring

`empty`

empty

Match records where a field is empty

`notEmpty`

not empty

Match records where a field is not empty

`between`

between

Match records where a value falls within a specified range

`notBetween`

not between

Match records where a value falls outside a specified range

`isToday`

today

Match records where a date is today's date

`isTomorrow`

tomorrow

Match records where a date is tomorrow's date

`isYesterday`

yesterday

Match records where a date is yesterday's date

`isThisWeek`

this week

Match records where a date is within the current week

`isLastWeek`

last week

Match records where a date is within the previous week

`isNextWeek`

next week

Match records where a date is within the next week

`isThisMonth`

this month

Match records where a date is within the current month

`isLastMonth`

last month

Match records where a date is within the previous month

`isNextMonth`

next month

Match records where a date is within the next month

`isThisYear`

this year

Match records where a date is within the current year

`isLastYear`

last year

Match records where a date is within the previous year

`isNextYear`

next year

Match records where a date is within the next year

`isYearToDate`

year to date

Match records where a date is within the current year to date

`isTrue`

true

Match records where a boolean value is true

`isFalse`

false

Match records where a boolean value is false

`or`

or

Combine multiple [children](https://bryntum.com/docs/gantt/api/#Core/util/CollectionFilter#config-children) filters using logical OR

`and`

and

Combine multiple [children](https://bryntum.com/docs/gantt/api/#Core/util/CollectionFilter#config-children) filters using logical AND
