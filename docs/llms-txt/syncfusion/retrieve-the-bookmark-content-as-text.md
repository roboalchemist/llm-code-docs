# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es6/how-to/retrieve-the-bookmark-content-as-text.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es5/how-to/retrieve-the-bookmark-content-as-text.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/vue/how-to/retrieve-the-bookmark-content-as-text.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/react/how-to/retrieve-the-bookmark-content-as-text.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/blazor/how-to/retrieve-the-bookmark-content-as-text.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/angular/how-to/retrieve-the-bookmark-content-as-text.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-mvc/how-to/retrieve-the-bookmark-content-as-text.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-core/how-to/retrieve-the-bookmark-content-as-text.md

# How to retrieve the whole document and bookmark content as text in  Document Editor component

You can get the bookmark or whole document content from the Document Editor component as plain text and SFDT (rich text).

## Get the bookmark content as plain text

You can [`selectBookmark`] API to navigate to the bookmark and use [`text`] API to get the bookmark content as plain text from Document Editor component.

The following example code illustrates how to get the bookmark content as plain text.


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
{% endhighlight %}{% endtabs %}


To get the bookmark content as SFDT (rich text), check this [`link`](../../asp-net-core/how-to/get-the-selected-content#get-the-selected-content-as-sfdt-rich-text)

## Get the whole document content as text

You can use [`text`] API to get the whole document content as plain text from Document Editor component.

The following example code illustrates how to get the whole document content as plain text.


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
{% endhighlight %}{% endtabs %}


## Get the whole document content as SFDT(rich text)

You can use [`serialize`] API to get the whole document content as SFDT string from Document Editor component.

The following example code illustrates how to get the whole document content as SFDT.


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
{% endhighlight %}{% endtabs %}


## Get the header content as text

You can use [`goToHeader`] API to navigate the selection to the header and then use [`text`] API to get the content as plain text.

The following example code illustrates how to get the header content as plain text.


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
{% endhighlight %}{% endtabs %}


Similarly, you can use [`goToFooter`] API to navigate the selection to the footer and then use [`text`] API to get the content as plain text.