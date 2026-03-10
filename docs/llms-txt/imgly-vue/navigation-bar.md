# Navigation Bar

This guide explains how to customize the navigation bar in CE.SDK. The navigation bar is the horizontal toolbar at the top of the editor containing buttons for back navigation, undo/redo, zoom controls, and export actions. You’ll learn how to reorder, remove, and add components using the Order API, and configure action button handlers for save and export operations.

![Navigation Bar Hero](/docs/cesdk/_astro/browser.hero.B8tlNHMZ_Z1tldAc.webp)

10 mins

estimated time

Live Demo[

Download](https://github.com/imgly/cesdk-web-examples/archive/refs/heads/main.zip)[

StackBlitz](https://stackblitz.com/~/github.com/imgly/cesdk-web-examples)[

GitHub](https://github.com/imgly/cesdk-web-examples)

Actions that affect browser navigation (e.g. going back or closing the editor), have global effects on the scene (e.g. undo/redo and zoom), or process the scene in some way (e.g. saving and exporting) should be placed in the navigation bar.

## Show or Hide the Navigation[#](#show-or-hide-the-navigation)

`show: boolean` is used to show or hide the complete navigation

`position: string` is used to set the location of the navigation bar to either top or bottom.

```
import CreativeEditorSDK from 'https://cdn.img.ly/packages/imgly/cesdk-js/1.67.0/index.js';
const config = {  // license: 'YOUR_CESDK_LICENSE_KEY',  userId: 'guides-user',  ui: {    elements: {      /* ... */      navigation: {        show: true, // 'false' to hide the navigation completely        position: 'top', // 'top' or 'bottom'        /* ... */      },      panels: {        /* ... */      },      dock: {        /* ... */      },      libraries: {        /* ... */      },      blocks: {        /* ... */      },    },  },};
CreativeEditorSDK.create('#cesdk_container', config).then(async cesdk => {  // Set the editor view mode  cesdk.ui.setView('default');
  // Do something with the instance of CreativeEditor SDK, for example:  // Populate the asset library with default / demo asset sources.  cesdk.addDefaultAssetSources();  cesdk.addDemoAssetSources({    sceneMode: 'Design',    withUploadAssetSources: true,  });  await cesdk.createDesignScene();});
```

## Configure Navigation Buttons[#](#configure-navigation-buttons)

Navigation bar components are configured dynamically using the Navigation Bar Order API. The `insertNavigationBarOrderComponent` method allows you to add or insert components into the navigation bar.

### Adding Action Buttons[#](#adding-action-buttons)

Use the actions dropdown component to add action buttons to the navigation bar:

```
import CreativeEditorSDK from 'https://cdn.img.ly/packages/imgly/cesdk-js/1.67.0/index.js';
const config = {  // license: 'YOUR_CESDK_LICENSE_KEY',  userId: 'guides-user',  ui: {    elements: {      /* ... */      navigation: {        show: true, // 'false' to hide the navigation completely        position: 'top', // 'top' or 'bottom'      },      panels: {        /* ... */      },      dock: {        /* ... */      },      libraries: {        /* ... */      },      blocks: {        /* ... */      },    },  },};
CreativeEditorSDK.create('#cesdk_container', config).then(async cesdk => {  // Configure navigation bar actions after initialization  cesdk.ui.insertNavigationBarOrderComponent('last', {    id: 'ly.img.actions.navigationBar',    children: [      'ly.img.saveScene.navigationBar',      'ly.img.importScene.navigationBar',      'ly.img.exportImage.navigationBar',      'ly.img.exportPDF.navigationBar',      'ly.img.exportScene.navigationBar',    ],  });
  // Add back button at the beginning  cesdk.ui.insertNavigationBarOrderComponent(    'first',    {      id: 'ly.img.back.navigationBar',      onClick: () => {        // Handle back action        window.history.back();      },    },    'before',  );
  // Add close button at the end  cesdk.ui.insertNavigationBarOrderComponent('last', {    id: 'ly.img.close.navigationBar',    onClick: () => {      // Handle close action      window.close();    },  });
  // Populate the asset library with default / demo asset sources.  cesdk.addDefaultAssetSources();  cesdk.addDemoAssetSources({    sceneMode: 'Design',    withUploadAssetSources: true,  });  await cesdk.createDesignScene();});
```

## Custom Call-To-Action Buttons[#](#custom-call-to-action-buttons)

Custom actions are added using the Navigation Bar Order API. Add custom buttons directly to the navigation bar or inside the actions dropdown with full control over their appearance and behavior.

### Button Properties[#](#button-properties)

*   `key` - unique identifier for custom actions (required for `ly.img.action.navigationBar`)
*   `label` - text label, can be an i18n key that will be looked up in the translation table
*   `icon` - icon id from our ‘Essentials’ set ( [see full list here](vue/user-interface/appearance/icons-679e32/) ), or a custom icon id added via `addIconSet`
*   `variant` - button style: `'regular'` (default) or `'plain'` (subtle/borderless)
*   `color` - button color: `'accent'` (primary/highlighted) or `'danger'` (red/warning)
*   `onClick` - callback function with signature `() => void | Promise<void>`. If returning a promise, a spinner shows until it resolves
*   `isDisabled` - boolean to disable the button
*   `isLoading` - boolean to show loading state

### Button Styles[#](#button-styles)

Custom buttons support different visual styles through the `variant` and `color` properties:

```
// Regular variant (default) - standard button appearance{  id: 'ly.img.action.navigationBar',  key: 'share',  label: 'Share',  icon: '@imgly/Share',  variant: 'regular',  onClick: () => { /* ... */ }}
// Accent color - highlighted/primary appearance{  id: 'ly.img.action.navigationBar',  key: 'publish',  label: 'Publish',  icon: '@imgly/Upload',  color: 'accent',  onClick: () => { /* ... */ }}
// Plain variant - subtle/borderless appearance{  id: 'ly.img.action.navigationBar',  key: 'preview',  label: 'Preview',  icon: '@imgly/EyeOpen',  variant: 'plain',  onClick: () => { /* ... */ }}
// Danger color - red/warning appearance for destructive actions{  id: 'ly.img.action.navigationBar',  key: 'reset',  label: 'Reset',  icon: '@imgly/Reset',  color: 'danger',  onClick: () => { /* ... */ }}
```

### Adding Multiple Custom Buttons[#](#adding-multiple-custom-buttons)

You can add custom buttons both as standalone items in the navigation bar and inside the actions dropdown:

```
cesdk.ui.setNavigationBarOrder([  // Back button  {    id: 'ly.img.back.navigationBar',    onClick: () => window.history.back(),  },
  'ly.img.undoRedo.navigationBar',  'ly.img.spacer',  'ly.img.title.navigationBar',  'ly.img.spacer',  'ly.img.zoom.navigationBar',
  // Standalone custom buttons with different styles  {    id: 'ly.img.action.navigationBar',    key: 'share',    label: 'Share',    icon: '@imgly/Share',    variant: 'regular',    onClick: () => {      cesdk.ui.showNotification({ message: 'Sharing...', type: 'info' });    },  },  {    id: 'ly.img.action.navigationBar',    key: 'publish',    label: 'Publish',    icon: '@imgly/Upload',    color: 'accent',    onClick: () => {      cesdk.ui.showNotification({ message: 'Publishing...', type: 'success' });    },  },
  // Actions dropdown with more options  {    id: 'ly.img.actions.navigationBar',    children: [      {        id: 'ly.img.saveScene.navigationBar',        onClick: async () => {          const scene = await cesdk.engine.scene.saveToString();          console.log('Scene saved:', scene.length, 'characters');        },      },      {        id: 'ly.img.exportImage.navigationBar',        onClick: async () => {          const { blobs } = await cesdk.utils.export({ mimeType: 'image/png' });          cesdk.utils.downloadFile(blobs[0], 'image/png');        },      },      {        id: 'ly.img.action.navigationBar',        key: 'print',        label: 'Print',        icon: '@imgly/Print',        onClick: () => window.print(),      },    ],  },]);
```

## Rearrange Components[#](#rearrange-components)

There are 6 APIs for getting, setting, updating, removing, and inserting components in the Navigation Bar.

The content of the Navigation Bar changes based on the current [edit mode](vue/concepts/edit-modes-1f5b6c/) (`'Transform'` (the default), `'Text'`, `'Crop'`, `'Trim'`, or a custom value), so all APIs accept an `orderContext` argument to specify the mode.

For example usage of similar APIs, see also [Moving Existing Buttons](vue/user-interface/customization/rearrange-buttons-97022a/) or [Adding New Buttons](vue/user-interface/ui-extensions/add-new-button-74884d/) in the Guides section.

Note that the Navigation Bar is also configurable using our [UI configuration](vue/user-interface/customization-72b2f8/) .

### Get the Current Order[#](#get-the-current-order)

```
getNavigationBarOrder(  orderContext: OrderContext = { editMode: 'Transform' })
```

When omitting the `orderContext` parameter, the order for the `'Transform'` edit mode is returned, e.g.

```
cesdk.ui.getNavigationBarOrder();// => [// {id: 'ly.img.back.navigationBar'},// {id: 'ly.img.undoRedo.navigationBar'},// ...// ]
```

### Set a new Order[#](#set-a-new-order)

```
setNavigationBarOrder(  navigationBarOrder: (NavigationBarComponentId | OrderComponent)[],  orderContext: OrderContext = { editMode: 'Transform' })
```

When omitting the `orderContext` parameter, the order is set for the default edit mode (`'Transform'`), e.g.:

```
// Sets the order for transform mode by defaultcesdk.ui.setNavigationBarOrder(['my.component.for.transform.mode']);
```

### Update Components[#](#update-components)

```
updateNavigationBarOrderComponent(  matcher: OrderComponentMatcher<OrderComponent<NavigationBarComponentId>>,  update: NavigationBarComponentId | Partial<OrderComponent<NavigationBarComponentId>> | ((component: OrderComponent<NavigationBarComponentId>) => Partial<OrderComponent<NavigationBarComponentId>>),  orderContext?: OrderContext)
```

Updates existing components in the navigation bar. The matcher can be:

*   `'first'` or `'last'` - matches the first or last component
*   A number - matches the component at that index
*   A component ID string
*   A partial object describing the component to match
*   A function that receives the component and index, returning true if it matches

The update can be:

*   A new component ID string
*   A partial object with updated properties
*   A function that receives the current component and returns the updated one

Returns an object with the number of updated components and the updated order array.

```
// Change the save button label and style for a specific contextcesdk.ui.updateNavigationBarOrderComponent(  'ly.img.saveScene.navigationBar',  component => ({    ...component,    label: 'Save Draft',    color: 'accent',  }),);
// Disable export buttons when user doesn't have export permissionscesdk.ui.updateNavigationBarOrderComponent(  { id: 'ly.img.exportImage.navigationBar' },  { isDisabled: true },);
// Replace the default actions with a custom action buttoncesdk.ui.updateNavigationBarOrderComponent(  component => component.id === 'ly.img.actions.navigationBar',  {    id: 'ly.img.customAction.navigationBar',    label: 'Publish',    icon: '@imgly/Share',  },);
```

### Remove Components[#](#remove-components)

```
removeNavigationBarOrderComponent(  matcher: OrderComponentMatcher<OrderComponent<NavigationBarComponentId>>,  orderContext?: OrderContext)
```

Removes components from the navigation bar. The matcher can be:

*   `'first'` or `'last'` - matches the first or last component
*   A number - matches the component at that index
*   A component ID string
*   A partial object describing the component to match
*   A function that receives the component and index, returning true if it matches

Returns an object with the number of removed components and the updated order array.

```
// Remove PDF export option for mobile userscesdk.ui.removeNavigationBarOrderComponent('ly.img.exportPDF.navigationBar');
// Remove all export buttons for users without export permissionscesdk.ui.removeNavigationBarOrderComponent(component =>  component.id.includes('export'),);
// Remove the close button in embedded modecesdk.ui.removeNavigationBarOrderComponent({  id: 'ly.img.close.navigationBar',});
```

### Insert Components[#](#insert-components)

```
insertNavigationBarOrderComponent(  matcher: OrderComponentMatcher<OrderComponent<NavigationBarComponentId>>,  component: NavigationBarComponentId | OrderComponent<NavigationBarComponentId>,  location?: InsertOrderComponentLocation,  orderContext?: OrderContext)
```

Inserts new components into the navigation bar. The matcher can be:

*   `'first'` or `'last'` - matches the first or last component
*   A number - matches the component at that index (e.g., `2`)
*   A component ID string (e.g., `'ly.img.saveScene.navigationBar'`)
*   A partial object describing the component to match (e.g., `{ id: 'ly.img.saveScene.navigationBar' }`)
*   A function that receives the component and index, returning true if it matches

The location can be:

*   `'before'` - Insert before the matched component
*   `'after'` - Insert after the matched component (default)
*   `'replace'` - Replace the matched component

Returns the updated navigation bar order array.

```
// Add actions dropdown at the end of the navigation barcesdk.ui.insertNavigationBarOrderComponent('last', {  id: 'ly.img.actions.navigationBar',  children: [    'ly.img.saveScene.navigationBar',    'ly.img.exportImage.navigationBar',  ],});
// Add a back button at the beginningcesdk.ui.insertNavigationBarOrderComponent(  'first',  {    id: 'ly.img.back.navigationBar',    onClick: () => window.history.back(),  },  'before',);
// Insert a custom button after the save buttoncesdk.ui.insertNavigationBarOrderComponent(  { id: 'ly.img.saveScene.navigationBar' },  {    id: 'ly.img.custom.navigationBar',    label: 'Custom Action',    onClick: () => console.log('Custom action'),  },  'after',);
```

## Navigation Bar Components[#](#navigation-bar-components)

The following lists the default Navigation Bar components available within CE.SDK.

### Available Action Components[#](#available-action-components)

These components can be added to the `ly.img.actions.navigationBar` container:

| Component ID | Description |
| --- | --- |
| `ly.img.saveScene.navigationBar` | Save scene action - saves the current scene |
| `ly.img.importScene.navigationBar` | Load scene action - loads a scene file |
| `ly.img.exportScene.navigationBar` | Download scene action - downloads the current scene |
| `ly.img.exportImage.navigationBar` | Export as image - exports the design as an image file |
| `ly.img.exportPDF.navigationBar` | Export as PDF - exports the design as a PDF file |
| `ly.img.exportVideo.navigationBar` | Export as video - exports the design as a video file |
| `ly.img.exportArchive.navigationBar` | Create archive - creates an archive of the scene |
| `ly.img.importArchive.navigationBar` | Load archive - loads an archive file |
| `ly.img.shareScene.navigationBar` | Share action - custom share functionality |
| `ly.img.action.navigationBar` | Custom action button (requires `key` property) |

### Layout Helpers[#](#layout-helpers)

| Component ID | Description |
| --- | --- |
| `ly.img.separator` | Adds a vertical separator (`<hr>` element) in the Navigation Bar.  
Separators follow some special layouting rules:  
\- If 2 or more separators end up next to each other (e.g. due to other components not rendering), **only 1** separator will be rendered.  
\- Separators that end up being the first or last element in the Inspector Bar will **not** be rendered.  
\- Separators directly adjacent _to the left side_ of a spacer (see below) will **not** be rendered. |
| `ly.img.spacer` | Adds horizontal spacing in the Navigation Bar.  
Spacers will try to fill all available whitespace, by distributing the available space between all spacers found in the Navigation Bar. |

### Common Controls[#](#common-controls)

| Component ID | Description |
| --- | --- |
| `ly.img.title.navigationBar` | Title:  
A section displaying the title of the currently opened scene file.  
  
The title displayed on the UI is set by the `config.ui.elements.navigation.title` parameter. If this parameter is not specified, the system will instead check the component’s payload. To define a payload, rather than adding the ID directly to the order, insert an object structured like this: `{ id: 'ly.img.title.navigationBar', title: 'My Scene' }` |
| `ly.img.back.navigationBar` | Back button:  
A button used to navigate to the previous page. Note that this button is hidden by default, and can be configured using the UI Elements configuration. |
| `ly.img.close.navigationBar` | Close button:  
A button used to close the editor. Note that this button is hidden by default, and can be configured using the UI Elements configuration. |
| `ly.img.undoRedo.navigationBar` | Undo/Redo controls:  
Two buttons for un-doing and re-doing recent changes. |
| `ly.img.pageResize.navigationBar` | Page Resize button:  
A button used to control the page resize panel. |
| `ly.img.zoom.navigationBar` | Zoom controls:  
Two buttons for zooming the view in and out, separated by a third button showing the current zoom level and opening a dropdown offering common zoom operations (Auto-Fit Page, Fit Page, Fit Selection, 200% Zoom, 100% Zoom, 50% Zoom, Zoom In, Zoom Out). |
| `ly.img.preview.navigationBar` | Preview button:  
Toggles Preview mode, which allows viewing and editing the scene like an Adopter would (e.g. with all Placeholder constraints enforced). Changes made in Preview are not saved and will be discarded when leaving Preview. |
| `ly.img.actions.navigationBar` | Call To Action buttons:  
A dropdown container for action buttons. You can customize its children to include any combination of save, export, load, and custom action buttons. The first child appears as a prominent button in the navigation bar, while additional children appear in the dropdown menu. |

## Default Order[#](#default-order)

The default order of the Navigation Bar is the following:

```
[  'ly.img.undoRedo.navigationBar',  'ly.img.pageResize.navigationBar',  'ly.img.spacer',  'ly.img.title.navigationBar',  'ly.img.spacer',  'ly.img.zoom.navigationBar',  'ly.img.preview.navigationBar',];
```

## Integration with Callbacks API[#](#integration-with-callbacks-api)

Action buttons in the navigation bar automatically trigger the corresponding callbacks registered with the Callbacks API when used as string IDs. You can also provide custom onClick handlers to override the default behavior.

### Using Registered Callbacks[#](#using-registered-callbacks)

```
// Register callbacks with the Callbacks APIcesdk.actions.register('saveScene', async () => {  const scene = await cesdk.engine.scene.saveToString();  console.log('Scene ready to save:', scene.length, 'characters');
  // Production:  // await fetch('/api/scenes', {  //   method: 'POST',  //   body: JSON.stringify({ scene }),  //   headers: { 'Content-Type': 'application/json' },  // });
  cesdk.ui.showNotification('Scene saved successfully');});
cesdk.actions.register('exportDesign', async options => {  const { blobs, options: exportOptions } = await cesdk.utils.export(options);  console.log('Export ready:', blobs[0].size, 'bytes');
  // Production:  // await uploadToCDN(blobs[0]);
  cesdk.ui.showNotification('Export successful');});
// Add navigation buttons that will use registered callbackscesdk.ui.insertNavigationBarOrderComponent('last', {  id: 'ly.img.actions.navigationBar',  children: [    'ly.img.saveScene.navigationBar', // Uses registered saveScene callback    'ly.img.exportImage.navigationBar', // Uses registered exportDesign callback  ],});
```

### Custom onClick Override[#](#custom-onclick-override)

```
// Override default callback with custom onClick handlercesdk.ui.insertNavigationBarOrderComponent('last', {  id: 'ly.img.actions.navigationBar',  children: [    {      id: 'ly.img.saveScene.navigationBar',      onClick: async () => {        // Custom logic that overrides the registered callback        const scene = await cesdk.engine.scene.saveToString();        console.log('Scene ready for custom save:', scene.length, 'characters');
        // Production:        // await customSaveLogic(scene);      },    },  ],});
```

## Default Behaviors[#](#default-behaviors)

The following action components trigger their corresponding callbacks when used as string IDs:

| Component ID | Callback Triggered | Default Behavior |
| --- | --- | --- |
| `ly.img.saveScene.navigationBar` | `saveScene` | Downloads the scene as a `.scene` file to the user’s device |
| `ly.img.importScene.navigationBar` | `importScene` | Opens a file picker to load a `.scene` file from the user’s device |
| `ly.img.exportScene.navigationBar` | `exportScene` | Downloads the current scene as a `.scene` file |
| `ly.img.exportImage.navigationBar` | `exportDesign` | Exports and downloads the design as an image file (PNG/JPEG) |
| `ly.img.exportPDF.navigationBar` | `exportDesign` | Exports and downloads the design as a PDF file |
| `ly.img.exportVideo.navigationBar` | `exportDesign` | Exports and downloads the design as a video file (MP4) |
| `ly.img.exportArchive.navigationBar` | `exportScene` | Creates and downloads an archive of the scene with all assets |
| `ly.img.importArchive.navigationBar` | `importScene` | Opens a file picker to load an archive file |
| `ly.img.shareScene.navigationBar` | `shareScene` | No default behavior - requires callback registration |

## Using Default vs Custom Behaviors[#](#using-default-vs-custom-behaviors)

### Example 1: Default Behavior[#](#example-1-default-behavior)

When using just the string ID without registering a custom callback, the default behavior is triggered (downloads the file to the user’s device):

```
// Using default behavior - downloads scene file to user's devicecesdk.ui.insertNavigationBarOrderComponent('last', {  id: 'ly.img.actions.navigationBar',  children: [    'ly.img.saveScene.navigationBar', // Uses default download behavior  ],});
```

### Example 2: Custom Behavior via Registered Callback[#](#example-2-custom-behavior-via-registered-callback)

Register a custom callback to override the default behavior for all instances of the button:

```
// Register custom saveScene callbackcesdk.actions.register('saveScene', async () => {  const scene = await cesdk.engine.scene.saveToString();  console.log('Scene ready to save:', scene.length, 'characters');
  // Production:  // await fetch('/api/scenes', {  //   method: 'POST',  //   body: JSON.stringify({ scene }),  //   headers: { 'Content-Type': 'application/json' },  // });
  cesdk.ui.showNotification('Scene saved to cloud');});
// String ID now uses the registered callback instead of defaultcesdk.ui.insertNavigationBarOrderComponent('last', {  id: 'ly.img.actions.navigationBar',  children: [    'ly.img.saveScene.navigationBar', // Triggers registered saveScene callback  ],});
```

### Example 3: Custom Behavior via onClick Handler[#](#example-3-custom-behavior-via-onclick-handler)

Provide a custom onClick handler directly in the component configuration to override both default and registered callbacks:

```
// Override with custom onClick handlercesdk.ui.insertNavigationBarOrderComponent('last', {  id: 'ly.img.actions.navigationBar',  children: [    {      id: 'ly.img.saveScene.navigationBar',      onClick: async () => {        // This custom onClick overrides any registered callback        const scene = await cesdk.engine.scene.saveToString();        console.log(          'Scene ready for alternative save:',          scene.length,          'characters',        );
        // Production:        // await alternativeSaveLogic(scene);
        cesdk.ui.showNotification('Saved with alternative method');      },    },  ],});
```

## API Reference[#](#api-reference)

| Method | Category | Purpose |
| --- | --- | --- |
| `cesdk.ui.getNavigationBarOrder()` | UI Layout | Get current navigation bar component order |
| `cesdk.ui.setNavigationBarOrder()` | UI Layout | Set navigation bar component order and configuration |
| `cesdk.ui.insertNavigationBarOrderComponent()` | UI Layout | Insert a component relative to an existing component |
| `cesdk.ui.removeNavigationBarOrderComponent()` | UI Layout | Remove a component from the navigation bar |
| `cesdk.ui.updateNavigationBarOrderComponent()` | UI Layout | Update properties of an existing component |
| `cesdk.ui.registerComponent()` | Component Registration | Register a custom component for use in ordering APIs |
| `cesdk.feature.enable()` | Feature | Enable a feature by ID |
| `cesdk.feature.disable()` | Feature | Disable a feature by ID |

---



[Source](https:/img.ly/docs/cesdk/vue/user-interface/customization/inspector-bar-8ca1cd)