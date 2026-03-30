# Source: https://img.ly/docs/cesdk/macos/colors/conversion-bcd82b/

---
title: "Color Conversion"
description: "Convert between RGB, CMYK, and other color formats based on your project’s output requirements."
platform: macos
url: "https://img.ly/docs/cesdk/macos/colors/conversion-bcd82b/"
---

> This is one page of the CE.SDK macOS documentation. For a complete overview, see the [macOS Documentation Index](https://img.ly/docs/cesdk/macos.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/macos/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/macos/guides-8d8b00/) > [Colors](https://img.ly/docs/cesdk/macos/colors-a9b79c/) > [Color Conversion](https://img.ly/docs/cesdk/macos/colors/conversion-bcd82b/)

---

To ease implementing advanced color interfaces, you may rely on the engine to perform color conversions.

Converts a color to the given color space.

- `color`: The color to convert.
- `colorSpace`: The color space to convert to.
- Returns The converted color.

```swift
// Convert a color
let rgbaGreen = Color(cgColor: CGColor(red: 0, green: 1, blue: 0, alpha: 1))!
let cmykGreen = try engine.editor.convertColorToColorSpace(color: rgbaGreen, colorSpace: .cmyk)
```



---

## More Resources

- **[macOS Documentation Index](https://img.ly/docs/cesdk/macos.md)** - Browse all macOS documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/macos/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/macos/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
