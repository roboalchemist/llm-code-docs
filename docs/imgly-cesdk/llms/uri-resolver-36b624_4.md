# Source: https://img.ly/docs/cesdk/ios/open-the-editor/uri-resolver-36b624/

---
title: "URI Resolver"
description: "Customize how asset URIs are resolved and loaded into the editor for full control over file handling."
platform: ios
url: "https://img.ly/docs/cesdk/ios/open-the-editor/uri-resolver-36b624/"
---

> This is one page of the CE.SDK iOS documentation. For a complete overview, see the [iOS Documentation Index](https://img.ly/docs/cesdk/ios.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/ios/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/ios/guides-8d8b00/) > [Open the Editor](https://img.ly/docs/cesdk/ios/open-the-editor-23a1db/) > [URI Resolver](https://img.ly/docs/cesdk/ios/open-the-editor/uri-resolver-36b624/)

---

```swift file=@cesdk_swift_examples/engine-guides-uri-resolver/URIResolver.swift reference-only
import Foundation
import IMGLYEngine

@MainActor
func uriResolver(engine: Engine) async throws {
  // This will return "https://cdn.img.ly/packages/imgly/cesdk-js/1.70.0/assets/banana.jpg"
  try engine.editor.getAbsoluteURI(relativePath: "/banana.jpg")

  // Replace all .jpg files with the IMG.LY logo!
  try engine.editor.setURIResolver { uri in
    if uri.hasSuffix(".jpg") {
      return URL(string: "https://img.ly/static/ubq_samples/imgly_logo.jpg")!
    }
    // Make use of the default URI resolution behavior.
    return URL(string: engine.editor.defaultURIResolver(relativePath: uri))!
  }

  // The custom resolver will return a path to the IMG.LY logo because the given path ends with ".jpg".
  // This applies regardless if the given path is relative or absolute.
  try engine.editor.getAbsoluteURI(relativePath: "/banana.jpg")

  // The custom resolver will not modify this path because it ends with ".png".
  try engine.editor.getAbsoluteURI(relativePath: "https://example.com/orange.png")

  // Because a custom resolver is set, relative paths that the resolver does not transform remain unmodified!
  try engine.editor.getAbsoluteURI(relativePath: "/orange.png")

  // Removes the previously set resolver.
  try engine.editor.setURIResolver(nil)

  // Since we"ve removed the custom resolver, this will return
  // "https://cdn.img.ly/packages/imgly/cesdk-js/1.70.0/assets/banana.jpg" like before.
  try engine.editor.getAbsoluteURI(relativePath: "/banana.jpg")
}
```

CE.SDK gives you full control over how URIs should be resolved. To register a custom resolver, use `setURIResolver` and pass in a function implementing your resolution logic.
If a custom resolver is set, any URI requested by the engine is passed through the resolver.
The URI your logic returns is then fetched by the engine.
The resolved URI is just used for the current request and not stored.
If, and only if, no custom resolver is set, the engine performs the default behaviour: absolute paths are unchanged and relative paths are prepended with the value of the `basePath` setting.

> **Note:** **Warning** Your custom URI resolver must return an URL.

We can preview the effects of setting a custom URI resolver with the function `func getAbsoluteURI(relativePath: String) throws -> String`.

Before setting a custom URI resolver, the default behavior is as before and the given relative path will be prepended with the contents of `basePath`.

```swift highlight-get-absolute-base-path
// This will return "https://cdn.img.ly/packages/imgly/cesdk-js/1.70.0/assets/banana.jpg"
try engine.editor.getAbsoluteURI(relativePath: "/banana.jpg")
```

To show that the resolver can be fairly free-form, in this example we register a custom URI resolver that replaces all `.jpg` images with our company logo.
The resolved URI are expected to be absolute.

Note: you can still access the default URI resolver by calling `func defaultURIResolver(relativePath: String) -> String`.

```swift highlight-resolver
// Replace all .jpg files with the IMG.LY logo!
try engine.editor.setURIResolver { uri in
  if uri.hasSuffix(".jpg") {
    return URL(string: "https://img.ly/static/ubq_samples/imgly_logo.jpg")!
  }
  // Make use of the default URI resolution behavior.
  return URL(string: engine.editor.defaultURIResolver(relativePath: uri))!
}
```

Given the same path as earlier, the custom resolver transforms it as specified.
Note that after a custom resolver is set, relative paths that the resolver does not transform remain unmodified.

```swift highlight-get-absolute-custom
  // The custom resolver will return a path to the IMG.LY logo because the given path ends with ".jpg".
  // This applies regardless if the given path is relative or absolute.
  try engine.editor.getAbsoluteURI(relativePath: "/banana.jpg")

  // The custom resolver will not modify this path because it ends with ".png".
  try engine.editor.getAbsoluteURI(relativePath: "https://example.com/orange.png")

  // Because a custom resolver is set, relative paths that the resolver does not transform remain unmodified!
  try engine.editor.getAbsoluteURI(relativePath: "/orange.png")
```

To remove a previously set custom resolver, call the function with a `nil` value.
The URI resolution is now back to the default behavior.

```swift highlight-remove-resolver
  // Removes the previously set resolver.
  try engine.editor.setURIResolver(nil)

  // Since we"ve removed the custom resolver, this will return
  // "https://cdn.img.ly/packages/imgly/cesdk-js/1.70.0/assets/banana.jpg" like before.
  try engine.editor.getAbsoluteURI(relativePath: "/banana.jpg")
```

## Full Code

Here's the full code:

```swift
import Foundation
import IMGLYEngine

@MainActor
func uriResolver(engine: Engine) async throws {
  // This will return "https://cdn.img.ly/packages/imgly/cesdk-js/$UBQ_VERSION$/assets/banana.jpg"
  try engine.editor.getAbsoluteURI(relativePath: "/banana.jpg")

  // Replace all .jpg files with the IMG.LY logo!
  try engine.editor.setURIResolver { uri in
    if uri.hasSuffix(".jpg") {
      return URL(string: "https://img.ly/static/ubq_samples/imgly_logo.jpg")!
    }
    // Make use of the default URI resolution behavior.
    return URL(string: engine.editor.defaultURIResolver(relativePath: uri))!
  }

  // The custom resolver will return a path to the IMG.LY logo because the given path ends with ".jpg".
  // This applies regardless if the given path is relative or absolute.
  try engine.editor.getAbsoluteURI(relativePath: "/banana.jpg")

  // The custom resolver will not modify this path because it ends with ".png".
  try engine.editor.getAbsoluteURI(relativePath: "https://example.com/orange.png")

  // Because a custom resolver is set, relative paths that the resolver does not transform remain unmodified!
  try engine.editor.getAbsoluteURI(relativePath: "/orange.png")

  // Removes the previously set resolver.
  try engine.editor.setURIResolver(nil)

  // Since we"ve removed the custom resolver, this will return
  // "https://cdn.img.ly/packages/imgly/cesdk-js/$UBQ_VERSION$/assets/banana.jpg" like before.
  try engine.editor.getAbsoluteURI(relativePath: "/banana.jpg")
}
```



---

## More Resources

- **[iOS Documentation Index](https://img.ly/docs/cesdk/ios.md)** - Browse all iOS documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/ios/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/ios/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
