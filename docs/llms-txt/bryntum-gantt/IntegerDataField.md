# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/data/field/IntegerDataField.md

# [IntegerDataField](https://bryntum.com/docs/gantt/api/Core/data/field/IntegerDataField)

This field class handles field of type `Number` with no decimal digits.

```
class Person extends Model {
    static get fields() {
        return [
            'name',
            { name : 'age', type : 'int' }
        ];
    }
}
```

When a field is declared as a `'int'`, non-null values are promoted to `Number` type and decimals are removed using a specified `rounding`. This field type can be useful if a field value is received as a string but should be stored as a number or has a fractional component that must be rounded or truncated.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[nullValue](https://bryntum.com/docs/gantt/api/Core/data/field/IntegerDataField#config-nullValue)
The value to replace `null` when the field is not `nullable`.

[rounding](https://bryntum.com/docs/gantt/api/Core/data/field/IntegerDataField#config-rounding)
The `Math` method to use to ensure fractional component is removed.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isIntegerDataField](https://bryntum.com/docs/gantt/api/Core/data/field/IntegerDataField#property-isIntegerDataField)
Identifies an object as an instance of [IntegerDataField](https://bryntum.com/docs/gantt/api/#Core/data/field/IntegerDataField) class, or subclass thereof.

[isIntegerDataField](https://bryntum.com/docs/gantt/api/Core/data/field/IntegerDataField#property-isIntegerDataField-static)
Identifies an object as an instance of [IntegerDataField](https://bryntum.com/docs/gantt/api/#Core/data/field/IntegerDataField) class, or subclass thereof.
