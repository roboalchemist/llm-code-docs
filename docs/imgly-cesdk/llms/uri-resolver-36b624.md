# Source: https://img.ly/docs/cesdk/android/open-the-editor/uri-resolver-36b624/

---
title: "URI Resolver"
description: "Customize how asset URIs are resolved and loaded into the editor for full control over file handling."
platform: android
url: "https://img.ly/docs/cesdk/android/open-the-editor/uri-resolver-36b624/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [Open the Editor](https://img.ly/docs/cesdk/android/open-the-editor-23a1db/) > [URI Resolver](https://img.ly/docs/cesdk/android/open-the-editor/uri-resolver-36b624/)

---

```kotlin file=@cesdk_android_examples/engine-guides-uri-resolver/UriResolver.kt reference-only
import android.net.Uri
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import ly.img.engine.Engine

fun uriResolver(
    license: String?, // pass null or empty for evaluation mode with watermark
    userId: String,
) = CoroutineScope(Dispatchers.Main).launch {
    val engine = Engine.getInstance(id = "ly.img.engine.example")
    engine.start(license = license, userId = userId)
    engine.bindOffscreen(width = 1080, height = 1920)

    // This will return uri to "banana.jpg" asset file
    engine.editor.getAbsoluteUri(uri = Uri.parse("banana.jpg"))
    // This will return uri to remote resource "https://example.com/orange.png"
    engine.editor.getAbsoluteUri(uri = Uri.parse("https://example.com/orange.png"))

    // Replace all .jpg files with the IMG.LY logo!
    engine.editor.setUriResolver {
        if (it.toString().endsWith(".jpg")) {
            Uri.parse("https://img.ly/static/ubq_samples/imgly_logo.jpg")
        } else {
            engine.editor.defaultUriResolver(it)
        }
    }

    // The custom resolver will return a path to the IMG.LY logo because the given path ends with ".jpg".
    // This applies regardless if the given path is relative or absolute.
    engine.editor.getAbsoluteUri(uri = Uri.parse("banana.jpg"))

    // The custom resolver will not modify this path because it ends with ".png".
    engine.editor.getAbsoluteUri(uri = Uri.parse("https://example.com/orange.png"))

    // Because a custom resolver is set, relative paths that the resolver does not transform remain unmodified!
    engine.editor.getAbsoluteUri(uri = Uri.parse("/orange.png"))

    // Removes the previously set resolver.
    engine.editor.setUriResolver(null)

    // Since we've removed the custom resolver, this will return
    // Uri.Asset("banana.jpg") like before.
    engine.editor.getAbsoluteUri(uri = Uri.parse("banana.jpg"))

    engine.editor.setUriResolver { uri ->
        val path = uri.path
        if (uri.host == "localhost" && path != null && path.startsWith("/scenes") && !path.endsWith(".scene")) {
            // Apply custom logic here, e.g. redirect to a different server
        }
        engine.editor.defaultUriResolver(uri)
    }

    engine.stop()
}
```

CE.SDK gives you full control over how Uris should be resolved. To register a custom resolver, use `setUriResolver` and pass in a function implementing your resolution logic.
If a custom resolver is set, any Uri (both relative and absolute) requested by the engine is passed through the resolver.
The Uri your logic returns is then fetched by the engine.
The resolved Uri is just used for the current request and not stored.
If, and only if, no custom resolver is set, the engine performs the default behaviour: absolute uri objects are unchanged and relative objects are turned into android asset Uris.

> **Note:** **Warning** Your custom Uri resolver must return an absolute Uri.

We can preview the effects of setting a custom Uri resolver with the function `fun getAbsoluteUri(uri: Uri): Uri`.

Before setting a custom Uri resolver, the default behavior is as before: absolute Uri is unchanged and relative is turned into android asset Uri.

```kotlin highlight-get-absolute-base-path
// This will return uri to "banana.jpg" asset file
engine.editor.getAbsoluteUri(uri = Uri.parse("banana.jpg"))
// This will return uri to remote resource "https://example.com/orange.png"
engine.editor.getAbsoluteUri(uri = Uri.parse("https://example.com/orange.png"))
```

