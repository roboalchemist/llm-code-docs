# Class: UserInterfaceAPI

Control the user interface and behavior of the Creative Editor SDK.

The UserInterfaceAPI provides comprehensive methods for managing panels, notifications, dialogs, component registration, UI ordering, asset libraries, and custom interface elements within the editor.

## Constructors[#](#constructors)

### Constructor[#](#constructor)

  

`UserInterfaceAPI`

## Experimental Features[#](#experimental-features)

### unstable\_registerCustomPanel()[#](#unstable_registercustompanel)

Registers a custom panel that hooks into a DOM element for custom UI rendering.

The onMount function is called when the panel opens, and its return value (if a function) is called when the panel closes for cleanup.

#### Parameters[#](#parameters)

| Parameter | Type | Description |
| --- | --- | --- |
| `panelId` | `string` | The unique ID for the custom panel. |
| `onMount` | [`CustomPanelMountFunction`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/custompanelmountfunction/) | Function called when the panel is mounted, should return a cleanup function. This API may change or be removed in future versions. |

#### Returns[#](#returns)

`void`

* * *

### ~unstable\_getView()~[#](#unstable_getview)

Gets the current view style of the editor interface.

#### Returns[#](#returns-1)

[`ViewStyle`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/viewstyle/)

The current view style (‘default’ or ‘advanced’).

#### Deprecated[#](#deprecated)

Use `getView()` instead. This experimental API will be removed in a future version. This API may change or be removed in future versions.

#### Example[#](#example)

```
// Before (deprecated)const view = cesdk.ui.unstable_getView();
// After (preferred)const view = cesdk.ui.getView();
```

## Asset Library[#](#asset-library)

### addAssetLibraryEntry()[#](#addassetlibraryentry)

  

Adds a new asset library entry for display in asset libraries.

If an entry with the same ID already exists, it will be replaced. The method validates sorting configurations and warns about duplicates.

#### Parameters[#](#parameters-1)

| Parameter | Type | Description |
| --- | --- | --- |
| `AssetLibraryEntry` | [`AssetLibraryEntry`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/assetlibraryentry/) | The asset library entry configuration to add. |

#### Returns[#](#returns-2)

`void`

#### Signature[#](#signature)

```
addAssetLibraryEntry(AssetLibraryEntry: AssetLibraryEntry): void
```

* * *

### updateAssetLibraryEntry()[#](#updateassetlibraryentry)

  

Updates an existing asset library entry with new properties.

The provided properties will be merged with the existing entry.

#### Parameters[#](#parameters-2)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | [`AssetEntryId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/assetentryid/) | The ID of the asset library entry to update. |
| `assetLibraryEntry` |  | `Partial`<`Omit`<[`AssetLibraryEntry`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/assetlibraryentry/), `"id"` |

#### Returns[#](#returns-3)

`void`

#### Example[#](#example-1)

```
// Simple static updatecesdk.ui.updateAssetLibraryEntry('ly.img.colors', {  sourceIds: ['my-custom-colors']});
// Update other properties using callback with entrycesdk.ui.updateAssetLibraryEntry('ly.img.pagePresets', (entry) => ({  title: entry?.title ? `${entry.title} (Custom)` : 'Page Formats',  icon: { name: 'format-icon' }}));
// Extend sourceIds with lazy resolution (preserves dynamic behavior)cesdk.ui.updateAssetLibraryEntry('ly.img.typefaces', {  sourceIds: ({ currentIds }) => [...currentIds, 'my-custom-fonts']});
```

#### Signature[#](#signature-1)

```
updateAssetLibraryEntry(id: AssetEntryId, assetLibraryEntry: Partial<Omit<AssetLibraryEntry, "id" | "sourceIds"> & object> | (entry: AssetLibraryEntry) => Partial<Omit<AssetLibraryEntry, "id" | "sourceIds"> & object>): void
```

* * *

### removeAssetLibraryEntry()[#](#removeassetlibraryentry)

  

Removes an asset library entry from the available entries.

#### Parameters[#](#parameters-3)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | [`AssetEntryId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/assetentryid/) | The ID of the asset library entry to remove. |

#### Returns[#](#returns-4)

`void`

#### Signature[#](#signature-2)

```
removeAssetLibraryEntry(id: AssetEntryId): void
```

* * *

### getAssetLibraryEntry()[#](#getassetlibraryentry)

  

Gets a specific asset library entry by its ID.

#### Parameters[#](#parameters-4)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | [`AssetEntryId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/assetentryid/) | The ID of the asset library entry to retrieve. |

#### Returns[#](#returns-5)

[`AssetLibraryEntry`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/assetlibraryentry/)

The asset library entry configuration, or undefined if not found.

#### Signature[#](#signature-3)

```
getAssetLibraryEntry(id: AssetEntryId): AssetLibraryEntry
```

* * *

### findAllAssetLibraryEntries()[#](#findallassetlibraryentries)

  

Gets all currently registered asset library entry IDs.

#### Returns[#](#returns-6)

[`AssetEntryId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/assetentryid/)\[\]

Array of asset library entry IDs.

#### Signature[#](#signature-4)

```
findAllAssetLibraryEntries(): AssetEntryId[]
```

* * *

### ~setBackgroundTrackAssetLibraryEntries()~[#](#setbackgroundtrackassetlibraryentries)

  

Sets the asset library entries to use for the background track in video scenes.

This setting only affects video scenes and has no impact on other scene types.

#### Parameters[#](#parameters-5)

| Parameter | Type | Description |
| --- | --- | --- |
| `backgroundTrackAssetLibraryEntries` | [`AssetEntryId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/assetentryid/)\[\] | Array of asset library entry IDs for the background track. |

#### Returns[#](#returns-7)

`void`

#### Deprecated[#](#deprecated-1)

please use the cesdk.actions API to register an action for ‘addClip’ and implement your own logic.

#### Example[#](#example-2)

```
// Beforecesdk.ui.setBackgroundTrackAssetLibraryEntries(['ly.img.video', 'ly.img.image']);// Aftercesdk.actions.register('addClip', async () => {  cesdk.ui.openPanel('//ly.img.panel/assetLibrary', {    payload: {      entries: ['ly.img.video', 'ly.img.image']    }  });});
```

* * *

### ~getBackgroundTrackAssetLibraryEntries()~[#](#getbackgroundtrackassetlibraryentries)

  

Gets the asset library entries configured for the background track in video scenes.

This setting only affects video scenes and has no impact on other scene types.

#### Returns[#](#returns-8)

[`AssetEntryId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/assetentryid/)\[\]

Array of asset library entry IDs configured for the background track.

#### Deprecated[#](#deprecated-2)

The background track entries are now defined via the cesdk.actions API.

* * *

### setReplaceAssetLibraryEntries()[#](#setreplaceassetlibraryentries)

  

Sets a function that determines which asset library entries to use for replacement operations.

The function receives context information (like selected blocks or default entry IDs) and returns the appropriate asset library entry IDs for replacement.

#### Parameters[#](#parameters-6)

| Parameter | Type | Description |
| --- | --- | --- |
| `replaceAssetLibraryEntries` | (`context`) => [`AssetEntryId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/assetentryid/)\[\] | Function that receives context and returns an array of asset library entry IDs for replacement. |

#### Returns[#](#returns-9)

`void`

#### Signature[#](#signature-5)

