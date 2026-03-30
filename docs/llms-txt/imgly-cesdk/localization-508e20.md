# Source: https://img.ly/docs/cesdk/android/user-interface/localization-508e20/

---
title: "Localization"
description: "Learn how to configure and manage multiple languages in the CE.SDK editor using the built-in internationalization API."
platform: android
url: "https://img.ly/docs/cesdk/android/user-interface/localization-508e20/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [User Interface](https://img.ly/docs/cesdk/android/user-interface-5a089a/) > [Localization](https://img.ly/docs/cesdk/android/user-interface/localization-508e20/)

---

The CE.SDK editor currently supports English and German languages on Android, however it provides convenient API to replace the values of existing localization keys or add support for more languages.

All the editor keys are located [here](https://github.com/imgly/cesdk-android/blob/v$UBQ_VERSION$/sources/editor-core/src/main/res/values/strings.xml) and they all follow strict naming convention to make locating keys simple and self-explanatory.
For instance, the gallery button in the dock can be found via `ly_img_editor_dock_button_gallery` key, or the title in the format text sheet can be found via `ly_img_editor_sheet_format_text_title` key.

### Replacing existing keys

In order to replace any of the existing editor keys, find the key of the desired text, copy the key to `res/values/strings.xml` file of your app module and replace with the desired value.

### Supporting new languages

In order to add support for a language that is not supported by the CE.SDK editor, copy the content of the English localization [file](https://github.com/imgly/cesdk-android/blob/v$UBQ_VERSION$/sources/editor-core/src/main/res/values/strings.xml) to `res/values-{desired-language-code}/strings.xml` file and replace the values with desired translations.



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
