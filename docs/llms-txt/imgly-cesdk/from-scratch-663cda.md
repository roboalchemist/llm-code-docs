# Source: https://img.ly/docs/cesdk/android/create-templates/from-scratch-663cda/

---
title: "Create Templates From Scratch in Android (Kotlin)"
description: "Build and save reusable CE.SDK templates programmatically in Android using Kotlin."
platform: android
url: "https://img.ly/docs/cesdk/android/create-templates/from-scratch-663cda/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [Create and Use Templates](https://img.ly/docs/cesdk/android/create-templates-3aef79/) > [Create From Scratch](https://img.ly/docs/cesdk/android/create-templates/from-scratch-663cda/)

---

Templates define a reusable design pattern—text regions, image placeholders, and locked brand elements that your app can populate at runtime. This guide walks you through creating a template **from scratch** in Android using Kotlin, enabling variable bindings, and saving the result as a string or archive for reuse.

## What You'll Learn

- Differences between **templates** and **scenes**.
- Programmatically build a template scene.
- Enable **variable** bindings for dynamic text.
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
- **Template**: a reusable pattern applied to scenes; often includes placeholders and variables to control what's editable versus locked.

## Create Templates Programmatically

The web-based CE.SDK editors include built-in template logic and UI. You can use them to:

- Mark blocks as placeholders
- Bind variables
- Assign granular edit permissions.

For most teams, this is the recommended path to author templates.

This guide shows how to achieve similar results **in Android/Kotlin**, which is useful for code‑driven generation, CI pipelines, or dynamic authoring.

In the code below:

- You'll create a scene.
- Add a page.
- Insert a text block bound to a variable
- Add an image block.

```kotlin
import ly.img.engine.DesignBlockType
import ly.img.engine.Engine
import ly.img.engine.FillType
import ly.img.engine.ShapeType

val scene = engine.scene.create()
val page = engine.block.create(DesignBlockType.Page)
engine.block.appendChild(parent = scene, child = page)

// Text block bound to a variable (e.g., {{name}})
val text = engine.block.create(DesignBlockType.Text)
engine.block.setString(text, property = "text/text", value = "{{name}}")
engine.block.setPositionX(text, value = 0.1F)
engine.block.setPositionY(text, value = 0.1F)
engine.block.appendChild(parent = page, child = text)

// Image block for dynamic content
val image = engine.block.create(DesignBlockType.Graphic)
val shape = engine.block.createShape(ShapeType.Rect)
engine.block.setShape(image, shape = shape)

val imageFill = engine.block.createFill(FillType.Image)
engine.block.setFill(image, fill = imageFill)

engine.block.setWidth(image, value = 300F)
engine.block.setHeight(image, value = 200F)
engine.block.setPositionX(image, value = 0.1F)
engine.block.setPositionY(image, value = 0.3F)
engine.block.appendChild(parent = page, child = image)
```

## Binding Variables

