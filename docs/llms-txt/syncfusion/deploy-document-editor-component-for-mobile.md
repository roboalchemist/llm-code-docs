# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es6/how-to/deploy-document-editor-component-for-mobile.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es5/how-to/deploy-document-editor-component-for-mobile.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/vue/how-to/deploy-document-editor-component-for-mobile.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/react/how-to/deploy-document-editor-component-for-mobile.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/angular/how-to/deploy-document-editor-component-for-mobile.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-mvc/how-to/deploy-document-editor-component-for-mobile.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-core/how-to/deploy-document-editor-component-for-mobile.md

# Deploy Document Editor component for Mobile

## Document editor component for Mobile

At present, Document editor component is not responsive for mobile, and the editing functionalities aren't ensured in mobile browsers. Whereas it works properly as a document viewer in mobile browsers.

Hence, it is recommended to switch the Document editor component as read-only in mobile browsers. Also, invoke `fitPage` method with `FitPageWidth` parameter in document change event, such as to display one full page by adjusting the zoom factor.


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-documenteditorcontainer id="container" enableToolbar=true documentChange="onDocumentChange" height="590px">
</ejs-documenteditorcontainer>
<script>
    function onDocumentChange() {
        var container = document.getElementById("container").ej2_instances[0];
        //To detect the device
        var isMobileDevice = /Android|Windows Phone|webOS/i.test(navigator.userAgent);

        if (isMobileDevice) {
            container.restrictEditing = true;
            setTimeout(() => {
                container.documentEditor.fitPage("FitPageWidth");
            }, 50);
        }
        else {
            container.restrictEditing = false;
        }
    }
</script>
{% endhighlight %}
{% highlight c# tabtitle="Mobile-view.cs" %}
{% endhighlight %}{% endtabs %}



N> You can use the [`restrictEditing`](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.DocumentEditor.DocumentEditorContainer.html#Syncfusion_EJ2_DocumentEditor_DocumentEditorContainer_RestrictEditing) in DocumentEditorContainer and [`isReadOnly`](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.DocumentEditor.DocumentEditor.html#Syncfusion_EJ2_DocumentEditor_DocumentEditor_IsReadOnly) in DocumentEditor based on your requirement to change component to read only mode.
