# Source: https://developers.webflow.com/designer/reference/get-users-designer-capabilities.mdx

***

title: Get user's Designer capabilities
slug: designer/reference/get-users-designer-capabilities
description: ''
hidden: false
'og:title': Get Designer capabilities
'og:description': Determine if the user has a specified list of App abilities.
------------------------------------------------------------------------------

## `webflow.canForAppMode()`

Determine if the user has a specified list of App abilities.

<Note title="What are App Modes?">
  Designer Extensions enhance user functionality while adhering to the Designer's current mode. Each method within the Designer API provides specific capabilities, aligning with actions available in each mode. For more context on this API, see the [App Modes](https://developers.webflow.com/designer/reference/app-modes) docs.
</Note>

### Querying User Capabilities by Designer Mode

Use this API to proactively query a user’s capabilities based on the Designer mode they are in, to see if they can use a certain feature of your App. There are a number of scenarios when you may use this method, including, but not limited to:

#### Scenarios

1. **On App Launch:**
   Determine the appropriate UI to display to the user based on the mode they are in.<br />
   ***Example:*** If your App’s core functionality requires the user to be in the “Editing” role, you can either show UI prompting them to switch to the “Designer” role or notify them that the App can only function in a “Designer” role.<br /><br />
2. **Dynamic UI/UX Adjustments**
   Adjust the App’s UI/UX dynamically to match the user's current capabilities.<br />
   ***Example:*** If your App can only show a subset of the UI/features based on the user's current mode, you can alter the App UI/UX to cater to their current capabilities.<br /><br />
3. **User Actions**
   Surface error notifications if a user attempts an action beyond their current capabilities.<br />
   ***Example:*** If a user starts your App in Design mode but switches to Editing mode mid-session and attempts to insert new elements, use `canForAppMode()` to check their capabilities before proceeding. This allows you to notify them that the action cannot be performed in the current mode.<br /><br />

### Syntax

```typescript
webflow.canForAppMode(appModes: Array<AppMode>): Promise<{[key in AppMode]: boolean}>
```

### Parameters

* **appModes:** `Array<AppMode>`
  A list of AppMode enums to request and see if the user has these abilities. You can find the list here:<br />

  ```json
  {
    "canAccessCanvas": "canAccessCanvas",
    "canManageAssets": "canManageAssets",
    "canAccessAssets": "canAccessAssets",
    "canDesign": "canDesign",
    "canEdit": "canEdit",
    "canCreateComponents": "canCreateComponents",
    "canModifyComponents": "canModifyComponents",
    "canCreateStyles": "canCreateStyles",
    "canModifyStyles": "canModifyStyles",
    "canCreatePage": "canCreatePage",
    "canReadPageSettings": "canReadPageSettings",
    "canManagePageSettings": "canManagePageSettings",
    "canReadVariables": "canReadVariables",
    "canModifyVariables": "canModifyVariables",
    "canModifyImageElement": "canModifyImageElement"
  }
  ```

  These AppMode strings can be accessed via `webflow.appModes` (e.g., `webflow.appModes.canDesign`).

<br />

### Returns

**Promise\<*\{\[key in AppMode]}: boolean*>**

A Promise that resolves to a record containing the ability being requested, which maps to whether or not the user has that ability.

### Example

```typescript
const capabilities  = await webflow.canForAppMode([
  webflow.appModes.canEdit,
  webflow.appModes.canDesign
]);

// User in "Editing" mode
// {capabilities.canEdit: true, capabilities.canDesign: false }
```

<div>
  <a href="https://webflow.com/oauth/authorize?response_type=code&client_id=19511de1ec410f9228d8dcbc9420e67916dea80d86d18f0c9a533eb475ea0f62">
    Try this example
  </a>
</div>

### Example: Checking and Executing Based on Capabilities

Let's build a function that checks if the app can perform the action of inserting an element. If yes, then perform the function; if not, trigger a notification.

```typescript
async function insertElementIfAllowed() {
  const capabilities = await webflow.canForAppMode([
    webflow.appModes.canDesign,
    webflow.appModes.canEdit
  ]);

  if (capabilities.canDesign) {
    try {
      // Get Selected Element
      const selectedElement = await webflow.getSelectedElement();

      if (selectedElement) {
        // Insert DIV before selected Element
        const newDiv = await selectedElement.before(webflow.elementPresets.DivBlock);

        // Print element details
        console.log(`Element inserted: ${JSON.stringify(newDiv)}`);
        // Notify success
        await webflow.notify({ type: 'Success', message: 'Element inserted successfully!' });
      } else {
        // Notify error: No selected element
        await webflow.notify({ type: 'Error', message: 'No element selected!' });
      }
    } catch (error) {
      // Notify error
      await webflow.notify({ type: 'Error', message: 'Failed to insert element!' });
      console.error(error);
    }
  } else {
    // Notify error: User does not have the required capabilities
    await webflow.notify({ type: 'Error', message: 'You do not have the required permissions to insert elements!' });
  }
}

// Execute the function
await insertElementIfAllowed();
```

<div>
  <a href="https://webflow.com/oauth/authorize?response_type=code&client_id=19511de1ec410f9228d8dcbc9420e67916dea80d86d18f0c9a533eb475ea0f62">
    Try this example
  </a>
</div>
