# Source: https://img.ly/docs/cesdk/android/edit-image/remove-bg-9dfcf7/

---
title: "Integrating Background Removal in Android (Kotlin)"
description: "Learn how to implement custom background removal using Google ML Kit's Selfie Segmentation in Android with CE.SDK."
platform: android
url: "https://img.ly/docs/cesdk/android/edit-image/remove-bg-9dfcf7/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [Create and Edit Images](https://img.ly/docs/cesdk/android/edit-image-c64912/) > [Remove Background](https://img.ly/docs/cesdk/android/edit-image/remove-bg-9dfcf7/)

---

The CE.SDK provides a flexible architecture that allows you to extend its capability to meet your specific needs.

This guide demonstrates how to integrate a custom background removal feature using Google ML Kit. You can apply the same approach to implement any custom image processing functionality in your Android app.

> **Note:** **ML Kit Selfie Segmentation** works best with images containing people. For more general subject segmentation, you may need to use third-party libraries or cloud-based APIs.

## What You'll Learn

- How to extract the current image from the CE.SDK engine.
- How to implement background removal using ML Kit Selfie Segmentation.
- How to process the image and apply the segmentation mask.
- How to update the image in the scene with the processed result.
- How to keep operations async and handle errors gracefully.

## When To Use It

- Want programmatic "Remove BG" functionality in your app.
- Prefer on-device processing (no uploads) for latency, privacy, or offline use.
- Need to integrate custom image processing logic (ML Kit, third-party libraries, or your own API).
- Building custom UI or automation workflows.

## Setup ML Kit

First, add the ML Kit Selfie Segmentation dependency to your `build.gradle`:

```kotlin
dependencies {
    implementation("com.google.mlkit:segmentation-selfie:16.0.0-beta5")
}
```

## Extracting the Image

A block that displays an image has an `imageFill` which contains the URI of the underlying image. The first step is to extract the image data from the fill.

```kotlin
import android.content.Context
import android.graphics.Bitmap
import android.graphics.BitmapFactory
import android.net.Uri
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import ly.img.engine.DesignBlockType
import ly.img.engine.Engine
import ly.img.engine.FillType
import java.io.ByteArrayOutputStream
import java.net.URL

suspend fun extractImageFromScene(
    engine: Engine,
    context: Context
): Bitmap? {
    // Get the current page from the scene
    val page = engine.scene.getCurrentPage() ?: return null
    
    // Validate that the page contains an image
    val imageFill = engine.block.getFill(page)
    val fillType = engine.block.getType(imageFill)
    
    if (fillType != "//ly.img.ubq/fill/image") {
        return null
    }
    
    // Extract the image URI
    val imageFileURI = engine.block.getString(imageFill, property = "fill/image/imageFileURI")
    
    // Download and decode the image
    return withContext(Dispatchers.IO) {
        try {
            val imageData = if (imageFileURI.startsWith("http")) {
                // Download from URL
                val url = URL(imageFileURI)
                val outputStream = ByteArrayOutputStream()
                url.openStream().use { inputStream ->
                    outputStream.use(inputStream::copyTo)
                }
                outputStream.toByteArray()
            } else {
                // Load from local file or content URI
                val uri = Uri.parse(imageFileURI)
                val inputStream = context.contentResolver.openInputStream(uri)
                inputStream?.readBytes() ?: byteArrayOf()
            }
            
            BitmapFactory.decodeByteArray(imageData, 0, imageData.size)
        } catch (e: Exception) {
            null
        }
    }
}
```

## Processing the Image with ML Kit

With a `Bitmap`, you can now process the image using ML Kit Selfie Segmentation. Here's a complete implementation:

