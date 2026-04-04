# Source: https://img.ly/docs/cesdk/android/text/edit-c5106b/

---
title: "Edit Text"
description: "Edit text content directly on the canvas or through the properties panel."
platform: android
url: "https://img.ly/docs/cesdk/android/text/edit-c5106b/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [Create and Edit Text](https://img.ly/docs/cesdk/android/text-8a993a/) > [Edit Text](https://img.ly/docs/cesdk/android/text/edit-c5106b/)

---

```kotlin reference-only
val text = engine.block.create(DesignBlockType.Text)

engine.block.replaceText(text, "Hello World")
engine.block.removeText(text, from = 0, to = 6)
engine.block.setTextColor(text, Color.fromHex("#FFFF0000"), from = 1, to = 4)
val colorsInRange = engine.block.getTextColors(text, from = 2, to = 5)
engine.block.setTextFontWeight(text, fontWeight = FontWeight.BOLD, from = 0, to = 5)
val fontWeights = engine.block.getTextFontWeights(text)
val fontWeights = engine.block.setTextFontSize(text, fontSize: 14, from = 2, to = 5)
val fontWeights = engine.block.getTextFontSizes(text)
engine.block.setTextFontStyle(text, fontStyle = FontStyle.ITALIC, from = 0, to = 5)
val fontStyles = engine.block.getTextFontStyles(text)
engine.block.setTextCase(text, textCase = TextCase.TITLE_CASE)
val textCases = engine.block.getTextCases()
val canToggleBoldFont = engine.block.canToggleBoldFont(text)
val canToggleItalicFont = engine.block.canToggleItalicFont(text)
engine.block.toggleBoldFont(text)
engine.block.toggleItalicFont(text)
val typefaceAssetResults = engine.asset.findAssets(
    sourceId = "ly.img.typeface",
    query = FindAssetsQuery(
        query = "Open Sans",
        page = 0,
        perPage = 100
    )
)
val typeface = typefaceAssetResults.assets[0].payload.typeface
val font = typeface.fonts.first { font -> font.subFamily == "Bold" }
engine.block.setFont(text, font.uri, typeface)
engine.block.setTypeface(text, typeface, from = 0, to = 5)
engine.block.setTypeface(text, typeface)
val defaultTypeface = engine.block.getTypeface(text)
val typefaces = engine.block.getTypefaces(text)
val range = engine.block.getTextCursorRange()
engine.block.setTextCursorRange(0..5)
val lineCount = engine.block.getTextVisibleLineCount(text)
val lineBoundingBox = engine.block.getTextLineBoundingBoxRect(text, 0)
val fontMetrics = engine.editor.getFontMetrics(fontFileUri = font.uri.toString())
```

