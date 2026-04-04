# Source: https://developers.webflow.com/designer/reference/enter-component.mdx

***

title: Enter into a component
slug: designer/reference/enter-component
description: ''
hidden: false
'og:title': 'Webflow Designer API: Enter into a component'
'og:description': Focus the Designer on a component definition in order to make changes.
----------------------------------------------------------------------------------------

## `webflow.enterComponent(instance)`

Focus the Designer on a component definition to [make changes](/designer/reference/components-overview#editing-a-component-definition) to a component definition. When a component is in focus, all supported Designer APIs and methods operate specifically on that component definition, not the entire Site.

### Syntax

```typescript
webflow.enterComponent(
  instance: ComponentElement
): Promise<null>
```

### Parameters

* **instance**: *ComponentElement* -  A Component Instance that's present on the page. If there’s no current instance, you’ll need to create one first.

### Returns

**Promise\<`null`>**

A Promise that resolves to `null` when the context switch is successful.

### Example

```typescript
// Step 1: Fetch the currently selected element
const selectedElement = await webflow.getSelectedElement();

if (selectedElement && selectedElement.type === "ComponentInstance") {

  //  Step 2: Enter the context of the selected ComponentElement
  await webflow.enterComponent(selectedElement as ComponentElement);
  console.log("Successfully entered the component context.");

  // Step 3: After entering the component's context, fetch the root element
  const rootElement = await webflow.getRootElement();
  if (rootElement) {
    console.log("Root element of the component:", rootElement);
  } else {
    console.log("No root element found in this component context.");
  }

} else {
  console.log("The selected element is not a ComponentElement.");
}
```

<div>
  <a href="https://webflow.com/oauth/authorize?response_type=code&client_id=19511de1ec410f9228d8dcbc9420e67916dea80d86d18f0c9a533eb475ea0f62">
    Try this example
  </a>
</div>

***

### Designer Ability

| Designer Ability        | Locale | Branch | Workflow | SiteMode |
| :---------------------- | :----- | :----- | :------- | :------- |
| **canModifyComponents** | any    | any    | canvas   | Design   |
