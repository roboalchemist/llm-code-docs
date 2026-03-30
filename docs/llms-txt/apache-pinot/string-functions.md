# Source: https://docs.pinot.apache.org/release-1.4.0/functions/string-functions.md

# Source: https://docs.pinot.apache.org/functions/string-functions.md

# String Functions

[**UPPER**](https://docs.pinot.apache.org/functions-1/upper)(col)\
convert string to upper case

[**LOWER**](https://docs.pinot.apache.org/functions-1/lower)(col)\
convert string to lower case

[**INITCAP**](https://github.com/pinot-contrib/pinot-docs/blob/latest/functions-1/initcap.md)(col)\
convert the first letter of each word to uppercase and the rest to lowercase

[**REVERSE**](https://docs.pinot.apache.org/functions-1/reverse)(col)\
reverse the string

[**SUBSTR**](https://docs.pinot.apache.org/functions-1/substr)(col, startIndex, endIndex)\
Gets substring of the input string from start to endIndex. Index begins at 0. Set endIndex to -1 to calculate till end of the string

[**CONCAT(col1, col2, seperator)**](https://docs.pinot.apache.org/functions-1/concat)\
Concatenate two input strings using the seperator

[**TRIM(col)**](https://docs.pinot.apache.org/functions-1/trim)\
trim spaces from both side of the string

[**LTRIM(col)**](https://docs.pinot.apache.org/functions-1/ltrim)\
trim spaces from left side of the string

[**RTRIM(col)**](https://docs.pinot.apache.org/functions-1/rtrim)\
trim spaces from right side of the string

[**LENGTH(col)**](https://docs.pinot.apache.org/functions-1/length)\
calculate length of the string

[**levenshtein\_distance(string1, string2)**](https://github.com/pinot-contrib/pinot-docs/blob/latest/functions-1/levenshtein_distance.md)\
Returns the Levenshtein edit distance between two strings

[**STRPOS(col, find, N)**](https://docs.pinot.apache.org/functions-1/strpos)\
Find Nth instance of `find` string in input. Returns 0 if input string is empty. Returns -1 if the Nth instance is not found or input string is null.

[**STARTSWITH(col, prefix)**](https://docs.pinot.apache.org/functions-1/startswith)\
returns `true` if columns starts with prefix string.

[**REPLACE(col, find, substitute)**](https://docs.pinot.apache.org/functions-1/replace)\
replace all instances of `find` with `replace` in input

[**RPAD(col, size, pad)**](https://docs.pinot.apache.org/functions-1/rpad)\
string padded from the right side with `pad` to reach final `size`

[**LPAD(col, size, pad)**](https://docs.pinot.apache.org/functions-1/lpad)\
string padded from the left side with `pad` to reach final `size`

[**CODEPOINT(col)**](https://docs.pinot.apache.org/functions-1/codepoint)\
the Unicode codepoint of the first character of the string

[**CHR(codepoint)**](https://docs.pinot.apache.org/functions-1/chr)\
the character corresponding to the Unicode codepoint

[**regexpExtract(value, regexp)**](https://docs.pinot.apache.org/functions-1/regexpextract)\
Extracts values that match the provided regular expression

[**regexpReplace(input, matchRegexp, replaceRegexp, matchStartPos, occurrence, flag)**<br>](https://docs.pinot.apache.org/functions-1/regexpreplace)Find and replace a string or regexp pattern with a target string or regexp pattern

[**remove(input, search)**](https://docs.pinot.apache.org/functions-1/remove)\
removes all instances of search from string

[**urlEncoding(string)**](https://docs.pinot.apache.org/functions-1/url)\
url-encode a string with UTF-8 format

[**urlDecoding(string)**](https://docs.pinot.apache.org/functions-1/url)\
decode a url to plaintext string

[**fromBase64(string)**](https://docs.pinot.apache.org/functions-1/base64)\
decode a Base64-encoded string to bytes represented as a hex string

[**toUtf8(string)**](https://docs.pinot.apache.org/functions-1/utf8)\
decode a UTF8-encoded string to bytes represented as a hex string

[**isSubnetOf(ipPrefix, ipAddress)**](https://docs.pinot.apache.org/functions-1/issubnetof)\
checks if ipAddress is in the subnet of the ipPrefix
