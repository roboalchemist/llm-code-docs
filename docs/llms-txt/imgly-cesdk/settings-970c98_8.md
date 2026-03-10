# Source: https://img.ly/docs/cesdk/macos/settings-970c98/

---
title: "Settings"
description: "Explore all configurable editor settings and learn how to read, update, and observe them via the Settings API."
platform: macos
url: "https://img.ly/docs/cesdk/macos/settings-970c98/"
---

> This is one page of the CE.SDK macOS documentation. For a complete overview, see the [macOS Documentation Index](https://img.ly/docs/cesdk/macos.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/macos/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/macos/guides-8d8b00/) > [Settings](https://img.ly/docs/cesdk/macos/settings-970c98/)

---

All keys listed below can be modified through the Editor API.
The nested settings inside `UBQSettings` can be reached via key paths, e.g. `page/title/show`.

## Settings

### `BlockAnimationSettings`

| Member  | Type   | Default | Description                                  |
| ------- | ------ | ------- | -------------------------------------------- |
| enabled | `bool` | `true`  | Whether animations should be enabled or not. |

### `CameraClampingSettings`

| Member        | Type                          | Default   | Description                                                                                                                                                                                               |
| ------------- | ----------------------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| overshootMode | `CameraClampingOvershootMode` | `Reverse` | Controls what happens when the clamp area is smaller than the viewport. Center: the clamp area is centered in the viewport. Reverse: the clamp area can move inside the viewport until it hits the edges. |

### `CameraSettings`

| Member   | Type                                                                | Default | Description                       |
| -------- | ------------------------------------------------------------------- | ------- | --------------------------------- |
| clamping | `CameraClampingSettings: CameraClampingOvershootMode overshootMode` | `{}`    | Clamping settings for the camera. |

### `ControlGizmoSettings`

| Member               | Type    | Default  | Description                                                                                                                                                                     |
| -------------------- | ------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| blockScaleDownLimit  | `float` | `8.0`    | Scale-down limit for blocks in screen pixels when scaling them with the gizmos or with touch gestures. The limit is ensured to be at least 0.1 to prevent scaling to size zero. |
| showCropHandles      | `bool`  | `{true}` | Whether or not to show the handles to adjust the crop area during crop mode.                                                                                                    |
| showCropScaleHandles | `bool`  | `{true}` | Whether or not to display the outer handles that scale the full image during crop.                                                                                              |
| showMoveHandles      | `bool`  | `{true}` | Whether or not to show the move handles.                                                                                                                                        |
| showResizeHandles    | `bool`  | `{true}` | Whether or not to display the non-proportional resize handles (edge handles)                                                                                                    |
| showRotateHandles    | `bool`  | `{true}` | Whether or not to show the rotation handles.                                                                                                                                    |
| showScaleHandles     | `bool`  | `{true}` | Whether or not to display the proportional scale handles (corner handles)                                                                                                       |

### `DebugFlags`

Flags that control debug outputs.

| Member                     | Type   | Default   | Description                                                                                                   |
| -------------------------- | ------ | --------- | ------------------------------------------------------------------------------------------------------------- |
| enforceScopesInAPIs        | `bool` | `false`   | Whether APIs calls that perform edits should throw errors if the corresponding scope does not allow the edit. |
| showHandlesInteractionArea | `bool` | `{false}` | Display the interaction area around the handles.                                                              |
| useDebugMipmaps            | `bool` | `false`   | Enable the use of colored mipmaps to see which mipmap is used.                                                |

### `MouseSettings`

| Member       | Type   | Default | Description                                       |
| ------------ | ------ | ------- | ------------------------------------------------- |
| enableScroll | `bool` | `true`  | Whether the engine processes mouse scroll events. |
| enableZoom   | `bool` | `true`  | Whether the engine processes mouse zoom events.   |

### `PageSettings`

| Member                                      | Type                                                                                                                                                      | Default                                 | Description                                                                                                                                                                                          |
| ------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| allowCropInteraction                        | `bool`                                                                                                                                                    | `true`                                  | If crop interaction (by handles and gestures) should be possible when the enabled arrangements allow resizing.                                                                                       |
| allowMoveInteraction                        | `bool`                                                                                                                                                    | `false`                                 | If move interaction (by handles and gestures) should be possible when the enabled arrangements allow moving and if the page layout is not controlled by the scene, e.g., in a 'VerticalStack'.       |
| allowResizeInteraction                      | `bool`                                                                                                                                                    | `false`                                 | If a resize interaction (by handles and gestures) should be possible when the enabled arrangements allow resizing.                                                                                   |
| allowRotateInteraction                      | `bool`                                                                                                                                                    | `false`                                 | If rotation interaction (by handles and gestures) should be possible when the enabled arrangements allow rotation and if the page layout is not controlled by the scene, e.g., in a 'VerticalStack'. |
| dimOutOfPageAreas                           | `bool`                                                                                                                                                    | `true`                                  | Whether the opacity of the region outside of all pages should be reduced.                                                                                                                            |
| innerBorderColor                            | `Color`                                                                                                                                                   | `createRGBColor(0.0, 0.0, 0.0, 0.0)`    | Color of the inner frame around the page.                                                                                                                                                            |
| marginFillColor                             | `Color`                                                                                                                                                   | `createRGBColor(0.79, 0.12, 0.40, 0.1)` | Color of frame around the bleed margin area of the pages.                                                                                                                                            |
| marginFrameColor                            | `Color`                                                                                                                                                   | `createRGBColor(0.79, 0.12, 0.40, 0.0)` | Color filled into the bleed margins of pages.                                                                                                                                                        |
| moveChildrenWhenCroppingFill                | `bool`                                                                                                                                                    | `false`                                 | Whether the children of the page should be transformed to match their old position relative to the page fill when a page fill is cropped.                                                            |
| outerBorderColor                            | `Color`                                                                                                                                                   | `createRGBColor(1.0, 1.0, 1.0, 0.0)`    | Color of the outer frame around the page.                                                                                                                                                            |
| restrictResizeInteractionToFixedAspectRatio | `bool`                                                                                                                                                    | `false`                                 | If the resize interaction should be restricted to fixed aspect ratio resizing.                                                                                                                       |
| title                                       | `PageTitleSettings(bool show, bool showOnSinglePage, bool showPageTitleTemplate, bool appendPageName, string separator, Color color, string fontFileUri)` | \`\`                                      | Page title settings.                                                                                                                                                                                 |

### `PageTitleSettings`

| Member                | Type     | Default                      | Description                                                                                                                                       |
| --------------------- | -------- | ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| appendPageName        | `bool`   | `true`                       | Whether to append the page name to the title if a page name is set even if the name is not specified in the template or the template is not shown |
| color                 | `Color`  | `createRGBColor(1., 1., 1.)` | Color of page titles visible in preview mode, can change with different themes.                                                                   |
| fontFileUri           | `string` | `DEFAULT_FONT`               | Font of page titles.                                                                                                                              |
| separator             | `string` | `"-"`                        | Title label separator between the page number and the page name.                                                                                  |
| show                  | `bool`   | `true`                       | Whether to show titles above each page.                                                                                                           |
| showOnSinglePage      | `bool`   | `true`                       | Whether to hide the the page title when only a single page is given.                                                                              |
| showPageTitleTemplate | `bool`   | `true`                       | Whether to include the default page title from `page.titleTemplate`                                                                               |

### `PlaceholderControlsSettings`

| Member      | Type   | Default | Description                  |
| ----------- | ------ | ------- | ---------------------------- |
| showButton  | `bool` | `true`  | Show the placeholder button. |
| showOverlay | `bool` | `true`  | Show the overlay pattern.    |

### `Settings`

| Member                               | Type                                                                                                                                                                                                                                                                                                                                                                | Default                                  | Description                                                                                                                                                                                                   |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| alwaysHighlightPlaceholders          | `bool`                                                                                                                                                                                                                                                                                                                                                              | `false`                                  | Whether placeholder elements should always be highlighted in the scene.                                                                                                                                       |
| basePath                             | `string`                                                                                                                                                                                                                                                                                                                                                            | `""`                                     | The root directory to be used when resolving relative paths or when accessing `bundle://` URIs on platforms that don't offer bundles.                                                                         |
| blockAnimations                      | `BlockAnimationSettings: bool enabled`                                                                                                                                                                                                                                                                                                                              | `{}`                                     | Settings that configure the behavior of block animations.                                                                                                                                                     |
| borderOutlineColor                   | `Color`                                                                                                                                                                                                                                                                                                                                                             | `createRGBColor(0., 0., 0., 1.0)`        | The border outline color, defaults to black.                                                                                                                                                                  |
| camera                               | `CameraSettings: CameraClampingSettings clamping`                                                                                                                                                                                                                                                                                                                   | `{}`                                     | Settings that configure the behavior of the camera.                                                                                                                                                           |
| clearColor                           | `Color`                                                                                                                                                                                                                                                                                                                                                             | `createClear()`                          | The color with which the render target is cleared before scenes get rendered. Only used while renderMode == Preview, else #00000000 (full transparency) is used.                                              |
| colorMaskingSettings                 | `ColorMaskingSettings(Color maskColor, bool secondPass)`                                                                                                                                                                                                                                                                                                            | `{}`                                     | A collection of settings used to perform color masking.                                                                                                                                                       |
| controlGizmo                         | `ControlGizmoSettings(bool showCropHandles, bool showCropScaleHandles, bool showMoveHandles, bool showResizeHandles, bool showScaleHandles, bool showRotateHandles, float blockScaleDownLimit)`                                                                                                                                                                     | `{}`                                     | Settings that configure which touch/click targets for move/scale/rotate/etc. are enabled and displayed.                                                                                                       |
| cropOverlayColor                     | `Color`                                                                                                                                                                                                                                                                                                                                                             | `createRGBColor(0., 0., 0., 0.39)`       | Color of the dimming overlay that's added in crop mode.                                                                                                                                                       |
| debug                                | `DebugFlags(bool useDebugMipmaps, bool showHandlesInteractionArea, bool enforceScopesInAPIs)`                                                                                                                                                                                                                                                                       | `{}`                                     | ?                                                                                                                                                                                                             |
| defaultEmojiFontFileUri              | `string`                                                                                                                                                                                                                                                                                                                                                            | `EMOJI_FONT`                             | URI of default font file for emojis.                                                                                                                                                                          |
| defaultFontFileUri                   | `string`                                                                                                                                                                                                                                                                                                                                                            | `DEFAULT_FONT`                           | URI of default font file This font file is the default everywhere unless overriden in specific settings.                                                                                                      |
| doubleClickSelectionMode             | `DoubleClickSelectionMode`                                                                                                                                                                                                                                                                                                                                          | `Hierarchical`                           | The current mode of selection on double-click.                                                                                                                                                                |
| doubleClickToCropEnabled             | `bool`                                                                                                                                                                                                                                                                                                                                                              | `true`                                   | Whether double clicking on an image element should switch into the crop editing mode.                                                                                                                         |
| emscriptenCORSConfigurations         | `vector< CORSConfiguration >`                                                                                                                                                                                                                                                                                                                                       | `{}`                                     | CORS Configurations: `<origin, value>` pairs. See `FetchAsyncService-emscripten.cpp` for details.                                                                                                             |
| errorStateColor                      | `Color`                                                                                                                                                                                                                                                                                                                                                             | `createRGBColor(1., 1., 1., 0.7)`        | The error state color for design blocks.                                                                                                                                                                      |
| fallbackFontUri                      | `string`                                                                                                                                                                                                                                                                                                                                                            | `""`                                     | The URI of the fallback font to use for text that is missing certain characters.                                                                                                                              |
| forceSystemEmojis                    | `bool`                                                                                                                                                                                                                                                                                                                                                              | `true`                                   | Whether the system emojis should be used for text.                                                                                                                                                            |
| globalScopes                         | `GlobalScopes(Text text, Fill fill, Stroke stroke, Shape shape, Layer layer, Appearance appearance, Lifecycle lifecycle, Editor editor)`                                                                                                                                                                                                                            | `Allow)`                                 | Global scopes.                                                                                                                                                                                                |
| handleFillColor                      | `Color`                                                                                                                                                                                                                                                                                                                                                             | `createWhite()`                          | The fill color for handles.                                                                                                                                                                                   |
| highlightColor                       | `Color`                                                                                                                                                                                                                                                                                                                                                             | `createRGBColor(0.2, 85. / 255., 1.)`    | Color of the selection, hover, and group frames and for the handle outlines for non-placeholder elements.                                                                                                     |
| license                              | `string`                                                                                                                                                                                                                                                                                                                                                            | `""`                                     | A valid license string in JWT format.                                                                                                                                                                         |
| maxImageSize                         | `int`                                                                                                                                                                                                                                                                                                                                                               | `4096`                                   | The maximum size at which images are loaded into the engine. Images that exceed this size are down-scaled prior to rendering. Reducing this size further reduces the memory footprint. Defaults to 4096x4096. |
| mouse                                | `MouseSettings(bool enableZoom, bool enableScroll)`                                                                                                                                                                                                                                                                                                                 | `{}`                                     | Settings that configure the behavior of the mouse.                                                                                                                                                            |
| page                                 | `PageSettings(PageTitleSettings title, Color marginFillColor, Color marginFrameColor, Color innerBorderColor, Color outerBorderColor, bool dimOutOfPageAreas, bool allowCropInteraction, bool allowResizeInteraction, bool restrictResizeInteractionToFixedAspectRatio, bool allowRotateInteraction, bool allowMoveInteraction, bool moveChildrenWhenCroppingFill)` | `{}`                                     | Page related settings.                                                                                                                                                                                        |
| pageHighlightColor                   | `Color`                                                                                                                                                                                                                                                                                                                                                             | `createRGBColor(0.5, 0.5, 0.5, 0.2)`     | Color of the outline of each page.                                                                                                                                                                            |
| placeholderControls                  | `PlaceholderControlsSettings(bool showOverlay, bool showButton)`                                                                                                                                                                                                                                                                                                    | `{}`                                     | Supersedes how the blocks' placeholder controls are applied.                                                                                                                                                  |
| placeholderHighlightColor            | `Color`                                                                                                                                                                                                                                                                                                                                                             | `createRGBColor(0.77, 0.06, 0.95)`       | Color of the selection, hover, and group frames and for the handle outlines for placeholder elements.                                                                                                         |
| positionSnappingThreshold            | `float`                                                                                                                                                                                                                                                                                                                                                             | `4.`                                     | Position snapping threshold in screen space.                                                                                                                                                                  |
| progressColor                        | `Color`                                                                                                                                                                                                                                                                                                                                                             | `createRGBColor(1., 1., 1., 0.7)`        | The progress indicator color.                                                                                                                                                                                 |
| renderTextCursorAndSelectionInEngine | `bool`                                                                                                                                                                                                                                                                                                                                                              | `true`                                   | Whether the engine should render the text cursor and selection highlights during text editing. This can be set to false, if the platform wants to perform this rendering itself.                              |
| rotationSnappingGuideColor           | `Color`                                                                                                                                                                                                                                                                                                                                                             | `createRGBColor(1., 0.004, 0.361)`       | Color of the rotation snapping guides.                                                                                                                                                                        |
| rotationSnappingThreshold            | `float`                                                                                                                                                                                                                                                                                                                                                             | `0.15`                                   | Rotation snapping threshold in radians.                                                                                                                                                                       |
| ruleOfThirdsLineColor                | `Color`                                                                                                                                                                                                                                                                                                                                                             | `createRGBColor(0.75, 0.75, 0.75, 0.75)` | Color of the rule-of-thirds lines.                                                                                                                                                                            |
| showBuildVersion                     | `bool`                                                                                                                                                                                                                                                                                                                                                              | `false`                                  | Show the build version on the canvas.                                                                                                                                                                         |
| snappingGuideColor                   | `Color`                                                                                                                                                                                                                                                                                                                                                             | `createRGBColor(1., 0.004, 0.361)`       | Color of the position snapping guides.                                                                                                                                                                        |
| textVariableHighlightColor           | `Color`                                                                                                                                                                                                                                                                                                                                                             | `createRGBColor(0.7, 0., 0.7)`           | Color of the text variable highlighting borders.                                                                                                                                                              |
| touch                                | `TouchSettings(bool dragStartCanSelect, bool singlePointPanning, PinchGestureAction pinchAction, RotateGestureAction rotateAction)`                                                                                                                                                                                                                                 | `{}`                                     | Settings that configure which touch gestures are enabled and which actions they trigger.                                                                                                                      |
| useSystemFontFallback                | `bool`                                                                                                                                                                                                                                                                                                                                                              | `false`                                  | Whether the IMG.LY hosted font fallback is used for fonts that are missing certain characters, covering most of the unicode range.                                                                            |

### `TouchSettings`

| Member             | Type                  | Default  | Description                                                                                                                                                                                           |
| ------------------ | --------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| dragStartCanSelect | `bool`                | `true`   | Whether dragging an element requires selecting it first. When not set, elements can be directly dragged.                                                                                              |
| pinchAction        | `PinchGestureAction`  | `Scale`  | The action to perform when a pinch gesture is performed.                                                                                                                                              |
| rotateAction       | `RotateGestureAction` | `Rotate` | Whether or not the two finger turn gesture can rotate selected elements.                                                                                                                              |
| singlePointPanning | `bool`                | `true`   | Whether or not dragging on the canvas should move the camera (scrolling). When not set, the scroll bars have to be used. This setting might get overwritten with the feature flag `preventScrolling`. |

```swift reference-only

engine.editor.findAllSettings()
try engine.editor.getSettingType("doubleClickSelectionMode")

let settingsTask = Task {
  for await _ in engine.editor.onSettingsChanged {
    print("Editor settings have changed")
  }
}

let roleTask = Task {
  for await role in engine.editor.onRoleChanged {
    print("Role changed to \(role)")
  }
}

try engine.editor.setSettingBool("doubleClickToCropEnabled", value: true)
try engine.editor.getSettingBool("doubleClickToCropEnabled")
try engine.editor.setSettingInt("integerSetting", value: 0)
try engine.editor.getSettingInt("integerSetting")
try engine.editor.setSettingFloat("positionSnappingThreshold", value: 2.0)
try engine.editor.getSettingFloat("positionSnappingThreshold")
try engine.editor.setSettingString("license", value: "invalid")
try engine.editor.getSettingString("license")
try engine.editor.setSettingColor("highlightColor", color: .rgba(r: 1, g: 0, b: 1, a: 1)) // Pink
try engine.editor.getSettingColor("highlightColor") as Color
try engine.editor.setSettingEnum("doubleClickSelectionMode", value: "Direct")
try engine.editor.getSettingEnum("doubleClickSelectionMode")
try engine.editor.getSettingEnumOptions("doubleClickSelectionMode")
try engine.editor.getRole()
try engine.editor.setRole("Adopter")
```

## Change Settings

In this example, we will show you how to use the [CreativeEditor SDK](https://img.ly/products/creative-sdk)'s CreativeEngine to control with the `editor` API.
A list of all available settings can be found above.

### Exploration

```swift
public func findAllSettings() -> [String]
```

Get a list of all available settings.

- Returns: A list of all available settings.

```swift
public func getSettingType(_ keypath: String) throws -> PropertyType
```

Get the type of a setting.

- `keypath:`: The settings keypath, e.g. `doubleClickSelectionMode`.
- Returns: The type of the setting.

### Functions

```swift
public var onSettingsChanged: AsyncStream<Void> { get }
```

Subscribe to changes to the editor settings.

```swift
public var onRoleChanged: AsyncStream<String> { get }
```

Subscribe to changes to the editor role.

```swift
public func setSettingBool(_ keypath: String, value: Bool) throws
```

Set a boolean setting.

- `keypath`: The settings keypath, e.g. `doubleClickToCropEnabled`.
- `value`: The value to set.

```swift
public func getSettingBool(_ keypath: String) throws -> Bool
```

Get a boolean setting.

- `keypath:`: The settings keypath, e.g. `doubleClickToCropEnabled`.
- Returns: The current value.

```swift
public func setSettingInt(_ keypath: String, value: Int) throws
```

Set an integer setting.

- `keypath`: The settings keypath.
- `value`: The value to set.

```swift
public func getSettingInt(_ keypath: String) throws -> Int
```

Get an integer setting.

- `keypath:`: The settings keypath.
- Returns: The current value.

```swift
public func setSettingFloat(_ keypath: String, value: Float) throws
```

Set a float setting.

- `keypath`: The settings keypath, e.g. `positionSnappingThreshold`.
- `value`: The value to set.

```swift
public func getSettingFloat(_ keypath: String) throws -> Float
```

Get a float setting.

- `keypath:`: The settings keypath, e.g. `positionSnappingThreshold`.
- Returns: The current value.

```swift
public func setSettingString(_ keypath: String, value: String) throws
```

Set a string setting.

- `keypath`: The settings keypath, e.g. `license`.
- `value`: The value to set.

```swift
public func getSettingString(_ keypath: String) throws -> String
```

Get a string setting.

- `keypath:`: The settings keypath, e.g. `license`.
- Returns: The current value.

```swift
public func setSettingColor(_ keypath: String, color: Color) throws
```

Set a color setting.

- `keypath`: The settings keypath, e.g. `highlightColor`.
- `color`: The value to set.

```swift
public func getSettingColor(_ keypath: String) throws -> Color
```

Get a color setting.

- `keypath:`: The settings keypath, e.g. `highlightColor`.
- Returns: An error, if the keypath is invalid.

```swift
public func setSettingEnum(_ keypath: String, value: String) throws
```

Set an enum setting.

- `keypath`: The settings keypath, e.g. `doubleClickSelectionMode`.
- `value`: The enum value as string.

```swift
public func getSettingEnum(_ keypath: String) throws -> String
```

Get an enum setting.

- `keypath:`: The settings keypath, e.g. `doubleClickSelectionMode`.
- Returns: The value as string.

```swift
public func getSettingEnumOptions(_ keypath: String) throws -> [String]
```

Get the available options for an enum setting.

- `keypath:`: The settings keypath, e.g. `doubleClickSelectionMode`.
- Returns: The available options as string array.

```swift
public func setSettingFloat(_ keypath: String, value: Float) throws
```

Set a float setting.

- `keypath`: The settings keypath, e.g. `positionSnappingThreshold`.
- `value`: The value to set.

```swift
public func getSettingFloat(_ keypath: String) throws -> Float
```

Get a float setting.

- `keypath:`: The settings keypath, e.g. `positionSnappingThreshold`.
- Returns: The current value.

```swift
public func setSettingString(_ keypath: String, value: String) throws
```

Set a string setting.

- `keypath`: The settings keypath, e.g. `license`.
- `value`: The value to set.

```swift
public func getSettingString(_ keypath: String) throws -> String
```

Get a string setting.

- `keypath:`: The settings keypath, e.g. `license`.
- Returns: The current value.

```swift
public func getRole() throws -> String
```

Get the current role of the user.

- Returns: The current role of the user.

```swift
public func setRole(_ role: String) throws
```

Set the role of the user and apply role-dependent defaults for scopes and settings.

- `role:`: The role of the user.




---

## More Resources

- **[macOS Documentation Index](https://img.ly/docs/cesdk/macos.md)** - Browse all macOS documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/macos/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/macos/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
