# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es6/how-to/insert-text-in-current-position.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es5/how-to/insert-text-in-current-position.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/vue/how-to/insert-text-in-current-position.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/react/how-to/insert-text-in-current-position.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/blazor/how-to/insert-text-in-current-position.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/angular/how-to/insert-text-in-current-position.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-mvc/how-to/insert-text-in-current-position.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-core/how-to/insert-text-in-current-position.md

# How to insert text, paragraph and rich-text content in Document Editor component

You can insert the text, paragraph and rich-text content in Document Editor component.

## Insert text in current cursor position

You can use [`insertText`](https://ej2.syncfusion.com/javascript/documentation/api/document-editor/editor/#inserttext) API in editor module to insert the text in current cursor position.

The following example code illustrates how to add the text in current selection.

```typescript
// It will insert the provided text in current selection
this.container.documentEditor.editor.insertText('Syncfusion');
```

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<button id='insert'>Insert Text</button>
<div class="control-section">
    <ejs-documenteditorcontainer id="container" enableToolbar=true created="onCreated" height="590px"></ejs-documenteditorcontainer>
</div>

<script>
    var documenteditor;
    var container;
    function onCreated() {
        var documenteditorElement = document.getElementById("container");
        container = documenteditorElement.ej2_instances[0];
    }
    document.getElementById('insert').addEventListener('click', () => {
        // It will insert the provided text in current selection
        container.documentEditor.editor.insertText('Syncfusion');
    });
</script>
{% endhighlight %}
{% highlight c# tabtitle="Insert-text.cs" %}
{% endhighlight %}{% endtabs %}


## Insert paragraph in current cursor position

To insert new paragraph at current selection, you can can use [`insertText`] API with parameter as `\r\n` or `\n`.

The following example code illustrates how to add the new paragraph in current selection.

```typescript
// It will add the new paragraph in current selection
this.container.documentEditor.editor.insertText('\n');
```

## Insert the rich-text content

To insert the HTML content, you have to convert the HTML content to SFDT Format using [`web service`]. Then use [`paste`] API to insert the sfdt at current cursor position.

N> HTML string should be well formatted html. [`DocIO`](https://help.syncfusion.com/file-formats/docio/html) support only well formatted XHTML.  

The following example illustrates how to insert the HTML content at current cursor position.

* Send the HTML content to server side for SFDT conversion. Refer to the following example to send the HTML content to server side and inserting it in current cursor position.


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<div class="control-section">
    <button id='export'>Export</button>
    <ejs-documenteditorcontainer id="container" serviceUrl="/api/DocumentEditor/" enableToolbar=true created="onCreated" height="590px"></ejs-documenteditorcontainer>
</div>

<script>
    var documenteditor;
    var container;
    function onCreated() {
        var documenteditorElement = document.getElementById("container");
        container = documenteditorElement.ej2_instances[0];
    }
    let htmltags =
  "<?xml version='1.0' encoding='utf - 8'?><!DOCTYPE html PUBLIC '-//W3C//DTD XHTML 1.0 Strict//EN''http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd'><html xmlns ='http://www.w3.org/1999/xhtml' xml:lang='en' lang ='en'><body><h1>The img element</h1><img src='https://www.w3schools.com/images/lamp.jpg' alt ='Lamp Image' width='500' height='600'/></body></html>";
    document.getElementById('export').addEventListener('click', () => {
        let http = new XMLHttpRequest();
        http.open('POST', '/api/documenteditor/LoadString');
        http.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');
        http.responseType = 'json';
        http.onreadystatechange = function () {
          if (http.readyState === 4) {
            if (http.status === 200 || http.status === 304) {
              // Insert the sfdt content in cursor position using paste API
              container.documentEditor.editor.paste(http.response);
            } else {
              alert('failed;');
            }
          }
        };

        let htmlContent = { content: htmltags };
        http.send(JSON.stringify(htmlContent));
    });
</script>

{% endhighlight %}
{% highlight c# tabtitle="Insert-rich-text.cs" %}
{% endhighlight %}{% endtabs %}


* Refer the following code example for server-side web implementation for HTML conversion using DocumentEditor.

```c#
//API controller for the conversion.
[HttpPost]
public string LoadString([FromBody]InputParameter data)
{
    // You can also load HTML file/string from server side.
    Syncfusion.EJ2.DocumentEditor.WordDocument document = Syncfusion.EJ2.DocumentEditor.WordDocument.LoadString(data.content, FormatType.Html); // Convert the HTML to SFDT format.
    string json = Newtonsoft.Json.JsonConvert.SerializeObject(document);
    document.Dispose();
    return json;
}

public class InputParameter
{
    public string content {get; set; }
}
```

N> The above example illustrates inserting HTML content. Similarly, you can insert any rich-text content by converting any of the supported file formats (DOCX, DOC, WordML, HTML, RTF) to SFDT.