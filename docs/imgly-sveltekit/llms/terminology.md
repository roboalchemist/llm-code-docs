# Terminology

A reference guide to the core terms and concepts used throughout CE.SDK documentation.

CE.SDK uses consistent terminology across all platforms. Understanding what we call things helps you navigate the API, read documentation efficiently, and communicate effectively with other developers working on CE.SDK integration.

## Core Architecture[#](#core-architecture)

### Engine[#](#engine)

All operations—creating scenes, manipulating blocks, rendering, and exporting—go through the _Engine_. Initialize it once and use it throughout your application’s lifecycle.

### Scene[#](#scene)

The root container for all design content. A _Scene_ contains _Pages_, which contain _Blocks_. Only one _Scene_ can be active per _Engine_ instance. You can create a _Scene_ programmatically or load one from a file.

_Scenes_ operate in one of two modes:

*   **Design Mode**: Static designs like social posts, print materials, and graphics
*   **Video Mode**: Timeline-based content with duration, playback, and animation

See [Scenes](sveltekit/concepts/scenes-e8596d/) for details.

### Page[#](#page)

_Pages_ are containers within a _Scene_ that hold content _Blocks_ (see below) and define working area dimensions.

In _Design Mode_, pages are individual artboards. In _Video Mode_, pages are timeline compositions where _Blocks_ are arranged across time. See [Pages](sveltekit/concepts/pages-7b6bae/) for details.

### Block[#](#block)

The fundamental building unit in CE.SDK. Everything visible in a design is a _Block_—images, text, shapes, graphics, audio, video—and even _Pages_ themselves. _Blocks_ form a parent-child hierarchy.

Each _Block_ has two identifiers:

*   **DesignBlockId**: A numeric handle (integer) used in API calls
*   **UUID**: A stable string identifier that persists across save and load operations

See [Blocks](sveltekit/concepts/blocks-90241e/) for details.

## Block Anatomy[#](#block-anatomy)

Modify a _Block’s_ appearance and behavior by attaching _Fills_, _Shapes_, and _Effects_. Most of these modifiers must be created separately and then attached to a _Block_.

### Fill[#](#fill)

_Fills_ cover the surface of a _Block’s_ shape:

*   **Color Fill**: Solid color
*   **Gradient Fill**: Linear, radial, or conical gradients
*   **Image Fill**: Image content
*   **Video Fill**: Video content

See the [Color Fills](sveltekit/fills/color-7129cd/) , [Gradient Fills](sveltekit/filters-and-effects/gradients-0ff079/) , [Image Fills](sveltekit/fills/image-e9cb5c/) , and [Video Fills](sveltekit/fills/video-ec7f9f/) guides.

### Shape[#](#shape)

_Shapes_ define a _Block’s_ outline and dimensions, determining the silhouette and how the _Fill_ is clipped. _Shape_ types include:

*   **Rect**: Rectangles and squares
*   **Ellipse**: Circles and ovals
*   **Polygon**: Multi-sided shapes
*   **Star**: Star shapes with configurable points
*   **Line**: Straight lines
*   **Vector Path**: Custom vector shapes

Like _Fills_, _Shapes_ are created separately and attached to _Blocks_. See [Shapes](sveltekit/shapes-9f1b2c/) for details.

### Effect[#](#effect)

_Effects_ are non-destructive visual modifications applied to a _Block_. Multiple _Effects_ can be stacked. _Effect_ categories include:

*   **Adjustments**: Brightness, contrast, saturation, and other image corrections
*   **Filters**: LUT-based color grading, duotone
*   **Stylization**: Pixelize, posterize, half-tone, dot pattern, linocut, outliner
*   **Distortion**: Liquid, mirror, shifter, cross-cut, extrude blur
*   **Focus**: Tilt-shift, vignette
*   **Color**: Recolor, green screen (chroma key)
*   **Other**: Glow, TV glitch

The order determines how multiple effects attached to a single block interact. See [Filters and Effects](sveltekit/filters-and-effects-6f88ac/) for details.

### Blur[#](#blur)

A modifier that reduces sharpness. _Blur_ types include:

*   **Uniform Blur**: Even blur across the entire block
*   **Radial Blur**: Circular blur from a center point
*   **Mirrored Blur**: Blur with reflection

**Blur has a dedicated API because it composites differently than other effects.** While most effects like brightness or saturation operate only on a block’s own pixels, blur needs to sample pixels from the surrounding area to calculate the blurred result. This means blur interacts with the scene’s layering and transparency in ways other effects don’t—when you blur a partially transparent block, the engine must handle how that blur blends with whatever content sits behind it.

