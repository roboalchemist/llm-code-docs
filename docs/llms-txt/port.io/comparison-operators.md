# Source: https://docs.port.io/search-and-query/operators/comparison-operators.md

# Comparison operators

This page details the available comparison operators when writing [rules](/search-and-query/structure-and-syntax.md#rules) as part of the search route.

### = (Equal)[â](#-equal "Direct link to = (Equal)")

The `=` operator checks exact matches of the specified value:

```
{
  "operator": "=",
  "property": "myProperty",
  "value": "myExactValue"
}
```

This operator can also be used to check the value of `boolean` properties:

```
{
  "operator": "=",
  "property": "myBooleanProperty",
  "value": true
}
```

For datetime properties, the `=` operator only supports ISO8601 format strings:

```
{
  "operator": "=",
  "property": "$createdAt",
  "value": "2022-07-26T16:38:06.839Z"
}
```

DateTime format support

The `=` operator only supports ISO8601 format strings for datetime values.<br /><!-- -->To use preset date ranges (like "lastWeek", "today", etc.), use the [between](#between) or [notBetween](#notbetween) operators instead.

### != (Not Equal)[â](#-not-equal "Direct link to != (Not Equal)")

The `!=` operator checks exact matches of the specified value and returns all results that fail to satisfy the check:

```
{
  "operator": "!=",
  "property": "myProperty",
  "value": "myExactValue"
}
```

This operator can also be used to check the value of `boolean` properties:

```
{
  "operator": "!=",
  "property": "myBooleanProperty",
  "value": false
}
```

### > (Greater Than)[â](#-greater-than "Direct link to > (Greater Than)")

The `>` operator checks values larger than the specified value:

```
{
  "operator": ">",
  "property": "myNumericProperty",
  "value": 7
}
```

### >= (Greater Than or Equal)[â](#-greater-than-or-equal "Direct link to >= (Greater Than or Equal)")

The `>=` operator checks values larger than or equal to the specified value:

```
{
  "operator": ">=",
  "property": "myNumericProperty",
  "value": 7
}
```

### < (Less Than)[â](#-less-than "Direct link to < (Less Than)")

The `<` operator checks values less than the specified value:

```
{
  "operator": "<",
  "property": "myNumericProperty",
  "value": 7
}
```

### <= (Less Than or Equal)[â](#-less-than-or-equal "Direct link to <= (Less Than or Equal)")

The `<=` operator checks values less than or equal to the specified value:

```
{
  "operator": "<=",
  "property": "myNumericProperty",
  "value": 7
}
```

### isEmpty[â](#isempty "Direct link to isEmpty")

The `isEmpty` operator checks if the value of the specified property is `null`:

```
{
  "operator": "isEmpty",
  "property": "myProperty"
}
```

### isNotEmpty[â](#isnotempty "Direct link to isNotEmpty")

The `isNotEmpty` operator checks if the value of the specified property is not `null`:

```
{
  "operator": "isNotEmpty",
  "property": "myProperty"
}
```

### propertySchema[â](#propertyschema "Direct link to propertySchema")

The `propertySchema` filter can be used with any standard operator. It allows you to filter entities based on a properties matching a specific type (for example, find all string properties with a given value):

* String
* URL

```
{
  "propertySchema": {
    "type": "string"
  },
  "operator": "=",
  "value": "My value"
}
```

```
{
  "propertySchema": {
    "type": "string",
    "format": "url"
  },
  "operator": "=",
  "value": "https://example.com"
}
```

tip

* The `propertySchema` can be used with any Port [property](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/.md#supported-properties);
* The `propertySchema` replaces the `property` filter when performing property schema search.

### between[â](#between "Direct link to between")

The `between` operator checks datetime values and returns entities whose relevant datetime property matches the given range:

```
{
  "operator": "between",
  "property": "$createdAt",
  "value": {
    "preset": "lastWeek"
  }
}
```

**Available Presets:**

* `last3Years` - In the past 3 years
* `last2Years` - In the past 2 years
* `last12Months` - In the past 365 days
* `last6Months` - In the past 180 days
* `last3Months` - In the past 90 days
* `lastMonth` - In the past 30 days
* `last2Weeks` - In the past 2 weeks
* `lastWeek` - In the past week
* `lastDay` - In the past day
* `today` - Today
* `tomorrow` - Tomorrow
* `yesterday` - Yesterday
* `nextDay` - In the next day
* `nextWeek` - In the next week
* `next2Weeks` - In the next 2 weeks
* `nextMonth` - In the next 30 days
* `next3Months` - In the next 90 days
* `next6Months` - In the next 180 days
* `next12Months` - In the next 365 days

When using the catalog page UI, these presets are available via the `is` operator when filtering datetime properties.

Future date presets availability

The future date presets (`nextDay`, `nextWeek`, `next2Weeks`, `nextMonth`, `next3Months`, `next6Months`, `next12Months`) are only available in the [catalog page](/customize-pages-dashboards-and-plugins/page/catalog-page.md) filters and initial filters. They are not supported in table widgets or other locations.

The `between` operator also supports standard date ranges:

```
{
  "combinator": "and",
  "rules": [
    {
      "operator": "between",
      "property": "$createdAt",
      "value": {
        "from": "2022-07-26T16:38:06.839Z",
        "to": "2022-07-29T17:00:28.006Z"
      }
    }
  ]
}
```

### notBetween[â](#notbetween "Direct link to notBetween")

The `notBetween` operator checks datetime values and returns entities whose relevant datetime property does not match the given range:

```
{
  "operator": "notBetween",
  "property": "$createdAt",
  "value": {
    "preset": "lastWeek"
  }
}
```

### contains[â](#contains "Direct link to contains")

The `contains` operator checks if the specified value exists within a **string** property:

```
{
  "property": "myStringProperty",
  "operator": "contains",
  "value": "mySubString"
}
```

### doesNotContains[â](#doesnotcontains "Direct link to doesNotContains")

The `doesNotContains` operator checks if the specified value **does not** exists in the specified property:

```
{
  "operator": "doesNotContains",
  "property": "myStringProperty",
  "value": "otherValue"
}
```

### containsAny[â](#containsany "Direct link to containsAny")

The `containsAny` operator checks if **any** of the specified strings exist in the target **array**:

```
{
  "operator": "containsAny",
  "property": "myArrayProperty",
  "value": ["Value1", "Value2", ...]
}
```

### beginsWith[â](#beginswith "Direct link to beginsWith")

The `beginsWith` operator checks if the specified property starts with the specified value:

```
{
  "operator": "beginsWith",
  "property": "myStringProperty",
  "value": "myString"
}
```

### doesNotBeginsWith[â](#doesnotbeginswith "Direct link to doesNotBeginsWith")

The `doesNotBeginsWith` operator checks if the specified property **does not** start with the specified value:

```
{
  "operator": "doesNotBeginsWith",
  "property": "myStringProperty",
  "value": "otherValue"
}
```

### endsWith[â](#endswith "Direct link to endsWith")

The `endsWith` operator checks if the specified property ends with the specified value:

```
{
  "operator": "endsWith",
  "property": "myStringProperty",
  "value": "myString"
}
```

### doesNotEndsWith[â](#doesnotendswith "Direct link to doesNotEndsWith")

The `doesNotEndsWith` operator checks if the specified property **does not** end with the specified value:

```
{
  "operator": "doesNotEndsWith",
  "property": "myStringProperty",
  "value": "otherValue"
}
```

### in[â](#in "Direct link to in")

The `in` operator checks if a `string` property is equal to one or more specified `string` values:

* Standard
* Dynamic Filter

```
{
  "property": "myStringProperty",
  "operator": "in",
  "value": ["Value1", "Value2"]
}
```

In order to filter entities that **belong to one or more of your teams** you can use the special `My Teams` filter:

```
{
  "property": "$team",
  "operator": "in",
  "value": ["My Teams"]
}
```

You can also use the `My Teams` filter in the UI:

![My Teams Filter](/assets/images/MyTeamsFilter-7b6d29f57461891c5ee5ebd78391d19b.png)

### notIn[â](#notin "Direct link to notIn")

The `notIn` operator checks if a `string` property is **not equal** to all of the specified `string` values:

```
{
  "property": "myStringProperty",
  "operator": "notIn",
  "value": ["Value1", "Value2"]
}
```
