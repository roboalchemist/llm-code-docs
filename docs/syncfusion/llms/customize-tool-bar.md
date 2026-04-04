# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es6/how-to/customize-tool-bar.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es5/how-to/customize-tool-bar.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/vue/how-to/customize-tool-bar.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/react/how-to/customize-tool-bar.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/blazor/how-to/customize-tool-bar.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/angular/how-to/customize-tool-bar.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-mvc/how-to/customize-tool-bar.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-core/how-to/customize-tool-bar.md

# Customize existing toolbar

## How to customize existing toolbar in DocumentEditorContainer

DocumentEditorContainer allows to customize (add, show, hide, enable, and disable) existing items in a toolbar.

* Add - New items can be defined by `CustomToolbarItemModel` and with existing items in [`ToolbarItems`](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.DocumentEditor.DocumentEditorContainer.html#Syncfusion_EJ2_DocumentEditor_DocumentEditorContainer_ToolbarItems) property. Newly added item click action can be defined in [`ToolbarClick`](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.DocumentEditor.DocumentEditorContainer.html#Syncfusion_EJ2_DocumentEditor_DocumentEditorContainer_ToolbarClick).
* Show, Hide - Existing items can be shown or hidden using the [`ToolbarItems`](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.DocumentEditor.DocumentEditorContainer.html#Syncfusion_EJ2_DocumentEditor_DocumentEditorContainer_ToolbarItems) property. Pre-defined toolbar items are available with `ToolbarItem`.
* Enable, Disable - Toolbar items can be enabled or disabled using `enableItems`


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-documenteditorcontainer id="container" created="onDocCreate"></ejs-documenteditorcontainer>
<script>
    function onDocCreate() {
        var container = document.getElementById("container").ej2_instances[0];
        var toolItem = {
            prefixIcon: "e-de-ctnr-lock",
            tooltipText: "Disable Image",
            text: onWrapText("Disable Image"),
            id: "Custom"
        };
        container.toolbarItems = [toolItem, 'Undo', 'Redo', 'Separator', 'Image', 'Table', 'Hyperlink', 'Bookmark', 'TableOfContents', 'Separator', 'Header', 'Footer', 'PageSetup', 'PageNumber', 'Break', 'InsertFootnote', 'InsertEndnote', 'Separator', 'Find', 'Separator', 'Comments', 'TrackChanges', 'Separator', 'LocalClipboard', 'RestrictEditing', 'Separator', 'FormFields', 'UpdateFields','ContentControl'];
        container.toolbarClick = function (args) {
            switch (args.item.id) {
                case 'Custom':
                    //Disable image toolbar item.
                    container.toolbar.enableItems(4, false);
                    break;
            }
        };
    }

    function onWrapText(text) {
        let content = '';
        const index = text.lastIndexOf(' ');

        if (index !== -1) {
            content = text.slice(0, index) + "<div class='e-de-text-wrap'>" + text.slice(index + 1) + "</div>";
        } else {
            content = text;
        }

        return content;
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