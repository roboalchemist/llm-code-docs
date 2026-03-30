# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/react/how-to/retrieve-id-of-the-document.md

## Retrieve document ID in React PDF Viewer

This article shows how to retrieve the PDF document ID that the viewer stores in `sessionStorage` under the key `hashId`.

Refer to the following minimal example that logs the stored document ID when a button is clicked:

```
<button onclick="uniqueId()">UniqueId</button>

<script>
    // Event triggers when you click the UniqueId button.
    function uniqueId() {
        //Prints the PDF document id in the console window.
        console.log(window.sessionStorage.getItem("hashId"));
    }
</script>
```

[View sample in GitHub](https://github.com/SyncfusionExamples/react-pdf-viewer-examples/tree/master/How%20to/Get%20hash%20id%20from%20storage).