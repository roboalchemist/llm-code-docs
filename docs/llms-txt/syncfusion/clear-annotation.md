# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/javascript-es5/how-to/clear-annotation.md

# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/react/how-to/clear-annotation.md

# Clear annotations in React PDF Viewer

Use the [deleteAnnotations](https://ej2.syncfusion.com/react/documentation/api/pdfviewer#deleteannotations) method to clear all annotations in the currently loaded document.

Example: Clear all annotations in the loaded document

```html
<button onclick="deleteAnnotations()">Delete Annotations</button>

<script>
// Clear all annotations
function deleteAnnotations() {
    var viewer = document.getElementById("container").ej2_instances[0];
    viewer.deleteAnnotations();
}
</script>
```

To remove a specific annotation, use the deleteAnnotationById method to target an annotation by its id.

Example: Delete a specific annotation by id

```html
<button onclick="deleteAnnotationbyId()">Delete Annotation by ID</button>

<script>
// Delete an annotation by id
function deleteAnnotationbyId() {
    var viewer = document.getElementById("container").ej2_instances[0];
    if (viewer.annotationCollection && viewer.annotationCollection.length > 0) {
        viewer.annotationModule.deleteAnnotationById(viewer.annotationCollection[0].annotationId);
    }
}
</script>
```

[How to clear annotations using deleteAnnotations](https://stackblitz.com/edit/react-xlvqkm?file=public%2Findex.html)