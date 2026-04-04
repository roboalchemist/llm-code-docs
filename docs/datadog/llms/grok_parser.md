# Source: https://docs.datadoghq.com/events/pipelines_and_processors/grok_parser.md

---
title: Grok Parser
description: >-
  Create custom grok rules to parse the full message or specific attributes of
  raw events into structured data
breadcrumbs: Docs > Event Management > Pipelines and Processors > Grok Parser
---

# Grok Parser

## Overview{% #overview %}

Create custom grok rules to parse the full message or a specific attribute of your raw event. As a best practice, it is recommended to use at most 10 parsing rules within a grok processor.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/events/grok-parser.a21124396f77ebb6320cdd3864c2ed9c.png?auto=format"
   alt="Parsing example 1" /%}

Click **Parse My Events** to kickstart a set of three parsing rules for the events flowing through the underlying pipeline. Refine attribute naming from there, and add new rules for other type of events if needed. This feature requires that the corresponding events are being indexed, and actually flowing inâyou can temporarily deactivate or sample down exclusion filters to make this work for you.

Select a sample by clicking on it to trigger its evaluation against the parsing rule and display the result at the bottom of the screen.

Up to five samples can be saved with the processor, and each sample can be up to 5000 characters in length. All samples show a status (match or no match), which highlights if one of the parsing rules of the grok parser matches the sample.

### Grok Syntax{% #grok-syntax %}

The Grok Parser extracts attributes from semi-structured text messages. Grok comes with reusable patterns to parse integers, IP addresses, hostnames, and more. These values must be sent into the grok parser as strings.

You can write parsing rules with the `%{MATCHER:EXTRACT:FILTER}` syntax:

- **Matcher**: A rule (possibly a reference to another token rule) that describes what to expect (number, word, notSpace, etc.).

- **Extract** (optional): An identifier representing the capture destination for the piece of text matched by the *Matcher*.

- **Filter** (optional): A post-processor of the match to transform it.

Example for a classic unstructured event:

```text
john connected on 11/08/2017
```

With the following parsing rule:

```text
MyParsingRule %{word:user} connected on %{date("MM/dd/yyyy"):date}
```

After processing, the following structured event is generated:

{% image
   source="https://datadog-docs.imgix.net/images/logs/processing/processors/_parser.c3032f266fcde50c88b1078d6e8a786a.png?auto=format"
   alt="Parsing example 1" /%}

**Note**:

- If you have multiple parsing rules in a single Grok parser:
  - Only one can match any given event. The first one that matches, from top to bottom, is the one that does the parsing.
  - Each rule can reference parsing rules defined above itself in the list.
- You must have unique rule names within the same Grok parser.
- The rule name must contain only: alphanumeric characters, `_`, and `.`. It must start with an alphanumeric character.
- Properties with null or empty values are not displayed.
- The regex matcher applies an implicit `^`, to match the start of a string, and `$`, to match the end of a string.
- Certain events can produce large gaps of whitespace. Use `\n` and `\s+` to account for newlines and whitespace.

### Matcher and filter{% #matcher-and-filter %}

Here is a list of all the matchers and filters natively implemented by Datadog:

{% tab title="Matchers" %}

{% dl %}

{% dt %}
`date("pattern"[, "timezoneId"[, "localeId"]])`
{% /dt %}

{% dd %}
Matches a date with the specified pattern and parses to produce a Unix timestamp. See the date Matcher examples.
{% /dd %}

{% dt %}
`regex("pattern")`
{% /dt %}

{% dd %}
Matches a regex. Check the regex Matcher examples.
{% /dd %}

{% dt %}
`notSpace`
{% /dt %}

{% dd %}
Matches any string until the next space.
{% /dd %}

{% dt %}
`boolean("truePattern", "falsePattern")`
{% /dt %}

{% dd %}
Matches and parses a Boolean, optionally defining the true and false patterns (defaults to `true` and `false`, ignoring case).
{% /dd %}

{% dt %}
`numberStr`
{% /dt %}

{% dd %}
Matches a decimal floating point number and parses it as a string.
{% /dd %}

{% dt %}
`number`
{% /dt %}

{% dd %}
Matches a decimal floating point number and parses it as a double precision number.
{% /dd %}

