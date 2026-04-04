# Source: https://img.ly/docs/cesdk/android/text/styling-269c48/

---
title: "Text Styling"
description: "Apply fonts, colors, alignment, and other styling options to customize text appearance."
platform: android
url: "https://img.ly/docs/cesdk/android/text/styling-269c48/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [Create and Edit Text](https://img.ly/docs/cesdk/android/text-8a993a/) > [Text Styling](https://img.ly/docs/cesdk/android/text/styling-269c48/)

---

```kotlin file=@cesdk_android_examples/engine-guides-text-properties/TextProperties.kt reference-only
import android.net.Uri
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import ly.img.engine.AnimationType
import ly.img.engine.Color
import ly.img.engine.DesignBlockType
import ly.img.engine.Engine
import ly.img.engine.Font
import ly.img.engine.FontStyle
import ly.img.engine.FontWeight
import ly.img.engine.SizeMode
import ly.img.engine.TextCase
import ly.img.engine.Typeface

fun textProperties(
    license: String?, // pass null or empty for evaluation mode with watermark
    userId: String,
) = CoroutineScope(Dispatchers.Main).launch {
    val engine = Engine.getInstance(id = "ly.img.engine.example")
    engine.start(license = license, userId = userId)
    engine.bindOffscreen(width = 1080, height = 1920)

    val scene = engine.scene.create()
    val text = engine.block.create(DesignBlockType.Text)
    engine.block.appendChild(parent = scene, child = text)
    engine.block.setWidthMode(text, mode = SizeMode.AUTO)
    engine.block.setHeightMode(text, mode = SizeMode.AUTO)

    engine.block.replaceText(text, text = "Hello World")

    // Add a "!" at the end of the text
    engine.block.replaceText(text, text = "!", from = 11)

    // Replace "World" with "Alex"
    engine.block.replaceText(text, text = "Alex", from = 6, to = 11)

    engine.scene.zoomToBlock(
        block = text,
        paddingLeft = 100F,
        paddingTop = 100F,
        paddingRight = 100F,
        paddingBottom = 100F,
    )

    // Remove the "Hello "
    engine.block.removeText(text, from = 0, to = 6)

    engine.block.setTextColor(text, color = Color.fromHex("#FFFF0000"))

    engine.block.setTextColor(text, color = Color.fromHex("#FFFF0000"), from = 1, to = 4)

    val allColors = engine.block.getTextColors(text)

    val colorsInRange = engine.block.getTextColors(text, from = 2, to = 5)

    engine.block.setBoolean(text, property = "backgroundColor/enabled", value = true)

    val color = engine.block.getColor(text, property = "backgroundColor/color")
    engine.block.setColor(text, property = "backgroundColor/color", value = Color.fromRGBA(r = 0, g = 0, b = 1, a = 1))

    engine.block.setFloat(text, property = "backgroundColor/paddingLeft", value = 1.0F)
    engine.block.setFloat(text, property = "backgroundColor/paddingTop", value = 2.0F)
    engine.block.setFloat(text, property = "backgroundColor/paddingRight", value = 3.0F)
    engine.block.setFloat(text, property = "backgroundColor/paddingBottom", value = 4.0F)

    engine.block.setFloat(text, property = "backgroundColor/cornerRadius", value = 4.0F)

    val animation = engine.block.createAnimation(AnimationType.Slide)
    engine.block.setEnum(animation, property = "textAnimationWritingStyle", value = "Block")

    engine.block.setInAnimation(text, animation = animation)
    engine.block.setOutAnimation(text, animation = animation)

    engine.block.setTextCase(text, textCase = TextCase.TITLE_CASE)

    val textCases = engine.block.getTextCases(text)

    val typeface = Typeface(
        name = "Roboto",
        fonts = listOf(
            Font(
                uri = Uri.parse("https://cdn.img.ly/assets/v3/ly.img.typeface/fonts/Roboto/Roboto-Bold.ttf"),
                subFamily = "Bold",
                weight = FontWeight.BOLD,
                style = FontStyle.NORMAL,
            ),
            Font(
                uri = Uri.parse("https://cdn.img.ly/assets/v3/ly.img.typeface/fonts/Roboto/Roboto-BoldItalic.ttf"),
                subFamily = "Bold Italic",
                weight = FontWeight.BOLD,
                style = FontStyle.ITALIC,
            ),
            Font(
                uri = Uri.parse("https://cdn.img.ly/assets/v3/ly.img.typeface/fonts/Roboto/Roboto-Italic.ttf"),
                subFamily = "Italic",
                weight = FontWeight.BOLD,
                style = FontStyle.NORMAL,
            ),
            Font(
                uri = Uri.parse("https://cdn.img.ly/assets/v3/ly.img.typeface/fonts/Roboto/Roboto-Regular.ttf"),
                subFamily = "Regular",
                weight = FontWeight.NORMAL,
                style = FontStyle.NORMAL,
            ),
        ),
    )
    engine.block.setFont(text, typeface.fonts[3].uri, typeface)

    engine.block.setTypeface(text, typeface, from = 1, to = 4)
    engine.block.setTypeface(text, typeface)

    val currentDefaultTypeface = engine.block.getTypeface(text)

    val currentTypefaces = engine.block.getTypefaces(text)
    val currentTypefacesOfRange = engine.block.getTypefaces(text, from = 1, to = 4)

    if (engine.block.canToggleBoldFont(text)) {
        engine.block.toggleBoldFont(text)
    }
    if (engine.block.canToggleBoldFont(text, from = 1, to = 4)) {
        engine.block.toggleBoldFont(text, from = 1, to = 4)
    }

    if (engine.block.canToggleItalicFont(text)) {
        engine.block.toggleItalicFont(text)
    }
    if (engine.block.canToggleItalicFont(text, from = 1, to = 4)) {
        engine.block.toggleItalicFont(text, from = 1, to = 4)
    }

    val fontWeights = engine.block.getTextFontWeights(text)

    engine.block.setTextFontStyle(text, FontStyle.NORMAL)

    val fontStyles = engine.block.getTextFontStyles(text)

    engine.stop()
}
```

