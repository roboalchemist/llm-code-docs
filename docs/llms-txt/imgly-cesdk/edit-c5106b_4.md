# Source: https://img.ly/docs/cesdk/ios/text/edit-c5106b/

---
title: "Edit Text"
description: "Edit text content directly on the canvas or through the properties panel."
platform: ios
url: "https://img.ly/docs/cesdk/ios/text/edit-c5106b/"
---

> This is one page of the CE.SDK iOS documentation. For a complete overview, see the [iOS Documentation Index](https://img.ly/docs/cesdk/ios.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/ios/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/ios/guides-8d8b00/) > [Create and Edit Text](https://img.ly/docs/cesdk/ios/text-8a993a/) > [Edit Text](https://img.ly/docs/cesdk/ios/text/edit-c5106b/)

---

```swift reference-only
let text = try engine.block.create(.text)

try engine.block.replaceText(text, text: "Hello World")
try engine.block.removeText(text, from: "Hello World".range(of: "Hello ")!)
try engine.block.setTextColor(
  text,
  color: .rgba(r: 0, g: 0, b: 0),
  in: "World".index(after: "World".startIndex) ..< "World".index(before: "World".endIndex)
)
let colorsInRange = try engine.block.getTextColors(text)
try engine.block.setTextFontWeight(text, fontWeight: .bold, "World".index(after: "World".startIndex) ..< "World".index(before: "World".endIndex)
let fontWeights = try engine.block.getTextFontWeights(text)
try engine.block.setTextFontSize(text, fontSize: 14, "World".index(after: "World".startIndex) ..< "World".index(before: "World".endIndex)
let fontSizes = try engine.block.getTextFontSizes(text)
try engine.block.setTextFontStyle(text, fontStyle: .italic, "World".index(after: "World".startIndex) ..< "World".index(before: "World".endIndex)
let fontStyles = try engine.block.getTextFontStyles(text)
try engine.block.setTextCase(text, textCase: .titlecase)
let textCases = try engine.block.getTextCases(text)
let canToggleBold = try engine.block.canToggleBoldFont(text)
let canToggleItalic = try engine.block.canToggleItalicFont(text)
try engine.block.toggleBoldFont(text)
try engine.block.toggleItalicFont(text)
let typefaceAssetResults = try await engine.asset.findAssets(
  sourceID: "ly.img.typeface",
  query: .init(
    query: "Open Sans",
    page: 0,
    perPage: 100
  )
)
let typeface = typefaceAssetResults.assets[0].payload?.typeface
let font = typeface!.fonts.first { font in font.subFamily == "Bold" }
try engine.block.setFont(text, fontFileURL: font!.uri, typeface: typeface!)
try engine.block.setTypeface(text, typeface: typeface!, "World".index(after: "World".startIndex) ..< "World".index(before: "World".endIndex)
try engine.block.setTypeface(text, typeface: typeface!)
let defaultTypeface = try engine.block.getTypeface(text)
let typefaces = try engine.block.getTypefaces(text)
let selectedRange = try engine.block.getTextCursorRange()
try engine.block.setTextCursorRange(text.startIndex..<text.index(text.startIndex, offsetBy: 5))
let lineCount = try engine.block.getTextVisibleLineCount(text)
let lineBoundingBox = try engine.block.getTextLineBoundingBoxRect(text, 0)
let fontMetrics = try await engine.editor.getFontMetrics(fontFileURI: font!.uri.absoluteString)
```

In this example, we will show you how to use the [CreativeEditor SDK](https://img.ly/products/creative-sdk)'s CreativeEngine to edit ranges within text blocks.

```swift
public func replaceText(_ id: DesignBlockID, text: String, in subrange: Range<String.Index>? = nil) throws
```

Replaces the given text in the selected range of the text block.
Required scope: "text/edit"

- `id`: The text block into which to insert the given text.
- `text`: The text which should replace the selected range in the block.
- `subrange`: The subrange of the string to replace. The bounds of the range must be valid indices of the string.
- Note: Passing `nil` to subrange is equivalent to the entire extisting string.

```swift
public func removeText(_ id: DesignBlockID, from subrange: Range<String.Index>? = nil) throws
```

Removes selected range of text of the given text block.
Required scope: "text/edit"

- `id`: The text block from which the selected text should be removed.
- `subrange`: The subrange of the string to replace. The bounds of the range must be valid indices of the string.
- Note: Passing `nil` to subrange is equivalent to the entire extisting string.

```swift
public func setTextColor(_ id: DesignBlockID, color: Color, in subrange: Range<String.Index>? = nil) throws
```

Changes the color of the text in the selected range to the given color.
Required scope: "fill/change"

- `id`: The text block whose color should be changed.
- `color`: The new color of the selected text range.
- `subrange`: The subrange of the string whose colors should be set. The bounds of the range must be valid indices
  of the string.
- Note: Passing `nil` to subrange is equivalent to the entire extisting string.

```swift
public func getTextColors(_ id: DesignBlockID, in subrange: Range<String.Index>? = nil) throws -> [Color]
```

Returns the ordered unique list of colors of the text in the selected range.

- `id`: The text block whose colors should be returned.
- `subrange`: The subrange of the string whose colors should be returned. The bounds of the range must be valid
  indices of the string.
- Note: Passing `nil` to subrange is equivalent to the entire extisting string.
- Returns: The text colors from the selected subrange.

```swift
public func setTextFontWeight(_ id: DesignBlockID, fontWeight: FontWeight, in subrange: Range<String.Index>? = nil) throws
```

Sets the given text weight for the selected range of text.
Required scope: "text/character"

- `id`: The text block whose text weight should be changed.
- `fontWeight`: The new weight of the selected text range.
- `subrange`: The subrange of the string whose weight should be set. The bounds of the range must be valid
  indices of the string.
- Note: Passing `nil` to subrange is equivalent to the entire extisting string.

```swift
public func getTextFontWeights(_ id: DesignBlockID, in subrange: Range<String.Index>? = nil) throws -> [FontWeight]
```

Returns the ordered unique list of font weights of the text in the selected range.

- `id`: The text block whose font weights should be returned.
- `subrange`: The subrange of the string whose font weights should be returned. The bounds of the range must be
  valid indices of the string.
- Note: Passing `nil` to subrange is equivalent to the entire extisting string.
- Returns: The font weights from the selected subrange.

```swift
public func setTextFontSize(_ id: DesignBlockID, fontSize: Float, in subrange: Range<String.Index>? = nil) throws
```

Sets the given text font size for the selected range of text.
If the font size is applied to the entire text block, its font size property will be updated.
Required scope: "text/character"

- `id`: The text block whose text font size should be changed.
- `fontSize`: The new font size of the selected text range.
- `subrange`: The subrange of the string whose size should be set. The bounds of the range must be valid
  indices of the string.
- Note: Passing `nil` to subrange is equivalent to the entire extisting string.

```swift
public func getTextFontSizes(_ id: DesignBlockID, in subrange: Range<String.Index>? = nil) throws -> [Float]
```

Returns the ordered unique list of font sizes of the text in the selected range.

- `id`: The text block whose font sizes should be returned.
- `subrange`: The subrange of the string whose font sizes should be returned. The bounds of the range must be
  valid indices of the string.
- Note: Passing `nil` to subrange is equivalent to the entire extisting string.
- Returns: The font sizes from the selected subrange.

```swift
public func setTextFontStyle(_ id: DesignBlockID, fontStyle: FontStyle, in subrange: Range<String.Index>? = nil) throws
```

Sets the given text style for the selected range of text.
Required scope: "text/character"

- `id`: The text block whose text style should be changed.
- `fontStyle`: The new style of the selected text range.
- `subrange`: The subrange of the string whose style should be set. The bounds of the range must be valid
  indices of the string.
- Note: Passing `nil` to subrange is equivalent to the entire extisting string.

```swift
public func getTextFontStyles(_ id: DesignBlockID, in subrange: Range<String.Index>? = nil) throws -> [FontStyle]
```

Returns the ordered unique list of font styles of the text in the selected range.

- `id`: The text block whose font styles should be returned.
- `subrange`: The subrange of the string whose font styles should be returned. The bounds of the range must be
  valid indices of the string.
- Note: Passing `nil` to subrange is equivalent to the entire extisting string.
- Returns: The font styles from the selected subrange.

```swift
public func setTextCase(_ id: DesignBlockID, textCase: TextCase, in subrange: Range<String.Index>? = nil) throws
```

Sets the given text case for the selected range of text.
Required scope: "text/character"

- `id`: The text block whose text case should be changed.
- `textCase`: The new text case value.
- `subrange`: The subrange of the string whose text cases should be set. The bounds of the range must be valid
  indices of the string.
- Note: Passing `nil` to subrange is equivalent to the entire extisting string.

```swift
public func getTextCases(_ id: DesignBlockID, in subrange: Range<String.Index>? = nil) throws -> [TextCase]
```

Returns the ordered list of text cases of the text in the selected range.

- `id`: The text block whose text cases should be returned.
- `subrange`: The subrange of the string whose text cases should be returned. The bounds of the range must be
  valid indices of the string.
- Note: Passing `nil` to subrange is equivalent to the entire extisting string.
- Returns: The text cases from the selected subrange.

```swift
public func canToggleBoldFont(_ id: DesignBlockID, in subrange: Range<String.Index>? = nil) throws -> Bool
```

Returns whether the font weight of the given block can be toggled between bold and normal.

- `id`: The text block block whose font weight should be toggled.
- `subrange`: The subrange of the string whose font weight should be toggled. The bounds of the range must be
  valid indices of the string.
- Returns:`true`, if the font weight of the given block can be toggled between bold and normal, `false` otherwise.

```swift
public func canToggleItalicFont(_ id: DesignBlockID, in subrange: Range<String.Index>? = nil) throws -> Bool
```

Returns whether the font style of the given block can be toggled between italic and normal.

- `id`: The text block block whose font style should be toggled.
- `subrange`: The subrange of the string whose font style should be toggled. The bounds of the range must be valid
  indices of the string.
- Returns: `true`, if the font style of the given block can be toggled between bold and normal, `false` otherwise.

```swift
public func toggleBoldFont(_ id: DesignBlockID, in subrange: Range<String.Index>? = nil) throws
```

Toggles the font weight of the given block between bold and normal.
Required scope: "text/character"

- `id`: The text block whose font weight should be toggled.
- `subrange`: The subrange of the string whose font weight should be toggled. The bounds of the range must be
  valid indices of the string.

```swift
public func toggleItalicFont(_ id: DesignBlockID, in subrange: Range<String.Index>? = nil) throws
```

Toggles the font style of the given block between italic and normal.
Required scope: "text/character"

- `id`: The text block whose font style should be toggled.
- `subrange`: The subrange of the string whose font style should be toggled. The bounds of the range must be valid
  indices of the string.

```swift
public func setFont(_ id: DesignBlockID, fontFileURL: URL, typeface: Typeface) throws
```

Sets the given font and typeface for the text block.
Existing formatting is reset.
Required scope: "text/character"

- `id`: The text block whose font should be changed.
- `fontFileURL`: The URL of the new font file.
- `typeface`: The typeface of the new font.

```swift
public func setTypeface(_ id: DesignBlockID, typeface: Typeface, in subrange: Range<String.Index>? = nil) throws
```

Sets the given font and typeface for the text block. The current formatting, e.g., bold or italic, is retained as
far as possible. Some formatting might change if the new typeface does not support it, e.g. thin might change to
light, bold to normal, and/or italic to non-italic.
If the typeface is applied to the entire text block, its typeface property will be updated.
If a run does not support the new typeface, it will fall back to the default typeface from the typeface property.
Required scope: "text/character"

- `id`: The text block whose font should be changed.
- `typeface`: The new typeface.
- `subrange`: The subrange of the string whose font sizes should be returned. The bounds of the range must be
  valid indices of the string.

```swift
public func getTypeface(_ id: DesignBlockID) throws -> Typeface
```

Returns the typeface property of the text block. Does not return the typefaces of the text runs.

- `id:`: The text block whose typeface should be returned.
- Returns: The typeface of the text block.

```swift
public func getTypefaces(_ id: DesignBlockID, in subrange: Range<String.Index>? = nil) throws -> [Typeface]
```

Returns the typefaces of the text block.

- `id`: The text block whose typeface should be returned.
- `subrange`: The subrange of the string whose typefaces should be returned. The bounds of the rangemust be valid
  indices of the string.
- `Returns`: The typefaces of the text block.

```swift
public func getTextCursorRange() throws -> Range<String.Index>?
```

Returns the indices of the selected grapheme range of the text block that is currently being edited.
If both the start and end index of the returned range have the same value, then the text cursor is positioned at
that index.

- Returns: The selected grapheme range or `nil` if no text block is currently being edited.

```swift
public func setTextCursorRange(_ range: Range<String.Index>) throws
```

Sets the text cursor range (selection) within the text block that is currently being edited.
Required scope: "text/edit"

- `range`: The grapheme range to set as the selection. If the range has equal bounds, the cursor is positioned at that index. To select all text, use `text.startIndex..<text.endIndex`.
- Throws: An error if no text block is currently being edited or if the range is invalid.

```swift
public func getTextVisibleLineCount(_ id: DesignBlockID) throws -> Int
```

Returns the number of visible lines in the given text block.

- `id:`: The text block whose line count should be returned.
- Returns: The number of lines in the text block.

```swift
public func getTextLineBoundingBoxRect(_ id: DesignBlockID, index: Int) throws -> CGRect
```

Returns the bounds of the visible area of the given line of the text block.
The values are in the scene's global coordinate space (which has its origin at the top left).

- `id`: The text block whose line bounding box should be returned.
- `index`: The index of the line whose bounding box should be returned.
- Returns: The bounding box of the line.

```swift
public func getFontMetrics(fontFileURI: String) async throws -> FontMetrics
```

Returns the font metrics for a given font file URI.
If the font is not yet loaded, it will be fetched asynchronously.
The returned metrics are in the font's design units coordinate space.

- `fontFileURI`: The URI of the font file to get metrics from.
- Returns: The font metrics containing `ascender`, `descender`, `unitsPerEm`, `lineGap`, `capHeight`, `xHeight`, `underlineOffset`, `underlineSize`, `strikeoutOffset`, and `strikeoutSize` values.

## Full Code

Here's the full code:

```swift
let text = try engine.block.create(.text)

try engine.block.replaceText(text, text: "Hello World")
try engine.block.removeText(text, from: "Hello World".range(of: "Hello ")!)
try engine.block.setTextColor(
  text,
  color: .rgba(r: 0, g: 0, b: 0),
  in: "World".index(after: "World".startIndex) ..< "World".index(before: "World".endIndex)
)
let colorsInRange = try engine.block.getTextColors(text)
try engine.block.setTextFontWeight(text, fontWeight: .bold, "World".index(after: "World".startIndex) ..< "World".index(before: "World".endIndex)
let fontWeights = try engine.block.getTextFontWeights(text)
try engine.block.setTextFontSize(text, fontSize: 14, "World".index(after: "World".startIndex) ..< "World".index(before: "World".endIndex)
let fontSizes = try engine.block.getTextFontSizes(text)
try engine.block.setTextFontStyle(text, fontStyle: .italic, "World".index(after: "World".startIndex) ..< "World".index(before: "World".endIndex)
let fontStyles = try engine.block.getTextFontStyles(text)
try engine.block.setTextCase(text, textCase: .titlecase)
let textCases = try engine.block.getTextCases(text)
let canToggleBold = try engine.block.canToggleBoldFont(text)
let canToggleItalic = try engine.block.canToggleItalicFont(text)
try engine.block.toggleBoldFont(text)
try engine.block.toggleItalicFont(text)
let typefaceAssetResults = try await engine.asset.findAssets(
  sourceID: "ly.img.typeface",
  query: .init(
    query: "Open Sans",
    page: 0,
    perPage: 100
  )
)
let typeface = typefaceAssetResults.assets[0].payload?.typeface
let font = typeface!.fonts.first { font in font.subFamily == "Bold" }
try engine.block.setFont(text, fontFileURL: font!.uri, typeface: typeface!)
try engine.block.setTypeface(text, typeface: typeface!, "World".index(after: "World".startIndex) ..< "World".index(before: "World".endIndex)
try engine.block.setTypeface(text, typeface: typeface!)
let defaultTypeface = try engine.block.getTypeface(text)
let typefaces = try engine.block.getTypefaces(text)
let selectedRange = try engine.block.getTextCursorRange()
let textString = try engine.block.getString(text, property: "text/text")
try engine.block.setTextCursorRange(textString.startIndex..<textString.index(textString.startIndex, offsetBy: 5))
let lineCount = try engine.block.getTextVisibleLineCount(text)
let lineBoundingBox = try engine.block.getTextLineBoundingBoxRect(text, 0)
let fontMetrics = try await engine.editor.getFontMetrics(fontFileURI: font!.uri.absoluteString)
```



---

## More Resources

- **[iOS Documentation Index](https://img.ly/docs/cesdk/ios.md)** - Browse all iOS documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/ios/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/ios/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
