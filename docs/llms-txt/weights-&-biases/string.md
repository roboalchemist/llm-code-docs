# Source: https://docs.wandb.ai/models/ref/query-panel/string.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# string

## Chainable Ops

### <a id="string-notEqual" />`string-notEqual`

Determines inequality of two values.

| Argument | Description                  |
| :------- | :--------------------------- |
| `lhs`    | The first value to compare.  |
| `rhs`    | The second value to compare. |

#### Return Value

Whether the two values are not equal.

### <a id="string-add" />`string-add`

Concatenates two [strings](/models/ref/query-panel/string/)

| Argument | Description                                         |
| :------- | :-------------------------------------------------- |
| `lhs`    | The first [string](/models/ref/query-panel/string)  |
| `rhs`    | The second [string](/models/ref/query-panel/string) |

#### Return Value

The concatenated [string](/models/ref/query-panel/string)

### <a id="string-equal" />`string-equal`

Determines equality of two values.

| Argument | Description                  |
| :------- | :--------------------------- |
| `lhs`    | The first value to compare.  |
| `rhs`    | The second value to compare. |

#### Return Value

Whether the two values are equal.

### <a id="string-append" />`string-append`

Appends a suffix to a [string](/models/ref/query-panel/string)

| Argument | Description                                               |
| :------- | :-------------------------------------------------------- |
| `str`    | The [string](/models/ref/query-panel/string) to append to |
| `suffix` | The suffix to append                                      |

#### Return Value

The [string](/models/ref/query-panel/string) with the suffix appended

### <a id="string-contains" />`string-contains`

Checks if a [string](/models/ref/query-panel/string) contains a substring

| Argument | Description                                           |
| :------- | :---------------------------------------------------- |
| `str`    | The [string](/models/ref/query-panel/string) to check |
| `sub`    | The substring to check for                            |

#### Return Value

Whether the [string](/models/ref/query-panel/string) contains the substring

### <a id="string-endsWith" />`string-endsWith`

Checks if a [string](/models/ref/query-panel/string) ends with a suffix

| Argument | Description                                           |
| :------- | :---------------------------------------------------- |
| `str`    | The [string](/models/ref/query-panel/string) to check |
| `suffix` | The suffix to check for                               |

#### Return Value

Whether the [string](/models/ref/query-panel/string) ends with the suffix

### <a id="string-findAll" />`string-findAll`

Finds all occurrences of a substring in a [string](/models/ref/query-panel/string)

| Argument | Description                                                                          |
| :------- | :----------------------------------------------------------------------------------- |
| `str`    | The [string](/models/ref/query-panel/string) to find occurrences of the substring in |
| `sub`    | The substring to find                                                                |

#### Return Value

The *list* of indices of the substring in the [string](/models/ref/query-panel/string)

### <a id="string-isAlnum" />`string-isAlnum`

Checks if a [string](/models/ref/query-panel/string) is alphanumeric

| Argument | Description                                           |
| :------- | :---------------------------------------------------- |
| `str`    | The [string](/models/ref/query-panel/string) to check |

#### Return Value

Whether the [string](/models/ref/query-panel/string) is alphanumeric

### <a id="string-isAlpha" />`string-isAlpha`

Checks if a [string](/models/ref/query-panel/string) is alphabetic

| Argument | Description                                           |
| :------- | :---------------------------------------------------- |
| `str`    | The [string](/models/ref/query-panel/string) to check |

#### Return Value

Whether the [string](/models/ref/query-panel/string) is alphabetic

### <a id="string-isNumeric" />`string-isNumeric`

Checks if a [string](/models/ref/query-panel/string) is numeric

| Argument | Description                                           |
| :------- | :---------------------------------------------------- |
| `str`    | The [string](/models/ref/query-panel/string) to check |

#### Return Value

Whether the [string](/models/ref/query-panel/string) is numeric

### <a id="string-lStrip" />`string-lStrip`

Strip leading whitespace

| Argument | Description                                            |
| :------- | :----------------------------------------------------- |
| `str`    | The [string](/models/ref/query-panel/string) to strip. |

#### Return Value

The stripped [string](/models/ref/query-panel/string).

### <a id="string-len" />`string-len`

Returns the length of a [string](/models/ref/query-panel/string)

| Argument | Description                                           |
| :------- | :---------------------------------------------------- |
| `str`    | The [string](/models/ref/query-panel/string) to check |

#### Return Value