- Use variables for [text substitution](https://img.ly/docs/cesdk/android/create-templates/add-dynamic-content/text-variables-7ecb50/).
- Use named blocks or image fills for media that users swap at runtime.

Define a variable in text using curly brackets. The variable can be the entire string or part of a string, such as `"Hello, {{guest_name}}"`.

To populate variables at runtime:

```kotlin
import ly.img.engine.Engine

// Populate the template with actual data
engine.variable.set(key = "name", value = "John Smith")
engine.variable.set(key = "guest_name", value = "Alice")
```

For image replacement in templates, use named blocks:

```kotlin
import ly.img.engine.Engine

// Give the image block a name for easy lookup
engine.block.setString(imageBlock, property = "name", value = "profile-photo")

// Later, find and replace the image fill
val blocks = engine.block.findByType(DesignBlockType.Graphic)
for (block in blocks) {
    val name = engine.block.getString(block, property = "name")
    if (name == "profile-photo") {
        val fill = engine.block.getFill(block)
        engine.block.setString(fill, property = "fill/image/imageFileURI", value = "https://example.com/photo.jpg")
    }
}
```

## Saving Templates

Templates are scenes with some extra settings. Save templates:

- Use the same logic as for scenes.
- Save as a **string** for a lightweight file: the template needs to be able to resolve all asset URLs at runtime.
- Save as an **archive** for a self-contained, portable file: bundles the assets into the file.

### Save as String

```kotlin
import ly.img.engine.Engine

val sceneAsString = engine.scene.saveToString(scene = scene)
// Persist to your DB or send to a backend
```

### Save as Archive

```kotlin
import android.content.Context
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import ly.img.engine.Engine
import java.io.File

suspend fun saveTemplateAsArchive(
    engine: Engine,
    context: Context,
    scene: Int
): File {
    val blob = engine.scene.saveToArchive(scene = scene)
    
    // Save to file
    val file = File(context.filesDir, "template_${System.currentTimeMillis()}.cesdk")
    withContext(Dispatchers.IO) {
        file.outputStream().channel.use { channel ->
            channel.write(blob)
        }
    }
    
    return file
}
```

Once you've created the string or data blob, use standard methods to persist it.

## Complete Example

Here's a complete example that creates a template from scratch:

```kotlin
import android.content.Context
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext
import ly.img.engine.Color
import ly.img.engine.DesignBlockType
import ly.img.engine.Engine
import ly.img.engine.FillType
import ly.img.engine.ShapeType
import ly.img.engine.SizeMode
import java.io.File

fun createTemplateFromScratch(
    context: Context,
    license: String,
    userId: String
) = CoroutineScope(Dispatchers.Main).launch {
    val engine = Engine.getInstance(id = "ly.img.engine.template")
    engine.start(license = license, userId = userId)
    engine.bindOffscreen(width = 1080, height = 1920)
    
    try {
        // Create scene and page
        val scene = engine.scene.create()
        val page = engine.block.create(DesignBlockType.Page)
        engine.block.appendChild(parent = scene, child = page)
        engine.block.setWidth(page, value = 1080F)
        engine.block.setHeight(page, value = 1920F)
        
        // Background (brand color that stays locked)
        val background = engine.block.create(DesignBlockType.Graphic)
        val bgShape = engine.block.createShape(ShapeType.Rect)
        engine.block.setShape(background, shape = bgShape)
        
        val bgFill = engine.block.createFill(FillType.Color)
        val bgColor = Color.fromRGBA(r = 0.95F, g = 0.95F, b = 0.98F, a = 1.0F)
        engine.block.setColor(bgFill, property = "fill/color/value", color = bgColor)
        engine.block.setFill(background, fill = bgFill)
        
        engine.block.appendChild(parent = page, child = background)
        engine.block.fillParent(background)
        engine.block.sendToBack(background)
        
        // Title text with variable
        val title = engine.block.create(DesignBlockType.Text)
        engine.block.setString(title, property = "text/text", value = "{{product_name}}")
        engine.block.setTextFontSize(title, fontSize = 48F)
        engine.block.setWidthMode(title, mode = SizeMode.AUTO)
        engine.block.setHeightMode(title, mode = SizeMode.AUTO)
        engine.block.setPositionX(title, value = 100F)
        engine.block.setPositionY(title, value = 200F)
        engine.block.appendChild(parent = page, child = title)
        
        // Description text with variable
        val description = engine.block.create(DesignBlockType.Text)
        engine.block.setString(description, property = "text/text", value = "{{description}}")
        engine.block.setTextFontSize(description, fontSize = 24F)
        engine.block.setWidthMode(description, mode = SizeMode.AUTO)
        engine.block.setHeightMode(description, mode = SizeMode.AUTO)
        engine.block.setPositionX(description, value = 100F)
        engine.block.setPositionY(description, value = 300F)
        engine.block.appendChild(parent = page, child = description)
        
        // Product image placeholder (named for easy replacement)
        val productImage = engine.block.create(DesignBlockType.Graphic)
        val imageShape = engine.block.createShape(ShapeType.Rect)
        engine.block.setShape(productImage, shape = imageShape)
        
        val imageFill = engine.block.createFill(FillType.Image)
        // Set a placeholder image URL
        engine.block.setString(
            imageFill,
            property = "fill/image/imageFileURI",
            value = "https://img.ly/static/ubq_samples/sample_1.jpg"
        )
        engine.block.setFill(productImage, fill = imageFill)
        
        // Name it for easy lookup later
        engine.block.setString(productImage, property = "name", value = "product-image")
        
        engine.block.setWidth(productImage, value = 600F)
        engine.block.setHeight(productImage, value = 600F)
        engine.block.setPositionX(productImage, value = 240F)
        engine.block.setPositionY(productImage, value = 600F)
        engine.block.appendChild(parent = page, child = productImage)
        
        // Price text with variable
        val price = engine.block.create(DesignBlockType.Text)
        engine.block.setString(price, property = "text/text", value = "${{price}}")
        engine.block.setTextFontSize(price, fontSize = 36F)
        engine.block.setTextColor(
            price,
            color = Color.fromRGBA(r = 0.2F, g = 0.6F, b = 0.2F, a = 1.0F)
        )
        engine.block.setWidthMode(price, mode = SizeMode.AUTO)
        engine.block.setHeightMode(price, mode = SizeMode.AUTO)
        engine.block.setPositionX(price, value = 100F)
        engine.block.setPositionY(price, value = 1350F)
        engine.block.appendChild(parent = page, child = price)
        
        // Save as string
        val templateString = engine.scene.saveToString(scene = scene)
        println("Template saved as string (${templateString.length} characters)")
        
        // Save to file (for demonstration)
        val stringFile = File(context.filesDir, "template_string.scene")
        withContext(Dispatchers.IO) {
            stringFile.writeText(templateString)
        }
        
        // Save as archive (includes all assets)
        val archiveBlob = engine.scene.saveToArchive(scene = scene)
        val archiveFile = File(context.filesDir, "template_archive.cesdk")
        withContext(Dispatchers.IO) {
            archiveFile.outputStream().channel.use { channel ->
                channel.write(archiveBlob)
            }
        }
        println("Template saved as archive: ${archiveFile.absolutePath}")
        
        // Example: Populate the template with actual data
        engine.variable.set(key = "product_name", value = "Premium Coffee Mug")
        engine.variable.set(key = "description", value = "Hand-crafted ceramic, dishwasher safe")
        engine.variable.set(key = "price", value = "24.99")
        
        println("Template created and saved successfully!")
        
    } finally {
        // Note: Don't stop the engine here if you want to keep using it
        // engine.stop()
    }
}
```

## Add Template Metadata

Like other assets, you can:

- Load templates into the [asset library](https://img.ly/docs/cesdk/android/import-media/asset-library-65d6c4/).
- Store metadata in your CMS or local database.
- Use the saved metadata later when you register the template as an `AssetDefinition` in an `AssetSource`.

That way the UI can display names, thumbnails, and categories.

Example metadata structure:

```kotlin
data class TemplateMetadata(
    val id: String,
    val name: String,
    val description: String,
    val thumbnailUrl: String,
    val category: String,
    val tags: List<String>,
    val variables: List<String>,
    val createdAt: Long,
    val updatedAt: Long
)
```

## Lock Template Properties

Templates can restrict editing at runtime so that users don't edit any part of the design that should remain static. To protect integrity, you can lock properties such as:

- Position
- Size
- Color
- Fill

The guide for [locking templates](https://img.ly/docs/cesdk/android/create-templates/lock-131489/) provides details on which properties are lockable and how to set up editor and adopter rules.

Example of locking a block:

```kotlin
import ly.img.engine.Engine

// Lock the background so users can't move or resize it
engine.block.setScopeEnabled(background, key = "layer/move", enabled = false)
engine.block.setScopeEnabled(background, key = "layer/resize", enabled = false)
engine.block.setScopeEnabled(background, key = "fill/change", enabled = false)
```

## Load and Use Templates

Once you've created and saved a template, load it back and populate with data:

### Load from String

```kotlin
import android.net.Uri
import ly.img.engine.Engine

// Load template from string
val scene = engine.scene.load(scene = templateString)

// Populate with data
engine.variable.set(key = "product_name", value = "Wireless Headphones")
engine.variable.set(key = "description", value = "Premium sound quality")
engine.variable.set(key = "price", value = "149.99")

// Find and replace the product image
val blocks = engine.block.findByType(DesignBlockType.Graphic)
for (block in blocks) {
    val name = engine.block.getString(block, property = "name")
    if (name == "product-image") {
        val fill = engine.block.getFill(block)
        engine.block.setString(
            fill,
            property = "fill/image/imageFileURI",
            value = "https://example.com/headphones.jpg"
        )
    }
}
```

### Load from Archive

Archives need to be unzipped before loading. Here's how to load a template from an archive file:

```kotlin
import android.content.Context
import android.net.Uri
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import ly.img.engine.Engine
import java.io.File
import java.io.FileOutputStream
import java.util.zip.ZipInputStream

suspend fun loadTemplateFromArchive(
    engine: Engine,
    context: Context,
    archiveFile: File
): Int {
    // Unzip archive to cache directory
    val extractDir = File(context.cacheDir, "template_${System.currentTimeMillis()}")
    extractDir.mkdirs()
    
    withContext(Dispatchers.IO) {
        ZipInputStream(archiveFile.inputStream()).use { zipInputStream ->
            var entry = zipInputStream.nextEntry
            while (entry != null) {
                val file = File(extractDir, entry.name)
                if (entry.isDirectory) {
                    file.mkdirs()
                } else {
                    file.parentFile?.mkdirs()
                    FileOutputStream(file).use { outputStream ->
                        zipInputStream.copyTo(outputStream)
                    }
                }
                zipInputStream.closeEntry()
                entry = zipInputStream.nextEntry
            }
        }
    }
    
    // Load the scene.scene file from the extracted archive
    val sceneFile = File(extractDir, "scene.scene")
    val sceneUri = Uri.fromFile(sceneFile)
    return engine.scene.load(sceneUri = sceneUri)
}
```

## Troubleshooting

**❌ Variables not populating**:

- Confirm the variable syntax uses double curly brackets: `{{variable_name}}`
- Verify that `engine.variable.set()` is called with the correct key.
- Check that the scene is loaded before setting variables.

**❌ Named blocks not found**:

- Use `engine.block.getString(block, property = "name")` to verify block names.
- Make sure the name was set during template creation.
- Search within the correct block type using `engine.block.findByType()`.

**❌ Missing fonts/images at runtime**:

- Use an archive save to embed assets into a template for portability.
- Ensure that the asset URIs are reachable and stable.
- For local files, use `file:///android_asset/` for assets in the app's assets folder.

**❌ Template won't load**:

- Verify the template string or archive file is not corrupted.
- Check that all required assets are accessible at the specified URIs.
- Ensure the CE.SDK version used to create the template matches the version loading it.

## Next Steps

Now that you can create templates, some related topics you may find helpful are:

- [Generate scenes](https://img.ly/docs/cesdk/android/use-templates/generate-334e15/) with templates as the source.
- [Apply templates](https://img.ly/docs/cesdk/android/use-templates/apply-template-35c73e/) to existing scenes.
- [Batch Processing](https://img.ly/docs/cesdk/android/automation/batch-processing-ab2d18/) — automate template population at scale.
- [Multi-Image Generation](https://img.ly/docs/cesdk/android/automation/multi-image-generation-2a0de4/) — generate multiple variants from a single template.



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
