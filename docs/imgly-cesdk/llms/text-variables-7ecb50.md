# Source: https://img.ly/docs/cesdk/android/create-templates/add-dynamic-content/text-variables-7ecb50/

---
title: "Text Variables"
description: "Define dynamic text elements that can be populated with custom values during design generation."
platform: android
url: "https://img.ly/docs/cesdk/android/create-templates/add-dynamic-content/text-variables-7ecb50/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [Create and Use Templates](https://img.ly/docs/cesdk/android/create-templates-3aef79/) > [Insert Dynamic Content](https://img.ly/docs/cesdk/android/create-templates/add-dynamic-content-53fad7/) > [Text Variables](https://img.ly/docs/cesdk/android/create-templates/add-dynamic-content/text-variables-7ecb50/)

---

```kotlin reference-only
// Query all variables
val variableNames = engine.variable.findAll()

// Set, get and remove a variable
engine.variable.set(key = "name", value = "Chris")
val name = engine.variable.get(key = "name") // Chris
engine.variable.remove(key = "name")

val block = engine.block.create(DesignBlockType.Graphic)
engine.block.referencesAnyVariables(block)
```

In this example, we will show you how to use the [CreativeEditor SDK](https://img.ly/products/creative-sdk)'s CreativeEngine to modify variables through the `variable` API. The `variable` API lets you set or get the contents of variables that exist in your scene.

## Functions

```kotlin
fun findAll(): List<String>
```

Get all text variables currently stored in the engine.

- Returns a list of variable names.

```kotlin
fun set(
    key: String,
    value: String,
)
```

Set a text variable.

- `key`: the variable's key.

- `value`: the text to replace the variable with.

```kotlin
fun get(key: String): String
```

Get a text variable.

- `key`: the variable's key.

- Returns the text value of the variable.

```kotlin
fun remove(key: String)
```

Destroy a text variable.

- `key`: the variable's key.

```kotlin
fun referencesAnyVariables(block: DesignBlock): Boolean
```

Checks whether the given block references any variables. Doesn't check the block's children.

- `block`: the block to query.

- Returns true if the block references variables, false otherwise.

## Localizing Variable Keys (CE.SDK only)

You can show localized labels for the registered variables to your users by
adding a corresponding label property to the object stored at
`i18n.<language>.variables.<key>.label` in the configuration.
Otherwise, the name used in `variable.setString()` will be shown.

![](./assets/variables-dark.png)

## Full Code

Here's the full code:

```kotlin
// Query all variables
val variableNames = engine.variable.findAll()

// Set, get and remove a variable
engine.variable.set(key = "name", value = "Chris")
val name = engine.variable.get(key = "name") // Chris
engine.variable.remove(key = "name")

val block = engine.block.create(DesignBlockType.Graphic)
engine.block.referencesAnyVariables(block)
```



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
