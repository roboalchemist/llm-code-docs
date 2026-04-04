# Source: https://docs.intelligems.io/performance-optimization/site-performance.md

# Site Performance

Intelligems is designed to have as minimal an effect on site performance as possible. We use tools like [pagespeed.web.dev](https://pagespeed.web.dev/) (Lighthouse) and [webpagetest.org](https://www.webpagetest.org/) to ensure our script runs efficiently.

Our goal is to create a seamless customer experience, preventing annoyances like flashing or flickering of elements on the page.

Every website is designed differently, has different underlying tools, and different ways of loading. We have a wide range of configurations to help provide the fastest experience. This guide should help maximize them.

## Debugging Performance Issues

### Javascript Tag

The default javascript tag looks like this:

{% code fullWidth="true" %}

```javascript
<script>
    window.Shopify = window.Shopify || {theme: {id: {{ theme.id }}, role: '{{ theme.role }}' } };
    window._template = {
        directory: "{{ template.directory }}",
        name: "{{ template.name }}",
        suffix: "{{ template.suffix }}"
    };
  </script>
  <script type="module" blocking="render" fetchpriority="high" src="https://cdn.intelligems.io/esm/31337h4x045/bundle.js" async></script>
```

{% endcode %}

* `type="module"` – This leverages a newer Javascript paradigm called ESM and natively provides speed benefits. **This cannot be changed.**
* `blocking="render"` – We include this to prevent flashing. However, for some very optimized sites, removing this parameter may improve LCP & FCP. **You may choose to experiment with removing this property.**
* `fetchpriority="high"` – This indicates to the browser to load Intelligems quickly so that our experiences are available as soon as the page is rendered.
* `src=""` – This is a reference to your customer-specific site. Make sure to copy from your [settings page](https://app.intelligems.io/settings); the unique customer ID in the code block above is just an example.
* `async` – This tells the browser to continue to render the page while Intelligems loads and is a best practice for high-performing sites. If you notice this is missing, please add it!

### Types of tests

Different tests leverage different browser capabilities to execute and have different impacts on site speed.

* **Javascript & CSS Injection:** These tests are some of the most efficient. We leverage the browser capabilities and simply add `<style>` and `<script>` elements to the `<head>` of your page and let the browser do the rest.
* **Onsite Edits:** These tests rely on our javascript to find the appropriate elements on the page and update them. While this can be incredibly fast, for large sections of HTML or elements that require loading additional content, e.g. images and videos, there may be other effects on page speed.
* **Price Tests:** Price tests are designed to be incredibly efficient, but there are many algorithms under the hood that are running to make this happen. You can read more about optimizing your pricing integration [here](https://docs.intelligems.io/performance-optimization/optimizing-your-price-test-integration).

### We're here to help!

If you're noticing undesirable impacts on site speed because of Intelligems, there's certainly an opportunity for improvement. Please [contact our support team](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) if you need assistance.
