# Source: https://docs.rootly.com/liquid/filters.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Available Liquid Filters

> Comprehensive reference of built-in and custom Liquid filters for data manipulation, formatting, and string processing in Rootly workflows.

## Rootly built-in

### find

* `find: arg1, 'arg2'`
  * `arg1`. String
  * `arg2`. String

```js JS theme={null}
// Pretending object is the following object [{"id": "apple"}, {"id": "banana"}]
{{ object | find: 'id', 'banana' }}
// Output
// {"id": "banana"}
```

### get

* `get: 'arg'`
  * `arg`. String

```js JS theme={null}
// Pretending object is the following object {"id": "id", "incident": {"title": "Something is on fire!"}}
{{ object | get: 'incident.title' }}
// Output
// Something is on fire!
```

### smart\_date

* `smart_date: 'arg'`
  * `arg`. String
* This is using [https://github.com/mojombo/chronic](https://github.com/mojombo/chronic) under the hood.

```js JS theme={null}


{{ 'now' | smart_date: 'tomorrow' }}
// Output
// 2023-06-29 12:00:00 -0700
```

### date\_add

* `date_add: amount, 'date_part'`
  * `amount`. Integer (positive to add, negative to subtract)
  * `date_part`. String - one of: year, month, day, hour, minute, second, millisecond (plurals supported)

Adds a specified amount of time to a date. Works with 'now', 'today', ISO date strings, Time, and Date objects.

```js JS theme={null}
{{ 'now' | date_add: 1, 'day' | date: '%Y-%m-%d' }}
// Output
// 2023-06-30 (tomorrow)

{{ '2023-06-29T10:30:00Z' | date_add: 2, 'hours' | date: '%Y-%m-%d %H:%M' }}
// Output  
// 2023-06-29 12:30

{{ incident.target_resolve_date | date_add: -30, 'minutes' }}
// Output
// 30 minutes before the target resolve date
```

### date\_minus

* `date_minus: amount, 'date_part'`
  * `amount`. Integer (positive to subtract, negative to add)
  * `date_part`. String - one of: year, month, day, hour, minute, second, millisecond (plurals supported)

Subtracts a specified amount of time from a date. Works with 'now', 'today', ISO date strings, Time, and Date objects.

```js JS theme={null}
{{ 'now' | date_minus: 7, 'days' | date: '%Y-%m-%d' }}
// Output
// 2023-06-22 (a week ago)

{{ incident.created_at | date_minus: 1, 'hour' | date: '%Y-%m-%d %H:%M' }}
// Output
// 1 hour before the incident was created

{{ 'today' | date_minus: 6, 'months' }}
// Output
// 6 months ago
```

### slice

* `slice: '\*arg'`
  * `arg`. String
  * ... As many args as you need

```js JS theme={null}


// Pretending object is the following object {"key": "hello", "value": "world", "foo": "bar"}

{{ object | slice: 'key' }}

// Output
// {"key": "hello"}

{{ object | slice: 'key', 'foo' }}

// Output
// {"key": "hello", "foo": "bar"}
```

### flatten

* flatten

```js JS theme={null}

// Pretending object is the following object \["1", "2", \["3"\]\]
{{ object | flatten }}
// Output
// \["1","2","3"\]
```

### to\_values

* `to_values: 'key'`
  * `key` is optional

```js JS theme={null}

// Pretending object is the following object {"key": "hello", "value": "world"}
{{ object | to_values }}

// Output
// \[{"value":"world"}\]

{{ object | to_values: 'key' }}

// Output
// \[{"value":"hello"}\]
```

### to\_json

* `to_json`

```js JS theme={null}
// Pretending object is the following object [{"key": "hello", "value": "world"}]
{{ object | to_json }}
// Output
// [{"key":"hello","value":"world"}]
```

### to\_iso8601

* `to_iso8601`

```js JS theme={null}
// Pretending object is the following datetime
{{ object | to_iso8601 }}
// Output
// 2023-06-29T12:00:00-07:00
```

### distance\_of\_time\_in\_words

* `distance_of_time_in_words: 'arg', 'precise'`
  * `arg`. String (optional)
  * `precise`. String (optional)

```js JS theme={null}
{{ 3720 | distance_of_time_in_words }}
// Output
// about 1 hour
{{ 3720 | distance_of_time_in_words: 0, 'precise' }}
// Output
// 1 hour and 2 minutes
{{ 'May 1, 2020' | distance_of_time_in_words: 'May 31, 2020' }}
// Output
// about 1 month
{{ 'May 1, 2020' | distance_of_time_in_words: 'May 31, 2020', 'precise' }}
// Output
// 4 weeks and 2 days
```

### distance\_of\_time\_in\_words\_to\_now

* `distance_of_time_in_words_to_now: 'precise'`
  * `precise`. String (optional)

```js JS theme={null}
{{ 'May 1, 2020' | distance_of_time_in_words_to_now }}
// Output
// over 2 years
{{ 'May 1, 2020' | distance_of_time_in_words_to_now: 'precise' }}
// Output
// 2 years and 7 months
```

### in\_time\_zone

* ` in_time_zone: 'time_zone'`
  * `time_zone`. Any timezone listed in [Timezones](/liquid/timezones)﻿﻿

```js JS theme={null}

{{ now | in_time_zone: 'Europe/London' | date: '%Y-%m-%d %H:%M %Z' }}
```

See [Timezones](/liquid/timezones)﻿ for available values

### to\_utc

* `to_utc`

Converts a date to UTC timezone. Works with 'now', 'today', ISO date strings, Time, and Date objects.

```js JS theme={null}
{{ incident.started_at | to_utc | date: '%Y-%m-%d %H:%M:%S' }}
// Output
// 2023-06-29 15:30:00 (converted to UTC)

{{ 'now' | to_utc | date: '%Y-%m-%d %H:%M:%S UTC' }}
// Output  
// 2023-06-29 19:45:23 UTC

{{ '2023-06-29T10:30:00-05:00' | to_utc | date: '%Y-%m-%d %H:%M:%S' }}
// Output
// 2023-06-29 15:30:00
```

Useful for synchronizing incident timestamps with timeline values, ensuring all dates display in UTC regardless of user timezone.

### to\_table

* `to_table: 'table_type', 'title', 'time_zone', 'format'`
  * `table_type` is either events or action\_items
  * `time_zone`. Any timezone listed in [Timezones](/liquid/timezones)﻿﻿
  * `format` can be ascii , markdown , html, atlassian\_markdown

```js JS theme={null}

{{ incident.events | to_table: 'events', 'Hello world', 'America/Los_Angeles', 'markdown' }}
```

### regex\_replace

Global replace

* `regex_replace: 'regex', 'replacement'`
  * `regexp` a ruby regular expression
  * `replacement` a ruby regular expression

```js JS theme={null}
{{ 'foo bar 123 456' | regex_replace: '\d+', 'baz' }}
// Output
// foo bar baz baz
```

### regex\_replace\_first

First match replace

* `regex_replace_first: 'regex', 'replacement'`
  * `regexp` a ruby regular expression
  * `replacement` a ruby regular expression

```js JS theme={null}
{{ 'foo bar 123 456' | regex_replace: '\d+', 'baz' }}
// Output
// foo bar baz 456
```

### regex\_remove

Global match remove

* `regex_remove: 'regex'`
  * `regexp` a ruby regular expression

```js JS theme={null}
{{ 'foo bar 123 456' | regex_remove: '\d+' }}
// Output
// foo bar
```

### regex\_remove\_first

First match remove

* `regex_remove_first: 'regex'`
  * `regexp` a ruby regular expression

```js JS theme={null}
{{ 'foo bar 123 456' | regex_remove_first: '\d+' }}
// Output
// foo bar  456
```

### regex\_match

Find first match and return array with full match and capture groups

* `regex_match: 'regex', 'flags'`
  * `regex` a ruby regular expression
  * `flags` optional string with regex flags: 'i' (case insensitive), 'm' (multiline), 'x' (extended)

```js JS theme={null}
{{ 'Key1: value1' | regex_match: 'Key(\d+): (.+)' | first }}
// Output
// Key1: value1

{{ 'Key1: value1' | regex_match: 'Key(\d+): (.+)' | last }}
// Output  
// value1

{{ 'user@example.com' | regex_match: '(\w+)@(\w+\.\w+)' | size }}
// Output
// 3 (full match + 2 capture groups)
```

```js JS theme={null}
// Case insensitive matching
{{ 'HELLO world' | regex_match: 'hello', 'i' | first }}
// Output
// HELLO

// Multiline matching  
{{ "Line 1\nLine 2\nDone" | regex_match: 'line.*done', 'im' | first }}
// Output
// Line 1
// Line 2  
// Done
```

Perfect for extracting data from email alert payloads:

```js JS theme={null}
{{ alert.body | regex_match: 'Severity: (.+)' | last }}
// Extract severity level from alert body

{{ alert.body | regex_match: 'Host: ([\w\.-]+)' | last }}  
// Extract hostname from alert
```

### regex\_match\_all

Find all matches and return array of results

* `regex_match_all: 'regex', 'flags'`
  * `regex` a ruby regular expression
  * `flags` optional string with regex flags: 'i' (case insensitive), 'm' (multiline), 'x' (extended)

```js JS theme={null}
{{ 'foo 123 bar 456 baz 789' | regex_match_all: '\d+' | size }}
// Output
// 3

{{ 'foo 123 bar 456 baz 789' | regex_match_all: '\d+' | first }}
// Output
// 123

{{ 'foo 123 bar 456 baz 789' | regex_match_all: '\d+' | last }}
// Output  
// 789
```

```js JS theme={null}
// Extract all email addresses
{{ 'Contact support@example.com or admin@test.org' | regex_match_all: '[\w\.-]+@[\w\.-]+\.\w+' | size }}
// Output
// 2

// Case insensitive matching
{{ 'ERROR: failed, error: timeout' | regex_match_all: 'error: (\w+)', 'i' | first }}
// Output
// failed
```

Ideal for parsing multiple values from alert payloads:

```js JS theme={null}
// Extract all IP addresses from alert body
{{ alert.body | regex_match_all: '\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b' }}

// Extract all key-value pairs
{{ alert.body | regex_match_all: 'Key\d+: ([^\n]+)' }}
```

### dasherize

* `dasherize`

```js JS theme={null}
{{ 'hello_world' | dasherize }}
// Output
// hello-world
```

### parameterize

* `parameterize`
  * `separator` (default to '-')

```js JS theme={null}
{{ 'Hello World' | parameterize }}
// Output
// hello-world
{{ 'Hello World' | parameterize: '_' }}
// Output
// hello_world
```

### camelize

* `camelize`

```js JS theme={null}
{{ 'hello world' | camelize }}
// Output
// Hello world
```

### titleize

* `titleize`

```js JS theme={null}

{{ 'hello world' | titleize }}
// Output
// Hello World
```

### singularize

* `singularize`

```js JS theme={null}
{{ 'cars' | singularize }}
// Output
// car
```

### pluralize

* `pluralize`

```js JS theme={null}
{{ 'car' | pluralize }}
// Output
// cars
```

### humanize

* `humanize`

```js JS theme={null}
{{ '0' | humanize }}
// Output
// No
{{ '1' | humanize }}
// Output
// Yes
{{ 'incident_management' | humanize }}
// Output
// Incident Management
```

### shuffle

* `shuffle`

```js JS theme={null}
{{ '123456789' | shuffle }}
// Output
// 973426581
```

## Liquid built-in

* [https://shopify.github.io/liquid/](https://shopify.github.io/liquid/)

### html\_to\_markdown

* `html_to_markdown`

Converts HTML content to Markdown format. Handles most common HTML elements including headings, paragraphs, lists, links, code blocks, and tables.

```js JS theme={null}
{{ '<h1>Title</h1><p>This is <strong>bold</strong> text.</p>' | html_to_markdown }}
// Output
// # Title
// 
// This is **bold** text.
```

```js JS theme={null}
{{ '<ul><li>Item 1</li><li>Item 2</li></ul>' | html_to_markdown }}
// Output
// - Item 1
// - Item 2
```

Returns empty string for nil or empty input. Preserves original HTML on conversion errors.

### shortener

* `shortener`

```js JS theme={null}
{{ 'https://rootly.com/account/incidents/123456' | shortener }}
// Output
// https://root.ly/1234
```


Built with [Mintlify](https://mintlify.com).