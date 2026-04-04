# Source: https://docs.buildnatively.com/guides/integration/clipboard.md

# Clipboard

* [Bubble.io Plugin](#bubble.io-plugin)
* [JavaScript SDK](#javascript-sdk)

## 🧋 Bubble.io Plugin

### \[Element] Natively - Clipboard

#### Events:

* Clipboard value received

#### States:

* **Latest clipboard value** - text

#### Actions:

* Copy text to clipboard
* Get text from clipboard

## 🛠 JavaScript SDK

### Device App Info

{% code overflow="wrap" lineNumbers="true" %}

```javascript
// Check if native app
const clipboard = new NativelyClipboard();
clipboard.copy(text);
const callback = function (resp) {
    console.log(resp.text);
}
clipboard.paste(callback);
```

{% endcode %}