{% dt %}
`numberExtStr`
{% /dt %}

{% dd %}
Matches a floating point number (with scientific notation support) and parses it as a string.
{% /dd %}

{% dt %}
`numberExt`
{% /dt %}

{% dd %}
Matches a floating point number (with scientific notation support) and parses it as a double precision number.
{% /dd %}

{% dt %}
`integerStr`
{% /dt %}

{% dd %}
Matches an integer number and parses it as a string.
{% /dd %}

{% dt %}
`integer`
{% /dt %}

{% dd %}
Matches an integer number and parses it as an integer number.
{% /dd %}

{% dt %}
`integerExtStr`
{% /dt %}

{% dd %}
Matches an integer number (with scientific notation support) and parses it as a string.
{% /dd %}

{% dt %}
`integerExt`
{% /dt %}

{% dd %}
Matches an integer number (with scientific notation support) and parses it as an integer number.
{% /dd %}

{% dt %}
`word`
{% /dt %}

{% dd %}
Matches characters from a-z, A-Z, 0-9, including the _ (underscore) character.
{% /dd %}

{% dt %}
`doubleQuotedString`
{% /dt %}

{% dd %}
Matches a double-quoted string.
{% /dd %}

{% dt %}
`singleQuotedString`
{% /dt %}

{% dd %}
Matches a single-quoted string.
{% /dd %}

{% dt %}
`quotedString`
{% /dt %}

{% dd %}
Matches a double-quoted or single-quoted string.
{% /dd %}

{% dt %}
`uuid`
{% /dt %}

{% dd %}
Matches a UUID.
{% /dd %}

{% dt %}
`mac`
{% /dt %}

{% dd %}
Matches a MAC address.
{% /dd %}

{% dt %}
`ipv4`
{% /dt %}

{% dd %}
Matches an IPV4.
{% /dd %}

{% dt %}
`ipv6`
{% /dt %}

{% dd %}
Matches an IPV6.
{% /dd %}

{% dt %}
`ip`
{% /dt %}

{% dd %}
Matches an IP (v4 or v6).
{% /dd %}

{% dt %}
`hostname`
{% /dt %}

{% dd %}
Matches a hostname.
{% /dd %}

{% dt %}
`ipOrHost`
{% /dt %}

{% dd %}
Matches a hostname or IP.
{% /dd %}

{% dt %}
`port`
{% /dt %}

{% dd %}
Matches a port number.
{% /dd %}

{% dt %}
`data`
{% /dt %}

{% dd %}
Matches any string including spaces and newlines. Equivalent to `.*` in regex. Use when none of above patterns is appropriate.
{% /dd %}

{% /dl %}

{% /tab %}

{% tab title="Filters" %}

{% dl %}

{% dt %}
`number`
{% /dt %}

{% dd %}
Parses a match as double precision number.
{% /dd %}

{% dt %}
`integer`
{% /dt %}

{% dd %}
Parses a match as an integer number.
{% /dd %}

{% dt %}
`boolean`
{% /dt %}

{% dd %}
Parses 'true' and 'false' strings as booleans ignoring case.
{% /dd %}

{% dt %}
`nullIf("value")`
{% /dt %}

{% dd %}
Returns null if the match is equal to the provided value.
{% /dd %}

{% dt %}
`json`
{% /dt %}

{% dd %}
Parses properly formatted JSON.
{% /dd %}

{% dt %}
`rubyhash`
{% /dt %}

{% dd %}
Parses a properly formatted Ruby hash such as `{name => "John", "job" => {"company" => "Big Company", "title" => "CTO"}}`
{% /dd %}

{% dt %}
`useragent([decodeuricomponent:true/false])`
{% /dt %}

{% dd %}
Parses a user-agent and returns a JSON object that contains the device, OS, and the browser represented by the Agent. [Check the User Agent processor][1].
{% /dd %}

{% dt %}
`querystring`
{% /dt %}

{% dd %}
Extracts all the key-value pairs in a matching URL query string (for example, `?productId=superproduct&promotionCode=superpromo`).
{% /dd %}

{% dt %}
`decodeuricomponent`
{% /dt %}

{% dd %}
Decodes URI components. For instance, it transforms `%2Fservice%2Ftest` into `/service/test`.
{% /dd %}

