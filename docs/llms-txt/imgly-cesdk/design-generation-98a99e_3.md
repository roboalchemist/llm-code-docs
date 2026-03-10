# Source: https://img.ly/docs/cesdk/ios/automation/design-generation-98a99e/

---
title: "Automate Design Generation"
description: "Generate on-brand designs programmatically using templates, variables, and CE.SDK’s headless API."
platform: ios
url: "https://img.ly/docs/cesdk/ios/automation/design-generation-98a99e/"
---

> This is one page of the CE.SDK iOS documentation. For a complete overview, see the [iOS Documentation Index](https://img.ly/docs/cesdk/ios.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/ios/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/ios/guides-8d8b00/) > [Automate Workflows](https://img.ly/docs/cesdk/ios/automation-715209/) > [Design Generation](https://img.ly/docs/cesdk/ios/automation/design-generation-98a99e/)

---

Automate on-brand output at scale. Feed data (JSON, APIs, user input) into CE.SDK templates and export print- or web-ready assets. No manual editing required. This guide shows the Swift/iOS workflow using the headless engine.

## What You’ll Learn

- Load a template scene from bundle or URL.
- Populate **text variables** via the variable API.
- Replace **images** by updating a block’s image fill.
- Export to PDF/PNG/JPEG and batch the whole process.

## When to Use It

Use automation when you need to mass-produce personalized postcards, product cards, certificates, multi-locale variants, or nightly batch refreshes—either fully headless or hybrid with UI confirmation.

## Load a Template

You can host templated scenes on your CDN or bundle them with the app. Once you start the engine:

1. Load the template you want to populate.
2. Display the template with UI, use it headless, or mix and match.

```swift
import IMGLYEngine

let engine = try Engine(license: "<your license key>")

let templateURL = URL(string:
  "https://cdn.img.ly/assets/demo/v3/ly.img.template/templates/cesdk_postcard_2.scene"
)!
try await engine.scene.load(from: templateURL)
```

## Inject Dynamic Data

Templates expose placeholders for dynamic content. Text tokens, such as \{\{first\_name}}, are set through the variable API. This is typically a straight mapping from your data model to the variable keys you’ve designed into the scene.

```swift
try engine.variable.set(key: "first_name", value: "John")
try engine.variable.set(key: "last_name",  value: "DuPont")
try engine.variable.set(key: "address",    value: "123 Main St.")
try engine.variable.set(key: "city",       value: "Anytown")
```

If you prefer to discover what the template expects:

1. List the keys.
2. Fill them from your data store.

```swift
let keys = engine.variable.findAll()
// assert or log missing keys before a long batch run
```

This approach scales well for batch jobs and minimizes key-mismatch errors.

## Replace Images via Image Fill

Image placeholders in templates are just graphic blocks that use an image fill. To swap the picture, point the fill to your asset’s URL. In production, you’ll usually:

1. Target a specific block (via your own metadata or naming convention).
2. Set the file URI.

```swift
let graphic = try engine.block.find(byType: .graphic).first!
let imageFill = try engine.block.createFill(.image)
try engine.block.setFill(graphic, fill: imageFill)

try engine.block.setString(
  imageFill,
  property: "fill/image/fileURI",
  value: "https://cdn.example.com/assets/photo_001.jpg"
)
```

This property path sets the image file used by the fill. This is ideal for server-hosted libraries or results fetched from your API.

## Export the Final Design

After the template is populated, export the scene to your desired format (PDF for print, PNG/JPEG for web). In a batch flow, you’ll typically:

1. Export
2. Store or upload
3. Loop to the next record.

```swift
guard let scene = try engine.scene.get() else { fatalError("No scene") }
let pdfData = try await engine.block.export(scene, mimeType: .pdf)

let url = FileManager.default.temporaryDirectory.appendingPathComponent("Postcard.pdf")
try pdfData.write(to: url)
```

## Batch It

Automation shines when you repeat the same steps for many records. You can:

1. Load the template **once**.
2. Map your model into variables.
3. (Optional) Swap imagery
4. Export.

You can either:

- Run the preceding process completely headless.
- Pause between steps to let a user approve variants in the UI (if your workflow calls for it).

```swift
struct Recipient {
  let firstName: String
  let lastName: String
  let address: String
  let city: String
  let photoURL: URL
}

for recipient in recipients {
  try engine.variable.set(key: "first_name", value: recipient.firstName)
  try engine.variable.set(key: "last_name",  value: recipient.lastName)
  try engine.variable.set(key: "address",    value: recipient.address)
  try engine.variable.set(key: "city",       value: recipient.city)

  let graphic = try engine.block.find(byType: .graphic).first!
  let imageFill = try engine.block.createFill(.image)
  try engine.block.setFill(graphic, fill: imageFill)
  try engine.block.setString(imageFill, property: "fill/image/fileURI", value: recipient.photoURL.absoluteString)

  _ = try await engine.block.export(try engine.scene.get()!, mimeType: .pdf)
}
```

## Troubleshooting

**❌ Text didn’t update**:

- Confirm variable names match the template’s tokens exactly; enumerating keys first helps prevent mismatches.

**❌ Image didn’t change**:

- Ensure you’re setting the image file on an image fill and that the fill is applied to the target block.

**❌ Export is empty**:

- Verify the scene is loaded and you’re exporting the correct node (usually the scene).

**❌ Print colors look off**:

- Prepare templates with appropriate print settings and export to PDF for print workflows.

## Next Steps

Now that you’ve seen the general workflow for design generation, explore some of these topics to fine tune your projects.

- [Create Templates](https://img.ly/docs/cesdk/ios/create-templates/overview-4ebe30/) – design for automation and add variables/placeholders.
- [Automate Workflows](https://img.ly/docs/cesdk/ios/automation-715209/) – patterns for client/server and hybrid flows.
- [Export Overview](https://img.ly/docs/cesdk/ios/export-save-publish/export-82f968/) – formats, presets, and print-ready output.



---

## More Resources

- **[iOS Documentation Index](https://img.ly/docs/cesdk/ios.md)** - Browse all iOS documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/ios/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/ios/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
