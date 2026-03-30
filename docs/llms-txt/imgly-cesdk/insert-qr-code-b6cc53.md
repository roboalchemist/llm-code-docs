# Source: https://img.ly/docs/cesdk/android/stickers-and-shapes/insert-qr-code-b6cc53/

---
title: "Insert QR Code in Android (Kotlin)"
description: "Generate a QR code with ZXing and insert it into a scene as an image fill, with positioning, sizing, and optional metadata for later updates."
platform: android
url: "https://img.ly/docs/cesdk/android/stickers-and-shapes/insert-qr-code-b6cc53/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [Create and Edit Shapes](https://img.ly/docs/cesdk/android/shapes-9f1b2c/) > [Insert QR Code](https://img.ly/docs/cesdk/android/stickers-and-shapes/insert-qr-code-b6cc53/)

---

QR codes are a practical way to turn any design into a scannable gateway for:

- Landing pages
- App installs
- Product info
- Event tickets
- You name it

CE.SDK doesn't include a built-in QR generator, but you can create the image with **ZXing** in just a few lines and place it on the canvas as an **image fill**. This guide shows the full workflow with Kotlin examples.

## What You'll Learn

- Generate a QR code image from a `String` using **ZXing**.
- Add it to a CE.SDK scene as an **image fill** on a shape block.
- Control **size**, **position**, and **color** for brand consistency.
- Store **metadata** for quick regeneration later.

## When You'll Use It

- Business cards, flyers, or packaging that need a **scannable link**.
- Apps that let users personalize templates with their own URLs.
- Automated workflows that embed links into generated designs.

## Setup ZXing Dependency

Add the ZXing library to your `build.gradle` file:

```kotlin
dependencies {
    implementation("com.google.zxing:core:3.5.3")
}
```

## Generate a QR Code Image

Use **ZXing** to create a high-resolution QR code, then colorize it to match your brand.

```kotlin
import android.graphics.Bitmap
import android.graphics.Color
import com.google.zxing.BarcodeFormat
import com.google.zxing.EncodeHintType
import com.google.zxing.qrcode.QRCodeWriter
import com.google.zxing.qrcode.decoder.ErrorCorrectionLevel

/**
 * Generate a QR code with brand colors.
 * @param content The content to encode.
 * @param size The size of the QR code in pixels.
 * @param errorCorrection Error correction level (L, M, Q, H).
 * @param foreground Color for the QR modules.
 * @param background Color for the QR background.
 */
fun generateQRCode(
    content: String,
    size: Int = 512,
    errorCorrection: ErrorCorrectionLevel = ErrorCorrectionLevel.M,
    foreground: Int = Color.BLACK,
    background: Int = Color.WHITE
): Bitmap {
    val hints = hashMapOf<EncodeHintType, Any>(
        EncodeHintType.ERROR_CORRECTION to errorCorrection,
        EncodeHintType.MARGIN to 1
    )
    
    val writer = QRCodeWriter()
    val bitMatrix = writer.encode(content, BarcodeFormat.QR_CODE, size, size, hints)
    
    val bitmap = Bitmap.createBitmap(size, size, Bitmap.Config.ARGB_8888)
    for (x in 0 until size) {
        for (y in 0 until size) {
            bitmap.setPixel(x, y, if (bitMatrix[x, y]) foreground else background)
        }
    }
    
    return bitmap
}
```

Keep the foreground dark and the background light for reliable scanning.

## Insert the QR as an Image Fill

Create a `graphic` block, assign it a `rect` shape, and fill it with your generated QR image.

