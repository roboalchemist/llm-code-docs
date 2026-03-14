# Source: https://docs.logrocket.com/reference/react-native-automatically-sanitize-text.md

# Automatically Sanitize Text

To configure the React Native SDK to automatically redact all text use the configuration below. Any rendered text will be replaced with black bars where the text would have appeared.

```text textSanitizer
textSanitizer: 'excluded'
```