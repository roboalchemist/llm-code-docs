# Source: https://docs.pinot.apache.org/release-0.9.0/users/user-guide-query/supported-transformations.md

# Source: https://docs.pinot.apache.org/release-0.10.0/users/user-guide-query/supported-transformations.md

# Source: https://docs.pinot.apache.org/release-0.11.0/users/user-guide-query/supported-transformations.md

# Source: https://docs.pinot.apache.org/release-0.12.0/users/user-guide-query/supported-transformations.md

# Source: https://docs.pinot.apache.org/release-0.12.1/users/user-guide-query/supported-transformations.md

# Source: https://docs.pinot.apache.org/release-1.0.0/for-users/user-guide-query/supported-transformations.md

# Source: https://docs.pinot.apache.org/release-1.1.0/for-users/user-guide-query/query-syntax/supported-transformations.md

# Source: https://docs.pinot.apache.org/release-1.2.0/for-users/user-guide-query/query-syntax/supported-transformations.md

# Source: https://docs.pinot.apache.org/release-1.3.0/for-users/user-guide-query/query-syntax/supported-transformations.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions/supported-transformations.md

# Source: https://docs.pinot.apache.org/functions/supported-transformations.md

# Transformation Functions

## Math Functions

| Function                                                                                                                                             |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p><a href="../functions-1/add"><strong>ADD(col1, col2, col3...)</strong></a><br>Sum of at least two values</p>                                      |
| <p><a href="../functions-1/sub"><strong>SUB(col1, col2)</strong></a><br>Difference between two values</p>                                            |
| <p><a href="../functions-1/mult"><strong>MULT(col1, col2, col3...)</strong></a><br>Product of at least two values</p>                                |
| <p><a href="../functions-1/div"><strong>DIV(col1, col2)</strong></a><br>Quotient of two values</p>                                                   |
| <p><a href="../functions-1/mod"><strong>MOD(col1, col2)</strong></a><br>Modulo of two values</p>                                                     |
| <p><a href="../functions-1/abs"><strong>ABS(col1)</strong></a><br>Absolute of a value</p>                                                            |
| <p><a href="../../functions-1/ceil#signature"><strong>CEIL(col1)</strong></a><br>Rounded up to the nearest integer</p>                               |
| <p><a href="../functions-1/floor"><strong>FLOOR(col1)</strong></a><br>Rounded down to the nearest integer</p>                                        |
| <p><a href="../functions-1/exp"><strong>EXP(col1)</strong></a><br>Euler’s number(e) raised to the power of col.</p>                                  |
| <p><a href="../functions-1/ln"><strong>LN(col1)</strong></a><br>Natural log of value</p>                                                             |
| <p><a href="../functions-1/sqrt"><strong>SQRT(col1)</strong></a><br>Square root of a value</p>                                                       |
| <p><a href="../functions-1/round-1"><strong>ROUNDDECIMAL(col1, col2)</strong><br></a></p><p>Rounds value to a specified number of decimal places</p> |

## String Functions

Multiple string functions are supported out of the box from release-0.5.0 .

