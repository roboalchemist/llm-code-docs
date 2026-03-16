# Source: https://www.apollographql.com/docs/graphos/connectors/mapping/methods.md

# Mapping Methods Reference

Check out the [Connectors Mapping Playground](https://www.apollographql.com/docs/graphos/connectors/tooling/mapping-playground) to experiment with and troubleshoot mapping expressions.

This reference documents all available transformation methods in the Connectors mapping language.
You use methods with the `->method` syntax to manipulate strings, objects, arrays, and other data types.
Each method accepts arguments that can be JSON literals (numbers, strings, booleans, arrays, objects, and `null`) or special [variables](https://www.apollographql.com/docs/graphos/connectors/mapping/variables) like `$`, `$args`, `$this`, or `$config`.

See the common mapping patterns pages in the [response mapping docs](https://www.apollographql.com/docs/graphos/connectors/responses) for example snippets of common transformations.

## String methods

Method
Description
Example

`slice`

Returns a slice of a string

`firstTwoChars: countryCode->slice(0, 2)`

`size`

Returns the length of a string

`wordLength: word->size`

## Object methods

Method
Description
Example

`entries`

Returns a list of key-value pairs

`keyValuePairs: object->entries`

`size`

Returns the number of properties in an object

`propCount: object->size`

## Array methods

Method
Description
Example

`filter`

Returns a new array containing all array items that match the criteria outlined in the first argument of `filter`

`evenNumbers: numbers->filter(@->mod(2)->eq(0))`

`find`

Returns the first item in the array that matches the criteria outlined in the first argument of `find`

`firstEven: numbers->find(@->mod(2)->eq(0))`

`first`

Returns the first value in a list

`firstColor: colors->first`

`get`

For a string, returns the character at the specified index. For an array, returns the item at the specified index. For an object, returns the property with the specified name

`thirdItem: items->get(2)`

`userName: user->get("name")`

`joinNotNull`

Concatenates an array of string values using the specified separator and ignoring `null` values

`$(["a", "b", null, "c"])->joinNotNull(',')`

`last`

Returns the last value in a list

`lastColor: colors->last`

`map`

Maps a list of values to a new list, or converts a single item to a list

`colors: colors->map({ name: @ })`

`slice`

Returns a slice of a list

`firstTwoColors: colors->slice(0, 2)`

`size`

Returns the length of a list

`colorCount: colors->size`

## Logical methods

Method
Description
Example

`and`

Given two or more values to compare, returns `true` if all of the values are `true`

`bothTrue: value1->and(value2, value3)`

`contains`

Returns `true` if the array contains the argument

`hasRed: colors->contains("red")`

`eq`

Returns `true` if the value is equal to the argument

`isActive: status->eq("active")`

`gt`

Returns `true` if the value is greater than the argument

`isLarge: size->gt(100)`

`gte`

Returns `true` if the value is greater than or equal to the argument

`isAtLeastTen: count->gte(10)`

`in`

Returns `true` if the list of arguments contains the value

`isValidStatus: status->in("active", "pending", "complete")`

`lt`

Returns `true` if the value is less than the argument

`isSmall: size->lt(50)`

`lte`

Returns `true` if the value is less than or equal to the argument

`isWithinLimit: count->lte(100)`

`ne`

Returns `true` if the value is not equal to the argument

`isNotEmpty: value->ne("")`

`not`

Inverts the boolean of the value. `true` becomes `false`, and `false` becomes `true`

`isInactive: isActive->not`

`or`

Returns `true` if the value or any of the arguments are `true`

`isValidOrDefault: isValid->or(useDefault)`

## Math methods

Method
Description
Example

`add`

Adds the argument to the value

`total: price->add(tax)`

`div`

Divides the value by the argument

`average: sum->div(count)`

`mod`

Divides the value by the argument and returns the remainder

`remainder: number->mod(5)`

`mul`

Multiplies the value by the argument

`area: width->mul(height)`

`sub`

Subtracts the argument from the value

`difference: total->sub(discount)`

## Type coercion

Method
Description
Example

`parseInt`

Converts a value to an `Int`

`count: stringCount->parseInt`

`toString`

Converts an input to a `String`

`id: userId->toString`

## Other methods

Method
Description
Example

`echo`

Evaluates and returns its first argument

`wrappedValue: value->echo({ wrapped: @ })`

`jsonStringify`

Converts a value to a JSON string

`jsonBody: body->jsonStringify`

`match`

Replaces a value with a new value if it matches another value

`status: status->match([1, "one"], [2, "two"], [@, "other"])`
