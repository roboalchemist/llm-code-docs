# Source: https://developers.webflow.com/browser/custom-goals/on-site-conversions/sendEvent.mdx

***

title: sendEvent()
slug: custom-goals/on-site-conversions/sendEvent
description: Trigger an on-site conversion goal with the sendEvent API
hidden: false
'og:title': sendEvent()
'og:description': Trigger an on-site conversion goal with the sendEvent API
---------------------------------------------------------------------------

## `wf.sendEvent(eventName, options?)`

Trigger a custom goal event to track conversions on your site.

<Note title="Create a custom goal first">
  Before calling `wf.sendEvent()`, create a custom goal first. The `eventName` you create is what you'll pass to this method.
</Note>

### Syntax

```typescript
wf.sendEvent(eventName: string)
```

```typescript
wf.sendEvent(eventName: string, options: { value: number | string })
```

### Parameters

* **eventName** (required): `string` — The name of the custom event you created in your custom goal. Must be 40 printable ASCII characters or fewer, and cannot contain spaces.

* **options** (optional): `{ value: number | string }` — An object containing a `value` property for tracking monetary or numeric values with the conversion.

<Info title="Value formatting">
  When including a `value`, it must meet these conditions:

  * Can be a string or number
  * Must not be negative (e.g., `10` is valid, `-10` is not)
  * Can include up to two decimal places (e.g., `10`, `10.5`, `10.50`)
  * Must not include currency symbols (e.g., `10.50` is valid, `$10.50` is not)

  To ensure two-decimal accuracy when working with dynamic values:

  ```javascript
  Number.parseFloat(rawValue).toFixed(2);
  ```
</Info>

### Use with Google Tag Manager

If you're using Google Tag Manager (GTM) and already have triggers set up for actions you want to track, you can create a custom HTML tag that calls `wf.sendEvent()`:

```html
<script>
wf.ready(function() {
    wf.sendEvent('form_submitted');
});
</script>
```

Then attach this tag to an existing GTM trigger (e.g., a "Form Submission" trigger you're already using for other tracking).

### Examples

#### Basic usage

Track a simple on-site conversion:

```javascript
wf.ready(function() {
    wf.sendEvent('form_submitted');
});
```

#### With a value

Track an on-site conversion with an associated monetary value:

```javascript
wf.ready(function() {
    wf.sendEvent('purchase', { value: 149.99 });
});
```

#### Recording dynamic values

Track values that vary based on user action, such as a shopping cart total:

```javascript
wf.ready(function() {
    var eventName = 'purchase';
    var price = document.getElementById('total_price').value;
    wf.sendEvent(eventName, { value: price });
});
```

### Returns

This method doesn't return a value. The event is sent to Webflow and recorded in your optimization results.

### FAQs

{/* <!-- vale off --> */}

<Accordion title="Why isn't my custom goal showing up in Analyze/Optimize?">
  {/* <!-- vale on --> */}

  Make sure you've:

  * Created the custom goal in Webflow, following the instructions here: [Create a custom goal](https://help-optimize.webflow.com/hc/en-us/articles/41355869779347-Create-or-edit-a-custom-goal)
  * Used the exact `eventName` (case-sensitive) in your `wf.sendEvent()` call
  * Wrapped your code in `wf.ready()` to ensure the Browser API is available

  {/* <!-- vale off --> */}
</Accordion>

<Accordion title="How quickly do on-site conversion goals appear in my Analyze/Optimize dashboard?">
  {/* <!-- vale on --> */}

  On-site conversion events are recorded in real time and should appear in your Analyze/Optimize dashboard within approximately 15 - 30 minutes.

  {/* <!-- vale off --> */}
</Accordion>

{/* <!-- vale on --> */}