```
setReplaceAssetLibraryEntries(replaceAssetLibraryEntries: (context: ReplaceAssetLibraryEntriesContext) => AssetEntryId[]): void
```

## Component Registration[#](#component-registration)

### registerPanel()[#](#registerpanel)

  

Registers a panel with builder-based rendering system.

The builder render function will be called with a builder and the engine as arguments. The builder object is used to defined what base components should be rendered (such as a button). The engine can be used to get any state from the engine. The render function will be re-called if anything in the engine changes regarding the made engine calls.

#### Type Parameters[#](#type-parameters)

| Type Parameter | Default type |
| --- | --- |
| `P` _extends_ [`ComponentPayload`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/componentpayload/) | [`ComponentPayload`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/componentpayload/) |

#### Parameters[#](#parameters-7)

| Parameter | Type | Description |
| --- | --- | --- |
| `panelId` | `string` | The panel ID for use with panel management APIs. |
| `renderPanel` | [`BuilderRenderFunction`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/builderrenderfunction/)<`P`\> | Function that renders the panel content using the builder system. |

#### Returns[#](#returns-10)

`void`

#### Signature[#](#signature-6)

```
registerPanel(panelId: string, renderPanel: BuilderRenderFunction<P>): void
```

* * *

### ~unstable\_registerPanel()~[#](#unstable_registerpanel)

  

Registers a panel with builder-based rendering system.

#### Type Parameters[#](#type-parameters-1)

| Type Parameter | Default type |
| --- | --- |
| `P` _extends_ [`ComponentPayload`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/componentpayload/) | [`ComponentPayload`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/componentpayload/) |

#### Parameters[#](#parameters-8)

| Parameter | Type | Description |
| --- | --- | --- |
| `panelId` | `string` | The panel ID for use with panel management APIs. |
| `renderComponent` | [`BuilderRenderFunction`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/builderrenderfunction/)<`P`\> | Function that renders the panel content using the builder system. |

#### Returns[#](#returns-11)

`void`

#### Deprecated[#](#deprecated-3)

Use `registerPanel` instead.

* * *

### registerComponent()[#](#registercomponent)

  

Registers a component that can be rendered at different UI locations.

The builder render function will be called with a builder and the engine as arguments. The builder object is used to defined what base components should be rendered (such as a button). The engine can be used to get any state from the engine. The render function will be re-called if anything in the engine changes regarding the made engine calls.

#### Type Parameters[#](#type-parameters-2)

| Type Parameter | Default type |
| --- | --- |
| `P` _extends_ [`ComponentPayload`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/componentpayload/) | [`ComponentPayload`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/componentpayload/) |

#### Parameters[#](#parameters-9)

| Parameter | Type | Description |
| --- | --- | --- |
| `ids` | `string` | `string`\[\] |
| `renderComponent` | [`BuilderRenderFunction`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/builderrenderfunction/)<`P`\> | Function that renders the component using the builder system. |

#### Returns[#](#returns-12)

`void`

#### Signature[#](#signature-7)

```
registerComponent(ids: string | string[], renderComponent: BuilderRenderFunction<P>): void
```

## Dialogs[#](#dialogs)

### showDialog()[#](#showdialog)

  

Displays a modal dialog with custom content and actions.

Dialogs can have different types (info, success, warning, error, loading) and support custom actions like OK, Cancel, or custom buttons.

#### Parameters[#](#parameters-10)

| Parameter | Type | Description |
| --- | --- | --- |
| `dialog` | `string` | [`Dialog`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/dialog/) |

#### Returns[#](#returns-13)

`string`

The dialog ID for programmatic updates or closure.

#### Signature[#](#signature-8)

```
showDialog(dialog: string | Dialog): string
```

* * *

### updateDialog()[#](#updatedialog)

  

Updates an existing dialog with new content or properties.

The dialog properties will be merged with the existing dialog configuration.

#### Parameters[#](#parameters-11)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `string` | The ID of the dialog to update. |
| `dialog` |  | `Partial`<[`Dialog`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/dialog/)\> |

#### Returns[#](#returns-14)

`void`

#### Signature[#](#signature-9)

```
updateDialog(id: string, dialog: Partial<Dialog> | (dialog: Dialog) => Partial<Dialog>): void
```

* * *

### closeDialog()[#](#closedialog)

  

Closes a dialog programmatically.

If the dialog has an onClose callback, it will be executed before removal. Closing an already closed dialog has no effect.

#### Parameters[#](#parameters-12)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `string` | The ID of the dialog to close. |

#### Returns[#](#returns-15)

`void`

#### Signature[#](#signature-10)

```
closeDialog(id: string): void
```

## Notifications[#](#notifications)

### showNotification()[#](#shownotification)

  

Displays a non-blocking notification message to the user.

Notifications appear temporarily and can be dismissed by the user. They support different types (info, success, warning, error) and durations.

#### Parameters[#](#parameters-13)

| Parameter | Type | Description |
| --- | --- | --- |
| `notification` |  | `string` |

#### Returns[#](#returns-16)

`string`

The notification ID for programmatic updates or dismissal.

#### Signature[#](#signature-11)

```
showNotification(notification: string | Notification_2): string
```

* * *

### dismissNotification()[#](#dismissnotification)

  

Dismisses a notification programmatically.

#### Parameters[#](#parameters-14)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `string` | The ID of the notification to dismiss. |

#### Returns[#](#returns-17)

`void`

#### Signature[#](#signature-12)

```
dismissNotification(id: string): void
```

* * *

### updateNotification()[#](#updatenotification)

  

Updates an existing notification with new content or properties.

The notification object will be merged with the existing notification. If the duration is updated, the timeout will be reset. Updates to dismissed notifications are ignored.

#### Parameters[#](#parameters-15)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `string` | The ID of the notification to update. |
| `notification` | `Partial`<[`Notification`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/notification/)\> | Partial notification properties to merge. |

#### Returns[#](#returns-18)

`void`

#### Signature[#](#signature-13)

```
updateNotification(id: string, notification: Partial<Notification_2>): void
```

## Other[#](#other)

### experimental[#](#experimental)

  

PLEASE NOTE: This contains experimental APIs.

Use them with caution since they might change without warning and might be replaced with a completely different concept or maybe not at all.

* * *

### getView()[#](#getview)

  

Gets the current view style of the editor interface.

The view style controls the complexity and feature set shown in the UI. ‘default’ provides a simplified interface, while ‘advanced’ shows more comprehensive editing tools and options.

#### Returns[#](#returns-19)

[`ViewStyle`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/viewstyle/)

The current view style (‘default’ or ‘advanced’).

#### Example[#](#example-3)

```
// Get the current view styleconst viewStyle = cesdk.ui.getView(); // 'default' or 'advanced'
// Use for conditional UI logicconst showAdvancedOptions = cesdk.ui.getView() === 'advanced';
// Switch to advanced mode if currently in defaultif (cesdk.ui.getView() === 'default') {  cesdk.ui.setView('advanced');}
```

#### Signature[#](#signature-14)

```
getView(): ViewStyle
```

* * *

### setView()[#](#setview)

  

Sets the view style of the editor interface.

This immediately updates the UI to reflect the new view style. The view style controls which UI elements and features are available.

#### Parameters[#](#parameters-16)

| Parameter | Type | Description |
| --- | --- | --- |
| `view` | [`ViewStyle`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/viewstyle/) | The view style to set (‘default’ or ‘advanced’). |

