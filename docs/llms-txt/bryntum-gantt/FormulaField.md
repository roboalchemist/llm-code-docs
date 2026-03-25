# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/mixin/FormulaField.md

# [FormulaField](https://bryntum.com/docs/gantt/api/Core/widget/mixin/FormulaField)

A mixin to add the [dataField](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/FormulaField#config-dataField) config to [TextField](https://bryntum.com/docs/gantt/api/#Core/widget/TextField).

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[dataField](https://bryntum.com/docs/gantt/api/Core/widget/mixin/FormulaField#config-dataField)
A [DataField](https://bryntum.com/docs/gantt/api/#Core/data/field/DataField) which describes a field of a [Model](https://bryntum.com/docs/gantt/api/#Core/data/Model) that we are editing.

This is used to find [formulaProviders](https://bryntum.com/docs/gantt/api/#Core/data/field/DataField#config-formulaProviders) which the field may support.

```
items : {
    formulaField : {
        type      : 'textfield',
        dataField : myStore.modelClass.getFieldDefinition('name')
    }
}
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isFormulaField](https://bryntum.com/docs/gantt/api/Core/widget/mixin/FormulaField#property-isFormulaField)
Identifies an object as an instance of [FormulaField](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/FormulaField) class, or subclass thereof.

[isFormulaField](https://bryntum.com/docs/gantt/api/Core/widget/mixin/FormulaField#property-isFormulaField-static)
Identifies an object as an instance of [FormulaField](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/FormulaField) class, or subclass thereof.

[formulaPrefix](https://bryntum.com/docs/gantt/api/Core/widget/mixin/FormulaField#property-formulaPrefix)
The Formula provider prefix currently being used

[formula](https://bryntum.com/docs/gantt/api/Core/widget/mixin/FormulaField#property-formula)
The formula typed between the parentheses in a `=XXX(...)` expression in the field's value if the `XXX` matches an available [FormulaProvider](https://bryntum.com/docs/gantt/api/#Core/util/FormulaProvider).
