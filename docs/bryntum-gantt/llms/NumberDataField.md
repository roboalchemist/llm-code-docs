# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/data/field/NumberDataField.md

# [NumberDataField](https://bryntum.com/docs/gantt/api/Core/data/field/NumberDataField)

This field class handles field of type `Number`.

```
class Person extends Model {
    static get fields() {
        return [
            'name',
            { name : 'age', type : 'number' }
        ];
    }
}
```

When a field is declared as a `'number'`, non-null values are promoted to `Number` type. This is seldom required, but can be useful if a field value is received as a string but should be treated as a number.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[nullValue](https://bryntum.com/docs/gantt/api/Core/data/field/NumberDataField#config-nullValue)
The value to replace `null` when the field is not `nullable`.

[precision](https://bryntum.com/docs/gantt/api/Core/data/field/NumberDataField#config-precision)
The numeric precision of this field. Values are rounded to the specified number of digits. If `null`, the default, no rounding is performed.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isNumberDataField](https://bryntum.com/docs/gantt/api/Core/data/field/NumberDataField#property-isNumberDataField)
Identifies an object as an instance of [NumberDataField](https://bryntum.com/docs/gantt/api/#Core/data/field/NumberDataField) class, or subclass thereof.

[isNumberDataField](https://bryntum.com/docs/gantt/api/Core/data/field/NumberDataField#property-isNumberDataField-static)
Identifies an object as an instance of [NumberDataField](https://bryntum.com/docs/gantt/api/#Core/data/field/NumberDataField) class, or subclass thereof.
