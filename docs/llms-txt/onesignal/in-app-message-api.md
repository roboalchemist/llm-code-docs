# Source: https://documentation.onesignal.com/docs/en/in-app-message-api.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# In-app message JavaScript API reference

> JavaScript methods for interactive HTML in-app messages in OneSignal.

This guide covers the **JavaScript API** for HTML in-app messages created with the [OneSignal HTML Editor](./design-your-in-app-message-with-html).

If you are looking for **SDK methods** to set triggers, handle in-app click events, or manage the in-app lifecycle, see the [Mobile SDK Reference](./mobile-sdk-reference#in-app-messages).

***

## Requirements

### Use the `data-onesignal-unique-label` attribute for click tracking

All clickable elements must have a `data-onesignal-unique-label` attribute with a **unique** value. This enables OneSignal to:

* Track click analytics
* Correctly trigger associated actions

```html HTML theme={null}
<button id="unique-button-id" data-onesignal-unique-label="unique-label-for-onesignal">
  Tag User
</button>
```

<Warning> If two elements share the same `data-onesignal-unique-label`, clicks may be logged incorrectly or actions may not fire. </Warning>

### Attach event listeners

You must explicitly attach JavaScript event listeners to trigger OneSignal in-app actions.

```javascript JavaScript  theme={null}
document.getElementById("unique-button-id")
  .addEventListener("click", function(e) {
    OneSignalIamApi.tagUser(e, { fiz: "baz" });
  });
```

**Example:**

```html HTML  theme={null}
<button id="buy-now-button" data-onesignal-unique-label="buy-now-button-for-onesignal">
  Buy Now
</button>
<script>
  document.getElementById("buy-now-button").addEventListener("click", function(e) {
    OneSignalIamApi.tagUser(e, { coupon: "10OFF" });
  });
</script>
```

***

## Handling click tracking in sandboxed HTML in-app messages

Because HTML in-app messages run in a sandboxed WebView, click tracking and navigation must occur inside the same frame.
Standard anchors (`<a href="...">`) and `window.open()` calls are not tracked and can trigger console warnings such as:

```
SOAuthorizationCoordinator::tryAuthorize (2): Attempting to perform subframe navigation.
```

### Correct: use a button and OneSignal APIs

```html HTML  theme={null}
<button id="shop-now" data-onesignal-unique-label="your-unique-label-for-this-button">
  Shop Now
</button>
<script>
  document.addEventListener("DOMContentLoaded", function() {
    const btn = document.getElementById("shop-now");
    btn.addEventListener("click", function(e) {
      OneSignalIamApi.trackClick(e);
      OneSignalIamApi.openUrl(e, "https://shop.example.com/");
    });
  });
</script>
```

### Incorrect: using `<a>` or `window.open()`

```html HTML  theme={null}
<a href="https://shop.example.com" target="_blank">
  Shop Now
</a>
```

This navigation occurs outside the in-app sandbox, preventing OneSignal from logging the click event.

<Note>
  * Each clickable element must have a **unique** `data-onesignal-unique-label`.
  * Always call `OneSignalIamApi.trackClick(e)` **before** `openUrl()` or any other OneSignal API method.
  * Bind event listeners after `DOMContentLoaded` to ensure that the elements exist.
  * OneSignal automatically tracks clicks only for methods listed in this reference; any custom navigation must call `trackClick()` manually.
</Note>

### Common issues

* **Clicks not recorded:** `trackClick()` was not called or the element is missing a `data-onesignal-unique-label`.
  * Call `trackClick(e)` and ensure each element has a unique label.
* **Console shows “Attempting to perform subframe navigation”:**\
  The code uses `window.open()` or an `<a>` link instead of `OneSignalIamApi.openUrl()`.
  * Use `OneSignalIamApi.openUrl(e, "https://example.com/")` inside the same click handler.
* **Wrong label appears in analytics:**\
  Multiple elements share the same `data-onesignal-unique-label`.
  * Give each clickable element a unique label.

***

## Available functions

All [click actions](./iam-click-actions) from the [Block Editor](./design-your-in-app-message) are also available for HTML in-app messages.

### Push permission prompt

Shows the native push notification permission prompt. Click events are automatically tracked.

See [Prompt for push permissions](./prompt-for-push-permissions).

```html HTML  theme={null}
<button id="push-prompt-button" data-onesignal-unique-label="your-unique-label-for-this-button">
  Enable Push
</button>
<script>
  document.getElementById("push-prompt-button").addEventListener("click", function(e) {
    OneSignalIamApi.triggerPushPrompt(e);
  });
</script>
```

### Location permission prompt

Shows the native location permission prompt. Click events are automatically tracked.

See [Location permission prompts](./location-opt-in-prompt).

```html HTML  theme={null}
<button id="location-prompt-button" data-onesignal-unique-label="your-unique-label-for-this-button">
  Enable Location
</button>
<script>
  document.getElementById("location-prompt-button").addEventListener("click", function(e) {
    OneSignalIamApi.triggerLocationPrompt(e);
  });
</script>
```

### Close in-app message

Dismisses the current in-app message. Click events are automatically tracked.

```html html  theme={null}
<button id="close-button" data-onesignal-unique-label="your-unique-label-for-this-button">
  Close
</button>
<script>
  document.getElementById("close-button").addEventListener("click", function(e) {
    OneSignalIamApi.close(e);
  });
</script>
```

### Tag user

Sets a [Tag](./add-user-data-tags). Click events are automatically tracked.

```html HTML  theme={null}
<button id="tag-user-button" data-onesignal-unique-label="your-unique-label-for-this-button">
  Tag User
</button>
<script>
  document.getElementById("tag-user-button").addEventListener("click", function(e) {
    OneSignalIamApi.tagUser(e, { fiz: "baz" });
  });
</script>
```

### Open URL

Opens a URL in the device's browser and closes the in-app message. Click events are automatically tracked.

Supports [Deep Linking](./deep-linking).

```html HTML  theme={null}
<button id="open-url-button" data-onesignal-unique-label="your-unique-label-for-this-button">
  Visit Site
</button>
<script>
  document.getElementById("open-url-button").addEventListener("click", function(e) {
    OneSignalIamApi.openUrl(e, "https://example.com");
  });
</script>
```

### Click name

Assigns a click name that can be read in the [in-app message click listener](./mobile-sdk-reference#addclicklistener-in-app). Click events are automatically tracked.

Supports [Deep Linking](./deep-linking).

```html HTML theme={null}
<button id="click-name-button" data-onesignal-unique-label="your-unique-label-for-this-button">
  Click Me
</button>
<script>
  document.getElementById("click-name-button").addEventListener("click", function(e) {
    OneSignalIamApi.addClickName(e, "test_click_name");
  });
</script>
```

### Track click

Tracks a click event when you’re not using other clickable API methods.

```html HTML  theme={null}
<button id="track-click-button" data-onesignal-unique-label="your-unique-label-for-this-button">
  Track Click
</button>
<script>
  document.getElementById("track-click-button").addEventListener("click", function(e) {
    OneSignalIamApi.trackClick(e);
  });
</script>
```

### Send Outcome

Tracks an unattributed [Custom Outcome](./custom-outcomes) and sets a [Tag](./add-user-data-tags) on the user in format `outcome name : true`. Click events are automatically tracked.

```html html  theme={null}
<button id="send-outcome-button" data-onesignal-unique-label="your-unique-label-for-this-button">
  Claim Bonus
</button>
<script>
  document.getElementById("send-outcome-button").addEventListener("click", function(e) {
    OneSignalIamApi.sendOutcome(e, "bonus_claimed");
  });
</script>
```

***

## Personalizing HTML in-app messages

You can use tag substitution in HTML in-app messages just like in the Block Editor.

<Warning> Tag substitution **does not work** inside `<script>` tags. </Warning>

Tag substitution works for:

* Inline text (`<h1>`, `<p>`, `<li>`, etc.)

* `<style>` rules:

  ```css CSS  theme={null}
  body { background-color: "{{ favorite_color | default: '#fff' }}"; }
  ```

* Attributes with URLs:
  * `href`
  * `src`
  * `<form action>`
  * `<object data>`

### Using tags in `openUrl()` and `addClickName()`

Since `<script>` tags don’t support substitution, use one of these methods:

**1. Access all tags with `liquidPlayerTags`**

This global object becomes available after `DOMContentLoaded`.

```html HTML theme={null}
<div class="my-tags">--test checking all tags--</div>
<button id="open-url-button" data-onesignal-unique-label="promo-link">
  Personalized Offer
</button>
<script>
  document.addEventListener("DOMContentLoaded", function() {
    if (liquidPlayerTags) {
      document.querySelector(".my-tags").innerHTML = JSON.stringify(liquidPlayerTags);
    }
  });
  document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("open-url-button").addEventListener("click", function(e) {
      OneSignalIamApi.openUrl(e, "https://shop.com?coupon=" + liquidPlayerTags["coupon"]);
    });
  });
</script>
```

**2. Store a tag in the `href` attribute**

```html HTML theme={null}
<a
  id="open-url-button"
  href="app://deeplink?code={{ coupon | default: '10OFF' }}"
  data-onesignal-unique-label="promo-link"
>
  Redeem Offer
</a>
<script>
  document.getElementById("open-url-button").addEventListener("click", function(e) {
    e.preventDefault();
    OneSignalIamApi.openUrl(e, e.currentTarget.href);
  });
</script>
```

***

## Next steps

* Learn more about [using liquid syntax for tag substitution](./using-liquid-syntax)
* Explore [Deep Linking](./deep-linking) for URL handling
* [Design in-app messages with HTML](./design-your-in-app-message-with-html)

***

Built with [Mintlify](https://mintlify.com).
