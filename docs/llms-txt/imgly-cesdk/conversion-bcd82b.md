# Source: https://img.ly/docs/cesdk/android/colors/conversion-bcd82b/

---
title: "Color Conversion"
description: "Convert between RGB, CMYK, and other color formats based on your project’s output requirements."
platform: android
url: "https://img.ly/docs/cesdk/android/colors/conversion-bcd82b/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [Colors](https://img.ly/docs/cesdk/android/colors-a9b79c/) > [Color Conversion](https://img.ly/docs/cesdk/android/colors/conversion-bcd82b/)

---

To ease implementing advanced color interfaces, you may rely on the engine to perform color conversions.

Converts a color to the given color space.

- `color`: The color to convert.
- `colorSpace`: The color space to convert to.
- Returns The converted color.

```kotlin
// Convert a color
val rgbaGreen = Color.fromRGBA(r = 0F, g = 1F, b = 0F, a = 0F)
val cmykGreen = engine.editor.convertColorToColorSpace(color = rgbaGreen, colorSpace = ColorSpace.CMYK)
```



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