#### Returns[#](#returns-20)

`void`

#### Example[#](#example-4)

```
// Set view to advanced modecesdk.ui.setView('advanced');
// Set view to simplified modecesdk.ui.setView('default');
// Toggle between view stylesconst currentView = cesdk.ui.getView();const newView = currentView === 'advanced' ? 'default' : 'advanced';cesdk.ui.setView(newView);
```

* * *

### applyForceCrop()[#](#applyforcecrop)

  

programmatically applies a crop preset to a design block.

This is useful in scenarios where you want to enforce a particular format (e.g., fixed aspect ratio) and define how the editor should respond after the preset is applied.

#### Parameters[#](#parameters-17)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The ID of the design block to apply the crop preset to. |
| `options` | { `sourceId`: `string`; `presetId`: `string`; `mode`: `"silent"` | `"always"` |
| `options.sourceId` | `string` | \- |
| `options.presetId` | `string` | \- |
| `options.mode` | `"silent"` | `"always"` |

#### Returns[#](#returns-21)

`Promise`<`void`\>

#### Signature[#](#signature-15)

```
applyForceCrop(id: number, options: object): Promise<void>
```

## Panel Management[#](#panel-management)

### openPanel()[#](#openpanel)

  

Opens a panel if it exists, is not already open, and is currently registered.

If requirements are not met, this is a no-op.

Available built-in panel IDs:

*   `//ly.img.panel/inspector` - Opens the inspector panel for the selected block
*   `//ly.img.panel/assetLibrary.replace` - Opens the asset library for replacing the selected block. Beware that the library might show nothing depending on how it was configured.

#### Type Parameters[#](#type-parameters-3)

| Type Parameter |
| --- |
| `T` _extends_ [`PanelId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/panelid/) |

#### Parameters[#](#parameters-18)

| Parameter | Type | Description |
| --- | --- | --- |
| `panelId` | `T` | The ID of the panel to open. |
| `options?` | [`PanelOptions`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/paneloptions/)<`T`\> | Optional configuration for panel position and floating state. |

#### Returns[#](#returns-22)

`void`

#### Signature[#](#signature-16)

```
openPanel(panelId: T, options?: PanelOptions<T>): void
```

* * *

### closePanel()[#](#closepanel)

  

Closes panels that match the given pattern. Supports wildcard matching.

Available built-in panel IDs:

*   `//ly.img.panel/inspector` - Inspector panel
*   `//ly.img.panel/assetLibrary` - Asset library
*   `//ly.img.panel/assetLibrary.replace` - Replacement asset library

#### Parameters[#](#parameters-19)

| Parameter | Type | Description |
| --- | --- | --- |
| `panelId` | `string` | The panel ID or pattern to match panels for closing. |

#### Returns[#](#returns-23)

`void`

#### Example[#](#example-5)

```
// Close a specific panel by exact IDcesdk.ui.closePanel('//ly.img.panel/inspector');
// Close all ly.img panels using wildcardcesdk.ui.closePanel('//ly.img.*');
// Close all panels with specific prefixcesdk.ui.closePanel('//ly.img.panel/*');
// Close panels matching complex patterncesdk.ui.closePanel('//ly.img.panel/' + '*' + '/stroke/' + '*');
// Close any inspector panels regardless of namespacecesdk.ui.closePanel('*' + '/inspector');
// Close all asset library panelscesdk.ui.closePanel('*assetLibrary*');
```

#### Signature[#](#signature-17)

```
closePanel(panelId: string): void
```

* * *

### isPanelOpen()[#](#ispanelopen)

  

Checks if a panel is currently open.

Available built-in panel IDs:

*   `//ly.img.panel/inspector` - Inspector panel for the selected block
*   `//ly.img.panel/assetLibrary` - Asset library panel
*   `//ly.img.panel/assetLibrary.replace` - Replacement asset library panel

#### Type Parameters[#](#type-parameters-4)

| Type Parameter |
| --- |
| `T` _extends_ [`PanelId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/panelid/) |

#### Parameters[#](#parameters-20)

| Parameter | Type | Description |
| --- | --- | --- |
| `panelId` | `T` | The ID of the panel to check. |
| `options?` | [`PanelOptions`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/paneloptions/)<`T`\> | Optional criteria to match against the panel’s current state. |

#### Returns[#](#returns-24)

`boolean`

True if the panel is open and matches the specified options, false otherwise.

#### Signature[#](#signature-18)

```
isPanelOpen(panelId: T, options?: PanelOptions<T>): boolean
```

* * *

### findAllPanels()[#](#findallpanels)

  

Gets all panel IDs, optionally filtered by state or position.

#### Type Parameters[#](#type-parameters-5)

| Type Parameter |
| --- |
| `T` _extends_ [`PanelId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/panelid/) |

#### Parameters[#](#parameters-21)

| Parameter | Type | Description |
| --- | --- | --- |
| `options?` | [`PanelOptions`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/paneloptions/)<`T`\> & `object` | Optional filter criteria for panel state and position. |

#### Returns[#](#returns-25)

`string`\[\]

Array of panel IDs matching the specified criteria.

#### Example[#](#example-6)

```
cesdk.ui.findAllPanels();cesdk.ui.findAllPanels({ open: true, position: 'left' });
```

#### Signature[#](#signature-19)

```
findAllPanels(options?: PanelOptions<T> & object): string[]
```

* * *

### setPanelPosition()[#](#setpanelposition)

  

Sets the position of a panel within the editor interface.

#### Parameters[#](#parameters-22)

| Parameter | Type | Description |
| --- | --- | --- |
| `panelId` | `string` | The ID of the panel to position. |
| `panelPosition` |  | [`PanelPosition`](https://img.ly/docs/cesdk/vue/api/cesdk-js/enumerations/panelposition/) |

#### Returns[#](#returns-26)

`void`

#### Signature[#](#signature-20)

```
setPanelPosition(panelId: string, panelPosition: PanelPosition | () => PanelPosition): void
```

* * *

### getPanelPosition()[#](#getpanelposition)

  

Gets the current position of a panel.

#### Parameters[#](#parameters-23)

| Parameter | Type | Description |
| --- | --- | --- |
| `panelId` | `string` | The ID of the panel. |

#### Returns[#](#returns-27)

[`PanelPosition`](https://img.ly/docs/cesdk/vue/api/cesdk-js/enumerations/panelposition/)

The panel’s position (‘left’ or ‘right’).

#### Signature[#](#signature-21)

```
getPanelPosition(panelId: string): PanelPosition
```

* * *

### setPanelFloating()[#](#setpanelfloating)

  

Sets whether a panel floats over the canvas.

#### Parameters[#](#parameters-24)

| Parameter | Type | Description |
| --- | --- | --- |
| `panelId` | `string` | The ID of the panel to configure. |
| `floating` | `boolean` | () => `boolean` |

#### Returns[#](#returns-28)

`void`

#### Signature[#](#signature-22)

```
setPanelFloating(panelId: string, floating: boolean | () => boolean): void
```

* * *

### getPanelFloating()[#](#getpanelfloating)

  

Checks if a panel is currently floating over the canvas.

#### Parameters[#](#parameters-25)

| Parameter | Type | Description |
| --- | --- | --- |
| `panelId` | `string` | The ID of the panel to check. |

#### Returns[#](#returns-29)

`boolean`

True if the panel is floating, false if it’s docked.

#### Signature[#](#signature-23)

```
getPanelFloating(panelId: string): boolean
```

## Theme Management[#](#theme-management)

### getTheme()[#](#gettheme)

  

Gets the resolved theme that is currently being used. If the theme configuration is ‘system’, returns the OS preference. If the theme configuration is a function, it is evaluated lazily and the result is returned.

#### Returns[#](#returns-30)

[`Theme`](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/configtypes/type-aliases/theme/)

The resolved theme (‘light’ or ‘dark’).

#### Example[#](#example-7)

```
// Get the actual theme being usedconst theme = cesdk.ui.getTheme(); // 'light' or 'dark'
// Use for conditional stylingconst iconColor = cesdk.ui.getTheme() === 'dark' ? 'white' : 'black';
// Theme function is evaluated each time getTheme() is calledcesdk.ui.setTheme(() => new Date().getHours() >= 18 ? 'dark' : 'light');const currentTheme = cesdk.ui.getTheme(); // Function is evaluated here
```

#### Signature[#](#signature-24)

```
getTheme(): Theme
```

* * *

### setTheme()[#](#settheme)

  

Sets the theme configuration.

This will immediately update the UI to reflect the new theme. Can be set to:

*   ‘light’ or ‘dark’ for a specific theme
*   ‘system’ to use the OS preference
*   A function that returns ‘light’ or ‘dark’ for dynamic theming

#### Parameters[#](#parameters-26)

| Parameter | Type | Description |
| --- | --- | --- |
| `theme` | [`ThemeConfig`](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/configtypes/type-aliases/themeconfig/) | The theme configuration to set. |

#### Returns[#](#returns-31)

`void`

#### Example[#](#example-8)

```
// Set a specific themecesdk.ui.setTheme('dark');
// Use system preferencecesdk.ui.setTheme('system');
// Set theme based on custom logiccesdk.ui.setTheme(() => {  const hour = new Date().getHours();  return hour >= 18 || hour < 6 ? 'dark' : 'light';});
// Toggle between themesconst currentTheme = cesdk.ui.getTheme();const newTheme = currentTheme === 'dark' ? 'light' : 'dark';cesdk.ui.setTheme(newTheme);
```

## UI Layout[#](#ui-layout)

### setDockOrder()[#](#setdockorder)

  

Sets the rendering order of components in the dock area.

The ids in this order refer to registered default components or custom components registered in `registerComponent`.

Different orders can be set depending on different contexts. The context consists of the edit mode (e.g. `Transform` or `Text`) right now. If no context is given, the default order is set for the `Transform` edit mode.

#### Parameters[#](#parameters-27)

| Parameter | Type | Description |
| --- | --- | --- |
| `dockOrder` | ( | [`DockOrderComponentId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/dockordercomponentid/) |
| `orderContext?` | [`OrderContext`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercontext/) | Optional context specifying when this order applies. |

#### Returns[#](#returns-32)

`void`

#### Signature[#](#signature-25)

```
setDockOrder(dockOrder: DockOrderComponentId | DockOrderComponent[], orderContext?: OrderContext): void
```

* * *

### getDockOrder()[#](#getdockorder)

  

Gets the current rendering order of dock components.

The id in this order refer to registered default components or custom components registered in `registerComponent`.

Different orders could have been set depending on different contexts. The context consists of the edit mode (e.g. `Transform` or `Text`) right now. If no context is given, the default order (with `Transform` edit mode) is returned.

#### Parameters[#](#parameters-28)

| Parameter | Type | Description |
| --- | --- | --- |
| `orderContext?` | [`OrderContext`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercontext/) | Optional context specifying which order to retrieve. |

#### Returns[#](#returns-33)

[`DockOrderComponent`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/dockordercomponent/)\[\]

Array of component configurations defining the dock order.

#### Signature[#](#signature-26)

```
getDockOrder(orderContext?: OrderContext): DockOrderComponent[]
```

* * *

### updateDockOrderComponent()[#](#updatedockordercomponent)

  

Updates a component in the render order of the dock area.

This method finds a dock order component matching the provided matcher and updates it with the given component, ID, or updater function. The matcher can be a function or an object describing the component to match. The update can be a new ID, a partial object with updated properties, or a function that receives the current component and returns the updated one.

The update API can be used in different contexts (such as edit modes).

#### Parameters[#](#parameters-29)

| Parameter | Type | Description |
| --- | --- | --- |
| `matcher` | [`OrderComponentMatcher`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/ordercomponentmatcher/)<[`OrderComponent`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercomponent/)<[`DockOrderComponentId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/dockordercomponentid/)\>> | Function or object to match the component to update. |
| `update` |  | [`DockOrderComponentId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/dockordercomponentid/) |
| `orderContext?` | [`OrderContext`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercontext/) | Optional context specifying which order to update. |

#### Returns[#](#returns-34)

`object`

The updated dock order array.

| Name | Type |
| --- | --- |
| `updated` | `number` |
| `order` | [`OrderComponent`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercomponent/)<[`DockOrderComponentId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/dockordercomponentid/)\>\[\] |

#### Signature[#](#signature-27)

```
updateDockOrderComponent(matcher: OrderComponentMatcher<OrderComponent<DockOrderComponentId>>, update: DockOrderComponentId | Partial<OrderComponent<DockOrderComponentId>> | (component: OrderComponent<DockOrderComponentId>) => Partial<OrderComponent<DockOrderComponentId>>, orderContext?: OrderContext): object
```

* * *

### removeDockOrderComponent()[#](#removedockordercomponent)

  

Removes a component from the render order of the dock area.

This method finds a dock order component matching the provided matcher and removes it from the current order. The matcher can be a function or an object describing the component to match.

The remove API can be used in different contexts (such as edit modes).

#### Parameters[#](#parameters-30)

| Parameter | Type | Description |
| --- | --- | --- |
| `matcher` | [`OrderComponentMatcher`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/ordercomponentmatcher/)<[`OrderComponent`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercomponent/)<[`DockOrderComponentId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/dockordercomponentid/)\>> | Function or object to match the component to remove. |
| `orderContext?` | [`OrderContext`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercontext/) | Optional context specifying which order to update. |

#### Returns[#](#returns-35)

`object`

The updated dock order array.

| Name | Type |
| --- | --- |
| `removed` | `number` |
| `order` | [`DockOrderComponent`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/dockordercomponent/)\[\] |

#### Signature[#](#signature-28)

```
removeDockOrderComponent(matcher: OrderComponentMatcher<OrderComponent<DockOrderComponentId>>, orderContext?: OrderContext): object
```

* * *

### insertDockOrderComponent()[#](#insertdockordercomponent)

  

Inserts a component into the render order of the dock area.

This method inserts a new dock order component before, after, or to replace a component matching the provided matcher. The matcher can be a function or an object describing the component to match. The location can be ‘before’, ‘after’, or ‘replace’.

The insert API can be used in different contexts (such as edit modes).

#### Parameters[#](#parameters-31)

| Parameter | Type | Description |
| --- | --- | --- |
| `matcher` | [`OrderComponentMatcher`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/ordercomponentmatcher/)<[`OrderComponent`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercomponent/)<[`DockOrderComponentId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/dockordercomponentid/)\>> | Function or object to match the component to insert relative to. |
| `component` |  | [`DockOrderComponentId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/dockordercomponentid/) |
| `location?` | [`InsertOrderComponentLocation`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/insertordercomponentlocation/) | Where to insert the new component relative to the matched component (‘before’ or ‘after’). |
| `orderContext?` | [`OrderContext`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercontext/) | Optional context specifying which order to update. |

#### Returns[#](#returns-36)

`object`

The updated dock order array.

| Name | Type |
| --- | --- |
| `inserted` | `boolean` |
| `order` | [`DockOrderComponent`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/dockordercomponent/)\[\] |

#### Signature[#](#signature-29)

```
insertDockOrderComponent(matcher: OrderComponentMatcher<OrderComponent<DockOrderComponentId>>, component: DockOrderComponentId | OrderComponent<DockOrderComponentId>, location?: InsertOrderComponentLocation, orderContext?: OrderContext): object
```

* * *

### setInspectorBarOrder()[#](#setinspectorbarorder)

  

Sets the rendering order of components in the inspector bar.

The id in this order refer to registered default components or custom components registered in `registerComponent`.

Different orders can be set depending on different contexts. The context consists of the edit mode (e.g. `Transform` or `Text`) right now. If no context is given, the default order is set for the `Transform` edit mode.

#### Parameters[#](#parameters-32)

| Parameter | Type | Description |
| --- | --- | --- |
| `inspectorBarOrder` | ( | [`InspectorBarComponentId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/inspectorbarcomponentid/) |
| `orderContext?` | [`OrderContext`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercontext/) | Optional context specifying when this order applies. |

#### Returns[#](#returns-37)

`void`

#### Signature[#](#signature-30)

```
setInspectorBarOrder(inspectorBarOrder: InspectorBarComponentId | OrderComponent<InspectorBarComponentId>[], orderContext?: OrderContext): void
```

* * *

### getInspectorBarOrder()[#](#getinspectorbarorder)

  

Gets the current rendering order of inspector bar components.

Component IDs refer to built-in components or those registered via registerComponent. Returns the order for the specified context, or defaults to Transform mode if no context is provided.

#### Parameters[#](#parameters-33)

| Parameter | Type | Description |
| --- | --- | --- |
| `orderContext?` | [`OrderContext`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercontext/) | Optional context specifying which order to retrieve. |

#### Returns[#](#returns-38)

[`OrderComponent`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercomponent/)<[`ComponentId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/componentid/)\>\[\]

Array of component configurations defining the inspector bar order.

#### Signature[#](#signature-31)

```
getInspectorBarOrder(orderContext?: OrderContext): OrderComponent<ComponentId>[]
```

* * *

### updateInspectorBarOrderComponent()[#](#updateinspectorbarordercomponent)

  

Updates a component in the render order of the inspector bar.

This method finds an inspector bar order component matching the provided matcher and updates it with the given component, ID, or updater function. The matcher can be a function or an object describing the component to match. The update can be a new ID, a partial object with updated properties, or a function that receives the current component and returns the updated one.

The update API can be used in different contexts (such as edit modes).

#### Parameters[#](#parameters-34)

| Parameter | Type | Description |
| --- | --- | --- |
| `matcher` | [`OrderComponentMatcher`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/ordercomponentmatcher/)<[`OrderComponent`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercomponent/)<[`InspectorBarComponentId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/inspectorbarcomponentid/)\>> | Function or object to match the component to update. |
| `update` |  | [`InspectorBarComponentId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/inspectorbarcomponentid/) |
| `orderContext?` | [`OrderContext`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercontext/) | Optional context specifying which order to update. |

#### Returns[#](#returns-39)

`object`

The updated inspector bar order array.

| Name | Type |
| --- | --- |
| `updated` | `number` |
| `order` | [`OrderComponent`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercomponent/)<[`InspectorBarComponentId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/inspectorbarcomponentid/)\>\[\] |

#### Signature[#](#signature-32)

```
updateInspectorBarOrderComponent(matcher: OrderComponentMatcher<OrderComponent<InspectorBarComponentId>>, update: InspectorBarComponentId | Partial<OrderComponent<InspectorBarComponentId>> | (component: OrderComponent<InspectorBarComponentId>) => Partial<OrderComponent<InspectorBarComponentId>>, orderContext?: OrderContext): object
```

* * *

### removeInspectorBarOrderComponent()[#](#removeinspectorbarordercomponent)

  

Removes a component from the render order of the inspector bar.

This method finds an inspector bar order component matching the provided matcher and removes it from the current order. The matcher can be a function or an object describing the component to match.

The remove API can be used in different contexts (such as edit modes).

#### Parameters[#](#parameters-35)

| Parameter | Type | Description |
| --- | --- | --- |
| `matcher` | [`OrderComponentMatcher`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/ordercomponentmatcher/)<[`OrderComponent`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercomponent/)<[`InspectorBarComponentId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/inspectorbarcomponentid/)\>> | Function or object to match the component to remove. |
| `orderContext?` | [`OrderContext`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercontext/) | Optional context specifying which order to update. |

#### Returns[#](#returns-40)

`object`

The updated inspector bar order array.

| Name | Type |
| --- | --- |
| `removed` | `number` |
| `order` | [`OrderComponent`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercomponent/)<[`InspectorBarComponentId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/inspectorbarcomponentid/)\>\[\] |

#### Signature[#](#signature-33)

```
removeInspectorBarOrderComponent(matcher: OrderComponentMatcher<OrderComponent<InspectorBarComponentId>>, orderContext?: OrderContext): object
```

* * *

### insertInspectorBarOrderComponent()[#](#insertinspectorbarordercomponent)

  

Inserts a component into the render order of the inspector bar.

This method inserts a new inspector bar order component before, after, or to replace a component matching the provided matcher. The matcher can be a function or an object describing the component to match. The location can be ‘before’, ‘after’, or ‘replace’.

The insert API can be used in different contexts (such as edit modes).

#### Parameters[#](#parameters-36)

| Parameter | Type | Description |
| --- | --- | --- |
| `matcher` | [`OrderComponentMatcher`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/ordercomponentmatcher/)<[`OrderComponent`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercomponent/)<[`InspectorBarComponentId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/inspectorbarcomponentid/)\>> | Function or object to match the component to insert relative to. |
| `component` |  | [`InspectorBarComponentId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/inspectorbarcomponentid/) |
| `location?` | [`InsertOrderComponentLocation`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/insertordercomponentlocation/) | Where to insert the new component relative to the matched component (‘before’ or ‘after’). |
| `orderContext?` | [`OrderContext`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercontext/) | Optional context specifying which order to update. |

#### Returns[#](#returns-41)

`object`

The updated inspector bar order array.

| Name | Type |
| --- | --- |
| `inserted` | `boolean` |
| `order` | [`OrderComponent`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercomponent/)<[`InspectorBarComponentId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/inspectorbarcomponentid/)\>\[\] |

#### Signature[#](#signature-34)

```
insertInspectorBarOrderComponent(matcher: OrderComponentMatcher<OrderComponent<InspectorBarComponentId>>, component: InspectorBarComponentId | OrderComponent<InspectorBarComponentId>, location?: InsertOrderComponentLocation, orderContext?: OrderContext): object
```

* * *

### setCanvasMenuOrder()[#](#setcanvasmenuorder)

  

Sets the rendering order of components in the canvas menu.

Component IDs refer to built-in components or those registered via registerComponent. Different orders can be set for different contexts (e.g., Transform or Text edit modes). Defaults to Transform mode if no context is provided.

#### Parameters[#](#parameters-37)

| Parameter | Type | Description |
| --- | --- | --- |
| `canvasMenuOrder` | ( | [`CanvasMenuComponentId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/canvasmenucomponentid/) |
| `orderContext?` | [`OrderContext`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercontext/) | Optional context specifying when this order applies. |

#### Returns[#](#returns-42)

`void`

#### Signature[#](#signature-35)

```
setCanvasMenuOrder(canvasMenuOrder: CanvasMenuComponentId | CanvasMenuOrderComponent[], orderContext?: OrderContext): void
```

* * *

### getCanvasMenuOrder()[#](#getcanvasmenuorder)

  

Gets the current rendering order of canvas menu components.

Component IDs refer to built-in components or those registered via registerComponent. Returns the order for the specified context, or defaults to Transform mode if no context is provided.

#### Parameters[#](#parameters-38)

| Parameter | Type | Description |
| --- | --- | --- |
| `orderContext?` | [`OrderContext`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercontext/) | Optional context specifying which order to retrieve. |

#### Returns[#](#returns-43)

[`CanvasMenuOrderComponent`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/canvasmenuordercomponent/)\[\]

Array of component configurations defining the canvas menu order.

#### Signature[#](#signature-36)

```
getCanvasMenuOrder(orderContext?: OrderContext): CanvasMenuOrderComponent[]
```

* * *

### updateCanvasMenuOrderComponent()[#](#updatecanvasmenuordercomponent)

  

Updates a component in the render order of the canvas menu.

This method finds a canvas menu order component matching the provided matcher and updates it with the given component, ID, or updater function. The matcher can be a function or an object describing the component to match. The update can be a new ID, a partial object with updated properties, or a function that receives the current component and returns the updated one.

The update API can be used in different contexts (such as edit modes).

#### Parameters[#](#parameters-39)

| Parameter | Type | Description |
| --- | --- | --- |
| `matcher` | [`OrderComponentMatcher`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/ordercomponentmatcher/)<[`OrderComponent`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercomponent/)<[`CanvasMenuComponentId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/canvasmenucomponentid/)\>> | Function or object to match the component to update. |
| `update` |  | [`CanvasMenuComponentId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/canvasmenucomponentid/) |
| `orderContext?` | [`OrderContext`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercontext/) | Optional context specifying which order to update. |

#### Returns[#](#returns-44)

`object`

An object containing the number of updated components and the updated canvas menu order array.

| Name | Type |
| --- | --- |
| `updated` | `number` |
| `order` | [`CanvasMenuOrderComponent`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/canvasmenuordercomponent/)\[\] |

#### Signature[#](#signature-37)

```
updateCanvasMenuOrderComponent(matcher: OrderComponentMatcher<OrderComponent<CanvasMenuComponentId>>, update: CanvasMenuComponentId | Partial<CanvasMenuOrderComponent> | (component: CanvasMenuOrderComponent) => Partial<CanvasMenuOrderComponent>, orderContext?: OrderContext): object
```

* * *

### removeCanvasMenuOrderComponent()[#](#removecanvasmenuordercomponent)

  

Removes a component from the render order of the canvas menu.

This method finds a canvas menu order component matching the provided matcher and removes it from the current order. The matcher can be a function or an object describing the component to match.

The remove API can be used in different contexts (such as edit modes).

#### Parameters[#](#parameters-40)

| Parameter | Type | Description |
| --- | --- | --- |
| `matcher` | [`OrderComponentMatcher`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/ordercomponentmatcher/)<[`OrderComponent`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercomponent/)<[`CanvasMenuComponentId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/canvasmenucomponentid/)\>> | Function or object to match the component to remove. |
| `orderContext?` | [`OrderContext`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercontext/) | Optional context specifying which order to update. |

#### Returns[#](#returns-45)

`object`

An object containing the number of removed components and the updated canvas menu order array.

| Name | Type |
| --- | --- |
| `removed` | `number` |
| `order` | [`CanvasMenuOrderComponent`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/canvasmenuordercomponent/)\[\] |

#### Signature[#](#signature-38)

```
removeCanvasMenuOrderComponent(matcher: OrderComponentMatcher<OrderComponent<CanvasMenuComponentId>>, orderContext?: OrderContext): object
```

* * *

### insertCanvasMenuOrderComponent()[#](#insertcanvasmenuordercomponent)

  

Inserts a component into the render order of the canvas menu.

This method inserts a new canvas menu order component before, after, or to replace a component matching the provided matcher. The matcher can be a function or an object describing the component to match. The location can be ‘before’, ‘after’, or ‘replace’.

The insert API can be used in different contexts (such as edit modes).

#### Parameters[#](#parameters-41)

| Parameter | Type | Description |
| --- | --- | --- |
| `matcher` | [`OrderComponentMatcher`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/ordercomponentmatcher/)<[`OrderComponent`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercomponent/)<[`CanvasMenuComponentId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/canvasmenucomponentid/)\>> | Function or object to match the component to insert relative to. |
| `component` |  | [`CanvasMenuComponentId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/canvasmenucomponentid/) |
| `location?` | [`InsertOrderComponentLocation`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/insertordercomponentlocation/) | Where to insert the new component relative to the matched component (‘before’ or ‘after’). |
| `orderContext?` | [`OrderContext`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercontext/) | Optional context specifying which order to update. |

#### Returns[#](#returns-46)

`object`

The updated canvas menu order array.

| Name | Type |
| --- | --- |
| `inserted` | `boolean` |
| `order` | [`OrderComponent`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercomponent/)<[`CanvasMenuComponentId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/canvasmenucomponentid/)\>\[\] |

#### Signature[#](#signature-39)

```
insertCanvasMenuOrderComponent(matcher: OrderComponentMatcher<OrderComponent<CanvasMenuComponentId>>, component: CanvasMenuComponentId | CanvasMenuOrderComponent, location?: InsertOrderComponentLocation, orderContext?: OrderContext): object
```

* * *

### setNavigationBarOrder()[#](#setnavigationbarorder)

  

Sets the rendering order of components in the navigation bar.

Component IDs refer to built-in components or those registered via registerComponent. Different orders can be set for different contexts (e.g., Transform or Text edit modes). Defaults to Transform mode if no context is provided.

#### Parameters[#](#parameters-42)

| Parameter | Type | Description |
| --- | --- | --- |
| `navigationBarOrder` | ( | [`NavigationBarComponentId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/navigationbarcomponentid/) |
| `orderContext?` | [`OrderContext`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercontext/) | Optional context specifying when this order applies. |

#### Returns[#](#returns-47)

`void`

#### Signature[#](#signature-40)

```
setNavigationBarOrder(navigationBarOrder: NavigationBarComponentId | NavigationBarOrderComponent[], orderContext?: OrderContext): void
```

* * *

### updateNavigationBarOrderComponent()[#](#updatenavigationbarordercomponent)

  

Updates a component in the render order of the navigation bar.

This method finds a navigation bar order component matching the provided matcher and updates it with the given component, ID, or updater function. The matcher can be a function or an object describing the component to match. The update can be a new ID, a partial object with updated properties, or a function that receives the current component and returns the updated one.

The update API can be used in different contexts (such as edit modes).

#### Parameters[#](#parameters-43)

| Parameter | Type | Description |
| --- | --- | --- |
| `matcher` | [`OrderComponentMatcher`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/ordercomponentmatcher/)<[`OrderComponent`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercomponent/)<[`NavigationBarComponentId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/navigationbarcomponentid/)\>> | Function or object to match the component to update. |
| `update` |  | [`NavigationBarComponentId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/navigationbarcomponentid/) |
| `orderContext?` | [`OrderContext`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercontext/) | Optional context specifying which order to update. |

#### Returns[#](#returns-48)

`object`

An object containing the number of updated components and the updated navigation bar order array.

| Name | Type |
| --- | --- |
| `updated` | `number` |
| `order` | [`NavigationBarOrderComponent`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/navigationbarordercomponent/)\[\] |

#### Signature[#](#signature-41)

```
updateNavigationBarOrderComponent(matcher: OrderComponentMatcher<OrderComponent<NavigationBarComponentId>>, update: NavigationBarComponentId | Partial<NavigationBarOrderComponent> | (component: NavigationBarOrderComponent) => Partial<NavigationBarOrderComponent>, orderContext?: OrderContext): object
```

* * *

### removeNavigationBarOrderComponent()[#](#removenavigationbarordercomponent)

  

Removes a component from the render order of the navigation bar.

This method finds a navigation bar order component matching the provided matcher and removes it from the current order. The matcher can be a function or an object describing the component to match.

The remove API can be used in different contexts (such as edit modes).

#### Parameters[#](#parameters-44)

| Parameter | Type | Description |
| --- | --- | --- |
| `matcher` | [`OrderComponentMatcher`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/ordercomponentmatcher/)<[`OrderComponent`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercomponent/)<[`NavigationBarComponentId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/navigationbarcomponentid/)\>> | Function or object to match the component to remove. |
| `orderContext?` | [`OrderContext`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercontext/) | Optional context specifying which order to update. |

#### Returns[#](#returns-49)

`object`

An object containing the number of removed components and the updated navigation bar order array.

| Name | Type |
| --- | --- |
| `removed` | `number` |
| `order` | [`NavigationBarOrderComponent`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/navigationbarordercomponent/)\[\] |

#### Signature[#](#signature-42)

```
removeNavigationBarOrderComponent(matcher: OrderComponentMatcher<OrderComponent<NavigationBarComponentId>>, orderContext?: OrderContext): object
```

* * *

### insertNavigationBarOrderComponent()[#](#insertnavigationbarordercomponent)

  

Inserts a component into the render order of the navigation bar.

This method inserts a new navigation bar order component before, after, or to replace a component matching the provided matcher. The matcher can be a function or an object describing the component to match. The location can be ‘before’, ‘after’, or ‘replace’.

The insert API can be used in different contexts (such as edit modes).

#### Parameters[#](#parameters-45)

| Parameter | Type | Description |
| --- | --- | --- |
| `matcher` | [`OrderComponentMatcher`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/ordercomponentmatcher/)<[`OrderComponent`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercomponent/)<[`NavigationBarComponentId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/navigationbarcomponentid/)\>> | Function or object to match the component to insert relative to. |
| `component` |  | [`NavigationBarComponentId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/navigationbarcomponentid/) |
| `location?` | [`InsertOrderComponentLocation`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/insertordercomponentlocation/) | Where to insert the new component relative to the matched component (‘before’ or ‘after’). |
| `orderContext?` | [`OrderContext`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercontext/) | Optional context specifying which order to update. |

#### Returns[#](#returns-50)

`object`

The updated navigation bar order array.

| Name | Type |
| --- | --- |
| `inserted` | `boolean` |
| `order` | [`OrderComponent`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercomponent/)<[`NavigationBarComponentId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/navigationbarcomponentid/)\>\[\] |

#### Signature[#](#signature-43)

```
insertNavigationBarOrderComponent(matcher: OrderComponentMatcher<OrderComponent<NavigationBarComponentId>>, component: NavigationBarComponentId | NavigationBarOrderComponent, location?: InsertOrderComponentLocation, orderContext?: OrderContext): object
```

* * *

### getNavigationBarOrder()[#](#getnavigationbarorder)

  

Gets the current rendering order of navigation bar components.

Component IDs refer to built-in components or those registered via registerComponent. Returns the order for the specified context, or defaults to Transform mode if no context is provided.

#### Parameters[#](#parameters-46)

| Parameter | Type | Description |
| --- | --- | --- |
| `orderContext?` | [`OrderContext`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercontext/) | Optional context specifying which order to retrieve. |

#### Returns[#](#returns-51)

[`OrderComponent`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercomponent/)<[`ComponentId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/componentid/)\>\[\]

Array of component configurations defining the navigation bar order.

#### Signature[#](#signature-44)

```
getNavigationBarOrder(orderContext?: OrderContext): OrderComponent<ComponentId>[]
```

* * *

### setCanvasBarOrder()[#](#setcanvasbarorder)

  

Sets the rendering order of components in the canvas bar.

Component IDs refer to built-in components or those registered via registerComponent. Canvas bars can be positioned at the top or bottom of the canvas. Different orders can be set for different contexts (e.g., Transform or Text edit modes). Defaults to Transform mode if no context is provided.

#### Parameters[#](#parameters-47)

| Parameter | Type | Description |
| --- | --- | --- |
| `canvasBarOrder` | ( | [`CanvasBarComponentId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/canvasbarcomponentid/) |
| `position` | `"top"` | `"bottom"` |
| `orderContext?` | [`OrderContext`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercontext/) | Optional context specifying when this order applies. |

#### Returns[#](#returns-52)

`void`

#### Signature[#](#signature-45)

```
setCanvasBarOrder(canvasBarOrder: CanvasBarComponentId | OrderComponent<CanvasBarComponentId>[], position: "top" | "bottom", orderContext?: OrderContext): void
```

* * *

### getCanvasBarOrder()[#](#getcanvasbarorder)

  

Gets the current rendering order of canvas bar components at the specified position.

Component IDs refer to built-in components or those registered via registerComponent. Returns the order for the specified context, or defaults to Transform mode if no context is provided.

#### Parameters[#](#parameters-48)

| Parameter | Type | Description |
| --- | --- | --- |
| `position` | `"top"` | `"bottom"` |
| `orderContext?` | [`OrderContext`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercontext/) | Optional context specifying which order to retrieve. |

#### Returns[#](#returns-53)

[`OrderComponent`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercomponent/)<[`ComponentId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/componentid/)\>\[\]

Array of component configurations defining the canvas bar order.

#### Signature[#](#signature-46)

```
getCanvasBarOrder(position: "top" | "bottom", orderContext?: OrderContext): OrderComponent<ComponentId>[]
```

* * *

### updateCanvasBarOrderComponent()[#](#updatecanvasbarordercomponent)

  

Updates a component in the render order of the canvas bar.

This method finds a canvas bar order component matching the provided matcher and updates it with the given component, ID, or updater function. The matcher can be a function or an object describing the component to match. The update can be a new ID, a partial object with updated properties, or a function that receives the current component and returns the updated one.

The update API can be used in different contexts (such as edit modes and bar positions).

#### Parameters[#](#parameters-49)

| Parameter | Type | Description |
| --- | --- | --- |
| `matcher` | [`OrderComponentMatcher`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/ordercomponentmatcher/)<[`OrderComponent`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercomponent/)<[`CanvasBarComponentId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/canvasbarcomponentid/)\>> | Function or object to match the component to update. |
| `update` |  | [`CanvasBarComponentId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/canvasbarcomponentid/) |
| `position` | `"top"` | `"bottom"` |
| `orderContext?` | [`OrderContext`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercontext/) | Optional context specifying which order to update. |

#### Returns[#](#returns-54)

`object`

The updated canvas bar order array.

| Name | Type |
| --- | --- |
| `updated` | `number` |
| `order` | [`OrderComponent`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercomponent/)<[`CanvasBarComponentId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/canvasbarcomponentid/)\>\[\] |

#### Signature[#](#signature-47)

```
updateCanvasBarOrderComponent(matcher: OrderComponentMatcher<OrderComponent<CanvasBarComponentId>>, update: CanvasBarComponentId | Partial<OrderComponent<CanvasBarComponentId>> | (component: OrderComponent<CanvasBarComponentId>) => Partial<OrderComponent<CanvasBarComponentId>>, position: "top" | "bottom", orderContext?: OrderContext): object
```

* * *

### removeCanvasBarOrderComponent()[#](#removecanvasbarordercomponent)

  

Removes a component from the render order of the canvas bar.

This method finds a canvas bar order component matching the provided matcher and removes it from the current order. The matcher can be a function or an object describing the component to match.

The remove API can be used in different contexts (such as edit modes and bar positions).

#### Parameters[#](#parameters-50)

| Parameter | Type | Description |
| --- | --- | --- |
| `matcher` | [`OrderComponentMatcher`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/ordercomponentmatcher/)<[`OrderComponent`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercomponent/)<[`CanvasBarComponentId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/canvasbarcomponentid/)\>> | Function or object to match the component to remove. |
| `position` | `"top"` | `"bottom"` |
| `orderContext?` | [`OrderContext`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercontext/) | Optional context specifying which order to update. |

#### Returns[#](#returns-55)

`object`

The updated canvas bar order array.

| Name | Type |
| --- | --- |
| `removed` | `number` |
| `order` | [`OrderComponent`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercomponent/)<[`CanvasBarComponentId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/canvasbarcomponentid/)\>\[\] |

#### Signature[#](#signature-48)

```
removeCanvasBarOrderComponent(matcher: OrderComponentMatcher<OrderComponent<CanvasBarComponentId>>, position: "top" | "bottom", orderContext?: OrderContext): object
```

* * *

### insertCanvasBarOrderComponent()[#](#insertcanvasbarordercomponent)

  

Inserts a component into the render order of the canvas bar.

This method inserts a new canvas bar order component before, after, or to replace a component matching the provided matcher. The matcher can be a function or an object describing the component to match. The location can be ‘before’, ‘after’, or ‘replace’.

The insert API can be used in different contexts (such as edit modes and bar positions).

#### Parameters[#](#parameters-51)

| Parameter | Type | Description |
| --- | --- | --- |
| `matcher` | [`OrderComponentMatcher`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/ordercomponentmatcher/)<[`OrderComponent`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercomponent/)<[`CanvasBarComponentId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/canvasbarcomponentid/)\>> | Function or object to match the component to insert relative to. |
| `component` |  | [`CanvasBarComponentId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/canvasbarcomponentid/) |
| `position` | `"top"` | `"bottom"` |
| `location?` | [`InsertOrderComponentLocation`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/insertordercomponentlocation/) | Where to insert the new component relative to the matched component (‘before’ or ‘after’). |
| `orderContext?` | [`OrderContext`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercontext/) | Optional context specifying which order to update. |

#### Returns[#](#returns-56)

`object`

The updated canvas bar order array.

| Name | Type |
| --- | --- |
| `inserted` | `boolean` |
| `order` | [`OrderComponent`](https://img.ly/docs/cesdk/vue/api/cesdk-js/interfaces/ordercomponent/)<[`CanvasBarComponentId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/canvasbarcomponentid/)\>\[\] |

#### Signature[#](#signature-49)

```
insertCanvasBarOrderComponent(matcher: OrderComponentMatcher<OrderComponent<CanvasBarComponentId>>, component: CanvasBarComponentId | OrderComponent<CanvasBarComponentId>, position: "top" | "bottom", location?: InsertOrderComponentLocation, orderContext?: OrderContext): object
```

* * *

### addIconSet()[#](#addiconset)

  

Adds a custom icon set to the editor interface.

The icon set should be an SVG sprite containing symbol elements. Symbol IDs must start with ’@’ to be recognized by the editor.

**Security Warning**: The SVG sprite is injected into the DOM without sanitization. Only use trusted sources to prevent XSS attacks. Consider using libraries like DOMPurify for untrusted content.

#### Parameters[#](#parameters-52)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `string` | The unique identifier for the icon set. |
| `svgSprite` | `string` | The SVG sprite string containing symbol definitions. |

#### Returns[#](#returns-57)

`void`

#### Signature[#](#signature-50)

```
addIconSet(id: string, svgSprite: string): void
```

## UI Scale Management[#](#ui-scale-management)

### getScale()[#](#getscale)

  

Gets the resolved scale that is currently being used. If the scale configuration is a function, it is evaluated lazily and the result is returned.

#### Returns[#](#returns-58)

[`Scale`](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/configtypes/type-aliases/scale/)

The resolved scale (‘normal’ or ‘large’).

#### Example[#](#example-9)

```
// Get the actual scale being usedconst scale = cesdk.ui.getScale(); // 'normal' or 'large'
// Use for conditional sizingconst fontSize = cesdk.ui.getScale() === 'large' ? '16px' : '14px';
// Scale function is evaluated each time getScale() is calledcesdk.ui.setScale(({ containerWidth }) => containerWidth < 768 ? 'large' : 'normal');const currentScale = cesdk.ui.getScale(); // Function is evaluated here
```

#### Signature[#](#signature-51)

```
getScale(): Scale
```

* * *

### setScale()[#](#setscale)

  

Sets the scale configuration.

This will immediately update the UI to reflect the new scale. Can be set to:

*   ‘normal’ or ‘large’ for a specific scale
*   A function that returns ‘normal’ or ‘large’ based on viewport properties

#### Parameters[#](#parameters-53)

| Parameter | Type | Description |
| --- | --- | --- |
| `scale` | [`ScaleConfig`](https://img.ly/docs/cesdk/vue/api/cesdk-js/documentation/namespaces/configtypes/type-aliases/scaleconfig/) | The scale configuration to set. |

#### Returns[#](#returns-59)

`void`

#### Example[#](#example-10)

```
// Set a specific scalecesdk.ui.setScale('large');
// Set scale based on viewportcesdk.ui.setScale(({ containerWidth, isTouch }) => {  if (isTouch || containerWidth < 768) {    return 'large';  }  return 'normal';});
// Toggle between scalesconst currentScale = cesdk.ui.getScale();const newScale = currentScale === 'normal' ? 'large' : 'normal';cesdk.ui.setScale(newScale);
```

---



[Source](https:/img.ly/docs/cesdk/vue/api/cesdk-js/classes/sceneapi)