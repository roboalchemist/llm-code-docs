# Source: https://img.ly/docs/cesdk/ios/colors/for-print/spot-c3a150/

---
title: "Spot Colors"
description: "Learn how to define spot colors and set their color approximation in the CreativeEditor SDK."
platform: ios
url: "https://img.ly/docs/cesdk/ios/colors/for-print/spot-c3a150/"
---

> This is one page of the CE.SDK iOS documentation. For a complete overview, see the [iOS Documentation Index](https://img.ly/docs/cesdk/ios.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/ios/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/ios/guides-8d8b00/) > [Colors](https://img.ly/docs/cesdk/ios/colors-a9b79c/) > [For Print](https://img.ly/docs/cesdk/ios/colors/for-print-59bc05/) > [Spot Colors](https://img.ly/docs/cesdk/ios/colors/for-print/spot-c3a150/)

---

```swift reference-only
// Create a spot color with an RGB color approximation.
engine.editor.setSpotColor(name: "Red", r: 1.0, g: 0.0, b: 0.0)

// Create a spot color with a CMYK color approximation.
// Add a CMYK approximation to the already defined 'Red' spot color.
engine.editor.setSpotColor(name: "Yellow", c: 0.0, m: 0.0, y: 1.0, k: 0.0)
engine.editor.setSpotColor(name: "Red", c: 0.0, m: 1.0, y: 1.0, k: 0.0)

// List all defined spot colors.
engine.editor.findAllSpotColors() // ["Red", "Yellow"]

// Retrieve the RGB color approximation for a defined color.
// The alpha value will always be 1.0.
let rgbaSpotRed: RGBA = engine.editor.getSpotColor(name: "Red")

// Retrieve the CMYK color approximation for a defined color.
let cmykSpotRed: CMYK = engine.editor.getSpotColor(name: "Red")

// Retrieving the approximation of an undefined spot color returns magenta.
let cmykSpotUnknown: CMYK = engine.editor.getSpotColor(name: "Unknown") // Returns CMYK values for magenta.

// Removes a spot color from the list of defined spot colors.
try engine.editor.removeSpotColor(name: "Red")
```

In this example, we will show you how to use the [CreativeEditor SDK](https://img.ly/creative-sdk)'s CreativeEngine to manage spot colors in the `editor` API.

## Functions

```swift
public func findAllSpotColors() -> [String]
```

Queries the names of currently set spot colors previously set with `setSpotColor`.

- Returns: The names of set spot colors.

```swift
public func getSpotColor(name: String) -> RGBA
```

Queries the RGB representation set for a spot color.
If the value of the queried spot color has not been set yet, returns the default RGB representation (of magenta).
The alpha value is always 1.0.

- `name:`: The name of a spot color.
- Returns: A result holding the four color components.

```swift
public func getSpotColor(name: String) -> CMYK
```

Queries the CMYK representation set for a spot color.
If the value of the queried spot color has not been set yet, returns the default CMYK representation (of magenta).

- `name:`: The name of a spot color.
- Returns: A result holding the four color components.

```swift
public func setSpotColor(name: String, r: Float, g: Float, b: Float)
```

Sets the RGB representation of a spot color.
Use this function to both create a new spot color or update an existing spot color.

- `name`: The name of a spot color.
- `r`: The red color component in the range of 0 to 1.
- `g`: The green color component in the range of 0 to 1.
- `b`: The blue color component in the range of 0 to 1.

```swift
public func setSpotColor(name: String, c: Float, m: Float, y: Float, k: Float)
```

Sets the CMYK representation of a spot color.
Use this function to both create a new spot color or update an existing spot color.

- `name`: The name of a spot color.
- `c`: The cyan color component in the range of 0 to 1.
- `m`: The magenta color component in the range of 0 to 1.
- `y`: The yellow color component in the range of 0 to 1.
- `k`: The key color component in the range of 0 to 1.

```swift
public func removeSpotColor(name: String) throws
```

Removes a spot color from the list of set spot colors.

- `name:`: The name of a spot color.

## Full Code

Here's the full code:

```swift
// Create a spot color with an RGB color approximation.
engine.editor.setSpotColor(name: "Red", r: 1.0, g: 0.0, b: 0.0)

// Create a spot color with a CMYK color approximation.
// Add a CMYK approximation to the already defined 'Red' spot color.
engine.editor.setSpotColor(name: "Yellow", c: 0.0, m: 0.0, y: 1.0, k: 0.0)
engine.editor.setSpotColor(name: "Red", c: 0.0, m: 1.0, y: 1.0, k: 0.0)

// List all defined spot colors.
engine.editor.findAllSpotColors() // ["Red", "Yellow"]

// Retrieve the RGB color approximation for a defined color.
// The alpha value will always be 1.0.
let rgbaSpotRed: RGBA = engine.editor.getSpotColor(name: "Red")

// Retrieve the CMYK color approximation for a defined color.
let cmykSpotRed: CMYK = engine.editor.getSpotColor(name: "Red")

// Retrieving the approximation of an undefined spot color returns magenta.
let cmykSpotUnknown: CMYK = engine.editor.getSpotColor(name: "Unknown") // Returns CMYK values for magenta.

// Removes a spot color from the list of defined spot colors.
try engine.editor.removeSpotColor(name: "Red")
```



---

## More Resources

- **[iOS Documentation Index](https://img.ly/docs/cesdk/ios.md)** - Browse all iOS documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/ios/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/ios/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
