# Source: https://docs.syncfusion.com/windowsforms/treeview/find-and-replace.md

# Source: https://docs.syncfusion.com/windowsforms/multicolumn-treeview/find-and-replace.md

# Source: https://docs.syncfusion.com/windowsforms/grid-control/find-and-replace.md

# Source: https://docs.syncfusion.com/wpf/syntax-editor/basic-editing/find-and-replace.md

# Source: https://docs.syncfusion.com/document-processing/excel/excel-library/net/cells-manipulation/find-and-replace.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/wpf/find-and-replace.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/winforms/find-and-replace.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/uwp/find-and-replace.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/wpf/find-and-replace.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/uwp/find-and-replace.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es6/find-and-replace.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es5/find-and-replace.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/vue/find-and-replace.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/react/find-and-replace.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/blazor/find-and-replace.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/angular/find-and-replace.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-mvc/find-and-replace.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-core/find-and-replace.md

# Find and Replace in ASP.NET Core in Document Editor Component

The document editor component searches a portion of text in the document through a built-in interface called `OptionsPane` or rich APIs. When used in combination with selection performs various operations on the search results like replacing it with some other text, highlighting it, making it bolder, and more.

## Options pane

This provides the options to search for a portion of text in the document. After search operation is completed, the search results will be displayed in a list and options to navigate between them. The current occurrence of matched text or all occurrences with another text can be replaced by switching to `Replace` tab. This pane is opened using the keyboard shortcut `CTRL+F`.


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-button id="showhidepane">Show hide pane</ejs-button>
<div id="documenteditor" style="width:100%;height:100%" >
    <ejs-documenteditor isReadOnly=false enableEditor=true enableSelection=true enableSearch=true enableOptionsPane=true id="container"></ejs-documenteditor>
</div>

<script>
    var documenteditor;
    document.addEventListener('DOMContentLoaded', function () {
        documenteditor = document.getElementById("container").ej2_instances[0];
        var sfdt = {
            "sections": [
                {
                    "blocks": [
                        {
                            "inlines": [
                                {
                                    "characterFormat": {
                                        "bold": true,
                                        "italic": true
                                    },
                                    "text": "Adventure Works Cycles, the fictitious company on which the AdventureWorks sample databases are based, is a large, multinational manufacturing company. The company manufactures and sells metal and composite bicycles to North American, European and Asian commercial markets. While its base operation is located in Bothell, Washington with 290 employees, several regional sales teams are located throughout their market base."
                                }
                            ]
                        }
                    ]
                }
            ]
        };
        documenteditor.open(JSON.stringify(sfdt));

        document.getElementById('showhidepane').addEventListener('click', function () {
            documenteditor.showOptionsPane();
        });
    });
</script>