In this example, we want to show how to read and modify the text block's contents via the API in the offscreen Engine.

## Editing the Text String

You can edit the text string contents of a text block using the `fun replaceText(block: DesignBlock, text: String, from: Int = -1, to: Int = -1)` and `fun removeText(block: DesignBlock, from: Int = -1, to: Int = -1)` APIs.
The range of text that should be edited is defined using the UTF-16 indices \[from, to).

When omitting both the `from` and `to` arguments, the entire existing string is replaced.

```kotlin highlight-replaceText
engine.block.replaceText(text, text = "Hello World")
```

When only specifying the `from` index, the new text is inserted at this index.

```kotlin highlight-replaceText-single-index
// Add a "!" at the end of the text
engine.block.replaceText(text, text = "!", from = 11)
```

When both `from` and `to` indices are specified, then that range of text is replaced with the new text.

```kotlin highlight-replaceText-range
// Replace "World" with "Alex"
engine.block.replaceText(text, text = "Alex", from = 6, to = 11)
```

Similarly, the `removeText` API can be called to remove either a specific range or the entire text.

```kotlin highlight-removeText
// Remove the "Hello "
engine.block.removeText(text, from = 0, to = 6)
```

## Text Colors

Text blocks in the Engine allow different ranges to have multiple colors.

Use the `fun setTextColor(block: DesignBlock, color: Color, from: Int = -1, to: Int = -1)` API to change either the color of the entire text

```kotlin highlight-setTextColor
engine.block.setTextColor(text, color = Color.fromHex("#FFFF0000"))
```

or only that of a range. After these two calls, the text "Alex!" now starts with one yellow character, followed by three black characters and two more yellow ones.

```kotlin highlight-setTextColor-range
engine.block.setTextColor(text, color = Color.fromHex("#FFFF0000"), from = 1, to = 4)
```

The `fun getTextColors(block: DesignBlock, from: Int = -1, to: Int = -1): List<Color>` API returns an ordered list of unique colors in the requested range. Here, `allColors` will be a list containing the colors yellow and black (in this order).

```kotlin highlight-getTextColors
val allColors = engine.block.getTextColors(text)
```

When only the colors in the UTF-16 range from 2 to 5 are requested, the result will be an array containing black and then yellow, since black appears first in the requested range.

```kotlin highlight-getTextColors-range
val colorsInRange = engine.block.getTextColors(text, from = 2, to = 5)
```

## Text Background

You can create and edit the background of a text block by setting specific block properties.

To add a colored background to a text block use the `fun setBoolean(block: DesignBlock, property: String, value: Boolean))` API and enable the `backgroundColor/enabled` property.

```kotlin highlight-backgroundColor-enabled
engine.block.setBoolean(text, property = "backgroundColor/enabled", value = true)
```

The color of the text background can be queried (by making use of the `fun setColor(block: DesignBlock, property: String, value: Color)` API ) and also changed (with the `fun setColor(block: DesignBlock, property: String, value: Color)` API).

