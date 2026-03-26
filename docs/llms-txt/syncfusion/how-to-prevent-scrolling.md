# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/blazor/faqs/how-to-prevent-scrolling.md

# Prevent the PDF from scrolling and remove the vertical scrollbar

To prevent a PDF from scrolling and remove the vertical scrollbar in the Syncfusion<sup style="font-size:70%">&reg;</sup> Blazor SfPdfViewer component, set the container's CSS `overflow` property to `hidden`.

Setting `overflow: hidden` removes scrollbars and disables user scrolling. To target only vertical scrolling, consider `overflow-y: hidden`.

```html

<style>
    .e-pv-viewer-container {
        overflow: hidden !important;
    }
</style>

```

[View the prevent scrolling sample on GitHub](https://github.com/SyncfusionExamples/blazor-pdf-viewer-examples/tree/master/Common/Prevent%20the%20PDF%20from%20scrolling)
