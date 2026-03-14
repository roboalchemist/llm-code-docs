# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/data/field/BooleanDataField.md

# [BooleanDataField](https://bryntum.com/docs/gantt/api/Core/data/field/BooleanDataField)

This field class handles field of type `Boolean`.

```
class Person extends Model {
    static get fields() {
        return [
            'name',
            { name : 'active', type : 'boolean' }
        ];
    }
}
```

When a field is declared as a `'boolean'`, non-null values are promoted to `Boolean` type. This is seldom required, but can be useful if a field value is received as a number but should be treated as a boolean.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[nullValue](https://bryntum.com/docs/gantt/api/Core/data/field/BooleanDataField#config-nullValue)
The value to replace `null` when the field is not `nullable`. To automatically convert `null` or `undefined` to `false`, set [nullable](https://bryntum.com/docs/gantt/api/#Core/data/field/BooleanDataField#config-nullable) to `false`.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isBooleanDataField](https://bryntum.com/docs/gantt/api/Core/data/field/BooleanDataField#property-isBooleanDataField)
Identifies an object as an instance of [BooleanDataField](https://bryntum.com/docs/gantt/api/#Core/data/field/BooleanDataField) class, or subclass thereof.

[isBooleanDataField](https://bryntum.com/docs/gantt/api/Core/data/field/BooleanDataField#property-isBooleanDataField-static)
Identifies an object as an instance of [BooleanDataField](https://bryntum.com/docs/gantt/api/#Core/data/field/BooleanDataField) class, or subclass thereof.
