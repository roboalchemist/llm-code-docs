# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/blazor/faqs/how-to-create-sfpdfviewer-in-a-splitter-component.md

# Create the PDF Viewer in a Splitter component in Blazor

The Syncfusion Blazor Splitter organizes content into resizable panes. The following example shows how to place the PDF Viewer inside a Splitter pane so users can view a document alongside other UI content.

```cshtml

@using Syncfusion.Blazor.SfPdfViewer
@using Syncfusion.Blazor.Layouts

<!--This splitter layout holds two panes-->
<SfSplitter Height="100%" Width="100%">
    <!--Configures one or more panes to construct different layouts-->
    <SplitterPanes>

        <SplitterPane Size="200px">
            <ContentTemplate>
                <div> Left pane </div>
            </ContentTemplate>
        </SplitterPane>

        <SplitterPane Size="200px">
            <ContentTemplate>

                <!--Build the PDF Viewer inside a splitter pane-->
                <SfPdfViewer2 @ref="@viewer"
                              DocumentPath="@DocumentPath">
                </SfPdfViewer2>

            </ContentTemplate>
        </SplitterPane>

    </SplitterPanes>
</SfSplitter>

@code
{
    SfPdfViewer2 viewer;
    private string DocumentPath { get; set; } = "wwwroot/Data/PDF_Succinctly.pdf";
}

```

[View sample in GitHub](https://github.com/SyncfusionExamples/blazor-pdf-viewer-examples/tree/master/Common/Render%20the%20PDF%20Viewer%20on%20Splitter).