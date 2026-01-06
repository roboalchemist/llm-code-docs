# Source: https://docs.velodb.io/cloud/4.x/sql-manual/basic-element/sql-data-types/data-type-overview

Version: 4.x

On this page

# Overview

## Numeric Types​

Doris supports the following numeric data types:

### BOOLEAN​

There are two possible values: 0 represents false, and 1 represents true.

For more info, please refer [BOOLEAN](/cloud/4.x/sql-manual/basic-element/sql-
data-types/numeric/BOOLEAN)。

### Integer​

All are signed integers. The differences among the INT types are the number of
bytes occupied and the range of values they can represent:

  * **[TINYINT](/cloud/4.x/sql-manual/basic-element/sql-data-types/numeric/TINYINT)** : 1 byte, [-128, 127]

  * **[SMALLINT](/cloud/4.x/sql-manual/basic-element/sql-data-types/numeric/SMALLINT)** : 2 bytes, [-32768, 32767]

  * **[INT](/cloud/4.x/sql-manual/basic-element/sql-data-types/numeric/INT)** : 4 bytes, [-2147483648, 2147483647]

  * **[BIGINT](/cloud/4.x/sql-manual/basic-element/sql-data-types/numeric/BIGINT)** : 8 bytes, [-9223372036854775808, 9223372036854775807]

  * **[LARGEINT](/cloud/4.x/sql-manual/basic-element/sql-data-types/numeric/LARGEINT)** : 16 bytes, [-2^127, 2^127 - 1]

### Floating-point​

Including imprecise floating-point types [FLOAT](/cloud/4.x/sql-manual/basic-
element/sql-data-types/numeric/FLOAT) and [DOUBLE](/cloud/4.x/sql-
manual/basic-element/sql-data-types/numeric/DOUBLE), corresponding to the
`float` and `double` in common programming languages

### Fixed-point​

The precise fixed-point type [DECIMAL](/cloud/4.x/sql-manual/basic-
element/sql-data-types/numeric/DECIMAL), used in financial and other cases
that require strict accuracy.

## Date Types​

Date types include DATE, TIME and DATETIME, DATE type only stores the date
accurate to the day, DATETIME type stores the date and time, which can be
accurate to microseconds. TIME type only stores the time, and **does not
support the construction of the table storage for the time being, can only be
used in the query process**.

Do calculation for datetime types or converting them to numeric types, please
use functions like [TIME_TO_SEC](/cloud/4.x/sql-manual/sql-functions/scalar-
functions/date-time-functions/time-to-sec), [DATE_DIFF](/cloud/4.x/sql-
manual/sql-functions/scalar-functions/date-time-functions/datediff),
[UNIX_TIMESTAMP](/cloud/4.x/sql-manual/sql-functions/scalar-functions/date-
time-functions/unix-timestamp) . The result of directly converting them as
numeric types as not guaranteed.

For more information refer to [DATE](/cloud/4.x/sql-manual/basic-element/sql-
data-types/date-time/DATE), [TIME](/cloud/4.x/sql-manual/basic-element/sql-
data-types/date-time/TIME) and [DATETIME](/cloud/4.x/sql-manual/basic-
element/sql-data-types/date-time/DATETIME) documents.

## String Types​

Doris supports both fixed-length and variable-length strings, including:

  * **[CHAR(M)](/cloud/4.x/sql-manual/basic-element/sql-data-types/string-type/CHAR)** : A fixed-length string, where M is the byte length. The range for M is [1, 255].

  * **[VARCHAR(M)](/cloud/4.x/sql-manual/basic-element/sql-data-types/string-type/VARCHAR)** : A variable-length string, where M is the maximum length. The range for M is [1, 65533].

  * **[STRING](/cloud/4.x/sql-manual/basic-element/sql-data-types/string-type/STRING)** : A variable-length string with a default maximum length of 1,048,576 bytes (1 MB). This maximum length can be increased up to 2,147,483,643 bytes (2 GB) by configuring the `string_type_length_soft_limit_bytes`setting.

