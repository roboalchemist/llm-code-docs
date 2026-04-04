# Source: https://docs.chatling.ai/web-widget/widget-sdk.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.chatling.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Widget SDK

## Configuration

You can configure the widget during launch by setting the `window.chtlConfig` object, as shown below.

```javascript  theme={null}
window.chtlConfig = {
    // Configuration options
};
```

Below are the available properties you can set.

### `chatIconVisible`

Whether to display the chat icon (open and close buttons).

* Possible values: `true`, `false`
* Default: `true`

```javascript  theme={null}
window.chtlConfig = {
    chatIconVisible: true,
    // ... other config options
};
```

### `displayType`

The type of widget to display.

* Possible values: `floating`, `fullscreen`, `page_inline`
* Default: `floating`

```javascript  theme={null}
window.chtlConfig = {
    displayType: 'floating',
    // ... other config options
};
```

### `language`

The language of the widget in ISO 639-1 format. This will override the language set in your chatbot's appearance settings.

* Possible values: `en`, `ar`, `az`, `bg`, `bn`, `bs`, `ca`, `cs`, `da`, `de`, `el`, `en`, `es`, `et`, `fa`, `fi`, `fr`, `he`, `hi`, `hr`, `hu`, `hy`, `id`, `it`, `ja`, `ko`, `lt`, `lv`, `mn`, `ms`, `nl`, `no`, `pl`, `pt`, `pt-br`, `ro`, `ru`, `sk`, `sl`, `sq`, `sr`, `sv`, `th`, `tr`, `uk`, `ur`, `vi`, `zh-cn`, `zh-tw`

```javascript  theme={null}
window.chtlConfig = {
    language: 'en',
    // ... other config options
};
```

## Methods

Below are the SDK methods you can call to interact with the widget.

<Note>You must wait for the widget script to load before calling these methods.</Note>

### `open()`

Opens the chatbot, similar to when a user clicks the chat icon.

```javascript  theme={null}
window.Chatling.open();
```

### `minimize()`

Minimizes the chatbot, similar to when a user clicks the minimize button in the widget.

```javascript  theme={null}
window.Chatling.minimize();
```

### `hideChatIcon()`

Hides the chat icon.

```javascript  theme={null}
window.Chatling.hideChatIcon();
```

### `showChatIcon()`

Shows the chat icon.

```javascript  theme={null}
window.Chatling.showChatIcon();
```

### `setVariables()`

You can pass custom values to the chatbot at any point after it's loaded.

The method takes an object containing the variable names and values. You must make sure that the variables [have been created](/chatbot/builder/variables/how-to-create-variables) in the builder and that the names match exactly.

<Note>To pass custom data during launch, read [this guide](/web-widget/pass-custom-data#pass-custom-data-during-launch).</Note>

```javascript  theme={null}
window.Chatling.setVariables({
    "contact_name": "Rick Astley",
    "contact_email": "rick.astley@example.com",
    "age": 30
}, function(success, errorMessage) {
    if (!success) {
        // handle error
    }
});
```

### `destroy()`

Permanently removes the chatbot from the page.

```javascript  theme={null}
window.Chatling.destroy();
```