| Function                                                                                                                                                                                                                                             |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p><a href="../functions-1/upper"><strong>UPPER</strong></a>(col)<br>convert string to upper case</p>                                                                                                                                                |
| <p><a href="../functions-1/lower"><strong>LOWER</strong></a>(col)<br>convert string to lower case</p>                                                                                                                                                |
| <p><a href="../functions-1/reverse"><strong>REVERSE</strong></a>(col)<br>reverse the string</p>                                                                                                                                                      |
| <p><a href="../functions-1/substr"><strong>SUBSTR</strong></a>(col, startIndex, endIndex)<br>Gets substring of the input string from start to endIndex. Index begins at 0. Set endIndex to -1 to calculate till end of the string</p>                |
| <p><a href="../functions-1/concat"><strong>CONCAT(col1, col2, seperator)</strong></a><br>Concatenate two input strings using the seperator</p>                                                                                                       |
| <p><a href="../functions-1/trim"><strong>TRIM(col)</strong></a><br>trim spaces from both side of the string</p>                                                                                                                                      |
| <p><a href="../functions-1/ltrim"><strong>LTRIM(col)</strong></a><br>trim spaces from left side of the string</p>                                                                                                                                    |
| <p><a href="../functions-1/rtrim"><strong>RTRIM(col)</strong></a><br>trim spaces from right side of the string</p>                                                                                                                                   |
| <p><a href="../functions-1/length"><strong>LENGTH(col)</strong></a><br>calculate length of the string</p>                                                                                                                                            |
| <p><a href="../functions-1/strpos"><strong>STRPOS(col, find, N)</strong></a><br>Find Nth instance of <code>find</code> string in input. Returns 0 if input string is empty. Returns -1 if the Nth instance is not found or input string is null.</p> |
| <p><a href="../functions-1/startswith"><strong>STARTSWITH(col, prefix)</strong></a><br>returns <code>true</code> if columns starts with prefix string.</p>                                                                                           |
| <p><a href="../functions-1/replace"><strong>REPLACE(col, find, substitute)</strong></a><br>replace all instances of <code>find</code> with <code>replace</code> in input</p>                                                                         |
| <p><a href="../functions-1/rpad"><strong>RPAD(col, size, pad)</strong></a><br>string padded from the right side with <code>pad</code> to reach final <code>size</code></p>                                                                           |
| <p><a href="../functions-1/lpad"><strong>LPAD(col, size, pad)</strong></a><br>string padded from the left side with <code>pad</code> to reach final <code>size</code></p>                                                                            |
| <p><a href="../functions-1/codepoint"><strong>CODEPOINT(col)</strong></a><br>the Unicode codepoint of the first character of the string</p>                                                                                                          |
| <p><a href="../functions-1/chr"><strong>CHR(codepoint)</strong></a><br>the character corresponding to the Unicode codepoint</p>                                                                                                                      |
| <p><a href="../functions-1/regexpextract"><strong>regexpExtract(value, regexp)</strong></a><br>Extracts values that match the provided regular expression</p>                                                                                        |
| <p><a href="../functions-1/regexpreplace"><strong>regexpReplace(input, matchRegexp, replaceRegexp, matchStartPos, occurrence, flag)</strong><br></a>Find and replace a string or regexp pattern with a target string or regexp pattern</p>           |
| <p><a href="../functions-1/remove"><strong>remove(input, search)</strong></a><br>removes all instances of search from string</p>                                                                                                                     |
| <p><a href="../functions-1/url"><strong>urlEncoding(string)</strong></a><br>url-encode a string with UTF-8 format</p>                                                                                                                                |
| <p><a href="../functions-1/url"><strong>urlDecoding(string)</strong></a><br>decode a url to plaintext string</p>                                                                                                                                     |
| <p><a href="../functions-1/base64"><strong>fromBase64(string)</strong></a><br>decode a Base64-encoded string to bytes represented as a hex string</p>                                                                                                |
| <p><a href="../functions-1/utf8"><strong>toUtf8(string)</strong></a><br>decode a UTF8-encoded string to bytes represented as a hex string</p>                                                                                                        |
| <p><a href="../functions-1/issubnetof"><strong>isSubnetOf(ipPrefix, ipAddress)</strong></a><br>checks if ipAddress is in the subnet of the ipPrefix</p>                                                                                              |

## DateTime Functions

Date time functions allow you to perform transformations on columns that contain timestamps or dates.

