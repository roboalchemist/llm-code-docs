# Class: EditorAPI

Control the design editor’s behavior and settings.

The EditorAPI provides access to edit modes, history management, editor settings, color management, resource handling, and global scope controls. It serves as the central configuration and control interface for the design editor engine.

## Constructors[#](#constructors)

### Constructor[#](#constructor)

  

`EditorAPI`

## Role & Scope Management[#](#role--scope-management)

Manage user roles and global scope permissions.

### setRole()[#](#setrole)

  

Set the user role and apply role-dependent defaults.

Automatically configures scopes and settings based on the specified role.

#### Parameters[#](#parameters)

| Parameter | Type | Description |
| --- | --- | --- |
| `role` | [`RoleString`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/rolestring/) | The role to assign to the user. |

#### Returns[#](#returns)

`void`

#### Signature[#](#signature)

```
setRole(role: RoleString): void
```

* * *

### getRole()[#](#getrole)

  

Get the current user role.

#### Returns[#](#returns-1)

[`RoleString`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/rolestring/)

The current role of the user.

#### Signature[#](#signature-1)

```
getRole(): RoleString
```

* * *

### findAllScopes()[#](#findallscopes)

  

Get all available global scope names.

#### Returns[#](#returns-2)

[`Scope`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/scope/)\[\]

The names of all available global scopes.

#### Signature[#](#signature-2)

```
findAllScopes(): Scope[]
```

* * *

### setGlobalScope()[#](#setglobalscope)

  

Set a global scope permission level.

#### Parameters[#](#parameters-1)

| Parameter | Type | Description |
| --- | --- | --- |
| `key` | [`Scope`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/scope/) | The scope to configure. |
| `value` | `"Allow"` | `"Deny"` |

#### Returns[#](#returns-3)

`void`

#### Signature[#](#signature-3)

```
setGlobalScope(key: Scope, value: "Allow" | "Deny" | "Defer"): void
```

* * *

### getGlobalScope()[#](#getglobalscope)

  

Get a global scope’s permission level.

#### Parameters[#](#parameters-2)

| Parameter | Type | Description |
| --- | --- | --- |
| `key` | [`Scope`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/scope/) | The scope to query. |

#### Returns[#](#returns-4)

`"Allow"` | `"Deny"` | `"Defer"`

`Allow`, `Deny`, or `Defer` indicating the scope’s permission level.

#### Signature[#](#signature-4)

```
getGlobalScope(key: Scope): "Allow" | "Deny" | "Defer"
```

## Event Subscriptions[#](#event-subscriptions)

Subscribe to editor state changes, history updates, and role changes.

### onStateChanged()[#](#onstatechanged)

  

Subscribe to editor state changes.

#### Parameters[#](#parameters-3)

| Parameter | Type | Description |
| --- | --- | --- |
| `callback` | () => `void` | Function called when the editor state changes. |

#### Returns[#](#returns-5)

A method to unsubscribe from the event.

```
(): void;
```

##### Returns[#](#returns-6)

`void`

* * *

### onHistoryUpdated()[#](#onhistoryupdated)

  

Subscribe to undo/redo history changes.

```
const unsubscribe = engine.editor.onHistoryUpdated(() => {  const canUndo = engine.editor.canUndo();  const canRedo = engine.editor.canRedo();  console.log("History updated", {canUndo, canRedo});})
```

#### Parameters[#](#parameters-4)

| Parameter | Type | Description |
| --- | --- | --- |
| `callback` | () => `void` | Function called when the undo/redo history changes. |

#### Returns[#](#returns-7)

A method to unsubscribe from the event.

```
(): void;
```

##### Returns[#](#returns-8)

`void`

* * *

### onSettingsChanged()[#](#onsettingschanged)

  

Subscribe to editor settings changes.

#### Parameters[#](#parameters-5)

| Parameter | Type | Description |
| --- | --- | --- |
| `callback` | () => `void` | Function called when editor settings change. |

#### Returns[#](#returns-9)

A method to unsubscribe from the event.

```
(): void;
```

##### Returns[#](#returns-10)

`void`

* * *

### onRoleChanged()[#](#onrolechanged)

  

Subscribe to editor role changes.

Allows reacting to role changes and updating engine settings accordingly. The callback is triggered immediately after role changes and default settings are applied.

#### Parameters[#](#parameters-6)

| Parameter | Type | Description |
| --- | --- | --- |
| `callback` | (`role`) => `void` | Function called when the user role changes. |

#### Returns[#](#returns-11)

A method to unsubscribe from the event.

```
(): void;
```

##### Returns[#](#returns-12)

`void`

## Edit Mode Management[#](#edit-mode-management)

Control the editor’s current editing mode and interaction state.

### setEditMode()[#](#seteditmode)

  

Set the editor’s current edit mode.

Edit modes represent different tools or interaction states within the editor. Common ones, are “Crop” while the crop tool is shown or “Text” when inline-editing text.

```
engine.editor.setEditMode('Crop');// With a base modeengine.editor.setEditMode('CustomMode', 'Crop');
```

#### Parameters[#](#parameters-7)

| Parameter | Type | Description |
| --- | --- | --- |
| `mode` | [`EditMode`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/editmode/) | ”Transform”, “Crop”, “Text”, “Playback”, “Trim” or a custom value. |
| `baseMode?` | `string` | Optional base mode from which the custom mode will inherit the settings. |

#### Returns[#](#returns-13)

`void`

#### Signature[#](#signature-5)

```
setEditMode(mode: EditMode, baseMode?: string): void
```

* * *

### getEditMode()[#](#geteditmode)

  

Get the editor’s current edit mode.

Edit modes represent different tools or interaction states within the editor. Common ones, are “Crop” while the crop tool is shown or “Text” when inline-editing text.

#### Returns[#](#returns-14)

[`EditMode`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/editmode/)

“Transform”, “Crop”, “Text”, “Playback”, “Trim” or a custom value.

#### Signature[#](#signature-6)

```
getEditMode(): EditMode
```

* * *

### getCursorType()[#](#getcursortype)

  

Get the cursor type that should be displayed.

#### Returns[#](#returns-15)

`"Text"` | `"Arrow"` | `"Move"` | `"MoveNotPermitted"` | `"Resize"` | `"Rotate"`

The cursor type.

#### Signature[#](#signature-7)

```
getCursorType(): "Text" | "Arrow" | "Move" | "MoveNotPermitted" | "Resize" | "Rotate"
```

* * *

### getCursorRotation()[#](#getcursorrotation)

  

Get the cursor rotation angle.

#### Returns[#](#returns-16)

`number`

The angle in radians.

#### Signature[#](#signature-8)

```
getCursorRotation(): number
```

