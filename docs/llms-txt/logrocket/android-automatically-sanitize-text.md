# Source: https://docs.logrocket.com/reference/android-automatically-sanitize-text.md

# Automatically Sanitize Text

To configure the Android SDK to automatically redact all text use the configuration below. Any rendered text will be replaced with black bars where the text would have appeared.

Movement and clicks over redacted elements will be captured, but not the selector or text in the redacted element.

```text textSanitizer
options.setTextSanitizer(SDK.SanitizerType.EXCLUDED)
```

Example Screenshot

![346](https://files.readme.io/3d3b87a-Screen_Shot_2023-01-13_at_1.40.28_PM.png "Screen Shot 2023-01-13 at 1.40.28 PM.png")