```kotlin highlight-backgroundColor-get-set
val color = engine.block.getColor(text, property = "backgroundColor/color")
```

The padding of the rectangular background shape can be edited by using the `fun setFloat(block: DesignBlock, property: String, value: Float)` API and setting the target value for the desired padding property like:

- `backgroundColor/paddingLeft`:
- `backgroundColor/paddingRight`:
- `backgroundColor/paddingTop`:
- `backgroundColor/paddingBottom`:

```kotlin highlight-backgroundColor-padding
engine.block.setFloat(text, property = "backgroundColor/paddingLeft", value = 1.0F)
```

Additionally, the rectangular shape of the background can be rounded by setting a corner radius with the `fun setFloat(block: DesignBlock, property: String, value: Float)` API to adjust the value of the `backgroundColor/cornerRadius` property.

```kotlin highlight-backgroundColor-cornerRadius
engine.block.setFloat(text, property = "backgroundColor/cornerRadius", value = 4.0F)
```

Text backgrounds inherit the animations assigned to their respective text block when the animation text writing style is set to `Block`.

```kotlin highlight-backgroundColor-animation
val animation = engine.block.createAnimation(AnimationType.Slide)
```

## Text Case

You can apply text case modifications to ranges of text in order to display them in upper case, lower case or title case. It is important to note that these modifiers do not change the `text` string value of the text block but are only applied when the block is rendered.
By default, the text case of all text within a text block is set to `TextCase.NORMAL`, which does not modify the appearance of the text at all.

The `fun setTextCase(block: DesignBlock, textCase: TextCase, from: Int = -1, to: Int = -1)` API sets the given text case for the selected range of text.
Possible values for `TextCase` are:

- `NORMAL`: The text string is rendered without modifications.
- `UPPER_CASE`: All characters are rendered in upper case.
- `LOWER_CASE`: All characters are rendered in lower case.
- `TITLE_CASE`: The first character of each word is rendered in upper case.

```kotlin highlight-setTextCase
engine.block.setTextCase(text, textCase = TextCase.TITLE_CASE)
```

The `fun getTextCases(block: DesignBlock, from: Int = -1, to: Int = -1): List<TextCase>` API returns the ordered list of text cases of the text in the selected range.

```kotlin highlight-getTextCases
val textCases = engine.block.getTextCases(text)
```

## Typefaces

In order to change the font of a text block, you have to call the `fun setFont(block: DesignBlock, fontFileUri: Uri, typeface: Typeface)` API and provide it with both the uri of the font file to be actively used and the complete typeface definition of the corresponding typeface. Existing formatting of the block is reset.

A typeface definition consists of the unique typeface name (as it is defined within the font files), and a list of all font definitions that belong to this typeface. Each font definition must provide a `Uri` which points to the font file and a `subFamily` string which is this font's effective name within its typeface. The subfamily value is typically also defined within the font file. The `weight` and `style` properties default to `NORMAL`, but must be provided in other cases.

For the sake of this example, we define a `Roboto` typeface with only four fonts: `Regular`, `Bold`, `Italic`, and `Bold Italic` and we change the font of the text block to the Roboto Regular font.

```kotlin highlight-setFont
val typeface = Typeface(
    name = "Roboto",
    fonts = listOf(
        Font(
            uri = Uri.parse("https://cdn.img.ly/assets/v3/ly.img.typeface/fonts/Roboto/Roboto-Bold.ttf"),
            subFamily = "Bold",
            weight = FontWeight.BOLD,
            style = FontStyle.NORMAL,
        ),
        Font(
            uri = Uri.parse("https://cdn.img.ly/assets/v3/ly.img.typeface/fonts/Roboto/Roboto-BoldItalic.ttf"),
            subFamily = "Bold Italic",
            weight = FontWeight.BOLD,
            style = FontStyle.ITALIC,
        ),
        Font(
            uri = Uri.parse("https://cdn.img.ly/assets/v3/ly.img.typeface/fonts/Roboto/Roboto-Italic.ttf"),
            subFamily = "Italic",
            weight = FontWeight.BOLD,
            style = FontStyle.NORMAL,
        ),
        Font(
            uri = Uri.parse("https://cdn.img.ly/assets/v3/ly.img.typeface/fonts/Roboto/Roboto-Regular.ttf"),
            subFamily = "Regular",
            weight = FontWeight.NORMAL,
            style = FontStyle.NORMAL,
        ),
    ),
)
engine.block.setFont(text, typeface.fonts[3].uri, typeface)
```

