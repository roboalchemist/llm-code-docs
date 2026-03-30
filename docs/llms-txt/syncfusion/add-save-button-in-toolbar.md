# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es6/how-to/add-save-button-in-toolbar.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es5/how-to/add-save-button-in-toolbar.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/vue/how-to/add-save-button-in-toolbar.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/react/how-to/add-save-button-in-toolbar.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/blazor/how-to/add-save-button-in-toolbar.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/angular/how-to/add-save-button-in-toolbar.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-mvc/how-to/add-save-button-in-toolbar.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-core/how-to/add-save-button-in-toolbar.md

# Add save button in Document editor toolbar

## To add a save button to the existing toolbar in DocumentEditorContainer

DocumentEditorContainer allows you to add a new button to the existing items in a toolbar using [`CustomToolbarItemModel`] and with existing items in [`toolbarItems`](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.DocumentEditor.DocumentEditorContainer.html#Syncfusion_EJ2_DocumentEditor_DocumentEditorContainer_ToolbarItems) property. Newly added item click action can be defined in [`toolbarClick`](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.DocumentEditor.DocumentEditorContainer.html#Syncfusion_EJ2_DocumentEditor_DocumentEditorContainer_ToolbarClick).


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-documenteditorcontainer id="container" created="onDocCreate"></ejs-documenteditorcontainer>
<script>
    function onDocCreate() {
        var container = document.getElementById("container").ej2_instances[0];
        var toolItem = {
            prefixIcon: "e-de-ctnr-lock",
            tooltipText: "Disable Image",
            text: "Disable Image",
            id: "Custom"
        };
        container.toolbarItems = ['New','Open',toolItem, 'Separator' ,'Undo', 'Redo', 'Separator', 'Image', 'Table', 'Hyperlink', 'Bookmark', 'Comments', 'TableOfContents', 'Separator', 'Header', 'Footer', 'PageSetup', 'PageNumber', 'Break', 'Separator', 'Find', 'Separator', 'LocalClipboard', 'RestrictEditing'];
        container.toolbarClick = function (args) {
            switch (args.item.id) {
                case 'Custom':
                    container.documentEditor.save('Sample', 'Docx');
                    break;
            }
        };
    }
</script>

{% endhighlight %}
{% highlight c# tabtitle="Document-editor.cs" %}
public ActionResult Default()
{
    return View();
}
   

{% endhighlight %}
{% endtabs %}


N> Default value of `ToolbarItems` is `['New', 'Open', 'Separator', 'Undo', 'Redo', 'Separator', 'Image', 'Table', 'Hyperlink', 'Bookmark', 'TableOfContents', 'Separator', 'Header', 'Footer', 'PageSetup', 'PageNumber', 'Break', 'InsertFootnote', 'InsertEndnote', 'Separator', 'Find', 'Separator', 'Comments', 'TrackChanges', 'Separator', 'LocalClipboard', 'RestrictEditing', 'Separator', 'FormFields', 'UpdateFields','ContentControl']`.