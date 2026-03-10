# Source: https://img.ly/docs/cesdk/ios/use-templates/generate-334e15/

---
title: "Generate From Templates"
description: "Learn how to load, apply, and populate CE.SDK templates in Swift for iOS, macOS, and Mac Catalyst."
platform: ios
url: "https://img.ly/docs/cesdk/ios/use-templates/generate-334e15/"
---

> This is one page of the CE.SDK iOS documentation. For a complete overview, see the [iOS Documentation Index](https://img.ly/docs/cesdk/ios.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/ios/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/ios/guides-8d8b00/) > [Create and Use Templates](https://img.ly/docs/cesdk/ios/create-templates-3aef79/) > [Generate From Template](https://img.ly/docs/cesdk/ios/use-templates/generate-334e15/)

---

Once you create templates, either in CE.SDK’s web-based editor or programmatically, your app can load and apply them to scenes at runtime. This guide explains **how to load templates**, populate them with variables and images, and use template libraries to integrate them into your app.

## What You’ll Learn

- Load and apply templates from string or URL.
- Launch the editor with a template as the initial scene.
- Populate templates with dynamic content using variables and placeholders.
- Create custom template libraries with thumbnails and metadata.
- Adapt templates automatically to target dimensions.

## When to Use It

Use this guide when your app needs to **load and apply existing templates** to generate new scenes, such as:

- Starting from a brand template.
- Building a “Start from Template” screen.
- Populating designs dynamically with user or product data.

## Applying Templates

A template can replace or populate an existing scene while keeping the current page size and units.

### Apply from String

Use `.applyTemplate(from:)` with a `String` when you’ve saved the template using `.saveToString()` or when your back-end returns the raw string encoding instead of a `.scene` file or a `Blob`.

```swift
try await engine.scene.applyTemplate(from: "UBQ1ewoiZm9ybWF0Ij...")
```

### Apply from URL

```swift
let url = URL(string: "https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_postcard_1.scene")!
try await engine.scene.applyTemplate(from: url)
```

When applying a template to an existing scene, CE.SDK automatically adjusts template content to fit the current scene’s dimensions.

> **Note:** When using a prebuilt editor, end users can do these actions:* Visually replace images by drag-and-drop.
> * Update text directly in the editor interface.In code-only, CI, or headless workflows, you must replace media or text programmatically by:* Changing the fill URI for images
> * Updating variable text values in code.

## Loading Templates as Scenes

Instead of applying a template to an existing scene, you can load a template as the active scene when you either:

- Start the engine.
- Launch a prebuilt editor with a template as the active scene.

This is ideal when you want to either:

- Open directly into a predefined layout.
- Start an editing session from a template.

### Load from String

```swift
try await engine.scene.load(from: "UBQ1ewoiZm9ybWF0Ij...")
```

### Load from URL

```swift
let url = URL(string: "https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_postcard_1.scene")!
try await engine.scene.load(from: url)
```

### Load from Archive

Use `.loadArchive(from:)` when you've saved the template using `.saveToArchive()` to bundle resources.

```swift
let url = URL(string: "https://cdn.img.ly/assets/demo/postcard.archive")!
try await engine.scene.loaArchive(from: url)
```

The preceding code would typically appear in the `.imgly.onCreate` modifier when using one of the prebuilt editors.

## Comparison

| Use Case | Method | Behavior|
|---|---|---|
|Apply a template to an existing design|.applyTemplate(from:) |Merges the template layout into the current scene while preserving size|
|Launch with a predefined template|.load(from:)|The template becomes the initial scene|
|Automate batch generation|Headless mode .load(from:)|Loads and renders templates programmatically|

## Template Libraries

You can present templates in the Asset Library along with other assets via a custom `AssetSource`. Each entry includes metadata that points to your template file and a preview image.

## Dynamic Population (Variables & Placeholders)

Templates can include variable placeholders like \{\{name}} or image placeholders. Your app can inject values at runtime.

> **Note:** Interactive placeholder behavior (tap-to-replace, drag-drop) is available only in **CE.SDK’s predefined editors**.In **code-only, CI, or headless workflows**, use the `Variable` and `Block` APIs to replace media by:* Updating the image fill URI.
> * Updating text via variables.

```swift
// Example: Replace an image by setting a new fill URI
try engine.block.setString(block, property: "fill/image/imageFileURI", value: "https://cdn.example.com/images/new_photo.jpg")
```

```swift
// Example: Update a variable-based text field
try engine.variable.set(key: "name", value: "Chris")
```

## Template Adaptation

When you apply a template, CE.SDK keeps the current scene’s design unit and page size, automatically fitting the template content to match the target dimensions. This makes it easy to reuse templates for multiple aspect ratios.

## Troubleshooting

**❌ Wrong size or scaling**:

- Ensure the scene is initialized with the correct dimensions before applying the template.

**❌ Missing assets**:

- Confirm that external URLs or archives are accessible.

**❌ Text variables not updating**:

- Check that variable keys match the placeholders used.

## Next Steps

Now that you can generate creations from templates, some related topics you may find helpful are:

- [Create templates](https://img.ly/docs/cesdk/ios/create-templates/from-scratch-663cda/) from scratch.
- [Apply templates](https://img.ly/docs/cesdk/ios/use-templates/apply-template-35c73e/) to existing scenes.
- Work with [dynamic content](https://img.ly/docs/cesdk/ios/create-templates/add-dynamic-content-53fad7/) to update templates at runtime.



---

## More Resources

- **[iOS Documentation Index](https://img.ly/docs/cesdk/ios.md)** - Browse all iOS documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/ios/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/ios/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
