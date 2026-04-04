# Source: https://lynxjs.org/api/lynx-api/main-thread/main-thread-element.md

# Element

<APISummary />

`MainThread.Element` represents an element. You can access or modify the element's properties in main thread scripts.

## Instance Methods

### `Element.getAttribute()`

Get the specified attribute value of the element. If the element does not have the specified attribute, returns `undefined`.

```ts
const value = element.getAttribute(attrName);
```

### `Element.getAttributeNames()`

Get an array of the element's attribute names.

```ts
const nameArray = element.getAttributeNames();
```

### `Element.invoke()`

Asynchronously invoke the element's UI method. Returns a `Promise`. When the UI method completes successfully, the `Promise` is resolved and returns the UI method's return value. If an exception occurs during the UI method call, the `Promise` is rejected and returns an `Error` object, with its `message` describing the error in detail.

```ts
const result = await element.invoke(methodName, params?);
```

### `Element.setAttribute()`

Set the specified attribute of the element.

```ts
element.setAttribute(attrName, value);
```

### `Element.setStyleProperty()`

Set the specified style of the element. The style name must be in [kebab-case](https://developer.mozilla.org/en-US/docs/Glossary/Kebab_case).

```ts
element.setStyleProperty(styleName, value);
```

### `Element.setStyleProperties()`

Set the specified styles of the element using an object that can contain multiple "styleName: styleValue" records. The style names must be in [kebab-case](https://developer.mozilla.org/en-US/docs/Glossary/Kebab_case).

```ts
element.setStyleProperties(styleProperties);
```

### `Element.getComputedStyleProperty()`

Get the ComputedStyle for the element by key. The style name must be in [kebab-case](https://developer.mozilla.org/en-US/docs/Glossary/Kebab_case).

Refer to [Element.getComputedStyleProperty](/api/lynx-api/main-thread/element-get-computed-style.md).

```ts
const width = element.getComputedStyleProperty(styleName);
```

### `Element.querySelector()`

Find the first element within the element's child elements that matches the specified selector. Returns a `MainThread.Element`. If no matching element is found, returns `null`. For a list of supported selectors, see [selector](/api/lynx-api/selector-query/selector-query-select.md#selector).

```ts
const element = element.querySelector(selector);
```

### `Element.querySelectorAll()`

Find all elements within the element's child elements that match the specified selector. Returns an array of `MainThread.Element`. If no matching elements are found, returns an empty array. For a list of supported selectors, see [selector](/api/lynx-api/selector-query/selector-query-select.md#selector).

```ts
const elementArray = element.querySelectorAll(selector);
```

### `Element.animate()`

Start an animation on the element. Returns an `Animation` object. For more details, see [Element.animate()](/api/lynx-api/main-thread/lynx-animate-api.md).

```ts
const animation = element.animate(keyframes, options);
```

## Compatibility

**Compatibility Table**
**Query:** `lynx-api.main-thread.Element`

**Status:** 🧪 Experimental

**Platform Support**

| Platform | Version Added | Notes |
|----------|---------------|-------|
| Android | 2.14 | - |
| iOS | 2.14 | - |
| HarmonyOS | 3.4 | - |
| Web | ❌ No | - |

**Description:** Represents an element in the main thread.