| Function                                                                                                                                                                                                                                                             |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p><a href="../functions-1/timeconvert"><strong>TIMECONVERT(col, fromUnit, toUnit)</strong></a><br>Converts the value into another time unit. the column should be an epoch timestamp.</p>                                                                           |
| <p><a href="../functions-1/datetimeconvert"><strong>DATETIMECONVERT(columnName, inputFormat, outputFormat, outputGranularity)</strong></a><br>Converts the value into another date time format, and buckets time based on the given time granularity.</p>            |
| <p><a href="../functions-1/datetrunc"><strong>DATETRUNC</strong></a><br>Converts the value into a specified output granularity seconds since UTC epoch that is bucketed on a unit in a specified timezone.</p>                                                       |
| <p><a href="../functions-1/toepoch"><strong>ToEpoch\<TIME\_UNIT>(timeInMillis)</strong></a><br>Convert epoch milliseconds to epoch \<Time Unit>.</p>                                                                                                                 |
| <p><a href="../functions-1/toepochrounded"><strong>ToEpoch\<TIME\_UNIT>Rounded(timeInMillis, bucketSize)</strong></a><br>Convert epoch milliseconds to epoch \<Time Unit>, round to nearest rounding bucket(Bucket size is defined in \<Time Unit>).</p>             |
| <p><a href="../functions-1/toepochbucket"><strong>ToEpoch\<TIME\_UNIT>Bucket(timeInMillis, bucketSize)</strong></a><br>Convert epoch milliseconds to epoch \<Time Unit>, and divided by bucket size(Bucket size is defined in \<Time Unit>).</p>                     |
| <p><a href="../functions-1/fromepoch"><strong>FromEpoch\<TIME\_UNIT></strong><br></a>Convert epoch \<Time Unit> to epoch milliseconds.<a href="../functions-1/fromepoch"><strong>(timeIn\<Time\_UNIT>)</strong></a></p>                                              |
| <p><a href="../functions-1/fromepochbucket"><strong>FromEpoch\<TIME\_UNIT>Bucket(timeIn\<Time\_UNIT>, bucketSizeIn\<Time\_UNIT>)</strong></a><br>Convert epoch \<Bucket Size>\<Time Unit> to epoch milliseconds.</p>                                                 |
| <p><a href="../functions-1/todatetime"><strong>ToDateTime(timeInMillis, pattern\[, timezoneId])</strong></a><br>Convert epoch millis value to DateTime string represented by pattern.</p>                                                                            |
| <p><a href="../functions-1/fromdatetime"><strong>FromDateTime(dateTimeString, pattern)</strong></a><br>Convert DateTime string represented by pattern to epoch millis.</p>                                                                                           |
| <p><a href="../functions-1/round"><strong>round(timeValue, bucketSize)</strong></a><br>Round the given time value to nearest bucket start value.</p>                                                                                                                 |
| <p><a href="../functions-1/now"><strong>now()</strong></a><br>Return current time as epoch millis</p>                                                                                                                                                                |
| <p><a href="../functions-1/ago"><strong>ago()</strong></a><br>Return time as epoch millis before the given period (in ISO-8601 duration format)</p>                                                                                                                  |
| <p><a href="../functions-1/timezonehour"><strong>timezoneHour(timeZoneId)</strong></a><br>Returns the hour of the time zone offset.</p>                                                                                                                              |
| <p><a href="../functions-1/timezoneminute"><strong>timezoneMinute(timeZoneId)</strong></a><br>Returns the minute of the time zone offset.</p>                                                                                                                        |
| <p><a href="../functions-1/year"><strong>year(tsInMillis)</strong></a><br>Returns the year from the given epoch millis in UTC timezone.</p>                                                                                                                          |
| <p><a href="../functions-1/year"><strong>year(tsInMillis, timeZoneId)</strong></a><br>Returns the year from the given epoch millis and timezone id.</p>                                                                                                              |
| <p><a href="../functions-1/yearofweek"><strong>yearOfWeek(tsInMillis)</strong></a><br>Returns the year of the ISO week from the given epoch millis in UTC timezone. Alias <code>yow</code>is also supported.</p>                                                     |
| <p><a href="../functions-1/yearofweek"><strong>yearOfWeek(tsInMillis, timeZoneId)</strong></a><br>Returns the year of the ISO week from the given epoch millis and timezone id. Alias <code>yow</code>is also supported.</p>                                         |
| <p><a href="../functions-1/quarter"><strong>quarter(tsInMillis)</strong></a><br>Returns the quarter of the year from the given epoch millis in UTC timezone. The value ranges from 1 to 4.</p>                                                                       |
| <p><a href="../functions-1/quarter"><strong>quarter(tsInMillis, timeZoneId)</strong></a><br>Returns the quarter of the year from the given epoch millis and timezone id. The value ranges from 1 to 4.</p>                                                           |
| <p><a href="../functions-1/month"><strong>month(tsInMillis)</strong></a><br>Returns the month of the year from the given epoch millis in UTC timezone. The value ranges from 1 to 12.</p>                                                                            |
| <p><a href="../functions-1/month"><strong>month(tsInMillis, timeZoneId)</strong></a><br>Returns the month of the year from the given epoch millis and timezone id. The value ranges from 1 to 12.</p>                                                                |
| <p><a href="../functions-1/week"><strong>week(tsInMillis)</strong></a><br>Returns the ISO week of the year from the given epoch millis in UTC timezone. The value ranges from 1 to 53. Alias <code>weekOfYear</code> is also supported.</p>                          |
| <p><a href="../functions-1/week"><strong>week(tsInMillis, timeZoneId)</strong></a><br>Returns the ISO week of the year from the given epoch millis and timezone id. The value ranges from 1 to 53. Alias <code>weekOfYear</code> is also supported.</p>              |
| <p><a href="../functions-1/dayofyear"><strong>dayOfYear(tsInMillis)</strong></a><br>Returns the day of the year from the given epoch millis in UTC timezone. The value ranges from 1 to 366. Alias <code>doy</code> is also supported.</p>                           |
| <p><a href="../functions-1/dayofyear"><strong>dayOfYear(tsInMillis, timeZoneId)</strong></a><br>Returns the day of the year from the given epoch millis and timezone id. The value ranges from 1 to 366. Alias <code>doy</code> is also supported.</p>               |
| <p><a href="../functions-1/day"><strong>day(tsInMillis)</strong></a><br>Returns the day of the month from the given epoch millis in UTC timezone. The value ranges from 1 to 31. Alias <code>dayOfMonth</code> is also supported.</p>                                |
| <p><a href="../functions-1/day"><strong>day(tsInMillis, timeZoneId)</strong></a><br>Returns the day of the month from the given epoch millis and timezone id. The value ranges from 1 to 31. Alias <code>dayOfMonth</code> is also supported.</p>                    |
| <p><a href="../functions-1/dayofweek"><strong>dayOfWeek(tsInMillis)</strong></a><br>Returns the day of the week from the given epoch millis in UTC timezone. The value ranges from 1(Monday) to 7(Sunday). Alias <code>dow</code> is also supported.</p>             |
| <p><a href="../functions-1/dayofweek"><strong>dayOfWeek(tsInMillis, timeZoneId)</strong></a><br>Returns the day of the week from the given epoch millis and timezone id. The value ranges from 1(Monday) to 7(Sunday). Alias <code>dow</code> is also supported.</p> |
| <p><a href="../functions-1/hour"><strong>hour(tsInMillis)</strong></a><br>Returns the hour of the day from the given epoch millis in UTC timezone. The value ranges from 0 to 23.</p>                                                                                |
| <p><a href="../functions-1/hour"><strong>hour(tsInMillis, timeZoneId)</strong></a><br>Returns the hour of the day from the given epoch millis and timezone id. The value ranges from 0 to 23.</p>                                                                    |
| <p><a href="../functions-1/minute"><strong>minute(tsInMillis)</strong></a><br>Returns the minute of the hour from the given epoch millis in UTC timezone. The value ranges from 0 to 59.</p>                                                                         |
| <p><a href="../functions-1/minute"><strong>minute(tsInMillis, timeZoneId)</strong></a><br>Returns the minute of the hour from the given epoch millis and timezone id. The value ranges from 0 to 59.</p>                                                             |
| <p><a href="../functions-1/second"><strong>second(tsInMillis)</strong></a><br>Returns the second of the minute from the given epoch millis in UTC timezone. The value ranges from 0 to 59.</p>                                                                       |
| <p><a href="../functions-1/second"><strong>second(tsInMillis, timeZoneId)</strong></a><br>Returns the second of the minute from the given epoch millis and timezone id. The value ranges from 0 to 59.</p>                                                           |
| <p><a href="../functions-1/millisecond"><strong>millisecond(tsInMillis)</strong></a><br>Returns the millisecond of the second from the given epoch millis in UTC timezone. The value ranges from 0 to 999.</p>                                                       |
| <p><a href="../functions-1/millisecond"><strong>millisecond(tsInMillis, timeZoneId)</strong></a><br>Returns the millisecond of the second from the given epoch millis and timezone id. The value ranges from 0 to 999.</p>                                           |

