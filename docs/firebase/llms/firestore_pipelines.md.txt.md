# Source: https://firebase.google.com/docs/reference/js/firestore_pipelines.md.txt

# @firebase/firestore/pipelines

## Functions

| Function | Description |
|---|---|
| **function()** |   |
| [countAll()](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#countall) | ***(Public Preview)*** Creates an aggregation that counts the total number of stage inputs. |
| [currentTimestamp()](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#currenttimestamp) | ***(Public Preview)*** Creates an expression that evaluates to the current server timestamp. |
| [rand()](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#rand) | ***(Public Preview)*** Creates an expression that generates a random number between 0.0 and 1.0 but not including 1.0. |
| **function(array, ...)** |   |
| [arrayContains(array, element)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#arraycontains_a00ea48) | ***(Public Preview)*** Creates an expression that checks if an array expression contains a specific element. |
| [arrayContains(array, element)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#arraycontains_7328608) | ***(Public Preview)*** Creates an expression that checks if an array expression contains a specific element. |
| [arrayContainsAll(array, values)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#arraycontainsall_c658ad5) | ***(Public Preview)*** Creates an expression that checks if an array expression contains all the specified elements. |
| [arrayContainsAll(array, arrayExpression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#arraycontainsall_7b535db) | ***(Public Preview)*** Creates an expression that checks if an array expression contains all the specified elements. |
| [arrayContainsAny(array, values)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#arraycontainsany_c658ad5) | ***(Public Preview)*** Creates an expression that checks if an array expression contains any of the specified elements. |
| [arrayContainsAny(array, values)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#arraycontainsany_c381a96) | ***(Public Preview)*** Creates an expression that checks if an array expression contains any of the specified elements. |
| [arrayLength(array)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#arraylength_195e339) | ***(Public Preview)*** Creates an expression that calculates the length of an array expression. |
| **function(arrayExpression, ...)** |   |
| [arrayGet(arrayExpression, offset)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#arrayget_f2e27cc) | ***(Public Preview)*** Creates an expression that indexes into an array from the beginning or end and return the element. If the offset exceeds the array length, an error is returned. A negative offset, starts from the end. |
| [arrayGet(arrayExpression, offsetExpr)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#arrayget_484550d) | ***(Public Preview)*** Creates an expression that indexes into an array from the beginning or end and return the element. If the offset exceeds the array length, an error is returned. A negative offset, starts from the end. |
| [join(arrayExpression, delimiterExpression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#join_313e6aa) | ***(Public Preview)*** Creates an expression that joins the elements of an array into a string. |
| [join(arrayExpression, delimiter)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#join_d088d29) | ***(Public Preview)*** Creates an expression that joins the elements of an array into a string. |
| **function(arrayField, ...)** |   |
| [arrayGet(arrayField, offset)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#arrayget_3f58471) | ***(Public Preview)*** Creates an expression that indexes into an array from the beginning or end and return the element. If the offset exceeds the array length, an error is returned. A negative offset, starts from the end. |
| [arrayGet(arrayField, offsetExpr)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#arrayget_1904c9a) | ***(Public Preview)*** Creates an expression that indexes into an array from the beginning or end and return the element. If the offset exceeds the array length, an error is returned. A negative offset, starts from the end. |
| **function(arrayFieldName, ...)** |   |
| [join(arrayFieldName, delimiter)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#join_478ef36) | ***(Public Preview)*** Creates an expression that joins the elements of an array into a string. |
| [join(arrayFieldName, delimiterExpression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#join_829294c) | ***(Public Preview)*** Creates an expression that joins the elements of an array into a string. |
| **function(base, ...)** |   |
| [pow(base, exponent)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#pow_e4a9e64) | ***(Public Preview)*** Creates an expression that returns the value of the base expression raised to the power of the exponent expression. |
| [pow(base, exponent)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#pow_93eae7f) | ***(Public Preview)*** Creates an expression that returns the value of the base expression raised to the power of the exponent. |
| [pow(base, exponent)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#pow_a237721) | ***(Public Preview)*** Creates an expression that returns the value of the base field raised to the power of the exponent expression. |
| [pow(base, exponent)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#pow_f4d7908) | ***(Public Preview)*** Creates an expression that returns the value of the base field raised to the power of the exponent. |
| **function(booleanExpr, ...)** |   |
| [countIf(booleanExpr)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#countif_c5b8fb1) | ***(Public Preview)*** Creates an aggregation that counts the number of stage inputs where the provided boolean expression evaluates to true. |
| [not(booleanExpr)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#not_c5b8fb1) | ***(Public Preview)*** Creates an expression that negates a filter condition. |
| **function(condition, ...)** |   |
| [conditional(condition, thenExpr, elseExpr)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#conditional_07a206d) | ***(Public Preview)*** Creates a conditional expression that evaluates to a 'then' expression if a condition is true and an 'else' expression if the condition is false. |
| **function(documentPath, ...)** |   |
| [documentId(documentPath)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#documentid_cef293c) | ***(Public Preview)*** Creates an expression that returns the document ID from a path. |
| **function(documentPathExpr, ...)** |   |
| [documentId(documentPathExpr)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#documentid_9a69021) | ***(Public Preview)*** Creates an expression that returns the document ID from a path. |
| **function(element, ...)** |   |
| [notEqualAny(element, values)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#notequalany_c2c5bcb) | ***(Public Preview)*** Creates an expression that checks if an expression is not equal to any of the provided values or expressions. |
| [notEqualAny(element, arrayExpression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#notequalany_16b2851) | ***(Public Preview)*** Creates an expression that checks if an expression is not equal to any of the provided values or expressions. |
| **function(elements, ...)** |   |
| [array(elements)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#array_7d853aa) | ***(Public Preview)*** Creates an expression that creates a Firestore array value from an input array. |
| [map(elements)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#map_ce5dee1) | ***(Public Preview)*** Creates an expression that creates a Firestore map value from an input object. |
| **function(expr, ...)** |   |
| [abs(expr)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#abs_005f3d4) | ***(Public Preview)*** Creates an expression that computes the absolute value of a numeric value. |
| [ascending(expr)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#ascending_005f3d4) | ***(Public Preview)*** Creates an [Ordering](https://firebase.google.com/docs/reference/js/firestore_pipelines.ordering.md#ordering_class) that sorts documents in ascending order based on an expression. |
| [byteLength(expr)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#bytelength_005f3d4) | ***(Public Preview)*** Creates an expression that calculates the byte length of a string in UTF-8, or just the length of a Blob. |
| [countDistinct(expr)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#countdistinct_3c28b08) | ***(Public Preview)*** Creates an aggregation that counts the number of distinct values of a field. |
| [descending(expr)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#descending_005f3d4) | ***(Public Preview)*** Creates an [Ordering](https://firebase.google.com/docs/reference/js/firestore_pipelines.ordering.md#ordering_class) that sorts documents in descending order based on an expression. |
| [floor(expr)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#floor_005f3d4) | ***(Public Preview)*** Creates an expression that computes the floor of a numeric value. |
| [timestampToUnixMicros(expr)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#timestamptounixmicros_005f3d4) | ***(Public Preview)*** Creates an expression that converts a timestamp expression to the number of microseconds since the Unix epoch (1970-01-01 00:00:00 UTC). |
| [timestampToUnixMillis(expr)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#timestamptounixmillis_005f3d4) | ***(Public Preview)*** Creates an expression that converts a timestamp expression to the number of milliseconds since the Unix epoch (1970-01-01 00:00:00 UTC). |
| [timestampToUnixSeconds(expr)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#timestamptounixseconds_005f3d4) | ***(Public Preview)*** Creates an expression that converts a timestamp expression to the number of seconds since the Unix epoch (1970-01-01 00:00:00 UTC). |
| [unixMicrosToTimestamp(expr)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#unixmicrostotimestamp_005f3d4) | ***(Public Preview)*** Creates an expression that interprets an expression as the number of microseconds since the Unix epoch (1970-01-01 00:00:00 UTC) and returns a timestamp. |
| [unixMillisToTimestamp(expr)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#unixmillistotimestamp_005f3d4) | ***(Public Preview)*** Creates an expression that interprets an expression as the number of milliseconds since the Unix epoch (1970-01-01 00:00:00 UTC) and returns a timestamp. |
| [unixSecondsToTimestamp(expr)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#unixsecondstotimestamp_005f3d4) | ***(Public Preview)*** Creates an expression that interprets an expression as the number of seconds since the Unix epoch (1970-01-01 00:00:00 UTC) and returns a timestamp. |
| **function(expression, ...)** |   |
| [arrayAgg(expression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#arrayagg_1138a27) | ***(Public Preview)*** Creates an aggregation that collects all values of an expression across multiple stage inputs into an array. |
| [arrayAggDistinct(expression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#arrayaggdistinct_1138a27) | ***(Public Preview)*** Creates an aggregation that collects all distinct values of an expression across multiple stage inputs into an array. |
| [arraySum(expression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#arraysum_1138a27) | ***(Public Preview)*** Creates an expression that computes the sum of the elements in an array. |
| [average(expression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#average_1138a27) | ***(Public Preview)*** Creates an aggregation that calculates the average (mean) of values from an expression across multiple stage inputs. |
| [ceil(expression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#ceil_1138a27) | ***(Public Preview)*** Creates an expression that computes the ceiling of a numeric value. |
| [collectionId(expression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#collectionid_1138a27) | ***(Public Preview)*** Creates an expression that returns the collection ID from a path. |
| [count(expression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#count_1138a27) | ***(Public Preview)*** Creates an aggregation that counts the number of stage inputs with valid evaluations of the provided expression. |
| [divide(expression, value)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#divide_01df3cf) | ***(Public Preview)*** Creates an expression that divides an expression by a constant value. |
| [equal(expression, value)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#equal_01df3cf) | ***(Public Preview)*** Creates an expression that checks if an expression is equal to a constant value. |
| [equalAny(expression, values)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#equalany_7e759b5) | ***(Public Preview)*** Creates an expression that checks if an expression, when evaluated, is equal to any of the provided values or expressions. |
| [equalAny(expression, arrayExpression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#equalany_214ce68) | ***(Public Preview)*** Creates an expression that checks if an expression is equal to any of the provided values. |
| [exp(expression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#exp_1138a27) | ***(Public Preview)*** Creates an expression that computes e to the power of the expression's result. |
| [first(expression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#first_1138a27) | ***(Public Preview)*** Creates an aggregation that finds the first value of an expression across multiple stage inputs. |
| [greaterThan(expression, value)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#greaterthan_01df3cf) | ***(Public Preview)*** Creates an expression that checks if an expression is greater than a constant value. |
| [greaterThanOrEqual(expression, value)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#greaterthanorequal_01df3cf) | ***(Public Preview)*** Creates an expression that checks if an expression is greater than or equal to a constant value. |
| [isType(expression, type)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#istype_27398ce) | ***(Public Preview)*** Creates an expression that checks if the result of an expression is of the given type. |
| [last(expression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#last_1138a27) | ***(Public Preview)*** Creates an aggregation that finds the last value of an expression across multiple stage inputs. |
| [length_2(expression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#length_2_1138a27) | ***(Public Preview)*** Creates an expression that calculates the length of a string, array, map, vector, or bytes. |
| [lessThan(expression, value)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#lessthan_01df3cf) | ***(Public Preview)*** Creates an expression that checks if an expression is less than a constant value. |
| [lessThanOrEqual(expression, value)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#lessthanorequal_01df3cf) | ***(Public Preview)*** Creates an expression that checks if an expression is less than or equal to a constant value. |
| [ln(expression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#ln_1138a27) | ***(Public Preview)*** Creates an expression that computes the natural logarithm of a numeric value. |
| [log(expression, base)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#log_ac183e2) | ***(Public Preview)*** Creates an expression that computes the logarithm of an expression to a given base. |
| [log(expression, base)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#log_1894737) | ***(Public Preview)*** Creates an expression that computes the logarithm of an expression to a given base. |
| [log10(expression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#log10_1138a27) | ***(Public Preview)*** Creates an expression that computes the base-10 logarithm of a numeric value. |
| [ltrim(expression, valueToTrim)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#ltrim_775e2f2) | ***(Public Preview)*** Trims whitespace or a specified set of characters/bytes from the beginning of a string or byte array. |
| [maximum(expression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#maximum_1138a27) | ***(Public Preview)*** Creates an aggregation that finds the maximum value of an expression across multiple stage inputs. |
| [minimum(expression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#minimum_1138a27) | ***(Public Preview)*** Creates an aggregation that finds the minimum value of an expression across multiple stage inputs. |
| [mod(expression, value)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#mod_01df3cf) | ***(Public Preview)*** Creates an expression that calculates the modulo (remainder) of dividing an expression by a constant. |
| [notEqual(expression, value)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#notequal_01df3cf) | ***(Public Preview)*** Creates an expression that checks if an expression is not equal to a constant value. |
| [round(expression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#round_1138a27) | ***(Public Preview)*** Creates an expression that rounds a numeric value to the nearest whole number. |
| [round(expression, decimalPlaces)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#round_a3a92d0) | ***(Public Preview)*** Creates an expression that rounds a numeric value to the specified number of decimal places. |
| [rtrim(expression, valueToTrim)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#rtrim_775e2f2) | ***(Public Preview)*** Trims whitespace or a specified set of characters/bytes from the end of a string or byte array. |
| [split(expression, delimiter)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#split_5b5612b) | ***(Public Preview)*** Creates an expression that splits a string into an array of substrings based on the provided delimiter. |
| [split(expression, delimiter)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#split_5a171ed) | ***(Public Preview)*** Creates an expression that splits a string into an array of substrings based on the provided delimiter. |
| [sqrt(expression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#sqrt_1138a27) | ***(Public Preview)*** Creates an expression that computes the square root of a numeric value. |
| [stringIndexOf(expression, search)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#stringindexof_6dfca5f) | ***(Public Preview)*** Creates an expression that finds the index of the first occurrence of a substring or byte sequence. |
| [stringRepeat(expression, repetitions)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#stringrepeat_a55ba16) | ***(Public Preview)*** Creates an expression that repeats a string or byte array a specified number of times. |
| [stringReplaceAll(expression, find, replacement)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#stringreplaceall_197ecbe) | ***(Public Preview)*** Creates an expression that replaces all occurrences of a substring or byte sequence with a replacement. |
| [stringReplaceOne(expression, find, replacement)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#stringreplaceone_197ecbe) | ***(Public Preview)*** Creates an expression that replaces the first occurrence of a substring or byte sequence with a replacement. |
| [subtract(expression, value)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#subtract_01df3cf) | ***(Public Preview)*** Creates an expression that subtracts a constant value from an expression. |
| [sum(expression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#sum_1138a27) | ***(Public Preview)*** Creates an aggregation that calculates the sum of values from an expression across multiple stage inputs. |
| [trunc(expression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#trunc_1138a27) | ***(Public Preview)*** Creates an expression that truncates the numeric value of an expression to an integer. |
| [trunc(expression, decimalPlaces)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#trunc_a3a92d0) | ***(Public Preview)*** Creates an expression that truncates a numeric value to the specified number of decimal places. |
| [type(expression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#type_1138a27) | ***(Public Preview)*** Creates an expression that returns the data type of an expression's result. |
| **function(field, ...)** |   |
| [isAbsent(field)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#isabsent_0fb8cd4) | ***(Public Preview)*** Creates an expression that returns `true` if a field is absent. Otherwise, returns `false` even if the field value is `null`. |
| [reverse(field)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#reverse_0fb8cd4) | ***(Public Preview)*** Creates an expression that reverses a string value in the specified field. |
| [stringReverse(field)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#stringreverse_0fb8cd4) | ***(Public Preview)*** Creates an expression that reverses a string value in the specified field. |
| [substring(field, position, length)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#substring_0d9573a) | ***(Public Preview)*** Creates an expression that returns a substring of a string or byte array. |
| [substring(field, position, length)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#substring_05cb14e) | ***(Public Preview)*** Creates an expression that returns a substring of a string or byte array. |
| **function(fieldName, ...)** |   |
| [abs(fieldName)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#abs_e5b0480) | ***(Public Preview)*** Creates an expression that computes the absolute value of a numeric value. |
| [add(fieldName, second)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#add_b75bb8b) | ***(Public Preview)*** Creates an expression that adds a field's value to an expression. |
| [arrayAgg(fieldName)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#arrayagg_e5b0480) | ***(Public Preview)*** Creates an aggregation that collects all values of a field across multiple stage inputs into an array. |
| [arrayAggDistinct(fieldName)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#arrayaggdistinct_e5b0480) | ***(Public Preview)*** Creates an aggregation that collects all distinct values of a field across multiple stage inputs into an array. |
| [arrayContains(fieldName, element)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#arraycontains_aaace4a) | ***(Public Preview)*** Creates an expression that checks if a field's array value contains a specific element. |
| [arrayContains(fieldName, element)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#arraycontains_999590f) | ***(Public Preview)*** Creates an expression that checks if a field's array value contains a specific value. |
| [arrayContainsAll(fieldName, values)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#arraycontainsall_8060b23) | ***(Public Preview)*** Creates an expression that checks if a field's array value contains all the specified values or expressions. |
| [arrayContainsAll(fieldName, arrayExpression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#arraycontainsall_48da8d9) | ***(Public Preview)*** Creates an expression that checks if a field's array value contains all the specified values or expressions. |
| [arrayContainsAny(fieldName, values)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#arraycontainsany_8060b23) | ***(Public Preview)*** Creates an expression that checks if a field's array value contains any of the specified elements. |
| [arrayContainsAny(fieldName, values)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#arraycontainsany_1b4f7cd) | ***(Public Preview)*** Creates an expression that checks if a field's array value contains any of the specified elements. |
| [arrayLength(fieldName)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#arraylength_e5b0480) | ***(Public Preview)*** Creates an expression that calculates the length of an array in a specified field. |
| [arraySum(fieldName)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#arraysum_e5b0480) | ***(Public Preview)*** Creates an expression that computes the sum of the elements in an array. |
| [ascending(fieldName)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#ascending_e5b0480) | ***(Public Preview)*** Creates an [Ordering](https://firebase.google.com/docs/reference/js/firestore_pipelines.ordering.md#ordering_class) that sorts documents in ascending order based on a field. |
| [average(fieldName)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#average_e5b0480) | ***(Public Preview)*** Creates an aggregation that calculates the average (mean) of a field's values across multiple stage inputs. |
| [byteLength(fieldName)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#bytelength_e5b0480) | ***(Public Preview)*** Creates an expression that calculates the length of a string represented by a field in UTF-8 bytes, or just the length of a Blob. |
| [ceil(fieldName)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#ceil_e5b0480) | ***(Public Preview)*** Creates an expression that computes the ceiling of a numeric value. |
| [charLength(fieldName)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#charlength_e5b0480) | ***(Public Preview)*** Creates an expression that calculates the character length of a string field in UTF8. |
| [collectionId(fieldName)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#collectionid_e5b0480) | ***(Public Preview)*** Creates an expression that returns the collection ID from a path. |
| [concat(fieldName, second, others)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#concat_828272e) | ***(Public Preview)*** Creates an expression that concatenates strings, arrays, or blobs. Types cannot be mixed. |
| [cosineDistance(fieldName, vector)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#cosinedistance_463a23e) | ***(Public Preview)*** Calculates the Cosine distance between a field's vector value and a literal vector value. |
| [cosineDistance(fieldName, vectorExpression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#cosinedistance_ed766a1) | ***(Public Preview)*** Calculates the Cosine distance between a field's vector value and a vector expression. |
| [count(fieldName)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#count_e5b0480) | ***(Public Preview)*** Creates an aggregation that counts the number of stage inputs where the input field exists. |
| [descending(fieldName)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#descending_e5b0480) | ***(Public Preview)*** Creates an [Ordering](https://firebase.google.com/docs/reference/js/firestore_pipelines.ordering.md#ordering_class) that sorts documents in descending order based on a field. |
| [divide(fieldName, expressions)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#divide_cf36e43) | ***(Public Preview)*** Creates an expression that divides a field's value by an expression. |
| [divide(fieldName, value)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#divide_65e2f32) | ***(Public Preview)*** Creates an expression that divides a field's value by a constant value. |
| [dotProduct(fieldName, vector)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#dotproduct_463a23e) | ***(Public Preview)*** Calculates the dot product between a field's vector value and a double array. |
| [dotProduct(fieldName, vectorExpression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#dotproduct_ed766a1) | ***(Public Preview)*** Calculates the dot product between a field's vector value and a vector expression. |
| [endsWith(fieldName, suffix)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#endswith_05ca3b0) | ***(Public Preview)*** Creates an expression that checks if a field's value ends with a given postfix. |
| [endsWith(fieldName, suffix)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#endswith_8fc0ebc) | ***(Public Preview)*** Creates an expression that checks if a field's value ends with a given postfix. |
| [equal(fieldName, expression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#equal_1e91657) | ***(Public Preview)*** Creates an expression that checks if a field's value is equal to an expression. |
| [equal(fieldName, value)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#equal_65e2f32) | ***(Public Preview)*** Creates an expression that checks if a field's value is equal to a constant value. |
| [equalAny(fieldName, values)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#equalany_8060b23) | ***(Public Preview)*** Creates an expression that checks if a field's value is equal to any of the provided values or expressions. |
| [equalAny(fieldName, arrayExpression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#equalany_48da8d9) | ***(Public Preview)*** Creates an expression that checks if a field's value is equal to any of the provided values or expressions. |
| [euclideanDistance(fieldName, vector)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#euclideandistance_463a23e) | ***(Public Preview)*** Calculates the Euclidean distance between a field's vector value and a double array. |
| [euclideanDistance(fieldName, vectorExpression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#euclideandistance_ed766a1) | ***(Public Preview)*** Calculates the Euclidean distance between a field's vector value and a vector expression. |
| [exists(fieldName)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#exists_e5b0480) | ***(Public Preview)*** Creates an expression that checks if a field exists. |
| [exp(fieldName)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#exp_e5b0480) | ***(Public Preview)*** Creates an expression that computes e to the power of the expression's result. |
| [first(fieldName)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#first_e5b0480) | ***(Public Preview)*** Creates an aggregation that finds the first value of a field across multiple stage inputs. |
| [floor(fieldName)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#floor_e5b0480) | ***(Public Preview)*** Creates an expression that computes the floor of a numeric value. |
| [greaterThan(fieldName, expression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#greaterthan_1e91657) | ***(Public Preview)*** Creates an expression that checks if a field's value is greater than an expression. |
| [greaterThan(fieldName, value)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#greaterthan_65e2f32) | ***(Public Preview)*** Creates an expression that checks if a field's value is greater than a constant value. |
| [greaterThanOrEqual(fieldName, value)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#greaterthanorequal_2e16acb) | ***(Public Preview)*** Creates an expression that checks if a field's value is greater than or equal to an expression. |
| [greaterThanOrEqual(fieldName, value)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#greaterthanorequal_65e2f32) | ***(Public Preview)*** Creates an expression that checks if a field's value is greater than or equal to a constant value. |
| [isType(fieldName, type)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#istype_5da287e) | ***(Public Preview)*** Creates an expression that checks if the value in the specified field is of the given type. |
| [last(fieldName)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#last_e5b0480) | ***(Public Preview)*** Creates an aggregation that finds the last value of a field across multiple stage inputs. |
| [length_2(fieldName)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#length_2_e5b0480) | ***(Public Preview)*** Creates an expression that calculates the length of a string, array, map, vector, or bytes. |
| [lessThan(fieldName, expression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#lessthan_1e91657) | ***(Public Preview)*** Creates an expression that checks if a field's value is less than an expression. |
| [lessThan(fieldName, value)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#lessthan_65e2f32) | ***(Public Preview)*** Creates an expression that checks if a field's value is less than a constant value. |
| [lessThanOrEqual(fieldName, expression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#lessthanorequal_1e91657) | ***(Public Preview)*** Creates an expression that checks if a field's value is less than or equal to an expression. |
| [lessThanOrEqual(fieldName, value)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#lessthanorequal_65e2f32) | ***(Public Preview)*** Creates an expression that checks if a field's value is less than or equal to a constant value. |
| [like(fieldName, pattern)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#like_67f7432) | ***(Public Preview)*** Creates an expression that performs a case-sensitive wildcard string comparison against a field. |
| [like(fieldName, pattern)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#like_cb1318d) | ***(Public Preview)*** Creates an expression that performs a case-sensitive wildcard string comparison against a field. |
| [ln(fieldName)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#ln_e5b0480) | ***(Public Preview)*** Creates an expression that computes the natural logarithm of a numeric value. |
| [log(fieldName, base)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#log_a89e21b) | ***(Public Preview)*** Creates an expression that computes the logarithm of a field to a given base. |
| [log(fieldName, base)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#log_805b11f) | ***(Public Preview)*** Creates an expression that computes the logarithm of a field to a given base. |
| [log10(fieldName)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#log10_e5b0480) | ***(Public Preview)*** Creates an expression that computes the base-10 logarithm of a numeric value. |
| [logicalMaximum(fieldName, second, others)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#logicalmaximum_828272e) | ***(Public Preview)*** Creates an expression that returns the largest value between multiple input expressions or literal values. Based on Firestore's value type ordering. |
| [logicalMinimum(fieldName, second, others)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#logicalminimum_828272e) | ***(Public Preview)*** Creates an expression that returns the smallest value between a field's value and other input expressions or literal values. Based on Firestore's value type ordering. |
| [ltrim(fieldName, valueToTrim)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#ltrim_c0e3211) | ***(Public Preview)*** Trims whitespace or a specified set of characters/bytes from the beginning of a string or byte array. |
| [mapGet(fieldName, subField)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#mapget_06663cf) | ***(Public Preview)*** Accesses a value from a map (object) field using the provided key. |
| [maximum(fieldName)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#maximum_e5b0480) | ***(Public Preview)*** Creates an aggregation that finds the maximum value of a field across multiple stage inputs. |
| [minimum(fieldName)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#minimum_e5b0480) | ***(Public Preview)*** Creates an aggregation that finds the minimum value of a field across multiple stage inputs. |
| [mod(fieldName, expression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#mod_1e91657) | ***(Public Preview)*** Creates an expression that calculates the modulo (remainder) of dividing a field's value by an expression. |
| [mod(fieldName, value)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#mod_65e2f32) | ***(Public Preview)*** Creates an expression that calculates the modulo (remainder) of dividing a field's value by a constant. |
| [multiply(fieldName, second)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#multiply_b75bb8b) | ***(Public Preview)*** Creates an expression that multiplies a field's value by an expression. |
| [notEqual(fieldName, expression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#notequal_1e91657) | ***(Public Preview)*** Creates an expression that checks if a field's value is not equal to an expression. |
| [notEqual(fieldName, value)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#notequal_65e2f32) | ***(Public Preview)*** Creates an expression that checks if a field's value is not equal to a constant value. |
| [notEqualAny(fieldName, values)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#notequalany_8060b23) | ***(Public Preview)*** Creates an expression that checks if a field's value is not equal to any of the provided values or expressions. |
| [notEqualAny(fieldName, arrayExpression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#notequalany_48da8d9) | ***(Public Preview)*** Creates an expression that checks if a field's value is not equal to any of the values in the evaluated expression. |
| [regexContains(fieldName, pattern)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#regexcontains_67f7432) | ***(Public Preview)*** Creates an expression that checks if a string field contains a specified regular expression as a substring. |
| [regexContains(fieldName, pattern)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#regexcontains_cb1318d) | ***(Public Preview)*** Creates an expression that checks if a string field contains a specified regular expression as a substring. |
| [regexFind(fieldName, pattern)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#regexfind_67f7432) | ***(Public Preview)*** Creates an expression that returns the first substring of a string field that matches a specified regular expression.This expression uses the [RE2](https://github.com/google/re2/wiki/Syntax) regular expression syntax. |
| [regexFind(fieldName, pattern)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#regexfind_cb1318d) | ***(Public Preview)*** Creates an expression that returns the first substring of a string field that matches a specified regular expression.This expression uses the [RE2](https://github.com/google/re2/wiki/Syntax) regular expression syntax. |
| [regexFindAll(fieldName, pattern)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#regexfindall_67f7432) | ***(Public Preview)*** Creates an expression that evaluates to a list of all substrings in a string field that match a specified regular expression.This expression uses the [RE2](https://github.com/google/re2/wiki/Syntax) regular expression syntax. |
| [regexFindAll(fieldName, pattern)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#regexfindall_cb1318d) | ***(Public Preview)*** Creates an expression that evaluates to a list of all substrings in a string field that match a specified regular expression.This expression uses the [RE2](https://github.com/google/re2/wiki/Syntax) regular expression syntax. |
| [regexMatch(fieldName, pattern)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#regexmatch_67f7432) | ***(Public Preview)*** Creates an expression that checks if a string field matches a specified regular expression. |
| [regexMatch(fieldName, pattern)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#regexmatch_cb1318d) | ***(Public Preview)*** Creates an expression that checks if a string field matches a specified regular expression. |
| [round(fieldName)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#round_e5b0480) | ***(Public Preview)*** Creates an expression that rounds a numeric value to the nearest whole number. |
| [round(fieldName, decimalPlaces)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#round_07d0cf0) | ***(Public Preview)*** Creates an expression that rounds a numeric value to the specified number of decimal places. |
| [rtrim(fieldName, valueToTrim)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#rtrim_c0e3211) | ***(Public Preview)*** Trims whitespace or a specified set of characters/bytes from the end of a string or byte array. |
| [split(fieldName, delimiter)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#split_2cfdd37) | ***(Public Preview)*** Creates an expression that splits the value of a field on the provided delimiter. |
| [split(fieldName, delimiter)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#split_f4fe06a) | ***(Public Preview)*** Creates an expression that splits the value of a field on the provided delimiter. |
| [sqrt(fieldName)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#sqrt_e5b0480) | ***(Public Preview)*** Creates an expression that computes the square root of a numeric value. |
| [startsWith(fieldName, prefix)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#startswith_89325cc) | ***(Public Preview)*** Creates an expression that checks if a field's value starts with a given prefix. |
| [startsWith(fieldName, prefix)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#startswith_266c338) | ***(Public Preview)*** Creates an expression that checks if a field's value starts with a given prefix. |
| [stringConcat(fieldName, secondString, otherStrings)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#stringconcat_d80077e) | ***(Public Preview)*** Creates an expression that concatenates string functions, fields or constants together. |
| [stringContains(fieldName, substring)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#stringcontains_5b94cfe) | ***(Public Preview)*** Creates an expression that checks if a string field contains a specified substring. |
| [stringContains(fieldName, substring)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#stringcontains_ac3ba47) | ***(Public Preview)*** Creates an expression that checks if a string field contains a substring specified by an expression. |
| [stringIndexOf(fieldName, search)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#stringindexof_6c4650e) | ***(Public Preview)*** Creates an expression that finds the index of the first occurrence of a substring or byte sequence. |
| [stringRepeat(fieldName, repetitions)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#stringrepeat_e144a59) | ***(Public Preview)*** Creates an expression that repeats a string or byte array a specified number of times. |
| [stringReplaceAll(fieldName, find, replacement)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#stringreplaceall_b0db15f) | ***(Public Preview)*** Creates an expression that replaces all occurrences of a substring or byte sequence with a replacement. |
| [stringReplaceOne(fieldName, find, replacement)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#stringreplaceone_b0db15f) | ***(Public Preview)*** Creates an expression that replaces the first occurrence of a substring or byte sequence with a replacement. |
| [subtract(fieldName, expression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#subtract_1e91657) | ***(Public Preview)*** Creates an expression that subtracts an expression from a field's value. |
| [subtract(fieldName, value)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#subtract_65e2f32) | ***(Public Preview)*** Creates an expression that subtracts a constant value from a field's value. |
| [sum(fieldName)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#sum_e5b0480) | ***(Public Preview)*** Creates an aggregation that calculates the sum of a field's values across multiple stage inputs. |
| [timestampAdd(fieldName, unit, amount)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#timestampadd_341fe7d) | ***(Public Preview)*** Creates an expression that adds a specified amount of time to a timestamp represented by a field. |
| [timestampSubtract(fieldName, unit, amount)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#timestampsubtract_341fe7d) | ***(Public Preview)*** Creates an expression that subtracts a specified amount of time from a timestamp represented by a field. |
| [timestampToUnixMicros(fieldName)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#timestamptounixmicros_e5b0480) | ***(Public Preview)*** Creates an expression that converts a timestamp field to the number of microseconds since the Unix epoch (1970-01-01 00:00:00 UTC). |
| [timestampToUnixMillis(fieldName)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#timestamptounixmillis_e5b0480) | ***(Public Preview)*** Creates an expression that converts a timestamp field to the number of milliseconds since the Unix epoch (1970-01-01 00:00:00 UTC). |
| [timestampToUnixSeconds(fieldName)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#timestamptounixseconds_e5b0480) | ***(Public Preview)*** Creates an expression that converts a timestamp field to the number of seconds since the Unix epoch (1970-01-01 00:00:00 UTC). |
| [timestampTruncate(fieldName, granularity, timezone)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#timestamptruncate_b6c7512) | ***(Public Preview)*** Creates an expression that truncates a timestamp to a specified granularity. |
| [timestampTruncate(fieldName, granularity, timezone)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#timestamptruncate_ed83d46) | ***(Public Preview)*** Creates an expression that truncates a timestamp to a specified granularity. |
| [toLower(fieldName)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#tolower_e5b0480) | ***(Public Preview)*** Creates an expression that converts a string field to lowercase. |
| [toUpper(fieldName)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#toupper_e5b0480) | ***(Public Preview)*** Creates an expression that converts a string field to uppercase. |
| [trim(fieldName, valueToTrim)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#trim_c9f90ee) | ***(Public Preview)*** Creates an expression that removes leading and trailing whitespace from a string or byte array. |
| [trunc(fieldName)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#trunc_e5b0480) | ***(Public Preview)*** Creates an expression that truncates the numeric value of a field to an integer. |
| [trunc(fieldName, decimalPlaces)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#trunc_07d0cf0) | ***(Public Preview)*** Creates an expression that truncates a numeric expression to the specified number of decimal places. |
| [type(fieldName)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#type_e5b0480) | ***(Public Preview)*** Creates an expression that returns the data type of the data in the specified field. |
| [unixMicrosToTimestamp(fieldName)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#unixmicrostotimestamp_e5b0480) | ***(Public Preview)*** Creates an expression that interprets a field's value as the number of microseconds since the Unix epoch (1970-01-01 00:00:00 UTC) and returns a timestamp. |
| [unixMillisToTimestamp(fieldName)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#unixmillistotimestamp_e5b0480) | ***(Public Preview)*** Creates an expression that interprets a field's value as the number of milliseconds since the Unix epoch (1970-01-01 00:00:00 UTC) and returns a timestamp. |
| [unixSecondsToTimestamp(fieldName)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#unixsecondstotimestamp_e5b0480) | ***(Public Preview)*** Creates an expression that interprets a field's value as the number of seconds since the Unix epoch (1970-01-01 00:00:00 UTC) and returns a timestamp. |
| [vectorLength(fieldName)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#vectorlength_e5b0480) | ***(Public Preview)*** Creates an expression that calculates the length of a Firestore Vector represented by a field. |
| **function(first, ...)** |   |
| [add(first, second)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#add_846ca1b) | ***(Public Preview)*** Creates an expression that adds two expressions together. |
| [and(first, second, more)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#and_e0c48bd) | ***(Public Preview)*** Creates an expression that performs a logical 'AND' operation on multiple filter conditions. |
| [concat(first, second, others)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#concat_83be015) | ***(Public Preview)*** Creates an expression that concatenates strings, arrays, or blobs. Types cannot be mixed. |
| [logicalMaximum(first, second, others)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#logicalmaximum_83be015) | ***(Public Preview)*** Creates an expression that returns the largest value between multiple input expressions or literal values. Based on Firestore's value type ordering. |
| [logicalMinimum(first, second, others)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#logicalminimum_83be015) | ***(Public Preview)*** Creates an expression that returns the smallest value between multiple input expressions and literal values. Based on Firestore's value type ordering. |
| [multiply(first, second)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#multiply_846ca1b) | ***(Public Preview)*** Creates an expression that multiplies two expressions together. |
| [or(first, second, more)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#or_e0c48bd) | ***(Public Preview)*** Creates an expression that performs a logical 'OR' operation on multiple filter conditions. |
| [xor(first, second, additionalConditions)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#xor_8197113) | ***(Public Preview)*** Creates an expression that performs a logical 'XOR' (exclusive OR) operation on multiple BooleanExpressions. |
| **function(firstArray, ...)** |   |
| [arrayConcat(firstArray, secondArray, otherArrays)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#arrayconcat_c00d5d7) | ***(Public Preview)*** Creates an expression that concatenates an array expression with other arrays. |
| **function(firstArrayField, ...)** |   |
| [arrayConcat(firstArrayField, secondArray, otherArrays)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#arrayconcat_f92063d) | ***(Public Preview)*** Creates an expression that concatenates a field's array value with other arrays. |
| **function(firstMap, ...)** |   |
| [mapMerge(firstMap, secondMap, otherMaps)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#mapmerge_cfe77ce) | ***(Public Preview)*** Creates an expression that merges multiple map values. |
| **function(firstString, ...)** |   |
| [stringConcat(firstString, secondString, otherStrings)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#stringconcat_8a8d1b6) | ***(Public Preview)*** Creates an expression that concatenates string expressions together. |
| **function(ifExpr, ...)** |   |
| [ifAbsent(ifExpr, elseExpr)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#ifabsent_0e6d161) | ***(Public Preview)*** Creates an expression that returns the `elseExpr` argument if `ifExpr` is absent, else return the result of the `ifExpr` argument evaluation. |
| [ifAbsent(ifExpr, elseValue)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#ifabsent_c34e5ed) | ***(Public Preview)*** Creates an expression that returns the `elseValue` argument if `ifExpr` is absent, else return the result of the `ifExpr` argument evaluation. |
| **function(ifFieldName, ...)** |   |
| [ifAbsent(ifFieldName, elseExpr)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#ifabsent_e6dabea) | ***(Public Preview)*** Creates an expression that returns the `elseExpr` argument if `ifFieldName` is absent, else return the value of the field. |
| [ifAbsent(ifFieldName, elseValue)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#ifabsent_d8f2823) | ***(Public Preview)*** Creates an expression that returns the `elseValue` argument if `ifFieldName` is absent, else return the value of the field. |
| **function(input, ...)** |   |
| [substring(input, position, length)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#substring_e6e0aa3) | ***(Public Preview)*** Creates an expression that returns a substring of a string or byte array. |
| [substring(input, position, length)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#substring_ab56dc6) | ***(Public Preview)*** Creates an expression that returns a substring of a string or byte array. |
| **function(left, ...)** |   |
| [divide(left, right)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#divide_b3c3382) | ***(Public Preview)*** Creates an expression that divides two expressions. |
| [equal(left, right)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#equal_b3c3382) | ***(Public Preview)*** Creates an expression that checks if two expressions are equal. |
| [greaterThan(left, right)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#greaterthan_b3c3382) | ***(Public Preview)*** Creates an expression that checks if the first expression is greater than the second expression. |
| [greaterThanOrEqual(left, right)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#greaterthanorequal_b3c3382) | ***(Public Preview)*** Creates an expression that checks if the first expression is greater than or equal to the second expression. |
| [lessThan(left, right)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#lessthan_b3c3382) | ***(Public Preview)*** Creates an expression that checks if the first expression is less than the second expression. |
| [lessThanOrEqual(left, right)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#lessthanorequal_b3c3382) | ***(Public Preview)*** Creates an expression that checks if the first expression is less than or equal to the second expression. |
| [mod(left, right)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#mod_b3c3382) | ***(Public Preview)*** Creates an expression that calculates the modulo (remainder) of dividing two expressions. |
| [notEqual(left, right)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#notequal_b3c3382) | ***(Public Preview)*** Creates an expression that checks if two expressions are not equal. |
| [pipelineResultEqual(left, right)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#pipelineresultequal_707a755) | ***(Public Preview)*** Test equality of two PipelineResults. |
| [subtract(left, right)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#subtract_b3c3382) | ***(Public Preview)*** Creates an expression that subtracts two expressions. |
| **function(mapExpr, ...)** |   |
| [mapRemove(mapExpr, key)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#mapremove_23c7d51) | ***(Public Preview)*** Creates an expression that removes a key from the map produced by evaluating an expression. |
| [mapRemove(mapExpr, keyExpr)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#mapremove_9fbcaa3) | ***(Public Preview)*** Creates an expression that removes a key from the map produced by evaluating an expression. |
| **function(mapExpression, ...)** |   |
| [mapEntries(mapExpression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#mapentries_9cf124c) | ***(Public Preview)*** Creates an expression that returns the entries of a map as an array of maps, where each map contains a `"k"` property for the key and a `"v"` property for the value. For example: `[{ k: "key1", v: "value1" }, ...]`. |
| [mapGet(mapExpression, subField)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#mapget_688c050) | ***(Public Preview)*** Accesses a value from a map (object) expression using the provided key. |
| [mapKeys(mapExpression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#mapkeys_9cf124c) | ***(Public Preview)*** Creates an expression that returns the keys of a map. |
| [mapSet(mapExpression, key, value, moreKeyValues)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#mapset_45b48ff) | ***(Public Preview)*** Creates an expression that returns a new map with the specified entries added or updated. |
| [mapValues(mapExpression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#mapvalues_9cf124c) | ***(Public Preview)*** Creates an expression that returns the values of a map. |
| **function(mapField, ...)** |   |
| [mapEntries(mapField)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#mapentries_83ad836) | ***(Public Preview)*** Creates an expression that returns the entries of a map as an array of maps, where each map contains a `"k"` property for the key and a `"v"` property for the value. For example: `[{ k: "key1", v: "value1" }, ...]`. |
| [mapKeys(mapField)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#mapkeys_83ad836) | ***(Public Preview)*** Creates an expression that returns the keys of a map. |
| [mapMerge(mapField, secondMap, otherMaps)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#mapmerge_70a564b) | ***(Public Preview)*** Creates an expression that merges multiple map values. |
| [mapRemove(mapField, key)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#mapremove_bd5726e) | ***(Public Preview)*** Creates an expression that removes a key from the map at the specified field name. |
| [mapRemove(mapField, keyExpr)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#mapremove_8406d13) | ***(Public Preview)*** Creates an expression that removes a key from the map at the specified field name. |
| [mapSet(mapField, key, value, moreKeyValues)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#mapset_baadc2a) | ***(Public Preview)*** Creates an expression that returns a new map with the specified entries added or updated. |
| [mapValues(mapField)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#mapvalues_83ad836) | ***(Public Preview)*** Creates an expression that returns the values of a map. |
| **function(name, ...)** |   |
| [field(name)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#field_1eaaff4) | ***(Public Preview)*** Creates a [Field](https://firebase.google.com/docs/reference/js/firestore_pipelines.field.md#field_class) instance representing the field at the given path.The path can be a simple field name (e.g., "name") or a dot-separated path to a nested field (e.g., "address.city"). |
| **function(options, ...)** |   |
| [execute(options)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#execute_9e87e31) | ***(Public Preview)*** Executes a pipeline and returns a Promise to represent the asynchronous operation.The returned Promise can be used to track the progress of the pipeline execution and retrieve the results (or handle any errors) asynchronously.The pipeline results are returned as a [PipelineSnapshot](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelinesnapshot.md#pipelinesnapshot_class) that contains a list of [PipelineResult](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelineresult.md#pipelineresult_class) objects. Each [PipelineResult](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelineresult.md#pipelineresult_class) typically represents a single key/value map that has passed through all the stages of the pipeline, however this might differ depending on the stages involved in the pipeline. For example: - If there are no stages or only transformation stages, each [PipelineResult](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelineresult.md#pipelineresult_class) represents a single document. - If there is an aggregation, only a single [PipelineResult](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelineresult.md#pipelineresult_class) is returned, representing the aggregated results over the entire dataset . - If there is an aggregation stage with grouping, each [PipelineResult](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelineresult.md#pipelineresult_class) represents a distinct group and its associated aggregated values. |
| **function(path, ...)** |   |
| [field(path)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#field_34ee07d) | ***(Public Preview)*** Creates a [Field](https://firebase.google.com/docs/reference/js/firestore_pipelines.field.md#field_class) instance representing the field at the given path. |
| **function(pipeline, ...)** |   |
| [execute(pipeline)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#execute_01df620) | ***(Public Preview)*** Executes a pipeline and returns a Promise to represent the asynchronous operation.The returned Promise can be used to track the progress of the pipeline execution and retrieve the results (or handle any errors) asynchronously.The pipeline results are returned as a [PipelineSnapshot](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelinesnapshot.md#pipelinesnapshot_class) that contains a list of [PipelineResult](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelineresult.md#pipelineresult_class) objects. Each [PipelineResult](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelineresult.md#pipelineresult_class) typically represents a single key/value map that has passed through all the stages of the pipeline, however this might differ depending on the stages involved in the pipeline. For example: - If there are no stages or only transformation stages, each [PipelineResult](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelineresult.md#pipelineresult_class) represents a single document. - If there is an aggregation, only a single [PipelineResult](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelineresult.md#pipelineresult_class) is returned, representing the aggregated results over the entire dataset . - If there is an aggregation stage with grouping, each [PipelineResult](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelineresult.md#pipelineresult_class) represents a distinct group and its associated aggregated values. |
| **function(stringExpression, ...)** |   |
| [charLength(stringExpression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#charlength_c25a54a) | ***(Public Preview)*** Creates an expression that calculates the character length of a string expression in UTF-8. |
| [endsWith(stringExpression, suffix)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#endswith_0a0b889) | ***(Public Preview)*** Creates an expression that checks if a string expression ends with a given postfix. |
| [endsWith(stringExpression, suffix)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#endswith_13aee0d) | ***(Public Preview)*** Creates an expression that checks if a string expression ends with a given postfix. |
| [like(stringExpression, pattern)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#like_a84c581) | ***(Public Preview)*** Creates an expression that performs a case-sensitive wildcard string comparison. |
| [like(stringExpression, pattern)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#like_b534848) | ***(Public Preview)*** Creates an expression that performs a case-sensitive wildcard string comparison. |
| [regexContains(stringExpression, pattern)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#regexcontains_a84c581) | ***(Public Preview)*** Creates an expression that checks if a string expression contains a specified regular expression as a substring. |
| [regexContains(stringExpression, pattern)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#regexcontains_b534848) | ***(Public Preview)*** Creates an expression that checks if a string expression contains a specified regular expression as a substring. |
| [regexFind(stringExpression, pattern)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#regexfind_a84c581) | ***(Public Preview)*** Creates an expression that returns the first substring of a string expression that matches a specified regular expression.This expression uses the [RE2](https://github.com/google/re2/wiki/Syntax) regular expression syntax. |
| [regexFind(stringExpression, pattern)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#regexfind_b534848) | ***(Public Preview)*** Creates an expression that returns the first substring of a string expression that matches a specified regular expression.This expression uses the [RE2](https://github.com/google/re2/wiki/Syntax) regular expression syntax. |
| [regexFindAll(stringExpression, pattern)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#regexfindall_a84c581) | ***(Public Preview)*** Creates an expression that evaluates to a list of all substrings in a string expression that match a specified regular expression.This expression uses the [RE2](https://github.com/google/re2/wiki/Syntax) regular expression syntax. |
| [regexFindAll(stringExpression, pattern)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#regexfindall_b534848) | ***(Public Preview)*** Creates an expression that evaluates to a list of all substrings in a string expression that match a specified regular expression.This expression uses the [RE2](https://github.com/google/re2/wiki/Syntax) regular expression syntax. |
| [regexMatch(stringExpression, pattern)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#regexmatch_a84c581) | ***(Public Preview)*** Creates an expression that checks if a string expression matches a specified regular expression. |
| [regexMatch(stringExpression, pattern)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#regexmatch_b534848) | ***(Public Preview)*** Creates an expression that checks if a string expression matches a specified regular expression. |
| [reverse(stringExpression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#reverse_c25a54a) | ***(Public Preview)*** Creates an expression that reverses a string. |
| [startsWith(stringExpression, prefix)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#startswith_75c3dbb) | ***(Public Preview)*** Creates an expression that checks if a string expression starts with a given prefix. |
| [startsWith(stringExpression, prefix)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#startswith_52f218a) | ***(Public Preview)*** Creates an expression that checks if a string expression starts with a given prefix. |
| [stringContains(stringExpression, substring)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#stringcontains_3e9ff32) | ***(Public Preview)*** Creates an expression that checks if a string expression contains a specified substring. |
| [stringContains(stringExpression, substring)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#stringcontains_cc6ee02) | ***(Public Preview)*** Creates an expression that checks if a string expression contains a substring specified by another expression. |
| [stringReverse(stringExpression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#stringreverse_c25a54a) | ***(Public Preview)*** Creates an expression that reverses a string. |
| [toLower(stringExpression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#tolower_c25a54a) | ***(Public Preview)*** Creates an expression that converts a string expression to lowercase. |
| [toUpper(stringExpression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#toupper_c25a54a) | ***(Public Preview)*** Creates an expression that converts a string expression to uppercase. |
| [trim(stringExpression, valueToTrim)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#trim_dd54322) | ***(Public Preview)*** Creates an expression that removes leading and trailing characters from a string or byte array expression. |
| **function(timestamp, ...)** |   |
| [timestampAdd(timestamp, unit, amount)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#timestampadd_98418f9) | ***(Public Preview)*** Creates an expression that adds a specified amount of time to a timestamp. |
| [timestampAdd(timestamp, unit, amount)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#timestampadd_ffe8e57) | ***(Public Preview)*** Creates an expression that adds a specified amount of time to a timestamp. |
| [timestampSubtract(timestamp, unit, amount)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#timestampsubtract_98418f9) | ***(Public Preview)*** Creates an expression that subtracts a specified amount of time from a timestamp. |
| [timestampSubtract(timestamp, unit, amount)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#timestampsubtract_ffe8e57) | ***(Public Preview)*** Creates an expression that subtracts a specified amount of time from a timestamp. |
| **function(timestampExpression, ...)** |   |
| [timestampTruncate(timestampExpression, granularity, timezone)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#timestamptruncate_ad5d843) | ***(Public Preview)*** Creates an expression that truncates a timestamp to a specified granularity. |
| [timestampTruncate(timestampExpression, granularity, timezone)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#timestamptruncate_d6ab2a4) | ***(Public Preview)*** Creates an expression that truncates a timestamp to a specified granularity. |
| **function(tryExpr, ...)** |   |
| [ifError(tryExpr, catchExpr)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#iferror_a99a327) | ***(Public Preview)*** Creates an expression that returns the `catch` argument if there is an error, else return the result of the `try` argument evaluation.This overload is useful when a BooleanExpression is required. |
| [ifError(tryExpr, catchExpr)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#iferror_756c12e) | ***(Public Preview)*** Creates an expression that returns the `catch` argument if there is an error, else return the result of the `try` argument evaluation. |
| [ifError(tryExpr, catchValue)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#iferror_dc532f9) | ***(Public Preview)*** Creates an expression that returns the `catch` argument if there is an error, else return the result of the `try` argument evaluation. |
| **function(value, ...)** |   |
| [constant(value)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#constant_0c00f91) | ***(Public Preview)*** Creates a `Constant` instance for a number value. |
| [constant(value)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#constant_6dac335) | ***(Public Preview)*** Creates a `Constant` instance for a VectorValue value. |
| [constant(value)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#constant_7c807cd) | ***(Public Preview)*** Creates a `Constant` instance for a string value. |
| [constant(value)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#constant_b2e4f8d) | ***(Public Preview)*** Creates a `BooleanExpression` instance for a boolean value. |
| [constant(value)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#constant_73ebd84) | ***(Public Preview)*** Creates a `Constant` instance for a null value. |
| [constant(value)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#constant_72a76cb) | ***(Public Preview)*** Creates a `Constant` instance for a GeoPoint value. |
| [constant(value)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#constant_000477d) | ***(Public Preview)*** Creates a `Constant` instance for a Timestamp value. |
| [constant(value)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#constant_5131bf7) | ***(Public Preview)*** Creates a `Constant` instance for a Date value. |
| [constant(value)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#constant_fdf565d) | ***(Public Preview)*** Creates a `Constant` instance for a Bytes value. |
| [constant(value)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#constant_bcd2b0b) | ***(Public Preview)*** Creates a `Constant` instance for a DocumentReference value. |
| [exists(value)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#exists_f3daf14) | ***(Public Preview)*** Creates an expression that checks if a field exists. |
| [isAbsent(value)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#isabsent_f3daf14) | ***(Public Preview)*** Creates an expression that returns `true` if a value is absent. Otherwise, returns `false` even if the value is `null`. |
| [isError(value)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#iserror_f3daf14) | ***(Public Preview)*** Creates an expression that checks if a given expression produces an error. |
| **function(vectorExpression, ...)** |   |
| [cosineDistance(vectorExpression, vector)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#cosinedistance_3a80317) | ***(Public Preview)*** Calculates the Cosine distance between a vector expression and a vector literal. |
| [cosineDistance(vectorExpression, otherVectorExpression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#cosinedistance_17b5bcc) | ***(Public Preview)*** Calculates the Cosine distance between two vector expressions. |
| [dotProduct(vectorExpression, vector)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#dotproduct_3a80317) | ***(Public Preview)*** Calculates the dot product between a vector expression and a double array. |
| [dotProduct(vectorExpression, otherVectorExpression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#dotproduct_17b5bcc) | ***(Public Preview)*** Calculates the dot product between two vector expressions. |
| [euclideanDistance(vectorExpression, vector)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#euclideandistance_3a80317) | ***(Public Preview)*** Calculates the Euclidean distance between a vector expression and a double array. |
| [euclideanDistance(vectorExpression, otherVectorExpression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#euclideandistance_17b5bcc) | ***(Public Preview)*** Calculates the Euclidean distance between two vector expressions. |
| [vectorLength(vectorExpression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#vectorlength_58a039b) | ***(Public Preview)*** Creates an expression that calculates the length of a Firestore Vector. |

## Classes

| Class | Description |
|---|---|
| [AggregateFunction](https://firebase.google.com/docs/reference/js/firestore_pipelines.aggregatefunction.md#aggregatefunction_class) | ***(Public Preview)*** A class that represents an aggregate function. |
| [AliasedAggregate](https://firebase.google.com/docs/reference/js/firestore_pipelines.aliasedaggregate.md#aliasedaggregate_class) | ***(Public Preview)*** An AggregateFunction with alias. |
| [AliasedExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.aliasedexpression.md#aliasedexpression_class) | ***(Public Preview)*** |
| [BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class) | ***(Public Preview)*** An interface that represents a filter condition. |
| [Bytes](https://firebase.google.com/docs/reference/js/firestore_pipelines.bytes.md#bytes_class) | An immutable object representing an array of bytes. |
| [CollectionReference](https://firebase.google.com/docs/reference/js/firestore_pipelines.collectionreference.md#collectionreference_class) | A `CollectionReference` object can be used for adding documents, getting document references, and querying for documents (using [query()](https://firebase.google.com/docs/reference/js/firestore_.md#query_9f7b0f4)). |
| [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_pipelines.documentreference.md#documentreference_class) | A `DocumentReference` refers to a document location in a Firestore database and can be used to write, read, or listen to the location. The document at the referenced location may or may not exist. |
| [DocumentSnapshot](https://firebase.google.com/docs/reference/js/firestore_pipelines.documentsnapshot.md#documentsnapshot_class) | A `DocumentSnapshot` contains data read from a document in your Firestore database. The data can be extracted with `.data()` or `.get(<field>)` to get a specific field.For a `DocumentSnapshot` that points to a non-existing document, any data access will return 'undefined'. You can use the `exists()` method to explicitly verify a document's existence. |
| [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | ***(Public Preview)*** Represents an expression that can be evaluated to a value within the execution of a [Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class).Expressions are the building blocks for creating complex queries and transformations in Firestore pipelines. They can represent:- \*\*Field references:\*\* Access values from document fields. - \*\*Literals:\*\* Represent constant values (strings, numbers, booleans). - \*\*Function calls:\*\* Apply functions to one or more expressions.The `Expression` class provides a fluent API for building expressions. You can chain together method calls to create complex expressions. |
| [Field](https://firebase.google.com/docs/reference/js/firestore_pipelines.field.md#field_class) | ***(Public Preview)*** Represents a reference to a field in a Firestore document, or outputs of a [Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class) stage. Field references are used to access document field values in expressions and to specify fields for sorting, filtering, and projecting data in Firestore pipelines. You can create a `Field` instance using the static method: |
| [FieldPath](https://firebase.google.com/docs/reference/js/firestore_pipelines.fieldpath.md#fieldpath_class) | A `FieldPath` refers to a field in a document. The path may consist of a single field name (referring to a top-level field in the document), or a list of field names (referring to a nested field in the document).Create a `FieldPath` by providing field names. If more than one field name is provided, the path will point to a nested field in a document. |
| [FieldValue](https://firebase.google.com/docs/reference/js/firestore_pipelines.fieldvalue.md#fieldvalue_class) | Sentinel values that can be used when writing document fields with `set()` or `update()`. |
| [Firestore](https://firebase.google.com/docs/reference/js/firestore_pipelines.firestore.md#firestore_class) | The Cloud Firestore service interface.Do not call this constructor directly. Instead, use [getFirestore()](https://firebase.google.com/docs/reference/js/firestore_.md#getfirestore). |
| [FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class) | ***(Public Preview)*** This class defines the base class for Firestore [Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class) functions, which can be evaluated within pipeline execution.Typically, you would not use this class or its children directly. Use either the functions like [and()](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#and_e0c48bd), [equal()](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#equal_b3c3382), or the methods on [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) ([Expression.equal()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionequal), [Expression.lessThan()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionlessthan), etc.) to construct new Function instances. |
| [GeoPoint](https://firebase.google.com/docs/reference/js/firestore_pipelines.geopoint.md#geopoint_class) | An immutable object representing a geographic location in Firestore. The location is represented as latitude/longitude pair.Latitude values are in the range of \[-90, 90\]. Longitude values are in the range of \[-180, 180\]. |
| [Ordering](https://firebase.google.com/docs/reference/js/firestore_pipelines.ordering.md#ordering_class) | ***(Public Preview)*** Represents an ordering criterion for sorting documents in a Firestore pipeline.You create `Ordering` instances using the `ascending` and `descending` helper functions. |
| [Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class) | ***(Public Preview)*** |
| [PipelineResult](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelineresult.md#pipelineresult_class) | ***(Public Preview)*** A PipelineResult contains data read from a Firestore Pipeline. The data can be extracted with the [PipelineResult.data()](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelineresult.md#pipelineresultdata) or [PipelineResult.get()](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelineresult.md#pipelineresultget) methods. If the PipelineResult represents a non-document result, `ref` will return a undefined value. |
| [PipelineSnapshot](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelinesnapshot.md#pipelinesnapshot_class) | ***(Public Preview)*** Represents the results of a Firestore pipeline execution.A `PipelineSnapshot` contains zero or more [PipelineResult](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelineresult.md#pipelineresult_class) objects representing the documents returned by a pipeline query. It provides methods to iterate over the documents and access metadata about the query results. |
| [PipelineSource](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelinesource.md#pipelinesource_class) | ***(Public Preview)*** Provides the entry point for defining the data source of a Firestore [Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class).Use the methods of this class (e.g., [PipelineSource.collection()](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelinesource.md#pipelinesourcecollection), [PipelineSource.collectionGroup()](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelinesource.md#pipelinesourcecollectiongroup), [PipelineSource.database()](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelinesource.md#pipelinesourcedatabase), or [PipelineSource.documents()](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelinesource.md#pipelinesourcedocuments)) to specify the initial data for your pipeline, such as a collection, a collection group, the entire database, or a set of specific documents. |
| [Query](https://firebase.google.com/docs/reference/js/firestore_pipelines.query.md#query_class) | A `Query` refers to a query which you can read or listen to. You can also construct refined `Query` objects by adding filters and ordering. |
| [QueryDocumentSnapshot](https://firebase.google.com/docs/reference/js/firestore_pipelines.querydocumentsnapshot.md#querydocumentsnapshot_class) | A `QueryDocumentSnapshot` contains data read from a document in your Firestore database as part of a query. The document is guaranteed to exist and its data can be extracted with `.data()` or `.get(<field>)` to get a specific field.A `QueryDocumentSnapshot` offers the same API surface as a `DocumentSnapshot`. Since query results contain only existing documents, the `exists` property will always be true and `data()` will never return 'undefined'. |
| [SnapshotMetadata](https://firebase.google.com/docs/reference/js/firestore_pipelines.snapshotmetadata.md#snapshotmetadata_class) | Metadata about a snapshot, describing the state of the snapshot. |
| [Timestamp](https://firebase.google.com/docs/reference/js/firestore_pipelines.timestamp.md#timestamp_class) | A `Timestamp` represents a point in time independent of any time zone or calendar, represented as seconds and fractions of seconds at nanosecond resolution in UTC Epoch time.It is encoded using the Proleptic Gregorian Calendar which extends the Gregorian calendar backwards to year one. It is encoded assuming all minutes are 60 seconds long, i.e. leap seconds are "smeared" so that no leap second table is needed for interpretation. Range is from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59.999999999Z.For examples and further specifications, refer to the [Timestamp definition](https://github.com/google/protobuf/blob/master/src/google/protobuf/timestamp.proto). |
| [VectorValue](https://firebase.google.com/docs/reference/js/firestore_pipelines.vectorvalue.md#vectorvalue_class) | Represents a vector type in Firestore documents. Create an instance with `https://firebase.google.com/docs/reference/js/firestore_.md#vector_0dbdaf2`. |

## Interfaces

| Interface | Description |
|---|---|
| [DocumentData](https://firebase.google.com/docs/reference/js/firestore_pipelines.documentdata.md#documentdata_interface) | Document data (for use with [setDoc()](https://firebase.google.com/docs/reference/js/firestore_lite.md#setdoc_ee215ad)) consists of fields mapped to values. |
| [FirestoreDataConverter](https://firebase.google.com/docs/reference/js/firestore_pipelines.firestoredataconverter.md#firestoredataconverter_interface) | Converter used by `withConverter()` to transform user objects of type `AppModelType` into Firestore data of type `DbModelType`.Using the converter allows you to specify generic type arguments when storing and retrieving objects from Firestore.In this context, an "AppModel" is a class that is used in an application to package together related information and functionality. Such a class could, for example, have properties with complex, nested data types, properties used for memoization, properties of types not supported by Firestore (such as `symbol` and `bigint`), and helper functions that perform compound operations. Such classes are not suitable and/or possible to store into a Firestore database. Instead, instances of such classes need to be converted to "plain old JavaScript objects" (POJOs) with exclusively primitive properties, potentially nested inside other POJOs or arrays of POJOs. In this context, this type is referred to as the "DbModel" and would be an object suitable for persisting into Firestore. For convenience, applications can implement `FirestoreDataConverter` and register the converter with Firestore objects, such as `DocumentReference` or `Query`, to automatically convert `AppModel` to `DbModel` when storing into Firestore, and convert `DbModel` to `AppModel` when retrieving from Firestore. |
| [PipelineExecuteOptions](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelineexecuteoptions.md#pipelineexecuteoptions_interface) | ***(Public Preview)*** Options defining Pipeline execution. |
| [Selectable](https://firebase.google.com/docs/reference/js/firestore_pipelines.selectable.md#selectable_interface) | ***(Public Preview)*** An interface that represents a selectable expression. |
| [SnapshotOptions](https://firebase.google.com/docs/reference/js/firestore_pipelines.snapshotoptions.md#snapshotoptions_interface) | Options that configure how data is retrieved from a `DocumentSnapshot` (for example the desired behavior for server timestamps that have not yet been set to their final value). |
| [StageOptions](https://firebase.google.com/docs/reference/js/firestore_pipelines.stageoptions.md#stageoptions_interface) | ***(Public Preview)*** Options defining how a Stage is evaluated. |

## Type Aliases

| Type Alias | Description |
|---|---|
| [AddFieldsStageOptions](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#addfieldsstageoptions) | ***(Public Preview)*** Options defining how an AddFieldsStage is evaluated. See [Pipeline.addFields()](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipelineaddfields). |
| [AggregateStageOptions](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#aggregatestageoptions) | ***(Public Preview)*** Options defining how an AggregateStage is evaluated. See [Pipeline.aggregate()](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipelineaggregate). |
| [CollectionGroupStageOptions](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#collectiongroupstageoptions) | ***(Public Preview)*** Defines the configuration options for a CollectionGroupStage within a pipeline. This type extends [StageOptions](https://firebase.google.com/docs/reference/js/firestore_pipelines.stageoptions.md#stageoptions_interface) and provides specific settings for how a collection group is identified and processed during pipeline execution.See [PipelineSource.collectionGroup()](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelinesource.md#pipelinesourcecollectiongroup) to create a collection group stage. |
| [CollectionStageOptions](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#collectionstageoptions) | ***(Public Preview)*** Options defining how a CollectionStage is evaluated. See [PipelineSource.collection()](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelinesource.md#pipelinesourcecollection). |
| [DatabaseStageOptions](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#databasestageoptions) | ***(Public Preview)*** Options defining how a DatabaseStage is evaluated. See [PipelineSource.database()](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelinesource.md#pipelinesourcedatabase). |
| [DistinctStageOptions](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#distinctstageoptions) | ***(Public Preview)*** Options defining how a DistinctStage is evaluated. See [Pipeline.distinct()](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipelinedistinct). |
| [DocumentsStageOptions](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#documentsstageoptions) | ***(Public Preview)*** Options defining how a DocumentsStage is evaluated. See [PipelineSource.documents()](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelinesource.md#pipelinesourcedocuments). |
| [ExpressionType](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#expressiontype) | ***(Public Preview)*** An enumeration of the different types of expressions. |
| [FindNearestStageOptions](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#findneareststageoptions) | ***(Public Preview)*** Options defining how a FindNearestStage is evaluated. See [Pipeline.findNearest()](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipelinefindnearest). |
| [LimitStageOptions](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#limitstageoptions) | ***(Public Preview)*** Options defining how a LimitStage is evaluated. See [Pipeline.limit()](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipelinelimit). |
| [OffsetStageOptions](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#offsetstageoptions) | ***(Public Preview)*** Options defining how an OffsetStage is evaluated. See [Pipeline.offset()](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipelineoffset). |
| [OneOf](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#oneof) | ***(Public Preview)*** Utility type to create an type that only allows one property of the Type param T to be set. |
| [PartialWithFieldValue](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#partialwithfieldvalue) | Similar to TypeScript's `Partial<T>`, but allows nested fields to be omitted and FieldValues to be passed in as property values. |
| [Primitive](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#primitive) | Primitive types. |
| [RemoveFieldsStageOptions](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#removefieldsstageoptions) | ***(Public Preview)*** Options defining how a RemoveFieldsStage is evaluated. See [Pipeline.removeFields()](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipelineremovefields). |
| [ReplaceWithStageOptions](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#replacewithstageoptions) | ***(Public Preview)*** Options defining how a ReplaceWithStage is evaluated. See [Pipeline.replaceWith()](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipelinereplacewith). |
| [SampleStageOptions](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#samplestageoptions) | ***(Public Preview)*** Defines the options for evaluating a sample stage within a pipeline. This type combines common [StageOptions](https://firebase.google.com/docs/reference/js/firestore_pipelines.stageoptions.md#stageoptions_interface) with a specific configuration where only one of the defined sampling methods can be applied.See [Pipeline.sample()](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipelinesample) to create a sample stage.. |
| [SelectStageOptions](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#selectstageoptions) | ***(Public Preview)*** Options defining how a SelectStage is evaluated. See [Pipeline.select()](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipelineselect). |
| [SetOptions](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#setoptions) | An options object that configures the behavior of [setDoc()](https://firebase.google.com/docs/reference/js/firestore_lite.md#setdoc_ee215ad), and calls. These calls can be configured to perform granular merges instead of overwriting the target documents in their entirety by providing a `SetOptions` with `merge: true`. |
| [SortStageOptions](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#sortstageoptions) | ***(Public Preview)*** Options defining how a SortStage is evaluated. See [Pipeline.sort()](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipelinesort). |
| [TimeGranularity](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#timegranularity) | ***(Public Preview)*** Specify time granularity for expressions. |
| [Type](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#type) | ***(Public Preview)*** An enumeration of the different types generated by the Firestore backend. - Numerics evaluate directly to backend representation (`int64` or `float64`), not JS `number`. - JavaScript `Date` and firestore `Timestamp` objects strictly evaluate to `'timestamp'`. - Advanced configurations parsing backend types (such as `decimal128`, `max_key` or `min_key` from BSON) are also incorporated in this union string type. Note that `decimal128` is a backend-only numeric type that the JavaScript SDK cannot create natively, but can be evaluated in pipelines. |
| [UnionStageOptions](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#unionstageoptions) | ***(Public Preview)*** Options defining how a UnionStage is evaluated. See [Pipeline.union()](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipelineunion). |
| [UnnestStageOptions](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#unneststageoptions) | ***(Public Preview)*** Represents the specific options available for configuring an `UnnestStage` within a pipeline. |
| [WhereStageOptions](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#wherestageoptions) | ***(Public Preview)*** Options defining how a WhereStage is evaluated. See [Pipeline.where()](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipelinewhere). |
| [WithFieldValue](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#withfieldvalue) | Allows FieldValues to be passed in as a property value while maintaining type safety. |

## function()

### countAll()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an aggregation that counts the total number of stage inputs.

**Signature:**

    export declare function countAll(): AggregateFunction;

**Returns:**

[AggregateFunction](https://firebase.google.com/docs/reference/js/firestore_pipelines.aggregatefunction.md#aggregatefunction_class)

A new [AggregateFunction](https://firebase.google.com/docs/reference/js/firestore_pipelines.aggregatefunction.md#aggregatefunction_class) representing the 'countAll' aggregation.

### Example

    // Count the total number of input documents
    countAll().as("totalDocument");

### currentTimestamp()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that evaluates to the current server timestamp.

**Signature:**

    export declare function currentTimestamp(): FunctionExpression;

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new Expression representing the current server timestamp.

### Example

    // Get the current server timestamp
    currentTimestamp()

### rand()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that generates a random number between 0.0 and 1.0 but not including 1.0.

**Signature:**

    export declare function rand(): FunctionExpression;

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the rand operation.

### Example

    // Generate a random number between 0.0 and 1.0.
    rand();

## function(array, ...)

### arrayContains(array, element)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if an array expression contains a specific element.

**Signature:**

    export declare function arrayContains(array: Expression, element: Expression): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| array | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The array expression to check. |
| element | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The element to search for in the array. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the 'array_contains' comparison.

### Example

    // Check if the 'colors' array contains the value of field 'selectedColor'
    arrayContains(field("colors"), field("selectedColor"));

### arrayContains(array, element)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if an array expression contains a specific element.

**Signature:**

    export declare function arrayContains(array: Expression, element: unknown): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| array | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The array expression to check. |
| element | unknown | The element to search for in the array. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the 'array_contains' comparison.

### Example

    // Check if the 'colors' array contains "red"
    arrayContains(field("colors"), "red");

### arrayContainsAll(array, values)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if an array expression contains all the specified elements.

**Signature:**

    export declare function arrayContainsAll(array: Expression, values: Array<Expression | unknown>): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| array | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The array expression to check. |
| values | Array\<[Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| unknown\> | The elements to check for in the array. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the 'array_contains_all' comparison.

### Example

    // Check if the "tags" array contains all of the values: "SciFi", "Adventure", and the value from field "tag1"
    arrayContainsAll(field("tags"), [field("tag1"), constant("SciFi"), "Adventure"]);

### arrayContainsAll(array, arrayExpression)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if an array expression contains all the specified elements.

**Signature:**

    export declare function arrayContainsAll(array: Expression, arrayExpression: Expression): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| array | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The array expression to check. |
| arrayExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The elements to check for in the array. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the 'array_contains_all' comparison.

### Example

    // Check if the "tags" array contains all of the values: "SciFi", "Adventure", and the value from field "tag1"
    arrayContainsAll(field("tags"), [field("tag1"), constant("SciFi"), "Adventure"]);

### arrayContainsAny(array, values)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if an array expression contains any of the specified elements.

**Signature:**

    export declare function arrayContainsAny(array: Expression, values: Array<Expression | unknown>): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| array | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The array expression to check. |
| values | Array\<[Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| unknown\> | The elements to check for in the array. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the 'array_contains_any' comparison.

### Example

    // Check if the 'categories' array contains either values from field "cate1" or "Science"
    arrayContainsAny(field("categories"), [field("cate1"), "Science"]);

### arrayContainsAny(array, values)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if an array expression contains any of the specified elements.

**Signature:**

    export declare function arrayContainsAny(array: Expression, values: Expression): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| array | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The array expression to check. |
| values | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | An expression that evaluates to an array, whose elements to check for in the array. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the 'array_contains_any' comparison.

### Example

    // Check if the 'categories' array contains either values from field "cate1" or "Science"
    arrayContainsAny(field("categories"), array([field("cate1"), "Science"]));

### arrayLength(array)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that calculates the length of an array expression.

**Signature:**

    export declare function arrayLength(array: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| array | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The array expression to calculate the length of. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the length of the array.

### Example

    // Get the number of items in the 'cart' array
    arrayLength(field("cart"));

## function(arrayExpression, ...)

### arrayGet(arrayExpression, offset)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that indexes into an array from the beginning or end and return the element. If the offset exceeds the array length, an error is returned. A negative offset, starts from the end.

**Signature:**

    export declare function arrayGet(arrayExpression: Expression, offset: number): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| arrayExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | An `Expression` evaluating to an array. |
| offset | number | The index of the element to return. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the 'arrayGet' operation.

### Example

    // Return the value in the tags field array at index 1.
    arrayGet(field('tags'), 1);

### arrayGet(arrayExpression, offsetExpr)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that indexes into an array from the beginning or end and return the element. If the offset exceeds the array length, an error is returned. A negative offset, starts from the end.

**Signature:**

    export declare function arrayGet(arrayExpression: Expression, offsetExpr: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| arrayExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | An `Expression` evaluating to an array. |
| offsetExpr | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | An `Expression` evaluating to the index of the element to return. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the 'arrayGet' operation.

### Example

    // Return the value in the tags field array at index specified by field
    // 'favoriteTag'.
    arrayGet(field('tags'), field('favoriteTag'));

### join(arrayExpression, delimiterExpression)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that joins the elements of an array into a string.

**Signature:**

    export declare function join(arrayExpression: Expression, delimiterExpression: Expression): Expression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| arrayExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | An expression that evaluates to an array. |
| delimiterExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression that evaluates to the delimiter string. |

**Returns:**

[Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class)

A new Expression representing the join operation.

### Example

    // Join an array of string using the delimiter from the 'separator' field.
    join(array(['foo', 'bar']), field("separator"))

### join(arrayExpression, delimiter)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that joins the elements of an array into a string.

**Signature:**

    export declare function join(arrayExpression: Expression, delimiter: string): Expression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| arrayExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | An expression that evaluates to an array. |
| delimiter | string | The string to use as a delimiter. |

**Returns:**

[Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class)

A new Expression representing the join operation.

### Example

    // Join the elements of the 'tags' field with a comma and space.
    join(field("tags"), ", ")

## function(arrayField, ...)

### arrayGet(arrayField, offset)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that indexes into an array from the beginning or end and return the element. If the offset exceeds the array length, an error is returned. A negative offset, starts from the end.

**Signature:**

    export declare function arrayGet(arrayField: string, offset: number): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| arrayField | string | The name of the array field. |
| offset | number | The index of the element to return. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the 'arrayGet' operation.

### Example

    // Return the value in the tags field array at index 1.
    arrayGet('tags', 1);

### arrayGet(arrayField, offsetExpr)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that indexes into an array from the beginning or end and return the element. If the offset exceeds the array length, an error is returned. A negative offset, starts from the end.

**Signature:**

    export declare function arrayGet(arrayField: string, offsetExpr: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| arrayField | string | The name of the array field. |
| offsetExpr | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | An `Expression` evaluating to the index of the element to return. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the 'arrayGet' operation.

### Example

    // Return the value in the tags field array at index specified by field
    // 'favoriteTag'.
    arrayGet('tags', field('favoriteTag'));

## function(arrayFieldName, ...)

### join(arrayFieldName, delimiter)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that joins the elements of an array into a string.

**Signature:**

    export declare function join(arrayFieldName: string, delimiter: string): Expression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| arrayFieldName | string | The name of the field containing the array. |
| delimiter | string | The string to use as a delimiter. |

**Returns:**

[Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class)

A new Expression representing the join operation.

### Example

    // Join the elements of the 'tags' field with a comma and space.
    join("tags", ", ")

### join(arrayFieldName, delimiterExpression)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that joins the elements of an array into a string.

**Signature:**

    export declare function join(arrayFieldName: string, delimiterExpression: Expression): Expression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| arrayFieldName | string | The name of the field containing the array. |
| delimiterExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression that evaluates to the delimiter string. |

**Returns:**

[Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class)

A new Expression representing the join operation.

### Example

    // Join the elements of the 'tags' field with the delimiter from the 'separator' field.
    join('tags', field("separator"))

## function(base, ...)

### pow(base, exponent)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns the value of the base expression raised to the power of the exponent expression.

**Signature:**

    export declare function pow(base: Expression, exponent: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| base | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression to raise to the power of the exponent. |
| exponent | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression to raise the base to the power of. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the power operation.

### Example

    // Raise the value of the 'base' field to the power of the 'exponent' field.
    pow(field("base"), field("exponent"));

### pow(base, exponent)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns the value of the base expression raised to the power of the exponent.

**Signature:**

    export declare function pow(base: Expression, exponent: number): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| base | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression to raise to the power of the exponent. |
| exponent | number | The constant value to raise the base to the power of. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the power operation.

### Example

    // Raise the value of the 'base' field to the power of 2.
    pow(field("base"), 2);

### pow(base, exponent)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns the value of the base field raised to the power of the exponent expression.

**Signature:**

    export declare function pow(base: string, exponent: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| base | string | The name of the field to raise to the power of the exponent. |
| exponent | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression to raise the base to the power of. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the power operation.

### Example

    // Raise the value of the 'base' field to the power of the 'exponent' field.
    pow("base", field("exponent"));

### pow(base, exponent)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns the value of the base field raised to the power of the exponent.

**Signature:**

    export declare function pow(base: string, exponent: number): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| base | string | The name of the field to raise to the power of the exponent. |
| exponent | number | The constant value to raise the base to the power of. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the power operation.

### Example

    // Raise the value of the 'base' field to the power of 2.
    pow("base", 2);

## function(booleanExpr, ...)

### countIf(booleanExpr)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an aggregation that counts the number of stage inputs where the provided boolean expression evaluates to true.

**Signature:**

    export declare function countIf(booleanExpr: BooleanExpression): AggregateFunction;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| booleanExpr | [BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class) | The boolean expression to evaluate on each input. |

**Returns:**

[AggregateFunction](https://firebase.google.com/docs/reference/js/firestore_pipelines.aggregatefunction.md#aggregatefunction_class)

A new `AggregateFunction` representing the 'countIf' aggregation.

### Example

    // Count the number of documents where 'is_active' field equals true
    countIf(field("is_active").equal(true)).as("numActiveDocuments");

### not(booleanExpr)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that negates a filter condition.

**Signature:**

    export declare function not(booleanExpr: BooleanExpression): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| booleanExpr | [BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class) | The filter condition to negate. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the negated filter condition.

### Example

    // Find documents where the 'completed' field is NOT true
    not(equal("completed", true));

## function(condition, ...)

### conditional(condition, thenExpr, elseExpr)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates a conditional expression that evaluates to a 'then' expression if a condition is true and an 'else' expression if the condition is false.

**Signature:**

    export declare function conditional(condition: BooleanExpression, thenExpr: Expression, elseExpr: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| condition | [BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class) | The condition to evaluate. |
| thenExpr | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression to evaluate if the condition is true. |
| elseExpr | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression to evaluate if the condition is false. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the conditional expression.

### Example

    // If 'age' is greater than 18, return "Adult"; otherwise, return "Minor".
    conditional(
        greaterThan("age", 18), constant("Adult"), constant("Minor"));

## function(documentPath, ...)

### documentId(documentPath)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns the document ID from a path.

**Signature:**

    export declare function documentId(documentPath: string | DocumentReference): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| documentPath | string \| [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_.documentreference.md#documentreference_class) |   |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the documentId operation.

### Example

    // Get the document ID from a path.
    documentId(myDocumentReference);

## function(documentPathExpr, ...)

### documentId(documentPathExpr)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns the document ID from a path.

**Signature:**

    export declare function documentId(documentPathExpr: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| documentPathExpr | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) |   |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the documentId operation.

### Example

    // Get the document ID from a path.
    documentId(field("__path__"));

## function(element, ...)

### notEqualAny(element, values)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if an expression is not equal to any of the provided values or expressions.

**Signature:**

    export declare function notEqualAny(element: Expression, values: Array<Expression | unknown>): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| element | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression to compare. |
| values | Array\<[Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| unknown\> | The values to check against. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the 'NOT IN' comparison.

### Example

    // Check if the 'status' field is neither "pending" nor the value of 'rejectedStatus'
    notEqualAny(field("status"), ["pending", field("rejectedStatus")]);

### notEqualAny(element, arrayExpression)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if an expression is not equal to any of the provided values or expressions.

**Signature:**

    export declare function notEqualAny(element: Expression, arrayExpression: Expression): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| element | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression to compare. |
| arrayExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The values to check against. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the 'NOT IN' comparison.

### Example

    // Check if the 'status' field is neither "pending" nor the value of the field 'rejectedStatus'
    notEqualAny(field("status"), ["pending", field("rejectedStatus")]);

## function(elements, ...)

### array(elements)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that creates a Firestore array value from an input array.

**Signature:**

    export declare function array(elements: unknown[]): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| elements | unknown\[\] | The input array to evaluate in the expression. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the array function.

### Example

    // Create an array value from the input array and reference the 'baz' field value from the input document.
    array(['bar', Field.of('baz')]).as('foo');

### map(elements)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that creates a Firestore map value from an input object.

**Signature:**

    export declare function map(elements: Record<string, unknown>): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| elements | Record\<string, unknown\> | The input map to evaluate in the expression. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the map function.

### Example

    // Create a map from the input object and reference the 'baz' field value from the input document.
    map({foo: 'bar', baz: Field.of('baz')}).as('data');

## function(expr, ...)

### abs(expr)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that computes the absolute value of a numeric value.

**Signature:**

    export declare function abs(expr: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expr | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression to compute the absolute value of. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the absolute value of the numeric value.

### ascending(expr)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an [Ordering](https://firebase.google.com/docs/reference/js/firestore_pipelines.ordering.md#ordering_class) that sorts documents in ascending order based on an expression.

**Signature:**

    export declare function ascending(expr: Expression): Ordering;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expr | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression to create an ascending ordering for. |

**Returns:**

[Ordering](https://firebase.google.com/docs/reference/js/firestore_pipelines.ordering.md#ordering_class)

A new `Ordering` for ascending sorting.

### Example

    // Sort documents by the 'name' field in lowercase in ascending order
    firestore.pipeline().collection("users")
      .sort(ascending(field("name").toLower()));

### byteLength(expr)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that calculates the byte length of a string in UTF-8, or just the length of a Blob.

**Signature:**

    export declare function byteLength(expr: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expr | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression representing the string. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the length of the string in bytes.

### Example

    // Calculate the length of the 'myString' field in bytes.
    byteLength(field("myString"));

### countDistinct(expr)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an aggregation that counts the number of distinct values of a field.

**Signature:**

    export declare function countDistinct(expr: Expression | string): AggregateFunction;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expr | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| string | The expression or field to count distinct values of. |

**Returns:**

[AggregateFunction](https://firebase.google.com/docs/reference/js/firestore_pipelines.aggregatefunction.md#aggregatefunction_class)

A new `AggregateFunction` representing the 'count_distinct' aggregation.

### descending(expr)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an [Ordering](https://firebase.google.com/docs/reference/js/firestore_pipelines.ordering.md#ordering_class) that sorts documents in descending order based on an expression.

**Signature:**

    export declare function descending(expr: Expression): Ordering;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expr | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression to create a descending ordering for. |

**Returns:**

[Ordering](https://firebase.google.com/docs/reference/js/firestore_pipelines.ordering.md#ordering_class)

A new `Ordering` for descending sorting.

### Example

    // Sort documents by the 'name' field in lowercase in descending order
    firestore.pipeline().collection("users")
      .sort(descending(field("name").toLower()));

### floor(expr)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that computes the floor of a numeric value.

**Signature:**

    export declare function floor(expr: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expr | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression to compute the floor of. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the floor of the numeric value.

### timestampToUnixMicros(expr)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that converts a timestamp expression to the number of microseconds since the Unix epoch (1970-01-01 00:00:00 UTC).

**Signature:**

    export declare function timestampToUnixMicros(expr: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expr | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression representing the timestamp. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the number of microseconds since epoch.

### Example

    // Convert the 'timestamp' field to microseconds since epoch.
    timestampToUnixMicros(field("timestamp"));

### timestampToUnixMillis(expr)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that converts a timestamp expression to the number of milliseconds since the Unix epoch (1970-01-01 00:00:00 UTC).

**Signature:**

    export declare function timestampToUnixMillis(expr: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expr | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression representing the timestamp. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the number of milliseconds since epoch.

### Example

    // Convert the 'timestamp' field to milliseconds since epoch.
    timestampToUnixMillis(field("timestamp"));

### timestampToUnixSeconds(expr)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that converts a timestamp expression to the number of seconds since the Unix epoch (1970-01-01 00:00:00 UTC).

**Signature:**

    export declare function timestampToUnixSeconds(expr: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expr | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression representing the timestamp. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the number of seconds since epoch.

### Example

    // Convert the 'timestamp' field to seconds since epoch.
    timestampToUnixSeconds(field("timestamp"));

### unixMicrosToTimestamp(expr)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that interprets an expression as the number of microseconds since the Unix epoch (1970-01-01 00:00:00 UTC) and returns a timestamp.

**Signature:**

    export declare function unixMicrosToTimestamp(expr: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expr | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression representing the number of microseconds since epoch. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the timestamp.

### Example

    // Interpret the 'microseconds' field as microseconds since epoch.
    unixMicrosToTimestamp(field("microseconds"));

### unixMillisToTimestamp(expr)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that interprets an expression as the number of milliseconds since the Unix epoch (1970-01-01 00:00:00 UTC) and returns a timestamp.

**Signature:**

    export declare function unixMillisToTimestamp(expr: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expr | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression representing the number of milliseconds since epoch. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the timestamp.

### Example

    // Interpret the 'milliseconds' field as milliseconds since epoch.
    unixMillisToTimestamp(field("milliseconds"));

### unixSecondsToTimestamp(expr)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that interprets an expression as the number of seconds since the Unix epoch (1970-01-01 00:00:00 UTC) and returns a timestamp.

**Signature:**

    export declare function unixSecondsToTimestamp(expr: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expr | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression representing the number of seconds since epoch. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the timestamp.

### Example

    // Interpret the 'seconds' field as seconds since epoch.
    unixSecondsToTimestamp(field("seconds"));

## function(expression, ...)

### arrayAgg(expression)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an aggregation that collects all values of an expression across multiple stage inputs into an array.

If the expression resolves to an absent value, it is converted to `null`. The order of elements in the output array is not stable and shouldn't be relied upon.

**Signature:**

    export declare function arrayAgg(expression: Expression): AggregateFunction;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression to collect values from. |

**Returns:**

[AggregateFunction](https://firebase.google.com/docs/reference/js/firestore_pipelines.aggregatefunction.md#aggregatefunction_class)

A new [AggregateFunction](https://firebase.google.com/docs/reference/js/firestore_pipelines.aggregatefunction.md#aggregatefunction_class) representing the 'array_agg' aggregation.

### Example

    // Collect all tags from books into an array
    arrayAgg(field("tags")).as("allTags");

### arrayAggDistinct(expression)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an aggregation that collects all distinct values of an expression across multiple stage inputs into an array.

If the expression resolves to an absent value, it is converted to `null`. The order of elements in the output array is not stable and shouldn't be relied upon.

**Signature:**

    export declare function arrayAggDistinct(expression: Expression): AggregateFunction;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression to collect values from. |

**Returns:**

[AggregateFunction](https://firebase.google.com/docs/reference/js/firestore_pipelines.aggregatefunction.md#aggregatefunction_class)

A new [AggregateFunction](https://firebase.google.com/docs/reference/js/firestore_pipelines.aggregatefunction.md#aggregatefunction_class) representing the 'array_agg_distinct' aggregation.

### Example

    // Collect all distinct tags from books into an array
    arrayAggDistinct(field("tags")).as("allDistinctTags");

### arraySum(expression)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that computes the sum of the elements in an array.

**Signature:**

    export declare function arraySum(expression: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | An expression evaluating to a numeric array, which the sum will be computed for. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the sum of the elements in the array.

### Example

    // Compute the sum of the elements in the 'scores' field.
    arraySum(field("scores"));

### average(expression)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an aggregation that calculates the average (mean) of values from an expression across multiple stage inputs.

**Signature:**

    export declare function average(expression: Expression): AggregateFunction;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression representing the values to average. |

**Returns:**

[AggregateFunction](https://firebase.google.com/docs/reference/js/firestore_pipelines.aggregatefunction.md#aggregatefunction_class)

A new [AggregateFunction](https://firebase.google.com/docs/reference/js/firestore_pipelines.aggregatefunction.md#aggregatefunction_class) representing the 'average' aggregation.

### Example

    // Calculate the average age of users
    average(field("age")).as("averageAge");

### ceil(expression)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that computes the ceiling of a numeric value.

**Signature:**

    export declare function ceil(expression: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | An expression evaluating to a numeric value, which the ceiling will be computed for. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the ceiling of the numeric value.

### Example

    // Compute the ceiling of the 'price' field.
    ceil(field("price"));

### collectionId(expression)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns the collection ID from a path.

**Signature:**

    export declare function collectionId(expression: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | An expression evaluating to a path, which the collection ID will be extracted from. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the collectionId operation.

### Example

    // Get the collection ID from a path.
    collectionId(field("__name__"));

### count(expression)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an aggregation that counts the number of stage inputs with valid evaluations of the provided expression.

**Signature:**

    export declare function count(expression: Expression): AggregateFunction;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression to count. |

**Returns:**

[AggregateFunction](https://firebase.google.com/docs/reference/js/firestore_pipelines.aggregatefunction.md#aggregatefunction_class)

A new [AggregateFunction](https://firebase.google.com/docs/reference/js/firestore_pipelines.aggregatefunction.md#aggregatefunction_class) representing the 'count' aggregation.

### Example

    // Count the number of items where the price is greater than 10
    count(field("price").greaterThan(10)).as("expensiveItemCount");

### divide(expression, value)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that divides an expression by a constant value.

**Signature:**

    export declare function divide(expression: Expression, value: unknown): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression to be divided. |
| value | unknown | The constant value to divide by. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the division operation.

### Example

    // Divide the 'value' field by 10
    divide(field("value"), 10);

### equal(expression, value)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if an expression is equal to a constant value.

**Signature:**

    export declare function equal(expression: Expression, value: unknown): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression to compare. |
| value | unknown | The constant value to compare to. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `Expression` representing the equality comparison.

### Example

    // Check if the 'age' field is equal to 21
    equal(field("age"), 21);

### equalAny(expression, values)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if an expression, when evaluated, is equal to any of the provided values or expressions.

**Signature:**

    export declare function equalAny(expression: Expression, values: Array<Expression | unknown>): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression whose results to compare. |
| values | Array\<[Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| unknown\> | The values to check against. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the 'IN' comparison.

### Example

    // Check if the 'category' field is either "Electronics" or value of field 'primaryType'
    equalAny(field("category"), [constant("Electronics"), field("primaryType")]);

### equalAny(expression, arrayExpression)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if an expression is equal to any of the provided values.

**Signature:**

    export declare function equalAny(expression: Expression, arrayExpression: Expression): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression whose results to compare. |
| arrayExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | An expression that evaluates to an array, whose elements to check for equality to the input. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the 'IN' comparison.

### Example

    // Check if the 'category' field is set to a value in the disabledCategories field
    equalAny(field("category"), field('disabledCategories'));

### exp(expression)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that computes e to the power of the expression's result.

**Signature:**

    export declare function exp(expression: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) |   |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the exp of the numeric value.

### Example

    // Compute e to the power of 2.
    exp(constant(2));

### first(expression)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an aggregation that finds the first value of an expression across multiple stage inputs.

**Signature:**

    export declare function first(expression: Expression): AggregateFunction;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression to find the first value of. |

**Returns:**

[AggregateFunction](https://firebase.google.com/docs/reference/js/firestore_pipelines.aggregatefunction.md#aggregatefunction_class)

A new [AggregateFunction](https://firebase.google.com/docs/reference/js/firestore_pipelines.aggregatefunction.md#aggregatefunction_class) representing the 'first' aggregation.

### Example

    // Find the first value of the 'rating' field
    first(field("rating")).as("firstRating");

### greaterThan(expression, value)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if an expression is greater than a constant value.

**Signature:**

    export declare function greaterThan(expression: Expression, value: unknown): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression to compare. |
| value | unknown | The constant value to compare to. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `Expression` representing the greater than comparison.

### Example

    // Check if the 'age' field is greater than 18
    greaterThan(field("age"), 18);

### greaterThanOrEqual(expression, value)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if an expression is greater than or equal to a constant value.

**Signature:**

    export declare function greaterThanOrEqual(expression: Expression, value: unknown): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression to compare. |
| value | unknown | The constant value to compare to. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `Expression` representing the greater than or equal to comparison.

### Example

    // Check if the 'quantity' field is greater than or equal to 10
    greaterThanOrEqual(field("quantity"), 10);

### isType(expression, type)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if the result of an expression is of the given type.

Null or undefined fields evaluate to skip/error. Use `ifAbsent()` / `isAbsent()` to evaluate missing data.

**Signature:**

    export declare function isType(expression: Expression, type: Type): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression to check. |
| type | [Type](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#type) | The type to check for. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `BooleanExpression` that evaluates to true if the expression's result is of the given type, false otherwise.

### Example

    // Check if the result of a calculation is a number
    isType(add('count', 1), 'number')

### last(expression)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an aggregation that finds the last value of an expression across multiple stage inputs.

**Signature:**

    export declare function last(expression: Expression): AggregateFunction;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression to find the last value of. |

**Returns:**

[AggregateFunction](https://firebase.google.com/docs/reference/js/firestore_pipelines.aggregatefunction.md#aggregatefunction_class)

A new [AggregateFunction](https://firebase.google.com/docs/reference/js/firestore_pipelines.aggregatefunction.md#aggregatefunction_class) representing the 'last' aggregation.

### Example

    // Find the last value of the 'rating' field
    last(field("rating")).as("lastRating");

### length_2(expression)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that calculates the length of a string, array, map, vector, or bytes.

**Signature:**

    declare function length_2(expression: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | An expression evaluating to a string, array, map, vector, or bytes, which the length will be calculated for. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the length of the string, array, map, vector, or bytes.

### Example

    // Get the length of the 'name' field.
    length(field("name"));

    // Get the number of items in the 'cart' array.
    length(field("cart"));

### lessThan(expression, value)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if an expression is less than a constant value.

**Signature:**

    export declare function lessThan(expression: Expression, value: unknown): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression to compare. |
| value | unknown | The constant value to compare to. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `Expression` representing the less than comparison.

### Example

    // Check if the 'age' field is less than 30
    lessThan(field("age"), 30);

### lessThanOrEqual(expression, value)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if an expression is less than or equal to a constant value.

**Signature:**

    export declare function lessThanOrEqual(expression: Expression, value: unknown): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression to compare. |
| value | unknown | The constant value to compare to. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `Expression` representing the less than or equal to comparison.

### Example

    // Check if the 'quantity' field is less than or equal to 20
    lessThan(field("quantity"), 20);

### ln(expression)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that computes the natural logarithm of a numeric value.

**Signature:**

    export declare function ln(expression: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | An expression evaluating to a numeric value, which the natural logarithm will be computed for. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the natural logarithm of the numeric value.

### Example

    // Compute the natural logarithm of the 'value' field.
    ln(field("value"));

### log(expression, base)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that computes the logarithm of an expression to a given base.

**Signature:**

    export declare function log(expression: Expression, base: number): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | An expression evaluating to a numeric value, which the logarithm will be computed for. |
| base | number | The base of the logarithm. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the logarithm of the numeric value.

### Example

    // Compute the logarithm of the 'value' field with base 10.
    log(field("value"), 10);

### log(expression, base)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that computes the logarithm of an expression to a given base.

**Signature:**

    export declare function log(expression: Expression, base: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | An expression evaluating to a numeric value, which the logarithm will be computed for. |
| base | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The base of the logarithm. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the logarithm of the numeric value.

### Example

    // Compute the logarithm of the 'value' field with the base in the 'base' field.
    log(field("value"), field("base"));

### log10(expression)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that computes the base-10 logarithm of a numeric value.

**Signature:**

    export declare function log10(expression: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | An expression evaluating to a numeric value, which the base-10 logarithm will be computed for. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the base-10 logarithm of the numeric value.

### Example

    // Compute the base-10 logarithm of the 'value' field.
    log10(field("value"));

### ltrim(expression, valueToTrim)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Trims whitespace or a specified set of characters/bytes from the beginning of a string or byte array.

**Signature:**

    export declare function ltrim(expression: Expression, valueToTrim?: string | Expression | Bytes): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression representing the string or byte array. |
| valueToTrim | string \| [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| [Bytes](https://firebase.google.com/docs/reference/js/firestore_.bytes.md#bytes_class) | Optional. A string or byte array containing the characters/bytes to trim. If not specified, whitespace will be trimmed. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the trimmed string or byte array.

### Example

    // Trim whitespace from the beginning of the 'userInput' field
    ltrim(field("userInput"));

    // Trim quotes from the beginning of the 'userInput' field
    ltrim(field("userInput"), '"');

### maximum(expression)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an aggregation that finds the maximum value of an expression across multiple stage inputs.

**Signature:**

    export declare function maximum(expression: Expression): AggregateFunction;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression to find the maximum value of. |

**Returns:**

[AggregateFunction](https://firebase.google.com/docs/reference/js/firestore_pipelines.aggregatefunction.md#aggregatefunction_class)

A new [AggregateFunction](https://firebase.google.com/docs/reference/js/firestore_pipelines.aggregatefunction.md#aggregatefunction_class) representing the 'maximum' aggregation.

### Example

    // Find the highest score in a leaderboard
    maximum(field("score")).as("highestScore");

### minimum(expression)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an aggregation that finds the minimum value of an expression across multiple stage inputs.

**Signature:**

    export declare function minimum(expression: Expression): AggregateFunction;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression to find the minimum value of. |

**Returns:**

[AggregateFunction](https://firebase.google.com/docs/reference/js/firestore_pipelines.aggregatefunction.md#aggregatefunction_class)

A new [AggregateFunction](https://firebase.google.com/docs/reference/js/firestore_pipelines.aggregatefunction.md#aggregatefunction_class) representing the 'minimum' aggregation.

### Example

    // Find the lowest price of all products
    minimum(field("price")).as("lowestPrice");

### mod(expression, value)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that calculates the modulo (remainder) of dividing an expression by a constant.

**Signature:**

    export declare function mod(expression: Expression, value: unknown): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The dividend expression. |
| value | unknown | The divisor constant. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the modulo operation.

### Example

    // Calculate the remainder of dividing 'field1' by 5.
    mod(field("field1"), 5);

### notEqual(expression, value)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if an expression is not equal to a constant value.

**Signature:**

    export declare function notEqual(expression: Expression, value: unknown): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression to compare. |
| value | unknown | The constant value to compare to. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `Expression` representing the inequality comparison.

### Example

    // Check if the 'status' field is not equal to "completed"
    notEqual(field("status"), "completed");

### round(expression)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that rounds a numeric value to the nearest whole number.

**Signature:**

    export declare function round(expression: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | An expression evaluating to a numeric value, which will be rounded. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the rounded value.

### Example

    // Round the value of the 'price' field.
    round(field("price"));

### round(expression, decimalPlaces)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that rounds a numeric value to the specified number of decimal places.

**Signature:**

    export declare function round(expression: Expression, decimalPlaces: number | Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | An expression evaluating to a numeric value, which will be rounded. |
| decimalPlaces | number \| [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | A constant or expression specifying the rounding precision in decimal places. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the rounded value.

### Example

    // Round the value of the 'price' field to two decimal places.
    round(field("price"), constant(2));

### rtrim(expression, valueToTrim)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Trims whitespace or a specified set of characters/bytes from the end of a string or byte array.

**Signature:**

    export declare function rtrim(expression: Expression, valueToTrim?: string | Expression | Bytes): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression representing the string or byte array. |
| valueToTrim | string \| [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| [Bytes](https://firebase.google.com/docs/reference/js/firestore_.bytes.md#bytes_class) | Optional. A string or byte array containing the characters/bytes to trim. If not specified, whitespace will be trimmed. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the trimmed string or byte array.

### Example

    // Trim whitespace from the end of the 'userInput' field
    rtrim(field("userInput"));

    // Trim quotes from the end of the 'userInput' field
    rtrim(field("userInput"), '"');

### split(expression, delimiter)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that splits a string into an array of substrings based on the provided delimiter.

**Signature:**

    export declare function split(expression: Expression, delimiter: string): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | Split the result of this expression. |
| delimiter | string | Split on this delimiter. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the split function.

### Example

    // Split the 'scoresCsv' field on delimiter ','
    split(field('scoresCsv'), ',')

### split(expression, delimiter)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that splits a string into an array of substrings based on the provided delimiter.

**Signature:**

    export declare function split(expression: Expression, delimiter: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | Split the result of this expression. |
| delimiter | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | Split on this delimiter returned by evaluating this expression. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the split function.

### Example

    // Split the 'scores' field on delimiter ',' or ':' depending on the stored format
    split(field('scores'), conditional(field('format').equal('csv'), constant(','), constant(':'))

### sqrt(expression)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that computes the square root of a numeric value.

**Signature:**

    export declare function sqrt(expression: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | An expression evaluating to a numeric value, which the square root will be computed for. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the square root of the numeric value.

### Example

    // Compute the square root of the 'value' field.
    sqrt(field("value"));

### stringIndexOf(expression, search)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that finds the index of the first occurrence of a substring or byte sequence.

**Signature:**

    export declare function stringIndexOf(expression: Expression, search: string | Expression | Bytes): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression representing the string or byte array. |
| search | string \| [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| [Bytes](https://firebase.google.com/docs/reference/js/firestore_.bytes.md#bytes_class) | The substring or byte sequence to search for. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the index of the first occurrence.

### Example

    // Find the index of "foo" in the 'text' field
    stringIndexOf(field("text"), "foo");

### stringRepeat(expression, repetitions)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that repeats a string or byte array a specified number of times.

**Signature:**

    export declare function stringRepeat(expression: Expression, repetitions: number | Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression representing the string or byte array. |
| repetitions | number \| [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The number of times to repeat the string or byte array. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the repeated string or byte array.

### Example

    // Repeat the 'label' field 3 times
    stringRepeat(field("label"), 3);

### stringReplaceAll(expression, find, replacement)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that replaces all occurrences of a substring or byte sequence with a replacement.

**Signature:**

    export declare function stringReplaceAll(expression: Expression, find: string | Expression | Bytes, replacement: string | Expression | Bytes): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression representing the string or byte array. |
| find | string \| [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| [Bytes](https://firebase.google.com/docs/reference/js/firestore_.bytes.md#bytes_class) | The substring or byte sequence to search for. |
| replacement | string \| [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| [Bytes](https://firebase.google.com/docs/reference/js/firestore_.bytes.md#bytes_class) | The replacement string or byte sequence. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the string or byte array with replacements.

### Example

    // Replace all occurrences of "foo" with "bar" in the 'text' field
    stringReplaceAll(field("text"), "foo", "bar");

### stringReplaceOne(expression, find, replacement)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that replaces the first occurrence of a substring or byte sequence with a replacement.

**Signature:**

    export declare function stringReplaceOne(expression: Expression, find: string | Expression | Bytes, replacement: string | Expression | Bytes): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression representing the string or byte array. |
| find | string \| [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| [Bytes](https://firebase.google.com/docs/reference/js/firestore_.bytes.md#bytes_class) | The substring or byte sequence to search for. |
| replacement | string \| [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| [Bytes](https://firebase.google.com/docs/reference/js/firestore_.bytes.md#bytes_class) | The replacement string or byte sequence. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the string or byte array with the replacement.

### Example

    // Replace the first occurrence of "foo" with "bar" in the 'text' field
    stringReplaceOne(field("text"), "foo", "bar");

### subtract(expression, value)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that subtracts a constant value from an expression.

**Signature:**

    export declare function subtract(expression: Expression, value: unknown): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression to subtract from. |
| value | unknown | The constant value to subtract. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the subtraction operation.

### Example

    // Subtract the constant value 2 from the 'value' field
    subtract(field("value"), 2);

### sum(expression)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an aggregation that calculates the sum of values from an expression across multiple stage inputs.

**Signature:**

    export declare function sum(expression: Expression): AggregateFunction;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression to sum up. |

**Returns:**

[AggregateFunction](https://firebase.google.com/docs/reference/js/firestore_pipelines.aggregatefunction.md#aggregatefunction_class)

A new [AggregateFunction](https://firebase.google.com/docs/reference/js/firestore_pipelines.aggregatefunction.md#aggregatefunction_class) representing the 'sum' aggregation.

### Example

    // Calculate the total revenue from a set of orders
    sum(field("orderAmount")).as("totalRevenue");

### trunc(expression)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that truncates the numeric value of an expression to an integer.

**Signature:**

    export declare function trunc(expression: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | An expression evaluating to a numeric value, which will be truncated. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the truncated value.

### Example

    // Truncate the value of the 'rating' field.
    trunc(field("rating"));

### trunc(expression, decimalPlaces)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that truncates a numeric value to the specified number of decimal places.

**Signature:**

    export declare function trunc(expression: Expression, decimalPlaces: number | Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | An expression evaluating to a numeric value, which will be truncated. |
| decimalPlaces | number \| [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | A constant or expression specifying the truncation precision in decimal places. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the truncated value.

### Example

    // Truncate the value of the 'rating' field to two decimal places.
    trunc(field("rating"), constant(2));

### type(expression)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns the data type of an expression's result.

**Signature:**

    export declare function type(expression: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) |   |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the data type.

### Example

    // Get the data type of a conditional expression
    type(conditional(exists('foo'), constant(1), constant(true)))

## function(field, ...)

### isAbsent(field)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns `true` if a field is absent. Otherwise, returns `false` even if the field value is `null`.

**Signature:**

    export declare function isAbsent(field: string): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| field | string | The field to check. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the 'isAbsent' check.

### Example

    // Check if the field `value` is absent.
    isAbsent("value");

### reverse(field)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that reverses a string value in the specified field.

**Signature:**

    export declare function reverse(field: string): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| field | string | The name of the field representing the string to reverse. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the reversed string.

### Example

    // Reverse the value of the 'myString' field.
    reverse("myString");

### stringReverse(field)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that reverses a string value in the specified field.

**Signature:**

    export declare function stringReverse(field: string): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| field | string | The name of the field representing the string to reverse. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the reversed string.

### Example

    // Reverse the value of the 'myString' field.
    strReverse("myString");

### substring(field, position, length)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns a substring of a string or byte array.

**Signature:**

    export declare function substring(field: string, position: number, length?: number): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| field | string | The name of a field containing a string or byte array to compute the substring from. |
| position | number | Index of the first character of the substring. |
| length | number | Length of the substring. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

### substring(field, position, length)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns a substring of a string or byte array.

**Signature:**

    export declare function substring(field: string, position: Expression, length?: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| field | string | The name of a field containing a string or byte array to compute the substring from. |
| position | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | An expression that returns the index of the first character of the substring. |
| length | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | An expression that returns the length of the substring. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

## function(fieldName, ...)

### abs(fieldName)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that computes the absolute value of a numeric value.

**Signature:**

    export declare function abs(fieldName: string): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The field to compute the absolute value of. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the absolute value of the numeric value.

### add(fieldName, second)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that adds a field's value to an expression.

**Signature:**

    export declare function add(fieldName: string, second: Expression | unknown): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field containing the value to add. |
| second | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| unknown | The second expression or literal to add. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the addition operation.

### Example

    // Add the value of the 'quantity' field and the 'reserve' field.
    add("quantity", field("reserve"));

### arrayAgg(fieldName)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an aggregation that collects all values of a field across multiple stage inputs into an array.

If the expression resolves to an absent value, it is converted to `null`. The order of elements in the output array is not stable and shouldn't be relied upon.

**Signature:**

    export declare function arrayAgg(fieldName: string): AggregateFunction;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field to collect values from. |

**Returns:**

[AggregateFunction](https://firebase.google.com/docs/reference/js/firestore_pipelines.aggregatefunction.md#aggregatefunction_class)

A new [AggregateFunction](https://firebase.google.com/docs/reference/js/firestore_pipelines.aggregatefunction.md#aggregatefunction_class) representing the 'array_agg' aggregation.

### Example

    // Collect all tags from books into an array
    arrayAgg("tags").as("allTags");

### arrayAggDistinct(fieldName)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an aggregation that collects all distinct values of a field across multiple stage inputs into an array.

If the expression resolves to an absent value, it is converted to `null`. The order of elements in the output array is not stable and shouldn't be relied upon.

**Signature:**

    export declare function arrayAggDistinct(fieldName: string): AggregateFunction;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field to collect values from. |

**Returns:**

[AggregateFunction](https://firebase.google.com/docs/reference/js/firestore_pipelines.aggregatefunction.md#aggregatefunction_class)

A new [AggregateFunction](https://firebase.google.com/docs/reference/js/firestore_pipelines.aggregatefunction.md#aggregatefunction_class) representing the 'array_agg_distinct' aggregation.

### Example

    // Collect all distinct tags from books into an array
    arrayAggDistinct("tags").as("allDistinctTags");

### arrayContains(fieldName, element)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if a field's array value contains a specific element.

**Signature:**

    export declare function arrayContains(fieldName: string, element: Expression): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The field name to check. |
| element | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The element to search for in the array. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the 'array_contains' comparison.

### Example

    // Check if the 'colors' array contains the value of field 'selectedColor'
    arrayContains("colors", field("selectedColor"));

### arrayContains(fieldName, element)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if a field's array value contains a specific value.

**Signature:**

    export declare function arrayContains(fieldName: string, element: unknown): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The field name to check. |
| element | unknown | The element to search for in the array. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the 'array_contains' comparison.

### Example

    // Check if the 'colors' array contains "red"
    arrayContains("colors", "red");

### arrayContainsAll(fieldName, values)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if a field's array value contains all the specified values or expressions.

**Signature:**

    export declare function arrayContainsAll(fieldName: string, values: Array<Expression | unknown>): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The field name to check. |
| values | Array\<[Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| unknown\> | The elements to check for in the array. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the 'array_contains_all' comparison.

### Example

    // Check if the 'tags' array contains both of the values from field 'tag1', the value "SciFi", and "Adventure"
    arrayContainsAll("tags", [field("tag1"), "SciFi", "Adventure"]);

### arrayContainsAll(fieldName, arrayExpression)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if a field's array value contains all the specified values or expressions.

**Signature:**

    export declare function arrayContainsAll(fieldName: string, arrayExpression: Expression): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The field name to check. |
| arrayExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The elements to check for in the array. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the 'array_contains_all' comparison.

### Example

    // Check if the 'tags' array contains both of the values from field 'tag1', the value "SciFi", and "Adventure"
    arrayContainsAll("tags", [field("tag1"), "SciFi", "Adventure"]);

### arrayContainsAny(fieldName, values)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if a field's array value contains any of the specified elements.

**Signature:**

    export declare function arrayContainsAny(fieldName: string, values: Array<Expression | unknown>): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The field name to check. |
| values | Array\<[Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| unknown\> | The elements to check for in the array. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the 'array_contains_any' comparison.

### Example

    // Check if the 'groups' array contains either the value from the 'userGroup' field
    // or the value "guest"
    arrayContainsAny("categories", [field("cate1"), "Science"]);

### arrayContainsAny(fieldName, values)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if a field's array value contains any of the specified elements.

**Signature:**

    export declare function arrayContainsAny(fieldName: string, values: Expression): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The field name to check. |
| values | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | An expression that evaluates to an array, whose elements to check for in the array field. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the 'array_contains_any' comparison.

### Example

    // Check if the 'groups' array contains either the value from the 'userGroup' field
    // or the value "guest"
    arrayContainsAny("categories", array([field("cate1"), "Science"]));

### arrayLength(fieldName)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that calculates the length of an array in a specified field.

**Signature:**

    export declare function arrayLength(fieldName: string): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field containing an array to calculate the length of. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the length of the array.

### Example

    // Get the number of items in field 'cart'
    arrayLength('cart');

### arraySum(fieldName)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that computes the sum of the elements in an array.

**Signature:**

    export declare function arraySum(fieldName: string): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field to compute the sum of. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the sum of the elements in the array.

### Example

    // Compute the sum of the elements in the 'scores' field.
    arraySum("scores");

### ascending(fieldName)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an [Ordering](https://firebase.google.com/docs/reference/js/firestore_pipelines.ordering.md#ordering_class) that sorts documents in ascending order based on a field.

**Signature:**

    export declare function ascending(fieldName: string): Ordering;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The field to create an ascending ordering for. |

**Returns:**

[Ordering](https://firebase.google.com/docs/reference/js/firestore_pipelines.ordering.md#ordering_class)

A new `Ordering` for ascending sorting.

### Example

    // Sort documents by the 'name' field in ascending order
    firestore.pipeline().collection("users")
      .sort(ascending("name"));

### average(fieldName)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an aggregation that calculates the average (mean) of a field's values across multiple stage inputs.

**Signature:**

    export declare function average(fieldName: string): AggregateFunction;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field containing numeric values to average. |

**Returns:**

[AggregateFunction](https://firebase.google.com/docs/reference/js/firestore_pipelines.aggregatefunction.md#aggregatefunction_class)

A new [AggregateFunction](https://firebase.google.com/docs/reference/js/firestore_pipelines.aggregatefunction.md#aggregatefunction_class) representing the 'average' aggregation.

### Example

    // Calculate the average age of users
    average("age").as("averageAge");

### byteLength(fieldName)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that calculates the length of a string represented by a field in UTF-8 bytes, or just the length of a Blob.

**Signature:**

    export declare function byteLength(fieldName: string): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field containing the string. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the length of the string in bytes.

### Example

    // Calculate the length of the 'myString' field in bytes.
    byteLength("myString");

### ceil(fieldName)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that computes the ceiling of a numeric value.

**Signature:**

    export declare function ceil(fieldName: string): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field to compute the ceiling of. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the ceiling of the numeric value.

### Example

    // Compute the ceiling of the 'price' field.
    ceil("price");

### charLength(fieldName)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that calculates the character length of a string field in UTF8.

**Signature:**

    export declare function charLength(fieldName: string): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field containing the string. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the length of the string.

### Example

    // Get the character length of the 'name' field in UTF-8.
    strLength("name");

### collectionId(fieldName)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns the collection ID from a path.

**Signature:**

    export declare function collectionId(fieldName: string): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field to get the collection ID from. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the collectionId operation.

### Example

    // Get the collection ID from a path.
    collectionId("__name__");

### concat(fieldName, second, others)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that concatenates strings, arrays, or blobs. Types cannot be mixed.

**Signature:**

    export declare function concat(fieldName: string, second: Expression | unknown, ...others: Array<Expression | unknown>): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of a field to concatenate. |
| second | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| unknown | The second literal or expression to concatenate. |
| others | Array\<[Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| unknown\> | Additional literal or expressions to concatenate. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the concatenation.

### Example

    // Concatenate a field with a literal string.
    concat(field("firstName"), "Doe")

### cosineDistance(fieldName, vector)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Calculates the Cosine distance between a field's vector value and a literal vector value.

**Signature:**

    export declare function cosineDistance(fieldName: string, vector: number[] | VectorValue): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field containing the first vector. |
| vector | number\[\] \| [VectorValue](https://firebase.google.com/docs/reference/js/firestore_.vectorvalue.md#vectorvalue_class) | The other vector (as an array of doubles) or [VectorValue](https://firebase.google.com/docs/reference/js/firestore_.vectorvalue.md#vectorvalue_class) to compare against. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the Cosine distance between the two vectors.

### Example

    // Calculate the Cosine distance between the 'location' field and a target location
    cosineDistance("location", [37.7749, -122.4194]);

### cosineDistance(fieldName, vectorExpression)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Calculates the Cosine distance between a field's vector value and a vector expression.

**Signature:**

    export declare function cosineDistance(fieldName: string, vectorExpression: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field containing the first vector. |
| vectorExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The other vector (represented as an `Expression`) to compare against. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the cosine distance between the two vectors.

### Example

    // Calculate the cosine distance between the 'userVector' field and the 'itemVector' field
    cosineDistance("userVector", field("itemVector"));

### count(fieldName)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an aggregation that counts the number of stage inputs where the input field exists.

**Signature:**

    export declare function count(fieldName: string): AggregateFunction;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field to count. |

**Returns:**

[AggregateFunction](https://firebase.google.com/docs/reference/js/firestore_pipelines.aggregatefunction.md#aggregatefunction_class)

A new [AggregateFunction](https://firebase.google.com/docs/reference/js/firestore_pipelines.aggregatefunction.md#aggregatefunction_class) representing the 'count' aggregation.

### Example

    // Count the total number of products
    count("productId").as("totalProducts");

### descending(fieldName)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an [Ordering](https://firebase.google.com/docs/reference/js/firestore_pipelines.ordering.md#ordering_class) that sorts documents in descending order based on a field.

**Signature:**

    export declare function descending(fieldName: string): Ordering;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The field to create a descending ordering for. |

**Returns:**

[Ordering](https://firebase.google.com/docs/reference/js/firestore_pipelines.ordering.md#ordering_class)

A new `Ordering` for descending sorting.

### Example

    // Sort documents by the 'name' field in descending order
    firestore.pipeline().collection("users")
      .sort(descending("name"));

### divide(fieldName, expressions)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that divides a field's value by an expression.

**Signature:**

    export declare function divide(fieldName: string, expressions: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The field name to be divided. |
| expressions | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression to divide by. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the division operation.

### Example

    // Divide the 'total' field by the 'count' field
    divide("total", field("count"));

### divide(fieldName, value)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that divides a field's value by a constant value.

**Signature:**

    export declare function divide(fieldName: string, value: unknown): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The field name to be divided. |
| value | unknown | The constant value to divide by. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the division operation.

### Example

    // Divide the 'value' field by 10
    divide("value", 10);

### dotProduct(fieldName, vector)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Calculates the dot product between a field's vector value and a double array.

**Signature:**

    export declare function dotProduct(fieldName: string, vector: number[] | VectorValue): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field containing the first vector. |
| vector | number\[\] \| [VectorValue](https://firebase.google.com/docs/reference/js/firestore_.vectorvalue.md#vectorvalue_class) | The other vector (as an array of doubles or VectorValue) to calculate with. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the dot product between the two vectors.

### Example

    // Calculate the dot product distance between a feature vector and a target vector
    dotProduct("features", [0.5, 0.8, 0.2]);

### dotProduct(fieldName, vectorExpression)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Calculates the dot product between a field's vector value and a vector expression.

**Signature:**

    export declare function dotProduct(fieldName: string, vectorExpression: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field containing the first vector. |
| vectorExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The other vector (represented as an `Expression`) to calculate with. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the dot product between the two vectors.

### Example

    // Calculate the dot product distance between two document vectors: 'docVector1' and 'docVector2'
    dotProduct("docVector1", field("docVector2"));

### endsWith(fieldName, suffix)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if a field's value ends with a given postfix.

**Signature:**

    export declare function endsWith(fieldName: string, suffix: string): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The field name to check. |
| suffix | string | The postfix to check for. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the 'ends with' comparison.

### Example

    // Check if the 'filename' field ends with ".txt"
    endsWith("filename", ".txt");

### endsWith(fieldName, suffix)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if a field's value ends with a given postfix.

**Signature:**

    export declare function endsWith(fieldName: string, suffix: Expression): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The field name to check. |
| suffix | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression representing the postfix. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the 'ends with' comparison.

### Example

    // Check if the 'url' field ends with the value of the 'extension' field
    endsWith("url", field("extension"));

### equal(fieldName, expression)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if a field's value is equal to an expression.

**Signature:**

    export declare function equal(fieldName: string, expression: Expression): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The field name to compare. |
| expression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression to compare to. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `Expression` representing the equality comparison.

### Example

    // Check if the 'age' field is equal to the 'limit' field
    equal("age", field("limit"));

### equal(fieldName, value)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if a field's value is equal to a constant value.

**Signature:**

    export declare function equal(fieldName: string, value: unknown): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The field name to compare. |
| value | unknown | The constant value to compare to. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `Expression` representing the equality comparison.

### Example

    // Check if the 'city' field is equal to string constant "London"
    equal("city", "London");

### equalAny(fieldName, values)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if a field's value is equal to any of the provided values or expressions.

**Signature:**

    export declare function equalAny(fieldName: string, values: Array<Expression | unknown>): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The field to compare. |
| values | Array\<[Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| unknown\> | The values to check against. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the 'IN' comparison.

### Example

    // Check if the 'category' field is either "Electronics" or value of field 'primaryType'
    equalAny("category", [constant("Electronics"), field("primaryType")]);

### equalAny(fieldName, arrayExpression)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if a field's value is equal to any of the provided values or expressions.

**Signature:**

    export declare function equalAny(fieldName: string, arrayExpression: Expression): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The field to compare. |
| arrayExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | An expression that evaluates to an array, whose elements to check for equality to the input field. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the 'IN' comparison.

### Example

    // Check if the 'category' field is either "Electronics" or value of field 'primaryType'
    equalAny("category", ["Electronics", field("primaryType")]);

### euclideanDistance(fieldName, vector)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Calculates the Euclidean distance between a field's vector value and a double array.

**Signature:**

    export declare function euclideanDistance(fieldName: string, vector: number[] | VectorValue): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field containing the first vector. |
| vector | number\[\] \| [VectorValue](https://firebase.google.com/docs/reference/js/firestore_.vectorvalue.md#vectorvalue_class) | The other vector (as an array of doubles or VectorValue) to compare against. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the Euclidean distance between the two vectors.

### Example

    // Calculate the Euclidean distance between the 'location' field and a target location
    euclideanDistance("location", [37.7749, -122.4194]);

### euclideanDistance(fieldName, vectorExpression)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Calculates the Euclidean distance between a field's vector value and a vector expression.

**Signature:**

    export declare function euclideanDistance(fieldName: string, vectorExpression: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field containing the first vector. |
| vectorExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The other vector (represented as an `Expression`) to compare against. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the Euclidean distance between the two vectors.

### Example

    // Calculate the Euclidean distance between two vector fields: 'pointA' and 'pointB'
    euclideanDistance("pointA", field("pointB"));

### exists(fieldName)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if a field exists.

**Signature:**

    export declare function exists(fieldName: string): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The field name to check. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the 'exists' check.

### Example

    // Check if the document has a field named "phoneNumber"
    exists("phoneNumber");

### exp(fieldName)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that computes e to the power of the expression's result.

**Signature:**

    export declare function exp(fieldName: string): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string |   |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the exp of the numeric value.

### Example

    // Compute e to the power of the 'value' field.
    exp('value');

### first(fieldName)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an aggregation that finds the first value of a field across multiple stage inputs.

**Signature:**

    export declare function first(fieldName: string): AggregateFunction;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field to find the first value of. |

**Returns:**

[AggregateFunction](https://firebase.google.com/docs/reference/js/firestore_pipelines.aggregatefunction.md#aggregatefunction_class)

A new [AggregateFunction](https://firebase.google.com/docs/reference/js/firestore_pipelines.aggregatefunction.md#aggregatefunction_class) representing the 'first' aggregation.

### Example

    // Find the first value of the 'rating' field
    first("rating").as("firstRating");

### floor(fieldName)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that computes the floor of a numeric value.

**Signature:**

    export declare function floor(fieldName: string): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field to compute the floor of. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the floor of the numeric value.

### greaterThan(fieldName, expression)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if a field's value is greater than an expression.

**Signature:**

    export declare function greaterThan(fieldName: string, expression: Expression): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The field name to compare. |
| expression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression to compare to. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `Expression` representing the greater than comparison.

### Example

    // Check if the value of field 'age' is greater than the value of field 'limit'
    greaterThan("age", field("limit"));

### greaterThan(fieldName, value)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if a field's value is greater than a constant value.

**Signature:**

    export declare function greaterThan(fieldName: string, value: unknown): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The field name to compare. |
| value | unknown | The constant value to compare to. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `Expression` representing the greater than comparison.

### Example

    // Check if the 'price' field is greater than 100
    greaterThan("price", 100);

### greaterThanOrEqual(fieldName, value)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if a field's value is greater than or equal to an expression.

**Signature:**

    export declare function greaterThanOrEqual(fieldName: string, value: Expression): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The field name to compare. |
| value | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression to compare to. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `Expression` representing the greater than or equal to comparison.

### Example

    // Check if the value of field 'age' is greater than or equal to the value of field 'limit'
    greaterThanOrEqual("age", field("limit"));

### greaterThanOrEqual(fieldName, value)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if a field's value is greater than or equal to a constant value.

**Signature:**

    export declare function greaterThanOrEqual(fieldName: string, value: unknown): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The field name to compare. |
| value | unknown | The constant value to compare to. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `Expression` representing the greater than or equal to comparison.

### Example

    // Check if the 'score' field is greater than or equal to 80
    greaterThanOrEqual("score", 80);

### isType(fieldName, type)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if the value in the specified field is of the given type.

Null or undefined fields evaluate to skip/error. Use `ifAbsent()` / `isAbsent()` to evaluate missing data.

**Signature:**

    export declare function isType(fieldName: string, type: Type): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field to check. |
| type | [Type](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#type) | The type to check for. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `BooleanExpression` that evaluates to true if the field's value is of the given type, false otherwise.

### Example

    // Check if the 'price' field is a floating point number (evaluating to true inside pipeline conditionals)
    isType('price', 'float64');

### last(fieldName)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an aggregation that finds the last value of a field across multiple stage inputs.

**Signature:**

    export declare function last(fieldName: string): AggregateFunction;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field to find the last value of. |

**Returns:**

[AggregateFunction](https://firebase.google.com/docs/reference/js/firestore_pipelines.aggregatefunction.md#aggregatefunction_class)

A new [AggregateFunction](https://firebase.google.com/docs/reference/js/firestore_pipelines.aggregatefunction.md#aggregatefunction_class) representing the 'last' aggregation.

### Example

    // Find the last value of the 'rating' field
    last("rating").as("lastRating");

### length_2(fieldName)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that calculates the length of a string, array, map, vector, or bytes.

**Signature:**

    declare function length_2(fieldName: string): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field to calculate the length of. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the length of the string, array, map, vector, or bytes.

### Example

    // Get the length of the 'name' field.
    length("name");

    // Get the number of items in the 'cart' array.
    length("cart");

### lessThan(fieldName, expression)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if a field's value is less than an expression.

**Signature:**

    export declare function lessThan(fieldName: string, expression: Expression): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The field name to compare. |
| expression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression to compare to. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `Expression` representing the less than comparison.

### Example

    // Check if the 'age' field is less than the 'limit' field
    lessThan("age", field("limit"));

### lessThan(fieldName, value)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if a field's value is less than a constant value.

**Signature:**

    export declare function lessThan(fieldName: string, value: unknown): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The field name to compare. |
| value | unknown | The constant value to compare to. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `Expression` representing the less than comparison.

### Example

    // Check if the 'price' field is less than 50
    lessThan("price", 50);

### lessThanOrEqual(fieldName, expression)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if a field's value is less than or equal to an expression.

**Signature:**

    export declare function lessThanOrEqual(fieldName: string, expression: Expression): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The field name to compare. |
| expression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression to compare to. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `Expression` representing the less than or equal to comparison.

### Example

    // Check if the 'quantity' field is less than or equal to the 'limit' field
    lessThan("quantity", field("limit"));

### lessThanOrEqual(fieldName, value)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if a field's value is less than or equal to a constant value.

**Signature:**

    export declare function lessThanOrEqual(fieldName: string, value: unknown): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The field name to compare. |
| value | unknown | The constant value to compare to. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `Expression` representing the less than or equal to comparison.

### Example

    // Check if the 'score' field is less than or equal to 70
    lessThan("score", 70);

### like(fieldName, pattern)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that performs a case-sensitive wildcard string comparison against a field.

**Signature:**

    export declare function like(fieldName: string, pattern: string): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field containing the string. |
| pattern | string | The pattern to search for. You can use "%" as a wildcard character. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the 'like' comparison.

### Example

    // Check if the 'title' field contains the string "guide"
    like("title", "%guide%");

### like(fieldName, pattern)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that performs a case-sensitive wildcard string comparison against a field.

**Signature:**

    export declare function like(fieldName: string, pattern: Expression): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field containing the string. |
| pattern | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The pattern to search for. You can use "%" as a wildcard character. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the 'like' comparison.

### Example

    // Check if the 'title' field contains the string "guide"
    like("title", field("pattern"));

### ln(fieldName)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that computes the natural logarithm of a numeric value.

**Signature:**

    export declare function ln(fieldName: string): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field to compute the natural logarithm of. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the natural logarithm of the numeric value.

### Example

    // Compute the natural logarithm of the 'value' field.
    ln("value");

### log(fieldName, base)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that computes the logarithm of a field to a given base.

**Signature:**

    export declare function log(fieldName: string, base: number): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field to compute the logarithm of. |
| base | number | The base of the logarithm. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the logarithm of the numeric value.

### Example

    // Compute the logarithm of the 'value' field with base 10.
    log("value", 10);

### log(fieldName, base)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that computes the logarithm of a field to a given base.

**Signature:**

    export declare function log(fieldName: string, base: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field to compute the logarithm of. |
| base | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The base of the logarithm. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the logarithm of the numeric value.

### Example

    // Compute the logarithm of the 'value' field with the base in the 'base' field.
    log("value", field("base"));

### log10(fieldName)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that computes the base-10 logarithm of a numeric value.

**Signature:**

    export declare function log10(fieldName: string): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field to compute the base-10 logarithm of. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the base-10 logarithm of the numeric value.

### Example

    // Compute the base-10 logarithm of the 'value' field.
    log10("value");

### logicalMaximum(fieldName, second, others)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns the largest value between multiple input expressions or literal values. Based on Firestore's value type ordering.

**Signature:**

    export declare function logicalMaximum(fieldName: string, second: Expression | unknown, ...others: Array<Expression | unknown>): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The first operand field name. |
| second | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| unknown | The second expression or literal. |
| others | Array\<[Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| unknown\> | Optional additional expressions or literals. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the logical maximum operation.

### Example

    // Returns the largest value between the 'field1' field, the 'field2' field,
    // and 1000.
    logicalMaximum("field1", field("field2"), 1000);

### logicalMinimum(fieldName, second, others)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns the smallest value between a field's value and other input expressions or literal values. Based on Firestore's value type ordering.

**Signature:**

    export declare function logicalMinimum(fieldName: string, second: Expression | unknown, ...others: Array<Expression | unknown>): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The first operand field name. |
| second | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| unknown | The second expression or literal. |
| others | Array\<[Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| unknown\> | Optional additional expressions or literals. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the logical minimum operation.

### Example

    // Returns the smallest value between the 'field1' field, the 'field2' field,
    // and 1000.
    logicalMinimum("field1", field("field2"), 1000);

### ltrim(fieldName, valueToTrim)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Trims whitespace or a specified set of characters/bytes from the beginning of a string or byte array.

**Signature:**

    export declare function ltrim(fieldName: string, valueToTrim?: string | Expression | Bytes): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field containing the string or byte array. |
| valueToTrim | string \| [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| [Bytes](https://firebase.google.com/docs/reference/js/firestore_.bytes.md#bytes_class) | Optional. A string or byte array containing the characters/bytes to trim. If not specified, whitespace will be trimmed. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the trimmed string or byte array.

### Example

    // Trim whitespace from the beginning of the 'userInput' field
    ltrim(field("userInput"));

    // Trim quotes from the beginning of the 'userInput' field
    ltrim(field("userInput"), '"');

### mapGet(fieldName, subField)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Accesses a value from a map (object) field using the provided key.

**Signature:**

    export declare function mapGet(fieldName: string, subField: string): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The field name of the map field. |
| subField | string | The key to access in the map. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the value associated with the given key in the map.

### Example

    // Get the 'city' value from the 'address' map field
    mapGet("address", "city");

### maximum(fieldName)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an aggregation that finds the maximum value of a field across multiple stage inputs.

**Signature:**

    export declare function maximum(fieldName: string): AggregateFunction;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field to find the maximum value of. |

**Returns:**

[AggregateFunction](https://firebase.google.com/docs/reference/js/firestore_pipelines.aggregatefunction.md#aggregatefunction_class)

A new [AggregateFunction](https://firebase.google.com/docs/reference/js/firestore_pipelines.aggregatefunction.md#aggregatefunction_class) representing the 'maximum' aggregation.

### Example

    // Find the highest score in a leaderboard
    maximum("score").as("highestScore");

### minimum(fieldName)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an aggregation that finds the minimum value of a field across multiple stage inputs.

**Signature:**

    export declare function minimum(fieldName: string): AggregateFunction;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field to find the minimum value of. |

**Returns:**

[AggregateFunction](https://firebase.google.com/docs/reference/js/firestore_pipelines.aggregatefunction.md#aggregatefunction_class)

A new [AggregateFunction](https://firebase.google.com/docs/reference/js/firestore_pipelines.aggregatefunction.md#aggregatefunction_class) representing the 'minimum' aggregation.

### Example

    // Find the lowest price of all products
    minimum("price").as("lowestPrice");

### mod(fieldName, expression)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that calculates the modulo (remainder) of dividing a field's value by an expression.

**Signature:**

    export declare function mod(fieldName: string, expression: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The dividend field name. |
| expression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The divisor expression. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the modulo operation.

### Example

    // Calculate the remainder of dividing 'field1' by 'field2'.
    mod("field1", field("field2"));

### mod(fieldName, value)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that calculates the modulo (remainder) of dividing a field's value by a constant.

**Signature:**

    export declare function mod(fieldName: string, value: unknown): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The dividend field name. |
| value | unknown | The divisor constant. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the modulo operation.

### Example

    // Calculate the remainder of dividing 'field1' by 5.
    mod("field1", 5);

### multiply(fieldName, second)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that multiplies a field's value by an expression.

**Signature:**

    export declare function multiply(fieldName: string, second: Expression | unknown): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field containing the value to add. |
| second | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| unknown | The second expression or literal to add. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the multiplication operation.

### Example

    // Multiply the 'quantity' field by the 'price' field
    multiply("quantity", field("price"));

### notEqual(fieldName, expression)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if a field's value is not equal to an expression.

**Signature:**

    export declare function notEqual(fieldName: string, expression: Expression): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The field name to compare. |
| expression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression to compare to. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `Expression` representing the inequality comparison.

### Example

    // Check if the 'status' field is not equal to the value of 'expectedStatus'
    notEqual("status", field("expectedStatus"));

### notEqual(fieldName, value)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if a field's value is not equal to a constant value.

**Signature:**

    export declare function notEqual(fieldName: string, value: unknown): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The field name to compare. |
| value | unknown | The constant value to compare to. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `Expression` representing the inequality comparison.

### Example

    // Check if the 'country' field is not equal to "USA"
    notEqual("country", "USA");

### notEqualAny(fieldName, values)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if a field's value is not equal to any of the provided values or expressions.

**Signature:**

    export declare function notEqualAny(fieldName: string, values: Array<Expression | unknown>): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The field name to compare. |
| values | Array\<[Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| unknown\> | The values to check against. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the 'NOT IN' comparison.

### Example

    // Check if the 'status' field is neither "pending" nor the value of 'rejectedStatus'
    notEqualAny("status", [constant("pending"), field("rejectedStatus")]);

### notEqualAny(fieldName, arrayExpression)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if a field's value is not equal to any of the values in the evaluated expression.

**Signature:**

    export declare function notEqualAny(fieldName: string, arrayExpression: Expression): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The field name to compare. |
| arrayExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The values to check against. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the 'NOT IN' comparison.

### Example

    // Check if the 'status' field is not equal to any value in the field 'rejectedStatuses'
    notEqualAny("status", field("rejectedStatuses"));

### regexContains(fieldName, pattern)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if a string field contains a specified regular expression as a substring.

**Signature:**

    export declare function regexContains(fieldName: string, pattern: string): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field containing the string. |
| pattern | string | The regular expression to use for the search. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the 'contains' comparison.

### Example

    // Check if the 'description' field contains "example" (case-insensitive)
    regexContains("description", "(?i)example");

### regexContains(fieldName, pattern)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if a string field contains a specified regular expression as a substring.

**Signature:**

    export declare function regexContains(fieldName: string, pattern: Expression): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field containing the string. |
| pattern | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The regular expression to use for the search. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the 'contains' comparison.

### Example

    // Check if the 'description' field contains "example" (case-insensitive)
    regexContains("description", field("pattern"));

### regexFind(fieldName, pattern)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns the first substring of a string field that matches a specified regular expression.

This expression uses the [RE2](https://github.com/google/re2/wiki/Syntax) regular expression syntax.

**Signature:**

    export declare function regexFind(fieldName: string, pattern: string): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field containing the string to search. |
| pattern | string | The regular expression to search for. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the regular expression find function.

### Example

    // Extract the domain name from an email field
    regexFind("email", "@[A-Za-z0-9.-]+");

### regexFind(fieldName, pattern)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns the first substring of a string field that matches a specified regular expression.

This expression uses the [RE2](https://github.com/google/re2/wiki/Syntax) regular expression syntax.

**Signature:**

    export declare function regexFind(fieldName: string, pattern: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field containing the string to search. |
| pattern | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The regular expression to search for. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the regular expression find function.

### Example

    // Extract a substring from 'email' based on a pattern stored in another field
    regexFind("email", field("pattern"));

### regexFindAll(fieldName, pattern)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that evaluates to a list of all substrings in a string field that match a specified regular expression.

This expression uses the [RE2](https://github.com/google/re2/wiki/Syntax) regular expression syntax.

**Signature:**

    export declare function regexFindAll(fieldName: string, pattern: string): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field containing the string to search. |
| pattern | string | The regular expression to search for. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class) that evaluates to an array of matched substrings.

### Example

    // Extract all hashtags from a post content field
    regexFindAll("content", "#[A-Za-z0-9_]+");

### regexFindAll(fieldName, pattern)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that evaluates to a list of all substrings in a string field that match a specified regular expression.

This expression uses the [RE2](https://github.com/google/re2/wiki/Syntax) regular expression syntax.

**Signature:**

    export declare function regexFindAll(fieldName: string, pattern: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field containing the string to search. |
| pattern | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The regular expression to search for. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class) that evaluates to an array of matched substrings.

### Example

    // Extract all matches from 'content' based on a pattern stored in another field
    regexFindAll("content", field("pattern"));

### regexMatch(fieldName, pattern)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if a string field matches a specified regular expression.

**Signature:**

    export declare function regexMatch(fieldName: string, pattern: string): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field containing the string. |
| pattern | string | The regular expression to use for the match. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the regular expression match.

### Example

    // Check if the 'email' field matches a valid email pattern
    regexMatch("email", "[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}");

### regexMatch(fieldName, pattern)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if a string field matches a specified regular expression.

**Signature:**

    export declare function regexMatch(fieldName: string, pattern: Expression): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field containing the string. |
| pattern | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The regular expression to use for the match. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the regular expression match.

### Example

    // Check if the 'email' field matches a valid email pattern
    regexMatch("email", field("pattern"));

### round(fieldName)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that rounds a numeric value to the nearest whole number.

**Signature:**

    export declare function round(fieldName: string): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field to round. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the rounded value.

### Example

    // Round the value of the 'price' field.
    round("price");

### round(fieldName, decimalPlaces)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that rounds a numeric value to the specified number of decimal places.

**Signature:**

    export declare function round(fieldName: string, decimalPlaces: number | Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field to round. |
| decimalPlaces | number \| [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | A constant or expression specifying the rounding precision in decimal places. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the rounded value.

### Example

    // Round the value of the 'price' field to two decimal places.
    round("price", 2);

### rtrim(fieldName, valueToTrim)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Trims whitespace or a specified set of characters/bytes from the end of a string or byte array.

**Signature:**

    export declare function rtrim(fieldName: string, valueToTrim?: string | Expression | Bytes): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field containing the string or byte array. |
| valueToTrim | string \| [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| [Bytes](https://firebase.google.com/docs/reference/js/firestore_.bytes.md#bytes_class) | Optional. A string or byte array containing the characters/bytes to trim. If not specified, whitespace will be trimmed. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the trimmed string or byte array.

### Example

    // Trim whitespace from the end of the 'userInput' field
    rtrim(field("userInput"));

    // Trim quotes from the end of the 'userInput' field
    rtrim(field("userInput"), '"');

### split(fieldName, delimiter)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that splits the value of a field on the provided delimiter.

**Signature:**

    export declare function split(fieldName: string, delimiter: string): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | Split the value in this field. |
| delimiter | string | Split on this delimiter. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the split function.

### Example

    // Split the 'scoresCsv' field on delimiter ','
    split('scoresCsv', ',')

### split(fieldName, delimiter)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that splits the value of a field on the provided delimiter.

**Signature:**

    export declare function split(fieldName: string, delimiter: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | Split the value in this field. |
| delimiter | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | Split on this delimiter returned by evaluating this expression. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the split function.

### Example

    // Split the 'scores' field on delimiter ',' or ':' depending on the stored format
    split('scores', conditional(field('format').equal('csv'), constant(','), constant(':'))

### sqrt(fieldName)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that computes the square root of a numeric value.

**Signature:**

    export declare function sqrt(fieldName: string): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field to compute the square root of. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the square root of the numeric value.

### Example

    // Compute the square root of the 'value' field.
    sqrt("value");

### startsWith(fieldName, prefix)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if a field's value starts with a given prefix.

**Signature:**

    export declare function startsWith(fieldName: string, prefix: string): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The field name to check. |
| prefix | string | The prefix to check for. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the 'starts with' comparison.

### Example

    // Check if the 'name' field starts with "Mr."
    startsWith("name", "Mr.");

### startsWith(fieldName, prefix)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if a field's value starts with a given prefix.

**Signature:**

    export declare function startsWith(fieldName: string, prefix: Expression): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The field name to check. |
| prefix | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression representing the prefix. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the 'starts with' comparison.

### Example

    // Check if the 'fullName' field starts with the value of the 'firstName' field
    startsWith("fullName", field("firstName"));

### stringConcat(fieldName, secondString, otherStrings)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that concatenates string functions, fields or constants together.

**Signature:**

    export declare function stringConcat(fieldName: string, secondString: Expression | string, ...otherStrings: Array<Expression | string>): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The field name containing the initial string value. |
| secondString | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| string | An expression or string literal to concatenate. |
| otherStrings | Array\<[Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| string\> | Optional additional expressions or literals (typically strings) to concatenate. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the concatenated string.

### Example

    // Combine the 'firstName', " ", and 'lastName' fields into a single string
    stringConcat("firstName", " ", field("lastName"));

### stringContains(fieldName, substring)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if a string field contains a specified substring.

**Signature:**

    export declare function stringContains(fieldName: string, substring: string): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field containing the string. |
| substring | string | The substring to search for. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the 'contains' comparison.

### Example

    // Check if the 'description' field contains "example".
    stringContains("description", "example");

### stringContains(fieldName, substring)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if a string field contains a substring specified by an expression.

**Signature:**

    export declare function stringContains(fieldName: string, substring: Expression): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field containing the string. |
| substring | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression representing the substring to search for. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the 'contains' comparison.

### Example

    // Check if the 'description' field contains the value of the 'keyword' field.
    stringContains("description", field("keyword"));

### stringIndexOf(fieldName, search)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that finds the index of the first occurrence of a substring or byte sequence.

**Signature:**

    export declare function stringIndexOf(fieldName: string, search: string | Expression | Bytes): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field containing the string or byte array. |
| search | string \| [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| [Bytes](https://firebase.google.com/docs/reference/js/firestore_.bytes.md#bytes_class) | The substring or byte sequence to search for. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the index of the first occurrence.

### Example

    // Find the index of "foo" in the 'text' field
    stringIndexOf("text", "foo");

### stringRepeat(fieldName, repetitions)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that repeats a string or byte array a specified number of times.

**Signature:**

    export declare function stringRepeat(fieldName: string, repetitions: number | Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field containing the string or byte array. |
| repetitions | number \| [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The number of times to repeat the string or byte array. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the repeated string or byte array.

### Example

    // Repeat the 'label' field 3 times
    stringRepeat("label", 3);

### stringReplaceAll(fieldName, find, replacement)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that replaces all occurrences of a substring or byte sequence with a replacement.

**Signature:**

    export declare function stringReplaceAll(fieldName: string, find: string | Expression | Bytes, replacement: string | Expression | Bytes): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field containing the string or byte array. |
| find | string \| [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| [Bytes](https://firebase.google.com/docs/reference/js/firestore_.bytes.md#bytes_class) | The substring or byte sequence to search for. |
| replacement | string \| [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| [Bytes](https://firebase.google.com/docs/reference/js/firestore_.bytes.md#bytes_class) | The replacement string or byte sequence. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the string or byte array with replacements.

### Example

    // Replace all occurrences of "foo" with "bar" in the 'text' field
    stringReplaceAll("text", "foo", "bar");

### stringReplaceOne(fieldName, find, replacement)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that replaces the first occurrence of a substring or byte sequence with a replacement.

**Signature:**

    export declare function stringReplaceOne(fieldName: string, find: string | Expression | Bytes, replacement: string | Expression | Bytes): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field containing the string or byte array. |
| find | string \| [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| [Bytes](https://firebase.google.com/docs/reference/js/firestore_.bytes.md#bytes_class) | The substring or byte sequence to search for. |
| replacement | string \| [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| [Bytes](https://firebase.google.com/docs/reference/js/firestore_.bytes.md#bytes_class) | The replacement string or byte sequence. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the string or byte array with the replacement.

### Example

    // Replace the first occurrence of "foo" with "bar" in the 'text' field
    stringReplaceOne("text", "foo", "bar");

### subtract(fieldName, expression)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that subtracts an expression from a field's value.

**Signature:**

    export declare function subtract(fieldName: string, expression: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The field name to subtract from. |
| expression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression to subtract. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the subtraction operation.

### Example

    // Subtract the 'discount' field from the 'price' field
    subtract("price", field("discount"));

### subtract(fieldName, value)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that subtracts a constant value from a field's value.

**Signature:**

    export declare function subtract(fieldName: string, value: unknown): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The field name to subtract from. |
| value | unknown | The constant value to subtract. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the subtraction operation.

### Example

    // Subtract 20 from the value of the 'total' field
    subtract("total", 20);

### sum(fieldName)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an aggregation that calculates the sum of a field's values across multiple stage inputs.

**Signature:**

    export declare function sum(fieldName: string): AggregateFunction;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field containing numeric values to sum up. |

**Returns:**

[AggregateFunction](https://firebase.google.com/docs/reference/js/firestore_pipelines.aggregatefunction.md#aggregatefunction_class)

A new [AggregateFunction](https://firebase.google.com/docs/reference/js/firestore_pipelines.aggregatefunction.md#aggregatefunction_class) representing the 'sum' aggregation.

### Example

    // Calculate the total revenue from a set of orders
    sum("orderAmount").as("totalRevenue");

### timestampAdd(fieldName, unit, amount)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that adds a specified amount of time to a timestamp represented by a field.

**Signature:**

    export declare function timestampAdd(fieldName: string, unit: 'microsecond' | 'millisecond' | 'second' | 'minute' | 'hour' | 'day', amount: number): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field representing the timestamp. |
| unit | 'microsecond' \| 'millisecond' \| 'second' \| 'minute' \| 'hour' \| 'day' | The unit of time to add (e.g., "day", "hour"). |
| amount | number | The amount of time to add. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the resulting timestamp.

### Example

    // Add 1 day to the 'timestamp' field.
    timestampAdd("timestamp", "day", 1);

### timestampSubtract(fieldName, unit, amount)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that subtracts a specified amount of time from a timestamp represented by a field.

**Signature:**

    export declare function timestampSubtract(fieldName: string, unit: 'microsecond' | 'millisecond' | 'second' | 'minute' | 'hour' | 'day', amount: number): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field representing the timestamp. |
| unit | 'microsecond' \| 'millisecond' \| 'second' \| 'minute' \| 'hour' \| 'day' | The unit of time to subtract (e.g., "day", "hour"). |
| amount | number | The amount of time to subtract. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the resulting timestamp.

### Example

    // Subtract 1 day from the 'timestamp' field.
    timestampSubtract("timestamp", "day", 1);

### timestampToUnixMicros(fieldName)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that converts a timestamp field to the number of microseconds since the Unix epoch (1970-01-01 00:00:00 UTC).

**Signature:**

    export declare function timestampToUnixMicros(fieldName: string): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field representing the timestamp. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the number of microseconds since epoch.

### Example

    // Convert the 'timestamp' field to microseconds since epoch.
    timestampToUnixMicros("timestamp");

### timestampToUnixMillis(fieldName)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that converts a timestamp field to the number of milliseconds since the Unix epoch (1970-01-01 00:00:00 UTC).

**Signature:**

    export declare function timestampToUnixMillis(fieldName: string): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field representing the timestamp. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the number of milliseconds since epoch.

### Example

    // Convert the 'timestamp' field to milliseconds since epoch.
    timestampToUnixMillis("timestamp");

### timestampToUnixSeconds(fieldName)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that converts a timestamp field to the number of seconds since the Unix epoch (1970-01-01 00:00:00 UTC).

**Signature:**

    export declare function timestampToUnixSeconds(fieldName: string): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field representing the timestamp. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the number of seconds since epoch.

### Example

    // Convert the 'timestamp' field to seconds since epoch.
    timestampToUnixSeconds("timestamp");

### timestampTruncate(fieldName, granularity, timezone)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that truncates a timestamp to a specified granularity.

**Signature:**

    export declare function timestampTruncate(fieldName: string, granularity: TimeGranularity, timezone?: string | Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | Truncate the timestamp value contained in this field. |
| granularity | [TimeGranularity](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#timegranularity) | The granularity to truncate to. |
| timezone | string \| [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The timezone to use for truncation. Valid values are from the TZ database (e.g., "America/Los_Angeles") or in the format "Etc/GMT-1". |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the truncated timestamp.

### Example

    // Truncate the 'createdAt' timestamp to the beginning of the day.
    field('createdAt').timestampTruncate('day')

### timestampTruncate(fieldName, granularity, timezone)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that truncates a timestamp to a specified granularity.

**Signature:**

    export declare function timestampTruncate(fieldName: string, granularity: Expression, timezone?: string | Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | Truncate the timestamp value contained in this field. |
| granularity | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The granularity to truncate to. |
| timezone | string \| [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The timezone to use for truncation. Valid values are from the TZ database (e.g., "America/Los_Angeles") or in the format "Etc/GMT-1". |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the truncated timestamp.

### Example

    // Truncate the 'createdAt' timestamp to the granularity specified in the field 'granularity'.
    field('createdAt').timestampTruncate(field('granularity'))

### toLower(fieldName)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that converts a string field to lowercase.

**Signature:**

    export declare function toLower(fieldName: string): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field containing the string. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the lowercase string.

### Example

    // Convert the 'name' field to lowercase
    toLower("name");

### toUpper(fieldName)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that converts a string field to uppercase.

**Signature:**

    export declare function toUpper(fieldName: string): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field containing the string. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the uppercase string.

### Example

    // Convert the 'title' field to uppercase
    toUpper("title");

### trim(fieldName, valueToTrim)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that removes leading and trailing whitespace from a string or byte array.

**Signature:**

    export declare function trim(fieldName: string, valueToTrim?: string | Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field containing the string or byte array. |
| valueToTrim | string \| [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | Optional This parameter is treated as a set of characters or bytes that will be trimmed from the input. If not specified, then whitespace will be trimmed. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the trimmed string.

### Example

    // Trim whitespace from the 'userInput' field
    trim("userInput");

    // Trim quotes from the 'userInput' field
    trim("userInput", '"');

### trunc(fieldName)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that truncates the numeric value of a field to an integer.

**Signature:**

    export declare function trunc(fieldName: string): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field containing the number to truncate. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the truncated value.

### Example

    // Truncate the value of the 'rating' field
    trunc("rating");

### trunc(fieldName, decimalPlaces)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that truncates a numeric expression to the specified number of decimal places.

**Signature:**

    export declare function trunc(fieldName: string, decimalPlaces: number | Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field to truncate. |
| decimalPlaces | number \| [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | A constant or expression specifying the truncation precision in decimal places. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the truncated value.

### Example

    // Truncate the value of the 'rating' field to two decimal places.
    trunc("rating", 2);

### type(fieldName)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns the data type of the data in the specified field.

String inputs passed iteratively to this global function act as `field()` path lookups. If you wish to pass a string literal value, it must be wrapped: `type(constant("my_string"))`.

**Signature:**

    export declare function type(fieldName: string): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string |   |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the data type.

### Example

    // Get the data type of the value in field 'title'
    type('title')

### unixMicrosToTimestamp(fieldName)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that interprets a field's value as the number of microseconds since the Unix epoch (1970-01-01 00:00:00 UTC) and returns a timestamp.

**Signature:**

    export declare function unixMicrosToTimestamp(fieldName: string): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field representing the number of microseconds since epoch. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the timestamp.

### Example

    // Interpret the 'microseconds' field as microseconds since epoch.
    unixMicrosToTimestamp("microseconds");

### unixMillisToTimestamp(fieldName)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that interprets a field's value as the number of milliseconds since the Unix epoch (1970-01-01 00:00:00 UTC) and returns a timestamp.

**Signature:**

    export declare function unixMillisToTimestamp(fieldName: string): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field representing the number of milliseconds since epoch. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the timestamp.

### Example

    // Interpret the 'milliseconds' field as milliseconds since epoch.
    unixMillisToTimestamp("milliseconds");

### unixSecondsToTimestamp(fieldName)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that interprets a field's value as the number of seconds since the Unix epoch (1970-01-01 00:00:00 UTC) and returns a timestamp.

**Signature:**

    export declare function unixSecondsToTimestamp(fieldName: string): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field representing the number of seconds since epoch. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the timestamp.

### Example

    // Interpret the 'seconds' field as seconds since epoch.
    unixSecondsToTimestamp("seconds");

### vectorLength(fieldName)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that calculates the length of a Firestore Vector represented by a field.

**Signature:**

    export declare function vectorLength(fieldName: string): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| fieldName | string | The name of the field representing the Firestore Vector. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the length of the array.

### Example

    // Get the vector length (dimension) of the field 'embedding'.
    vectorLength("embedding");

## function(first, ...)

### add(first, second)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that adds two expressions together.

**Signature:**

    export declare function add(first: Expression, second: Expression | unknown): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| first | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The first expression to add. |
| second | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| unknown | The second expression or literal to add. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the addition operation.

### Example

    // Add the value of the 'quantity' field and the 'reserve' field.
    add(field("quantity"), field("reserve"));

### and(first, second, more)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that performs a logical 'AND' operation on multiple filter conditions.

**Signature:**

    export declare function and(first: BooleanExpression, second: BooleanExpression, ...more: BooleanExpression[]): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| first | [BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class) | The first filter condition. |
| second | [BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class) | The second filter condition. |
| more | [BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)\[\] | Additional filter conditions to 'AND' together. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the logical 'AND' operation.

### Example

    // Check if the 'age' field is greater than 18 AND the 'city' field is "London" AND
    // the 'status' field is "active"
    const condition = and(greaterThan("age", 18), equal("city", "London"), equal("status", "active"));

### concat(first, second, others)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that concatenates strings, arrays, or blobs. Types cannot be mixed.

**Signature:**

    export declare function concat(first: Expression, second: Expression | unknown, ...others: Array<Expression | unknown>): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| first | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The first expressions to concatenate. |
| second | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| unknown | The second literal or expression to concatenate. |
| others | Array\<[Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| unknown\> | Additional literals or expressions to concatenate. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the concatenation.

### Example

    // Concatenate the 'firstName' and 'lastName' fields with a space in between.
    concat(field("firstName"), " ", field("lastName"))

### logicalMaximum(first, second, others)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns the largest value between multiple input expressions or literal values. Based on Firestore's value type ordering.

**Signature:**

    export declare function logicalMaximum(first: Expression, second: Expression | unknown, ...others: Array<Expression | unknown>): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| first | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The first operand expression. |
| second | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| unknown | The second expression or literal. |
| others | Array\<[Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| unknown\> | Optional additional expressions or literals. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the logical maximum operation.

### Example

    // Returns the largest value between the 'field1' field, the 'field2' field,
    // and 1000
    logicalMaximum(field("field1"), field("field2"), 1000);

### logicalMinimum(first, second, others)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns the smallest value between multiple input expressions and literal values. Based on Firestore's value type ordering.

**Signature:**

    export declare function logicalMinimum(first: Expression, second: Expression | unknown, ...others: Array<Expression | unknown>): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| first | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The first operand expression. |
| second | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| unknown | The second expression or literal. |
| others | Array\<[Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| unknown\> | Optional additional expressions or literals. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the logical minimum operation.

### Example

    // Returns the smallest value between the 'field1' field, the 'field2' field,
    // and 1000.
    logicalMinimum(field("field1"), field("field2"), 1000);

### multiply(first, second)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that multiplies two expressions together.

**Signature:**

    export declare function multiply(first: Expression, second: Expression | unknown): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| first | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The first expression to multiply. |
| second | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| unknown | The second expression or literal to multiply. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the multiplication operation.

### Example

    // Multiply the 'quantity' field by the 'price' field
    multiply(field("quantity"), field("price"));

### or(first, second, more)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that performs a logical 'OR' operation on multiple filter conditions.

**Signature:**

    export declare function or(first: BooleanExpression, second: BooleanExpression, ...more: BooleanExpression[]): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| first | [BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class) | The first filter condition. |
| second | [BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class) | The second filter condition. |
| more | [BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)\[\] | Additional filter conditions to 'OR' together. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the logical 'OR' operation.

### Example

    // Check if the 'age' field is greater than 18 OR the 'city' field is "London" OR
    // the 'status' field is "active"
    const condition = or(greaterThan("age", 18), equal("city", "London"), equal("status", "active"));

### xor(first, second, additionalConditions)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that performs a logical 'XOR' (exclusive OR) operation on multiple BooleanExpressions.

**Signature:**

    export declare function xor(first: BooleanExpression, second: BooleanExpression, ...additionalConditions: BooleanExpression[]): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| first | [BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class) | The first condition. |
| second | [BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class) | The second condition. |
| additionalConditions | [BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)\[\] | Additional conditions to 'XOR' together. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the logical 'XOR' operation.

### Example

    // Check if only one of the conditions is true: 'age' greater than 18, 'city' is "London",
    // or 'status' is "active".
    const condition = xor(
        greaterThan("age", 18),
        equal("city", "London"),
        equal("status", "active"));

## function(firstArray, ...)

### arrayConcat(firstArray, secondArray, otherArrays)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that concatenates an array expression with other arrays.

**Signature:**

    export declare function arrayConcat(firstArray: Expression, secondArray: Expression | unknown[], ...otherArrays: Array<Expression | unknown[]>): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| firstArray | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The first array expression to concatenate to. |
| secondArray | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| unknown\[\] | The second array expression or array literal to concatenate to. |
| otherArrays | Array\<[Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| unknown\[\]\> | Optional additional array expressions or array literals to concatenate. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the concatenated array.

### Example

    // Combine the 'items' array with two new item arrays
    arrayConcat(field("items"), [field("newItems"), field("otherItems")]);

## function(firstArrayField, ...)

### arrayConcat(firstArrayField, secondArray, otherArrays)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that concatenates a field's array value with other arrays.

**Signature:**

    export declare function arrayConcat(firstArrayField: string, secondArray: Expression | unknown[], ...otherArrays: Array<Expression | unknown[]>): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| firstArrayField | string | The first array to concatenate to. |
| secondArray | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| unknown\[\] | The second array expression or array literal to concatenate to. |
| otherArrays | Array\<[Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| unknown\[\]\> | Optional additional array expressions or array literals to concatenate. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the concatenated array.

### Example

    // Combine the 'items' array with two new item arrays
    arrayConcat("items", [field("newItems"), field("otherItems")]);

## function(firstMap, ...)

### mapMerge(firstMap, secondMap, otherMaps)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that merges multiple map values.

**Signature:**

    export declare function mapMerge(firstMap: Record<string, unknown> | Expression, secondMap: Record<string, unknown> | Expression, ...otherMaps: Array<Record<string, unknown> | Expression>): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| firstMap | Record\<string, unknown\> \| [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | An expression or literal map value that will be merged. |
| secondMap | Record\<string, unknown\> \| [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | A required second map to merge. Represented as a literal or an expression that returns a map. |
| otherMaps | Array\<Record\<string, unknown\> \| [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class)\> | Optional additional maps to merge. Each map is represented as a literal or an expression that returns a map. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

### Example

    // Merges the map in the settings field with, a map literal, and a map in
    // that is conditionally returned by another expression
    mapMerge(field('settings'), { enabled: true }, conditional(field('isAdmin'), { admin: true}, {})

## function(firstString, ...)

### stringConcat(firstString, secondString, otherStrings)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that concatenates string expressions together.

**Signature:**

    export declare function stringConcat(firstString: Expression, secondString: Expression | string, ...otherStrings: Array<Expression | string>): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| firstString | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The initial string expression to concatenate to. |
| secondString | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| string | An expression or string literal to concatenate. |
| otherStrings | Array\<[Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| string\> | Optional additional expressions or literals (typically strings) to concatenate. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the concatenated string.

### Example

    // Combine the 'firstName', " ", and 'lastName' fields into a single string
    stringConcat(field("firstName"), " ", field("lastName"));

## function(ifExpr, ...)

### ifAbsent(ifExpr, elseExpr)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns the `elseExpr` argument if `ifExpr` is absent, else return the result of the `ifExpr` argument evaluation.

**Signature:**

    export declare function ifAbsent(ifExpr: Expression, elseExpr: Expression): Expression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| ifExpr | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression to check for absence. |
| elseExpr | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression that will be evaluated and returned if \[ifExpr\] is absent. |

**Returns:**

[Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class)

A new Expression representing the ifAbsent operation.

### Example

    // Returns the value of the optional field 'optional_field', or returns 'default_value'
    // if the field is absent.
    ifAbsent(field("optional_field"), constant("default_value"))

### ifAbsent(ifExpr, elseValue)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns the `elseValue` argument if `ifExpr` is absent, else return the result of the `ifExpr` argument evaluation.

**Signature:**

    export declare function ifAbsent(ifExpr: Expression, elseValue: unknown): Expression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| ifExpr | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression to check for absence. |
| elseValue | unknown | The value that will be returned if `ifExpr` evaluates to an absent value. |

**Returns:**

[Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class)

A new \[Expression\] representing the ifAbsent operation.

### Example

    // Returns the value of the optional field 'optional_field', or returns 'default_value'
    // if the field is absent.
    ifAbsent(field("optional_field"), "default_value")

## function(ifFieldName, ...)

### ifAbsent(ifFieldName, elseExpr)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns the `elseExpr` argument if `ifFieldName` is absent, else return the value of the field.

**Signature:**

    export declare function ifAbsent(ifFieldName: string, elseExpr: Expression): Expression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| ifFieldName | string | The field to check for absence. |
| elseExpr | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression that will be evaluated and returned if `ifFieldName` is absent. |

**Returns:**

[Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class)

A new Expression representing the ifAbsent operation.

### Example

    // Returns the value of the optional field 'optional_field', or returns the value of
    // 'default_field' if 'optional_field' is absent.
    ifAbsent("optional_field", field("default_field"))

### ifAbsent(ifFieldName, elseValue)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns the `elseValue` argument if `ifFieldName` is absent, else return the value of the field.

**Signature:**

    export declare function ifAbsent(ifFieldName: string | Expression, elseValue: Expression | unknown): Expression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| ifFieldName | string \| [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The field to check for absence. |
| elseValue | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| unknown | The value that will be returned if \[ifFieldName\] is absent. |

**Returns:**

[Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class)

A new Expression representing the ifAbsent operation.

### Example

    // Returns the value of the optional field 'optional_field', or returns 'default_value'
    // if the field is absent.
    ifAbsent("optional_field", "default_value")

## function(input, ...)

### substring(input, position, length)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns a substring of a string or byte array.

**Signature:**

    export declare function substring(input: Expression, position: number, length?: number): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| input | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | An expression returning a string or byte array to compute the substring from. |
| position | number | Index of the first character of the substring. |
| length | number | Length of the substring. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

### substring(input, position, length)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns a substring of a string or byte array.

**Signature:**

    export declare function substring(input: Expression, position: Expression, length?: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| input | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | An expression returning a string or byte array to compute the substring from. |
| position | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | An expression that returns the index of the first character of the substring. |
| length | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | An expression that returns the length of the substring. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

## function(left, ...)

### divide(left, right)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that divides two expressions.

**Signature:**

    export declare function divide(left: Expression, right: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| left | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression to be divided. |
| right | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression to divide by. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the division operation.

### Example

    // Divide the 'total' field by the 'count' field
    divide(field("total"), field("count"));

### equal(left, right)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if two expressions are equal.

**Signature:**

    export declare function equal(left: Expression, right: Expression): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| left | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The first expression to compare. |
| right | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The second expression to compare. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `Expression` representing the equality comparison.

### Example

    // Check if the 'age' field is equal to an expression
    equal(field("age"), field("minAge").add(10));

### greaterThan(left, right)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if the first expression is greater than the second expression.

**Signature:**

    export declare function greaterThan(left: Expression, right: Expression): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| left | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The first expression to compare. |
| right | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The second expression to compare. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `Expression` representing the greater than comparison.

### Example

    // Check if the 'age' field is greater than 18
    greaterThan(field("age"), Constant(9).add(9));

### greaterThanOrEqual(left, right)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if the first expression is greater than or equal to the second expression.

**Signature:**

    export declare function greaterThanOrEqual(left: Expression, right: Expression): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| left | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The first expression to compare. |
| right | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The second expression to compare. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `Expression` representing the greater than or equal to comparison.

### Example

    // Check if the 'quantity' field is greater than or equal to the field "threshold"
    greaterThanOrEqual(field("quantity"), field("threshold"));

### lessThan(left, right)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if the first expression is less than the second expression.

**Signature:**

    export declare function lessThan(left: Expression, right: Expression): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| left | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The first expression to compare. |
| right | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The second expression to compare. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `Expression` representing the less than comparison.

### Example

    // Check if the 'age' field is less than 30
    lessThan(field("age"), field("limit"));

### lessThanOrEqual(left, right)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if the first expression is less than or equal to the second expression.

**Signature:**

    export declare function lessThanOrEqual(left: Expression, right: Expression): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| left | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The first expression to compare. |
| right | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The second expression to compare. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `Expression` representing the less than or equal to comparison.

### Example

    // Check if the 'quantity' field is less than or equal to 20
    lessThan(field("quantity"), field("limit"));

### mod(left, right)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that calculates the modulo (remainder) of dividing two expressions.

**Signature:**

    export declare function mod(left: Expression, right: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| left | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The dividend expression. |
| right | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The divisor expression. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the modulo operation.

### Example

    // Calculate the remainder of dividing 'field1' by 'field2'.
    mod(field("field1"), field("field2"));

### notEqual(left, right)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if two expressions are not equal.

**Signature:**

    export declare function notEqual(left: Expression, right: Expression): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| left | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The first expression to compare. |
| right | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The second expression to compare. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `Expression` representing the inequality comparison.

### Example

    // Check if the 'status' field is not equal to field 'finalState'
    notEqual(field("status"), field("finalState"));

### pipelineResultEqual(left, right)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Test equality of two PipelineResults.

**Signature:**

    export declare function pipelineResultEqual(left: PipelineResult, right: PipelineResult): boolean;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| left | [PipelineResult](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelineresult.md#pipelineresult_class) | First PipelineResult to compare. |
| right | [PipelineResult](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelineresult.md#pipelineresult_class) | Second PipelineResult to compare. |

**Returns:**

boolean

### subtract(left, right)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that subtracts two expressions.

**Signature:**

    export declare function subtract(left: Expression, right: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| left | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression to subtract from. |
| right | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression to subtract. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the subtraction operation.

### Example

    // Subtract the 'discount' field from the 'price' field
    subtract(field("price"), field("discount"));

## function(mapExpr, ...)

### mapRemove(mapExpr, key)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that removes a key from the map produced by evaluating an expression.

**Signature:**

    export declare function mapRemove(mapExpr: Expression, key: string): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| mapExpr | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | An expression return a map value. |
| key | string | The name of the key to remove from the input map. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

### Example

    // Removes the key 'baz' from the input map.
    mapRemove(map({foo: 'bar', baz: true}), 'baz');
    @example

### mapRemove(mapExpr, keyExpr)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that removes a key from the map produced by evaluating an expression.

**Signature:**

    export declare function mapRemove(mapExpr: Expression, keyExpr: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| mapExpr | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | An expression return a map value. |
| keyExpr | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | An expression that produces the name of the key to remove from the input map. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

### Example

    // Removes the key 'baz' from the input map.
    mapRemove(map({foo: 'bar', baz: true}), constant('baz'));
    @example

## function(mapExpression, ...)

### mapEntries(mapExpression)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns the entries of a map as an array of maps, where each map contains a `"k"` property for the key and a `"v"` property for the value. For example: `[{ k: "key1", v: "value1" }, ...]`.

While the backend generally preserves insertion order, relying on the order of the output array is not guaranteed and should be avoided.

**Signature:**

    export declare function mapEntries(mapExpression: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| mapExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression representing the map to get the entries of. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the entries of the map.

### Example

    // Get the entries of the map expression
    mapEntries(map({"city": "San Francisco"}));

### mapGet(mapExpression, subField)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Accesses a value from a map (object) expression using the provided key.

**Signature:**

    export declare function mapGet(mapExpression: Expression, subField: string): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| mapExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression representing the map. |
| subField | string | The key to access in the map. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the value associated with the given key in the map.

### Example

    // Get the 'city' value from the 'address' map field
    mapGet(field("address"), "city");

### mapKeys(mapExpression)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns the keys of a map.

While the backend generally preserves insertion order, relying on the order of the output array is not guaranteed and should be avoided.

**Signature:**

    export declare function mapKeys(mapExpression: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| mapExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression representing the map to get the keys of. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the keys of the map.

### Example

    // Get the keys of the map expression
    mapKeys(map({"city": "San Francisco"}));

### mapSet(mapExpression, key, value, moreKeyValues)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns a new map with the specified entries added or updated.

This only performs shallow updates to the map. Setting a value to `null` will retain the key with a `null` value. To remove a key entirely, use `mapRemove`.

**Signature:**

    export declare function mapSet(mapExpression: Expression, key: string | Expression, value: unknown, ...moreKeyValues: unknown[]): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| mapExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression representing the map. |
| key | string \| [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The key to set. Must be a string or a constant string expression. |
| value | unknown | The value to set. |
| moreKeyValues | unknown\[\] | Additional key-value pairs to set. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the map with the entries set.

### Example

    // Set the 'city' to "San Francisco"
    mapSet(map({"state": "California"}), "city", "San Francisco");

### mapValues(mapExpression)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns the values of a map.

While the backend generally preserves insertion order, relying on the order of the output array is not guaranteed and should be avoided.

**Signature:**

    export declare function mapValues(mapExpression: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| mapExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression representing the map to get the values of. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the values of the map.

### Example

    // Get the values of the map expression
    mapValues(map({"city": "San Francisco"}));

## function(mapField, ...)

### mapEntries(mapField)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns the entries of a map as an array of maps, where each map contains a `"k"` property for the key and a `"v"` property for the value. For example: `[{ k: "key1", v: "value1" }, ...]`.

While the backend generally preserves insertion order, relying on the order of the output array is not guaranteed and should be avoided.

**Signature:**

    export declare function mapEntries(mapField: string): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| mapField | string | The map field to get the entries of. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the entries of the map.

### Example

    // Get the entries of the 'address' map field
    mapEntries("address");

### mapKeys(mapField)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns the keys of a map.

While the backend generally preserves insertion order, relying on the order of the output array is not guaranteed and should be avoided.

**Signature:**

    export declare function mapKeys(mapField: string): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| mapField | string | The map field to get the keys of. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the keys of the map.

### Example

    // Get the keys of the 'address' map field
    mapKeys("address");

### mapMerge(mapField, secondMap, otherMaps)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that merges multiple map values.

**Signature:**

    export declare function mapMerge(mapField: string, secondMap: Record<string, unknown> | Expression, ...otherMaps: Array<Record<string, unknown> | Expression>): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| mapField | string | Name of a field containing a map value that will be merged. |
| secondMap | Record\<string, unknown\> \| [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | A required second map to merge. Represented as a literal or an expression that returns a map. |
| otherMaps | Array\<Record\<string, unknown\> \| [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class)\> | Optional additional maps to merge. Each map is represented as a literal or an expression that returns a map. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

### Example

    // Merges the map in the settings field with, a map literal, and a map in
    // that is conditionally returned by another expression
    mapMerge('settings', { enabled: true }, conditional(field('isAdmin'), { admin: true}, {})

### mapRemove(mapField, key)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that removes a key from the map at the specified field name.

**Signature:**

    export declare function mapRemove(mapField: string, key: string): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| mapField | string | The name of a field containing a map value. |
| key | string | The name of the key to remove from the input map. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

### Example

    // Removes the key 'city' field from the map in the address field of the input document.
    mapRemove('address', 'city');

### mapRemove(mapField, keyExpr)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that removes a key from the map at the specified field name.

**Signature:**

    export declare function mapRemove(mapField: string, keyExpr: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| mapField | string | The name of a field containing a map value. |
| keyExpr | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | An expression that produces the name of the key to remove from the input map. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

### Example

    // Removes the key 'city' field from the map in the address field of the input document.
    mapRemove('address', constant('city'));

### mapSet(mapField, key, value, moreKeyValues)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns a new map with the specified entries added or updated.

This only performs shallow updates to the map. Setting a value to `null` will retain the key with a `null` value. To remove a key entirely, use `mapRemove`.

**Signature:**

    export declare function mapSet(mapField: string, key: string | Expression, value: unknown, ...moreKeyValues: unknown[]): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| mapField | string | The map field to set entries in. |
| key | string \| [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The key to set. Must be a string or a constant string expression. |
| value | unknown | The value to set. |
| moreKeyValues | unknown\[\] | Additional key-value pairs to set. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the map with the entries set.

### Example

    // Set the 'city' to 'San Francisco' in the 'address' map field
    mapSet("address", "city", "San Francisco");

### mapValues(mapField)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns the values of a map.

While the backend generally preserves insertion order, relying on the order of the output array is not guaranteed and should be avoided.

**Signature:**

    export declare function mapValues(mapField: string): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| mapField | string | The map field to get the values of. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the values of the map.

### Example

    // Get the values of the 'address' map field
    mapValues("address");

## function(name, ...)

### field(name)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates a [Field](https://firebase.google.com/docs/reference/js/firestore_pipelines.field.md#field_class) instance representing the field at the given path.

The path can be a simple field name (e.g., "name") or a dot-separated path to a nested field (e.g., "address.city").

**Signature:**

    export declare function field(name: string): Field;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| name | string | The path to the field. |

**Returns:**

[Field](https://firebase.google.com/docs/reference/js/firestore_pipelines.field.md#field_class)

A new [Field](https://firebase.google.com/docs/reference/js/firestore_pipelines.field.md#field_class) instance representing the specified field.

### Example

    // Create a Field instance for the 'title' field
    const titleField = field("title");

    // Create a Field instance for a nested field 'author.firstName'
    const authorFirstNameField = field("author.firstName");

## function(options, ...)

### execute(options)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Executes a pipeline and returns a Promise to represent the asynchronous operation.

The returned Promise can be used to track the progress of the pipeline execution and retrieve the results (or handle any errors) asynchronously.

The pipeline results are returned as a [PipelineSnapshot](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelinesnapshot.md#pipelinesnapshot_class) that contains a list of [PipelineResult](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelineresult.md#pipelineresult_class) objects. Each [PipelineResult](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelineresult.md#pipelineresult_class) typically represents a single key/value map that has passed through all the stages of the pipeline, however this might differ depending on the stages involved in the pipeline. For example:

- If there are no stages or only transformation stages, each \[PipelineResult\](./firestore_pipelines.pipelineresult.md#pipelineresult_class) represents a single document.
- If there is an aggregation, only a single \[PipelineResult\](./firestore_pipelines.pipelineresult.md#pipelineresult_class) is returned, representing the aggregated results over the entire dataset .
- If there is an aggregation stage with grouping, each \[PipelineResult\](./firestore_pipelines.pipelineresult.md#pipelineresult_class) represents a distinct group and its associated aggregated values.

**Signature:**

    export declare function execute(options: PipelineExecuteOptions): Promise<PipelineSnapshot>;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| options | [PipelineExecuteOptions](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelineexecuteoptions.md#pipelineexecuteoptions_interface) | Specifies the pipeline to execute and other options for execute. |

**Returns:**

Promise\<[PipelineSnapshot](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelinesnapshot.md#pipelinesnapshot_class)\>

A Promise representing the asynchronous pipeline execution.

### Example

    const snapshot: PipelineSnapshot = await execute(firestore.pipeline().collection("books")
        .where(gt(field("rating"), 4.5))
        .select("title", "author", "rating"));

    const results: PipelineResults = snapshot.results;

## function(path, ...)

### field(path)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates a [Field](https://firebase.google.com/docs/reference/js/firestore_pipelines.field.md#field_class) instance representing the field at the given path.

**Signature:**

    export declare function field(path: FieldPath): Field;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| path | [FieldPath](https://firebase.google.com/docs/reference/js/firestore_.fieldpath.md#fieldpath_class) | A FieldPath specifying the field. |

**Returns:**

[Field](https://firebase.google.com/docs/reference/js/firestore_pipelines.field.md#field_class)

A new [Field](https://firebase.google.com/docs/reference/js/firestore_pipelines.field.md#field_class) instance representing the specified field.

## function(pipeline, ...)

### execute(pipeline)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Executes a pipeline and returns a Promise to represent the asynchronous operation.

The returned Promise can be used to track the progress of the pipeline execution and retrieve the results (or handle any errors) asynchronously.

The pipeline results are returned as a [PipelineSnapshot](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelinesnapshot.md#pipelinesnapshot_class) that contains a list of [PipelineResult](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelineresult.md#pipelineresult_class) objects. Each [PipelineResult](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelineresult.md#pipelineresult_class) typically represents a single key/value map that has passed through all the stages of the pipeline, however this might differ depending on the stages involved in the pipeline. For example:

- If there are no stages or only transformation stages, each \[PipelineResult\](./firestore_pipelines.pipelineresult.md#pipelineresult_class) represents a single document.
- If there is an aggregation, only a single \[PipelineResult\](./firestore_pipelines.pipelineresult.md#pipelineresult_class) is returned, representing the aggregated results over the entire dataset .
- If there is an aggregation stage with grouping, each \[PipelineResult\](./firestore_pipelines.pipelineresult.md#pipelineresult_class) represents a distinct group and its associated aggregated values.

**Signature:**

    export declare function execute(pipeline: Pipeline): Promise<PipelineSnapshot>;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| pipeline | [Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class) | The pipeline to execute. |

**Returns:**

Promise\<[PipelineSnapshot](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelinesnapshot.md#pipelinesnapshot_class)\>

A Promise representing the asynchronous pipeline execution.

### Example

    const snapshot: PipelineSnapshot = await execute(firestore.pipeline().collection("books")
        .where(gt(field("rating"), 4.5))
        .select("title", "author", "rating"));

    const results: PipelineResults = snapshot.results;

## function(stringExpression, ...)

### charLength(stringExpression)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that calculates the character length of a string expression in UTF-8.

**Signature:**

    export declare function charLength(stringExpression: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| stringExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression representing the string to calculate the length of. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the length of the string.

### Example

    // Get the character length of the 'name' field in UTF-8.
    strLength(field("name"));

### endsWith(stringExpression, suffix)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if a string expression ends with a given postfix.

**Signature:**

    export declare function endsWith(stringExpression: Expression, suffix: string): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| stringExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression to check. |
| suffix | string | The postfix to check for. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the 'ends with' comparison.

### Example

    // Check if the result of concatenating 'firstName' and 'lastName' fields ends with "Jr."
    endsWith(field("fullName"), "Jr.");

### endsWith(stringExpression, suffix)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if a string expression ends with a given postfix.

**Signature:**

    export declare function endsWith(stringExpression: Expression, suffix: Expression): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| stringExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression to check. |
| suffix | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The postfix to check for. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the 'ends with' comparison.

### Example

    // Check if the result of concatenating 'firstName' and 'lastName' fields ends with "Jr."
    endsWith(field("fullName"), constant("Jr."));

### like(stringExpression, pattern)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that performs a case-sensitive wildcard string comparison.

**Signature:**

    export declare function like(stringExpression: Expression, pattern: string): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| stringExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression representing the string to perform the comparison on. |
| pattern | string | The pattern to search for. You can use "%" as a wildcard character. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the 'like' comparison.

### Example

    // Check if the 'title' field contains the string "guide"
    like(field("title"), "%guide%");

### like(stringExpression, pattern)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that performs a case-sensitive wildcard string comparison.

**Signature:**

    export declare function like(stringExpression: Expression, pattern: Expression): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| stringExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression representing the string to perform the comparison on. |
| pattern | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The pattern to search for. You can use "%" as a wildcard character. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the 'like' comparison.

### Example

    // Check if the 'title' field contains the string "guide"
    like(field("title"), field("pattern"));

### regexContains(stringExpression, pattern)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if a string expression contains a specified regular expression as a substring.

**Signature:**

    export declare function regexContains(stringExpression: Expression, pattern: string): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| stringExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression representing the string to perform the comparison on. |
| pattern | string | The regular expression to use for the search. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the 'contains' comparison.

### Example

    // Check if the 'description' field contains "example" (case-insensitive)
    regexContains(field("description"), "(?i)example");

### regexContains(stringExpression, pattern)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if a string expression contains a specified regular expression as a substring.

**Signature:**

    export declare function regexContains(stringExpression: Expression, pattern: Expression): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| stringExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression representing the string to perform the comparison on. |
| pattern | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The regular expression to use for the search. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the 'contains' comparison.

### Example

    // Check if the 'description' field contains "example" (case-insensitive)
    regexContains(field("description"), field("pattern"));

### regexFind(stringExpression, pattern)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns the first substring of a string expression that matches a specified regular expression.

This expression uses the [RE2](https://github.com/google/re2/wiki/Syntax) regular expression syntax.

**Signature:**

    export declare function regexFind(stringExpression: Expression, pattern: string): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| stringExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression representing the string to search. |
| pattern | string | The regular expression to search for. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the regular expression find function.

### Example

    // Extract the domain from a lower-cased email address
    regexFind(field("email"), "@[A-Za-z0-9.-]+");

### regexFind(stringExpression, pattern)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns the first substring of a string expression that matches a specified regular expression.

This expression uses the [RE2](https://github.com/google/re2/wiki/Syntax) regular expression syntax.

**Signature:**

    export declare function regexFind(stringExpression: Expression, pattern: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| stringExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression representing the string to search. |
| pattern | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The regular expression to search for. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the regular expression find function.

### Example

    // Extract a substring based on a dynamic pattern field
    regexFind(field("email"), field("pattern"));

### regexFindAll(stringExpression, pattern)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that evaluates to a list of all substrings in a string expression that match a specified regular expression.

This expression uses the [RE2](https://github.com/google/re2/wiki/Syntax) regular expression syntax.

**Signature:**

    export declare function regexFindAll(stringExpression: Expression, pattern: string): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| stringExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression representing the string to search. |
| pattern | string | The regular expression to search for. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class) that evaluates to an array of matched substrings.

### Example

    // Extract all mentions from a lower-cased comment
    regexFindAll(field("comment"), "@[A-Za-z0-9_]+");

### regexFindAll(stringExpression, pattern)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that evaluates to a list of all substrings in a string expression that match a specified regular expression.

This expression uses the [RE2](https://github.com/google/re2/wiki/Syntax) regular expression syntax.

**Signature:**

    export declare function regexFindAll(stringExpression: Expression, pattern: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| stringExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression representing the string to search. |
| pattern | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The regular expression to search for. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class) that evaluates to an array of matched substrings.

### Example

    // Extract all matches based on a dynamic pattern expression
    regexFindAll(field("comment"), field("pattern"));

### regexMatch(stringExpression, pattern)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if a string expression matches a specified regular expression.

**Signature:**

    export declare function regexMatch(stringExpression: Expression, pattern: string): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| stringExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression representing the string to match against. |
| pattern | string | The regular expression to use for the match. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the regular expression match.

### Example

    // Check if the 'email' field matches a valid email pattern
    regexMatch(field("email"), "[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}");

### regexMatch(stringExpression, pattern)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if a string expression matches a specified regular expression.

**Signature:**

    export declare function regexMatch(stringExpression: Expression, pattern: Expression): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| stringExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression representing the string to match against. |
| pattern | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The regular expression to use for the match. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the regular expression match.

### Example

    // Check if the 'email' field matches a valid email pattern
    regexMatch(field("email"), field("pattern"));

### reverse(stringExpression)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that reverses a string.

**Signature:**

    export declare function reverse(stringExpression: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| stringExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | An expression evaluating to a string value, which will be reversed. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the reversed string.

### Example

    // Reverse the value of the 'myString' field.
    reverse(field("myString"));

### startsWith(stringExpression, prefix)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if a string expression starts with a given prefix.

**Signature:**

    export declare function startsWith(stringExpression: Expression, prefix: string): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| stringExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression to check. |
| prefix | string | The prefix to check for. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the 'starts with' comparison.

### Example

    // Check if the result of concatenating 'firstName' and 'lastName' fields starts with "Mr."
    startsWith(field("fullName"), "Mr.");

### startsWith(stringExpression, prefix)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if a string expression starts with a given prefix.

**Signature:**

    export declare function startsWith(stringExpression: Expression, prefix: Expression): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| stringExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression to check. |
| prefix | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The prefix to check for. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the 'starts with' comparison.

### Example

    // Check if the result of concatenating 'firstName' and 'lastName' fields starts with "Mr."
    startsWith(field("fullName"), field("prefix"));

### stringContains(stringExpression, substring)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if a string expression contains a specified substring.

**Signature:**

    export declare function stringContains(stringExpression: Expression, substring: string): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| stringExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression representing the string to perform the comparison on. |
| substring | string | The substring to search for. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the 'contains' comparison.

### Example

    // Check if the 'description' field contains "example".
    stringContains(field("description"), "example");

### stringContains(stringExpression, substring)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if a string expression contains a substring specified by another expression.

**Signature:**

    export declare function stringContains(stringExpression: Expression, substring: Expression): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| stringExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression representing the string to perform the comparison on. |
| substring | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression representing the substring to search for. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the 'contains' comparison.

### Example

    // Check if the 'description' field contains the value of the 'keyword' field.
    stringContains(field("description"), field("keyword"));

### stringReverse(stringExpression)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that reverses a string.

**Signature:**

    export declare function stringReverse(stringExpression: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| stringExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | An expression evaluating to a string value, which will be reversed. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the reversed string.

### Example

    // Reverse the value of the 'myString' field.
    strReverse(field("myString"));

### toLower(stringExpression)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that converts a string expression to lowercase.

**Signature:**

    export declare function toLower(stringExpression: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| stringExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression representing the string to convert to lowercase. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the lowercase string.

### Example

    // Convert the 'name' field to lowercase
    toLower(field("name"));

### toUpper(stringExpression)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that converts a string expression to uppercase.

**Signature:**

    export declare function toUpper(stringExpression: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| stringExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression representing the string to convert to uppercase. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the uppercase string.

### Example

    // Convert the 'title' field to uppercase
    toUppercase(field("title"));

### trim(stringExpression, valueToTrim)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that removes leading and trailing characters from a string or byte array expression.

**Signature:**

    export declare function trim(stringExpression: Expression, valueToTrim?: string | Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| stringExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression representing the string or byte array to trim. |
| valueToTrim | string \| [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | Optional This parameter is treated as a set of characters or bytes that will be trimmed from the input. If not specified, then whitespace will be trimmed. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the trimmed string or byte array.

### Example

    // Trim whitespace from the 'userInput' field
    trim(field("userInput"));

    // Trim quotes from the 'userInput' field
    trim(field("userInput"), '"');

## function(timestamp, ...)

### timestampAdd(timestamp, unit, amount)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that adds a specified amount of time to a timestamp.

**Signature:**

    export declare function timestampAdd(timestamp: Expression, unit: Expression, amount: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| timestamp | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression representing the timestamp. |
| unit | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression evaluates to unit of time, must be one of 'microsecond', 'millisecond', 'second', 'minute', 'hour', 'day'. |
| amount | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression evaluates to amount of the unit. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the resulting timestamp.

### Example

    // Add some duration determined by field 'unit' and 'amount' to the 'timestamp' field.
    timestampAdd(field("timestamp"), field("unit"), field("amount"));

### timestampAdd(timestamp, unit, amount)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that adds a specified amount of time to a timestamp.

**Signature:**

    export declare function timestampAdd(timestamp: Expression, unit: 'microsecond' | 'millisecond' | 'second' | 'minute' | 'hour' | 'day', amount: number): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| timestamp | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression representing the timestamp. |
| unit | 'microsecond' \| 'millisecond' \| 'second' \| 'minute' \| 'hour' \| 'day' | The unit of time to add (e.g., "day", "hour"). |
| amount | number | The amount of time to add. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the resulting timestamp.

### Example

    // Add 1 day to the 'timestamp' field.
    timestampAdd(field("timestamp"), "day", 1);

### timestampSubtract(timestamp, unit, amount)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that subtracts a specified amount of time from a timestamp.

**Signature:**

    export declare function timestampSubtract(timestamp: Expression, unit: Expression, amount: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| timestamp | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression representing the timestamp. |
| unit | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression evaluates to unit of time, must be one of 'microsecond', 'millisecond', 'second', 'minute', 'hour', 'day'. |
| amount | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression evaluates to amount of the unit. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the resulting timestamp.

### Example

    // Subtract some duration determined by field 'unit' and 'amount' from the 'timestamp' field.
    timestampSubtract(field("timestamp"), field("unit"), field("amount"));

### timestampSubtract(timestamp, unit, amount)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that subtracts a specified amount of time from a timestamp.

**Signature:**

    export declare function timestampSubtract(timestamp: Expression, unit: 'microsecond' | 'millisecond' | 'second' | 'minute' | 'hour' | 'day', amount: number): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| timestamp | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression representing the timestamp. |
| unit | 'microsecond' \| 'millisecond' \| 'second' \| 'minute' \| 'hour' \| 'day' | The unit of time to subtract (e.g., "day", "hour"). |
| amount | number | The amount of time to subtract. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the resulting timestamp.

### Example

    // Subtract 1 day from the 'timestamp' field.
    timestampSubtract(field("timestamp"), "day", 1);

## function(timestampExpression, ...)

### timestampTruncate(timestampExpression, granularity, timezone)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that truncates a timestamp to a specified granularity.

**Signature:**

    export declare function timestampTruncate(timestampExpression: Expression, granularity: TimeGranularity, timezone?: string | Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| timestampExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | Truncate the timestamp value that is returned by this expression. |
| granularity | [TimeGranularity](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#timegranularity) | The granularity to truncate to. |
| timezone | string \| [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The timezone to use for truncation. Valid values are from the TZ database (e.g., "America/Los_Angeles") or in the format "Etc/GMT-1". |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the truncated timestamp.

### Example

    // Truncate the 'createdAt' timestamp to the beginning of the day.
    field('createdAt').timestampTruncate('day')

### timestampTruncate(timestampExpression, granularity, timezone)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that truncates a timestamp to a specified granularity.

**Signature:**

    export declare function timestampTruncate(timestampExpression: Expression, granularity: Expression, timezone?: string | Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| timestampExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | Truncate the timestamp value that is returned by this expression. |
| granularity | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The granularity to truncate to. |
| timezone | string \| [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The timezone to use for truncation. Valid values are from the TZ database (e.g., "America/Los_Angeles") or in the format "Etc/GMT-1". |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the truncated timestamp.

### Example

    // Truncate the 'createdAt' timestamp to the granularity specified in the field 'granularity'.
    field('createdAt').timestampTruncate(field('granularity'))

## function(tryExpr, ...)

### ifError(tryExpr, catchExpr)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns the `catch` argument if there is an error, else return the result of the `try` argument evaluation.

This overload is useful when a BooleanExpression is required.

**Signature:**

    export declare function ifError(tryExpr: BooleanExpression, catchExpr: BooleanExpression): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| tryExpr | [BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class) | The try expression. |
| catchExpr | [BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class) | The catch expression that will be evaluated and returned if the tryExpr produces an error. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the 'ifError' operation.

### Example

    // Create an expression that protects against a divide by zero error
    // but always returns a boolean expression.
    ifError(constant(50).divide('length').gt(1), constant(false));

### ifError(tryExpr, catchExpr)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns the `catch` argument if there is an error, else return the result of the `try` argument evaluation.

**Signature:**

    export declare function ifError(tryExpr: Expression, catchExpr: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| tryExpr | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The try expression. |
| catchExpr | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The catch expression that will be evaluated and returned if the tryExpr produces an error. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the 'ifError' operation.

### Example

    // Returns the first item in the title field arrays, or returns
    // the entire title field if the array is empty or the field is another type.
    ifError(field("title").arrayGet(0), field("title"));

### ifError(tryExpr, catchValue)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns the `catch` argument if there is an error, else return the result of the `try` argument evaluation.

**Signature:**

    export declare function ifError(tryExpr: Expression, catchValue: unknown): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| tryExpr | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The try expression. |
| catchValue | unknown | The value that will be returned if the tryExpr produces an error. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the 'ifError' operation.

### Example

    // Returns the first item in the title field arrays, or returns
    // "Default Title"
    ifError(field("title").arrayGet(0), "Default Title");

## function(value, ...)

### constant(value)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates a `Constant` instance for a number value.

**Signature:**

    export declare function constant(value: number): Expression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| value | number | The number value. |

**Returns:**

[Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class)

A new `Constant` instance.

### constant(value)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates a `Constant` instance for a VectorValue value.

**Signature:**

    export declare function constant(value: VectorValue): Expression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| value | [VectorValue](https://firebase.google.com/docs/reference/js/firestore_.vectorvalue.md#vectorvalue_class) | The VectorValue value. |

**Returns:**

[Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class)

A new `Constant` instance.

### constant(value)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates a `Constant` instance for a string value.

**Signature:**

    export declare function constant(value: string): Expression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| value | string | The string value. |

**Returns:**

[Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class)

A new `Constant` instance.

### constant(value)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates a `BooleanExpression` instance for a boolean value.

**Signature:**

    export declare function constant(value: boolean): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| value | boolean | The boolean value. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `Constant` instance.

### constant(value)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates a `Constant` instance for a null value.

**Signature:**

    export declare function constant(value: null): Expression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| value | null | The null value. |

**Returns:**

[Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class)

A new `Constant` instance.

### constant(value)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates a `Constant` instance for a GeoPoint value.

**Signature:**

    export declare function constant(value: GeoPoint): Expression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| value | [GeoPoint](https://firebase.google.com/docs/reference/js/firestore_.geopoint.md#geopoint_class) | The GeoPoint value. |

**Returns:**

[Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class)

A new `Constant` instance.

### constant(value)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates a `Constant` instance for a Timestamp value.

**Signature:**

    export declare function constant(value: Timestamp): Expression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| value | [Timestamp](https://firebase.google.com/docs/reference/js/firestore_.timestamp.md#timestamp_class) | The Timestamp value. |

**Returns:**

[Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class)

A new `Constant` instance.

### constant(value)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates a `Constant` instance for a Date value.

**Signature:**

    export declare function constant(value: Date): Expression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| value | Date | The Date value. |

**Returns:**

[Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class)

A new `Constant` instance.

### constant(value)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates a `Constant` instance for a Bytes value.

**Signature:**

    export declare function constant(value: Bytes): Expression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| value | [Bytes](https://firebase.google.com/docs/reference/js/firestore_.bytes.md#bytes_class) | The Bytes value. |

**Returns:**

[Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class)

A new `Constant` instance.

### constant(value)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates a `Constant` instance for a DocumentReference value.

**Signature:**

    export declare function constant(value: DocumentReference): Expression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| value | [DocumentReference](https://firebase.google.com/docs/reference/js/firestore_.documentreference.md#documentreference_class) | The DocumentReference value. |

**Returns:**

[Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class)

A new `Constant` instance.

### exists(value)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if a field exists.

**Signature:**

    export declare function exists(value: Expression): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| value | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | An expression evaluates to the name of the field to check. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the 'exists' check.

### Example

    // Check if the document has a field named "phoneNumber"
    exists(field("phoneNumber"));

### isAbsent(value)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns `true` if a value is absent. Otherwise, returns `false` even if the value is `null`.

**Signature:**

    export declare function isAbsent(value: Expression): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| value | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression to check. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the 'isAbsent' check.

### Example

    // Check if the field `value` is absent.
    isAbsent(field("value"));

### isError(value)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if a given expression produces an error.

**Signature:**

    export declare function isError(value: Expression): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| value | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression to check. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the 'isError' check.

### Example

    // Check if the result of a calculation is an error
    isError(field("title").arrayContains(1));

## function(vectorExpression, ...)

### cosineDistance(vectorExpression, vector)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Calculates the Cosine distance between a vector expression and a vector literal.

**Signature:**

    export declare function cosineDistance(vectorExpression: Expression, vector: number[] | VectorValue): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| vectorExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The first vector (represented as an `Expression`) to compare against. |
| vector | number\[\] \| [VectorValue](https://firebase.google.com/docs/reference/js/firestore_.vectorvalue.md#vectorvalue_class) | The other vector (as an array of doubles or VectorValue) to compare against. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the cosine distance between the two vectors.

### Example

    // Calculate the cosine distance between the 'location' field and a target location
    cosineDistance(field("location"), [37.7749, -122.4194]);

### cosineDistance(vectorExpression, otherVectorExpression)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Calculates the Cosine distance between two vector expressions.

**Signature:**

    export declare function cosineDistance(vectorExpression: Expression, otherVectorExpression: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| vectorExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The first vector (represented as an `Expression`) to compare against. |
| otherVectorExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The other vector (represented as an `Expression`) to compare against. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the cosine distance between the two vectors.

### Example

    // Calculate the cosine distance between the 'userVector' field and the 'itemVector' field
    cosineDistance(field("userVector"), field("itemVector"));

### dotProduct(vectorExpression, vector)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Calculates the dot product between a vector expression and a double array.

**Signature:**

    export declare function dotProduct(vectorExpression: Expression, vector: number[] | VectorValue): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| vectorExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The first vector (represented as an `Expression`) to calculate with. |
| vector | number\[\] \| [VectorValue](https://firebase.google.com/docs/reference/js/firestore_.vectorvalue.md#vectorvalue_class) | The other vector (as an array of doubles or VectorValue) to calculate with. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the dot product between the two vectors.

### Example

    // Calculate the dot product between a feature vector and a target vector
    dotProduct(field("features"), [0.5, 0.8, 0.2]);

### dotProduct(vectorExpression, otherVectorExpression)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Calculates the dot product between two vector expressions.

**Signature:**

    export declare function dotProduct(vectorExpression: Expression, otherVectorExpression: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| vectorExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The first vector (represented as an `Expression`) to calculate with. |
| otherVectorExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The other vector (represented as an `Expression`) to calculate with. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the dot product between the two vectors.

### Example

    // Calculate the dot product between two document vectors: 'docVector1' and 'docVector2'
    dotProduct(field("docVector1"), field("docVector2"));

### euclideanDistance(vectorExpression, vector)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Calculates the Euclidean distance between a vector expression and a double array.

**Signature:**

    export declare function euclideanDistance(vectorExpression: Expression, vector: number[] | VectorValue): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| vectorExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The first vector (represented as an `Expression`) to compare against. |
| vector | number\[\] \| [VectorValue](https://firebase.google.com/docs/reference/js/firestore_.vectorvalue.md#vectorvalue_class) | The other vector (as an array of doubles or VectorValue) to compare against. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the Euclidean distance between the two vectors.

### Example

    // Calculate the Euclidean distance between the 'location' field and a target location

    euclideanDistance(field("location"), [37.7749, -122.4194]);

### euclideanDistance(vectorExpression, otherVectorExpression)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Calculates the Euclidean distance between two vector expressions.

**Signature:**

    export declare function euclideanDistance(vectorExpression: Expression, otherVectorExpression: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| vectorExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The first vector (represented as an `Expression`) to compare against. |
| otherVectorExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The other vector (represented as an `Expression`) to compare against. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the Euclidean distance between the two vectors.

### Example

    // Calculate the Euclidean distance between two vector fields: 'pointA' and 'pointB'
    euclideanDistance(field("pointA"), field("pointB"));

### vectorLength(vectorExpression)

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that calculates the length of a Firestore Vector.

**Signature:**

    export declare function vectorLength(vectorExpression: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| vectorExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression representing the Firestore Vector. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the length of the array.

### Example

    // Get the vector length (dimension) of the field 'embedding'.
    vectorLength(field("embedding"));

## AddFieldsStageOptions

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Options defining how an AddFieldsStage is evaluated. See [Pipeline.addFields()](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipelineaddfields).

**Signature:**

    export declare type AddFieldsStageOptions = StageOptions & {
        fields: Selectable[];
    };

## AggregateStageOptions

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Options defining how an AggregateStage is evaluated. See [Pipeline.aggregate()](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipelineaggregate).

**Signature:**

    export declare type AggregateStageOptions = StageOptions & {
        accumulators: AliasedAggregate[];
        groups?: Array<string | Selectable>;
    };

## CollectionGroupStageOptions

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Defines the configuration options for a CollectionGroupStage within a pipeline. This type extends [StageOptions](https://firebase.google.com/docs/reference/js/firestore_pipelines.stageoptions.md#stageoptions_interface) and provides specific settings for how a collection group is identified and processed during pipeline execution.

See [PipelineSource.collectionGroup()](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelinesource.md#pipelinesourcecollectiongroup) to create a collection group stage.

**Signature:**

    export declare type CollectionGroupStageOptions = StageOptions & {
        collectionId: string;
        forceIndex?: string;
    };

## CollectionStageOptions

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Options defining how a CollectionStage is evaluated. See [PipelineSource.collection()](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelinesource.md#pipelinesourcecollection).

**Signature:**

    export declare type CollectionStageOptions = StageOptions & {
        collection: string | Query;
        forceIndex?: string;
    };

## DatabaseStageOptions

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Options defining how a DatabaseStage is evaluated. See [PipelineSource.database()](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelinesource.md#pipelinesourcedatabase).

**Signature:**

    export declare type DatabaseStageOptions = StageOptions & {};

## DistinctStageOptions

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Options defining how a DistinctStage is evaluated. See [Pipeline.distinct()](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipelinedistinct).

**Signature:**

    export declare type DistinctStageOptions = StageOptions & {
        groups: Array<string | Selectable>;
    };

## DocumentsStageOptions

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Options defining how a DocumentsStage is evaluated. See [PipelineSource.documents()](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelinesource.md#pipelinesourcedocuments).

**Signature:**

    export declare type DocumentsStageOptions = StageOptions & {
        docs: Array<string | DocumentReference>;
    };

## ExpressionType

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

An enumeration of the different types of expressions.

**Signature:**

    export declare type ExpressionType = 'Field' | 'Constant' | 'Function' | 'AggregateFunction' | 'ListOfExpressions' | 'AliasedExpression';

## FindNearestStageOptions

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Options defining how a FindNearestStage is evaluated. See [Pipeline.findNearest()](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipelinefindnearest).

**Signature:**

    export declare type FindNearestStageOptions = StageOptions & {
        field: Field | string;
        vectorValue: VectorValue | number[];
        distanceMeasure: 'euclidean' | 'cosine' | 'dot_product';
        limit?: number;
        distanceField?: string;
    };

## LimitStageOptions

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Options defining how a LimitStage is evaluated. See [Pipeline.limit()](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipelinelimit).

**Signature:**

    export declare type LimitStageOptions = StageOptions & {
        limit: number;
    };

## OffsetStageOptions

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Options defining how an OffsetStage is evaluated. See [Pipeline.offset()](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipelineoffset).

**Signature:**

    export declare type OffsetStageOptions = StageOptions & {
        offset: number;
    };

## OneOf

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Utility type to create an type that only allows one property of the Type param T to be set.

**Signature:**

    export declare type OneOf<T> = {
        [K in keyof T]: Pick<T, K> & {
            [P in Exclude<keyof T, K>]?: undefined;
        };
    }[keyof T];

### Example

    type XorY = OneOf<{ x: unknown, y: unknown }>
    let a = { x: "foo" }           // OK
    let b = { y: "foo" }           // OK
    let c = { a: "foo", y: "foo" } // Not OK

## PartialWithFieldValue

Similar to TypeScript's `Partial<T>`, but allows nested fields to be omitted and FieldValues to be passed in as property values.

**Signature:**

    export declare type PartialWithFieldValue<T> = Partial<T> | (T extends Primitive ? T : T extends {} ? {
        [K in keyof T]?: PartialWithFieldValue<T[K]> | FieldValue;
    } : never);

## Primitive

Primitive types.

**Signature:**

    export declare type Primitive = string | number | boolean | undefined | null;

## RemoveFieldsStageOptions

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Options defining how a RemoveFieldsStage is evaluated. See [Pipeline.removeFields()](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipelineremovefields).

**Signature:**

    export declare type RemoveFieldsStageOptions = StageOptions & {
        fields: Array<Field | string>;
    };

## ReplaceWithStageOptions

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Options defining how a ReplaceWithStage is evaluated. See [Pipeline.replaceWith()](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipelinereplacewith).

**Signature:**

    export declare type ReplaceWithStageOptions = StageOptions & {
        map: Expression | string;
    };

## SampleStageOptions

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Defines the options for evaluating a sample stage within a pipeline. This type combines common [StageOptions](https://firebase.google.com/docs/reference/js/firestore_pipelines.stageoptions.md#stageoptions_interface) with a specific configuration where only one of the defined sampling methods can be applied.

See [Pipeline.sample()](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipelinesample) to create a sample stage..

**Signature:**

    export declare type SampleStageOptions = StageOptions & OneOf<{
        percentage: number;
        documents: number;
    }>;

## SelectStageOptions

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Options defining how a SelectStage is evaluated. See [Pipeline.select()](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipelineselect).

**Signature:**

    export declare type SelectStageOptions = StageOptions & {
        selections: Array<Selectable | string>;
    };

## SetOptions

An options object that configures the behavior of [setDoc()](https://firebase.google.com/docs/reference/js/firestore_lite.md#setdoc_ee215ad), and calls. These calls can be configured to perform granular merges instead of overwriting the target documents in their entirety by providing a `SetOptions` with `merge: true`.

**Signature:**

    export declare type SetOptions = {
        readonly merge?: boolean;
    } | {
        readonly mergeFields?: Array<string | FieldPath>;
    };

## SortStageOptions

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Options defining how a SortStage is evaluated. See [Pipeline.sort()](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipelinesort).

**Signature:**

    export declare type SortStageOptions = StageOptions & {
        orderings: Ordering[];
    };

## TimeGranularity

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Specify time granularity for expressions.

**Signature:**

    export declare type TimeGranularity = 'microsecond' | 'millisecond' | 'second' | 'minute' | 'hour' | 'day' | 'week' | 'week(monday)' | 'week(tuesday)' | 'week(wednesday)' | 'week(thursday)' | 'week(friday)' | 'week(saturday)' | 'week(sunday)' | 'isoWeek' | 'month' | 'quarter' | 'year' | 'isoYear';

## Type

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

An enumeration of the different types generated by the Firestore backend.

- Numerics evaluate directly to backend representation (\`int64\` or \`float64\`), not JS \`number\`.
- JavaScript \`Date\` and firestore \`Timestamp\` objects strictly evaluate to \`'timestamp'\`.
- Advanced configurations parsing backend types (such as \`decimal128\`, \`max_key\` or \`min_key\` from BSON) are also incorporated in this union string type. Note that \`decimal128\` is a backend-only numeric type that the JavaScript SDK cannot create natively, but can be evaluated in pipelines.

**Signature:**

    export declare type Type = 'null' | 'array' | 'boolean' | 'bytes' | 'timestamp' | 'geo_point' | 'number' | 'int32' | 'int64' | 'float64' | 'decimal128' | 'map' | 'reference' | 'string' | 'vector' | 'max_key' | 'min_key' | 'object_id' | 'regex' | 'request_timestamp';

## UnionStageOptions

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Options defining how a UnionStage is evaluated. See [Pipeline.union()](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipelineunion).

**Signature:**

    export declare type UnionStageOptions = StageOptions & {
        other: Pipeline;
    };

## UnnestStageOptions

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Represents the specific options available for configuring an `UnnestStage` within a pipeline.

**Signature:**

    export declare type UnnestStageOptions = StageOptions & {
        selectable: Selectable;
        indexField?: string;
    };

## WhereStageOptions

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Options defining how a WhereStage is evaluated. See [Pipeline.where()](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipelinewhere).

**Signature:**

    export declare type WhereStageOptions = StageOptions & {
        condition: BooleanExpression;
    };

## WithFieldValue

Allows FieldValues to be passed in as a property value while maintaining type safety.

**Signature:**

    export declare type WithFieldValue<T> = T | (T extends Primitive ? T : T extends {} ? {
        [K in keyof T]: WithFieldValue<T[K]> | FieldValue;
    } : never);