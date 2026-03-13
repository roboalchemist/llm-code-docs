# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/data/Wbs.md

# [Wbs](https://bryntum.com/docs/gantt/api/Core/data/Wbs)

Wbs constructor.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[value](https://bryntum.com/docs/gantt/api/Core/data/Wbs#property-value)
The WBS value

## Functions

Functions are methods available for calling on the class

[from](https://bryntum.com/docs/gantt/api/Core/data/Wbs#function-from-static)
Returns a `Wbs` instance given a `value`. If the `value` is already a `Wbs` object, it is returned. Otherwise, a new `Wbs` is created. If `value` is `null` or `undefined`, that value is returned.

[pad](https://bryntum.com/docs/gantt/api/Core/data/Wbs#function-pad-static)
Returns a WBS code where each component is 0-padded on the left to 6 digits. That is "1.2" is padded to be "000001.000002". These values can be compared for proper semantic order (e.g., Wbs.pad('1.2') < Wbs.pad('1.10')).

[split](https://bryntum.com/docs/gantt/api/Core/data/Wbs#function-split-static)
Returns an array of digits from a given WBS code `value`. If the value cannot be converted, an empty array is returned.

[compare](https://bryntum.com/docs/gantt/api/Core/data/Wbs#function-compare-static)
Compares two WBS values, returning 0 if equal, -1 if `lhs` is less than `rhs, or 1 if` lhs`is greater than`rhs\`.

[append](https://bryntum.com/docs/gantt/api/Core/data/Wbs#function-append)
Appends a sub-level WBS value to this WBS code and returns a `Wbs` instance for it.

[isEqual](https://bryntum.com/docs/gantt/api/Core/data/Wbs#function-isEqual)
Returns truthy value if this Wbs equals the passed value.

[match](https://bryntum.com/docs/gantt/api/Core/data/Wbs#function-match)
Compares this WBS value with a specified pattern, returning `true` if they match. If the `pattern` is simply a sequence of digits and decimal points (e.g., "1.2"), it is a match if it is a substring of this WBS code (e.g., "3.1.2.4"). If the `pattern` starts with `*` (e.g., "\*.1.2"), it is a match if this WBS code ends with the text following the `*` (e.g., "4.3.1.2"). If the `pattern` ends with `*`, it is a match if this WBS code starts with the text up to the `*`.

Some examples:

```
 console.log(Wbs.from('1.2.3.4').match('2.3'));
 > true
 console.log(Wbs.from('1.2.3.4').match('*.4'));
 > true
 console.log(Wbs.from('1.2.3.4').match('1.2.*'));
 > true

 console.log(Wbs.from('1.2.3.4').match('2.4'));
 > false
 console.log(Wbs.from('1.2.3.4').match('*.3'));
 > false
 console.log(Wbs.from('1.2.3.4').match('2.*'));
 > false
```