## JSON Functions

### **Transform Functions**

These functions can only be used in Pinot SQL queries.

| Function                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p><a href="../functions-1/jsonextractscalar"><strong>JSONEXTRACTSCALAR(jsonField, 'jsonPath', 'resultsType', \[defaultValue])</strong></a><br>Evaluates the <code>'jsonPath'</code> on <code>jsonField</code>, returns the result as the type <code>'resultsType'</code>, use optional <code>defaultValue</code>for null or parsing error.</p>                                                                                                                                  |
| <p><a href="../functions-1/jsonextractkey"><strong>JSONEXTRACTKEY</strong></a><a href="../functions-1/jsonextractkey"><strong>(</strong>jsonField, 'jsonPath'<strong>)</strong></a><br>Extracts all matched JSON field keys based on <code>'jsonPath'</code> into a <code>STRING\_ARRAY.</code></p>                                                                                                                                                                              |
| <p><a href="https://github.com/pinot-contrib/pinot-docs/blob/latest/configuration-reference/functions/extract.md"><strong>EXTRACT(dateTimeField FROM dateTimeExpression)</strong></a><br>Extracts the field from the DATETIME expression of the format <code>'YYYY-MM-DD HH:MM:SS'</code>. Currently, this transformation function supports <code>YEAR</code>, <code>MONTH</code>, <code>DAY</code>, <code>HOUR</code>, <code>MINUTE</code>, and <code>SECOND</code> fields.</p> |