{% dt %}
`lowercase`
{% /dt %}

{% dd %}
Returns the lower-cased string.
{% /dd %}

{% dt %}
`uppercase`
{% /dt %}

{% dd %}
Returns the upper-cased string.
{% /dd %}

{% dt %}
`keyvalue([separatorStr[, characterAllowList[, quotingStr[, delimiter]]]])`
{% /dt %}

{% dd %}
Extracts the key value pattern and returns a JSON object. See the key-value filter examples.
{% /dd %}

{% dt %}
`xml`
{% /dt %}

{% dd %}
Parses properly formatted XML. See the XML filter examples.
{% /dd %}

{% dt %}
`csv(headers[, separator[, quotingcharacter]])`
{% /dt %}

{% dd %}
Parses properly formatted CSV or TSV lines. See the CSV filter examples.
{% /dd %}

{% dt %}
`scale(factor)`
{% /dt %}

{% dd %}
Multiplies the expected numerical value by the provided factor.
{% /dd %}

{% dt %}
`array([[openCloseStr, ] separator][, subRuleOrFilter)`
{% /dt %}

{% dd %}
Parses a string sequence of tokens and returns it as an array. See the list to array example.
{% /dd %}

{% dt %}
`url`
{% /dt %}

{% dd %}
Parses a URL and returns all the tokenized members (domain, query params, port, etc.) in a JSON object.
{% /dd %}

{% /dl %}

{% /tab %}

## Advanced settings{% #advanced-settings %}

At the bottom of your Grok processor tiles, there is an **Advanced Settings** section:

{% image
   source="https://datadog-docs.imgix.net/images/logs/processing/parsing/advanced_settings.f5e1dc55d9d5986eb31426ea7d1fe7d6.png?auto=format"
   alt="Advanced Settings" /%}

### Parsing a specific text attribute{% #parsing-a-specific-text-attribute %}

Use the **Extract from** field to apply your Grok processor on a given text attribute instead of the default `message` attribute.

For example, consider an event containing a `command.line` attribute that should be parsed as a key-value. You could parse this event as follows:

{% image
   source="https://datadog-docs.imgix.net/images/logs/processing/parsing/parsing_attribute.c6a8ba92fbdf1c94ec7bcb6a1c3ee9da.png?auto=format"
   alt="Parsing Command Line" /%}

### Using helper rules to factorize multiple parsing rules{% #using-helper-rules-to-factorize-multiple-parsing-rules %}

Use the **Helper Rules** field to define tokens for your parsing rules. Helper rules help you to factorize Grok patterns across your parsing rules. This is useful when you have several rules in the same Grok parser that use the same tokens.

Example for a classic unstructured event:

```text
john id:12345 connected on 11/08/2017 on server XYZ in production
```

Use the following parsing rule:

```text
MyParsingRule %{user} %{connection} %{server}
```

With the following helpers:

```text
user %{word:user.name} id:%{integer:user.id}
connection connected on %{date("MM/dd/yyyy"):connect_date}
server on server %{notSpace:server.name} in %{notSpace:server.env}
```

{% image
   source="https://datadog-docs.imgix.net/images/logs/processing/parsing/helper_rules.311405180d16349691a042023cc23e5a.png?auto=format"
   alt="helper rules" /%}

## Examples{% #examples %}

Some examples demonstrating how to use parsers:

- Key value or logfmt
- Parsing dates
- Alternating patterns
- Optional attribute
- Nested JSON
- Regex
- List and Arrays
- Glog format
- XML
- CSV

### Key value or logfmt{% #key-value-or-logfmt %}

This is the key-value core filter: `keyvalue([separatorStr[, characterAllowList[, quotingStr[, delimiter]]]])` where:

- `separatorStr`: defines the separator between key and values. Defaults to `=`.
- `characterAllowList`: defines extra non-escaped value chars in addition to the default `\\w.\\-_@`. Used only for non-quoted values (for example, `key=@valueStr`).
- `quotingStr`: defines quotes, replacing the default quotes detection: `<>`, `""`, `''`.
- `delimiter`: defines the separator between the different key values pairs (for example, `|`is the delimiter in `key1=value1|key2=value2`). Defaults to (normal space), `,` and `;`.