```kotlin
import android.content.Context
import android.graphics.Bitmap
import android.net.Uri
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import ly.img.engine.DesignBlockType
import ly.img.engine.Engine
import ly.img.engine.FillType
import ly.img.engine.ShapeType
import java.io.File
import java.io.FileOutputStream

suspend fun insertQRCode(
    engine: Engine,
    context: Context,
    page: Int,
    urlString: String,
    positionX: Float = 200f,
    positionY: Float = 200f,
    size: Float = 160f
): Int {
    // Generate QR code bitmap
    val qrBitmap = generateQRCode(content = urlString, size = 512)
    
    // Save to temporary file
    val file = File(context.cacheDir, "qr_${System.currentTimeMillis()}.png")
    withContext(Dispatchers.IO) {
        FileOutputStream(file).use { out ->
            qrBitmap.compress(Bitmap.CompressFormat.PNG, 100, out)
        }
    }
    
    val fileUri = Uri.fromFile(file)
    
    // Create graphic block with rect shape
    val graphic = engine.block.create(DesignBlockType.Graphic)
    val rectShape = engine.block.createShape(ShapeType.Rect)
    engine.block.setShape(graphic, shape = rectShape)
    
    // Create and apply image fill
    val imageFill = engine.block.createFill(FillType.Image)
    engine.block.setString(imageFill, property = "fill/image/imageFileURI", value = fileUri.toString())
    engine.block.setFill(graphic, fill = imageFill)
    
    // Set size and position
    engine.block.setWidth(graphic, value = size)
    engine.block.setHeight(graphic, value = size)
    engine.block.setPositionX(graphic, value = positionX)
    engine.block.setPositionY(graphic, value = positionY)
    
    // Add to page
    engine.block.appendChild(parent = page, child = graphic)
    
    return graphic
}
```

The preceding code creates a QR code and then saves it to the cache directory to generate a file URI the block can use.

## Add Optional Metadata

Store the URL alongside the block for quick updates later. Metadata `key` values are anything you want. The `key` and the `value` must be `String` types.

```kotlin
import ly.img.engine.Engine

fun storeQRMetadata(engine: Engine, qrBlock: Int, urlString: String) {
    engine.block.setMetadata(qrBlock, key = "qr/url", value = urlString)
}
```

## Update an Existing QR Code

If data changes, just regenerate the QR image and update the fill URI.

```kotlin
import android.content.Context
import android.graphics.Bitmap
import android.net.Uri
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import ly.img.engine.Engine
import java.io.File
import java.io.FileOutputStream

suspend fun updateQRCode(
    engine: Engine,
    context: Context,
    qrBlock: Int,
    newURL: String
) {
    // Generate new QR code bitmap
    val qrBitmap = generateQRCode(content = newURL, size = 512)
    
    // Save to temporary file
    val file = File(context.cacheDir, "qr_${System.currentTimeMillis()}.png")
    withContext(Dispatchers.IO) {
        FileOutputStream(file).use { out ->
            qrBitmap.compress(Bitmap.CompressFormat.PNG, 100, out)
        }
    }
    
    val fileUri = Uri.fromFile(file)
    
    // Update the fill URI
    val fill = engine.block.getFill(qrBlock)
    engine.block.setString(fill, property = "fill/image/imageFileURI", value = fileUri.toString())
    engine.block.setMetadata(qrBlock, key = "qr/url", value = newURL)
}
```

To generate many QR codes, for instance during a batch run, loop through your data and call `insertQRCode` for each.

## Troubleshooting

| Symptom | Cause | Solution |
|----------|--------|-----------|
| QR looks blurry | Bitmap size too small | Increase the `size` parameter in `generateQRCode` (e.g., 1024). |
| QR won't scan | Low contrast or invalid URL | Use dark-on-light colors and ensure URLs are properly encoded. |
| QR not visible | Shape missing from block | Call `setShape` before applying the fill. |
| File I/O error | Invalid cache directory | Always use `context.cacheDir` for temporary files. |

## Next Steps

Now that you can generate QR codes, here are some related guides to help you learn more.

- [Insert Shapes or Stickers](https://img.ly/docs/cesdk/android/insert-media/shapes-or-stickers-20ac68/) — Learn how fills and shapes interact.
- [Batch Processing](https://img.ly/docs/cesdk/android/automation/batch-processing-ab2d18/) — Automate multiple QR insertions.
- [Export Overview](https://img.ly/docs/cesdk/android/export-save-publish/export/overview-9ed3a8/) — Save and test your codes.
- [Use Templates: Overview](https://img.ly/docs/cesdk/android/create-templates/overview-4ebe30/) — Add a placeholder for QR blocks in templates.



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
