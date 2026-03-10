# Source: https://screenshotone.com/docs/errors/selector-not-found/

# Selector Not Found

It is an API error returned when the specified selector is not found or not visible within the given timeout period.

```json
{
    "is_successful": false,
    "error_code": "selector_not_found",
    "error_message": "If `selector` is specified and `error_on_selector_not_found`=true, or `click` is specified and `error_on_click_selector_not_found`=true, the error will be returned if the element by selector is not visible or it took more than timeout seconds to render it, but not more than 30 seconds.",
    "documentation_url": "https://screenshotone.com/docs/errors/selector-not-found/"
}
```

## Reasons and how to fix

### Selector Not Visible

The most common reason for the "selector_not_found" error is that the element specified by the selector is not visible on the page within the given timeout period.

To fix this, you can:

1. **Check the selector**: Ensure that the selector you are using is correct and matches an element on the page.
2. **Increase timeout**: If the element takes longer to load, increase the timeout value to give the element more time to become visible.

### Element is visible but has zero height

If there is an empty element on the page, the API will not be able to take a screenshot of it. In that case you will still get the "selector_not_found" error.

One of the ways to still get a screenshot is to make sure that [`error_on_selector_not_found`](https://screenshotone.com/docs/options/#error_on_selector_not_found) is set to `false` (and it is `false` by default).

You will get then the screenshot of the page instead of the error.

### Incorrect Selector

An incorrect or invalid selector can lead to this error, as the API cannot find the element on the page.

To fix this, verify that the selector is correctly specified and matches the element you want to target.

### Element Not Rendered

If the element is not rendered within the timeout period (not more than 30 seconds), the error will be triggered.

To fix this, ensure that the element is being rendered properly and within the expected time frame. You might need to investigate any delays in rendering the element.

### Conditional Visibility

If the element's visibility is conditional (e.g., depends on user interaction or specific page states), it might not be visible when the API checks for it.

To fix this, ensure that the conditions for the element's visibility are met before making the API request.

### Page Load Issues

Page load issues or JavaScript errors on the page can prevent the element from becoming visible.

To fix this, check for any page load issues or JavaScript errors that might be interfering with the rendering of the element.

## Reach out to support

If you continue to face issues or need further assistance, please reach out to `support@screenshotone.com`, and we will assist you as soon as possible.