# Source: https://docs.nimbleway.io/nimble-sdk/web-api/nimble-web-api-functions/page-interaction/infinite-scrolling.md

# Infinite Scrolling

## infinite\_scroll Function

A common use case for Page Interactions is to scroll down pages that differ loading off-screen content until a user scrolls down to reveal it. Also known as "lazy loading", websites often do this to reduce page load times or as an alternative to pagination. Some examples include Facebook's newsfeed, Google News, and YouTube's search pages.

Page Interactions include a dedicated feature named `infinite_scroll` designed specifically to scroll through lazy loading web pages. It's controlled using three parameters:

<table><thead><tr><th width="229">Parameter</th><th width="193">Required</th><th>Description</th></tr></thead><tbody><tr><td><code>duration</code></td><td>Required when <code>infinite_scroll</code> is being used</td><td>Integer | A time interval in milliseconds during which scrolling should be continuously attempted.</td></tr><tr><td><code>loading_selector</code></td><td>Optional</td><td>String | An identifier of the HTML element that displays the loading/spinner indicator. This helps identify when loading starts and ends.</td></tr><tr><td><code>delay_after_scroll</code></td><td>Optional</td><td>Integer | The time delay, in ms, between scrolls.</td></tr><tr><td><code>click_on_selector</code></td><td>Optional</td><td>Bool | CSS selector to click after each scroll (foe example "Load more" button)</td></tr><tr><td><code>idle_timeout</code></td><td>Optional</td><td>Integer | Time (ms) to wait after scroll; ends if no height change, optimizing infinite scroll.</td></tr><tr><td><code>scroll_in_element</code></td><td>Optional</td><td>String | Enables scrolling inside a specific element (e.g., sidebar, modal, or div).</td></tr></tbody></table>

{% hint style="info" %}
Scrolling is initiated as soon as the page load event is fired.
{% endhint %}

Infinite Scroll was designed to be used in one of two main methods:

### **Identifying the loading element**

Where possible, it is recommended to use this method, as it allows for more accurate scrolling operation. Use the `loading_selector` parameter to identify the loading indicator or spinner that is displayed while the page loads additional content, and refine the scrolling behavior with the `delay_after_scroll` and `duration` parameter&#x73;**.**

### **Time-based scrolling**

In cases where there is no loading indicator, the `delay_after_scroll` and `duration` parameters can be used to define and refine the scrolling action until it is well-timed for the particular webpage in question.

### **Example Request**

{% tabs %}
{% tab title="cURL" %}

```bash
curl -X POST 'https://api.webit.live/api/v1/realtime/web' \
--header 'Authorization: Basic <credential string>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "url": "https://www.example.com",
    "render": true,
    "format": "json",
    "country": "US",
    "parse": true,
    "render_flow": [
        {
            "infinite_scroll": {
                "loading_selector": ".spinner",
                "delay_after_scroll": 2000,
                "duration": 15000
            }
        }    
    ]
}'
```

{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Like all Page Interactions, infinite scrolling is capped by the global 120-second session timeout, and will be terminated if this limit is reached.
{% endhint %}
