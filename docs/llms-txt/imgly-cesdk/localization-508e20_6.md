# Source: https://img.ly/docs/cesdk/mac-catalyst/user-interface/localization-508e20/

---
title: "Localization"
description: "Learn how to configure and manage multiple languages in the CE.SDK editor using the built-in internationalization API."
platform: mac-catalyst
url: "https://img.ly/docs/cesdk/mac-catalyst/user-interface/localization-508e20/"
---

> This is one page of the CE.SDK Mac Catalyst documentation. For a complete overview, see the [Mac Catalyst Documentation Index](https://img.ly/docs/cesdk/mac-catalyst.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/mac-catalyst/llms-full.txt).

---

The CE.SDK editor currently supports English and German languages on iOS, however it provides convenient API to replace the values of existing localization keys or add support for more languages.

All the editor keys are located [here](https://github.com/imgly/IMGLYUI-swift/tree/$UBQ_VERSION$/Sources/IMGLYCoreUI/IMGLYEditor.xcstrings) and they all follow strict naming convention to make locating keys simple and self-explanatory.
For instance, the photo roll button in the dock can be found via `ly_img_editor_dock_button_photo_roll` key, or the title in the format text sheet can be found via `ly_img_editor_sheet_format_text_title` key.

### Replacing existing keys

In order to replace any of the existing editor keys, find the key of the desired text, add the key to `Localizable.xcstrings` file of your app and replace with the desired value or copy the `IMGLYEditor.xcstrings` file to your app and edit it. Keys defined in `Localizable.xcstrings` take precedence over the ones defined in `IMGLYEditor.xcstrings`.

### Supporting new languages

In order to add support for a language that is not supported by the CE.SDK editor add a new language to your `Localizable.xcstrings` or `IMGLYEditor.xcstrings` file and replace the values with desired translations.

```
```



---

## More Resources

- **[Mac Catalyst Documentation Index](https://img.ly/docs/cesdk/mac-catalyst.md)** - Browse all Mac Catalyst documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/mac-catalyst/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/mac-catalyst/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
