# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es6/how-to/get-the-selected-content.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es5/how-to/get-the-selected-content.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/vue/how-to/get-the-selected-content.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/react/how-to/get-the-selected-content.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/blazor/how-to/get-the-selected-content.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/angular/how-to/get-the-selected-content.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-mvc/how-to/get-the-selected-content.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-core/how-to/get-the-selected-content.md

# How to get the selected content in Document Editor component

You can get the selected content from the React Document Editor component as plain text and SFDT (rich text).

## Get the selected content as plain text

You can use `text` API to get the selected content as plain text from React Document Editor component.


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<div class="control-section">
    <ejs-documenteditorcontainer id="container" serviceUrl="/api/DocumentEditor/" enableToolbar=true created="onCreated" height="590px"></ejs-documenteditorcontainer>
</div>

<script>
    var documenteditor;
    var container;
    function onCreated() {
        var documenteditorElement = document.getElementById("container");
        container = documenteditorElement.ej2_instances[0];
        documenteditor = container.documentEditor;
        // creating Custom Options
        let menuItems = [
            {
              text: 'Search In Google',
              id: 'search_in_google',
              iconCss: 'e-icons e-de-ctnr-find',
            },
        ];
        // adding Custom Options
        container.documentEditor.contextMenu.addCustomMenu(menuItems, false);
        // custom Options Select Event
        container.documentEditor.customContextMenuSelect =function (args){
          // custom Options Functionality
          let id = container.documentEditor.element.id;
          switch (args.id) {
            case id + 'search_in_google':
              // To get the selected content as plain text
              let searchContent =
                container.documentEditor.selection.text;
              if (!container.documentEditor.selection.isEmpty &&
                /\S/.test(searchContent)) {
                window.open('http://google.com/search?q=' + searchContent);
              }
              break;
          }
        };
    }
</script>

{% endhighlight %}
{% highlight c# tabtitle="Get-text.cs" %}
{% endhighlight %}
{% endtabs %}


You can add the following custom options using this API,

* Save or export the selected text as text file.
* Search the selected text in Google or other search engines.
* Show synonyms for the selected word in context menu and replace with selected synonym using the setter method of same API.

## Get the selected content as SFDT (rich text)

You can use `sfdt` API to get the selected content as rich text from React Document Editor component.


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}

<ejs-documenteditorcontainer id="container" serviceUrl="/api/DocumentEditor/" enableToolbar=true created="onCreated" height="590px"></ejs-documenteditorcontainer>

<script>
    var documenteditor;
    var container;
    function onCreated() {
        var documenteditorElement = document.getElementById("container");
        container = documenteditorElement.ej2_instances[0];
        documenteditor = container.documentEditor;
        // To insert text in cursor position
        container.documentEditor.editor.insertText('Document editor');
        // To select all the content in document
        container.documentEditor.selection.selectAll();
        // Insert bookmark to selected content
        container.documentEditor.editor.insertBookmark('Bookmark1');
        //Select the bookmark
        container.documentEditor.selection.selectBookmark('Bookmark1');
        // To get the selected content as sfdt
        let selectedContent = container.documentEditor.selection.sfdt;
        // Insert the sfdt content in cursor position using paste API
        container.documentEditor.editor.paste(selectedContent);
    }
</script>


{% endhighlight %}
{% highlight c# tabtitle="Get-sfdt.cs" %}
{% endhighlight %}
{% endtabs %}


You can add the following custom options using this API,

* Save or export the selected content as SFDT file.
* Get the content of a bookmark in Word document as SFDT by selecting a bookmark using `select bookmark` API.
* Create template content that can be inserted to multiple documents in cursor position using `paste` API.