```kotlin
import android.graphics.Bitmap
import android.graphics.Color
import com.google.mlkit.vision.common.InputImage
import com.google.mlkit.vision.segmentation.Segmentation
import com.google.mlkit.vision.segmentation.SegmentationMask
import com.google.mlkit.vision.segmentation.selfie.SelfieSegmenterOptions
import kotlinx.coroutines.tasks.await

/**
 * Removes the background from an image using ML Kit Selfie Segmentation.
 * @param original The source bitmap to process.
 * @return A new bitmap with the background removed (transparent), or null if processing fails.
 */
suspend fun removeBackgroundWithMLKit(original: Bitmap): Bitmap? {
    try {
        // Configure ML Kit Selfie Segmentation
        val options = SelfieSegmenterOptions.Builder()
            .setDetectorMode(SelfieSegmenterOptions.SINGLE_IMAGE_MODE)
            .enableRawSizeMask() // Get mask at original image resolution
            .build()
        
        val segmenter = Segmentation.getClient(options)
        
        // Create InputImage from bitmap
        val inputImage = InputImage.fromBitmap(original, 0)
        
        // Process the image and get the segmentation mask
        val segmentationMask: SegmentationMask = segmenter.process(inputImage).await()
        
        // Create output bitmap with transparency
        val width = original.width
        val height = original.height
        val result = Bitmap.createBitmap(width, height, Bitmap.Config.ARGB_8888)
        
        // Get mask data
        val mask = segmentationMask.buffer
        val maskWidth = segmentationMask.width
        val maskHeight = segmentationMask.height
        
        // Apply the mask to create transparent background
        for (y in 0 until height) {
            for (x in 0 until width) {
                // Map image coordinates to mask coordinates
                val maskX = (x * maskWidth / width).coerceIn(0, maskWidth - 1)
                val maskY = (y * maskHeight / height).coerceIn(0, maskHeight - 1)
                
                // Get mask confidence (0.0 = background, 1.0 = foreground)
                val maskIndex = maskY * maskWidth + maskX
                val confidence = mask.getFloat(maskIndex * 4) // 4 bytes per float
                
                // Get original pixel color
                val originalPixel = original.getPixel(x, y)
                
                if (confidence > 0.5f) {
                    // Foreground - keep original pixel
                    result.setPixel(x, y, originalPixel)
                } else {
                    // Background - make transparent
                    result.setPixel(x, y, Color.TRANSPARENT)
                }
            }
        }
        
        // Clean up
        segmenter.close()
        
        return result
        
    } catch (e: Exception) {
        e.printStackTrace()
        return null
    }
}
```

## Replace the Image in the Scene

With a processed image, the last step is to update the fill with the new image:

1. Save the processed bitmap to a file.
2. Get the file URI.
3. Update the image fill's source set with the new URI.

```kotlin
import android.content.Context
import android.graphics.Bitmap
import android.net.Uri
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import ly.img.engine.Engine
import ly.img.engine.Source
import java.io.File
import java.io.FileOutputStream

suspend fun replaceImageInScene(
    engine: Engine,
    context: Context,
    processedBitmap: Bitmap
) {
    // Save the bitmap to a file
    val imageFile = withContext(Dispatchers.IO) {
        val file = File(context.cacheDir, "bg_removed_${System.currentTimeMillis()}.png")
        FileOutputStream(file).use { outputStream ->
            processedBitmap.compress(Bitmap.CompressFormat.PNG, 100, outputStream)
        }
        file
    }
    
    val processedImageUri = Uri.fromFile(imageFile)
    
    // Get the current page and its fill
    val page = engine.scene.getCurrentPage() ?: return
    val imageFill = engine.block.getFill(page)
    
    // Update the source set with the new image
    engine.block.setSourceSet(
        block = imageFill,
        property = "fill/image/sourceSet",
        sourceSet = listOf(
            Source(
                uri = processedImageUri,
                width = processedBitmap.width.toUInt(),
                height = processedBitmap.height.toUInt()
            )
        )
    )
}
```

## Complete Function

Here's the complete function that combines all the steps:

