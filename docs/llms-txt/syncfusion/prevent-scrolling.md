# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/blazor-classic/how-to/prevent-scrolling.md

# Prevent Scrolling in Blazor PDF Viewer

To prevent a PDF from scrolling and remove the vertical scroll bar in the Syncfusion<sup style="font-size:70%">&reg;</sup> Blazor PDF Viewer component, use CSS to set the `overflow` property of the component container to `hidden`.

By setting the overflow property to hidden, the PDF viewer component will be displayed without a vertical scrollbar, and the user will not be able to scroll the content of a PDF.

```html
<style>
    .e-pv-viewer-container {
        overflow: hidden !important;
    }
</style>
```

[View Sample in GitHub](https://github.com/SyncfusionExamples/blazor-pdf-viewer-examples/tree/BLAZ-28848-preventScroll/Common/Prevent%20the%20PDF%20from%20scrolling)