# Source: https://clerc.so1ve.dev/reference/api/advanced-types.md

---

url: /reference/api/advanced-types.md
---

# @clerc/advanced-types

## Classes

[FlagValidationError](Class.FlagValidationError.md)

‐

## Functions

[Enum](Function.Enum.md)

Creates a Enum type function that validates the input against allowed values.
The display name will be formatted as "value1 | value2 | ..." for help
output.

**Example**

```typescript twoslash
// @include: imports
const format = Enum(["json", "yaml", "xml"]);
// Help output will show: json | yaml | xml
```

**Throws**

If the value is not in the allowed values list

[Range](Function.Range.md)

Creates a range type function that validates the input is a number within the
specified range.

**Throws**

If the value is not a number or is outside the specified
range

[Regex](Function.Regex.md)

Creates a regex type function that validates the input against the provided
pattern.

**Throws**

If the value does not match the regex pattern
