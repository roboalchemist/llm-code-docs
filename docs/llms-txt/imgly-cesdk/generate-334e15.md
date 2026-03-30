# Source: https://img.ly/docs/cesdk/android/use-templates/generate-334e15/

---
title: "Generate From Templates"
description: "Learn how to load and populate CE.SDK templates in Kotlin for Android applications."
platform: android
url: "https://img.ly/docs/cesdk/android/use-templates/generate-334e15/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [Create and Use Templates](https://img.ly/docs/cesdk/android/create-templates-3aef79/) > [Generate From Template](https://img.ly/docs/cesdk/android/use-templates/generate-334e15/)

---

Once you create templates, either in CE.SDK's web-based editor or programmatically, your Android app can load and apply them to scenes at runtime. This guide explains **how to load templates**, populate them with variables and images, and use template libraries to integrate them into your app.

## What You'll Learn

- Load templates from string or URL.
- Launch the editor with a template as the initial scene.
- Populate templates with dynamic content using variables and placeholders.
- Create custom template libraries with thumbnails and metadata.
- Work with template archives for bundled assets.

## When to Use It

Use this guide when your Android app needs to **load and apply existing templates** to generate new scenes, such as:

- Starting from a brand template.
- Building a "Start from Template" screen.
- Populating designs dynamically with user or product data.

## Loading Templates as Scenes

You can load a template as the active scene when you start the engine or launch the editor. This is ideal when you want to either open directly into a predefined layout or start an editing session from a template.

### Load from URL

Use `engine.scene.load(sceneUri =)` to load a template from a remote or local URL.

```kotlin
import android.net.Uri
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import ly.img.engine.Engine

fun loadTemplateFromURL(license: String, userId: String) = CoroutineScope(Dispatchers.Main).launch {
    val engine = Engine.getInstance(id = "ly.img.engine.template")
    engine.start(license = license, userId = userId)
    engine.bindOffscreen(width = 1080, height = 1920)
    
    val templateUri = Uri.parse("https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_postcard_1.scene")
    val scene = engine.scene.load(sceneUri = templateUri)
    
    // Template is now loaded and ready for modifications
}
```

### Load from String

Use `engine.scene.load(scene =)` when you have the template as a string, such as when loading from a database or when your backend returns the raw string encoding.

```kotlin
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext
import ly.img.engine.Engine
import java.io.ByteArrayOutputStream
import java.net.URL

fun loadTemplateFromString(license: String, userId: String) = CoroutineScope(Dispatchers.Main).launch {
    val engine = Engine.getInstance(id = "ly.img.engine.template")
    engine.start(license = license, userId = userId)
    engine.bindOffscreen(width = 1080, height = 1920)
    
    // Fetch template string (could be from database, API, etc.)
    val templateUrl = URL("https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_postcard_1.scene")
    val templateString = withContext(Dispatchers.IO) {
        val outputStream = ByteArrayOutputStream()
        templateUrl.openStream().use { inputStream ->
            outputStream.use(inputStream::copyTo)
        }
        String(outputStream.toByteArray(), Charsets.UTF_8)
    }
    
    val scene = engine.scene.load(scene = templateString)
    
    // Template is now loaded and ready for modifications
}
```

### Load from Assets

For templates bundled in your app's assets folder, use the `file:///android_asset/` URI scheme.

```kotlin
import android.net.Uri
import ly.img.engine.Engine

suspend fun loadTemplateFromAssets(engine: Engine) {
    val templateUri = Uri.parse("file:///android_asset/templates/postcard_template.scene")
    val scene = engine.scene.load(sceneUri = templateUri)
}
```

### Load from Archive

Archives bundle the scene file with all its assets (images, fonts) for portability. To load an archive:

