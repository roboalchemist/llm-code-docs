# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/javascript-es5/how-to/display-custom-tool-tip-for-annotations.md

# Display a custom tooltip for annotations in JavaScript PDF Viewer

Display custom tooltips for annotations by handling the [annotationMouseover](https://ej2.syncfusion.com/documentation/api/pdfviewer/#annotationmouseover) and `annotationMouseLeave` events.

- Include the JavaScript PDF Viewer script and the `Annotation` module on the page.
- Include the `ej.popups` module or equivalent tooltip library used in the example.
- Ensure the viewer instance is initialized before attaching the event handlers.

Example: show a tooltip on mouse over

```javascript

viewer.annotationSettings.author = "syncfusion";
var tooltip = new ej.popups.Tooltip({
    mouseTrail: true,
    opensOn: "Custom"
});
viewer.annotationMouseOver = function(args) {
    tooltip.appendTo("#pdfViewer_pageDiv_" + (viewer.currentPageNumber - 1));
    tooltip.content = args.annotation.author;
    tooltip.open();
    var ele = document.getElementsByClassName("e-tooltip-wrap")[0];
    ele.style.top = args.Y + 100 + "px";
    ele.style.left = args.X + "px";
};
viewer.annotationMouseLeave = function(args) {
    tooltip.close();
};

```

Sample: [Display a custom tooltip for annotations sample on GitHub/StackBlitz](https://stackblitz.com/edit/ztmvjx-byzwvq?file=index.js)