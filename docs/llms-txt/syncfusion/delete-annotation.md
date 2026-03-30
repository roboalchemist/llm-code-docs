# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/javascript-es6/how-to/delete-annotation.md

# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/javascript-es6/annotations/delete-annotation.md

# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/javascript-es5/annotations/delete-annotation.md

# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/vue/how-to/delete-annotation.md

# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/react/how-to/delete-annotation.md

# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/react/annotation/delete-annotation.md

# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/angular/how-to/delete-annotation.md

# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/asp-net-mvc/how-to/delete-annotation.md

# Delete a specific annotation by ID

The Syncfusion ASP.NET MVC PDF Viewer allows you to programmatically delete a specific annotation from a PDF document using the `deleteAnnotationById()` method. This method is useful for removing annotations based on user interaction, specific application logic, or cleanup tasks.

To delete a specific annotation, follow these steps:

**Step 1:** Create an ASP.NET MVC PDF Viewer sample by following the [getting started guide](https://help.syncfusion.com/document-processing/pdf/pdf-viewer/asp-net-mvc/getting-started/).

**Step 2:** Use the following code snippet to add a button and a JavaScript function to your Razor view (e.g., `Index.cshtml`) that will delete a specific annotation. The example assumes you have an annotation loaded and its ID can be accessed dynamically.

```html
<button type="button" onclick="deleteAnnotationbyId()">Delete Annotation by Id</button>

<script>
    // Delete Annotation by ID.
    function deleteAnnotationbyId() {
        var viewer = document.getElementById('pdfViewer').ej2_instances[0];
        viewer.annotationModule.deleteAnnotationById(viewer.annotationCollection[0].annotationId);
    }
</script>

```

Download the sample [how to delete a specific annotation using deleteAnnotationById](https://www.syncfusion.com/downloads/support/directtrac/general/ze/EJ2MvcSample357842164.zip)
