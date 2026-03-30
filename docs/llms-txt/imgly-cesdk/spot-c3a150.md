# Source: https://img.ly/docs/cesdk/android/colors/for-print/spot-c3a150/

---
title: "Spot Colors"
description: "Learn how to define spot colors and set their color approximation in the CreativeEditor SDK."
platform: android
url: "https://img.ly/docs/cesdk/android/colors/for-print/spot-c3a150/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [Colors](https://img.ly/docs/cesdk/android/colors-a9b79c/) > [For Print](https://img.ly/docs/cesdk/android/colors/for-print-59bc05/) > [Spot Colors](https://img.ly/docs/cesdk/android/colors/for-print/spot-c3a150/)

---

```kotlin reference-only
// Create a spot color with an RGB color approximation.
engine.editor.setSpotColor("Red", Color.fromRGBA(r = 1F, g = 0F, b = 0F, a = 1F))

// Create a spot color with a CMYK color approximation.
// Add a CMYK approximation to the already defined 'Red' spot color.
engine.editor.setSpotColor("Yellow", Color.fromCMYK(c = 0F, m = 0F, y = 1F, k = 0F))
engine.editor.setSpotColor("Red", Color.fromCMYK(c = 0F, m = 1F, y = 1F, k = 0F))

// List all defined spot colors.
engine.editor.findAllSpotColors() // ['Red', 'Yellow']

// Retrieve the RGB color approximation for a defined color.
// The alpha value will always be 1.0.
val rgbaSpotRed = engine.editor.getSpotColorRGB("Red")

// Retrieve the CMYK color approximation for a defined color.
val cmykSpotRed = engine.editor.getSpotColorCMYK("Red")

// Retrieving the approximation of an undefined spot color returns magenta.
val cmykSpotUnknown = engine.editor.getSpotColorCMYK("Unknown") // Returns CMYK values for magenta.

// Removes a spot color from the list of defined spot colors.
engine.editor.removeSpotColor("Red")
```

In this example, we will show you how to use the [CreativeEditor SDK](https://img.ly/creative-sdk)'s CreativeEngine to manage spot colors in the `editor` API.

## Functions

```kotlin
fun findAllSpotColors(): List<String>
```

Queries the names of currently set spot colors previously set with \`setSpotColor\`\`.

- Returns the names of set spot colors.

```kotlin
fun getSpotColorRGB(name: String): RGBAColor
```

Queries the RGB representation set for a spot color.

If the value of the queried spot color has not been set yet, returns the default RGB representation (of magenta).

The alpha value is always 1.0.

- `name`: the name of a spot color.

- Returns the RGB representation of a spot color.

```kotlin
fun getSpotColorCMYK(name: String): CMYKColor
```

Queries the CMYK representation set for a spot color.

If the value of the queried spot color has not been set yet, returns the default RGB representation (of magenta).

- `name`: the name of a spot color.

- Returns the CMYK representation of a spot color.

```kotlin
fun setSpotColor(
    name: String,
    color: RGBAColor,
)
```

Sets the RGB representation of a spot color.

Use this function to both create a new spot color or update an existing spot color.

Note: The alpha value is ignored.

- `name`: the name of a spot color.

- `color`: the RGB spot color.

```kotlin
fun setSpotColor(
    name: String,
    color: CMYKColor,
)
```

Sets the CMYK representation of a spot color.

Use this function to both create a new spot color or update an existing spot color.

- `name`: the name of a spot color.

- `color`: the CMYK spot color.

```kotlin
fun removeSpotColor(name: String)
```

Removes a spot color from the list of set spot colors.

- `name`: the name of a spot color.

## Full Code

Here's the full code:

```kotlin
// Create a spot color with an RGB color approximation.
engine.editor.setSpotColor("Red", Color.fromRGBA(r = 1F, g = 0F, b = 0F, a = 1F))

// Create a spot color with a CMYK color approximation.
// Add a CMYK approximation to the already defined 'Red' spot color.
engine.editor.setSpotColor("Yellow", Color.fromCMYK(c = 0F, m = 0F, y = 1F, k = 0F))
engine.editor.setSpotColor("Red", Color.fromCMYK(c = 0F, m = 1F, y = 1F, k = 0F))

// List all defined spot colors.
engine.editor.findAllSpotColors() // ['Red', 'Yellow']

// Retrieve the RGB color approximation for a defined color.
// The alpha value will always be 1.0.
val rgbaSpotRed = engine.editor.getSpotColorRGB("Red")

// Retrieve the CMYK color approximation for a defined color.
val cmykSpotRed = engine.editor.getSpotColorCMYK("Red")

// Retrieving the approximation of an undefined spot color returns magenta.
val cmykSpotUnknown = engine.editor.getSpotColorCMYK("Unknown") // Returns CMYK values for magenta.

// Removes a spot color from the list of defined spot colors.
engine.editor.removeSpotColor("Red")
```



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