```kotlin
import android.content.Context
import android.graphics.Bitmap
import android.graphics.BitmapFactory
import android.graphics.Color
import android.net.Uri
import com.google.mlkit.vision.common.InputImage
import com.google.mlkit.vision.segmentation.Segmentation
import com.google.mlkit.vision.segmentation.SegmentationMask
import com.google.mlkit.vision.segmentation.selfie.SelfieSegmenterOptions
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.tasks.await
import kotlinx.coroutines.withContext
import ly.img.engine.DesignBlockType
import ly.img.engine.Engine
import ly.img.engine.FillType
import ly.img.engine.Source
import java.io.ByteArrayOutputStream
import java.io.File
import java.io.FileOutputStream
import java.net.URL

suspend fun performBackgroundRemoval(
    engine: Engine,
    context: Context
): Boolean {
    return withContext(Dispatchers.Main) {
        try {
            // Step 1: Get the current page
            val page = engine.scene.getCurrentPage() ?: return@withContext false
            
            // Step 2: Validate it's an image fill
            val imageFill = engine.block.getFill(page)
            val fillType = engine.block.getType(imageFill)
            if (fillType != "//ly.img.ubq/fill/image") {
                return@withContext false
            }
            
            // Step 3: Extract image data
            val imageFileURI = engine.block.getString(imageFill, property = "fill/image/imageFileURI")
            val originalBitmap = withContext(Dispatchers.IO) {
                val imageData = if (imageFileURI.startsWith("http")) {
                    val url = URL(imageFileURI)
                    val outputStream = ByteArrayOutputStream()
                    url.openStream().use { inputStream ->
                        outputStream.use(inputStream::copyTo)
                    }
                    outputStream.toByteArray()
                } else {
                    val uri = Uri.parse(imageFileURI)
                    context.contentResolver.openInputStream(uri)?.readBytes() ?: byteArrayOf()
                }
                BitmapFactory.decodeByteArray(imageData, 0, imageData.size)
            } ?: return@withContext false
            
            // Step 4: Process with ML Kit
            val options = SelfieSegmenterOptions.Builder()
                .setDetectorMode(SelfieSegmenterOptions.SINGLE_IMAGE_MODE)
                .enableRawSizeMask()
                .build()
            
            val segmenter = Segmentation.getClient(options)
            val inputImage = InputImage.fromBitmap(originalBitmap, 0)
            val segmentationMask: SegmentationMask = segmenter.process(inputImage).await()
            
            // Step 5: Apply mask to create transparent background
            val width = originalBitmap.width
            val height = originalBitmap.height
            val result = Bitmap.createBitmap(width, height, Bitmap.Config.ARGB_8888)
            
            val mask = segmentationMask.buffer
            val maskWidth = segmentationMask.width
            val maskHeight = segmentationMask.height
            
            for (y in 0 until height) {
                for (x in 0 until width) {
                    val maskX = (x * maskWidth / width).coerceIn(0, maskWidth - 1)
                    val maskY = (y * maskHeight / height).coerceIn(0, maskHeight - 1)
                    val maskIndex = maskY * maskWidth + maskX
                    val confidence = mask.getFloat(maskIndex * 4)
                    val originalPixel = originalBitmap.getPixel(x, y)
                    
                    result.setPixel(
                        x, y,
                        if (confidence > 0.5f) originalPixel else Color.TRANSPARENT
                    )
                }
            }
            
            segmenter.close()
            
            // Step 6: Save processed image
            val imageFile = withContext(Dispatchers.IO) {
                val file = File(context.cacheDir, "bg_removed_${System.currentTimeMillis()}.png")
                FileOutputStream(file).use { outputStream ->
                    result.compress(Bitmap.CompressFormat.PNG, 100, outputStream)
                }
                file
            }
            
            val processedImageUri = Uri.fromFile(imageFile)
            
            // Step 7: Update the scene
            engine.block.setSourceSet(
                block = imageFill,
                property = "fill/image/sourceSet",
                sourceSet = listOf(
                    Source(
                        uri = processedImageUri,
                        width = result.width.toUInt(),
                        height = result.height.toUInt()
                    )
                )
            )
            
            return@withContext true
            
        } catch (e: Exception) {
            e.printStackTrace()
            return@withContext false
        }
    }
}
```

## Usage Example

Here's how to use the background removal function in your app:

```kotlin
import android.content.Context
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import ly.img.engine.Engine

fun removeBackgroundFromCurrentImage(
    engine: Engine,
    context: Context
) = CoroutineScope(Dispatchers.Main).launch {
    val success = performBackgroundRemoval(engine, context)
    
    if (success) {
        println("✅ Background removed successfully!")
    } else {
        println("❌ Failed to remove background")
    }
}
```

