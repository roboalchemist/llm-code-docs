# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/DisplayField.md

# [DisplayField](https://bryntum.com/docs/gantt/api/Core/widget/DisplayField)

A widget used to show a read only value. Can also use a [template string](https://bryntum.com/docs/gantt/api/#Core/widget/DisplayField#config-template) to show custom markup inside a Container.

```
const displayField = new DisplayField({
  appendTo : document.body,
  label    : 'Name',
  value    : 'John Doe',
  // or use a template
  // template : name => `${name} is the name`
});
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[template](https://bryntum.com/docs/gantt/api/Core/widget/DisplayField#config-template)
A template string used to render the value of this field. Please note you are responsible for encoding any strings protecting against XSS.

```
new DisplayField({
    appendTo : document.body,
    name     : 'age',
    label    : 'Age',
    template : data => `${data.value} years old`
})
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isDisplayField](https://bryntum.com/docs/gantt/api/Core/widget/DisplayField#property-isDisplayField)
Identifies an object as an instance of [DisplayField](https://bryntum.com/docs/gantt/api/#Core/widget/DisplayField) class, or subclass thereof.

[isDisplayField](https://bryntum.com/docs/gantt/api/Core/widget/DisplayField#property-isDisplayField-static)
Identifies an object as an instance of [DisplayField](https://bryntum.com/docs/gantt/api/#Core/widget/DisplayField) class, or subclass thereof.
