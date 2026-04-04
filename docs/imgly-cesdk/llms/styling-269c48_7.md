# Source: https://img.ly/docs/cesdk/macos/text/styling-269c48/

---
title: "Text Styling"
description: "Apply fonts, colors, alignment, and other styling options to customize text appearance."
platform: macos
url: "https://img.ly/docs/cesdk/macos/text/styling-269c48/"
---

> This is one page of the CE.SDK macOS documentation. For a complete overview, see the [macOS Documentation Index](https://img.ly/docs/cesdk/macos.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/macos/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/macos/guides-8d8b00/) > [Create and Edit Text](https://img.ly/docs/cesdk/macos/text-8a993a/) > [Text Styling](https://img.ly/docs/cesdk/macos/text/styling-269c48/)

---

```swift file=@cesdk_swift_examples/engine-guides-text-properties/TextProperties.swift reference-only
import Foundation
import IMGLYEngine

@MainActor
func textProperties(engine: Engine) async throws {
  let scene = try engine.scene.create()
  let text = try engine.block.create(.text)
  try engine.block.appendChild(to: scene, child: text)
  try engine.block.setWidthMode(text, mode: .auto)
  try engine.block.setHeightMode(text, mode: .auto)

  try engine.block.replaceText(text, text: "Hello World")
  // Add a "!" at the end of the text
  try engine.block.replaceText(text, text: "!", in: "Hello World".endIndex ..< "Hello World".endIndex)
  // Replace "World" with "Alex"
  try engine.block.replaceText(text, text: "Alex", in: "Hello World".range(of: "World")!)

  try await engine.scene.zoom(to: text, paddingLeft: 100, paddingTop: 100, paddingRight: 100, paddingBottom: 100)

  // Remove the "Hello "
  try engine.block.removeText(text, from: "Hello Alex".range(of: "Hello ")!)

  try engine.block.setTextColor(text, color: .rgba(r: 1, g: 1, b: 0))
  try engine.block.setTextColor(text, color: .rgba(r: 0, g: 0, b: 0), in: "Alex".range(of: "lex")!)
  let allColors = try engine.block.getTextColors(text)
  let colorsInRange = try engine.block.getTextColors(text, in: "Alex".range(of: "lex")!)

  try engine.block.setBool(text, property: "backgroundColor/enabled", value: true)

  try engine.block.getColor(text, property: "backgroundColor/color") as Color
  try engine.block.setColor(text, property: "backgroundColor/color", color: .rgba(r: 0.0, g: 0.0, b: 1.0, a: 1.0))

  try engine.block.setFloat(text, property: "backgroundColor/paddingLeft", value: 1)
  try engine.block.setFloat(text, property: "backgroundColor/paddingTop", value: 2)
  try engine.block.setFloat(text, property: "backgroundColor/paddingRight", value: 3)
  try engine.block.setFloat(text, property: "backgroundColor/paddingBottom", value: 4)

  try engine.block.setFloat(text, property: "backgroundColor/cornerRadius", value: 4)

  let animation = try engine.block.createAnimation(AnimationType.slide)
  try engine.block.setEnum(animation, property: "textAnimationWritingStyle", value: "Block")

  try engine.block.setInAnimation(text, animation: animation)
  try engine.block.setOutAnimation(text, animation: animation)

  try engine.block.setTextCase(text, textCase: .titlecase)

  let textCases = try engine.block.getTextCases(text)

  let typeface = Typeface(
    name: "Roboto",
    fonts: [
      Font(
        uri: URL(string: "https://cdn.img.ly/assets/v4/ly.img.typeface/fonts/Roboto/Roboto-Bold.ttf")!,
        subFamily: "Bold",
        weight: .bold,
        style: .normal,
      ),
      Font(
        uri: URL(string: "https://cdn.img.ly/assets/v4/ly.img.typeface/fonts/Roboto/Roboto-BoldItalic.ttf")!,
        subFamily: "Bold Italic",
        weight: .bold,
        style: .italic,
      ),
      Font(
        uri: URL(string: "https://cdn.img.ly/assets/v4/ly.img.typeface/fonts/Roboto/Roboto-Italic.ttf")!,
        subFamily: "Italic",
        weight: .normal,
        style: .italic,
      ),
      Font(
        uri: URL(string: "https://cdn.img.ly/assets/v4/ly.img.typeface/fonts/Roboto/Roboto-Regular.ttf")!,
        subFamily: "Regular",
        weight: .normal,
        style: .normal,
      ),
    ],
  )
  try engine.block.setFont(text, fontFileURL: typeface.fonts[3].uri, typeface: typeface)

  try engine.block.setTypeface(text, typeface: typeface, in: "Alex".range(of: "lex")!)
  try engine.block.setTypeface(text, typeface: typeface)

  let currentDefaultTypeface = try engine.block.getTypeface(text)

  let currentTypefaces = try engine.block.getTypefaces(text)
  let currentTypefacesOfRange = try engine.block.getTypefaces(text, in: "Alex".range(of: "lex")!)

  if try engine.block.canToggleBoldFont(text) {
    try engine.block.toggleBoldFont(text)
  }
  if try engine.block.canToggleBoldFont(text, in: "Alex".range(of: "lex")!) {
    try engine.block.toggleBoldFont(text, in: "Alex".range(of: "lex")!)
  }

  if try engine.block.canToggleItalicFont(text) {
    try engine.block.toggleItalicFont(text)
  }
  if try engine.block.canToggleItalicFont(text, in: "Alex".range(of: "lex")!) {
    try engine.block.toggleItalicFont(text, in: "Alex".range(of: "lex")!)
  }

  try engine.block.setTextFontWeight(text, fontWeight: .bold)

  let fontWeights = try engine.block.getTextFontWeights(text)

  try engine.block.setTextFontStyle(text, fontStyle: .italic)

  let fontStyles = try engine.block.getTextFontStyles(text)
}
```

In this example, we want to show how to read and modify the text block's contents via the API in the CreativeEngine.

## Editing the Text String

You can edit the text string contents of a text block using the `func replaceText(_ id: DesignBlockID, text: String, in subrange: Range<String.Index>? = nil) throws` and `func removeText(_ id: DesignBlockID, from subrange: Range<String.Index>? = nil) throws` APIs.
The range of text that should be edited is defined using the native Swift `Range<String.Index>` type.

When passing `nil` to `subrange` argument, the entire existing string is replaced.

```swift highlight-replaceText
try engine.block.replaceText(text, text: "Hello World")
```

When specifying an empty range, the new text is inserted at its lower bound.

```swift highlight-replaceText-single-index
// Add a "!" at the end of the text
try engine.block.replaceText(text, text: "!", in: "Hello World".endIndex ..< "Hello World".endIndex)
```

To replace a specific text, `.range(of:)` can be used to find the range of the text to be replaced.

```swift highlight-replaceText-range
// Replace "World" with "Alex"
try engine.block.replaceText(text, text: "Alex", in: "Hello World".range(of: "World")!)
```

Similarly, the `removeText` API can be called to remove either a specific range or the entire text.

```swift highlight-removeText
// Remove the "Hello "
try engine.block.removeText(text, from: "Hello Alex".range(of: "Hello ")!)
```

## Text Colors

Text blocks in the CreativeEngine allow different ranges to have multiple colors.

Use the `func setTextColor(_ id: DesignBlockID, color: Color, in subrange: Range<String.Index>? = nil) throws` API to change either the color of the entire text

```swift highlight-setTextColor
try engine.block.setTextColor(text, color: .rgba(r: 1, g: 1, b: 0))
```

or only that of a range. After these two calls, the text "Alex!" now starts with one yellow character, followed by three black characters and two more yellow ones.

```swift highlight-setTextColor-range
try engine.block.setTextColor(text, color: .rgba(r: 0, g: 0, b: 0), in: "Alex".range(of: "lex")!)
```

The `func getTextColors(_ id: DesignBlockID, in subrange: Range<String.Index>? = nil) throws -> [Color]` API returns an ordered list of unique colors in the requested range. Here, `allColors` will be an array containing the colors yellow and black (in this order).

```swift highlight-getTextColors
let allColors = try engine.block.getTextColors(text)
```

When only the colors in the specific range are requested, the result will be an array containing black and then yellow, since black appears first in the requested range.

```swift highlight-getTextColors-range
let colorsInRange = try engine.block.getTextColors(text, in: "Alex".range(of: "lex")!)
```

## Text Background

You can create and edit the background of a text block by setting specific block properties.

To add a colored background to a text block use the `func setBool(_ id: DesignBlockID, property: String, value: Bool)` API and enable the `backgroundColor/enabled` property.

```swift highlight-backgroundColor-enabled
try engine.block.setBool(text, property: "backgroundColor/enabled", value: true)
```

The color of the text background can be queried (by making use of the `func getColor(_ id: DesignBlockID, property: String)` API ) and also changed (with the `func setColor(_ id: DesignBlockID, property: String, color: Color)` API).

```swift highlight-backgroundColor-get-set
try engine.block.getColor(text, property: "backgroundColor/color") as Color
```

The padding of the rectangular background shape can be edited by using the `func setFloat(_ id: DesignBlockID, property: String, value: Float)` API and setting the target value for the desired padding property like:

- `backgroundColor/paddingLeft`:
- `backgroundColor/paddingRight`:
- `backgroundColor/paddingTop`:
- `backgroundColor/paddingBottom`:

```swift highlight-backgroundColor-padding
try engine.block.setFloat(text, property: "backgroundColor/paddingLeft", value: 1)
```

Additionally, the rectangular shape of the background can be rounded by setting a corner radius with the `func setFloat(_ id: DesignBlockID, property: String, value: Float)` API to adjust the value of the `backgroundColor/cornerRadius` property.

```swift highlight-backgroundColor-cornerRadius
try engine.block.setFloat(text, property: "backgroundColor/cornerRadius", value: 4)
```

Text backgrounds inherit the animations assigned to their respective text block when the animation text writing style is set to `Block`.

```swift highlight-backgroundColor-animation
let animation = try engine.block.createAnimation(AnimationType.slide)
```

## Text Case

You can apply text case modifications to ranges of text in order to display them in upper case, lower case or title case. It is important to note that these modifiers do not change the `text` string value of the text block but are only applied when the block is rendered.

By default, the text case of all text within a text block is set to `.normal`, which does not modify the appearance of the text at all.

The `func setTextCase(_ id: DesignBlockID, textCase: TextCase, in subrange: Range<String.Index>? = nil) throws` API sets the given text case for the selected range of text.

Possible values for `TextCase` are:

- `.normal`: The text string is rendered without modifications.
- `.uppercase`: All characters are rendered in upper case.
- `.lowercase`: All characters are rendered in lower case.
- `.titlecase`: The first character of each word is rendered in upper case.

```swift highlight-setTextCase
try engine.block.setTextCase(text, textCase: .titlecase)
```

The `func getTextCases(_ id: DesignBlockID, in subrange: Range<String.Index>? = nil) throws -> [TextCase]` API returns the ordered list of text cases of the text in the selected range.

```swift highlight-getTextCases
let textCases = try engine.block.getTextCases(text)
```

## Typefaces

In order to change the font of a text block, you have to call the `setFont(_ id: DesignBlockID, fontFileURL: URL, typeface: Typeface) throws` API and provide it with both the url of the font file to be actively used and the complete typeface definition of the corresponding typeface. Existing formatting of the block is reset.

A typeface definition consists of the unique typeface name (as it is defined within the font files), and a list of all font definitions that belong to this typeface. Each font definition must provide a `uri` which points to the font file and a `subFamily` string which is this font's effective name within its typeface. The subfamily value is typically also defined within the font file.

For the sake of this example, we define a `Roboto` typeface with only four fonts: `Regular`, `Bold`, `Italic`, and `Bold Italic` and we change the font of the text block to the Roboto Regular font.

```swift highlight-setFont
let typeface = Typeface(
  name: "Roboto",
  fonts: [
    Font(
      uri: URL(string: "https://cdn.img.ly/assets/v4/ly.img.typeface/fonts/Roboto/Roboto-Bold.ttf")!,
      subFamily: "Bold",
      weight: .bold,
      style: .normal,
    ),
    Font(
      uri: URL(string: "https://cdn.img.ly/assets/v4/ly.img.typeface/fonts/Roboto/Roboto-BoldItalic.ttf")!,
      subFamily: "Bold Italic",
      weight: .bold,
      style: .italic,
    ),
    Font(
      uri: URL(string: "https://cdn.img.ly/assets/v4/ly.img.typeface/fonts/Roboto/Roboto-Italic.ttf")!,
      subFamily: "Italic",
      weight: .normal,
      style: .italic,
    ),
    Font(
      uri: URL(string: "https://cdn.img.ly/assets/v4/ly.img.typeface/fonts/Roboto/Roboto-Regular.ttf")!,
      subFamily: "Regular",
      weight: .normal,
      style: .normal,
    ),
  ],
)
try engine.block.setFont(text, fontFileURL: typeface.fonts[3].uri, typeface: typeface)
```

If the formatting, e.g., bold or italic, of the text should be kept, you have to call the `fun setTypeface(block: DesignBlock, fontFileUri: Uri, typeface: Typeface)` API and provide it with both the uri of the font file to be used and the complete typeface definition of the corresponding typeface. The font file should be a fallback font, e.g., `Regular`, from the same typeface. The actual font that matches the formatting is chosen automatically with the current formatting retained as much as possible. If the new typeface does not support the current formatting, the formatting changes to a reasonable close one, e.g. thin might change to light, bold to normal, and/or italic to non-italic. If no reasonable font can be found, the fallback font is used.

```swift highlight-setTypeface
try engine.block.setTypeface(text, typeface: typeface, in: "Alex".range(of: "lex")!)
try engine.block.setTypeface(text, typeface: typeface)
```

You can query the currently used typeface definition of a text block by calling the `getTypeface(_ id: DesignBlockID) throws -> Typeface` API. It is important to note that new text blocks don't have any explicit typeface set until you call the `setFont` API. In this case, the `getTypeface` API will throw an error.

```swift highlight-getTypeface
let currentDefaultTypeface = try engine.block.getTypeface(text)
```

## Font Weights and Styles

Text blocks can have multiple ranges with different weights and styles.

In order to toggle the text of a text block between the normal and bold font weights, first call the `canToggleBoldFont(_ id: DesignBlockID, in subrange: Range<String.Index>? = nil) throws -> Bool` API to check whether such an edit is possible and if so, call the `toggleBoldFont(_ id: DesignBlockID, in subrange: Range<String.Index>? = nil) throws` API to change the weight.

```swift highlight-toggleBold
if try engine.block.canToggleBoldFont(text) {
  try engine.block.toggleBoldFont(text)
}
if try engine.block.canToggleBoldFont(text, in: "Alex".range(of: "lex")!) {
  try engine.block.toggleBoldFont(text, in: "Alex".range(of: "lex")!)
}
```

In order to toggle the text of a text block between the normal and italic font styles, first call the `canToggleItalicFont(_ id: DesignBlockID, in subrange: Range<String.Index>? = nil) throws -> Bool` API to check whether such an edit is possible and if so, call the `toggleItalicFont(_ id: DesignBlockID, in subrange: Range<String.Index>? = nil) throws` API to change the style.

```swift highlight-toggleItalic
if try engine.block.canToggleItalicFont(text) {
  try engine.block.toggleItalicFont(text)
}
if try engine.block.canToggleItalicFont(text, in: "Alex".range(of: "lex")!) {
  try engine.block.toggleItalicFont(text, in: "Alex".range(of: "lex")!)
}
```

In order to change the font weight or style, the typeface definition of the text block must include a font definition that corresponds to the requested font weight and style combination. For example, if the text block currently uses a bold font and you want to toggle the font style to italic - such as in the example code - the typeface must contain a font that is both bold and italic.

The `func setTextFontWeight(_ id: DesignBlockID, fontWeight: FontWeight, in subrange: Range<String.Index>? = nil) throws` API sets a font weight in the requested range, similar to the `setTextColor` API described above.

```swift highlight-setTextFontWeight
try engine.block.setTextFontWeight(text, fontWeight: .bold)
```

The `func getTextFontWeights(_ id: DesignBlockID, in subrange: Range<String.Index>? = nil) throws -> [FontWeight]` API returns an ordered list of unique font weights in the requested range, similar to the `getTextColors` API described above. For this example text, the result will be `[.bold]`.

```swift highlight-getTextFontWeights
let fontWeights = try engine.block.getTextFontWeights(text)
```

The `func setTextFontStyle(_ id: DesignBlockID, fontStyle: FontStyle, in subrange: Range<String.Index>? = nil) throws` API sets a font style in the requested range.

```swift highlight-setTextFontStyle
try engine.block.setTextFontStyle(text, fontStyle: .italic)
```

The `func getTextFontStyles(_ id: DesignBlockID, in subrange: Range<String.Index>? = nil) throws -> [FontStyle]` API returns an ordered list of unique font styles in the requested range. For this example text, the result will be `[.italic]`.

```swift highlight-getTextFontStyles
let fontStyles = try engine.block.getTextFontStyles(text)
```

## Full Code

Here's the full code:

```swift
import Foundation
import IMGLYEngine

@MainActor
func textProperties(engine: Engine) async throws {
  let scene = try engine.scene.create()
  let text = try engine.block.create(.text)
  try engine.block.appendChild(to: scene, child: text)
  try engine.block.setWidthMode(text, mode: .auto)
  try engine.block.setHeightMode(text, mode: .auto)

  try engine.block.replaceText(text, text: "Hello World")
  // Add a "!" at the end of the text
  try engine.block.replaceText(text, text: "!", in: "Hello World".endIndex ..< "Hello World".endIndex)
  // Replace "World" with "Alex"
  try engine.block.replaceText(text, text: "Alex", in: "Hello World".range(of: "World")!)

  try await engine.scene.zoom(to: text, paddingLeft: 100, paddingTop: 100, paddingRight: 100, paddingBottom: 100)

  // Remove the "Hello "
  try engine.block.removeText(text, from: "Hello Alex".range(of: "Hello ")!)

  try engine.block.setTextColor(text, color: .rgba(r: 1, g: 1, b: 0))
  try engine.block.setTextColor(text, color: .rgba(r: 0, g: 0, b: 0), in: "Alex".range(of: "lex")!)
  let allColors = try engine.block.getTextColors(text)
  let colorsInRange = try engine.block.getTextColors(text, in: "Alex".range(of: "lex")!)

  try engine.block.setBool(text, property: "backgroundColor/enabled", value: true)

  try engine.block.getColor(text, property: "backgroundColor/color") as Color
  try engine.block.setColor(text, property: "backgroundColor/color", color: .rgba(r: 0.0, g: 0.0, b: 1.0, a: 1.0))

  try engine.block.setFloat(text, property: "backgroundColor/paddingLeft", value: 1)
  try engine.block.setFloat(text, property: "backgroundColor/paddingTop", value: 2)
  try engine.block.setFloat(text, property: "backgroundColor/paddingRight", value: 3)
  try engine.block.setFloat(text, property: "backgroundColor/paddingBottom", value: 4)

  try engine.block.setFloat(text, property: "backgroundColor/cornerRadius", value: 4)

  let animation = try engine.block.createAnimation(AnimationType.slide)
  try engine.block.setEnum(animation, property: "textAnimationWritingStyle", value: "Block")

  try engine.block.setInAnimation(text, animation: animation)
  try engine.block.setOutAnimation(text, animation: animation)

  try engine.block.setTextCase(text, textCase: .titlecase)

  let textCases = try engine.block.getTextCases(text)

  let typeface = Typeface(
    name: "Roboto",
    fonts: [
      Font(
        uri: URL(string: "https://cdn.img.ly/assets/v4/ly.img.typeface/fonts/Roboto/Roboto-Bold.ttf")!,
        subFamily: "Bold",
        weight: .bold,
        style: .normal
      ),
      Font(
        uri: URL(string: "https://cdn.img.ly/assets/v4/ly.img.typeface/fonts/Roboto/Roboto-BoldItalic.ttf")!,
        subFamily: "Bold Italic",
        weight: .bold,
        style: .italic
      ),
      Font(
        uri: URL(string: "https://cdn.img.ly/assets/v4/ly.img.typeface/fonts/Roboto/Roboto-Italic.ttf")!,
        subFamily: "Italic",
        weight: .normal,
        style: .italic
      ),
      Font(
        uri: URL(string: "https://cdn.img.ly/assets/v4/ly.img.typeface/fonts/Roboto/Roboto-Regular.ttf")!,
        subFamily: "Regular",
        weight: .normal,
        style: .normal
      ),
    ]
  )
  try engine.block.setFont(text, fontFileURL: typeface.fonts[3].uri, typeface: typeface)

  try engine.block.setTypeface(text, typeface: typeface, in: "Alex".range(of: "lex")!)
  try engine.block.setTypeface(text, typeface: typeface)

  let currentDefaultTypeface = try engine.block.getTypeface(text)

  let currentTypefaces = try engine.block.getTypefaces(text)
  let currentTypefacesOfRange = try engine.block.getTypefaces(text, in: "Alex".range(of: "lex")!)

  if try engine.block.canToggleBoldFont(text) {
    try engine.block.toggleBoldFont(text)
  }
  if try engine.block.canToggleBoldFont(text, in: "Alex".range(of: "lex")!) {
    try engine.block.toggleBoldFont(text, in: "Alex".range(of: "lex")!)
  }

  if try engine.block.canToggleItalicFont(text) {
    try engine.block.toggleItalicFont(text)
  }
  if try engine.block.canToggleItalicFont(text, in: "Alex".range(of: "lex")!) {
    try engine.block.toggleItalicFont(text, in: "Alex".range(of: "lex")!)
  }

  let fontWeights = try engine.block.getTextFontWeights(text)

  try engine.block.setTextFontStyle(text, fontStyle: .italic)

  let fontStyles = try engine.block.getTextFontStyles(text)
}
```



---

## More Resources

- **[macOS Documentation Index](https://img.ly/docs/cesdk/macos.md)** - Browse all macOS documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/macos/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/macos/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
