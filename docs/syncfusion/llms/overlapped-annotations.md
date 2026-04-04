# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/javascript-es5/how-to/overlapped-annotations.md

# Get overlapped annotations on click in JavaScript PDF Viewer

Use the [annotationCollection](https://ej2.syncfusion.com/documentation/api/pdfviewer/#annotationcollection) property of the [annotationSelect](https://ej2.syncfusion.com/documentation/api/pdfviewer/#annotationselect) event to get overlapped annotations when the user clicks an annotation.

The following example shows how to access overlapped annotations on click:

```javascript

// Get overlapped annotation collections.
viewer.annotationSelect =(args) =>{
  console.log(args.annotationCollection);
}

```

Find the sample: [Get overlapped annotations on click](https://stackblitz.com/edit/a93cem-lprlap?devtoolsheight=33&file=index.js)