1. Unzip the archive to a location accessible to the engine
2. Load the `scene.scene` file from the unzipped location

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
    archiveUri: Uri
): Int {
    // Unzip archive to cache directory
    val extractDir = File(context.cacheDir, "template_${System.currentTimeMillis()}")
    extractDir.mkdirs()
    
    withContext(Dispatchers.IO) {
        context.contentResolver.openInputStream(archiveUri)?.use { inputStream ->
            ZipInputStream(inputStream).use { zipInputStream ->
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
    }
    
    // Load the scene.scene file from extracted directory
    val sceneFile = File(extractDir, "scene.scene")
    val sceneUri = Uri.fromFile(sceneFile)
    return engine.scene.load(sceneUri = sceneUri)
}
```

## Dynamic Population (Variables & Placeholders)

Templates can include variable placeholders like `{{name}}` or image placeholders. Your app can inject values at runtime.

> **Note:** Interactive placeholder behavior (tap-to-replace, drag-drop) is available only in **CE.SDK's predefined editors**.In **code-only or headless workflows**, use the `Variable` and `Block` APIs to replace content programmatically.

### Update Text Variables

Variables allow you to dynamically populate text fields in your template.

```kotlin
import ly.img.engine.Engine

fun populateTextVariables(engine: Engine, userName: String, itemPrice: String) {
    engine.variable.set(key = "name", value = userName)
    engine.variable.set(key = "price", value = itemPrice)
    engine.variable.set(key = "date", value = "November 23, 2025")
}
```

### Replace Image Placeholders

Find blocks by name and update their image fill URIs to replace placeholder images.

```kotlin
import ly.img.engine.Engine

fun replaceImagePlaceholder(engine: Engine, blockName: String, imageUri: String) {
    val blocks = engine.block.findByName(blockName)
    if (blocks.isNotEmpty()) {
        val block = blocks.first()
        val fill = engine.block.getFill(block)
        engine.block.setString(fill, property = "fill/image/imageFileURI", value = imageUri)
        engine.block.resetCrop(block)
    }
}
```

### Complete Population Example

Here's a complete example that loads a template and populates it with dynamic content:

```kotlin
import android.content.Context
import android.net.Uri
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import ly.img.engine.DesignBlockType
import ly.img.engine.Engine
import ly.img.engine.MimeType
import java.io.File

fun generateFromTemplate(
    context: Context,
    license: String,
    userId: String
) = CoroutineScope(Dispatchers.Main).launch {
    val engine = Engine.getInstance(id = "ly.img.engine.template")
    engine.start(license = license, userId = userId)
    engine.bindOffscreen(width = 1080, height = 1920)
    
    // Load template
    val templateUri = Uri.parse("file:///android_asset/templates/greeting_card.scene")
    val scene = engine.scene.load(sceneUri = templateUri)
    
    // Populate text variables
    engine.variable.set(key = "recipientName", value = "Alice")
    engine.variable.set(key = "message", value = "Happy Birthday!")
    engine.variable.set(key = "senderName", value = "Bob")
    
    // Replace image placeholder
    val photoBlocks = engine.block.findByName("userPhoto")
    if (photoBlocks.isNotEmpty()) {
        val photoBlock = photoBlocks.first()
        val fill = engine.block.getFill(photoBlock)
        engine.block.setString(
            fill,
            property = "fill/image/imageFileURI",
            value = "https://example.com/photos/alice.jpg"
        )
        engine.block.resetCrop(photoBlock)
    }
    
    // Export the result
    val page = engine.block.findByType(DesignBlockType.Page).firstOrNull()
    if (page != null) {
        val exportData = engine.block.export(page, mimeType = MimeType.PNG)
        // Save to file...
    }
    
    engine.stop()
}
```

## Template Libraries

You can present templates in the Asset Library along with other assets via a local asset source. Each entry includes metadata that points to your template file and a preview image. You can learn more about working with custom assets in the [custom asset source](https://img.ly/docs/cesdk/android/import-media/asset-library-65d6c4/) guide.

### Create a Template Asset Source

```kotlin
import ly.img.engine.AssetDefinition
import ly.img.engine.Engine

fun registerTemplateAssetSource(engine: Engine) {
    // Create a local source for templates
    engine.asset.addLocalSource(
        sourceId = "my-templates",
        supportedMimeTypes = listOf("application/octet-stream")
    )
    
    // Add template assets to the source
    val postcardTemplate = AssetDefinition(
        id = "template-postcard-1",
        label = mapOf("en" to "Postcard Template"),
        tags = mapOf("en" to listOf("postcard", "greeting")),
        meta = mapOf(
            "uri" to "file:///android_asset/templates/postcard_1.scene",
            "thumbUri" to "file:///android_asset/templates/thumbnails/postcard_1.png",
            "width" to "1080",
            "height" to "1080"
        )
    )
    
    val socialTemplate = AssetDefinition(
        id = "template-social-1",
        label = mapOf("en" to "Social Media Post"),
        tags = mapOf("en" to listOf("social", "instagram")),
        meta = mapOf(
            "uri" to "file:///android_asset/templates/social_1.scene",
            "thumbUri" to "file:///android_asset/templates/thumbnails/social_1.png",
            "width" to "1080",
            "height" to "1350"
        )
    )
    
    engine.asset.addAsset(sourceId = "my-templates", asset = postcardTemplate)
    engine.asset.addAsset(sourceId = "my-templates", asset = socialTemplate)
}
```

## Launch Editor with Template

When using one of CE.SDK's prebuilt editors, you can load a template as the initial scene:

```kotlin
import android.net.Uri
import androidx.compose.runtime.Composable
import androidx.navigation.NavHostController
import ly.img.editor.DesignEditor
import ly.img.editor.EngineConfiguration

@Composable
fun EditorWithTemplate(navController: NavHostController) {
    val engineConfiguration = EngineConfiguration.rememberForDesign(
        license = "your-license",
        userId = "user-id",
        sceneUri = Uri.parse("file:///android_asset/templates/default_template.scene")
    )
    
    DesignEditor(engineConfiguration = engineConfiguration) {
        navController.popBackStack()
    }
}
```

## Troubleshooting

**❌ Template fails to load**:

- Verify the URI is accessible and the file exists.
- Check network permissions for remote URLs.
- Ensure template format is compatible with your SDK version.

**❌ Text variables not updating**:

- Confirm variable names match exactly (case-sensitive).
- Check that variables are defined in the template with `{{variableName}}` syntax.
- Use `engine.variable.findAll()` to list available variables.

**❌ Images missing after loading**:

- Ensure image URIs in the template are accessible.
- For archives, verify extraction was successful.
- Check asset permissions in AndroidManifest.xml.

**❌ Wrong dimensions or scaling**:

- Templates maintain their original page dimensions.
- Use `engine.block.getFrameWidth()` and `engine.block.getFrameHeight()` to check dimensions.
- Consider template adaptation strategies for different aspect ratios.

**Debugging Tips**:

- Print all available variables: `engine.variable.findAll()`
- List named blocks: Use `engine.block.findByName()` to verify block names
- Test with a minimal template before using complex ones
- Use Android Logcat to track loading and population flow

## Next Steps

Now that you can generate creations from templates, some related topics you may find helpful are:

- [Create templates](https://img.ly/docs/cesdk/android/create-templates/from-scratch-663cda/) from scratch.
- Work with [text variables](https://img.ly/docs/cesdk/android/create-templates/add-dynamic-content/text-variables-7ecb50/) for dynamic content.
- Build [batch processing](https://img.ly/docs/cesdk/android/automation/batch-processing-ab2d18/) workflows with templates.
- Implement [multi-image generation](https://img.ly/docs/cesdk/android/automation/multi-image-generation-2a0de4/) for variants.
- [Save scenes](https://img.ly/docs/cesdk/android/export-save-publish/save-c8b124/) as templates for reuse.



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
