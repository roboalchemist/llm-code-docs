# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es6/how-to/get-current-word.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es5/how-to/get-current-word.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/vue/how-to/get-current-word.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/react/how-to/get-current-word.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/blazor/how-to/get-current-word.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/angular/how-to/get-current-word.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-mvc/how-to/get-current-word.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-core/how-to/get-current-word.md

# How to select and retrieve the word and paragraph in current cursor position in Document Editor component

You can get the current word or paragraph content from the  Document Editor component as plain text and SFDT (rich text).

## Select and get the word in current cursor position

You can use [`selectCurrentWord`] API in selection module to select the current word at cursor position and use [`text`] API to get the selected content as plain text from Document Editor component.

The following example code illustrates how to select and get the current word as plain text.



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
    // To select the current word in document
    container.documentEditor.selection.selectCurrentWord();

    // To get the selected content as text
    var selectedContentText = container.documentEditor.selection.text;
    // To get the selected content as SFDT (rich text)
    var selectedContentSFDT = container.documentEditor.selection.sfdt;
  }
</script>
{% endhighlight %}
{% highlight c# tabtitle="Get-word.cs" %}
{% endhighlight %}
{% endtabs %}


## Select and get the paragraph in current cursor position

You can use [`selectParagraph`] API in selection module to select the current paragraph at cursor position and use [`text`] API or [`sfdt`] API to get the selected content as plain text or SFDT from Document Editor component.

The following example code illustrates how to select and get the current paragraph as SFDT.


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
    // To select the current paragraph in document
    container.documentEditor.selection.selectParagraph();

    // To get the selected content as text
    var selectedContentText = container.documentEditor.selection.text;
    // To get the selected content as SFDT (rich text)
    var selectedContentSFDT = container.documentEditor.selection.sfdt;
  }
</script>
{% endhighlight %}
{% highlight c# tabtitle="Get-paragraph.cs" %}
{% endhighlight %}
{% endtabs %}