To show that the resolver can be fairly free-form, in this example we register a custom Uri resolver that replaces all `.jpg` images with our company logo.

Note: you can still access the default Uri resolver by calling `fun defaultUriResolver(uri: Uri): Uri`.

```kotlin highlight-resolver
// Replace all .jpg files with the IMG.LY logo!
engine.editor.setUriResolver {
    if (it.toString().endsWith(".jpg")) {
        Uri.parse("https://img.ly/static/ubq_samples/imgly_logo.jpg")
    } else {
        engine.editor.defaultUriResolver(it)
    }
}
```

Given the same uri as earlier, the custom resolver transforms it as specified.
Note that after a custom resolver is set, uris that the resolver does not transform remain unmodified thanks to `defaultUriResolver`.

```kotlin highlight-get-absolute-custom
    // The custom resolver will return a path to the IMG.LY logo because the given path ends with ".jpg".
    // This applies regardless if the given path is relative or absolute.
    engine.editor.getAbsoluteUri(uri = Uri.parse("banana.jpg"))

    // The custom resolver will not modify this path because it ends with ".png".
    engine.editor.getAbsoluteUri(uri = Uri.parse("https://example.com/orange.png"))

    // Because a custom resolver is set, relative paths that the resolver does not transform remain unmodified!
    engine.editor.getAbsoluteUri(uri = Uri.parse("/orange.png"))
```

To remove a previously set custom resolver, call the function with a `null` value.
The Uri resolution is now back to the default behavior.

```kotlin highlight-remove-resolver
    // Removes the previously set resolver.
    engine.editor.setUriResolver(null)

    // Since we've removed the custom resolver, this will return
    // Uri.Asset("banana.jpg") like before.
    engine.editor.getAbsoluteUri(uri = Uri.parse("banana.jpg"))
```

## Full Code

Here's the full code:

```kotlin
import android.net.Uri
import kotlinx.coroutines.*
import ly.img.engine.*

fun uriResolver(
    license: String,
    userId: String,
) = CoroutineScope(Dispatchers.Main).launch {
    val engine = Engine.getInstance(id = "ly.img.engine.example")
    engine.start(license = license, userId = userId)
    engine.bindOffscreen(width = 100, height = 100)

    // This will return uri to "banana.jpg" asset file
    engine.editor.getAbsoluteUri(uri = Uri.parse("banana.jpg"))
    // This will return uri to remote resource "https://example.com/orange.png"
    engine.editor.getAbsoluteUri(uri = Uri.parse("https://example.com/orange.png"))

    // Replace all .jpg files with the IMG.LY logo!
    engine.editor.setUriResolver {
        if (it.toString().endsWith(".jpg")) {
            Uri.parse("https://img.ly/static/ubq_samples/imgly_logo.jpg")
        } else {
            engine.editor.defaultUriResolver(it)
        }
    }

    // The custom resolver will return a path to the IMG.LY logo because the given path ends with ".jpg".
    // This applies regardless if the given path is relative or absolute.
    engine.editor.getAbsoluteUri(uri = Uri.parse("banana.jpg"))

    // The custom resolver will not modify this path because it ends with ".png".
    engine.editor.getAbsoluteUri(uri = Uri.parse("https://example.com/orange.png"))

    // Because a custom resolver is set, relative paths that the resolver does not transform remain unmodified!
    engine.editor.getAbsoluteUri(uri = Uri.parse("/orange.png"))

    // Removes the previously set resolver.
    engine.editor.setUriResolver(null)

    // Since we've removed the custom resolver, this will return
    // Uri.Asset("banana.jpg") like before.
    engine.editor.getAbsoluteUri(uri = Uri.parse("banana.jpg"))

    engine.editor.setUriResolver { uri ->
        val path = uri.path
        if (uri.host == "localhost" && path != null && path.startsWith("/scenes") && !path.endsWith(".scene")) {
            // Apply custom logic here, e.g. redirect to a different server
        }
        engine.editor.defaultUriResolver(uri)
    }

    engine.stop()
}
```



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
