# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/data/ComboModel.md

# [ComboModel](https://bryntum.com/docs/gantt/api/Core/data/ComboModel)

Combo model class, which can be used as `record` type for [listItemTpl](https://bryntum.com/docs/gantt/api/#Core/widget/Combo#config-listItemTpl) and [displayValueRenderer](https://bryntum.com/docs/gantt/api/#Core/widget/Combo#config-displayValueRenderer) configs in TypeScript applications.

Use when Combo's [displayField](https://bryntum.com/docs/gantt/api/#Core/widget/Combo#config-displayField) equals `text` and [items](https://bryntum.com/docs/gantt/api/#Core/widget/Combo#config-items) are configured with one of the value formats listed below:

```
items : [
    {value : 'small', text : 'Small'},
    {value : 'medium', text : 'Medium'},
    {value : 'large', text : 'Large'},
]
```

or

```
items : [
    ['small', 'Small'],
    ['medium', 'Medium'],
    ['large', 'Large'],
]
```

or

```
    items : ['Small', 'Medium', 'Large']
```

Class provides the [value](https://bryntum.com/docs/gantt/api/#Core/data/ComboModel#field-value) and [text](https://bryntum.com/docs/gantt/api/#Core/data/ComboModel#field-text) data fields for the Combo's list record.

## Fields

Fields belong to a Model class and define the Model data structure

[value](https://bryntum.com/docs/gantt/api/Core/data/ComboModel#field-value)
Value for the Combo's list record.

[text](https://bryntum.com/docs/gantt/api/Core/data/ComboModel#field-text)
Display text for the Combo's list record.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isComboModel](https://bryntum.com/docs/gantt/api/Core/data/ComboModel#property-isComboModel)
Identifies an object as an instance of [ComboModel](https://bryntum.com/docs/gantt/api/#Core/data/ComboModel) class, or subclass thereof.

[isComboModel](https://bryntum.com/docs/gantt/api/Core/data/ComboModel#property-isComboModel-static)
Identifies an object as an instance of [ComboModel](https://bryntum.com/docs/gantt/api/#Core/data/ComboModel) class, or subclass thereof.