* * *

### getTextCursorPositionInScreenSpaceX()[#](#gettextcursorpositioninscreenspacex)

  

Get the text cursor’s x position in screen space.

#### Returns[#](#returns-17)

`number`

The text cursor’s x position in screen space.

#### Signature[#](#signature-9)

```
getTextCursorPositionInScreenSpaceX(): number
```

* * *

### getTextCursorPositionInScreenSpaceY()[#](#gettextcursorpositioninscreenspacey)

  

Get the text cursor’s y position in screen space.

#### Returns[#](#returns-18)

`number`

The text cursor’s y position in screen space.

#### Signature[#](#signature-10)

```
getTextCursorPositionInScreenSpaceY(): number
```

## History Management[#](#history-management)

Create, manage, and operate on undo/redo history stacks.

### createHistory()[#](#createhistory)

  

Create a new undo/redo history stack.

Multiple histories can exist, but only one can be active at a time.

```
const newHistory = engine.editor.createHistory();
```

#### Returns[#](#returns-19)

`number`

The handle of the created history.

#### Signature[#](#signature-11)

```
createHistory(): number
```

* * *

### destroyHistory()[#](#destroyhistory)

  

Destroy a history stack and free its resources.

```
engine.editor.destroyHistory(oldHistory);
```

#### Parameters[#](#parameters-8)

| Parameter | Type | Description |
| --- | --- | --- |
| `history` | `number` | The history handle to destroy. |

#### Returns[#](#returns-20)

`void`

#### Throws[#](#throws)

Error if the handle doesn’t refer to a valid history.

#### Signature[#](#signature-12)

```
destroyHistory(history: number): void
```

* * *

### setActiveHistory()[#](#setactivehistory)

  

Set a history as the active undo/redo stack.

All other histories lose their active state. Undo/redo operations only apply to the active history.

```
engine.editor.setActiveHistory(newHistory);
```

#### Parameters[#](#parameters-9)

| Parameter | Type | Description |
| --- | --- | --- |
| `history` | `number` | The history handle to make active. |

#### Returns[#](#returns-21)

`void`

#### Throws[#](#throws-1)

Error if the handle doesn’t refer to a valid history.

#### Signature[#](#signature-13)

```
setActiveHistory(history: number): void
```

* * *

### getActiveHistory()[#](#getactivehistory)

  

Get the currently active history handle.

Creates a new history if none exists.

```
const oldHistory = engine.editor.getActiveHistory();
```

#### Returns[#](#returns-22)

`number`

The handle of the active history.

#### Signature[#](#signature-14)

```
getActiveHistory(): number
```

* * *

### addUndoStep()[#](#addundostep)

  

Add a new history state to the undo stack.

Only adds a state if undoable changes were made since the last undo step.

```
  engine.editor.addUndoStep();
```

#### Returns[#](#returns-23)

`void`

#### Signature[#](#signature-15)

```
addUndoStep(): void
```

* * *

### removeUndoStep()[#](#removeundostep)

  

Remove the last history state from the undo stack.

Removes the most recent undo step if available.

```
  engine.editor.removeUndoStep();
```

#### Returns[#](#returns-24)

`void`

#### Signature[#](#signature-16)

```
removeUndoStep(): void
```

* * *

### undo()[#](#undo)

  

Undo one step in the active history if an undo step is available.

```
engine.editor.undo();
```

#### Returns[#](#returns-25)

`void`

#### Signature[#](#signature-17)

```
undo(): void
```

* * *

### redo()[#](#redo)

  

Redo one step in the active history if a redo step is available.

```
engine.editor.redo();
```

#### Returns[#](#returns-26)

`void`

#### Signature[#](#signature-18)

```
redo(): void
```

* * *

### canUndo()[#](#canundo)

  

Check if an undo step is available.

```
if (engine.editor.canUndo()) {  engine.editor.undo();}
```

#### Returns[#](#returns-27)

`boolean`

True if an undo step is available.

#### Signature[#](#signature-19)

```
canUndo(): boolean
```

* * *

### canRedo()[#](#canredo)

  

Check if a redo step is available.

```
if (engine.editor.canRedo()) {  engine.editor.redo();}
```

#### Returns[#](#returns-28)

`boolean`

True if a redo step is available.

#### Signature[#](#signature-20)

```
canRedo(): boolean
```

## Color Management[#](#color-management)

Handle spot colors, color conversion, and color space operations.

### findAllSpotColors()[#](#findallspotcolors)

  

Get all spot color names currently defined.

#### Returns[#](#returns-29)

`string`\[\]

The names of all defined spot colors.

#### Signature[#](#signature-21)

```
findAllSpotColors(): string[]
```

* * *

### getSpotColorRGBA()[#](#getspotcolorrgba)

  

Queries the RGB representation set for a spot color.

If the value of the queried spot color has not been set yet, returns the default RGB representation (of magenta). The alpha value is always 1.0.

#### Parameters[#](#parameters-10)

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | The name of a spot color. |

#### Returns[#](#returns-30)

[`RGBA`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/rgba/)

A result holding a float array of the four color components.

#### Signature[#](#signature-22)

```
getSpotColorRGBA(name: string): RGBA
```

* * *

### getSpotColorCMYK()[#](#getspotcolorcmyk)

  

Queries the CMYK representation set for a spot color.

If the value of the queried spot color has not been set yet, returns the default CMYK representation (of magenta).

#### Parameters[#](#parameters-11)

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | The name of a spot color. |

#### Returns[#](#returns-31)

[`CMYK`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/cmyk/)

A result holding a float array of the four color components.

#### Signature[#](#signature-23)

```
getSpotColorCMYK(name: string): CMYK
```

* * *

### setSpotColorRGB()[#](#setspotcolorrgb)

  

Sets the RGB representation of a spot color.

Use this function to both create a new spot color or update an existing spot color.

#### Parameters[#](#parameters-12)

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | The name of a spot color. |
| `r` | `number` | The red color component in the range of 0 to 1. |
| `g` | `number` | The green color component in the range of 0 to 1. |
| `b` | `number` | The blue color component in the range of 0 to 1. |

#### Returns[#](#returns-32)

`void`

#### Signature[#](#signature-24)

```
setSpotColorRGB(name: string, r: number, g: number, b: number): void
```

* * *

### setSpotColorCMYK()[#](#setspotcolorcmyk)

  

Sets the CMYK representation of a spot color.

Use this function to both create a new spot color or update an existing spot color.

#### Parameters[#](#parameters-13)

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | The name of a spot color. |
| `c` | `number` | The cyan color component in the range of 0 to 1. |
| `m` | `number` | The magenta color component in the range of 0 to 1. |
| `y` | `number` | The yellow color component in the range of 0 to 1. |
| `k` | `number` | The key color component in the range of 0 to 1. |