## Optimizations

### 1. Performance for Large Images

For better performance with large images, downscale before processing:

```kotlin
fun downscaleIfNeeded(bitmap: Bitmap, maxSize: Int = 1024): Bitmap {
    val maxDimension = maxOf(bitmap.width, bitmap.height)
    if (maxDimension <= maxSize) return bitmap
    
    val scale = maxSize.toFloat() / maxDimension
    val newWidth = (bitmap.width * scale).toInt()
    val newHeight = (bitmap.height * scale).toInt()
    
    return Bitmap.createScaledBitmap(bitmap, newWidth, newHeight, true)
}
```

### 2. Improve Mask Quality

Apply smoothing to the mask for better edge quality:

```kotlin
/**
 * Apply feathering to the mask for softer edges.
 */
fun applyFeathering(confidence: Float, threshold: Float = 0.5f, feather: Float = 0.1f): Float {
    return when {
        confidence >= threshold + feather -> 1.0f
        confidence <= threshold - feather -> 0.0f
        else -> {
            // Linear interpolation in the feather range
            (confidence - (threshold - feather)) / (2 * feather)
        }
    }
}
```

Then use it when applying the mask:

```kotlin
val alpha = applyFeathering(confidence)
if (alpha > 0) {
    val r = Color.red(originalPixel)
    val g = Color.green(originalPixel)
    val b = Color.blue(originalPixel)
    val newAlpha = (alpha * 255).toInt()
    result.setPixel(x, y, Color.argb(newAlpha, r, g, b))
} else {
    result.setPixel(x, y, Color.TRANSPARENT)
}
```

## Troubleshooting

**❌ Fill is not an image**:

Always check the fill type before processing:

```kotlin
val fillType = engine.block.getType(imageFill)
if (fillType != "//ly.img.ubq/fill/image") {
    // Not an image fill, cannot process
    return
}
```

**❌ Mask quality is poor**:

- Use `enableRawSizeMask()` for full-resolution masks.
- Apply feathering (see optimization section above).
- Consider pre-processing the image for better lighting/contrast.

**❌ Performance is slow on large images**:

- Downscale images before processing (see optimization section).
- Use `STREAM_MODE` instead of `SINGLE_IMAGE_MODE` for video.
- Process on a background thread (already handled with coroutines in the example).

**❌ Segmentation only works for people**:

ML Kit Selfie Segmentation is optimized for human subjects. For general object segmentation, consider:

- Using TensorFlow Lite models for object detection.
- Cloud-based APIs (Google Cloud Vision, etc.).
- Third-party segmentation libraries.

**❌ App crashes or ML Kit errors**:

- Ensure ML Kit dependencies are properly included.
- Check that Google Play Services are available on the device.
- Handle exceptions gracefully and provide user feedback.

## Alternative: Custom Segmentation Models

For more advanced segmentation beyond people, you can use TensorFlow Lite models. Here's a basic structure:

```kotlin
import org.tensorflow.lite.Interpreter
import java.nio.ByteBuffer

class CustomSegmentation(modelPath: String) {
    private val interpreter: Interpreter = Interpreter(loadModelFile(modelPath))
    
    fun segment(bitmap: Bitmap): Bitmap? {
        // 1. Preprocess bitmap to model input format
        // 2. Run inference
        // 3. Post-process output to mask
        // 4. Apply mask to create transparent background
        // Implementation depends on your specific model
        return null
    }
    
    private fun loadModelFile(modelPath: String): ByteBuffer {
        // Load TFLite model file
        // Implementation omitted for brevity
        TODO("Load your .tflite model file")
    }
}
```

## Next Steps

Now that you can remove backgrounds, explore related guides:

- [Scale & Transform](https://img.ly/docs/cesdk/android/edit-image/transform/scale-ebe367/) images after background removal.
- [Chroma Key](https://img.ly/docs/cesdk/android/filters-and-effects/chroma-key-green-screen-1e3e99/) for green screen effects.
- [Batch Processing](https://img.ly/docs/cesdk/android/automation/batch-processing-ab2d18/) for processing multiple images.



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
