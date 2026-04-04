# Source: https://developers.webflow.com/designer/reference/close-extension.mdx

***

title: Close the extension
slug: designer/reference/close-extension
description: Close the Designer Extension using the Webflow object
hidden: false
'og:title': 'Webflow Designer API: Close the extension'
'og:description': Close the Designer Extension using the Webflow object
-----------------------------------------------------------------------

## `webflow.closeExtension()`

Close the Designer Extension using the Webflow object.

### Syntax

```typescript
webflow.closeExtension(): Promise<null>
```

### Returns

**Promise\<`null`>**

A Promise that resolves to `null`.

### Example

This ReactJSexample shows how to close the extension using a button.

```tsx
function CloseExtensionButton() {
    const handleCloseExtension = async () => {
        try {
            await webflow.closeExtension();
            console.log("Extension closed successfully.");
        } catch (error) {
            console.error("Failed to close the extension:", error);
        }
    };

    return (
        <button onClick={handleCloseExtension}>
            Close Extension
        </button>
    );
}
```

<div>
  <a href="https://webflow.com/oauth/authorize?response_type=code&client_id=19511de1ec410f9228d8dcbc9420e67916dea80d86d18f0c9a533eb475ea0f62">
    Try this example
  </a>
</div>