#### Returns[#](#returns-33)

`void`

#### Signature[#](#signature-25)

```
setSpotColorCMYK(name: string, c: number, m: number, y: number, k: number): void
```

* * *

### removeSpotColor()[#](#removespotcolor)

  

Removes a spot color from the list of set spot colors.

#### Parameters[#](#parameters-14)

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | The name of a spot color. |

#### Returns[#](#returns-34)

`void`

An empty result on success, an error otherwise.

#### Signature[#](#signature-26)

```
removeSpotColor(name: string): void
```

* * *

### setSpotColorForCutoutType()[#](#setspotcolorforcutouttype)

  

Set the spot color assign to a cutout type.

All cutout blocks of the given type will be immediately assigned that spot color.

#### Parameters[#](#parameters-15)

| Parameter | Type | Description |
| --- | --- | --- |
| `type` | `"Dashed"` | `"Solid"` |
| `color` | `string` | The spot color name to assign. |

#### Returns[#](#returns-35)

`void`

#### Signature[#](#signature-27)

```
setSpotColorForCutoutType(type: "Dashed" | "Solid", color: string): void
```

* * *

### getSpotColorForCutoutType()[#](#getspotcolorforcutouttype)

  

Get the name of the spot color assigned to a cutout type.

#### Parameters[#](#parameters-16)

| Parameter | Type | Description |
| --- | --- | --- |
| `type` | `"Dashed"` | `"Solid"` |

#### Returns[#](#returns-36)

`string`

The color spot name.

#### Signature[#](#signature-28)

```
getSpotColorForCutoutType(type: "Dashed" | "Solid"): string
```

* * *

### convertColorToColorSpace()[#](#convertcolortocolorspace)

  

Converts a color to the given color space.

##### Parameters[#](#parameters-17)

| Parameter | Type | Description |
| --- | --- | --- |
| `color` | [`Color`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/color/) | The color to convert. |
| `colorSpace` | `"sRGB"` | The color space to convert to. |

##### Returns[#](#returns-37)

[`RGBAColor`](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/rgbacolor/)

The converted color.

#### Call Signature[#](#call-signature)

```
convertColorToColorSpace(color, colorSpace): CMYKColor;
```

##### Parameters[#](#parameters-18)

| Parameter | Type |
| --- | --- |
| `color` | [`Color`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/color/) |
| `colorSpace` | `"CMYK"` |

##### Returns[#](#returns-38)

[`CMYKColor`](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/cmykcolor/)

#### Call Signature[#](#call-signature-1)

```
convertColorToColorSpace(color, colorSpace): never;
```

##### Parameters[#](#parameters-19)

| Parameter | Type |
| --- | --- |
| `color` | [`Color`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/color/) |
| `colorSpace` | [`ColorSpace`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/colorspace/) |

##### Returns[#](#returns-39)

`never`

#### Signatures[#](#signatures)

```
convertColorToColorSpace(color: Color, colorSpace: "sRGB"): RGBAColor
```

```
convertColorToColorSpace(color: Color, colorSpace: "CMYK"): CMYKColor
```

```
convertColorToColorSpace(color: Color, colorSpace: ColorSpace): never
```

## Resource Management[#](#resource-management)

Manage buffers, URIs, and resource data handling.

### createBuffer()[#](#createbuffer)

  

Create a resizable buffer for arbitrary data.

```
const buffer = engine.editor.createBuffer();
// Reference the buffer resource from the audio blockengine.block.setString(audioBlock, 'audio/fileURI', buffer);
```

#### Returns[#](#returns-40)

`string`

A URI to identify the created buffer.

#### Signature[#](#signature-29)

```
createBuffer(): string
```

* * *

### destroyBuffer()[#](#destroybuffer)

  

Destroy a buffer and free its resources.

```
engine.editor.destroyBuffer(buffer);
```

#### Parameters[#](#parameters-20)

| Parameter | Type | Description |
| --- | --- | --- |
| `uri` | `string` | The URI of the buffer to destroy. |

#### Returns[#](#returns-41)

`void`

#### Signature[#](#signature-30)

```
destroyBuffer(uri: string): void
```

* * *

### setBufferData()[#](#setbufferdata)

  

Set the data of a buffer at a given offset.

```
// Generate 10 seconds of stereo 48 kHz audio dataconst samples = new Float32Array(10 * 2 * 48000);for (let i = 0; i < samples.length; i += 2) {  samples[i] = samples[i + 1] = Math.sin((440 * i * Math.PI) / 48000);}// Assign the audio data to the bufferengine.editor.setBufferData(buffer, 0, new Uint8Array(samples.buffer));
```

#### Parameters[#](#parameters-21)

| Parameter | Type | Description |
| --- | --- | --- |
| `uri` | `string` | The URI of the buffer to update. |
| `offset` | `number` | The offset in bytes at which to start writing. |
| `data` | `Uint8Array` | The data to write. |

#### Returns[#](#returns-42)

`void`

#### Signature[#](#signature-31)

```
setBufferData(uri: string, offset: number, data: Uint8Array): void
```

* * *

### getBufferData()[#](#getbufferdata)

  

Get the data of a buffer at a given offset.

```
engine.editor.findAllTransientResources().forEach((resource) => {  const bufferURI = resource.URL;  const length = engine.editor.getBufferLength(buffer);  const data = engine.editor.getBufferData(buffer, 0, length);  const blob = new Blob([data]);})
```

#### Parameters[#](#parameters-22)

| Parameter | Type | Description |
| --- | --- | --- |
| `uri` | `string` | The URI of the buffer to query. |
| `offset` | `number` | The offset in bytes at which to start reading. |
| `length` | `number` | The number of bytes to read. |

#### Returns[#](#returns-43)

`Uint8Array`

The data at the given offset.

#### Signature[#](#signature-32)

```
getBufferData(uri: string, offset: number, length: number): Uint8Array
```

* * *

### setBufferLength()[#](#setbufferlength)

  

Set the length of a buffer.

```
// Reduce the buffer to half its lengthconst currentLength = engine.editor.getBufferLength(buffer);engine.editor.setBufferLength(buffer, currentLength / 2);
```

#### Parameters[#](#parameters-23)

| Parameter | Type | Description |
| --- | --- | --- |
| `uri` | `string` | The URI of the buffer to update. |
| `length` | `number` | The new length of the buffer in bytes. |

#### Returns[#](#returns-44)

`void`

#### Signature[#](#signature-33)

```
setBufferLength(uri: string, length: number): void
```

* * *

### getBufferLength()[#](#getbufferlength)

  

Get the length of a buffer.

