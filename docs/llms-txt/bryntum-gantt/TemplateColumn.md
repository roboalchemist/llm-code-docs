# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/column/TemplateColumn.md

# [TemplateColumn](https://bryntum.com/docs/gantt/api/Grid/column/TemplateColumn)

A column that uses a template for cell content. Any function can be used as template, and the function is passed { value, record, field } properties. It should return a string which will be rendered in the cell.

Default editor is a [TextField](https://bryntum.com/docs/gantt/api/#Core/widget/TextField).

```
new Grid({
    appendTo : document.body,

    columns : [
        { type: 'template', field: 'age', template: ({value}) => `${value} years old` }
    ]
});
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[template](https://bryntum.com/docs/gantt/api/Grid/column/TemplateColumn#config-template)
Template function used to generate a value displayed in the cell. Called with arguments `{ value, record, field }`

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTemplateColumn](https://bryntum.com/docs/gantt/api/Grid/column/TemplateColumn#property-isTemplateColumn)
Identifies an object as an instance of [TemplateColumn](https://bryntum.com/docs/gantt/api/#Grid/column/TemplateColumn) class, or subclass thereof.

[isTemplateColumn](https://bryntum.com/docs/gantt/api/Grid/column/TemplateColumn#property-isTemplateColumn-static)
Identifies an object as an instance of [TemplateColumn](https://bryntum.com/docs/gantt/api/#Grid/column/TemplateColumn) class, or subclass thereof.

[template](https://bryntum.com/docs/gantt/api/Grid/column/TemplateColumn#property-template)
Template function used to generate a value displayed in the cell. Called with arguments `{ value, record, field }`

## Functions

Functions are methods available for calling on the class

[defaultRenderer](https://bryntum.com/docs/gantt/api/Grid/column/TemplateColumn#function-defaultRenderer)
Renderer that uses a template for cell content.
