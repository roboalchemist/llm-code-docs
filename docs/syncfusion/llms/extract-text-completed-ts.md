# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/javascript-es6/how-to/extract-text-completed-ts.md

# Use extractTextCompleted to extract text in TypeScript PDF Viewer

Use the [isExtractText](https://ej2.syncfusion.com/documentation/api/pdfviewer/#isextracttext) property together with the [extractTextCompleted](https://ej2.syncfusion.com/documentation/api/pdfviewer/#extracttextcompleted) event to extract page text and its positional bounds from a loaded PDF document.

The following example shows how to enable text extraction and handle the completion event:

```ts

viewer.isExtractText = true;
viewer.extractTextCompleted = args => {
    //Extract the Complete text of load document
    console.log(args);
    console.log(args.documentTextCollection[1]);
    //Extract the Text data.
    console.log(args.documentTextCollection[1][1].textData);
    //Extract Text in the Page.
    console.log(args.documentTextCollection[1][1].pageText);
    //Extracts the first text of the PDF document along with its bounds
    console.log(args.documentTextCollection[1][1].textData[0].Bounds);
};

```

Find the sample: [How to extract text](https://stackblitz.com/edit/3xmbg6-m3ff47?devtoolsheight=33&file=index.ts)
