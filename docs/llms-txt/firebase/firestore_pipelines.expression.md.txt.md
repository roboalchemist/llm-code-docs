# Source: https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md.txt

# Expression class

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Represents an expression that can be evaluated to a value within the execution of a [Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class).

Expressions are the building blocks for creating complex queries and transformations in Firestore pipelines. They can represent:

- \*\*Field references:\*\* Access values from document fields. - \*\*Literals:\*\* Represent constant values (strings, numbers, booleans). - \*\*Function calls:\*\* Apply functions to one or more expressions.

The `Expression` class provides a fluent API for building expressions. You can chain together method calls to create complex expressions.

**Signature:**

    export declare abstract class Expression 

## Properties

| Property | Modifiers | Type | Description |
|---|---|---|---|
| [expressionType](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionexpressiontype) |   | [ExpressionType](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#expressiontype) | ***(Public Preview)*** |

## Methods

| Method | Modifiers | Description |
|---|---|---|
| [abs()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionabs) |   | ***(Public Preview)*** Creates an expression that computes the absolute value of a numeric value. |
| [add(second)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionadd) |   | ***(Public Preview)*** Creates an expression that adds this expression to another expression. |
| [arrayAgg()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionarrayagg) |   | ***(Public Preview)*** Creates an aggregation that collects all values of an expression across multiple stage inputs into an array. |
| [arrayAggDistinct()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionarrayaggdistinct) |   | ***(Public Preview)*** Creates an aggregation that collects all distinct values of an expression across multiple stage inputs into an array. |
| [arrayConcat(secondArray, otherArrays)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionarrayconcat) |   | ***(Public Preview)*** Creates an expression that concatenates an array expression with one or more other arrays. |
| [arrayContains(expression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionarraycontains) |   | ***(Public Preview)*** Creates an expression that checks if an array contains a specific element. |
| [arrayContains(value)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionarraycontains) |   | ***(Public Preview)*** Creates an expression that checks if an array contains a specific value. |
| [arrayContainsAll(values)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionarraycontainsall) |   | ***(Public Preview)*** Creates an expression that checks if an array contains all the specified elements. |
| [arrayContainsAll(arrayExpression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionarraycontainsall) |   | ***(Public Preview)*** Creates an expression that checks if an array contains all the specified elements. |
| [arrayContainsAny(values)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionarraycontainsany) |   | ***(Public Preview)*** Creates an expression that checks if an array contains any of the specified elements. |
| [arrayContainsAny(arrayExpression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionarraycontainsany) |   | ***(Public Preview)*** Creates an expression that checks if an array contains any of the specified elements. |
| [arrayGet(offset)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionarrayget) |   | ***(Public Preview)*** Creates an expression that indexes into an array from the beginning or end and returns the element. If the offset exceeds the array length, an error is returned. A negative offset, starts from the end. |
| [arrayGet(offsetExpr)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionarrayget) |   | ***(Public Preview)*** Creates an expression that indexes into an array from the beginning or end and returns the element. If the offset exceeds the array length, an error is returned. A negative offset, starts from the end. |
| [arrayLength()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionarraylength) |   | ***(Public Preview)*** Creates an expression that calculates the length of an array. |
| [arrayReverse()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionarrayreverse) |   | ***(Public Preview)*** Creates an expression that reverses an array. |
| [arraySum()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionarraysum) |   | ***(Public Preview)*** Creates an expression that computes the sum of the elements in an array. |
| [as(name)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionas) |   | ***(Public Preview)*** Assigns an alias to this expression.Aliases are useful for renaming fields in the output of a stage or for giving meaningful names to calculated values. |
| [asBoolean()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionasboolean) |   | ***(Public Preview)*** Wraps the expression in a \[BooleanExpression\]. |
| [ascending()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionascending) |   | ***(Public Preview)*** Creates an [Ordering](https://firebase.google.com/docs/reference/js/firestore_pipelines.ordering.md#ordering_class) that sorts documents in ascending order based on this expression. |
| [average()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionaverage) |   | ***(Public Preview)*** Creates an aggregation that calculates the average (mean) of a numeric field across multiple stage inputs. |
| [byteLength()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionbytelength) |   | ***(Public Preview)*** Creates an expression that calculates the length of this string expression in bytes. |
| [ceil()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionceil) |   | ***(Public Preview)*** Creates an expression that computes the ceiling of a numeric value. |
| [charLength()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressioncharlength) |   | ***(Public Preview)*** Creates an expression that calculates the character length of a string in UTF-8. |
| [collectionId()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressioncollectionid) |   | ***(Public Preview)*** Creates an expression that returns the collection ID from a path. |
| [concat(second, others)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionconcat) |   | ***(Public Preview)*** Creates an expression that concatenates expression results together. |
| [cosineDistance(vectorExpression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressioncosinedistance) |   | ***(Public Preview)*** Calculates the cosine distance between two vectors. |
| [cosineDistance(vector)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressioncosinedistance) |   | ***(Public Preview)*** Calculates the Cosine distance between two vectors. |
| [count()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressioncount) |   | ***(Public Preview)*** Creates an aggregation that counts the number of stage inputs with valid evaluations of the expression or field. |
| [countDistinct()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressioncountdistinct) |   | ***(Public Preview)*** Creates an aggregation that counts the number of distinct values of the expression or field. |
| [descending()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressiondescending) |   | ***(Public Preview)*** Creates an [Ordering](https://firebase.google.com/docs/reference/js/firestore_pipelines.ordering.md#ordering_class) that sorts documents in descending order based on this expression. |
| [divide(divisor)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressiondivide) |   | ***(Public Preview)*** Creates an expression that divides this expression by another expression. |
| [divide(divisor)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressiondivide) |   | ***(Public Preview)*** Creates an expression that divides this expression by a constant value. |
| [documentId()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressiondocumentid) |   | ***(Public Preview)*** Creates an expression that returns the document ID from a path. |
| [dotProduct(vectorExpression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressiondotproduct) |   | ***(Public Preview)*** Calculates the dot product between two vectors. |
| [dotProduct(vector)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressiondotproduct) |   | ***(Public Preview)*** Calculates the dot product between two vectors. |
| [endsWith(suffix)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionendswith) |   | ***(Public Preview)*** Creates an expression that checks if a string ends with a given postfix. |
| [endsWith(suffix)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionendswith) |   | ***(Public Preview)*** Creates an expression that checks if a string ends with a given postfix (represented as an expression). |
| [equal(expression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionequal) |   | ***(Public Preview)*** Creates an expression that checks if this expression is equal to another expression. |
| [equal(value)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionequal) |   | ***(Public Preview)*** Creates an expression that checks if this expression is equal to a constant value. |
| [equalAny(values)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionequalany) |   | ***(Public Preview)*** Creates an expression that checks if this expression is equal to any of the provided values or expressions. |
| [equalAny(arrayExpression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionequalany) |   | ***(Public Preview)*** Creates an expression that checks if this expression is equal to any of the provided values or expressions. |
| [euclideanDistance(vectorExpression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressioneuclideandistance) |   | ***(Public Preview)*** Calculates the Euclidean distance between two vectors. |
| [euclideanDistance(vector)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressioneuclideandistance) |   | ***(Public Preview)*** Calculates the Euclidean distance between two vectors. |
| [exists()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionexists) |   | ***(Public Preview)*** Creates an expression that checks if a field exists in the document. |
| [exp()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionexp) |   | ***(Public Preview)*** Creates an expression that computes e to the power of this expression. |
| [first()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionfirst) |   | ***(Public Preview)*** Creates an aggregation that finds the first value of an expression across multiple stage inputs. |
| [floor()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionfloor) |   | ***(Public Preview)*** Creates an expression that computes the floor of a numeric value. |
| [greaterThan(expression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressiongreaterthan) |   | ***(Public Preview)*** Creates an expression that checks if this expression is greater than another expression. |
| [greaterThan(value)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressiongreaterthan) |   | ***(Public Preview)*** Creates an expression that checks if this expression is greater than a constant value. |
| [greaterThanOrEqual(expression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressiongreaterthanorequal) |   | ***(Public Preview)*** Creates an expression that checks if this expression is greater than or equal to another expression. |
| [greaterThanOrEqual(value)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressiongreaterthanorequal) |   | ***(Public Preview)*** Creates an expression that checks if this expression is greater than or equal to a constant value. |
| [ifAbsent(elseValue)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionifabsent) |   | ***(Public Preview)*** Creates an expression that returns the `elseValue` argument if this expression results in an absent value, else return the result of the this expression evaluation. |
| [ifAbsent(elseExpression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionifabsent) |   | ***(Public Preview)*** Creates an expression that returns the `elseValue` argument if this expression results in an absent value, else return the result of this expression evaluation. |
| [ifError(catchExpr)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressioniferror) |   | ***(Public Preview)*** Creates an expression that returns the result of the `catchExpr` argument if there is an error, else return the result of this expression. |
| [ifError(catchValue)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressioniferror) |   | ***(Public Preview)*** Creates an expression that returns the `catch` argument if there is an error, else return the result of this expression. |
| [isAbsent()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionisabsent) |   | ***(Public Preview)*** Creates an expression that returns `true` if the result of this expression is absent. Otherwise, returns `false` even if the value is `null`. |
| [isError()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressioniserror) |   | ***(Public Preview)*** Creates an expression that checks if a given expression produces an error. |
| [isType(type)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionistype) |   | ***(Public Preview)*** Creates an expression that checks if the result of this expression is of the given type. |
| [join(delimiterExpression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionjoin) |   | ***(Public Preview)*** Creates an expression that joins the elements of an array into a string. |
| [join(delimiter)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionjoin) |   | ***(Public Preview)*** Creates an expression that joins the elements of an array field into a string. |
| [last()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionlast) |   | ***(Public Preview)*** Creates an aggregation that finds the last value of an expression across multiple stage inputs. |
| [length()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionlength) |   | ***(Public Preview)*** Creates an expression that calculates the length of a string, array, map, vector, or bytes. |
| [lessThan(experession)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionlessthan) |   | ***(Public Preview)*** Creates an expression that checks if this expression is less than another expression. |
| [lessThan(value)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionlessthan) |   | ***(Public Preview)*** Creates an expression that checks if this expression is less than a constant value. |
| [lessThanOrEqual(expression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionlessthanorequal) |   | ***(Public Preview)*** Creates an expression that checks if this expression is less than or equal to another expression. |
| [lessThanOrEqual(value)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionlessthanorequal) |   | ***(Public Preview)*** Creates an expression that checks if this expression is less than or equal to a constant value. |
| [like(pattern)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionlike) |   | ***(Public Preview)*** Creates an expression that performs a case-sensitive string comparison. |
| [like(pattern)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionlike) |   | ***(Public Preview)*** Creates an expression that performs a case-sensitive string comparison. |
| [ln()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionln) |   | ***(Public Preview)*** Creates an expression that computes the natural logarithm of a numeric value. |
| [log10()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionlog10) |   | ***(Public Preview)*** Creates an expression that computes the base-10 logarithm of a numeric value. |
| [logicalMaximum(second, others)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionlogicalmaximum) |   | ***(Public Preview)*** Creates an expression that returns the larger value between this expression and another expression, based on Firestore's value type ordering. |
| [logicalMinimum(second, others)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionlogicalminimum) |   | ***(Public Preview)*** Creates an expression that returns the smaller value between this expression and another expression, based on Firestore's value type ordering. |
| [ltrim(valueToTrim)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionltrim) |   | ***(Public Preview)*** Trims whitespace or a specified set of characters/bytes from the beginning of a string or byte array. |
| [mapEntries()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionmapentries) |   | ***(Public Preview)*** Creates an expression that returns the entries of a map as an array of maps, where each map contains a `"k"` property for the key and a `"v"` property for the value. For example: `[{ k: "key1", v: "value1" }, ...]`. |
| [mapGet(subfield)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionmapget) |   | ***(Public Preview)*** Accesses a value from a map (object) field using the provided key. |
| [mapKeys()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionmapkeys) |   | ***(Public Preview)*** Creates an expression that returns the keys of a map. |
| [mapMerge(secondMap, otherMaps)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionmapmerge) |   | ***(Public Preview)*** Creates an expression that merges multiple map values. |
| [mapRemove(key)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionmapremove) |   | ***(Public Preview)*** Creates an expression that removes a key from the map produced by evaluating this expression. |
| [mapRemove(keyExpr)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionmapremove) |   | ***(Public Preview)*** Creates an expression that removes a key from the map produced by evaluating this expression. |
| [mapSet(key, value, moreKeyValues)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionmapset) |   | ***(Public Preview)*** Creates an expression that returns a new map with the specified entries added or updated. |
| [mapValues()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionmapvalues) |   | ***(Public Preview)*** Creates an expression that returns the values of a map. |
| [maximum()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionmaximum) |   | ***(Public Preview)*** Creates an aggregation that finds the maximum value of a field across multiple stage inputs. |
| [minimum()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionminimum) |   | ***(Public Preview)*** Creates an aggregation that finds the minimum value of a field across multiple stage inputs. |
| [mod(expression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionmod) |   | ***(Public Preview)*** Creates an expression that calculates the modulo (remainder) of dividing this expression by another expression. |
| [mod(value)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionmod) |   | ***(Public Preview)*** Creates an expression that calculates the modulo (remainder) of dividing this expression by a constant value. |
| [multiply(second)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionmultiply) |   | ***(Public Preview)*** Creates an expression that multiplies this expression by another expression. |
| [notEqual(expression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionnotequal) |   | ***(Public Preview)*** Creates an expression that checks if this expression is not equal to another expression. |
| [notEqual(value)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionnotequal) |   | ***(Public Preview)*** Creates an expression that checks if this expression is not equal to a constant value. |
| [notEqualAny(values)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionnotequalany) |   | ***(Public Preview)*** Creates an expression that checks if this expression is not equal to any of the provided values or expressions. |
| [notEqualAny(arrayExpression)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionnotequalany) |   | ***(Public Preview)*** Creates an expression that checks if this expression is not equal to any of the values in the evaluated expression. |
| [pow(exponent)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionpow) |   | ***(Public Preview)*** Creates an expression that returns the value of this expression raised to the power of another expression. |
| [pow(exponent)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionpow) |   | ***(Public Preview)*** Creates an expression that returns the value of this expression raised to the power of a constant value. |
| [regexContains(pattern)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionregexcontains) |   | ***(Public Preview)*** Creates an expression that checks if a string contains a specified regular expression as a substring. |
| [regexContains(pattern)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionregexcontains) |   | ***(Public Preview)*** Creates an expression that checks if a string contains a specified regular expression as a substring. |
| [regexFind(pattern)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionregexfind) |   | ***(Public Preview)*** Creates an expression that returns the first substring of a string expression that matches a specified regular expression.This expression uses the [RE2](https://github.com/google/re2/wiki/Syntax) regular expression syntax. |
| [regexFind(pattern)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionregexfind) |   | ***(Public Preview)*** Creates an expression that returns the first substring of a string expression that matches a specified regular expression.This expression uses the [RE2](https://github.com/google/re2/wiki/Syntax) regular expression syntax. |
| [regexFindAll(pattern)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionregexfindall) |   | ***(Public Preview)*** Creates an expression that evaluates to a list of all substrings in this string expression that match a specified regular expression.This expression uses the [RE2](https://github.com/google/re2/wiki/Syntax) regular expression syntax. |
| [regexFindAll(pattern)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionregexfindall) |   | ***(Public Preview)*** Creates an expression that evaluates to a list of all substrings in this string expression that match a specified regular expression.This expression uses the [RE2](https://github.com/google/re2/wiki/Syntax) regular expression syntax. |
| [regexMatch(pattern)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionregexmatch) |   | ***(Public Preview)*** Creates an expression that checks if a string matches a specified regular expression. |
| [regexMatch(pattern)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionregexmatch) |   | ***(Public Preview)*** Creates an expression that checks if a string matches a specified regular expression. |
| [reverse()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionreverse) |   | ***(Public Preview)*** Creates an expression that reverses this string expression. |
| [round()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionround) |   | ***(Public Preview)*** Creates an expression that rounds a numeric value to the nearest whole number. |
| [round(decimalPlaces)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionround) |   | ***(Public Preview)*** Creates an expression that rounds a numeric value to the specified number of decimal places. |
| [round(decimalPlaces)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionround) |   | ***(Public Preview)*** Creates an expression that rounds a numeric value to the specified number of decimal places. |
| [rtrim(valueToTrim)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionrtrim) |   | ***(Public Preview)*** Trims whitespace or a specified set of characters/bytes from the end of a string or byte array. |
| [split(delimiter)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionsplit) |   | ***(Public Preview)*** Creates an expression that splits the result of this expression into an array of substrings based on the provided delimiter. |
| [split(delimiter)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionsplit) |   | ***(Public Preview)*** Creates an expression that splits the result of this expression into an array of substrings based on the provided delimiter. |
| [sqrt()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionsqrt) |   | ***(Public Preview)*** Creates an expression that computes the square root of a numeric value. |
| [startsWith(prefix)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionstartswith) |   | ***(Public Preview)*** Creates an expression that checks if a string starts with a given prefix. |
| [startsWith(prefix)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionstartswith) |   | ***(Public Preview)*** Creates an expression that checks if a string starts with a given prefix (represented as an expression). |
| [stringConcat(secondString, otherStrings)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionstringconcat) |   | ***(Public Preview)*** Creates an expression that concatenates string expressions together. |
| [stringContains(substring)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionstringcontains) |   | ***(Public Preview)*** Creates an expression that checks if a string contains a specified substring. |
| [stringContains(expr)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionstringcontains) |   | ***(Public Preview)*** Creates an expression that checks if a string contains the string represented by another expression. |
| [stringIndexOf(search)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionstringindexof) |   | ***(Public Preview)*** Creates an expression that finds the index of the first occurrence of a substring or byte sequence. |
| [stringRepeat(repetitions)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionstringrepeat) |   | ***(Public Preview)*** Creates an expression that repeats a string or byte array a specified number of times. |
| [stringReplaceAll(find, replacement)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionstringreplaceall) |   | ***(Public Preview)*** Creates an expression that replaces all occurrences of a substring or byte sequence with a replacement. |
| [stringReplaceOne(find, replacement)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionstringreplaceone) |   | ***(Public Preview)*** Creates an expression that replaces the first occurrence of a substring or byte sequence with a replacement. |
| [stringReverse()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionstringreverse) |   | ***(Public Preview)*** Creates an expression that reverses a string. |
| [substring(position, length)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionsubstring) |   | ***(Public Preview)*** Creates an expression that returns a substring of the results of this expression. |
| [substring(position, length)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionsubstring) |   | ***(Public Preview)*** Creates an expression that returns a substring of the results of this expression. |
| [subtract(subtrahend)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionsubtract) |   | ***(Public Preview)*** Creates an expression that subtracts another expression from this expression. |
| [subtract(subtrahend)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionsubtract) |   | ***(Public Preview)*** Creates an expression that subtracts a constant value from this expression. |
| [sum()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionsum) |   | ***(Public Preview)*** Creates an aggregation that calculates the sum of a numeric field across multiple stage inputs. |
| [timestampAdd(unit, amount)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressiontimestampadd) |   | ***(Public Preview)*** Creates an expression that adds a specified amount of time to this timestamp expression. |
| [timestampAdd(unit, amount)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressiontimestampadd) |   | ***(Public Preview)*** Creates an expression that adds a specified amount of time to this timestamp expression. |
| [timestampSubtract(unit, amount)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressiontimestampsubtract) |   | ***(Public Preview)*** Creates an expression that subtracts a specified amount of time from this timestamp expression. |
| [timestampSubtract(unit, amount)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressiontimestampsubtract) |   | ***(Public Preview)*** Creates an expression that subtracts a specified amount of time from this timestamp expression. |
| [timestampToUnixMicros()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressiontimestamptounixmicros) |   | ***(Public Preview)*** Creates an expression that converts this timestamp expression to the number of microseconds since the Unix epoch (1970-01-01 00:00:00 UTC). |
| [timestampToUnixMillis()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressiontimestamptounixmillis) |   | ***(Public Preview)*** Creates an expression that converts this timestamp expression to the number of milliseconds since the Unix epoch (1970-01-01 00:00:00 UTC). |
| [timestampToUnixSeconds()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressiontimestamptounixseconds) |   | ***(Public Preview)*** Creates an expression that converts this timestamp expression to the number of seconds since the Unix epoch (1970-01-01 00:00:00 UTC). |
| [timestampTruncate(granularity, timezone)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressiontimestamptruncate) |   | ***(Public Preview)*** Creates an expression that truncates a timestamp to a specified granularity. |
| [timestampTruncate(granularity, timezone)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressiontimestamptruncate) |   | ***(Public Preview)*** Creates an expression that truncates a timestamp to a specified granularity. |
| [toLower()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressiontolower) |   | ***(Public Preview)*** Creates an expression that converts a string to lowercase. |
| [toUpper()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressiontoupper) |   | ***(Public Preview)*** Creates an expression that converts a string to uppercase. |
| [trim(valueToTrim)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressiontrim) |   | ***(Public Preview)*** Creates an expression that removes leading and trailing characters from a string or byte array. |
| [trunc()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressiontrunc) |   | ***(Public Preview)*** Creates an expression that truncates the numeric value to an integer. |
| [trunc(decimalPlaces)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressiontrunc) |   | ***(Public Preview)*** Creates an expression that truncates a numeric value to the specified number of decimal places. |
| [trunc(decimalPlaces)](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressiontrunc) |   | ***(Public Preview)*** Creates an expression that truncates a numeric value to the specified number of decimal places. |
| [type()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressiontype) |   | ***(Public Preview)*** Creates an expression that returns the data type of this expression's result, as a string. |
| [unixMicrosToTimestamp()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionunixmicrostotimestamp) |   | ***(Public Preview)*** Creates an expression that interprets this expression as the number of microseconds since the Unix epoch (1970-01-01 00:00:00 UTC) and returns a timestamp. |
| [unixMillisToTimestamp()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionunixmillistotimestamp) |   | ***(Public Preview)*** Creates an expression that interprets this expression as the number of milliseconds since the Unix epoch (1970-01-01 00:00:00 UTC) and returns a timestamp. |
| [unixSecondsToTimestamp()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionunixsecondstotimestamp) |   | ***(Public Preview)*** Creates an expression that interprets this expression as the number of seconds since the Unix epoch (1970-01-01 00:00:00 UTC) and returns a timestamp. |
| [vectorLength()](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expressionvectorlength) |   | ***(Public Preview)*** Creates an expression that calculates the length (number of dimensions) of this Firestore Vector expression. |

## Expression.expressionType

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**

    abstract readonly expressionType: ExpressionType;

## Expression.abs()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that computes the absolute value of a numeric value.

**Signature:**

    abs(): FunctionExpression;

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the absolute value of the numeric value.

### Example

    // Compute the absolute value of the 'price' field.
    field("price").abs();

## Expression.add()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that adds this expression to another expression.

**Signature:**

    add(second: Expression | unknown): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| second | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| unknown | The expression or literal to add to this expression. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the addition operation.

### Example

    // Add the value of the 'quantity' field and the 'reserve' field.
    field("quantity").add(field("reserve"));

## Expression.arrayAgg()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an aggregation that collects all values of an expression across multiple stage inputs into an array.

If the expression resolves to an absent value, it is converted to `null`. The order of elements in the output array is not stable and shouldn't be relied upon.

**Signature:**

    arrayAgg(): AggregateFunction;

**Returns:**

[AggregateFunction](https://firebase.google.com/docs/reference/js/firestore_pipelines.aggregatefunction.md#aggregatefunction_class)

A new `AggregateFunction` representing the 'array_agg' aggregation.

### Example

    // Collect all tags from books into an array
    field("tags").arrayAgg().as("allTags");

## Expression.arrayAggDistinct()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an aggregation that collects all distinct values of an expression across multiple stage inputs into an array.

If the expression resolves to an absent value, it is converted to `null`. The order of elements in the output array is not stable and shouldn't be relied upon.

**Signature:**

    arrayAggDistinct(): AggregateFunction;

**Returns:**

[AggregateFunction](https://firebase.google.com/docs/reference/js/firestore_pipelines.aggregatefunction.md#aggregatefunction_class)

A new `AggregateFunction` representing the 'array_agg_distinct' aggregation.

### Example

    // Collect all distinct tags from books into an array
    field("tags").arrayAggDistinct().as("allDistinctTags");

## Expression.arrayConcat()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that concatenates an array expression with one or more other arrays.

**Signature:**

    arrayConcat(secondArray: Expression | unknown[], ...otherArrays: Array<Expression | unknown[]>): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| secondArray | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| unknown\[\] | Second array expression or array literal to concatenate. |
| otherArrays | Array\<[Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| unknown\[\]\> | Optional additional array expressions or array literals to concatenate. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the concatenated array.

### Example

    // Combine the 'items' array with another array field.
    field("items").arrayConcat(field("otherItems"));

## Expression.arrayContains()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if an array contains a specific element.

**Signature:**

    arrayContains(expression: Expression): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The element to search for in the array. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `Expression` representing the 'array_contains' comparison.

### Example

    // Check if the 'sizes' array contains the value from the 'selectedSize' field
    field("sizes").arrayContains(field("selectedSize"));

## Expression.arrayContains()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if an array contains a specific value.

**Signature:**

    arrayContains(value: unknown): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| value | unknown | The element to search for in the array. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `Expression` representing the 'array_contains' comparison.

### Example

    // Check if the 'colors' array contains "red"
    field("colors").arrayContains("red");

## Expression.arrayContainsAll()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if an array contains all the specified elements.

**Signature:**

    arrayContainsAll(values: Array<Expression | unknown>): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| values | Array\<[Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| unknown\> | The elements to check for in the array. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `Expression` representing the 'array_contains_all' comparison.

### Example

    // Check if the 'tags' array contains both the value in field "tag1" and the literal value "tag2"
    field("tags").arrayContainsAll([field("tag1"), "tag2"]);

## Expression.arrayContainsAll()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if an array contains all the specified elements.

**Signature:**

    arrayContainsAll(arrayExpression: Expression): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| arrayExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The elements to check for in the array. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `Expression` representing the 'array_contains_all' comparison.

### Example

    // Check if the 'tags' array contains both of the values from field "tag1" and the literal value "tag2"
    field("tags").arrayContainsAll(array([field("tag1"), "tag2"]));

## Expression.arrayContainsAny()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if an array contains any of the specified elements.

**Signature:**

    arrayContainsAny(values: Array<Expression | unknown>): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| values | Array\<[Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| unknown\> | The elements to check for in the array. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `Expression` representing the 'array_contains_any' comparison.

### Example

    // Check if the 'categories' array contains either values from field "cate1" or "cate2"
    field("categories").arrayContainsAny([field("cate1"), field("cate2")]);

## Expression.arrayContainsAny()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if an array contains any of the specified elements.

**Signature:**

    arrayContainsAny(arrayExpression: Expression): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| arrayExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The elements to check for in the array. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `Expression` representing the 'array_contains_any' comparison.

### Example

    // Check if the 'groups' array contains either the value from the 'userGroup' field
    // or the value "guest"
    field("groups").arrayContainsAny(array([field("userGroup"), "guest"]));

## Expression.arrayGet()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that indexes into an array from the beginning or end and returns the element. If the offset exceeds the array length, an error is returned. A negative offset, starts from the end.

**Signature:**

    arrayGet(offset: number): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| offset | number | The index of the element to return. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the 'arrayGet' operation.

### Example

    // Return the value in the 'tags' field array at index `1`.
    field('tags').arrayGet(1);

## Expression.arrayGet()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that indexes into an array from the beginning or end and returns the element. If the offset exceeds the array length, an error is returned. A negative offset, starts from the end.

**Signature:**

    arrayGet(offsetExpr: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| offsetExpr | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | An `Expression` evaluating to the index of the element to return. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the 'arrayGet' operation.

### Example

    // Return the value in the tags field array at index specified by field
    // 'favoriteTag'.
    field('tags').arrayGet(field('favoriteTag'));

## Expression.arrayLength()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that calculates the length of an array.

**Signature:**

    arrayLength(): FunctionExpression;

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the length of the array.

### Example

    // Get the number of items in the 'cart' array
    field("cart").arrayLength();

## Expression.arrayReverse()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that reverses an array.

**Signature:**

    arrayReverse(): FunctionExpression;

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the reversed array.

### Example

    // Reverse the value of the 'myArray' field.
    field("myArray").arrayReverse();

## Expression.arraySum()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that computes the sum of the elements in an array.

**Signature:**

    arraySum(): FunctionExpression;

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the sum of the elements in the array.

### Example

    // Compute the sum of the elements in the 'scores' field.
    field("scores").arraySum();

## Expression.as()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Assigns an alias to this expression.

Aliases are useful for renaming fields in the output of a stage or for giving meaningful names to calculated values.

**Signature:**

    as(name: string): AliasedExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| name | string | The alias to assign to this expression. |

**Returns:**

[AliasedExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.aliasedexpression.md#aliasedexpression_class)

A new [AliasedExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.aliasedexpression.md#aliasedexpression_class) that wraps this expression and associates it with the provided alias.

### Example

    // Calculate the total price and assign it the alias "totalPrice" and add it to the output.
    firestore.pipeline().collection("items")
      .addFields(field("price").multiply(field("quantity")).as("totalPrice"));

## Expression.asBoolean()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Wraps the expression in a \[BooleanExpression\].

**Signature:**

    asBoolean(): BooleanExpression;

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A \[BooleanExpression\] representing the same expression.

## Expression.ascending()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an [Ordering](https://firebase.google.com/docs/reference/js/firestore_pipelines.ordering.md#ordering_class) that sorts documents in ascending order based on this expression.

**Signature:**

    ascending(): Ordering;

**Returns:**

[Ordering](https://firebase.google.com/docs/reference/js/firestore_pipelines.ordering.md#ordering_class)

A new `Ordering` for ascending sorting.

### Example

    // Sort documents by the 'name' field in ascending order
    pipeline().collection("users")
      .sort(field("name").ascending());

## Expression.average()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an aggregation that calculates the average (mean) of a numeric field across multiple stage inputs.

**Signature:**

    average(): AggregateFunction;

**Returns:**

[AggregateFunction](https://firebase.google.com/docs/reference/js/firestore_pipelines.aggregatefunction.md#aggregatefunction_class)

A new `AggregateFunction` representing the 'average' aggregation.

### Example

    // Calculate the average age of users
    field("age").average().as("averageAge");

## Expression.byteLength()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that calculates the length of this string expression in bytes.

**Signature:**

    byteLength(): FunctionExpression;

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the length of the string in bytes.

### Example

    // Calculate the length of the 'myString' field in bytes.
    field("myString").byteLength();

## Expression.ceil()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that computes the ceiling of a numeric value.

**Signature:**

    ceil(): FunctionExpression;

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the ceiling of the numeric value.

### Example

    // Compute the ceiling of the 'price' field.
    field("price").ceil();

## Expression.charLength()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that calculates the character length of a string in UTF-8.

**Signature:**

    charLength(): FunctionExpression;

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the length of the string.

### Example

    // Get the character length of the 'name' field in its UTF-8 form.
    field("name").charLength();

## Expression.collectionId()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns the collection ID from a path.

**Signature:**

    collectionId(): FunctionExpression;

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the collectionId operation.

### Example

    // Get the collection ID from a path.
    field("__path__").collectionId();

## Expression.concat()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that concatenates expression results together.

**Signature:**

    concat(second: Expression | unknown, ...others: Array<Expression | unknown>): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| second | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| unknown | The additional expression or literal to concatenate. |
| others | Array\<[Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| unknown\> | Optional additional expressions or literals to concatenate. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the concatenated value.

### Example

    // Combine the 'firstName', ' ', and 'lastName' fields into a single value.
    field("firstName").concat(constant(" "), field("lastName"));

## Expression.cosineDistance()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Calculates the cosine distance between two vectors.

**Signature:**

    cosineDistance(vectorExpression: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| vectorExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The other vector (represented as an Expression) to compare against. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the cosine distance between the two vectors.

### Example

    // Calculate the cosine distance between the 'userVector' field and the 'itemVector' field
    field("userVector").cosineDistance(field("itemVector"));

## Expression.cosineDistance()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Calculates the Cosine distance between two vectors.

**Signature:**

    cosineDistance(vector: VectorValue | number[]): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| vector | [VectorValue](https://firebase.google.com/docs/reference/js/firestore_.vectorvalue.md#vectorvalue_class) \| number\[\] | The other vector (as a VectorValue) to compare against. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the Cosine\* distance between the two vectors.

### Example

    // Calculate the Cosine distance between the 'location' field and a target location
    field("location").cosineDistance(new VectorValue([37.7749, -122.4194]));

## Expression.count()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an aggregation that counts the number of stage inputs with valid evaluations of the expression or field.

**Signature:**

    count(): AggregateFunction;

**Returns:**

[AggregateFunction](https://firebase.google.com/docs/reference/js/firestore_pipelines.aggregatefunction.md#aggregatefunction_class)

A new `AggregateFunction` representing the 'count' aggregation.

### Example

    // Count the total number of products
    field("productId").count().as("totalProducts");

## Expression.countDistinct()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an aggregation that counts the number of distinct values of the expression or field.

**Signature:**

    countDistinct(): AggregateFunction;

**Returns:**

[AggregateFunction](https://firebase.google.com/docs/reference/js/firestore_pipelines.aggregatefunction.md#aggregatefunction_class)

A new `AggregateFunction` representing the 'count_distinct' aggregation.

### Example

    // Count the distinct number of products
    field("productId").countDistinct().as("distinctProducts");

## Expression.descending()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an [Ordering](https://firebase.google.com/docs/reference/js/firestore_pipelines.ordering.md#ordering_class) that sorts documents in descending order based on this expression.

**Signature:**

    descending(): Ordering;

**Returns:**

[Ordering](https://firebase.google.com/docs/reference/js/firestore_pipelines.ordering.md#ordering_class)

A new `Ordering` for descending sorting.

### Example

    // Sort documents by the 'createdAt' field in descending order
    firestore.pipeline().collection("users")
      .sort(field("createdAt").descending());

## Expression.divide()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that divides this expression by another expression.

**Signature:**

    divide(divisor: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| divisor | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression to divide by. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the division operation.

### Example

    // Divide the 'total' field by the 'count' field
    field("total").divide(field("count"));

## Expression.divide()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that divides this expression by a constant value.

**Signature:**

    divide(divisor: number): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| divisor | number | The constant value to divide by. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the division operation.

### Example

    // Divide the 'value' field by 10
    field("value").divide(10);

## Expression.documentId()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns the document ID from a path.

**Signature:**

    documentId(): FunctionExpression;

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the documentId operation.

### Example

    // Get the document ID from a path.
    field("__path__").documentId();

## Expression.dotProduct()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Calculates the dot product between two vectors.

**Signature:**

    dotProduct(vectorExpression: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| vectorExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The other vector (as an array of numbers) to calculate with. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the dot product between the two vectors.

### Example

    // Calculate the dot product between a feature vector and a target vector
    field("features").dotProduct([0.5, 0.8, 0.2]);

## Expression.dotProduct()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Calculates the dot product between two vectors.

**Signature:**

    dotProduct(vector: VectorValue | number[]): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| vector | [VectorValue](https://firebase.google.com/docs/reference/js/firestore_.vectorvalue.md#vectorvalue_class) \| number\[\] | The other vector (as an array of numbers) to calculate with. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the dot product between the two vectors.

### Example

    // Calculate the dot product between a feature vector and a target vector
    field("features").dotProduct(new VectorValue([0.5, 0.8, 0.2]));

## Expression.endsWith()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if a string ends with a given postfix.

**Signature:**

    endsWith(suffix: string): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| suffix | string | The postfix to check for. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `Expression` representing the 'ends with' comparison.

### Example

    // Check if the 'filename' field ends with ".txt"
    field("filename").endsWith(".txt");

## Expression.endsWith()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if a string ends with a given postfix (represented as an expression).

**Signature:**

    endsWith(suffix: Expression): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| suffix | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The postfix expression to check for. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `Expression` representing the 'ends with' comparison.

### Example

    // Check if the 'url' field ends with the value of the 'extension' field
    field("url").endsWith(field("extension"));

## Expression.equal()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if this expression is equal to another expression.

**Signature:**

    equal(expression: Expression): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression to compare for equality. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `Expression` representing the equality comparison.

### Example

    // Check if the 'age' field is equal to 21
    field("age").equal(21);

## Expression.equal()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if this expression is equal to a constant value.

**Signature:**

    equal(value: unknown): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| value | unknown | The constant value to compare for equality. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `Expression` representing the equality comparison.

### Example

    // Check if the 'city' field is equal to "London"
    field("city").equal("London");

## Expression.equalAny()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if this expression is equal to any of the provided values or expressions.

**Signature:**

    equalAny(values: Array<Expression | unknown>): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| values | Array\<[Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| unknown\> | The values or expressions to check against. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `Expression` representing the 'IN' comparison.

### Example

    // Check if the 'category' field is either "Electronics" or value of field 'primaryType'
    field("category").equalAny("Electronics", field("primaryType"));

## Expression.equalAny()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if this expression is equal to any of the provided values or expressions.

**Signature:**

    equalAny(arrayExpression: Expression): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| arrayExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | An expression that evaluates to an array of values to check against. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `Expression` representing the 'IN' comparison.

### Example

    // Check if the 'category' field is either "Electronics" or value of field 'primaryType'
    field("category").equalAny(array(["Electronics", field("primaryType")]));

## Expression.euclideanDistance()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Calculates the Euclidean distance between two vectors.

**Signature:**

    euclideanDistance(vectorExpression: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| vectorExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The other vector (as an array of numbers) to calculate with. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the Euclidean distance between the two vectors.

### Example

    // Calculate the Euclidean distance between the 'location' field and a target location
    field("location").euclideanDistance([37.7749, -122.4194]);

## Expression.euclideanDistance()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Calculates the Euclidean distance between two vectors.

**Signature:**

    euclideanDistance(vector: VectorValue | number[]): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| vector | [VectorValue](https://firebase.google.com/docs/reference/js/firestore_.vectorvalue.md#vectorvalue_class) \| number\[\] | The other vector (as a VectorValue) to compare against. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the Euclidean distance between the two vectors.

### Example

    // Calculate the Euclidean distance between the 'location' field and a target location
    field("location").euclideanDistance(new VectorValue([37.7749, -122.4194]));

## Expression.exists()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if a field exists in the document.

**Signature:**

    exists(): BooleanExpression;

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `Expression` representing the 'exists' check.

### Example

    // Check if the document has a field named "phoneNumber"
    field("phoneNumber").exists();

## Expression.exp()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that computes e to the power of this expression.

**Signature:**

    exp(): FunctionExpression;

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the exp of the numeric value.

### Example

    // Compute e to the power of the 'value' field.
    field("value").exp();

## Expression.first()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an aggregation that finds the first value of an expression across multiple stage inputs.

**Signature:**

    first(): AggregateFunction;

**Returns:**

[AggregateFunction](https://firebase.google.com/docs/reference/js/firestore_pipelines.aggregatefunction.md#aggregatefunction_class)

A new `AggregateFunction` representing the 'first' aggregation.

### Example

    // Find the first value of the 'rating' field
    field("rating").first().as("firstRating");

## Expression.floor()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that computes the floor of a numeric value.

**Signature:**

    floor(): FunctionExpression;

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the floor of the numeric value.

### Example

    // Compute the floor of the 'price' field.
    field("price").floor();

## Expression.greaterThan()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if this expression is greater than another expression.

**Signature:**

    greaterThan(expression: Expression): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression to compare for greater than. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `Expression` representing the greater than comparison.

### Example

    // Check if the 'age' field is greater than the 'limit' field
    field("age").greaterThan(field("limit"));

## Expression.greaterThan()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if this expression is greater than a constant value.

**Signature:**

    greaterThan(value: unknown): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| value | unknown | The constant value to compare for greater than. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `Expression` representing the greater than comparison.

### Example

    // Check if the 'price' field is greater than 100
    field("price").greaterThan(100);

## Expression.greaterThanOrEqual()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if this expression is greater than or equal to another expression.

**Signature:**

    greaterThanOrEqual(expression: Expression): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression to compare for greater than or equal to. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `Expression` representing the greater than or equal to comparison.

### Example

    // Check if the 'quantity' field is greater than or equal to field 'requirement' plus 1
    field("quantity").greaterThanOrEqual(field('requirement').add(1));

## Expression.greaterThanOrEqual()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if this expression is greater than or equal to a constant value.

**Signature:**

    greaterThanOrEqual(value: unknown): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| value | unknown | The constant value to compare for greater than or equal to. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `Expression` representing the greater than or equal to comparison.

### Example

    // Check if the 'score' field is greater than or equal to 80
    field("score").greaterThanOrEqual(80);

## Expression.ifAbsent()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns the `elseValue` argument if this expression results in an absent value, else return the result of the this expression evaluation.

**Signature:**

    ifAbsent(elseValue: unknown): Expression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| elseValue | unknown | The value that will be returned if this Expression evaluates to an absent value. |

**Returns:**

[Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class)

A new \[Expression\] representing the ifAbsent operation.

### Example

    // Returns the value of the optional field 'optional_field', or returns 'default_value'
    // if the field is absent.
    field("optional_field").ifAbsent("default_value")

## Expression.ifAbsent()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns the `elseValue` argument if this expression results in an absent value, else return the result of this expression evaluation.

**Signature:**

    ifAbsent(elseExpression: unknown): Expression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| elseExpression | unknown | The Expression that will be evaluated if this Expression evaluates to an absent value. |

**Returns:**

[Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class)

A new \[Expression\] representing the ifAbsent operation.

### Example

    // Returns the value of the optional field 'optional_field', or if that is
    // absent, then returns the value of the field `
    field("optional_field").ifAbsent(field('default_field'))

## Expression.ifError()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns the result of the `catchExpr` argument if there is an error, else return the result of this expression.

**Signature:**

    ifError(catchExpr: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| catchExpr | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The catch expression that will be evaluated and returned if this expression produces an error. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the 'ifError' operation.

### Example

    // Returns the first item in the title field arrays, or returns
    // the entire title field if the array is empty or the field is another type.
    field("title").arrayGet(0).ifError(field("title"));

## Expression.ifError()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns the `catch` argument if there is an error, else return the result of this expression.

**Signature:**

    ifError(catchValue: unknown): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| catchValue | unknown | The value that will be returned if this expression produces an error. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the 'ifError' operation.

### Example

    // Returns the first item in the title field arrays, or returns
    // "Default Title"
    field("title").arrayGet(0).ifError("Default Title");

## Expression.isAbsent()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns `true` if the result of this expression is absent. Otherwise, returns `false` even if the value is `null`.

**Signature:**

    isAbsent(): BooleanExpression;

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new [BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class) representing the 'isAbsent' check.

### Example

    // Check if the field `value` is absent.
    field("value").isAbsent();
    @example

## Expression.isError()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if a given expression produces an error.

**Signature:**

    isError(): BooleanExpression;

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new [BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class) representing the 'isError' check.

### Example

    // Check if the result of a calculation is an error
    field("title").arrayContains(1).isError();

## Expression.isType()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if the result of this expression is of the given type.

Null or undefined fields evaluate to skip/error. Use `ifAbsent()` / `isAbsent()` to evaluate missing data.

**Signature:**

    isType(type: Type): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| type | [Type](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#type) | The type to check for. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `BooleanExpression` that evaluates to true if the expression's result is of the given type, false otherwise.

### Example

    // Check if the 'price' field is specifically an integer (not just 'number')
    field('price').isType('int64');

## Expression.join()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that joins the elements of an array into a string.

**Signature:**

    join(delimiterExpression: Expression): Expression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| delimiterExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression that evaluates to the delimiter string. |

**Returns:**

[Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class)

A new Expression representing the join operation.

### Example

    // Join the elements of the 'tags' field with the delimiter from the 'separator' field.
    field("tags").join(field("separator"))

## Expression.join()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that joins the elements of an array field into a string.

**Signature:**

    join(delimiter: string): Expression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| delimiter | string | The string to use as a delimiter. |

**Returns:**

[Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class)

A new Expression representing the join operation.

### Example

    // Join the elements of the 'tags' field with a comma and space.
    field("tags").join(", ")

## Expression.last()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an aggregation that finds the last value of an expression across multiple stage inputs.

**Signature:**

    last(): AggregateFunction;

**Returns:**

[AggregateFunction](https://firebase.google.com/docs/reference/js/firestore_pipelines.aggregatefunction.md#aggregatefunction_class)

A new `AggregateFunction` representing the 'last' aggregation.

### Example

    // Find the last value of the 'rating' field
    field("rating").last().as("lastRating");

## Expression.length()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that calculates the length of a string, array, map, vector, or bytes.

**Signature:**

    length(): FunctionExpression;

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the length of the string, array, map, vector, or bytes.

### Example

    // Get the length of the 'name' field.
    field("name").length();

    // Get the number of items in the 'cart' array.
    field("cart").length();

## Expression.lessThan()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if this expression is less than another expression.

**Signature:**

    lessThan(experession: Expression): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| experession | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression to compare for less than. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `Expression` representing the less than comparison.

### Example

    // Check if the 'age' field is less than 'limit'
    field("age").lessThan(field('limit'));

## Expression.lessThan()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if this expression is less than a constant value.

**Signature:**

    lessThan(value: unknown): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| value | unknown | The constant value to compare for less than. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `Expression` representing the less than comparison.

### Example

    // Check if the 'price' field is less than 50
    field("price").lessThan(50);

## Expression.lessThanOrEqual()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if this expression is less than or equal to another expression.

**Signature:**

    lessThanOrEqual(expression: Expression): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression to compare for less than or equal to. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `Expression` representing the less than or equal to comparison.

### Example

    // Check if the 'quantity' field is less than or equal to 20
    field("quantity").lessThan(constant(20));

## Expression.lessThanOrEqual()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if this expression is less than or equal to a constant value.

**Signature:**

    lessThanOrEqual(value: unknown): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| value | unknown | The constant value to compare for less than or equal to. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `Expression` representing the less than or equal to comparison.

### Example

    // Check if the 'score' field is less than or equal to 70
    field("score").lessThan(70);

## Expression.like()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that performs a case-sensitive string comparison.

**Signature:**

    like(pattern: string): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| pattern | string | The pattern to search for. You can use "%" as a wildcard character. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `Expression` representing the 'like' comparison.

### Example

    // Check if the 'title' field contains the word "guide" (case-sensitive)
    field("title").like("%guide%");

## Expression.like()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that performs a case-sensitive string comparison.

**Signature:**

    like(pattern: Expression): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| pattern | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The pattern to search for. You can use "%" as a wildcard character. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `Expression` representing the 'like' comparison.

### Example

    // Check if the 'title' field contains the word "guide" (case-sensitive)
    field("title").like("%guide%");

## Expression.ln()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that computes the natural logarithm of a numeric value.

**Signature:**

    ln(): FunctionExpression;

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the natural logarithm of the numeric value.

### Example

    // Compute the natural logarithm of the 'value' field.
    field("value").ln();

## Expression.log10()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that computes the base-10 logarithm of a numeric value.

**Signature:**

    log10(): FunctionExpression;

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the base-10 logarithm of the numeric value.

### Example

    // Compute the base-10 logarithm of the 'value' field.
    field("value").log10();

## Expression.logicalMaximum()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns the larger value between this expression and another expression, based on Firestore's value type ordering.

**Signature:**

    logicalMaximum(second: Expression | unknown, ...others: Array<Expression | unknown>): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| second | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| unknown | The second expression or literal to compare with. |
| others | Array\<[Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| unknown\> | Optional additional expressions or literals to compare with. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the logical maximum operation.

### Example

    // Returns the larger value between the 'timestamp' field and the current timestamp.
    field("timestamp").logicalMaximum(Function.currentTimestamp());

## Expression.logicalMinimum()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns the smaller value between this expression and another expression, based on Firestore's value type ordering.

**Signature:**

    logicalMinimum(second: Expression | unknown, ...others: Array<Expression | unknown>): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| second | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| unknown | The second expression or literal to compare with. |
| others | Array\<[Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| unknown\> | Optional additional expressions or literals to compare with. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the logical minimum operation.

### Example

    // Returns the smaller value between the 'timestamp' field and the current timestamp.
    field("timestamp").logicalMinimum(Function.currentTimestamp());

## Expression.ltrim()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Trims whitespace or a specified set of characters/bytes from the beginning of a string or byte array.

**Signature:**

    ltrim(valueToTrim?: string | Expression | Bytes): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| valueToTrim | string \| [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| [Bytes](https://firebase.google.com/docs/reference/js/firestore_.bytes.md#bytes_class) | Optional. A string or byte array containing the characters/bytes to trim. If not specified, whitespace will be trimmed. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the trimmed string.

### Example

    // Trim whitespace from the beginning of the 'userInput' field
    field("userInput").ltrim();

    // Trim quotes from the beginning of the 'userInput' field
    field("userInput").ltrim('"');

## Expression.mapEntries()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns the entries of a map as an array of maps, where each map contains a `"k"` property for the key and a `"v"` property for the value. For example: `[{ k: "key1", v: "value1" }, ...]`.

**Signature:**

    mapEntries(): FunctionExpression;

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the entries of the map.

### Example

    // Get the entries of the 'address' map
    field("address").mapEntries();

## Expression.mapGet()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Accesses a value from a map (object) field using the provided key.

**Signature:**

    mapGet(subfield: string): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| subfield | string | The key to access in the map. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the value associated with the given key in the map.

### Example

    // Get the 'city' value from the 'address' map field
    field("address").mapGet("city");

## Expression.mapKeys()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns the keys of a map.

While the backend generally preserves insertion order, relying on the order of the output array is not guaranteed and should be avoided.

**Signature:**

    mapKeys(): FunctionExpression;

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the keys of the map.

### Example

    // Get the keys of the 'address' map
    field("address").mapKeys();

## Expression.mapMerge()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that merges multiple map values.

**Signature:**

    mapMerge(secondMap: Record<string, unknown> | Expression, ...otherMaps: Array<Record<string, unknown> | Expression>): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| secondMap | Record\<string, unknown\> \| [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | A required second map to merge. Represented as a literal or an expression that returns a map. |
| otherMaps | Array\<Record\<string, unknown\> \| [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class)\> | Optional additional maps to merge. Each map is represented as a literal or an expression that returns a map. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the 'mapMerge' operation.

### Example

    // Merges the map in the settings field with, a map literal, and a map in
    // that is conditionally returned by another expression
    field('settings').mapMerge({ enabled: true }, conditional(field('isAdmin'), { admin: true}, {})

## Expression.mapRemove()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that removes a key from the map produced by evaluating this expression.

**Signature:**

    mapRemove(key: string): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| key | string | The name of the key to remove from the input map. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the 'mapRemove' operation.

### Example

    // Removes the key 'baz' from the input map.
    map({foo: 'bar', baz: true}).mapRemove('baz');

## Expression.mapRemove()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that removes a key from the map produced by evaluating this expression.

**Signature:**

    mapRemove(keyExpr: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| keyExpr | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | An expression that produces the name of the key to remove from the input map. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the 'mapRemove' operation.

### Example

    // Removes the key 'baz' from the input map.
    map({foo: 'bar', baz: true}).mapRemove(constant('baz'));
    @example

## Expression.mapSet()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns a new map with the specified entries added or updated.

Note that `mapSet` only performs shallow updates to the map. Setting a value to `null` will retain the key with a `null` value. To remove a key entirely, use `mapRemove`.

**Signature:**

    mapSet(key: string | Expression, value: unknown, ...moreKeyValues: unknown[]): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| key | string \| [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The key to set. Must be a string or a constant string expression. |
| value | unknown | The value to set. |
| moreKeyValues | unknown\[\] | Additional key-value pairs to set. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the map with the entries set.

### Example

    // Set the 'city' to "San Francisco" in the 'address' map
    field("address").mapSet("city", "San Francisco");

## Expression.mapValues()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns the values of a map.

While the backend generally preserves insertion order, relying on the order of the output array is not guaranteed and should be avoided.

**Signature:**

    mapValues(): FunctionExpression;

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the values of the map.

### Example

    // Get the values of the 'address' map
    field("address").mapValues();

## Expression.maximum()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an aggregation that finds the maximum value of a field across multiple stage inputs.

**Signature:**

    maximum(): AggregateFunction;

**Returns:**

[AggregateFunction](https://firebase.google.com/docs/reference/js/firestore_pipelines.aggregatefunction.md#aggregatefunction_class)

A new `AggregateFunction` representing the 'maximum' aggregation.

### Example

    // Find the highest score in a leaderboard
    field("score").maximum().as("highestScore");

## Expression.minimum()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an aggregation that finds the minimum value of a field across multiple stage inputs.

**Signature:**

    minimum(): AggregateFunction;

**Returns:**

[AggregateFunction](https://firebase.google.com/docs/reference/js/firestore_pipelines.aggregatefunction.md#aggregatefunction_class)

A new `AggregateFunction` representing the 'minimum' aggregation.

### Example

    // Find the lowest price of all products
    field("price").minimum().as("lowestPrice");

## Expression.mod()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that calculates the modulo (remainder) of dividing this expression by another expression.

**Signature:**

    mod(expression: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression to divide by. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the modulo operation.

### Example

    // Calculate the remainder of dividing the 'value' field by the 'divisor' field
    field("value").mod(field("divisor"));

## Expression.mod()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that calculates the modulo (remainder) of dividing this expression by a constant value.

**Signature:**

    mod(value: number): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| value | number | The constant value to divide by. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the modulo operation.

### Example

    // Calculate the remainder of dividing the 'value' field by 10
    field("value").mod(10);

## Expression.multiply()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that multiplies this expression by another expression.

**Signature:**

    multiply(second: Expression | number): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| second | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| number | The second expression or literal to multiply by. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the multiplication operation.

### Example

    // Multiply the 'quantity' field by the 'price' field
    field("quantity").multiply(field("price"));

## Expression.notEqual()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if this expression is not equal to another expression.

**Signature:**

    notEqual(expression: Expression): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression to compare for inequality. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `Expression` representing the inequality comparison.

### Example

    // Check if the 'status' field is not equal to "completed"
    field("status").notEqual("completed");

## Expression.notEqual()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if this expression is not equal to a constant value.

**Signature:**

    notEqual(value: unknown): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| value | unknown | The constant value to compare for inequality. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `Expression` representing the inequality comparison.

### Example

    // Check if the 'country' field is not equal to "USA"
    field("country").notEqual("USA");

## Expression.notEqualAny()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if this expression is not equal to any of the provided values or expressions.

**Signature:**

    notEqualAny(values: Array<Expression | unknown>): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| values | Array\<[Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| unknown\> | The values or expressions to check against. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `Expression` representing the 'notEqualAny' comparison.

### Example

    // Check if the 'status' field is neither "pending" nor the value of 'rejectedStatus'
    field("status").notEqualAny(["pending", field("rejectedStatus")]);

## Expression.notEqualAny()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if this expression is not equal to any of the values in the evaluated expression.

**Signature:**

    notEqualAny(arrayExpression: Expression): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| arrayExpression | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The values or expressions to check against. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `Expression` representing the 'notEqualAny' comparison.

### Example

    // Check if the 'status' field is not equal to any value in the field 'rejectedStatuses'
    field("status").notEqualAny(field('rejectedStatuses'));

## Expression.pow()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns the value of this expression raised to the power of another expression.

**Signature:**

    pow(exponent: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| exponent | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression to raise this expression to the power of. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the power operation.

### Example

    // Raise the value of the 'base' field to the power of the 'exponent' field.
    field("base").pow(field("exponent"));

## Expression.pow()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns the value of this expression raised to the power of a constant value.

**Signature:**

    pow(exponent: number): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| exponent | number | The constant value to raise this expression to the power of. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the power operation.

### Example

    // Raise the value of the 'base' field to the power of 2.
    field("base").pow(2);

## Expression.regexContains()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if a string contains a specified regular expression as a substring.

**Signature:**

    regexContains(pattern: string): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| pattern | string | The regular expression to use for the search. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `Expression` representing the 'contains' comparison.

### Example

    // Check if the 'description' field contains "example" (case-insensitive)
    field("description").regexContains("(?i)example");

## Expression.regexContains()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if a string contains a specified regular expression as a substring.

**Signature:**

    regexContains(pattern: Expression): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| pattern | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The regular expression to use for the search. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `Expression` representing the 'contains' comparison.

### Example

    // Check if the 'description' field contains the regular expression stored in field 'regex'
    field("description").regexContains(field("regex"));

## Expression.regexFind()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns the first substring of a string expression that matches a specified regular expression.

This expression uses the [RE2](https://github.com/google/re2/wiki/Syntax) regular expression syntax.

**Signature:**

    regexFind(pattern: string): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| pattern | string | The regular expression to search for. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the regular expression find function.

### Example

    // Extract the domain from an email address
    field("email").regexFind("@.+")

## Expression.regexFind()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns the first substring of a string expression that matches a specified regular expression.

This expression uses the [RE2](https://github.com/google/re2/wiki/Syntax) regular expression syntax.

**Signature:**

    regexFind(pattern: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| pattern | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The regular expression to search for. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the regular expression find function.

### Example

    // Extract the domain from an email address
    field("email").regexFind(field("domain"))

## Expression.regexFindAll()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that evaluates to a list of all substrings in this string expression that match a specified regular expression.

This expression uses the [RE2](https://github.com/google/re2/wiki/Syntax) regular expression syntax.

**Signature:**

    regexFindAll(pattern: string): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| pattern | string | The regular expression to search for. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) that evaluates to an array of matched substrings.

### Example

    // Extract all hashtags from a post content field
    field("content").regexFindAll("#[A-Za-z0-9_]+")

## Expression.regexFindAll()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that evaluates to a list of all substrings in this string expression that match a specified regular expression.

This expression uses the [RE2](https://github.com/google/re2/wiki/Syntax) regular expression syntax.

**Signature:**

    regexFindAll(pattern: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| pattern | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The regular expression to search for. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) that evaluates to an array of matched substrings.

### Example

    // Extract all names from a post content field
    field("content").regexFindAll(field("names"))

## Expression.regexMatch()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if a string matches a specified regular expression.

**Signature:**

    regexMatch(pattern: string): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| pattern | string | The regular expression to use for the match. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `Expression` representing the regular expression match.

### Example

    // Check if the 'email' field matches a valid email pattern
    field("email").regexMatch("[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}");

## Expression.regexMatch()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if a string matches a specified regular expression.

**Signature:**

    regexMatch(pattern: Expression): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| pattern | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The regular expression to use for the match. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `Expression` representing the regular expression match.

### Example

    // Check if the 'email' field matches a regular expression stored in field 'regex'
    field("email").regexMatch(field("regex"));

## Expression.reverse()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that reverses this string expression.

**Signature:**

    reverse(): FunctionExpression;

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the reversed string.

### Example

    // Reverse the value of the 'myString' field.
    field("myString").reverse();

## Expression.round()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that rounds a numeric value to the nearest whole number.

**Signature:**

    round(): FunctionExpression;

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the rounded value.

### Example

    // Round the value of the 'price' field.
    field("price").round();

## Expression.round()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that rounds a numeric value to the specified number of decimal places.

**Signature:**

    round(decimalPlaces: number): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| decimalPlaces | number | A constant specifying the rounding precision in decimal places. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the rounded value.

### Example

    // Round the value of the 'price' field to two decimal places.
    field("price").round(2);

## Expression.round()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that rounds a numeric value to the specified number of decimal places.

**Signature:**

    round(decimalPlaces: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| decimalPlaces | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | An expression specifying the rounding precision in decimal places. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the rounded value.

### Example

    // Round the value of the 'price' field to two decimal places.
    field("price").round(constant(2));

## Expression.rtrim()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Trims whitespace or a specified set of characters/bytes from the end of a string or byte array.

**Signature:**

    rtrim(valueToTrim?: string | Expression | Bytes): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| valueToTrim | string \| [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| [Bytes](https://firebase.google.com/docs/reference/js/firestore_.bytes.md#bytes_class) | Optional. A string or byte array containing the characters/bytes to trim. If not specified, whitespace will be trimmed. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the trimmed string or byte array.

### Example

    // Trim whitespace from the end of the 'userInput' field
    field("userInput").rtrim();

    // Trim quotes from the end of the 'userInput' field
    field("userInput").rtrim('"');

## Expression.split()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that splits the result of this expression into an array of substrings based on the provided delimiter.

**Signature:**

    split(delimiter: string): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| delimiter | string |   |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the split function.

### Example

    // Split the 'scoresCsv' field on delimiter ','
    field('scoresCsv').split(',')

## Expression.split()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that splits the result of this expression into an array of substrings based on the provided delimiter.

**Signature:**

    split(delimiter: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| delimiter | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) |   |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the split function.

### Example

    // Split the 'scores' field on delimiter ',' or ':' depending on the stored format
    field('scores').split(conditional(field('format').equal('csv'), constant(','), constant(':'))

## Expression.sqrt()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that computes the square root of a numeric value.

**Signature:**

    sqrt(): FunctionExpression;

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the square root of the numeric value.

### Example

    // Compute the square root of the 'value' field.
    field("value").sqrt();

## Expression.startsWith()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if a string starts with a given prefix.

**Signature:**

    startsWith(prefix: string): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| prefix | string | The prefix to check for. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `Expression` representing the 'starts with' comparison.

### Example

    // Check if the 'name' field starts with "Mr."
    field("name").startsWith("Mr.");

## Expression.startsWith()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if a string starts with a given prefix (represented as an expression).

**Signature:**

    startsWith(prefix: Expression): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| prefix | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The prefix expression to check for. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `Expression` representing the 'starts with' comparison.

### Example

    // Check if the 'fullName' field starts with the value of the 'firstName' field
    field("fullName").startsWith(field("firstName"));

## Expression.stringConcat()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that concatenates string expressions together.

**Signature:**

    stringConcat(secondString: Expression | string, ...otherStrings: Array<Expression | string>): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| secondString | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| string | The additional expression or string literal to concatenate. |
| otherStrings | Array\<[Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| string\> | Optional additional expressions or string literals to concatenate. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the concatenated string.

### Example

    // Combine the 'firstName', " ", and 'lastName' fields into a single string
    field("firstName").stringConcat(constant(" "), field("lastName"));

## Expression.stringContains()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if a string contains a specified substring.

**Signature:**

    stringContains(substring: string): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| substring | string | The substring to search for. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `Expression` representing the 'contains' comparison.

### Example

    // Check if the 'description' field contains "example".
    field("description").stringContains("example");

## Expression.stringContains()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that checks if a string contains the string represented by another expression.

**Signature:**

    stringContains(expr: Expression): BooleanExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| expr | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression representing the substring to search for. |

**Returns:**

[BooleanExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.booleanexpression.md#booleanexpression_class)

A new `Expression` representing the 'contains' comparison.

### Example

    // Check if the 'description' field contains the value of the 'keyword' field.
    field("description").stringContains(field("keyword"));

## Expression.stringIndexOf()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that finds the index of the first occurrence of a substring or byte sequence.

**Signature:**

    stringIndexOf(search: string | Expression | Bytes): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| search | string \| [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| [Bytes](https://firebase.google.com/docs/reference/js/firestore_.bytes.md#bytes_class) | The substring or byte sequence to search for. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the index of the first occurrence.

### Example

    // Find the index of "foo" in the 'text' field
    field("text").stringIndexOf("foo");

## Expression.stringRepeat()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that repeats a string or byte array a specified number of times.

**Signature:**

    stringRepeat(repetitions: number | Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| repetitions | number \| [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The number of times to repeat the string or byte array. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the repeated string or byte array.

### Example

    // Repeat the 'label' field 3 times
    field("label").stringRepeat(3);

## Expression.stringReplaceAll()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that replaces all occurrences of a substring or byte sequence with a replacement.

**Signature:**

    stringReplaceAll(find: string | Expression | Bytes, replacement: string | Expression | Bytes): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| find | string \| [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| [Bytes](https://firebase.google.com/docs/reference/js/firestore_.bytes.md#bytes_class) | The substring or byte sequence to search for. |
| replacement | string \| [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| [Bytes](https://firebase.google.com/docs/reference/js/firestore_.bytes.md#bytes_class) | The replacement string or byte sequence. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the string or byte array with replacements.

### Example

    // Replace all occurrences of "foo" with "bar" in the 'text' field
    field("text").stringReplaceAll("foo", "bar");

## Expression.stringReplaceOne()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that replaces the first occurrence of a substring or byte sequence with a replacement.

**Signature:**

    stringReplaceOne(find: string | Expression | Bytes, replacement: string | Expression | Bytes): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| find | string \| [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| [Bytes](https://firebase.google.com/docs/reference/js/firestore_.bytes.md#bytes_class) | The substring or byte sequence to search for. |
| replacement | string \| [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| [Bytes](https://firebase.google.com/docs/reference/js/firestore_.bytes.md#bytes_class) | The replacement string or byte sequence. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the string or byte array with the replacement.

### Example

    // Replace the first occurrence of "foo" with "bar" in the 'text' field
    field("text").stringReplaceOne("foo", "bar");

## Expression.stringReverse()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that reverses a string.

**Signature:**

    stringReverse(): FunctionExpression;

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the reversed string.

### Example

    // Reverse the value of the 'myString' field.
    field("myString").stringReverse();

## Expression.substring()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns a substring of the results of this expression.

**Signature:**

    substring(position: number, length?: number): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| position | number | Index of the first character of the substring. |
| length | number | Length of the substring. If not provided, the substring will end at the end of the input. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

## Expression.substring()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns a substring of the results of this expression.

**Signature:**

    substring(position: Expression, length?: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| position | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | An expression returning the index of the first character of the substring. |
| length | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | An expression returning the length of the substring. If not provided the substring will end at the end of the input. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

## Expression.subtract()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that subtracts another expression from this expression.

**Signature:**

    subtract(subtrahend: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| subtrahend | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression to subtract from this expression. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the subtraction operation.

### Example

    // Subtract the 'discount' field from the 'price' field
    field("price").subtract(field("discount"));

## Expression.subtract()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that subtracts a constant value from this expression.

**Signature:**

    subtract(subtrahend: number): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| subtrahend | number | The constant value to subtract. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the subtraction operation.

### Example

    // Subtract 20 from the value of the 'total' field
    field("total").subtract(20);

## Expression.sum()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an aggregation that calculates the sum of a numeric field across multiple stage inputs.

**Signature:**

    sum(): AggregateFunction;

**Returns:**

[AggregateFunction](https://firebase.google.com/docs/reference/js/firestore_pipelines.aggregatefunction.md#aggregatefunction_class)

A new `AggregateFunction` representing the 'sum' aggregation.

### Example

    // Calculate the total revenue from a set of orders
    field("orderAmount").sum().as("totalRevenue");

## Expression.timestampAdd()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that adds a specified amount of time to this timestamp expression.

**Signature:**

    timestampAdd(unit: Expression, amount: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| unit | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression evaluates to unit of time, must be one of 'microsecond', 'millisecond', 'second', 'minute', 'hour', 'day'. |
| amount | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression evaluates to amount of the unit. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the resulting timestamp.

### Example

    // Add some duration determined by field 'unit' and 'amount' to the 'timestamp' field.
    field("timestamp").timestampAdd(field("unit"), field("amount"));

## Expression.timestampAdd()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that adds a specified amount of time to this timestamp expression.

**Signature:**

    timestampAdd(unit: 'microsecond' | 'millisecond' | 'second' | 'minute' | 'hour' | 'day', amount: number): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| unit | 'microsecond' \| 'millisecond' \| 'second' \| 'minute' \| 'hour' \| 'day' | The unit of time to add (e.g., "day", "hour"). |
| amount | number | The amount of time to add. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the resulting timestamp.

### Example

    // Add 1 day to the 'timestamp' field.
    field("timestamp").timestampAdd("day", 1);

## Expression.timestampSubtract()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that subtracts a specified amount of time from this timestamp expression.

**Signature:**

    timestampSubtract(unit: Expression, amount: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| unit | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression evaluates to unit of time, must be one of 'microsecond', 'millisecond', 'second', 'minute', 'hour', 'day'. |
| amount | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The expression evaluates to amount of the unit. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the resulting timestamp.

### Example

    // Subtract some duration determined by field 'unit' and 'amount' from the 'timestamp' field.
    field("timestamp").timestampSubtract(field("unit"), field("amount"));

## Expression.timestampSubtract()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that subtracts a specified amount of time from this timestamp expression.

**Signature:**

    timestampSubtract(unit: 'microsecond' | 'millisecond' | 'second' | 'minute' | 'hour' | 'day', amount: number): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| unit | 'microsecond' \| 'millisecond' \| 'second' \| 'minute' \| 'hour' \| 'day' | The unit of time to subtract (e.g., "day", "hour"). |
| amount | number | The amount of time to subtract. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the resulting timestamp.

### Example

    // Subtract 1 day from the 'timestamp' field.
    field("timestamp").timestampSubtract("day", 1);

## Expression.timestampToUnixMicros()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that converts this timestamp expression to the number of microseconds since the Unix epoch (1970-01-01 00:00:00 UTC).

**Signature:**

    timestampToUnixMicros(): FunctionExpression;

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the number of microseconds since epoch.

### Example

    // Convert the 'timestamp' field to microseconds since epoch.
    field("timestamp").timestampToUnixMicros();

## Expression.timestampToUnixMillis()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that converts this timestamp expression to the number of milliseconds since the Unix epoch (1970-01-01 00:00:00 UTC).

**Signature:**

    timestampToUnixMillis(): FunctionExpression;

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the number of milliseconds since epoch.

### Example

    // Convert the 'timestamp' field to milliseconds since epoch.
    field("timestamp").timestampToUnixMillis();

## Expression.timestampToUnixSeconds()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that converts this timestamp expression to the number of seconds since the Unix epoch (1970-01-01 00:00:00 UTC).

**Signature:**

    timestampToUnixSeconds(): FunctionExpression;

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the number of seconds since epoch.

### Example

    // Convert the 'timestamp' field to seconds since epoch.
    field("timestamp").timestampToUnixSeconds();

## Expression.timestampTruncate()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that truncates a timestamp to a specified granularity.

**Signature:**

    timestampTruncate(granularity: TimeGranularity, timezone?: string | Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| granularity | [TimeGranularity](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#timegranularity) | The granularity to truncate to. |
| timezone | string \| [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The timezone to use for truncation. Valid values are from the TZ database (e.g., "America/Los_Angeles") or in the format "Etc/GMT-1". |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the truncated timestamp.

### Example

    // Truncate the 'createdAt' timestamp to the beginning of the day.
    field('createdAt').timestampTruncate('day')

## Expression.timestampTruncate()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that truncates a timestamp to a specified granularity.

**Signature:**

    timestampTruncate(granularity: Expression, timezone?: string | Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| granularity | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The granularity to truncate to. |
| timezone | string \| [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | The timezone to use for truncation. Valid values are from the TZ database (e.g., "America/Los_Angeles") or in the format "Etc/GMT-1". |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the truncated timestamp.

### Example

    // Truncate the 'createdAt' timestamp to the granularity specified in the field 'granularity'.
    field('createdAt').timestampTruncate(field('granularity'))

## Expression.toLower()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that converts a string to lowercase.

**Signature:**

    toLower(): FunctionExpression;

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the lowercase string.

### Example

    // Convert the 'name' field to lowercase
    field("name").toLower();

## Expression.toUpper()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that converts a string to uppercase.

**Signature:**

    toUpper(): FunctionExpression;

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the uppercase string.

### Example

    // Convert the 'title' field to uppercase
    field("title").toUpper();

## Expression.trim()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that removes leading and trailing characters from a string or byte array.

**Signature:**

    trim(valueToTrim?: string | Expression | Bytes): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| valueToTrim | string \| [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) \| [Bytes](https://firebase.google.com/docs/reference/js/firestore_.bytes.md#bytes_class) | Optional This parameter is treated as a set of characters or bytes that will be trimmed from the input. If not specified, then whitespace will be trimmed. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the trimmed string or byte array.

### Example

    // Trim whitespace from the 'userInput' field
    field("userInput").trim();

    // Trim quotes from the 'userInput' field
    field("userInput").trim('"');

## Expression.trunc()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that truncates the numeric value to an integer.

**Signature:**

    trunc(): FunctionExpression;

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the truncated value.

### Example

    // Truncate the 'rating' field
    field("rating").trunc();

## Expression.trunc()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that truncates a numeric value to the specified number of decimal places.

**Signature:**

    trunc(decimalPlaces: number): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| decimalPlaces | number | A constant specifying the truncation precision in decimal places. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the truncated value.

### Example

    // Truncate the value of the 'rating' field to two decimal places.
    field("rating").trunc(2);

## Expression.trunc()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that truncates a numeric value to the specified number of decimal places.

**Signature:**

    trunc(decimalPlaces: Expression): FunctionExpression;

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| decimalPlaces | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | An expression specifying the truncation precision in decimal places. |

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the truncated value.

### Example

    // Truncate the value of the 'rating' field to two decimal places.
    field("rating").trunc(constant(2));

## Expression.type()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that returns the data type of this expression's result, as a string.

This is evaluated on the backend. This means: 1. Generic typed elements (like `array<string>`) evaluate strictly to the primitive `'array'`. 2. Any custom `FirestoreDataConverter` mappings are ignored. 3. For numeric values, the backend does not yield the JavaScript `"number"` type; it evaluates precisely as `"int64"` or `"float64"`. 4. For date or timestamp objects, the backend evaluates to `"timestamp"`.

**Signature:**

    type(): FunctionExpression;

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new `Expression` representing the data type.

### Example

    // Get the data type of the value in field 'title'
    field('title').type()

## Expression.unixMicrosToTimestamp()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that interprets this expression as the number of microseconds since the Unix epoch (1970-01-01 00:00:00 UTC) and returns a timestamp.

**Signature:**

    unixMicrosToTimestamp(): FunctionExpression;

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the timestamp.

### Example

    // Interpret the 'microseconds' field as microseconds since epoch.
    field("microseconds").unixMicrosToTimestamp();

## Expression.unixMillisToTimestamp()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that interprets this expression as the number of milliseconds since the Unix epoch (1970-01-01 00:00:00 UTC) and returns a timestamp.

**Signature:**

    unixMillisToTimestamp(): FunctionExpression;

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the timestamp.

### Example

    // Interpret the 'milliseconds' field as milliseconds since epoch.
    field("milliseconds").unixMillisToTimestamp();

## Expression.unixSecondsToTimestamp()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that interprets this expression as the number of seconds since the Unix epoch (1970-01-01 00:00:00 UTC) and returns a timestamp.

**Signature:**

    unixSecondsToTimestamp(): FunctionExpression;

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the timestamp.

### Example

    // Interpret the 'seconds' field as seconds since epoch.
    field("seconds").unixSecondsToTimestamp();

## Expression.vectorLength()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Creates an expression that calculates the length (number of dimensions) of this Firestore Vector expression.

**Signature:**

    vectorLength(): FunctionExpression;

**Returns:**

[FunctionExpression](https://firebase.google.com/docs/reference/js/firestore_pipelines.functionexpression.md#functionexpression_class)

A new [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) representing the length of the vector.

### Example

    // Get the vector length (dimension) of the field 'embedding'.
    field("embedding").vectorLength();