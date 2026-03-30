# Interface: Settings

Map of all available settings with their types. This provides type-safe access to all editor settings.

The settings are organized by type:

*   Boolean settings control various on/off features in the editor
*   String settings configure paths and textual values
*   Float settings define numerical thresholds and limits
*   Integer settings specify whole number limits
*   Color settings control the visual appearance
*   Enum settings provide predefined choice options

## Properties[#](#properties)

| Property | Type | Description |
| --- | --- | --- |
| `controlGizmo/showCropHandles` | `boolean` | Whether to show handles for adjusting the crop area during crop mode. |
| `controlGizmo/showCropScaleHandles` | `boolean` | Whether to display the outer handles that scale the full image during crop. |
| `controlGizmo/showMoveHandles` | `boolean` | Whether to show the move handles. |
| `controlGizmo/showResizeHandles` | `boolean` | Whether to display the non-proportional resize handles (edge handles). |
| `controlGizmo/showRotateHandles` | `boolean` | Whether to show the rotation handles. |
| `controlGizmo/showScaleHandles` | `boolean` | Whether to display the proportional scale handles (corner handles). |
| `doubleClickToCropEnabled` | `boolean` | Enable double-click to enter crop mode. |
| `features/singlePageModeEnabled` | `boolean` | Enable single page mode where only one page is shown at a time. |
| `features/fileSystemUsageEnabled` | `boolean` | Enable file system usage, that allows the engine to use the file system to store files for local uploads. |
| `features/pageCarouselEnabled` | `boolean` | Enable the page carousel for navigating between pages. |
| `features/transformEditsRetainCoverMode` | `boolean` | Whether transform edits should retain the cover mode of the content. |
| `mouse/enableScroll` | `boolean` | Whether the engine processes mouse scroll events. |
| `mouse/enableZoom` | `boolean` | Whether the engine processes mouse zoom events. |
| `page/allowCropInteraction` | `boolean` | Whether crop interaction (by handles and gestures) should be possible. |
| `page/allowMoveInteraction` | `boolean` | Whether move interaction should be possible when page layout is not controlled by the scene. |
| `page/allowResizeInteraction` | `boolean` | Whether resize interaction (by handles and gestures) should be possible. |
| `page/allowRotateInteraction` | `boolean` | Whether rotation interaction should be possible when page layout is not controlled by the scene. |
| `page/dimOutOfPageAreas` | `boolean` | Whether the opacity of the region outside of all pages should be reduced. |
| `page/restrictResizeInteractionToFixedAspectRatio` | `boolean` | Whether resize interaction should be restricted to fixed aspect ratio. |
| `page/moveChildrenWhenCroppingFill` | `boolean` | Whether children of the page should be transformed to match their old position when cropping. |
| `page/title/appendPageName` | `boolean` | Whether to append the page name to the title even if not specified in the template. |
| `page/title/show` | `boolean` | Whether to show titles above each page. |
| `page/title/showOnSinglePage` | `boolean` | Whether to hide the page title when only a single page exists. |
| `page/title/showPageTitleTemplate` | `boolean` | Whether to include the default page title from page.titleTemplate. |
| `placeholderControls/showButton` | `boolean` | Whether to show the placeholder button. |
| `placeholderControls/showOverlay` | `boolean` | Whether to show the overlay pattern for placeholders. |
| `blockAnimations/enabled` | `boolean` | Whether animations should be enabled or not. |
| `showBuildVersion` | `boolean` | Whether to display the build version in the UI. |
| `touch/dragStartCanSelect` | `boolean` | Whether drag start can select elements. |
| `touch/singlePointPanning` | `boolean` | Whether single-point panning is enabled for touch interactions. |
| `useSystemFontFallback` | `boolean` | Whether to use system font as fallback for missing glyphs. |
| `forceSystemEmojis` | `boolean` | Whether to force the use of system emojis instead of custom emoji fonts. |
| `page/selectWhenNoBlocksSelected` | `boolean` | Whether to select the page when a block is deselected and no other blocks are selected. |
| `page/highlightWhenCropping` | `boolean` | Whether highlighting should be automatically enabled on the current page when entering crop mode. |
| `clampThumbnailTextureSizes` | `boolean` | Clamp thumbnail texture sizes to the platform’s GPU texture limit. |
| `dock/hideLabels` | `boolean` | Toggle the dock components visibility |
| `basePath` | `string` | The root directory used when resolving relative paths or accessing bundle:// URIs. |
| `defaultEmojiFontFileUri` | `string` | The URI for the default emoji font file. |
| `defaultFontFileUri` | `string` | The URI for the default font file. |
| `license` | `string` | The license key for the SDK. |
| `page/title/fontFileUri` | `string` | The font file URI for page titles. |
| `page/title/separator` | `string` | The separator between page number and page name in titles. |
| `fallbackFontUri` | `string` | The URI for the fallback font used when glyphs are missing. |
| `upload/supportedMimeTypes` | `string` | The supported MIME types for file uploads. |
| `web/fetchCredentials` | `"omit"` | `"same-origin"` |
| `controlGizmo/blockScaleDownLimit` | `number` | Scale-down limit for blocks in screen pixels when scaling with gizmos or touch gestures. |
| `positionSnappingThreshold` | `number` | The threshold distance in pixels for position snapping. |
| `rotationSnappingThreshold` | `number` | The threshold angle in degrees for rotation snapping. |
| `maxImageSize` | `number` | The maximum size (width or height) in pixels for images. |
| `borderOutlineColor` | [`Color`](https://img.ly/docs/cesdk/vue/api/engine/type-aliases/color/) | The color of the border outline for selected elements. |
| `clearColor` | [`Color`](https://img.ly/docs/cesdk/vue/api/engine/type-aliases/color/) | The background clear color. |
| `colorMaskingSettings/maskColor` | [`Color`](https://img.ly/docs/cesdk/vue/api/engine/type-aliases/color/) | The color used for color masking effects. |
| `cropOverlayColor` | [`Color`](https://img.ly/docs/cesdk/vue/api/engine/type-aliases/color/) | The color of the crop overlay. |
| `errorStateColor` | [`Color`](https://img.ly/docs/cesdk/vue/api/engine/type-aliases/color/) | The color indicating an error state. |
| `highlightColor` | [`Color`](https://img.ly/docs/cesdk/vue/api/engine/type-aliases/color/) | The highlight color for selected or active elements. |
| `page/innerBorderColor` | [`Color`](https://img.ly/docs/cesdk/vue/api/engine/type-aliases/color/) | The color of the inner frame around the page. |
| `page/marginFillColor` | [`Color`](https://img.ly/docs/cesdk/vue/api/engine/type-aliases/color/) | The color filled into the bleed margins of pages. |
| `page/marginFrameColor` | [`Color`](https://img.ly/docs/cesdk/vue/api/engine/type-aliases/color/) | The color of the frame around the bleed margin area. |
| `page/outerBorderColor` | [`Color`](https://img.ly/docs/cesdk/vue/api/engine/type-aliases/color/) | The color of the outer frame around the page. |
| `page/title/color` | [`Color`](https://img.ly/docs/cesdk/vue/api/engine/type-aliases/color/) | The color of page titles visible in preview mode. |
| `pageHighlightColor` | [`Color`](https://img.ly/docs/cesdk/vue/api/engine/type-aliases/color/) | Color of the outline of each page |
| `placeholderHighlightColor` | [`Color`](https://img.ly/docs/cesdk/vue/api/engine/type-aliases/color/) | The highlight color for placeholder elements. |
| `progressColor` | [`Color`](https://img.ly/docs/cesdk/vue/api/engine/type-aliases/color/) | The color indicating progress or loading states. |
| `rotationSnappingGuideColor` | [`Color`](https://img.ly/docs/cesdk/vue/api/engine/type-aliases/color/) | The color of rotation snapping guide lines. |
| `ruleOfThirdsLineColor` | [`Color`](https://img.ly/docs/cesdk/vue/api/engine/type-aliases/color/) | The color of rule of thirds guide lines. |
| `snappingGuideColor` | [`Color`](https://img.ly/docs/cesdk/vue/api/engine/type-aliases/color/) | The color of snapping guide lines. |
| `textVariableHighlightColor` | [`Color`](https://img.ly/docs/cesdk/vue/api/engine/type-aliases/color/) | The highlight color for text variables. |
| `handleFillColor` | [`Color`](https://img.ly/docs/cesdk/vue/api/engine/type-aliases/color/) | The fill color for handles. |
| `doubleClickSelectionMode` | `"Direct"` | `"Hierarchical"` |
| `touch/pinchAction` | `"None"` | `"Zoom"` |
| `touch/rotateAction` | `"None"` | `"Rotate"` |
| `camera/clamping/overshootMode` | `"Center"` | `"Reverse"` |
| `dock/iconSize` | `"normal"` | `"large"` |

---



[Source](https:/img.ly/docs/cesdk/vue/api/engine/interfaces/rgbacolor)