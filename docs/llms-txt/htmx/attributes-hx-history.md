# hx-history

**Title:** hx-history  
**Description:**  
The `hx-history` attribute in htmx allows you to prevent sensitive page data from being stored in the browser's localStorage cache during history navigation, ensuring that the page state is retrieved from the server instead when navigating through history.

## Set the `hx-history` attribute to `false`

To prevent sensitive data from being saved to the localStorage cache when htmx takes a snapshot of the page state, set the `hx-history` attribute to `false` on any element in the current document, or any html fragment loaded into the current document by htmx.

```html
<html>
<body>
<div hx-history="false">
 ...
</div>
</body>
</html>
```

## Notes

- `hx-history="false"` can be present anywhere in the document to embargo the current page state from the history cache (i.e., even outside the element specified for the history snapshot [hx-history-elt](@/attributes/hx-history-elt.md)).