See [Blur](sveltekit/filters-and-effects/blur-71d642/) for details.

### Drop Shadow[#](#drop-shadow)

A built-in block property (not an _Effect_) that renders a shadow beneath blocks. _Drop Shadow_ has dedicated API methods for enabling, color, offset, and blur radius.

Unlike effects, drop shadow is configured directly on the block rather than created and attached separately.

## Block Handling[#](#block-handling)

These terms describe how _Blocks_ are categorized and identified.

### Type[#](#type)

The built-in _Type_ defines a _Block’s_ core behavior and available properties. _Type_ is immutable—you choose it when creating the _Block_.

*   `//ly.img.ubq/graphic` — Visual block for images, shapes, and graphics
*   `//ly.img.ubq/text` — Text content
*   `//ly.img.ubq/audio` — Audio content
*   `//ly.img.ubq/page` — Page container
*   `//ly.img.ubq/scene` — Root scene container
*   `//ly.img.ubq/track` — Video timeline track
*   `//ly.img.ubq/stack` — Stack container for layering
*   `//ly.img.ubq/group` — Group container for organizing blocks
*   `//ly.img.ubq/camera` — Camera for scene viewing
*   `//ly.img.ubq/cutout` — Cutout/mask block
*   `//ly.img.ubq/caption` — Caption/subtitle block
*   `//ly.img.ubq/captionTrack` — Track for captions

The _Type_ determines which properties and capabilities a _Block_ has.

### Kind[#](#kind)

A custom string label you assign to categorize _Blocks_ for your application. Unlike _Type_, _Kind_ is mutable and application-defined. Changing the _Kind_ has no effect on appearance or behavior at the engine level. You can query and search for _Blocks_ by _Kind_. Common uses:

*   Categorizing template elements (“logo”, “headline”, “background”)
*   Filtering blocks for custom UI
*   Automation workflows that process blocks by purpose

### Property[#](#property)

A configurable attribute of a _Block_. _Properties_ have types (`Bool`, `Int`, `Float`, `String`, `Color`, `Enum`) and paths like `text/fontSize` or `fill/image/imageFileURI`.

Access _Properties_ using type-specific getter and setter methods. Each _Block_ type exposes different properties, which you can discover programmatically. See [Blocks](sveltekit/concepts/blocks-90241e/) for details.

## Assets and Resources[#](#assets-and-resources)

### Asset[#](#asset)

Think of _Assets_ as media items that you can provide to your users: images, videos, audio files, fonts, stickers, or templates—anything that can be added to a design. _Assets_ have metadata including:

*   **ID**: Unique identifier within an asset source
*   **Label**: Display name
*   **Meta**: Custom metadata (URI, dimensions, format)
*   **Thumbnail URI**: Preview image URL

_Assets_ are provided by _Asset Sources_ and added through the UI or programmatically.

### Asset Source[#](#asset-source)

A provider of _Assets_. _Asset Sources_ can be built-in (like the default sticker library) or custom. _Asset Sources_ implement a query interface returning paginated results with search and filtering.

*   **Local Asset Source**: Assets defined in JSON, loaded at initialization
*   **Remote Asset Source**: Custom implementation fetching from external APIs

Register _Asset Sources_ with the _Engine_ to make _Assets_ available throughout your application.

### Resource[#](#resource)

Loaded data from an _Asset_ URI. When you reference an image or video URL in a _Block_, the _Engine_ fetches and caches the _Resource_. _Resources_ include binary data and metadata for rendering. See [Resources](sveltekit/concepts/resources-a58d71/) for details.

### Buffer[#](#buffer)

A resizable container for arbitrary binary data. _Buffers_ are useful for dynamically generated content that doesn’t come from a URL, such as synthesized audio or programmatically created images.

Create a _Buffer_, write data to it, and reference it by URI in _Block_ properties. _Buffer_ data is not serialized with scenes and changes cannot be undone. See [Buffers](sveltekit/concepts/buffers-9c565b/) for details.

## Templating and Automation[#](#templating-and-automation)

These terms describe dynamic content and reusable designs.

### Template[#](#template)

A reusable design with predefined structure and styling. _Templates_ typically contain _Placeholders_ and _Variables_ that users customize while maintaining overall layout and branding.

_Templates_ are scenes saved in a format that can be loaded and modified.

### Placeholder[#](#placeholder)

