# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/blazor-classic/magnification.md

# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/flutter/magnification.md

# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/maui/magnification.md

# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/javascript-es6/magnification.md

# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/javascript-es5/magnification.md

# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/vue/magnification.md

# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/react/magnification.md

# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/blazor/magnification.md

# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/angular/magnification.md

# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/asp-net-mvc/magnification.md

# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/asp-net-core/magnification.md

# Magnification

The PDF Viewer includes magnification tools on the default toolbar: Zoom In, Zoom Out, Zoom, Fit Page, and Fit Width. The toolbar can be configured to show or hide magnification tools as needed.

The following example shows how to enable magnification:


{% tabs %}
{% highlight cshtml tabtitle="Standalone" %}

<div style="width:100%;height:600px">
    <ejs-pdfviewer id="pdfviewer"
                   style="height:600px"
                   documentPath="https://cdn.syncfusion.com/content/pdf/pdf-succinctly.pdf"
                   enableMagnification="true">
    </ejs-pdfviewer>
</div>

{% endhighlight %}
{% highlight cshtml tabtitle="Server-Backed" %}

<div style="width:100%;height:600px">
    <ejs-pdfviewer id="pdfviewer"
                   style="height:600px"
                   serviceUrl="/api/PdfViewer"
                   documentPath="https://cdn.syncfusion.com/content/pdf/pdf-succinctly.pdf"
                   enableMagnification="true">
    </ejs-pdfviewer>
</div>

{% endhighlight %}
{% endtabs %}

The following magnification options are available in the default toolbar:

* **ZoomIn**:- Zoom in from the current zoom value.
* **ZoomOut**:- Zoom out from the current zoom value.
* **Zoom**:- Zoom to a specific percentage.
* **FitPage**:- Fit the entire page within the available viewport.
* **FitWidth**:- Fit the page width to the viewport.
* **Auto**:- Fits the page content with-in the viewport on resizing action.

![Zoom controls in the PDF Viewer toolbar](./images/zoom.png)

N> The PDF Viewer supports zoom values from 10% to 400%.

## See also

* [Toolbar items](./toolbar)
* [Feature Modules](./feature-module)