Use filters such as **keyvalue** to more-easily map strings to attributes for keyvalue or logfmt formats:

**Event:**

```text
user=john connect_date=11/08/2017 id=123 action=click
```

**Rule:**

```text
rule %{data::keyvalue}
```

{% image
   source="https://datadog-docs.imgix.net/images/logs/processing/parsing/parsing_example_2.71a6d2c9cef679099c875197001efd9b.png?auto=format"
   alt="Parsing example 2" /%}

You don't need to specify the name of your parameters as they are already contained in the event. If you add an **extract** attribute `my_attribute` in your rule pattern you will see:

{% image
   source="https://datadog-docs.imgix.net/images/logs/processing/parsing/parsing_example_2_bis.0836951a49c1e377828278b9ddadbf5f.png?auto=format"
   alt="Parsing example 2 bis" /%}

If `=` is not the default separator between your key and values, add a parameter in your parsing rule with a separator.

**Event:**

```text
user: john connect_date: 11/08/2017 id: 123 action: click
```

**Rule:**

```text
rule %{data::keyvalue(": ")}
```

{% image
   source="https://datadog-docs.imgix.net/images/logs/processing/parsing/key_value_parser.6b8819cac345f70e7b4e20b41e3e85e4.png?auto=format"
   alt="Key value parser" /%}

If event contain special characters in an attribute value, such as `/` in a url for instance, add it to the allowlist in the parsing rule:

**Event:**

```text
url=https://app.datadoghq.com/event/stream user=john
```

**Rule:**

```text
rule %{data::keyvalue("=","/:")}
```

{% image
   source="https://datadog-docs.imgix.net/images/logs/processing/parsing/key_value_allowlist.5470ec412a16c31109afd84021c1d306.png?auto=format"
   alt="Key value allowlist" /%}

Other examples:

| **Raw string**              | **Parsing rule**                      | **Result**                           |
| --------------------------- | ------------------------------------- | ------------------------------------ |
| key=valueStr                | `%{data::keyvalue}`                   | {"key": "valueStr"}                  |
| key=<valueStr>              | `%{data::keyvalue}`                   | {"key": "valueStr"}                  |
| "key"="valueStr"            | `%{data::keyvalue}`                   | {"key": "valueStr"}                  |
| key:valueStr                | `%{data::keyvalue(":")}`              | {"key": "valueStr"}                  |
| key:"/valueStr"             | `%{data::keyvalue(":", "/")}`         | {"key": "/valueStr"}                 |
| /key:/valueStr              | `%{data::keyvalue(":", "/")}`         | {"/key": "/valueStr"}                |
| key:={valueStr}             | `%{data::keyvalue(":=", "", "{}")}`   | {"key": "valueStr"}                  |
| key1=value1|key2=value2     | `%{data::keyvalue("=", "", "", "|")}` | {"key1": "value1", "key2": "value2"} |
| key1="value1"|key2="value2" | `%{data::keyvalue("=", "", "", "|")}` | {"key1": "value1", "key2": "value2"} |

**Multiple QuotingString example**: When multiple quotingstring are defined, the default behavior is replaced with a defined quoting character. The key-value always matches inputs without any quoting characters, regardless of what is specified in `quotingStr`. When quoting characters are used, the `characterAllowList` is ignored as everything between the quoting characters is extracted.

**Event:**

```text
key1:=valueStr key2:=</valueStr2> key3:="valueStr3"
```

**Rule:**

```text
rule %{data::keyvalue(":=","","<>")}
```

**Result:**

```json
{"key1": "valueStr", "key2": "/valueStr2"}
```

**Note**:

- Empty values (`key=`) or `null` values (`key=null`) are not displayed in the output JSON.
- If you define a *keyvalue* filter on a `data` object, and this filter is not matched, then an empty JSON `{}` is returned (for example, input: `key:=valueStr`, parsing rule: `rule_test %{data::keyvalue("=")}`, output: `{}`).
- Defining `""` as `quotingStr` keeps the default configuration for quoting.

### Parsing dates{% #parsing-dates %}

The date matcher transforms your timestamp in the EPOCH format (unit of measure **millisecond**).