If the formatting, e.g., bold or italic, of the text should be kept, you have to call the `fun setTypeface(block: DesignBlock, fontFileUri: Uri, typeface: Typeface)` API and provide it with both the uri of the font file to be used and the complete typeface definition of the corresponding typeface. The font file should be a fallback font, e.g., `Regular`, from the same typeface. The actual font that matches the formatting is chosen automatically with the current formatting retained as much as possible. If the new typeface does not support the current formatting, the formatting changes to a reasonable close one, e.g. thin might change to light, bold to normal, and/or italic to non-italic. If no reasonable font can be found, the fallback font is used.

```kotlin highlight-setTypeface
engine.block.setTypeface(text, typeface, from = 1, to = 4)
engine.block.setTypeface(text, typeface)
```

You can query the currently used typeface definition of a text block by calling the `fun getTypeface(block: DesignBlock): Typeface` API. It is important to note that new text blocks don't have any explicit typeface set until you call the `setFont` API. In this case, the `getTypeface` API will throw an error.

```kotlin highlight-getTypeface
val currentDefaultTypeface = engine.block.getTypeface(text)
```

## Font Weights and Styles

Text blocks can also have multiple ranges with different weights and styles.

In order to toggle the text of a text block between the normal and bold font weights, first call the `fun canToggleBoldFont(block: DesignBlock, from: Int = -1, to: Int = -1): Boolean` API to check whether such an edit is possible and if so, call the `fun toggleBoldFont(block: DesignBlock, from: Int = -1, to: Int = -1)` API to change the weight.

```kotlin highlight-toggleBold
if (engine.block.canToggleBoldFont(text)) {
    engine.block.toggleBoldFont(text)
}
if (engine.block.canToggleBoldFont(text, from = 1, to = 4)) {
    engine.block.toggleBoldFont(text, from = 1, to = 4)
}
```

In order to toggle the text of a text block between the normal and italic font styles, first call the `fun canToggleItalicFont(block: DesignBlock, from: Int = -1, to: Int = -1): Boolean` API to check whether such an edit is possible and if so, call the `fun toggleItalicFont(block: DesignBlock, from: Int = -1, to: Int = -1)` API to change the style.

```kotlin highlight-toggleItalic
if (engine.block.canToggleItalicFont(text)) {
    engine.block.toggleItalicFont(text)
}
if (engine.block.canToggleItalicFont(text, from = 1, to = 4)) {
    engine.block.toggleItalicFont(text, from = 1, to = 4)
}
```

In order to change the font weight or style, the typeface definition of the text block must include a font definition that corresponds to the requested font weight and style combination. For example, if the text block currently uses a bold font and you want to toggle the font style to italic - such as in the example code - the typeface must contain a font that is both bold and italic.

The `fun getTextFontWeights(block: DesignBlock, from: Int = -1, to: Int = -1): List<FontWeight>` API returns an ordered list of unique font weights in the requested range, similar to the `getTextColors` API described above. For this example text, the result will be `listOf(FontWeight.BOLD)`.

```kotlin highlight-getTextFontWeights
val fontWeights = engine.block.getTextFontWeights(text)
```

The fun `setTextFontStyle(block: DesignBlock, fontStyle: FontStyle, from: Int = -1, to: Int = -1)` API sets a font style in the requested range.

```kotlin highlight-setTextFontStyle
engine.block.setTextFontStyle(text, FontStyle.NORMAL)
```

The `fun getTextFontStyles(block: DesignBlock, from: Int = -1, to: Int = -1): List<FontStyle>` API returns an ordered list of unique font styles in the requested range, similar to the `getTextColors` API described above. For this example text, the result will be `listOf(FontWeight.ITALIC)`.

```kotlin highlight-getTextFontStyles
val fontStyles = engine.block.getTextFontStyles(text)
```

## Full Code

Here's the full code:

