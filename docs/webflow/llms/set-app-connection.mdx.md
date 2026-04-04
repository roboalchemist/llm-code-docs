# Source: https://developers.webflow.com/designer/reference/set-app-connection.mdx

***

title: Set App Connection
slug: designer/reference/set-app-connection
description: Create a connection between an element and an App
hidden: true
'og:title': Set App Connection
'og:description': Create a connection between an element and an App
-------------------------------------------------------------------

## `element.setAppConnection()`

Enables the connection between an element and an App.

<Note title="Supported Elements">
  App Connections supports the following elements: `Image`, `FormForm`, and
  `FormWrapper`.
</Note>

### Syntax

```typescript
element.setAppConnection(value: string): Promise<null>
```

### Parameters

* **value**: *string* - An identifier for specific element-App connection.

### Returns

**Promise\<`null`>**

A Promise that resolves to `null`.

### Example

```typescript
const el = await webflow.getRootElement(); // Get Root Element

// Check for an element
if (!el || !el.children) throw new Error("Expected an element");

// Append a form element to the root element
const formEl = await el.append(webflow.elementPresets.FormForm);

// Check for App Connection support
if (!formEl || !formEl.appConnections) {
  throw new Error("App Connections not supported");
}

// Set App Connection
await formEl.setAppConnection("myAwesomeAppManageFormElement");
```

<div>
  <a href="https://webflow.com/oauth/authorize?response_type=code&client_id=19511de1ec410f9228d8dcbc9420e67916dea80d86d18f0c9a533eb475ea0f62">
    Try this example
  </a>
</div>

### Designer Ability

| Designer Ability    | Locale | Branch | Workflow | Sitemode |
| :------------------ | :----- | :----- | :------- | :------- |
| **canAccessCanvas** | Any    | Any    | Any      | Any      |
