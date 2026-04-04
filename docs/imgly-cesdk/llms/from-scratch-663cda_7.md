# Source: https://img.ly/docs/cesdk/macos/create-templates/from-scratch-663cda/

---
title: "Create From Scratch"
description: "Build and save reusable CE.SDK templates in Swift for iOS, macOS, and Mac Catalyst."
platform: macos
url: "https://img.ly/docs/cesdk/macos/create-templates/from-scratch-663cda/"
---

> This is one page of the CE.SDK macOS documentation. For a complete overview, see the [macOS Documentation Index](https://img.ly/docs/cesdk/macos.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/macos/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/macos/guides-8d8b00/) > [Create and Use Templates](https://img.ly/docs/cesdk/macos/create-templates-3aef79/) > [Create From Scratch](https://img.ly/docs/cesdk/macos/create-templates/from-scratch-663cda/)

---

Templates define a reusable design with pattern—text regions, image placeholders, and locked brand elements that your app can populate at runtime. This guide walks you through creating a template **from scratch** in Swift, enabling placeholder behavior and variable bindings, and saving the result as a string or archive for reuse.

## What You’ll Learn

- Differences between **templates** and **scenes**.
- Programmatically build a template scene.
- Enable **placeholder behavior** and **variable** bindings.
- Save templates to **string** or **archive**.
- Store basic **metadata** for library use.

## When to Use It

Choose this guide when you need to **author** templates programmatically for things such as:

- Automation pipelines
- Unit tests
- Code‑generated layouts.

Prefer the web-based CE.SDK editors if your goal is to let designers craft rich templates visually including:

- Marking placeholders.
- Locking styles.
- Setting edit permissions.

## Templates vs Scenes

- **Scene**: a complete document (pages, blocks, assets). Edit and export it directly.
- **Template**: a reusable pattern applied to scenes; often includes placeholders and variables to control what’s editable versus locked.

## Create Templates Programmatically

The web-based CE.SDK editors include built-in template logic and UI. You can use them to:

- Mark blocks as placeholders
- Bind variables
- Assign granular edit permissions.

For most teams, this is the recommended path to author templates.

This guide shows how to achieve similar results **in Swift**, which is useful for code‑driven generation, CI pipelines, or dynamic authoring.

In the code below:

- You’ll create a scene.
- Add a page.
- Insert a text block bound to a variable
- Add an image block with placeholder behavior.

```swift
let scene = try engine.scene.create()
let page = try engine.block.create(.page)
try engine.block.appendChild(to: scene, child: page)

// Text block bound to a variable (e.g., {{name}})
let text = try engine.block.create(.text)
try engine.block.setString(text, property: "text/text", value: "\{\{name\}\}")
try engine.block.setPositionX(text, value: 0.1)
try engine.block.setPositionY(text, value: 0.1)
try engine.block.appendChild(to: page, child: text)

// Image block acting as a placeholder
let image = try engine.block.create(.graphic)
if try engine.block.supportsPlaceholderBehavior(image) {
    try engine.block.setPlaceholderBehaviorEnabled(image, enabled: true)
}

try engine.block.setWidth(image, value: 300)
try engine.block.setHeight(image, value: 200)
try engine.block.setPositionX(image, value: 0.1)
try engine.block.setPositionY(image, value: 0.3)
try engine.block.appendChild(to: page, child: image)
```

## Binding Variables

- Use variables for [text substitution](https://img.ly/docs/cesdk/macos/create-templates/add-dynamic-content/text-variables-7ecb50/).
- Use [placeholders for media](https://img.ly/docs/cesdk/macos/create-templates/add-dynamic-content/placeholders-d9ba8a/) the user swaps at runtime.

Define a variable in text using curly brackets. The variable can be the entire string or part of a string, such as "Hello, \{\{guest\_name}}"

Placeholder behavior works as follows:

- Visible only in one of CE.SDK’s predefined editors (iOS or web).
- In CI or headless workflows: replace the fill URL of the placeholder block directly rather than relying on interactive placeholder behavior.

## Saving Templates

Templates are scenes with some extra settings. Save templates:

- Use the same logic as for scenes.
- Save as a **string** for a lightweight file: the template needs to be able to resolve all asset URLs at runtime.
- Save as an **archive** for a self contained, portable file: bundles the assets into the file.

```swift
let sceneAsString = try await engine.scene.saveToString()
// Persist to your DB or send to a backend
```

```swift
let blob = try await engine.scene.saveToArchive()
// Upload or store `blob` as a portable template package
```

Once you’ve created the string or data blob, use standard methods to persist it.

## Add Template Metadata

Like other assets, you can:

- Load templates into the [asset library](https://img.ly/docs/cesdk/macos/import-media/asset-library-65d6c4/).
- Store metadata in your CMS or local database.
- Use the saved metadata later when you register the template as an `AssetDefinition` in an `AssetSource`.

That way the UI can display names, thumbnails and, categories.

## Lock Template Properties

Templates can restrict editing at runtime so that users don’t edit any part of the design that should remain static. To protect integrity, you can lock properties such as:

- Position
- Size
- Color
- Fill

The guide for [locking templates](https://img.ly/docs/cesdk/macos/create-templates/lock-131489/) provides details on which properties are lockable and how to set up editor and adopter rules.

## Troubleshooting

**❌ Placeholders not working**:

- Confirm the block type supports placeholder behavior before enabling it.
- Make sure that you have set up the correct permissions on the block and that the `"fill/change"` property isn’t locked.

**❌ Missing fonts/images at runtime**:

- Use an archive save to embed assets into a template for portability.
- Ensure that the asset URIs are reachable and stable.

## Next Steps

Now that you can create templates, some related topics you may find helpful are:

- [Generate scenes](https://img.ly/docs/cesdk/macos/use-templates/generate-334e15/) with templates as the source.
- [Apply templates](https://img.ly/docs/cesdk/macos/use-templates/apply-template-35c73e/) to existing scenes.
- Work with [dynamic content](https://img.ly/docs/cesdk/macos/create-templates/add-dynamic-content-53fad7/) to update templates at runtime



---

## More Resources

- **[macOS Documentation Index](https://img.ly/docs/cesdk/macos.md)** - Browse all macOS documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/macos/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/macos/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