```
const length = engine.editor.getBufferLength(buffer);
```

#### Parameters[#](#parameters-24)

| Parameter | Type | Description |
| --- | --- | --- |
| `uri` | `string` | The URI of the buffer to query. |

#### Returns[#](#returns-45)

`number`

The length of the buffer in bytes.

#### Signature[#](#signature-34)

```
getBufferLength(uri: string): number
```

* * *

### getMimeType()[#](#getmimetype)

  

Get the MIME type of a resource.

Downloads the resource if not already cached.

#### Parameters[#](#parameters-25)

| Parameter | Type | Description |
| --- | --- | --- |
| `uri` | `string` | The URI of the resource. |

#### Returns[#](#returns-46)

`Promise`<`string`\>

Promise resolving to the resource’s MIME type.

#### Throws[#](#throws-2)

Error if the resource cannot be downloaded or MIME type determined.

#### Signature[#](#signature-35)

```
getMimeType(uri: string): Promise<string>
```

* * *

### findAllTransientResources()[#](#findalltransientresources)

  

Get all transient resources that would be lost during export.

Useful for identifying resources that need relocation (e.g., to a CDN) before export, as these resources are not included in the exported scene.

#### Returns[#](#returns-47)

[`TransientResource`](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/transientresource/)\[\]

The URLs and sizes of transient resources.

#### Signature[#](#signature-36)

```
findAllTransientResources(): TransientResource[]
```

* * *

### findAllMediaURIs()[#](#findallmediauris)

  

Get all media URIs referenced by blocks in the scene.

