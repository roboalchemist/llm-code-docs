# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/data/field/DateDataField.md

# [DateDataField](https://bryntum.com/docs/gantt/api/Core/data/field/DateDataField)

This field class handles field of type `Date`.

```
class Person extends Model {
    static get fields() {
        return [
            'name',
            { name : 'birthday', type : 'date', format : 'YYYY-MM-DD' },
            { name : 'age', readOnly : true }
        ];
    }
}
```

When a field is declared as a `'date'`, non-null values are promoted to `Date` type. This is frequently needed due to how date types are serialized to JSON strings.

Date fields can have a special `defaultValue` of `'now'` which will convert to the current date/time.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[format](https://bryntum.com/docs/gantt/api/Core/data/field/DateDataField#config-format)
The format of the date field.

See [DateHelper](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper) for details.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isDateDataField](https://bryntum.com/docs/gantt/api/Core/data/field/DateDataField#property-isDateDataField)
Identifies an object as an instance of [DateDataField](https://bryntum.com/docs/gantt/api/#Core/data/field/DateDataField) class, or subclass thereof.

[isDateDataField](https://bryntum.com/docs/gantt/api/Core/data/field/DateDataField#property-isDateDataField-static)
Identifies an object as an instance of [DateDataField](https://bryntum.com/docs/gantt/api/#Core/data/field/DateDataField) class, or subclass thereof.