The length of the [string](/models/ref/query-panel/string)

### <a id="string-lower" />`string-lower`

Converts a [string](/models/ref/query-panel/string) to lowercase

| Argument | Description                                                          |
| :------- | :------------------------------------------------------------------- |
| `str`    | The [string](/models/ref/query-panel/string) to convert to lowercase |

#### Return Value

The lowercase [string](/models/ref/query-panel/string)

### <a id="string-partition" />`string-partition`

Partitions a [string](/models/ref/query-panel/string) into a *list* of the [strings](/models/ref/query-panel/string/)

| Argument | Description                                           |
| :------- | :---------------------------------------------------- |
| `str`    | The [string](/models/ref/query-panel/string) to split |
| `sep`    | The separator to split on                             |

#### Return Value

A *list* of [strings](/models/ref/query-panel/string/): the [string](/models/ref/query-panel/string) before the separator, the separator, and the [string](/models/ref/query-panel/string) after the separator

### <a id="string-prepend" />`string-prepend`

Prepends a prefix to a [string](/models/ref/query-panel/string)

| Argument | Description                                                |
| :------- | :--------------------------------------------------------- |
| `str`    | The [string](/models/ref/query-panel/string) to prepend to |
| `prefix` | The prefix to prepend                                      |

#### Return Value

The [string](/models/ref/query-panel/string) with the prefix prepended

### <a id="string-rStrip" />`string-rStrip`

Strip trailing whitespace

| Argument | Description                                            |
| :------- | :----------------------------------------------------- |
| `str`    | The [string](/models/ref/query-panel/string) to strip. |

#### Return Value

The stripped [string](/models/ref/query-panel/string).

### <a id="string-replace" />`string-replace`

Replaces all occurrences of a substring in a [string](/models/ref/query-panel/string)

| Argument | Description                                                         |
| :------- | :------------------------------------------------------------------ |
| `str`    | The [string](/models/ref/query-panel/string) to replace contents of |
| `sub`    | The substring to replace                                            |
| `newSub` | The substring to replace the old substring with                     |

#### Return Value

The [string](/models/ref/query-panel/string) with the replacements

### <a id="string-slice" />`string-slice`

Slices a [string](/models/ref/query-panel/string) into a substring based on beginning and end indices

| Argument | Description                                           |
| :------- | :---------------------------------------------------- |
| `str`    | The [string](/models/ref/query-panel/string) to slice |
| `begin`  | The beginning index of the substring                  |
| `end`    | The ending index of the substring                     |

#### Return Value

The substring

### <a id="string-split" />`string-split`

Splits a [string](/models/ref/query-panel/string) into a *list* of [strings](/models/ref/query-panel/string/)

| Argument | Description                                           |
| :------- | :---------------------------------------------------- |
| `str`    | The [string](/models/ref/query-panel/string) to split |
| `sep`    | The separator to split on                             |

#### Return Value

The *list* of [strings](/models/ref/query-panel/string/)

### <a id="string-startsWith" />`string-startsWith`

Checks if a [string](/models/ref/query-panel/string) starts with a prefix

| Argument | Description                                           |
| :------- | :---------------------------------------------------- |
| `str`    | The [string](/models/ref/query-panel/string) to check |
| `prefix` | The prefix to check for                               |

#### Return Value

Whether the [string](/models/ref/query-panel/string) starts with the prefix

### <a id="string-strip" />`string-strip`

Strip whitespace from both ends of a [string](/models/ref/query-panel/string).

| Argument | Description                                            |
| :------- | :----------------------------------------------------- |
| `str`    | The [string](/models/ref/query-panel/string) to strip. |

#### Return Value

The stripped [string](/models/ref/query-panel/string).

### <a id="string-upper" />`string-upper`

Converts a [string](/models/ref/query-panel/string) to uppercase

| Argument | Description                                                          |
| :------- | :------------------------------------------------------------------- |
| `str`    | The [string](/models/ref/query-panel/string) to convert to uppercase |

#### Return Value

The uppercase [string](/models/ref/query-panel/string)

### <a id="string-levenshtein" />`string-levenshtein`

Calculates the Levenshtein distance between two [strings](/models/ref/query-panel/string/).

| Argument | Description                                          |
| :------- | :--------------------------------------------------- |
| `str1`   | The first [string](/models/ref/query-panel/string).  |
| `str2`   | The second [string](/models/ref/query-panel/string). |