In this example, we will show you how to use the [CreativeEditor SDK](https://img.ly/products/creative-sdk)'s CreativeEngine to edit ranges within text blocks.
A list of all available settings can be found above.

```kotlin
fun replaceText(
    block: DesignBlock,
    text: String,
    from: Int = -1,
    to: Int = -1,
)
```

Inserts the given text into the selected range of the text block.

Required scope: "text/edit"

- `block`: the text block into which to insert the given text.

- `text`: the text which should replace the selected range in the block.

- `from`: the start index of the range that should be replaced.

If the value is negative, this will fall back to the start of the entire text range.

- `to`: the index after the last character that should be replaced by the inserted text.

If the value is negative, this will fall back to the end of the entire text range.

```kotlin
fun removeText(
    block: DesignBlock,
    from: Int = -1,
    to: Int = -1,
)
```

Removes selected range of text of the given text block.

Required scope: "text/edit"

- `block`: the text block from which the selected text should be removed.

- `from`: the start index of the range that should be removed.

If the value is negative, this will fall back to the start of the entire text range.

- `to`: the index after the last character that should be removed.

If the value is negative, this will fall back to the end of the entire text range.

```kotlin
fun setTextColor(
    block: DesignBlock,
    color: Color,
    from: Int = -1,
    to: Int = -1,
)
```

Changes the color of the text in the selected range to the given color.

Required scope: "fill/change"

- `block`: the text block whose color should be changed.

- `color`: the new color of the selected text range.

- `from`: the start index of the range whose color should be changed.

If the value is negative and the block is currently being edited, this will fall back to the start of the current cursor index / selected range.

If the value is negative and the block is not being edited, this will fall back to the start of the entire text range.

- `to`: the index after the last character whose color should be changed.

If the value is negative and the block is currently being edited, this will fall back to the end of the current cursor index / selected range.

If the value is negative and the block is not being edited, this will fall back to the end of the entire text range.

```kotlin
fun getTextColors(
    block: DesignBlock,
    from: Int = -1,
    to: Int = -1,
): List<Color>
```

Returns the ordered unique list of colors of the text in the selected range.

- `block`: the text block whose colors should be returned.

- `from`: the start index of the range whose colors should be returned.

If the value is negative and the block is currently being edited, this will fall back to the start of the current cursor index / selected range.

If the value is negative and the block is not being edited, this will fall back to the start of the entire text range.

- `to`: the index after the last character of the range whose colors should be returned.

If the value is negative and the block is currently being edited, this will fall back to the end of the current cursor index / selected range.

If the value is negative and the block is not being edited, this will fall back to the end of the entire text range.

- Returns the ordered unique list of colors of the text in the selected range.

```kotlin
fun setTextFontWeight(
    block: DesignBlock,
    fontWeight: FontWeight,
    from: Int = -1,
    to: Int = -1,
)
```

Changes the weight of the text in the selected range to the given weight.

Required scope: "text/character"

- `block`: the text block whose weight should be changed.

- `fontWeight`: the new weight of the selected text range.

- `from`: the start index of the UTF-16 range whose weight should be changed.

If the value is negative and the block is currently being edited, this will fall back to the start of the current cursor index / selected grapheme range.

If the value is negative and the block is not being edited, this will fall back to the start of the entire text range.

- `to`: the UTF-16 index after the last grapheme whose weight should be changed.

If the value is negative and the block is currently being edited, this will fall back to the end of the current cursor index / selected grapheme range.

If the value is negative and the block is not being edited, this will fall back to the end of the entire text range.

```kotlin
fun getTextFontWeights(
    block: DesignBlock,
    from: Int = -1,
    to: Int = -1,
): List<FontWeight>
```

Returns the ordered unique list of font weights of the text in the selected range.

- `block`: the text block whose font weights should be returned.

- `from`: the start index of the range whose font weights should be returned.

If the value is negative and the block is currently being edited, this will fall back to the start of the current cursor index / selected range.

If the value is negative and the block is not being edited, this will fall back to the start of the entire text range.

- `to`: the index after the last character of the range whose font weights should be returned.

If the value is negative and the block is currently being edited, this will fall back to the end of the current cursor index / selected range.

If the value is negative and the block is not being edited, this will fall back to the end of the entire text range.

- Returns the ordered unique list of font weights of the text in the selected range.

```kotlin
fun setTextFontSize(
    block: DesignBlock,
    fontSize: Float,
    from: Int = -1,
    to: Int = -1,
)
```

Changes the size of the text in the selected range to the given size.

If the font size is applied to the entire text block, its font size property will be updated.

Required scope: "text/character"

- `block`: the text block whose size should be changed.

- `fontStyle`: the new size of the selected text range.

- `from`: the start index of the UTF-16 range whose size should be changed.

If the value is negative and the block is currently being edited, this will fall back to the start of the current cursor index / selected grapheme range.

If the value is negative and the block is not being edited, this will fall back to the start of the entire text range.

- `to`: the UTF-16 index after the last grapheme whose size should be changed.

If the value is negative and the block is currently being edited, this will fall back to the end of the current cursor index / selected grapheme range.

If the value is negative and the block is not being edited, this will fall back to the end of the entire text range.

```kotlin
fun getTextFontSizes(
    block: DesignBlock,
    from: Int = -1,
    to: Int = -1,
): List<Float>
```

Returns the ordered unique list of font sizes of the text in the selected range.

- `block`: the text block whose font sizes should be returned.

- `from`: the start index of the range whose font sizes should be returned.

If the value is negative and the block is currently being edited, this will fall back to the start of the current cursor index / selected range.

If the value is negative and the block is not being edited, this will fall back to the start of the entire text range.

- `to`: the index after the last character of the range whose font sizes should be returned.

If the value is negative and the block is currently being edited, this will fall back to the end of the current cursor index / selected range.

If the value is negative and the block is not being edited, this will fall back to the end of the entire text range.

- Returns the ordered unique list of font sizes of the text in the selected range.

```kotlin
fun setTextFontStyle(
    block: DesignBlock,
    fontStyle: FontStyle,
    from: Int = -1,
    to: Int = -1,
)
```

Changes the style of the text in the selected range to the given style.

Required scope: "text/character"

- `block`: the text block whose style should be changed.

- `fontStyle`: the new style of the selected text range.

- `from`: the start index of the UTF-16 range whose style should be changed.

If the value is negative and the block is currently being edited, this will fall back to the start of the current cursor index / selected grapheme range.

If the value is negative and the block is not being edited, this will fall back to the start of the entire text range.

- `to`: the UTF-16 index after the last grapheme whose style should be changed.

If the value is negative and the block is currently being edited, this will fall back to the end of the current cursor index / selected grapheme range.

If the value is negative and the block is not being edited, this will fall back to the end of the entire text range.

```kotlin
fun getTextFontStyles(
    block: DesignBlock,
    from: Int = -1,
    to: Int = -1,
): List<FontStyle>
```

Returns the ordered unique list of font styles of the text in the selected range.

- `block`: the text block whose font styles should be returned.

- `from`: the start index of the range whose font styles should be returned.

If the value is negative and the block is currently being edited, this will fall back to the start of the current cursor index / selected range.

If the value is negative and the block is not being edited, this will fall back to the start of the entire text range.

- `to`: the index after the last character of the range whose font styles should be returned.

If the value is negative and the block is currently being edited, this will fall back to the end of the current cursor index / selected range.

If the value is negative and the block is not being edited, this will fall back to the end of the entire text range.

- Returns the ordered unique list of font styles of the text in the selected range.

```kotlin
fun setTextFontStyle(
    block: DesignBlock,
    fontStyle: FontStyle,
    from: Int = -1,
    to: Int = -1,
)
```

Changes the style of the text in the selected range to the given style.

Required scope: "text/character"

- `block`: the text block whose style should be changed.

- `fontStyle`: the new style of the selected text range.

- `from`: the start index of the UTF-16 range whose style should be changed.

If the value is negative and the block is currently being edited, this will fall back to the start of the current cursor index / selected grapheme range.

If the value is negative and the block is not being edited, this will fall back to the start of the entire text range.

- `to`: the UTF-16 index after the last grapheme whose style should be changed.

If the value is negative and the block is currently being edited, this will fall back to the end of the current cursor index / selected grapheme range.

If the value is negative and the block is not being edited, this will fall back to the end of the entire text range.

```kotlin
fun getTextFontStyles(
    block: DesignBlock,
    from: Int = -1,
    to: Int = -1,
): List<FontStyle>
```

Returns the ordered unique list of font styles of the text in the selected range.

- `block`: the text block whose font styles should be returned.

- `from`: the start index of the range whose font styles should be returned.

If the value is negative and the block is currently being edited, this will fall back to the start of the current cursor index / selected range.

If the value is negative and the block is not being edited, this will fall back to the start of the entire text range.

- `to`: the index after the last character of the range whose font styles should be returned.

If the value is negative and the block is currently being edited, this will fall back to the end of the current cursor index / selected range.

If the value is negative and the block is not being edited, this will fall back to the end of the entire text range.

- Returns the ordered unique list of font styles of the text in the selected range.

```kotlin
fun setTextCase(
    block: DesignBlock,
    textCase: TextCase,
    from: Int = -1,
    to: Int = -1,
)
```

Sets the given text case for the selected range of text.

Required scope: "text/character"

- `block`: the text block whose text case should be changed.

- `textCase`: the new text case value.

- `from`: the start index of the range whose text case should be changed.

If the value is negative and the block is currently being edited, this will fall back to the start of the current cursor index / selected range.

If the value is negative and the block is not being edited, this will fall back to the start of the entire text range.

- `to`: the index after the last character whose text case should be changed.

If the value is negative and the block is currently being edited, this will fall back to the end of the current cursor index / selected range.

If the value is negative and the block is not being edited, this will fall back to the end of the entire text range.

```kotlin
fun getTextCases(
    block: DesignBlock,
    from: Int = -1,
    to: Int = -1,
): List<TextCase>
```

Returns the ordered list of text cases of the text in the selected range.

- `block`: the text block whose text cases should be returned.

- `from`: the start index of the range whose text cases should be returned.

If the value is negative and the block is currently being edited, this will fall back to the start of the current cursor index / selected range.

If the value is negative and the block is not being edited, this will fall back to the start of the entire text range.

- `to`: the index after the last character of the range whose text cases should be returned.

If the value is negative and the block is currently being edited, this will fall back to the end of the current cursor index / selected range.

If the value is negative and the block is not being edited, this will fall back to the end of the entire text range.

- Returns the ordered list of text cases of the text in the selected range.

```kotlin
fun canToggleBoldFont(
    block: DesignBlock,
    from: Int = -1,
    to: Int = -1,
): Boolean
```

Returns whether the font weight of the given block can be toggled between bold and normal.

- `block`: the text block block whose font weight should be toggled.

- `from`: the start index of the range whose whose font weight should be toggled.

If the value is negative and the block is currently being edited, this will fall back to the start of the current cursor index / selected range.

If the value is negative and the block is not being edited, this will fall back to the start of the entire text range.

- `to`: the index after the last character whose whose font weight should be toggled.

If the value is negative and the block is currently being edited, this will fall back to the end of the current cursor index / selected range.

If the value is negative and the block is not being edited, this will fall back to the end of the entire text range.

```kotlin
fun canToggleItalicFont(
    block: DesignBlock,
    from: Int = -1,
    to: Int = -1,
): Boolean
```

Returns whether the font style of the given block can be toggled between italic and normal.

- `block`: the text block block whose font style should be toggled.

- `from`: the start index of the range whose text case should be changed.

If the value is negative and the block is currently being edited, this will fall back to the start of the current cursor index / selected range.

If the value is negative and the block is not being edited, this will fall back to the start of the entire text range.

- `to`: the index after the last character whose text case should be changed.

If the value is negative and the block is currently being edited, this will fall back to the end of the current cursor index / selected range.

If the value is negative and the block is not being edited, this will fall back to the end of the entire text range.

```kotlin
fun toggleBoldFont(
    block: DesignBlock,
    from: Int = -1,
    to: Int = -1,
)
```

Toggles the font weight of the given block between bold and normal.

Required scope: "text/character"

- `block`: the text block whose font weight should be toggled.

- `from`: the start index of the range whose font weight should be toggled.

If the value is negative and the block is currently being edited, this will fall back to the start of the current cursor index / selected range.

If the value is negative and the block is not being edited, this will fall back to the start of the entire text range.

- `to`: the index after the last character whose font weight should be toggled.

If the value is negative and the block is currently being edited, this will fall back to the end of the current cursor index / selected range.

If the value is negative and the block is not being edited, this will fall back to the end of the entire text range.

```kotlin
fun toggleItalicFont(
    block: DesignBlock,
    from: Int = -1,
    to: Int = -1,
)
```

Toggles the font style of the given block between italic and normal.

Required scope: "text/character"

- `block`: the text block whose font style should be toggled.

- `from`: the start index of the range whose text case should be changed.

If the value is negative and the block is currently being edited, this will fall back to the start of the current cursor index / selected range.

If the value is negative and the block is not being edited, this will fall back to the start of the entire text range.

- `to`: the index after the last character whose text case should be changed.

If the value is negative and the block is currently being edited, this will fall back to the end of the current cursor index / selected range.

If the value is negative and the block is not being edited, this will fall back to the end of the entire text range.

```kotlin
fun setFont(
    block: DesignBlock,
    fontFileUri: Uri,
    typeface: Typeface,
)
```

Sets the given font and typeface for the text block.

Existing formatting is reset.

Required scope: "text/character"

- `block`: the text block whose font should be changed.

- `fontFileUri`: the Uri of the new font file.

- `typeface`: the typeface of the new font.

```kotlin
fun setTypeface(
    block: DesignBlock,
    typeface: Typeface,
    from: Int = -1,
    to: Int = -1,
)
```

Sets the given typeface for the text block.

The current formatting, e.g., bold or italic, is retained as far as possible. Some formatting might change if the

new typeface does not support it, e.g. thin might change to light, bold to normal, and/or italic to non-italic.

If the typeface is applied to the entire text block, its typeface property will be updated.

If a run does not support the new typeface, it will fall back to the default typeface from the typeface property.

Required scope: "text/character"

- `block`: the text block whose font should be changed.

- `typeface`: the new typeface.

- `from`: the start index of the range whose typeface should be set.

If the value is negative and the block is currently being edited, this will fall back to the start of the current cursor index / selected range.

If the value is negative and the block is not being edited, this will fall back to the start of the entire text range.

- `to`: the index after the last character of the range whose typeface should be set.

If the value is negative and the block is currently being edited, this will fall back to the end of the current cursor index / selected range.

If the value is negative and the block is not being edited, this will fall back to the end of the entire text range.

```kotlin
fun getTypeface(block: DesignBlock): Typeface
```

Returns the typeface property of the text block. Does not return the typefaces of the text runs.

- `block`: the text block whose typeface should be returned.

- Returns the typeface of the text block or throws exception if the typeface is unknown.

```kotlin
fun getTypefaces(
    block: DesignBlock,
    from: Int = -1,
    to: Int = -1,
): List<Typeface>
```

Returns the typefaces of the text block.

- `block`: the text block whose typefaces should be returned.

- `from`: the start index of the range whose typefaces should be returned.

If the value is negative and the block is currently being edited, this will fall back to the start of the current cursor index / selected range.

If the value is negative and the block is not being edited, this will fall back to the start of the entire text range.

- `to`: the index after the last character of the range whose typefaces should be returned.

If the value is negative and the block is currently being edited, this will fall back to the end of the current cursor index / selected range.

If the value is negative and the block is not being edited, this will fall back to the end of the entire text range.

- Returns the typefaces of the text block or throws exception if the typeface is unknown.

```kotlin
fun getTextCursorRange(): IntRange?
```

Returns the indices of the selected range of the text block that is currently being edited.

If both the start and end index of the returned range have the same value, then the text cursor is positioned at

that index.

- Returns the selected grapheme range or null if no text block is currently being edited.

```kotlin
fun setTextCursorRange(range: IntRange)
```

Sets the text cursor range (selection) within the text block that is currently being edited.

Required scope: "text/edit"

- `range`: The grapheme range to set as the selection. If start equals end, the cursor is positioned at that index. You can use -1 as a shorthand: `-1..-1` selects all text, `-1..5` selects from start to position 5, and `5..-1` selects from position 5 to the end.

- Throws exception if no text block is currently being edited or if the range is invalid.

```kotlin
fun getTextVisibleLineCount(block: DesignBlock): Int
```

Returns the number of visible lines in the given text block.

- `block`: the text block whose line count should be returned.

- Returns the number of lines of text in the block.

```kotlin
fun getTextLineBoundingBoxRect(
    block: DesignBlock,
    index: Int,
): RectF
```

Returns the bounds of the visible area of the given line of the text block.

The values are in the scene's global coordinate space (which has its origin at the top left).

- `block`: the text block whose line bounding box should be returned.

- `index`: the index of the line whose bounding box should be returned.

- Returns the bounding box of the line.

```kotlin
suspend fun getFontMetrics(fontFileUri: String): FontMetrics
```

Returns the font metrics for a given font file URI.
If the font is not yet loaded, it will be fetched asynchronously.
The returned metrics are in the font's design units coordinate space.

- `fontFileUri`: the URI of the font file to get metrics from.

- Returns the font metrics containing `ascender`, `descender`, `unitsPerEm`, `lineGap`, `capHeight`, `xHeight`, `underlineOffset`, `underlineSize`, `strikeoutOffset`, and `strikeoutSize` values.

## Full Code

Here's the full code:

```kotlin
val text = engine.block.create(DesignBlockType.Text)

engine.block.replaceText(text, "Hello World")
engine.block.removeText(text, from = 0, to = 6)
engine.block.setTextColor(text, Color.fromHex("#FFFF0000"), from = 1, to = 4)
val colorsInRange = engine.block.getTextColors(text, from = 2, to = 5)
engine.block.setTextFontWeight(text, fontWeight = FontWeight.BOLD, from = 0, to = 5)
val fontWeights = engine.block.getTextFontWeights(text)
val fontWeights = engine.block.setTextFontSize(text, fontSize: 14, from = 2, to = 5)
val fontWeights = engine.block.getTextFontSizes(text)
engine.block.setTextFontStyle(text, fontStyle = FontStyle.ITALIC, from = 0, to = 5)
val fontStyles = engine.block.getTextFontStyles(text)
engine.block.setTextCase(text, textCase = TextCase.TITLE_CASE)
val textCases = engine.block.getTextCases()
val canToggleBoldFont = engine.block.canToggleBoldFont(text)
val canToggleItalicFont = engine.block.canToggleItalicFont(text)
engine.block.toggleBoldFont(text)
engine.block.toggleItalicFont(text)
val typefaceAssetResults = engine.asset.findAssets(
    sourceId = "ly.img.typeface",
    query = FindAssetsQuery(
        query = "Open Sans",
        page = 0,
        perPage = 100
    )
)
val typeface = typefaceAssetResults.assets[0].payload.typeface
val font = typeface.fonts.first { font -> font.subFamily == "Bold" }
engine.block.setFont(text, font.uri, typeface)
engine.block.setTypeface(text, typeface, from = 0, to = 5)
engine.block.setTypeface(text, typeface)
val defaultTypeface = engine.block.getTypeface(text)
val typefaces = engine.block.getTypefaces(text)
val range = engine.block.getTextCursorRange()
engine.block.setTextCursorRange(0..5)
val lineCount = engine.block.getTextVisibleLineCount(text)
val lineBoundingBox = engine.block.getTextLineBoundingBoxRect(text, 0)
val fontMetrics = engine.editor.getFontMetrics(fontFileUri = font.uri.toString())
```



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