A _Block_ marked for content replacement. When a _Block’s_ placeholder property is enabled, it signals that the _Block_ expects user-provided content—an image drop zone or editable text field.

_Placeholders_ indicate which parts of a design should be customized versus fixed. See [Placeholders](sveltekit/create-templates/add-dynamic-content/placeholders-d9ba8a/) for details.

### Variable[#](#variable)

A named value referenced in text blocks using `{{variableName}}` syntax. _Variables_ enable data-driven design generation by populating templates with dynamic content.

Define _Variables_ at the scene level and reference them in text blocks. When a _Variable_ value changes, all referencing text blocks update automatically. See [Text Variables](sveltekit/create-templates/add-dynamic-content/text-variables-7ecb50/) for details.

## Permissions and Scopes[#](#permissions-and-scopes)

These terms relate to controlling what operations are allowed.

### Scope[#](#scope)

A permission setting controlling whether specific operations are allowed on a _Block_. _Scopes_ enable fine-grained control over what users can modify—essential for template workflows where some elements should be editable and others locked.

Common scopes:

*   `layer/move` — Allow or prevent moving
*   `layer/resize` — Allow or prevent resizing
*   `layer/rotate` — Allow or prevent rotation
*   `layer/visibility` — Allow or prevent hiding
*   `lifecycle/destroy` — Allow or prevent deletion
*   `editor/select` — Allow or prevent selection

Enable or disable _Scopes_ per _Block_ to create controlled editing experiences. See [Lock Design Elements](sveltekit/create-templates/lock-131489/) for details.

### Role[#](#role)

A preset collection of _Scope_ settings. CE.SDK defines two built-in _Roles_:

*   **Creator**: Full access to all operations, for template authors
*   **Adopter**: Restricted access for end-users customizing templates

_Roles_ provide a convenient way to apply consistent permission sets.

## Layout and Units[#](#layout-and-units)

These terms relate to positioning and measurement.

### Design Unit[#](#design-unit)

The measurement unit for dimensions in a _Scene_. The choice affects how positions, sizes, and exports are interpreted. Options:

*   **Pixel**: Screen pixels, default for digital designs
*   **Millimeter**: Metric measurement for print
*   **Inch**: Imperial measurement for print

Set the design unit at the scene level—all dimension values are interpreted in that unit. See [Design Units](sveltekit/concepts/design-units-cc6597/) for details.

### DPI (Dots Per Inch)[#](#dpi-dots-per-inch)

Resolution setting affecting export quality and unit conversion. Higher DPI produces larger exports with more detail. The default is 300 DPI, suitable for print-quality output.

DPI matters when working with physical units (millimeters, inches) as it determines how measurements translate to pixel dimensions during export.

## Operating Modes[#](#operating-modes)

These terms describe how CE.SDK runs.

### Scene Mode[#](#scene-mode)

The operational mode of a _Scene_ determining available features:

*   **Design Mode**: Static designs. No timeline, no playback. Content arranged spatially on pages.
*   **Video Mode**: Time-based content. Includes timeline, playback controls, duration properties, and animations.

Choose the mode when creating a scene—it affects which properties and operations are available. See [Scenes](sveltekit/concepts/scenes-e8596d/) for details.

### Headless Mode[#](#headless-mode)

Running CE.SDK without the built-in UI. Used for:

*   Server-side rendering and export
*   Automation pipelines
*   Custom UI implementations
*   Batch processing

In _Headless Mode_, you work directly with _Engine_ APIs without the visual editor. See [Headless Mode](sveltekit/concepts/headless-mode/browser-24ab98/) for setup.

## Events and State[#](#events-and-state)

These terms relate to monitoring changes.

### Event / Subscription[#](#event--subscription)

A callback mechanism for reacting to changes in the _Engine_. Subscribe to events and receive notifications when state changes. Common events:

*   Selection changes
*   Block state changes
*   History (undo/redo) changes

Subscriptions return an unsubscribe function to call when you no longer need notifications. See [Events](sveltekit/concepts/events-353f97/) for details.

### Block State[#](#block-state)

The current status of a _Block_ indicating readiness or issues:

*   **Ready**: Normal state, no pending operations
*   **Pending**: Operation in progress, with optional progress value (0-1)
*   **Error**: Operation failed, with error type (`ImageDecoding`, `VideoDecoding`, `FileFetch`, etc.)

_Block State_ reflects the combined status of the _Block_ and its attached _Fill_, _Shape_, and _Effects_.

---



[Source](https:/img.ly/docs/cesdk/sveltekit/concepts/templating-f94385)