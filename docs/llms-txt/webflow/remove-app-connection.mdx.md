# Source: https://developers.webflow.com/designer/reference/remove-app-connection.mdx

***

title: Remove App Connection
slug: designer/reference/remove-app-connection
description: Remove an App Connection from an element
hidden: false
'og:title': Remove App Connection
'og:description': Remove an App Connection from an element
----------------------------------------------------------

## `element.removeAppConnection()`

Remove an App Connection for a specific element. Only App Connections associated with the current App can be removed.

### Syntax

```typescript
removeAppConnection(value: string): Promise<null>
```

### Parameters

* **value**: *String* - The string identifier for the App Connection to be removed.

### Returns

**Promise\<`null`>**

A promise that returns to `null`.

### Example

```typescript
const el = await webflow.getRootElement(); // Get root element

// Check for an element
if (!el || !el.children) throw new Error("Expected an element");

// Create a form element
const formEl = await el.append(webflow.elementPresets.FormForm);

// Check for App Connections
if (!formEl || !formEl.appConnections) {
  throw new Error("App Connections not supported");
}

// Set App Connection
await formEl.setAppConnection("myAwesomeAppManageFormElement");

//  Get existing App Connections
const connections = await formEl.getAppConnections();

// Remove first App Connection
const connection = connections[0];
await removeAppConnection(connection);
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