#### Return Value

The Levenshtein distance between the two [strings](/models/ref/query-panel/string/).

## List Ops

### <a id="string-notEqual" />`string-notEqual`

Determines inequality of two values.

| Argument | Description                  |
| :------- | :--------------------------- |
| `lhs`    | The first value to compare.  |
| `rhs`    | The second value to compare. |

#### Return Value

Whether the two values are not equal.

### <a id="string-add" />`string-add`

Concatenates two [strings](/models/ref/query-panel/string/)

| Argument | Description                                         |
| :------- | :-------------------------------------------------- |
| `lhs`    | The first [string](/models/ref/query-panel/string)  |
| `rhs`    | The second [string](/models/ref/query-panel/string) |

#### Return Value

The concatenated [string](/models/ref/query-panel/string)

### <a id="string-equal" />`string-equal`

Determines equality of two values.

| Argument | Description                  |
| :------- | :--------------------------- |
| `lhs`    | The first value to compare.  |
| `rhs`    | The second value to compare. |

#### Return Value

Whether the two values are equal.

### <a id="string-append" />`string-append`

Appends a suffix to a [string](/models/ref/query-panel/string)

| Argument | Description                                               |
| :------- | :-------------------------------------------------------- |
| `str`    | The [string](/models/ref/query-panel/string) to append to |
| `suffix` | The suffix to append                                      |

#### Return Value

The [string](/models/ref/query-panel/string) with the suffix appended

### <a id="string-contains" />`string-contains`

Checks if a [string](/models/ref/query-panel/string) contains a substring

| Argument | Description                                           |
| :------- | :---------------------------------------------------- |
| `str`    | The [string](/models/ref/query-panel/string) to check |
| `sub`    | The substring to check for                            |

#### Return Value

Whether the [string](/models/ref/query-panel/string) contains the substring

### <a id="string-endsWith" />`string-endsWith`

Checks if a [string](/models/ref/query-panel/string) ends with a suffix

| Argument | Description                                           |
| :------- | :---------------------------------------------------- |
| `str`    | The [string](/models/ref/query-panel/string) to check |
| `suffix` | The suffix to check for                               |

#### Return Value

Whether the [string](/models/ref/query-panel/string) ends with the suffix

### <a id="string-findAll" />`string-findAll`

Finds all occurrences of a substring in a [string](/models/ref/query-panel/string)

| Argument | Description                                                                          |
| :------- | :----------------------------------------------------------------------------------- |
| `str`    | The [string](/models/ref/query-panel/string) to find occurrences of the substring in |
| `sub`    | The substring to find                                                                |

#### Return Value

The *list* of indices of the substring in the [string](/models/ref/query-panel/string)

### <a id="string-isAlnum" />`string-isAlnum`

Checks if a [string](/models/ref/query-panel/string) is alphanumeric

| Argument | Description                                           |
| :------- | :---------------------------------------------------- |
| `str`    | The [string](/models/ref/query-panel/string) to check |

#### Return Value

Whether the [string](/models/ref/query-panel/string) is alphanumeric

### <a id="string-isAlpha" />`string-isAlpha`

Checks if a [string](/models/ref/query-panel/string) is alphabetic

| Argument | Description                                           |
| :------- | :---------------------------------------------------- |
| `str`    | The [string](/models/ref/query-panel/string) to check |

#### Return Value

Whether the [string](/models/ref/query-panel/string) is alphabetic

### <a id="string-isNumeric" />`string-isNumeric`

Checks if a [string](/models/ref/query-panel/string) is numeric

| Argument | Description                                           |
| :------- | :---------------------------------------------------- |
| `str`    | The [string](/models/ref/query-panel/string) to check |

#### Return Value

Whether the [string](/models/ref/query-panel/string) is numeric

### <a id="string-lStrip" />`string-lStrip`

Strip leading whitespace

| Argument | Description                                            |
| :------- | :----------------------------------------------------- |
| `str`    | The [string](/models/ref/query-panel/string) to strip. |

#### Return Value

The stripped [string](/models/ref/query-panel/string).

### <a id="string-len" />`string-len`

Returns the length of a [string](/models/ref/query-panel/string)

| Argument | Description                                           |
| :------- | :---------------------------------------------------- |
| `str`    | The [string](/models/ref/query-panel/string) to check |

#### Return Value

The length of the [string](/models/ref/query-panel/string)

### <a id="string-lower" />`string-lower`

