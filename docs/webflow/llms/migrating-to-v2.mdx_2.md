# Source: https://developers.webflow.com/designer/reference/migrating-to-v2.mdx

***

title: Migrating to v2
slug: designer/reference/migrating-to-v2
description: ''
hidden: false
'og:title': Migrating to v2 of the Webflow Designer API
'og:description': Migrate to the latest version of the Webflow Designer API
---------------------------------------------------------------------------

We're excited to introduce the new version of Webflow's Designer APIs, featuring enhanced functionality and more efficient methods for interacting with the Designer. To ensure your app remains compatible, please follow the simple steps provided for updating your app's configuration and codebase. [Check the details below.](#app-configuration-updates)

## Notable Changes

### Simplified edit semantics

We have removed the `.save()` method from many of our objects.  Rather than staging “local changes” and explicitly synchronizing via `element.save()`, we’re now making changes as they’re invoked.

### Accessing native Elements

Through the introduction of the [Element Presets Object](/designer/reference/element-presets), the API now allows Apps to insert [native Elements](https://university.webflow.com/lesson/add-elements-panel?topics=elements) onto the canvas.

### Inserting Elements

We’re **introducing** new helper methods that make it easier to insert elements into a hierarchy

* `element.append() `
* `element.prepend() `
* `element.before()`
* `element.after()`

We've **removed** element-specific methods for adding an element to a canvas including

* `createDOM()`
* `createString()`
* `createHeading()`

### Direct editing of Components

This API allows a more streamlined way to edit Component Objects, by[ accessing the root element of a Component Object.](/designer/reference/get-root-element)

### Clear and consistent naming

We've made minor changes to clarify Designer API functionality

* *“Folders” → “PageFolders”* to disambiguate versus other Page resources (e.g. Asset pages)
* *“og-” -> “openGraph-”* prefix for Open Graph Page Fields

### Clear and consistent return objects

* Most methods that aren't meant to return a value now return a Promise that resolves to `null`  instead of `undefined`
* Element IDs are now identified by their component and element ids, e.g. `id: {component: '63486e4622e33733b9002e9c', element: 'cafe0045-d304-79d9-8f68-af3adaed06e8'}`

***

## App configuration Updates

1. Install the latest version of the Webflow CLI
2. Install the latest type definitions for the Designer APIs

```bash
npm i @webflow/designer-extension-typings@0.2.0-beta.3
```

3. Update `webflow.json` to include the new `apiVersion` parameter.

```json webflow.json
{
  "name": "My Webflow App",
  "publicDir": "dist",
  "apiVersion": "2"
}
```

4. Start your development server.

***

## Code Adjustments

Remove any references to `.save()`

```typescript
// v1
await myElement.setStyles([styles])
await myElement.save()

// v2
await myElement.setStyles([styles])
```

Adjust logic to access Element IDs

```typescript
// v1
const selectedElement = await webflow.getSelectedElement()
console.log(selectedElement)
// Prints: 'cafe0045-d304-79d9-8f68-af3adaed06e8'

// v2
const selectedElement = await webflow.getSelectedElement()
console.log(selectedElement)
// Prints id: {component: '63486e4622e33733b9002e9c', element: 'cafe0045-d304-79d9-8f68-af3adaed06e8'}\`

const elementID = selectedElement?.id.element
// Returns: 'cafe0045-d304-79d9-8f68-af3adaed06e8'
```

Adjust logic for element insertion

```typescript
// v1
const newDiv = await webflow.createDOM('div')

// v2
const selectedElement = await webflow.getSelectedElement()
const newDiv = await selectedElement?.before(webflow.elementPresets.DivBlock)
```