### **Scalar Functions**

These functions can be used for column transformation in table ingestion configs.

| Function                                                                                                                                                                                                                                                                                                                                                                                        |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p><a href="../functions-1/tojsonmapstr"><strong>TOJSONMAPSTR</strong>(map)<br>Convert map to JSON String</a></p>                                                                                                                                                                                                                                                                               |
| <p><a href="../functions-1/jsonformat"><strong>JSONFORMAT</strong>(object)</a><br>Convert object to JSON String</p>                                                                                                                                                                                                                                                                             |
| <p><a href="../functions-1/jsonpath"><strong>JSONPATH(jsonField, 'jsonPath')</strong></a><br>Extracts the object value from <code>jsonField</code> based on <code>'jsonPath'</code>, the result type is inferred based on JSON value. <strong>Cannot be used in query because data type is not specified.</strong></p>                                                                          |
| <p><a href="../functions-1/jsonpathlong"><strong>JSONPATHLONG</strong>(jsonField, 'jsonPath', \[defaultValue])</a><br>Extracts the <strong>Long</strong> value from <code>jsonField</code> based on <code>'jsonPath'</code>, use optional <code>defaultValue</code>for null or parsing error.</p>                                                                                               |
| <p><a href="../functions-1/jsonpathdouble"><strong>JSONPATHDOUBLE</strong>(jsonField, 'jsonPath', \[defaultValue])</a><br>Extracts the <strong>Double</strong> value from <code>jsonField</code> based on <code>'jsonPath'</code>, use optional <code>defaultValue</code>for null or parsing error.</p>                                                                                         |
| <p><a href="../functions-1/jsonpathstring"><strong>JSONPATHSTRING(jsonField, 'jsonPath', \[defaultValue])</strong></a><br>Extracts the <strong>String</strong> value from <code>jsonField</code> based on <code>'jsonPath'</code>, use optional <code>defaultValue</code>for null or parsing error.</p>                                                                                         |
| <p><a href="../functions-1/jsonpatharray"><strong>JSONPATHARRAY</strong>(jsonField, 'jsonPath')</a><br>Extracts an array from <code>jsonField</code> based on <code>'jsonPath'</code>, the result type is inferred based on JSON value. <strong>Cannot be used in query because data type is not specified.</strong></p>                                                                        |
| <p><a href="../functions-1/jsonpatharraydefaultempty"><strong>JSONPATHARRAYDEFAULTEMPTY</strong>(jsonField, 'jsonPath')</a><br>Extracts an array from <code>jsonField</code> based on <code>'jsonPath'</code>, the result type is inferred based on JSON value. Returns empty array for null or parsing error. <strong>Cannot be used in query because data type is not specified.</strong></p> |

