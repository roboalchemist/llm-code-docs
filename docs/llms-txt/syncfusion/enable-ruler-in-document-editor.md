# Source: https://docs.syncfusion.com/document-processing/word/word-processor/blazor/how-to/enable-ruler-in-document-editor.md

## How to enable ruler in Blazor Document Editor Container component

Using ruler we can refer to setting specific margins, tab stops, or indentations within a document to ensure consistent formatting in Document Editor Container.

The following example illustrates how to enable ruler in Document Editor Container.

```csharp
<button @onclick="ClickHandler">Show/Hide Ruler</button>

<div>
    <SfDocumentEditorContainer @ref="container" EnableToolbar=true Height="590px" DocumentEditorSettings="@settings">      
    </SfDocumentEditorContainer>    
</div>

@code {
    SfDocumentEditorContainer container;
    public DocumentEditorSettingsModel settings = new DocumentEditorSettingsModel() { ShowRuler = true };   
    
    private void ClickHandler()
    {
         container.DocumentEditorSettings.ShowRuler = !container.DocumentEditorSettings.ShowRuler;
         settings = new DocumentEditorSettingsModel() {
            ShowRuler = container.DocumentEditorSettings.ShowRuler,
        };
        StateHasChanged();
    }   
}
```


