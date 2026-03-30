# Source: https://developers.webflow.com/designer/reference/get-variable-binding.mdx

***

title: Get variable binding
slug: reference/get-variable-binding
description: Get the binding of a variable
hidden: false
'og:title': 'Webflow Designer API: Get variable binding'
'og:description': Get the binding of a variable
-----------------------------------------------

## `variable.getBinding()`

Returns a binding value for the variable. Use the binding value when creating or updating variables with [custom values.](/designer/reference/variables-detail-overview#custom-values)

### Syntax

```typescript
variable.getBinding(): Promise<string>
```

### Returns

**Promise\<*string*>**

A Promise that resolves to a string representing the variable's binding.

### Example

```typescript
// Create a variable
const webflowBlue = await collection?.createColorVariable(
  "blue-500",
  "#146EF5"
);

// Get the binding value for a variable
const binding = await webflowBlue.getBinding();
// binding = "var(--blue-500)"

// Use the binding value to create a variable with a custom value
const webflowBlue400 = await collection.createColorVariable("blue-400", {
  type: "custom",
  value: `color-mix(in srgb, ${binding}, white 50%)`,
});
```

### Designer Ability

| Designer Ability     | Locale | Branch | Workflow | Sitemode |
| :------------------- | :----- | :----- | :------- | :------- |
| **canReadVariables** | Any    | Any    | Any      | Any      |
