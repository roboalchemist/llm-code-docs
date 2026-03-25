# Source: https://code.kx.com/kdbai/latest/reference/supported-types.html

Title: About supported data types in KDB.AI

URL Source: https://code.kx.com/kdbai/latest/reference/supported-types.html

Markdown Content:
_This page provides details on the data types used within KDB.AI tables, including name, range/example, brief description, and usage._

In KDB.AI, tables are fundamental structures for storing and organizing data. A schema is a list of column definitions that defines the structure of a table. Each column holds data of a specific type, such as integers, symbols, or dates.

Here’s a list of supported data types ([scalar](https://code.kx.com/kdbai/latest/reference/glossary.html#scalar-type) and [list](https://code.kx.com/kdbai/latest/reference/glossary.html#list-type)) in KDB.AI tables:

| **Datatype** | **q Type (scalar/list)** | **JSON Type (scalar/list)** | **Python (scalar/list)** | **Example/Range** | **Description** | **Usage** |
| --- | --- | --- | --- | --- | --- | --- |
| boolean | b / B | boolean / booleans | bool / bools | true, false | Represents true or false values | Used for binary conditions and flags |
| byte | x / X | byte / bytes | uint8 / uint8s | 0 to 255 | 8-bit unsigned integer | Used for raw binary data |
| char | c / C | char / chars | char / bytes | 'a', 'b', 'c' | Single character | Used for single character data |
| date | d / D | date / dates | datetime64[D] / datetime64[D]s | 2024.10.30 | Calendar date | Used for date-specific data |
| float | f / F | float / floats | float64 / float64s | 3.14, 2.718 | Double-precision floating-point number | Used for high-precision numerical data |
| guid | g / G | guid / guids | guid / guids | 123e4567-e89b-12d3-a456-426614174000 | Globally unique identifier | Used for unique identification |
| int | i / I | int / ints | int32 / int32s | -2147483648 to 2147483647 | 32-bit signed integer | Used for general integer data |
| long | j / J | long / longs | int64 / int64s | -9223372036854775808 to 9223372036854775807 | 64-bit signed integer | Used for large integer data |
| minute | u / U | minute / minutes | timedelta64[m] / timedelta64[m]s | 12:34 | Time duration in minutes | Used for time intervals |
| month | m / M | month / months | datetime64[M] / datetime64[M]s | 2024.10 | Year and month | Used for monthly data |
| real | e / E | real / reals | float32 / float32s | 3.14, 2.718 | Single-precision floating-point number | Used for numerical data with less precision |
| second | v / V | second / seconds | timedelta64[s] / timedelta64[s]s | 12:34:56 | Time duration in seconds | Used for time intervals |
| short | h / H | short / shorts | int16 / int16s | -32768 to 32767 | 16-bit signed integer | Used for smaller integer data |
| symbol | s / S | symbol / symbols | str | `AAPL`, `GOOG` | Interned string | Used for categorical data |
| time | t / T | time / times | timedelta64[ms] / timedelta64[ms]s | 12:34:56.789 | Time of day with millisecond precision | Used for time-specific data |
| timestamp | p / P | timestamp / timestamps | datetime64[ns] / datetime64[ns]s | 2024.10.30T12:34:56.789 | Date and time with nanosecond precision | Used for precise date-time data |
| timespan | n / N | timespan / timespans | timedelta64[ns] | 1234567890ns | Time duration with nanosecond precision | Used for high-precision time intervals |

Database types and JSON formats
-------------------------------

For [data ingestion](https://code.kx.com/kdbai/latest/use/ingestion.html), use the corresponding JSON formats for database types as below:

| **Database type ID** | **Database type name** | **JSON data format** | **Description** | **Example** |
| --- | --- | --- | --- | --- |
| -1h | boolean | `Boolean` | A Boolean literal of `true` or `false` | `true` |
| -2h | guid | `String` | A 36 character UUIDv4 formatted String | `"77579e36-71e7-d395-5551-5a4221e86e2b"` |
| -4h | byte | `String` | A 2 character hex string | `ff` |
| -5h | short | `Number` | A 16 bit number | `32767` |
| -6h | int | `Number` | A 32 bit number | `2147483647` |
| -7h | long | `Number` | A 64 bit number | `4611686018427387904` |
| -8h | real | `Number` | A 32 bit floating point number | `3.14159265` |
| -9h | float | `Number` | A 64 bit floating point number | `3.14159265` |
| -10h | char | `String` | A string of a single character | `"a"` |
| -11h | symbol | `String` | A string representing a symbol | `"BTC"` |
| -12h | timestamp | `String` | A ISO date-time without an offset in format `'yyyy-MM-dd'T'HH:mm:ss'` with optional 0-9 decimals for nanoseconds | `"2023-01-01T00:00:00.000000000"` |
| -13h | month | `String` | A string representing a month in format `MM-dd` | `"2023-10"` |
| -14h | date | `String` | A string representing an ISO Date without an offset in format `yyyy-MM-dd` | `"2023-10-01"` |
| -15h | datetime | `String` | A ISO date-time without an offset in format `'yyyy-MM-dd'T'HH:mm:ss'` with optional 0-3 decimals for milliseconds | `"2023-01-01T00:00:00.000"` |
| -16h | timespan | `String` | A duration of time with units in nanoseconds `'d'D'HH:mm:ss'` with optional 0-9 decimals for nanoseconds | `"0D00:00:00.000000005"` |
| -17h | minute | `String` | A duration of time in `HH:mm` | `"22:59"` |
| -18h | second | `String` | A duration of time in `HH:mm:ss` | `"22:59:13"` |
| -19h | time | `String` | A duration fo time in `HH:mm:ss` with optional 0-9 decimals for nanosecond precision | `"22:59:13.000000000"` |
| 1h | booleans | `Array<Boolean>` | Array of boolean values | `[true, false]` |
| 2h | guids | `Array<String>` | Array of guid values | `["09c4f826-b3f2-e699-c7ff-5195d89a0925", "c0b9ec94-87b6-b0e9-3427-312d62aaec9c"]` |
| 4h | bytes | `Array<String>` | Array of byte values | `["ff", "0e"]` |
| 5h | shorts | `Array<Number>` | Array of short values | `[32767, -32767]` |
| 6h | ints | `Array<Number>` | Array of int values | `[2147483647, -2147483647]` |
| 7h | longs | `Array<Number>` | Array of long values | `[4611686018427387904, -4611686018427387904]` |
| 8h | reals | `Array<Number>` | Array of real values | `[1.1, 1.2]` |
| 9h | floats | `Array<Number>` | Array of float values | `[1.1, 1.2]` |
| 10h | string | `String` | A string of text | `"abcdef"` |
| 11h | symbols | `Array<String>` | Array of symbol values | `["BTC","MSFT"]` |
| 12h | timestamps | `Array<String>` | Array of timestamp values | `["2023-01-01T00:00:00.000000000", "2023-01-02T00:00:00.000000000"]` |
| 13h | months | `Array<String>` | Array of month values | `["2023-10", "2023-11"]` |
| 14h | dates | `Array<String>` | Array of date values | `["2023-10-01", "2023-10-02"]` |
| 15h | datetimes | `Array<String>` | Array of datetime values | `["2023-01-01T00:00:00.000", "2023-01-02T00:00:00.000"]` |
| 16h | timespans | `Array<String>` | Array of timespan values | `["0D00:00:00.000000005", "0D00:00:00.000000006"]` |
| 17h | minutes | `Array<String>` | Array of minute values | `["22:59", "23:00"]` |
| 18h | seconds | `Array<String>` | Array of second values | `["22:59:13", "22:59:14"]` |
| 19h | times | `Array<String>` | Array of time values | `["22:59:13.000000000", "2023-01-01T00:00:00.001"]` |
