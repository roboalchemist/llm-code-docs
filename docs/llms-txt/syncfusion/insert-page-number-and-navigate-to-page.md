# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es6/how-to/insert-page-number-and-navigate-to-page.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es5/how-to/insert-page-number-and-navigate-to-page.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/vue/how-to/insert-page-number-and-navigate-to-page.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/react/how-to/insert-page-number-and-navigate-to-page.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/blazor/how-to/insert-page-number-and-navigate-to-page.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/angular/how-to/insert-page-number-and-navigate-to-page.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-mvc/how-to/insert-page-number-and-navigate-to-page.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-core/how-to/insert-page-number-and-navigate-to-page.md

# How to insert page number and navigate to specific page in Document Editor component

You can insert page number and navigate to specific page in Document Editor component by following ways.

## Insert page number

You can use [`insertPageNumber`] API in editor module to insert the page number in current cursor position. By default, Page number will insert in Arabic number style. You can change it, by providing the number style in parameter.

N> Currently, Document Editor have options to insert page number at current cursor position.

The following example code illustrates how to insert page number in header.


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
       // To insert text in cursor position
       container.documentEditor.editor.insertText('Document editor');
       // To move the selection to header
       container.documentEditor.selection.goToHeader();
       // Insert page number in the current cursor position
       container.documentEditor.editor.insertPageNumber();
    }
</script>

{% endhighlight %}
{% highlight c# tabtitle="Insert-page-number.cs" %}
{% endhighlight %}{% endtabs %}


Also, you use [`insertField`] API in Editor module to insert the Page number in current position

```typescript
//Current page number
container.documentEditor.editor.insertField('PAGE \* MERGEFORMAT', '1');
```

## Get page count

You can use [`pageCount`] API to gets the total number of pages in Document.

The following example code illustrates how to get the number of pages in Document.


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
       // To insert text in cursor position
       container.documentEditor.editor.insertText('Document editor');
       // To get the total number of pages
       var pageCount =container.documentEditor.pageCount;
    }
</script>

{% endhighlight %}
{% highlight c# tabtitle="Page-count.cs" %}
{% endhighlight %}{% endtabs %}


## Navigate to specific page

You can use [`goToPage`] API in Selection module to move selection to the start of the specified page number.

The following example code illustrates how to move selection to specific page.


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
        // To move selection to page number 2
        container.documentEditor.selection.goToPage(2);
    }
</script>

{% endhighlight %}
{% highlight c# tabtitle="Go-to-page.cs" %}
{% endhighlight %}{% endtabs %}

