# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/data/field/StringDataField.md

# [StringDataField](https://bryntum.com/docs/gantt/api/Core/data/field/StringDataField)

This field class handles field of type `String`.

```
class Person extends Model {
    static get fields() {
        return [
            { name : 'name', type : 'string' }
        ];
    }
}
```

When a field is declared as a `'string'`, non-null values are promoted to `String` type. This is seldom required, but can be useful if a field value is received as a number but should be treated as a string.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[nullValue](https://bryntum.com/docs/gantt/api/Core/data/field/StringDataField#config-nullValue)
The value to replace `null` when the field is not `nullable`.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isStringDataField](https://bryntum.com/docs/gantt/api/Core/data/field/StringDataField#property-isStringDataField)
Identifies an object as an instance of [StringDataField](https://bryntum.com/docs/gantt/api/#Core/data/field/StringDataField) class, or subclass thereof.

[isStringDataField](https://bryntum.com/docs/gantt/api/Core/data/field/StringDataField#property-isStringDataField-static)
Identifies an object as an instance of [StringDataField](https://bryntum.com/docs/gantt/api/#Core/data/field/StringDataField) class, or subclass thereof.
