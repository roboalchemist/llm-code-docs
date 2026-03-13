# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/data/field/ModelDataField.md

# [ModelDataField](https://bryntum.com/docs/gantt/api/Core/data/field/ModelDataField)

This field class handles fields that hold other records.

```
class Person extends Model {
    static get fields() {
        return [
            'name',
            { name : 'address', type : 'model' }
        ];
    }
}
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[modelClass](https://bryntum.com/docs/gantt/api/Core/data/field/ModelDataField#config-modelClass)
Class used to contain data values in this field; should be a subclass of [Model](https://bryntum.com/docs/gantt/api/#Core/data/Model). Defining this configuration is necessary for some functionality (like filter editing) to identify the type of data held by the field without data present.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isModelDataField](https://bryntum.com/docs/gantt/api/Core/data/field/ModelDataField#property-isModelDataField)
Identifies an object as an instance of [ModelDataField](https://bryntum.com/docs/gantt/api/#Core/data/field/ModelDataField) class, or subclass thereof.

[isModelDataField](https://bryntum.com/docs/gantt/api/Core/data/field/ModelDataField#property-isModelDataField-static)
Identifies an object as an instance of [ModelDataField](https://bryntum.com/docs/gantt/api/#Core/data/field/ModelDataField) class, or subclass thereof.