## Binary Functions

| Function                                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p><a href="../functions-1/sha"><strong>SHA(bytesCol)</strong></a><br>Return SHA-1 digest of binary column(<code>bytes</code> type) as hex string</p>         |
| <p><a href="../functions-1/sha256"><strong>SHA256(bytesCol)</strong></a><br>Return SHA-256 digest of binary column(<code>bytes</code> type) as hex string</p> |
| <p><a href="../functions-1/sha512"><strong>SHA512(bytesCol)</strong></a><br>Return SHA-512 digest of binary column(<code>bytes</code> type) as hex string</p> |
| <p><a href="../functions-1/md5"><strong>MD5(bytesCol)</strong></a><br>Return MD5 digest of binary column(<code>bytes</code> type) as hex string</p>           |
| <p><a href="../functions-1/base64"><strong>toBase64(bytesCol)</strong></a><br>Return the Base64-encoded string of binary column(<code>bytes</code> type)</p>  |
| <p><a href="../functions-1/utf8"><strong>fromUtf8(bytesCol)</strong></a><br>Return the UTF8-encoded string of binary column(<code>bytes</code> type)</p>      |

## Multi-value Column Functions

All of the functions mentioned till now only support single value columns. You can use the following functions to do operations on multi-value columns.

| Function                                                                                                                                                                                                                                                                                                                           |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p><a href="../functions-1/arraylength"><strong>ARRAYLENGTH</strong></a><br>Returns the length of a multi-value</p>                                                                                                                                                                                                                |
| <p><strong>MAP\_VALUE</strong><br>Select the value for a key from Map stored in Pinot.<br><code>MAP\_VALUE(mapColumn, 'myKey', valueColumn)</code></p>                                                                                                                                                                             |
| <p><a href="../functions-1/valuein"><strong>VALUEIN</strong></a><br>The transform function will filter the value from the multi-valued column with the given constant values. The <code>VALUEIN</code> transform function is especially useful when the same multi-valued column is both filtering column and grouping column.</p> |

## Advanced Queries

### Geospatial Queries

Pinot supports Geospatial queries on columns containing text-based geographies. For more details on the queries and how to enable them, see [Geospatial](https://docs.pinot.apache.org/basics/indexing/geospatial-support).

### Text Queries

Pinot supports pattern matching on text-based columns. Only the columns mentioned as text columns in table config can be queried using this method. For more details on how to enable pattern matching, see [Text search support](https://docs.pinot.apache.org/basics/indexing/text-search-support).
