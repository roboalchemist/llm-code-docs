# Source: https://developers.webflow.com/designer/get-parent-style.mdx

***

title: Get parent style
subtitle: Get the parent style of a combo class style.
slug: get-parent-style
description: >-
Get the parent style of a [combo
class](https://help.webflow.com/hc/en-us/articles/33961311094419-Classes#how-to-create-a-combo-class)
style.
------

## `style.getParent()`

Get the parent style of a class when you've determined that a style is a [combo class](https://help.webflow.com/hc/en-us/articles/33961311094419-Classes#how-to-create-a-combo-class) and you want to:

* **Understand style inheritance** - See which properties the combo class inherits versus overrides
* **Copy base styles** - Apply the parent's properties to other elements
* **Debug styling conflicts** - Trace where specific CSS values originate
* **Build style auditing tools** - Map the relationship between styles in a project

### Syntax

```typescript
style.getParent(): Promise<Style | null>
```

### Returns

**Promise\<Style | null>**

A Promise that resolves to a Style object if a parent exists, or `null` if no parent is found.

### Example

```typescript
// Audit combo class inheritance
if (await style.isComboClass()) {
    const parentStyle = await style.getParent();

    if (parentStyle) {
        const parentProps = await parentStyle.getProperties();
        const comboProps = await style.getProperties();

        console.log('Inherited from parent:', parentProps);
        console.log('Overrides in combo class:', comboProps);
    }
} else {
    console.log('Style is not a combo class - no parent exists');
}
```

<div>
  <a href="https://webflow.com/oauth/authorize?response_type=code&client_id=19511de1ec410f9228d8dcbc9420e67916dea80d86d18f0c9a533eb475ea0f62">
    Try this example
  </a>
</div>

### Designer ability

| Designer Ability    | Locale | Branch | Workflow | Sitemode |
| :------------------ | :----- | :----- | :------- | :------- |
| **canAccessCanvas** | Any    | Any    | Any      | Any      |