## Semi-Structured Types​

Doris supports different semi-structured data types for JSON data processing,
each tailored to different use cases.

  * **[ARRAY](/cloud/4.x/sql-manual/basic-element/sql-data-types/semi-structured/ARRAY)** / **[MAP](/cloud/4.x/sql-manual/basic-element/sql-data-types/semi-structured/MAP)** / **[STRUCT](/cloud/4.x/sql-manual/basic-element/sql-data-types/semi-structured/STRUCT)** : They support nested data and fixed schema, making them well-suited for analytical workloads such as user behavior and profile analysis, as well as querying data lake formats like Parquet. Due to the fixed schema, there is no overhead for dynamic schema inference, resulting in high write and analysis performance.

  * **[VARIANT](/cloud/4.x/sql-manual/basic-element/sql-data-types/semi-structured/VARIANT)** : It supports nested data and flexible schema. It is well-suited for analytical workloads such as log, trace, and IoT data analysis. It can accommodate any legal JSON data, which will be automatically expanded into sub-columns in a columnar storage format. This approach enables high compression rate in storage and high performance in data aggregation, filtering, and sorting.

  * **[JSON](/cloud/4.x/sql-manual/basic-element/sql-data-types/semi-structured/JSON)** : It supports nested data and flexible schema. It is optimized for high-concurrency point query use cases. The flexible schema allows for ingesting any legal JSON data, which will be stored in a binary format. Extracting fields from this binary JSON format is more than 2X faster than using regular JSON strings.

## Aggregation Types​

The aggregation data types store aggregation results or intermediate results
during aggregation. They are used for accelerating aggregation-heavy queries.

  * **[BITMAP](/cloud/4.x/sql-manual/basic-element/sql-data-types/aggregate/BITMAP)** : It is used for exact deduplication, such as in (UV) statistics and audience segmentation. It works in conjunction with BITMAP functions like `bitmap_union`, `bitmap_union_count`, `bitmap_hash`, and `bitmap_hash64`.

  * **[HLL](/cloud/4.x/sql-manual/basic-element/sql-data-types/aggregate/HLL)** : It is used for approximate deduplication and provides better performance than `COUNT DISTINCT`. It works in conjunction with HLL functions like `hll_union_agg`, `hll_raw_agg`, `hll_cardinality`, and `hll_hash`.

  * **[QUANTILE_STATE](/cloud/4.x/sql-manual/basic-element/sql-data-types/aggregate/QUANTILE-STATE)** : It is used for approximate percentile calculations and offers better performance than the `PERCENTILE` function. It works with functions like `QUANTILE_PERCENT`, `QUANTILE_UNION`, and `TO_QUANTILE_STATE`.

  * **[AGG_STATE](/cloud/4.x/sql-manual/basic-element/sql-data-types/aggregate/AGG-STATE)** : It is used to accelerate aggregations, utilized in combination with aggregation function combinators like state/merge/union.

## IP Types​

IP data types store IP addresses in a binary format, which is faster and more
space-efficient for querying compared to storing them as strings. There are
two supported IP data types:

  * **[IPv4](/cloud/4.x/sql-manual/basic-element/sql-data-types/ip/IPV4)** : It stores IPv4 addresses as a 4-byte binary value. It is used in conjunction with the `ipv4_*` family of functions.
  * **[IPv6](/cloud/4.x/sql-manual/basic-element/sql-data-types/ip/IPV6)** : It stores IPv6 addresses as a 16-byte binary value. It is used in conjunction with the `ipv6_*` family of functions.

On This Page

  * Numeric Types
    * BOOLEAN
    * Integer
    * Floating-point
    * Fixed-point
  * Date Types
  * String Types
  * Semi-Structured Types
  * Aggregation Types
  * IP Types

