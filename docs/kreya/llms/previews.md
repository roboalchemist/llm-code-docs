# Source: https://kreya.app/docs/scripting-and-tests/previews.md

# Previewing data [Pro / Enterprise](/pricing.md)

Kreya previews allow you to programmatically create powerful data visualizations directly within Kreya. By adding preview calls to your scripts, you can turn raw response data into meaningful visual displays.

## Why use previews?[​](#why-use-previews "Direct link to Why use previews?")

* **Enhanced data interpretation**: Visualize raw response data in a more digestible format, making it easier to understand.
* **Customizable visualizations**: Tailor the preview to highlight the most relevant details for your use case.

## How previews work[​](#how-previews-work "Direct link to How previews work")

Kreya's [`kreya.preview` API](/docs/scripting-and-tests/general/kreya-base-script-api.md#previewscriptapi) provides methods to display various types of data in the preview tab. For example, you can render PDFs and HTML from in-memory data or preview files from the file system.

### Example: Displaying a PDF[​](#example-displaying-a-pdf "Direct link to Example: Displaying a PDF")

The following script demonstrates how to display a PDF document in Kreya's preview tab:

```
// preview a pdf file from the file system
await kreya.preview.file('./sample.pdf', 'Sample PDF');

// preview a pdf document based on in-memory data
const pdfData = new Uint8Array([
  /* ... */
]);
await krey.preview.pdf(pdfData, 'Sample PDF');
```

This will render the `sample.pdf` file or the provided data in the preview tab with the title "Sample PDF".

## Explore the API[​](#explore-the-api "Direct link to Explore the API")

To learn more about the `kreya.preview` API and its capabilities, check out the [kreya.preview API documentation](/docs/scripting-and-tests/general/kreya-base-script-api.md#previewscriptapi).

## Samples[​](#samples "Direct link to Samples")

Explore the [samples](/docs/category/preview-data.md) to see Kreya's preview capabilities in action.