| **Raw string**                | **Parsing rule**                                          | **Result**              |
| ----------------------------- | --------------------------------------------------------- | ----------------------- |
| 14:20:15                      | `%{date("HH:mm:ss"):date}`                                | {"date": 51615000}      |
| 02:20:15 PM                   | `%{date("hh:mm:ss a"):date}`                              | {"date": 51615000}      |
| 11/10/2014                    | `%{date("dd/MM/yyyy"):date}`                              | {"date": 1412978400000} |
| Thu Jun 16 08:29:03 2016      | `%{date("EEE MMM dd HH:mm:ss yyyy"):date}`                | {"date": 1466065743000} |
| Tue Nov 1 08:29:03 2016       | `%{date("EEE MMM d HH:mm:ss yyyy"):date}`                 | {"date": 1466065743000} |
| 06/Mar/2013:01:36:30 +0900    | `%{date("dd/MMM/yyyy:HH:mm:ss Z"):date}`                  | {"date": 1362501390000} |
| 2016-11-29T16:21:36.431+0000  | `%{date("yyyy-MM-dd'T'HH:mm:ss.SSSZ"):date}`              | {"date": 1480436496431} |
| 2016-11-29T16:21:36.431+00:00 | `%{date("yyyy-MM-dd'T'HH:mm:ss.SSSZZ"):date}`             | {"date": 1480436496431} |
| 06/Feb/2009:12:14:14.655      | `%{date("dd/MMM/yyyy:HH:mm:ss.SSS"):date}`                | {"date": 1233922454655} |
| 2007-08-31 19:22:22.427 ADT   | `%{date("yyyy-MM-dd HH:mm:ss.SSS z"):date}`               | {"date": 1188598942427} |
| Thu Jun 16 08:29:03 20161     | `%{date("EEE MMM dd HH:mm:ss yyyy","Europe/Paris"):date}` | {"date": 1466058543000} |
| Thu Jun 16 08:29:03 20161     | `%{date("EEE MMM dd HH:mm:ss yyyy","UTC+5"):date}`        | {"date": 1466047743000} |
| Thu Jun 16 08:29:03 20161     | `%{date("EEE MMM dd HH:mm:ss yyyy","+3"):date}`           | {"date": 1466054943000} |

1 Use the `timezone` parameter if you perform your own localizations and your timestamps are *not* in UTC. The supported format for timezones are:

- `GMT`, `UTC`, `UT` or `Z`
- `+h`, `+hh`, `+hh:mm`, `-hh:mm`, `+hhmm`, `-hhmm`, `+hh:mm:ss`, `-hh:mm:ss`, `+hhmmss` or `-hhmmss` . The maximum supported range is from +18:00 to -18:00 inclusive.
- Timezones starting with `UTC+`, `UTC-`, `GMT+`, `GMT-`, `UT+` or `UT-`. The maximum supported range is from +18:00 to -18:00 inclusive.
- Timezone IDs pulled from the TZ database. For more information, see [TZ database names](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).

**Note**: Parsing a date **doesn't** set its value as the event official date. For this use the [Event Date Remapper](https://docs.datadoghq.com/events/pipelines_and_processors/date_remapper) in a subsequent Processor.

### Alternating pattern{% #alternating-pattern %}

If you have events with two possible formats which differ in only one attribute, set a single rule using alternating with `(<REGEX_1>|<REGEX_2>)`. This rule is equivalent to a Boolean OR.

**Event**:

```text
john connected on 11/08/2017
12345 connected on 11/08/2017
```

**Rule**: Note that "id" is an integer and not a string.

```text
MyParsingRule (%{integer:user.id}|%{word:user.firstname}) connected on %{date("MM/dd/yyyy"):connect_date}
```

**Results**:

{% image
   source="https://datadog-docs.imgix.net/images/logs/processing/parsing/parsing_example_4.b517122596938ad69c6b98d4178c21f3.png?auto=format"
   alt="Parsing example 4" /%}

{% image
   source="https://datadog-docs.imgix.net/images/logs/processing/parsing/parsing_example_4_bis.3ee323462287fb10cb04ca593dc985d3.png?auto=format"
   alt="Parsing example 4 bis" /%}

### Optional attribute{% #optional-attribute %}

Some events contain values that only appear part of the time. In this case, make attribute extraction optional with `()?`.