Converts a [string](/models/ref/query-panel/string) to lowercase

| Argument | Description                                                          |
| :------- | :------------------------------------------------------------------- |
| `str`    | The [string](/models/ref/query-panel/string) to convert to lowercase |

#### Return Value

The lowercase [string](/models/ref/query-panel/string)

### <a id="string-partition" />`string-partition`

Partitions a [string](/models/ref/query-panel/string) into a *list* of the [strings](/models/ref/query-panel/string/)

| Argument | Description                                           |
| :------- | :---------------------------------------------------- |
| `str`    | The [string](/models/ref/query-panel/string) to split |
| `sep`    | The separator to split on                             |

#### Return Value

A *list* of [strings](/models/ref/query-panel/string/): the [string](/models/ref/query-panel/string) before the separator, the separator, and the [string](/models/ref/query-panel/string) after the separator

### <a id="string-prepend" />`string-prepend`

Prepends a prefix to a [string](/models/ref/query-panel/string)

| Argument | Description                                                |
| :------- | :--------------------------------------------------------- |
| `str`    | The [string](/models/ref/query-panel/string) to prepend to |
| `prefix` | The prefix to prepend                                      |

#### Return Value

The [string](/models/ref/query-panel/string) with the prefix prepended

### <a id="string-rStrip" />`string-rStrip`

Strip trailing whitespace

| Argument | Description                                            |
| :------- | :----------------------------------------------------- |
| `str`    | The [string](/models/ref/query-panel/string) to strip. |

#### Return Value

The stripped [string](/models/ref/query-panel/string).

### <a id="string-replace" />`string-replace`

Replaces all occurrences of a substring in a [string](/models/ref/query-panel/string)

| Argument | Description                                                         |
| :------- | :------------------------------------------------------------------ |
| `str`    | The [string](/models/ref/query-panel/string) to replace contents of |
| `sub`    | The substring to replace                                            |
| `newSub` | The substring to replace the old substring with                     |

#### Return Value

The [string](/models/ref/query-panel/string) with the replacements

### <a id="string-slice" />`string-slice`

Slices a [string](/models/ref/query-panel/string) into a substring based on beginning and end indices

| Argument | Description                                           |
| :------- | :---------------------------------------------------- |
| `str`    | The [string](/models/ref/query-panel/string) to slice |
| `begin`  | The beginning index of the substring                  |
| `end`    | The ending index of the substring                     |

#### Return Value

The substring

### <a id="string-split" />`string-split`

Splits a [string](/models/ref/query-panel/string) into a *list* of [strings](/models/ref/query-panel/string/)

| Argument | Description                                           |
| :------- | :---------------------------------------------------- |
| `str`    | The [string](/models/ref/query-panel/string) to split |
| `sep`    | The separator to split on                             |

#### Return Value

The *list* of [strings](/models/ref/query-panel/string/)

### <a id="string-startsWith" />`string-startsWith`

Checks if a [string](/models/ref/query-panel/string) starts with a prefix

| Argument | Description                                           |
| :------- | :---------------------------------------------------- |
| `str`    | The [string](/models/ref/query-panel/string) to check |
| `prefix` | The prefix to check for                               |

#### Return Value

Whether the [string](/models/ref/query-panel/string) starts with the prefix

### <a id="string-strip" />`string-strip`

Strip whitespace from both ends of a [string](/models/ref/query-panel/string).

| Argument | Description                                            |
| :------- | :----------------------------------------------------- |
| `str`    | The [string](/models/ref/query-panel/string) to strip. |

#### Return Value

The stripped [string](/models/ref/query-panel/string).

### <a id="string-upper" />`string-upper`

Converts a [string](/models/ref/query-panel/string) to uppercase

| Argument | Description                                                          |
| :------- | :------------------------------------------------------------------- |
| `str`    | The [string](/models/ref/query-panel/string) to convert to uppercase |

#### Return Value

The uppercase [string](/models/ref/query-panel/string)

### <a id="string-levenshtein" />`string-levenshtein`

Calculates the Levenshtein distance between two [strings](/models/ref/query-panel/string/).

| Argument | Description                                          |
| :------- | :--------------------------------------------------- |
| `str1`   | The first [string](/models/ref/query-panel/string).  |
| `str2`   | The second [string](/models/ref/query-panel/string). |

#### Return Value

The Levenshtein distance between the two [strings](/models/ref/query-panel/string/).