```kotlin
import android.net.Uri
import kotlinx.coroutines.*
import ly.img.engine.*

fun textProperties(
    license: String,
    userId: String,
) = CoroutineScope(Dispatchers.Main).launch {
    val engine = Engine.getInstance(id = "ly.img.engine.example")
    engine.start(license = license, userId = userId)
    engine.bindOffscreen(width = 100, height = 100)

    val scene = engine.scene.create()
    val text = engine.block.create(DesignBlockType.Text)
    engine.block.appendChild(parent = scene, child = text)
    engine.block.setWidthMode(text, mode = SizeMode.AUTO)
    engine.block.setHeightMode(text, mode = SizeMode.AUTO)

    engine.block.replaceText(text, text = "Hello World")

    // Add a "!" at the end of the text
    engine.block.replaceText(text, text = "!", from = 11)

    // Replace "World" with "Alex"
    engine.block.replaceText(text, text = "Alex", from = 6, to = 11)

    engine.scene.zoomToBlock(
        block = text,
        paddingLeft = 100F,
        paddingTop = 100F,
        paddingRight = 100F,
        paddingBottom = 100F,
    )

    // Remove the "Hello "
    engine.block.removeText(text, from = 0, to = 6)

    engine.block.setTextColor(text, color = Color.fromHex("#FFFF0000"))

    engine.block.setTextColor(text, color = Color.fromHex("#FFFF0000"), from = 1, to = 4)

    val allColors = engine.block.getTextColors(text)

    val colorsInRange = engine.block.getTextColors(text, from = 2, to = 5)

    engine.block.setBoolean(text, property = "backgroundColor/enabled", value = true)

    val color = engine.block.getColor(text, property = "backgroundColor/color")
    engine.block.setColor(text, property = "backgroundColor/color", value = Color.fromRGBA(r = 0, g = 0, b = 1, a = 1))

    engine.block.setFloat(text, property = "backgroundColor/paddingLeft", value = 1.0F)
    engine.block.setFloat(text, property = "backgroundColor/paddingTop", value = 2.0F)
    engine.block.setFloat(text, property = "backgroundColor/paddingRight", value = 3.0F)
    engine.block.setFloat(text, property = "backgroundColor/paddingBottom", value = 4.0F)

    engine.block.setFloat(text, property = "backgroundColor/cornerRadius", value = 4.0F)

    val animation = engine.block.createAnimation(AnimationType.Slide)
    engine.block.setEnum(animation, property = "textAnimationWritingStyle", value = "Block")

    engine.block.setInAnimation(text, animation = animation)
    engine.block.setOutAnimation(text, animation = animation)

    engine.block.setTextCase(text, textCase = TextCase.TITLE_CASE)

    val textCases = engine.block.getTextCases(text)

    val typeface =
        Typeface(
            name = "Roboto",
            fonts =
                listOf(
                    Font(
                        uri = Uri.parse("https://cdn.img.ly/assets/v2/ly.img.typeface/fonts/Roboto/Roboto-Bold.ttf"),
                        subFamily = "Bold",
                        weight = FontWeight.BOLD,
                        style = FontStyle.NORMAL,
                    ),
                    Font(
                        uri = Uri.parse("https://cdn.img.ly/assets/v2/ly.img.typeface/fonts/Roboto/Roboto-BoldItalic.ttf"),
                        subFamily = "Bold Italic",
                        weight = FontWeight.BOLD,
                        style = FontStyle.ITALIC,
                    ),
                    Font(
                        uri = Uri.parse("https://cdn.img.ly/assets/v2/ly.img.typeface/fonts/Roboto/Roboto-Italic.ttf"),
                        subFamily = "Italic",
                        weight = FontWeight.BOLD,
                        style = FontStyle.NORMAL,
                    ),
                    Font(
                        uri = Uri.parse("https://cdn.img.ly/assets/v2/ly.img.typeface/fonts/Roboto/Roboto-Regular.ttf"),
                        subFamily = "Regular",
                        weight = FontWeight.NORMAL,
                        style = FontStyle.NORMAL,
                    ),
                ),
        )
    engine.block.setFont(text, typeface.fonts[3].uri, typeface)

    engine.block.setTypeface(text, typeface, from = 1, to = 4)
    engine.block.setTypeface(text, typeface)

    val currentDefaultTypeface = engine.block.getTypeface(text)

    val currentTypefaces = engine.block.getTypefaces(text)
    val currentTypefacesOfRange = engine.block.getTypefaces(text, from = 1, to = 4)

    if (engine.block.canToggleBoldFont(text)) {
        engine.block.toggleBoldFont(text)
    }
    if (engine.block.canToggleBoldFont(text, from = 1, to = 4)) {
        engine.block.toggleBoldFont(text, from = 1, to = 4)
    }

    if (engine.block.canToggleItalicFont(text)) {
        engine.block.toggleItalicFont(text)
    }
    if (engine.block.canToggleItalicFont(text, from = 1, to = 4)) {
        engine.block.toggleItalicFont(text, from = 1, to = 4)
    }

    val fontWeights = engine.block.getTextFontWeights(text)

    engine.block.setTextFontStyle(text, FontStyle.NORMAL)
    val fontStyles = engine.block.getTextFontStyles(text)

    engine.stop()
}
```



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