**Event**:

```text
john 1234 connected on 11/08/2017
```

**Rule**:

```text
MyParsingRule %{word:user.firstname} (%{integer:user.id} )?connected on %{date("MM/dd/yyyy"):connect_date}
```

**Note**: A rule will not match if you include a space after the first word in the optional section.

{% image
   source="https://datadog-docs.imgix.net/images/logs/processing/parsing/parsing_example_5.cc8db31d292d13acf4c978961eaf8539.png?auto=format"
   alt="Parsing example 5" /%}

{% image
   source="https://datadog-docs.imgix.net/images/logs/processing/parsing/parsing_example_5_bis.4c64168ca5749fdf339377526ba2b1d5.png?auto=format"
   alt="Parsing example 5 bis" /%}

### Nested JSON{% #nested-json %}

Use the `json` filter to parse a JSON object nested after a raw text prefix:

**Event**:

```text
Sep 06 09:13:38 vagrant program[123]: server.1 {"method":"GET", "status_code":200, "url":"https://app.datadoghq.com/logs/pipelines", "duration":123456}
```

**Rule**:

```text
parsing_rule %{date("MMM dd HH:mm:ss"):timestamp} %{word:vm} %{word:app}\[%{number:logger.thread_id}\]: %{notSpace:server} %{data::json}
```

{% image
   source="https://datadog-docs.imgix.net/images/logs/processing/parsing/nested_json.4caef0844ce02f2bdbe457e638640a89.png?auto=format"
   alt="Nested JSON Parsing example" /%}

### Regex{% #regex %}

**Event**:

```text
john_1a2b3c4 connected on 11/08/2017
```

**Rule**:

```text
MyParsingRule %{regex("[a-z]*"):user.firstname}_%{regex("[a-zA-Z0-9]*"):user.id} .*
```

{% image
   source="https://datadog-docs.imgix.net/images/logs/processing/parsing/regex_parsing.5786fab9570bafd53c050879a4e74280.png?auto=format"
   alt="Parsing example 6" /%}

### List to array{% #list-to-array %}