{% endhighlight %}
{% highlight c# tabtitle="Options-pane.cs" %}
public ActionResult Default()
{
    return View();
}
   

{% endhighlight %}
{% endtabs %}


You can close the options pane by pressing `Esc` key.

## Search

The `Search` module of Document Editor exposes the following APIs:

|API Name|Type |Description|
|---|---|---|
|`findAll()` | Method |Searches for specified text in the whole document and highlights it with yellow.|
|`searchResults` |Property |This is an instance of `SearchResults`.|
|`find()` | Method |Find immediate occurrence of specified text from cursor position in the document and highlights it with yellow.|

### Find the immediate occurrence in the document

Using `find()` method, you can find the immediate occurrence of specified text from current cursor position in the document.

```typescript
documenteditor.search.find('Some text', 'None');
```

N> Second parameter is optional parameter and it denotes find Options. Possible values of find options are `'None' |'WholeWord' |'CaseSensitive'| 'CaseSensitiveWholeWord'`.

### Find all the occurrences in the document

Using `findAll()` method, you can find all the occurrences of specified text in the whole document and highlight it with yellow.

```typescript
documenteditor.search.findAll('Some text', 'None');
```

N> Second parameter is optional parameter and it denotes to find Options. Possible values of find options are `'None' |'WholeWord' |'CaseSensitive'| 'CaseSensitiveWholeWord'`.

## Search results

The `SearchResults` class provides information about the search results after search operation is completed that can be identified using the `searchResultsChange` event. This will expose the following APIs:

|API Name|Type |Description|
|---|---|---|
|`length` |Property|Returns the total number of results found on the search.|
|`index` |Property|Returns the index of selected search result. You can change the value for this property to move the selection.|
|`replaceAll()` |Method|Replaces all the occurrences with specified text.|
|`clear()` |Method|Clears the search result.|

### Replace all the occurrences

Using `replaceAll`, you can replace all the occurrences with specified text.

```typescript
documentEditor.search.findAll ('Some text');
// Replace all the searched text with word 'Mike'
documentEditor.search.searchResults.replaceAll("Mike");  
```

### Replace

Using `insertText`, you can replace the current searched text with specified text and it replaces single occurrence.

N>Note: This `insertText` API accepts following control characters.
<br/>* New line characters ("\r", "\r\n", "\n") - Inserts a new paragraph and appends the remaining text to the new paragraph.
<br/>* Line break character ("\v") - Moves the remaining text to start in new line.
<br/>* Tab character ("\t") - Allocates a tab space and continue the next character.

```typescript
container.documentEditor.search.findAll('works');

let searchLength: number = container.documentEditor.search.searchResults.length;

for (let i = searchLength - 1; i >= 0; i--) {
  // It will move selection to specific searched index,move to each occurrence one by one
  container.documentEditor.search.searchResults.index = i;
  // Replace it with some text
  container.documentEditor.editor.insertText('Hello');
}

container.documentEditor.search.searchResults.clear();
```

## SearchResultsChange event

`DocumentEditor` exposes the `searchResultsChangeâ`event that will be triggered whenever search results are changed. Consider the following scenarios:

* A search operation is completed with some results.
* The results are replaced with some other text, since it will be cleared automatically.
* The results are cleared explicitly.

```typescript
documenteditor.searchResultsChange = function() {

};
```

## Customize find and replace

Using the exposed APIs, you can customize the find and replace functionality in your application.


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-button id="replace_all">Replace All</ejs-button>
<div id="documenteditor" style="width:100%;height:100%" >
    <ejs-documenteditor isReadOnly=false enableEditor=true enableSelection=true enableSearch=true id="container"></ejs-documenteditor>
</div>

<script>
    var documenteditor;
    document.addEventListener('DOMContentLoaded', function () {
        documenteditor = document.getElementById("container").ej2_instances[0];
        var sfdt = {
            "sections": [
                {
                    "blocks": [
                        {
                            "inlines": [
                                {
                                    "characterFormat": {
                                        "bold": true,
                                        "italic": true
                                    },
                                    "text": "Adventure Works Cycles, the fictitious company on which the AdventureWorks sample databases are based, is a large, multinational manufacturing company. The company manufactures and sells metal and composite bicycles to North American, European and Asian commercial markets. While its base operation is located in Bothell, Washington with 290 employees, several regional sales teams are located throughout their market base."
                                }
                            ]
                        }
                    ]
                }
            ]
        };
        documenteditor.open(JSON.stringify(sfdt));

        document.getElementById('replace_all').addEventListener('click', function () {
            var textToFind = document.getElementById('find_text').value;
            var textToReplace = document.getElementById('replace_text').value;
            if (textToFind !== '') {
                // Find all the occurences of given text
                documenteditor.searchModule.findAll(textToFind);
                if (documenteditor.searchModule.searchResults.length > 0) {
                    // Replace all the occurences of given text
                    documenteditor.searchModule.searchResults.replaceAll(textToReplace);
                }
            }
        });
    });
</script>
{% endhighlight %}
{% highlight c# tabtitle="Find-replace.cs" %}
public ActionResult Default()
{
    return View();
}
   

{% endhighlight %}
{% endtabs %}


## See Also

* [Options pane](../asp-net-core/dialog#options-pane)
* [Feature modules](../asp-net-core/feature-module)