Returns URIs from image fills, video fills, and audio blocks, including their source sets. Only returns valid media URIs (http://, https://, file://), excluding transient resources like buffer URIs. Useful for determining which media files are referenced by a scene (e.g., for cleanup operations, CDN management, or file system tracking).

#### Returns[#](#returns-48)

`string`\[\]

The URLs of all media resources referenced in the scene, deduplicated.

#### Signature[#](#signature-37)

```
findAllMediaURIs(): string[]
```

* * *

### getResourceData()[#](#getresourcedata)

  

Provides the data of a resource at the given URL.

#### Parameters[#](#parameters-26)

| Parameter | Type | Description |
| --- | --- | --- |
| `uri` | `string` | The URL of the resource. |
| `chunkSize` | `number` | The size of the chunks in which the resource data is provided. |
| `onData` | (`result`) => `boolean` | The callback function that is called with the resource data or an error if an error occurred. The callback will be called as long as there is data left to provide and the callback returns `true`. |

#### Returns[#](#returns-49)

`void`

#### Signature[#](#signature-38)

```
getResourceData(uri: string, chunkSize: number, onData: (result: Uint8Array) => boolean): void
```

* * *

### relocateResource()[#](#relocateresource)

  

Changes the URL associated with a resource.

This function can be used change the URL of a resource that has been relocated (e.g., to a CDN).

#### Parameters[#](#parameters-27)

| Parameter | Type | Description |
| --- | --- | --- |
| `currentUrl` | `string` | The current URL of the resource. |
| `relocatedUrl` | `string` | The new URL of the resource. |

#### Returns[#](#returns-50)

`void`

#### Signature[#](#signature-39)

```
relocateResource(currentUrl: string, relocatedUrl: string): void
```

## Editor Settings[#](#editor-settings)

Configure editor behavior through typed settings for different data types.

### setSetting()[#](#setsetting)

  

Set a setting value using the unified API. The value type is automatically validated based on the key.

#### Type Parameters[#](#type-parameters)

| Type Parameter |
| --- |
| `K` _extends_ keyof [`Settings`](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/settings/) |

#### Parameters[#](#parameters-28)

| Parameter | Type | Description |
| --- | --- | --- |
| `keypath` | [`OptionalPrefix`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/optionalprefix/)<`K`\> | The setting key from Settings |
| `value` | [`SettingValueType`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/settingvaluetype/)<`K`\> | The value to set (type-safe based on key) |

#### Returns[#](#returns-51)

`void`

#### Throws[#](#throws-3)

Error if the keypath is invalid or value type doesn’t match

#### Example[#](#example)

```
// Boolean settingengine.editor.setSetting('doubleClickToCropEnabled', false);
// Color settingengine.editor.setSetting('highlightColor', { r: 1, g: 0, b: 1, a: 1 });
// Enum settingengine.editor.setSetting('doubleClickSelectionMode', 'Direct');
```

#### Signature[#](#signature-40)

```
setSetting(keypath: OptionalPrefix<K>, value: SettingValueType<K>): void
```

* * *

### getSetting()[#](#getsetting)

  

Get a setting value using the unified API. The return type is automatically inferred from the key.

#### Type Parameters[#](#type-parameters-1)

| Type Parameter |
| --- |
| `K` _extends_ keyof [`Settings`](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/settings/) |

#### Parameters[#](#parameters-29)

| Parameter | Type | Description |
| --- | --- | --- |
| `keypath` | [`OptionalPrefix`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/optionalprefix/)<`K`\> | The setting key from Settings |

#### Returns[#](#returns-52)

[`SettingValueType`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/settingvaluetype/)<`K`\>

The value of the setting (type-safe based on key)

#### Throws[#](#throws-4)

Error if the keypath is invalid

#### Example[#](#example-1)

```
// Boolean settingconst cropEnabled = engine.editor.getSetting('doubleClickToCropEnabled');
// Color settingconst highlight = engine.editor.getSetting('highlightColor');
// Enum settingconst selectionMode = engine.editor.getSetting('doubleClickSelectionMode');
```

#### Signature[#](#signature-41)

```
getSetting(keypath: OptionalPrefix<K>): SettingValueType<K>
```

* * *

### setSettingBool()[#](#setsettingbool)

  

Set a boolean setting value.

##### Parameters[#](#parameters-30)

| Parameter | Type | Description |
| --- | --- | --- |
| `keypath` | [`SettingBoolPropertyName`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/settingboolpropertyname/) | The settings keypath, e.g. `doubleClickToCropEnabled`. |
| `value` | `boolean` | The boolean value to set. |

##### Returns[#](#returns-53)

`void`

##### Throws[#](#throws-5)

Error if the keypath is invalid.

#### Call Signature[#](#call-signature-2)

```
setSettingBool(keypath, value): void;
```

##### Parameters[#](#parameters-31)

| Parameter | Type |
| --- | --- |
| `keypath` | `` `ubq://${string & {}}` `` |
| `value` | `boolean` |

##### Returns[#](#returns-54)

`void`

##### Deprecated[#](#deprecated)

Support for `ubq://` prefixed keypaths will be removed in a future release.

#### Signatures[#](#signatures-1)

```
setSettingBool(keypath: SettingBoolPropertyName, value: boolean): void
```

```
setSettingBool(keypath: `ubq://${string & {}}`, value: boolean): void
```

* * *

### getSettingBool()[#](#getsettingbool)

  

Get a boolean setting value.

##### Parameters[#](#parameters-32)

| Parameter | Type | Description |
| --- | --- | --- |
| `keypath` | [`SettingBoolPropertyName`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/settingboolpropertyname/) | The settings keypath, e.g. `doubleClickToCropEnabled`. |

##### Returns[#](#returns-55)

`boolean`

The boolean value of the setting.

##### Throws[#](#throws-6)

Error if the keypath is invalid.

#### Call Signature[#](#call-signature-3)

```
getSettingBool(keypath): boolean;
```

##### Parameters[#](#parameters-33)

| Parameter | Type |
| --- | --- |
| `keypath` | `` `ubq://${string & {}}` `` |

##### Returns[#](#returns-56)

`boolean`

##### Deprecated[#](#deprecated-1)

Support for `ubq://` prefixed keypaths will be removed in a future release.

#### Call Signature[#](#call-signature-4)

```
getSettingBool(keypath): boolean;
```

Get a boolean setting value.

##### Parameters[#](#parameters-34)

| Parameter | Type | Description |
| --- | --- | --- |
| `keypath` | [`SettingBoolPropertyName`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/settingboolpropertyname/) | The settings keypath, e.g. `doubleClickToCropEnabled`. |

##### Returns[#](#returns-57)

`boolean`

The boolean value of the setting.

##### Throws[#](#throws-7)

Error if the keypath is invalid.

#### Signatures[#](#signatures-2)

```
getSettingBool(keypath: SettingBoolPropertyName): boolean
```

```
getSettingBool(keypath: `ubq://${string & {}}`): boolean
```

```
getSettingBool(keypath: SettingBoolPropertyName): boolean
```

* * *

### setSettingInt()[#](#setsettingint)

  

Set an integer setting value.

##### Parameters[#](#parameters-35)

| Parameter | Type | Description |
| --- | --- | --- |
| `keypath` | [`SettingIntPropertyName`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/settingintpropertyname/) | The settings keypath. |
| `value` | `number` | The integer value to set. |

##### Returns[#](#returns-58)

`void`

##### Throws[#](#throws-8)

Error if the keypath is invalid.

#### Call Signature[#](#call-signature-5)

```
setSettingInt(keypath, value): void;
```

Set an integer setting value.

##### Parameters[#](#parameters-36)

| Parameter | Type | Description |
| --- | --- | --- |
| `keypath` | [`SettingIntPropertyName`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/settingintpropertyname/) | The settings keypath. |
| `value` | `number` | The integer value to set. |

##### Returns[#](#returns-59)

`void`

##### Throws[#](#throws-9)

Error if the keypath is invalid.

#### Signatures[#](#signatures-3)

```
setSettingInt(keypath: SettingIntPropertyName, value: number): void
```

```
setSettingInt(keypath: SettingIntPropertyName, value: number): void
```

* * *

### getSettingInt()[#](#getsettingint)

  

Get an integer setting value.

##### Parameters[#](#parameters-37)

| Parameter | Type | Description |
| --- | --- | --- |
| `keypath` | [`SettingIntPropertyName`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/settingintpropertyname/) | The settings keypath. |

##### Returns[#](#returns-60)

`number`

The integer value of the setting.

##### Throws[#](#throws-10)

Error if the keypath is invalid.

#### Call Signature[#](#call-signature-6)

```
getSettingInt(keypath): number;
```

Get an integer setting value.

##### Parameters[#](#parameters-38)

| Parameter | Type | Description |
| --- | --- | --- |
| `keypath` | [`SettingIntPropertyName`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/settingintpropertyname/) | The settings keypath. |

##### Returns[#](#returns-61)

`number`

The integer value of the setting.

##### Throws[#](#throws-11)

Error if the keypath is invalid.

#### Signatures[#](#signatures-4)

```
getSettingInt(keypath: SettingIntPropertyName): number
```

```
getSettingInt(keypath: SettingIntPropertyName): number
```

* * *

### setSettingFloat()[#](#setsettingfloat)

  

Set a float setting value.

##### Parameters[#](#parameters-39)

| Parameter | Type | Description |
| --- | --- | --- |
| `keypath` | [`SettingFloatPropertyName`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/settingfloatpropertyname/) | The settings keypath, e.g. `positionSnappingThreshold`. |
| `value` | `number` | The float value to set. |

##### Returns[#](#returns-62)

`void`

##### Throws[#](#throws-12)

Error if the keypath is invalid.

#### Call Signature[#](#call-signature-7)

```
setSettingFloat(keypath, value): void;
```

##### Parameters[#](#parameters-40)

| Parameter | Type |
| --- | --- |
| `keypath` | `` `ubq://${string & {}}` `` |
| `value` | `number` |

##### Returns[#](#returns-63)

`void`

##### Deprecated[#](#deprecated-2)

Support for `ubq://` prefixed keypaths will be removed in a future release.

#### Call Signature[#](#call-signature-8)

```
setSettingFloat(keypath, value): void;
```

Set a float setting value.

##### Parameters[#](#parameters-41)

| Parameter | Type | Description |
| --- | --- | --- |
| `keypath` | [`SettingFloatPropertyName`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/settingfloatpropertyname/) | The settings keypath, e.g. `positionSnappingThreshold`. |
| `value` | `number` | The float value to set. |

##### Returns[#](#returns-64)

`void`

##### Throws[#](#throws-13)

Error if the keypath is invalid.

#### Signatures[#](#signatures-5)

```
setSettingFloat(keypath: SettingFloatPropertyName, value: number): void
```

```
setSettingFloat(keypath: `ubq://${string & {}}`, value: number): void
```

```
setSettingFloat(keypath: SettingFloatPropertyName, value: number): void
```

* * *

### getSettingFloat()[#](#getsettingfloat)

  

Get a float setting value.

##### Parameters[#](#parameters-42)

| Parameter | Type | Description |
| --- | --- | --- |
| `keypath` | [`SettingFloatPropertyName`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/settingfloatpropertyname/) | The settings keypath, e.g. `positionSnappingThreshold`. |

##### Returns[#](#returns-65)

`number`

The float value of the setting.

##### Throws[#](#throws-14)

Error if the keypath is invalid.

#### Call Signature[#](#call-signature-9)

```
getSettingFloat(keypath): number;
```

##### Parameters[#](#parameters-43)

| Parameter | Type |
| --- | --- |
| `keypath` | `` `ubq://${string & {}}` `` |

##### Returns[#](#returns-66)

`number`

##### Deprecated[#](#deprecated-3)

Support for `ubq://` prefixed keypaths will be removed in a future release.

#### Call Signature[#](#call-signature-10)

```
getSettingFloat(keypath): number;
```

Get a float setting value.

##### Parameters[#](#parameters-44)

| Parameter | Type | Description |
| --- | --- | --- |
| `keypath` | [`SettingFloatPropertyName`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/settingfloatpropertyname/) | The settings keypath, e.g. `positionSnappingThreshold`. |

##### Returns[#](#returns-67)

`number`

The float value of the setting.

##### Throws[#](#throws-15)

Error if the keypath is invalid.

#### Signatures[#](#signatures-6)

```
getSettingFloat(keypath: SettingFloatPropertyName): number
```

```
getSettingFloat(keypath: `ubq://${string & {}}`): number
```

```
getSettingFloat(keypath: SettingFloatPropertyName): number
```

* * *

### setSettingString()[#](#setsettingstring)

  

Set a string setting value.

##### Parameters[#](#parameters-45)

| Parameter | Type | Description |
| --- | --- | --- |
| `keypath` | [`SettingStringPropertyName`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/settingstringpropertyname/) | The settings keypath, e.g. `license`. |
| `value` | `string` | The string value to set. |

##### Returns[#](#returns-68)

`void`

##### Throws[#](#throws-16)

Error if the keypath is invalid.

#### Call Signature[#](#call-signature-11)

```
setSettingString(keypath, value): void;
```

##### Parameters[#](#parameters-46)

| Parameter | Type |
| --- | --- |
| `keypath` | `` `ubq://${string & {}}` `` |
| `value` | `string` |

##### Returns[#](#returns-69)

`void`

##### Deprecated[#](#deprecated-4)

Support for `ubq://` prefixed keypaths will be removed in a future release.

#### Call Signature[#](#call-signature-12)

```
setSettingString(keypath, value): void;
```

Set a string setting value.

##### Parameters[#](#parameters-47)

| Parameter | Type | Description |
| --- | --- | --- |
| `keypath` | [`SettingStringPropertyName`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/settingstringpropertyname/) | The settings keypath, e.g. `license`. |
| `value` | `string` | The string value to set. |

##### Returns[#](#returns-70)

`void`

##### Throws[#](#throws-17)

Error if the keypath is invalid.

#### Signatures[#](#signatures-7)

```
setSettingString(keypath: SettingStringPropertyName, value: string): void
```

```
setSettingString(keypath: `ubq://${string & {}}`, value: string): void
```

```
setSettingString(keypath: SettingStringPropertyName, value: string): void
```

* * *

### getSettingString()[#](#getsettingstring)

  

Get a string setting value.

##### Parameters[#](#parameters-48)

| Parameter | Type | Description |
| --- | --- | --- |
| `keypath` | [`SettingStringPropertyName`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/settingstringpropertyname/) | The settings keypath, e.g. `license`. |

##### Returns[#](#returns-71)

`string`

The string value of the setting.

##### Throws[#](#throws-18)

Error if the keypath is invalid.

#### Call Signature[#](#call-signature-13)

```
getSettingString(keypath): string;
```

##### Parameters[#](#parameters-49)

| Parameter | Type |
| --- | --- |
| `keypath` | `` `ubq://${string & {}}` `` |

##### Returns[#](#returns-72)

`string`

##### Deprecated[#](#deprecated-5)

Support for `ubq://` prefixed keypaths will be removed in a future release.

#### Call Signature[#](#call-signature-14)

```
getSettingString(keypath): string;
```

Get a string setting value.

##### Parameters[#](#parameters-50)

| Parameter | Type | Description |
| --- | --- | --- |
| `keypath` | [`SettingStringPropertyName`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/settingstringpropertyname/) | The settings keypath, e.g. `license`. |

##### Returns[#](#returns-73)

`string`

The string value of the setting.

##### Throws[#](#throws-19)

Error if the keypath is invalid.

#### Signatures[#](#signatures-8)

```
getSettingString(keypath: SettingStringPropertyName): string
```

```
getSettingString(keypath: `ubq://${string & {}}`): string
```

```
getSettingString(keypath: SettingStringPropertyName): string
```

* * *

### setSettingColor()[#](#setsettingcolor)

  

Set a color setting.

##### Parameters[#](#parameters-51)

| Parameter | Type | Description |
| --- | --- | --- |
| `keypath` | [`SettingColorPropertyName`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/settingcolorpropertyname/) | The settings keypath, e.g. `highlightColor`. |
| `value` | [`Color`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/color/) | The The value to set. |

##### Returns[#](#returns-74)

`void`

#### Call Signature[#](#call-signature-15)

```
setSettingColor(keypath, value): void;
```

##### Parameters[#](#parameters-52)

| Parameter | Type |
| --- | --- |
| `keypath` | `` `ubq://${string & {}}` `` |
| `value` | [`Color`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/color/) |

##### Returns[#](#returns-75)

`void`

##### Deprecated[#](#deprecated-6)

Support for `ubq://` prefixed keypaths will be removed in a future release.

#### Call Signature[#](#call-signature-16)

```
setSettingColor(keypath, value): void;
```

Set a color setting.

##### Parameters[#](#parameters-53)

| Parameter | Type | Description |
| --- | --- | --- |
| `keypath` | [`SettingColorPropertyName`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/settingcolorpropertyname/) | The settings keypath, e.g. `highlightColor`. |
| `value` | [`Color`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/color/) | The The value to set. |

##### Returns[#](#returns-76)

`void`

#### Signatures[#](#signatures-9)

```
setSettingColor(keypath: SettingColorPropertyName, value: Color): void
```

```
setSettingColor(keypath: `ubq://${string & {}}`, value: Color): void
```

```
setSettingColor(keypath: SettingColorPropertyName, value: Color): void
```

* * *

### getSettingColor()[#](#getsettingcolor)

  

Get a color setting.

##### Parameters[#](#parameters-54)

| Parameter | Type | Description |
| --- | --- | --- |
| `keypath` | [`SettingColorPropertyName`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/settingcolorpropertyname/) | The settings keypath, e.g. `highlightColor`. |

##### Returns[#](#returns-77)

[`Color`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/color/)

##### Throws[#](#throws-20)

An error, if the keypath is invalid.

#### Call Signature[#](#call-signature-17)

```
getSettingColor(keypath): Color;
```

##### Parameters[#](#parameters-55)

| Parameter | Type |
| --- | --- |
| `keypath` | `` `ubq://${string & {}}` `` |

##### Returns[#](#returns-78)

[`Color`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/color/)

##### Deprecated[#](#deprecated-7)

Support for `ubq://` prefixed keypaths will be removed in a future release.

#### Call Signature[#](#call-signature-18)

```
getSettingColor(keypath): Color;
```

Get a color setting.

##### Parameters[#](#parameters-56)

| Parameter | Type | Description |
| --- | --- | --- |
| `keypath` | [`SettingColorPropertyName`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/settingcolorpropertyname/) | The settings keypath, e.g. `highlightColor`. |

##### Returns[#](#returns-79)

[`Color`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/color/)

##### Throws[#](#throws-21)

An error, if the keypath is invalid.

#### Signatures[#](#signatures-10)

```
getSettingColor(keypath: SettingColorPropertyName): Color
```

```
getSettingColor(keypath: `ubq://${string & {}}`): Color
```

```
getSettingColor(keypath: SettingColorPropertyName): Color
```

* * *

### setSettingEnum()[#](#setsettingenum)

  

Set an enum setting.

##### Type Parameters[#](#type-parameters-2)

| Type Parameter |
| --- |
| `T` _extends_ keyof [`SettingEnumType`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/settingenumtype/) |

##### Parameters[#](#parameters-57)

| Parameter | Type | Description |
| --- | --- | --- |
| `keypath` | `T` | The settings keypath, e.g. `doubleClickSelectionMode`. |
| `value` | [`SettingEnumType`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/settingenumtype/)\[`T`\] | The enum value as string. |

##### Returns[#](#returns-80)

`void`

#### Call Signature[#](#call-signature-19)

```
setSettingEnum(keypath, value): void;
```

Set an enum setting.

##### Parameters[#](#parameters-58)

| Parameter | Type | Description |
| --- | --- | --- |
| `keypath` | `string` | The settings keypath, e.g. `doubleClickSelectionMode`. |
| `value` | `string` | The enum value as string. |

##### Returns[#](#returns-81)

`void`

#### Signatures[#](#signatures-11)

```
setSettingEnum(keypath: T, value: SettingEnumType[T]): void
```

```
setSettingEnum(keypath: string, value: string): void
```

* * *

### getSettingEnum()[#](#getsettingenum)

  

Get an enum setting.

##### Type Parameters[#](#type-parameters-3)

| Type Parameter |
| --- |
| `T` _extends_ keyof [`SettingEnumType`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/settingenumtype/) |

##### Parameters[#](#parameters-59)

| Parameter | Type | Description |
| --- | --- | --- |
| `keypath` | `T` | The settings keypath, e.g. `doubleClickSelectionMode`. |

##### Returns[#](#returns-82)

[`SettingEnumType`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/settingenumtype/)\[`T`\]

The value as string.

#### Call Signature[#](#call-signature-20)

```
getSettingEnum(keypath): string;
```

Get an enum setting.

##### Parameters[#](#parameters-60)

| Parameter | Type | Description |
| --- | --- | --- |
| `keypath` | `string` | The settings keypath, e.g. `doubleClickSelectionMode`. |

##### Returns[#](#returns-83)

`string`

The value as string.

#### Signatures[#](#signatures-12)

```
getSettingEnum(keypath: T): SettingEnumType[T]
```

```
getSettingEnum(keypath: string): string
```

* * *

### getSettingEnumOptions()[#](#getsettingenumoptions)

  

Get the possible enum options for a given enum setting.

##### Type Parameters[#](#type-parameters-4)

| Type Parameter |
| --- |
| `T` _extends_ keyof [`SettingEnumType`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/settingenumtype/) |

##### Parameters[#](#parameters-61)

| Parameter | Type | Description |
| --- | --- | --- |
| `keypath` | `T` | The settings keypath, e.g. `doubleClickSelectionMode`. |

##### Returns[#](#returns-84)

[`SettingEnumType`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/settingenumtype/)\[`T`\]\[\]

The possible enum options as strings.

#### Call Signature[#](#call-signature-21)

```
getSettingEnumOptions(keypath): string[];
```

Get the possible enum options for a given enum setting.

##### Parameters[#](#parameters-62)

| Parameter | Type | Description |
| --- | --- | --- |
| `keypath` | `string` | The settings keypath, e.g. `doubleClickSelectionMode`. |

##### Returns[#](#returns-85)

`string`\[\]

The possible enum options as strings.

#### Signatures[#](#signatures-13)

```
getSettingEnumOptions(keypath: T): SettingEnumType[T][]
```

```
getSettingEnumOptions(keypath: string): string[]
```

* * *

### findAllSettings()[#](#findallsettings)

  

Returns a list of all the settings available.

#### Returns[#](#returns-86)

`string`\[\]

A list of settings keypaths.

#### Signature[#](#signature-42)

```
findAllSettings(): string[]
```

* * *

### getSettingType()[#](#getsettingtype)

  

Returns the type of a setting.

#### Parameters[#](#parameters-63)

| Parameter | Type | Description |
| --- | --- | --- |
| `keypath` | `string` | The settings keypath, e.g. `doubleClickSelectionMode`. |

#### Returns[#](#returns-87)

[`SettingType`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/settingtype/)

The setting type.

#### Signature[#](#signature-43)

```
getSettingType(keypath: string): SettingType
```

* * *

### setURIResolver()[#](#seturiresolver)

  

Sets a custom URI resolver.

This function can be called more than once. Subsequent calls will overwrite previous calls. To remove a previously set resolver, pass the value `null`. The given function must return an absolute path with a scheme and cannot be asynchronous. The input is allowed to be invalid URI, e.g., due to placeholders.

```
// Replace all .jpg files with the IMG.LY logoengine.editor.setURIResolver((uri) => {  if (uri.endsWith('.jpg')) {    return 'https://img.ly/static/ubq_samples/imgly_logo.jpg';  }  // Make use of the default URI resolution behavior.  return engine.editor.defaultURIResolver(uri);});
```

#### Parameters[#](#parameters-64)

| Parameter | Type | Description |
| --- | --- | --- |
| `resolver` | (`URI`, `defaultURIResolver`) => `string` | Custom resolution function. The resolution function should not reference variables outside of its scope. It receives the default URI resolver as its second argument |

#### Returns[#](#returns-88)

`void`

#### Signature[#](#signature-44)

```
setURIResolver(resolver: (URI: string, defaultURIResolver: (URI: string) => string) => string): void
```

* * *

### defaultURIResolver()[#](#defaulturiresolver)

  

This is the default implementation for the URI resolver.

It resolves the given path relative to the `basePath` setting.

```
engine.editor.defaultURIResolver(uri);
```

#### Parameters[#](#parameters-65)

| Parameter | Type | Description |
| --- | --- | --- |
| `relativePath` | `string` | The relative path that should be resolved. |

#### Returns[#](#returns-89)

`string`

The resolved absolute URI.

#### Signature[#](#signature-45)

```
defaultURIResolver(relativePath: string): string
```

* * *

### getAbsoluteURI()[#](#getabsoluteuri)

  

Resolves the given path.

If a custom resolver has been set with `setURIResolver`, it invokes it with the given path. Else, it resolves it as relative to the `basePath` setting. This performs NO validation of whether a file exists at the specified location.

#### Parameters[#](#parameters-66)

| Parameter | Type | Description |
| --- | --- | --- |
| `relativePath` | `string` | A relative path string |

#### Returns[#](#returns-90)

`string`

The resolved absolute uri or an error if an invalid path was given.

#### Signature[#](#signature-46)

```
getAbsoluteURI(relativePath: string): string
```

## System Information[#](#system-information)

Access memory usage, export limits, and system capabilities.

### getAvailableMemory()[#](#getavailablememory)

  

Get the currently available memory.

#### Returns[#](#returns-91)

`number`

The available memory in bytes.

#### Signature[#](#signature-47)

```
getAvailableMemory(): number
```

* * *

### getUsedMemory()[#](#getusedmemory)

  

Get the engine’s current memory usage.

#### Returns[#](#returns-92)

`number`

The current memory usage in bytes.

#### Signature[#](#signature-48)

```
getUsedMemory(): number
```

* * *

### getMaxExportSize()[#](#getmaxexportsize)

  

Get the maximum export size limit for the current device.

Exports are only possible when both width and height are below this limit. Note that exports may still fail due to other constraints like memory.

#### Returns[#](#returns-93)

`number`

The upper export size limit in pixels, or maximum 32-bit integer if unlimited.

#### Signature[#](#signature-49)

```
getMaxExportSize(): number
```

## Experimental[#](#experimental)

### unstable\_isInteractionHappening()[#](#unstable_isinteractionhappening)

Check if a user interaction is currently happening.

Detects active interactions like resize edits with drag handles or touch gestures.

#### Returns[#](#returns-94)

`boolean`

True if an interaction is happening. This API is experimental and may change or be removed in future versions.

## Other[#](#other)

### ~setSettingColorRGBA()~[#](#setsettingcolorrgba)

  

Set a color setting.

#### Parameters[#](#parameters-67)

| Parameter | Type | Description |
| --- | --- | --- |
| `keypath` |  | `` `ubq://${string & {}}` `` |
| `r` | `number` | The red color component in the range of 0 to 1. |
| `g` | `number` | The green color component in the range of 0 to 1. |
| `b` | `number` | The blue color component in the range of 0 to 1. |
| `a?` | `number` | The alpha color component in the range of 0 to 1. |

#### Returns[#](#returns-95)

`void`

#### Deprecated[#](#deprecated-8)

Use setSettingColor() instead.

* * *

### ~getSettingColorRGBA()~[#](#getsettingcolorrgba)

  

Get a color setting.

#### Parameters[#](#parameters-68)

| Parameter | Type | Description |
| --- | --- | --- |
| `keypath` |  | `` `ubq://${string & {}}` `` |

#### Returns[#](#returns-96)

[`RGBA`](https://img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/rgba/)

A tuple of channels red, green, blue and alpha in the range of 0 to 1.

#### Deprecated[#](#deprecated-9)

Use getSettingColor() instead.

* * *

### isHighlightingEnabled()[#](#ishighlightingenabled)

  

Checks wether the block has selection and hover highlighting enabled or disabled.

```
const highlightingIsEnabled = engine.editor.isHighlightingEnabled(block);
```

#### Parameters[#](#parameters-69)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-97)

`boolean`

True if highlighting is enabled, false otherwise.

#### Signature[#](#signature-50)

```
isHighlightingEnabled(id: number): boolean
```

* * *

### setHighlightingEnabled()[#](#sethighlightingenabled)

  

Enable or disable selection and hover highlighting for a block.

```
engine.editor.setHighlightingEnabled(block, true);
```

#### Parameters[#](#parameters-70)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to update. |
| `enabled` | `boolean` | Whether or not the block should show highlighting when selected or hovered. |

#### Returns[#](#returns-98)

`void`

#### Signature[#](#signature-51)

```
setHighlightingEnabled(id: number, enabled: boolean): void
```

* * *

### isSelectionEnabled()[#](#isselectionenabled)

  

Checks whether the block can currently be selected.

```
const selectionIsEnabled = engine.editor.isSelectionEnabled(block);
```

#### Parameters[#](#parameters-71)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to query. |

#### Returns[#](#returns-99)

`boolean`

True if selection is enabled, false otherwise.

#### Signature[#](#signature-52)

```
isSelectionEnabled(id: number): boolean
```

* * *

### setSelectionEnabled()[#](#setselectionenabled)

  

Enable or disable selection for a block.

```
engine.editor.setSelectionEnabled(block, true);
```

#### Parameters[#](#parameters-72)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `number` | The block to update. |
| `enabled` | `boolean` | Whether the block should be selectable. |

#### Returns[#](#returns-100)

`void`

#### Signature[#](#signature-53)

```
setSelectionEnabled(id: number, enabled: boolean): void
```

## Viewport[#](#viewport)

### setSafeAreaInsets()[#](#setsafeareainsets)

  

Set global safe area insets for UI overlays.

Safe area insets define UI-safe regions by specifying padding from screen edges. These insets are automatically applied to all camera operations (zoom, pan, clamping) to ensure important content remains visible when UI elements overlap the viewport edges. Set to zero to disable (default state).

#### Parameters[#](#parameters-73)

| Parameter | Type | Description |
| --- | --- | --- |
| `insets` | { `left?`: `number`; `top?`: `number`; `right?`: `number`; `bottom?`: `number`; } | The inset values in CSS pixels (device-independent) |
| `insets.left?` | `number` | \- |
| `insets.top?` | `number` | \- |
| `insets.right?` | `number` | \- |
| `insets.bottom?` | `number` | \- |

#### Returns[#](#returns-101)

`void`

#### Signature[#](#signature-54)

```
setSafeAreaInsets(insets: object): void
```

* * *

### getSafeAreaInsets()[#](#getsafeareainsets)

  

Get the current global safe area insets configuration.

#### Returns[#](#returns-102)

`object`

The current inset values in CSS pixels (device-independent)

| Name | Type |
| --- | --- |
| `left` | `number` |
| `top` | `number` |
| `right` | `number` |
| `bottom` | `number` |

#### Signature[#](#signature-55)

```
getSafeAreaInsets(): object
```

---



[Source](https:/img.ly/docs/cesdk/sveltekit/api/engine/classes/creativeengine)