Use the `array([[openCloseStr, ] separator][, subRuleOrFilter)` filter to extract a list into an array in a single attribute. The `subRuleOrFilter` is optional and accepts these [filters](https://docs.datadoghq.com/events/pipelines_and_processors/grok_parser/?tab=filters&tabs=filters#matcher-and-filter).

**Event**:

```text
Users [John, Oliver, Marc, Tom] have been added to the database
```

**Rule**:

```text
myParsingRule Users %{data:users:array("[]",",")} have been added to the database
```

{% image
   source="https://datadog-docs.imgix.net/images/logs/processing/parsing/array_parsing.ca36ff41521be80abf528f9fd0a49463.png?auto=format"
   alt="Parsing example 6" /%}

**Event**:

```text
Users {John-Oliver-Marc-Tom} have been added to the database
```

**Rule**:

```text
myParsingRule Users %{data:users:array("{}","-")} have been added to the database
```

**Rule using `subRuleOrFilter`**:

```text
myParsingRule Users %{data:users:array("{}","-", uppercase)} have been added to the database
```

### Glog format{% #glog-format %}

Kubernetes components sometimes log in the `glog` format; this example is from the Kube Scheduler item in the Pipeline Library.

Example Event:

```text
W0424 11:47:41.605188       1 authorization.go:47] Authorization is disabled
```

Parsing rule:

```text
kube_scheduler %{regex("\\w"):level}%{date("MMdd HH:mm:ss.SSSSSS"):timestamp}\s+%{number:logger.thread_id} %{notSpace:logger.name}:%{number:logger.lineno}\] %{data:msg}
```

And extracted JSON:

```json
{
  "level": "W",
  "timestamp": 1587728861605,
  "logger": {
    "thread_id": 1,
    "name": "authorization.go"
  },
  "lineno": 47,
  "msg": "Authorization is disabled"
}
```

### Parsing XML{% #parsing-xml %}

The XML parser transforms XML formatted messages into JSON.

**Event:**

```text
<book category="CHILDREN">
  <title lang="en">Harry Potter</title>
  <author>J K. Rowling</author>
  <year>2005</year>
</book>
```

**Rule:**

```text
rule %{data::xml}
```

**Result:**

```json
{
"book": {
  "year": "2005",
  "author": "J K. Rowling",
  "category": "CHILDREN",
  "title": {
    "lang": "en",
    "value": "Harry Potter"
  }
}
}
```

**Notes**:

- If the XML contains tags that have both an attribute and a string value between the two tags, a `value` attribute is generated. For example: `<title lang="en">Harry Potter</title>` is converted to `{"title": {"lang": "en", "value": "Harry Potter" } }`
- Repeated tags are automatically converted to arrays. For example: `<bookstore><book>Harry Potter</book><book>Everyday Italian</book></bookstore>` is converted to `{ "bookstore": { "book": [ "Harry Potter", "Everyday Italian" ] } }`

### Parsing CSV{% #parsing-csv %}

Use the **CSV** filter to more-easily map strings to attributes when separated by a given character (`,` by default).

The CSV filter is defined as `csv(headers[, separator[, quotingcharacter]])` where:

- `headers`: Defines the keys name separated by `,`. Keys names must start with alphabetical character and can contain any alphanumerical character in addition to `_`.
- `separator`: Defines separators used to separate the different values. Only one character is accepted. Default: `,`. **Note**: Use `tab` for the `separator` to represent the tabulation character for TSVs.
- `quotingcharacter`: Defines the quoting character. Only one character is accepted. Default: `"`

**Note**:

- Values containing a separator character must be quoted.
- Quoted Values containing a quoting character must be escaped with a quoting characters. For example, `""` within a quoted value represents `"`.
- If the event doesn't contain the same number of value as the number of keys in the header, the CSV parser will match the first ones.
- Intergers and Double are automatically casted if possible.

**Event**:

```text
John,Doe,120,Jefferson St.,Riverside
```

**Rule**:

```text
myParsingRule %{data:user:csv("first_name,name,st_nb,st_name,city")}
```

**Result:**

```json
{
  "user": {
    "first_name": "John",
    "name": "Doe",
    "st_nb": 120,
    "st_name": "Jefferson St.",
    "city": "Riverside"
  }
}
```

Other examples:

| **Raw string**                     | **Parsing rule**                         | **Result**                                            |
| ---------------------------------- | ---------------------------------------- | ----------------------------------------------------- |
| `John,Doe`                         | `%{data::csv("firstname,name")}`         | {"firstname": "John", "name":"Doe"}                   |
| `"John ""Da Man""",Doe`            | `%{data::csv("firstname,name")}`         | {"firstname": "John "Da Man"", "name":"Doe"}          |
| `'John ''Da Man''',Doe`            | `%{data::csv("firstname,name",",","'")}` | {"firstname": "John 'Da Man'", "name":"Doe"}          |
| `John|Doe`                         | `%{data::csv("firstname,name","|")}`     | {"firstname": "John", "name":"Doe"}                   |
| `value1,value2,value3`             | `%{data::csv("key1,key2")}`              | {"key1": "value1", "key2":"value2"}                   |
| `value1,value2`                    | `%{data::csv("key1,key2,key3")}`         | {"key1": "value1", "key2":"value2"}                   |
| `value1,,value3`                   | `%{data::csv("key1,key2,key3")}`         | {"key1": "value1", "key3":"value3"}                   |
| `Value1Â Â Â Â Value2Â Â Â Â Value3` (TSV) | `%{data::csv("key1,key2,key3","tab")}`   | {"key1": "value1", "key2": "value2", "key3":"value3"} |

### Use data matcher to discard unneeded text{% #use-data-matcher-to-discard-unneeded-text %}

If you have an event where after you have parsed what is needed and know that the text after that point is safe to discard, you can use the data matcher to do so. For the following event example, you can use the `data` matcher to discard the `%` at the end.

**Event**:

```
Usage: 24.3%
```

**Rule**:

```
MyParsingRule Usage\:\s+%{number:usage}%{data:ignore}
```

**Result**:

```
{
  "usage": 24.3,
  "ignore": "%"
}
```

### ASCII control characters{% #ascii-control-characters %}

If your events contain ASCII control characters, they are serialized upon ingestion. These can be handled by explicitly escaping the serialized value within your grok parser.
