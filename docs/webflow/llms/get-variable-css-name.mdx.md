# Source: https://developers.webflow.com/designer/reference/get-variable-css-name.mdx

***

title: Get CSS name
slug: reference/get-variable-css-name
description: Learn how to get the CSS name of a variable in the Designer.
hidden: false
-------------

## `variable.getCSSName()`

Returns the custom property name of a variable (e.g., `--primary`).

<Note>
  This is distinct from
  [`variable.getBinding()`](/designer/reference/get-variable-binding), which
  returns the variable wrapped in a `var()` function (e.g., `var(--primary)`).
  Use `getCSSName()` when you need a reference to the variable's name, for
  example, to override its value in a custom stylesheet.
</Note>

### Syntax

```typescript
variable.getCSSName(): Promise<string>
```

### Returns

**Promise\<*string*>**

A Promise that resolves to the variable's CSS name.

### Example

```typescript
// Create a variable
const webflowBlue = await collection?.createColorVariable(
  "blue-500",
  "#146EF5"
);

// Get the CSS name for the variable
const cssName = await webflowBlue.getCSSName();
// cssName = "--blue-500"
```

### Designer ability

| Designer Ability     | Locale | Branch | Workflow | Sitemode |
| :------------------- | :----- | :----- | :------- | :------- |
| **canReadVariables** | Any    | Any    | Any      | Any      |
