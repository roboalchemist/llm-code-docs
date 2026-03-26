# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es6/list-format.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es5/list-format.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/vue/list-format.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/react/list-format.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/blazor/list-format.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/angular/list-format.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-mvc/list-format.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-core/list-format.md

# Working with Lists

Document editor supports both the single-level and multilevel lists. Lists are used to organize data as step-by-step instructions in documents for easy understanding of key points. You can apply list to the paragraph either using supported APIs.

## Create bullet list

Bullets are usually used for unordered lists. To apply bulleted list for selected paragraphs, use the following method of âEditorâ instance.

N> applyBullet(bullet, fontFamily);

|Parameter|Type|Description|
|---------|----|-----------|
|Bullet|string|Bullet character.|
|fontFamily|string|Bullet font family.|

```typescript
documenteditor.editor.applyBullet('\uf0b7', 'Symbol');
```

## Create numbered list

Numbered lists are usually used for ordered lists. To apply numbered list for selected paragraphs, use the following method of âEditorâ instance.

N> applyNumbering(numberFormat,listLevelPattern)

|Parameter|Type|Description|
|---------|----|-----------|
|numberFormat|string|â%nâ representations in ânumberFormatâ parameter will be replaced by respective list levelâs value.â%1)â will be displayed as â1)â|
|listLevelPattern(optional)|string|Default value is 'Arabic'.|

```typescript
documenteditor.editor.applyNumbering('%1)', 'UpRoman');
```

## Clear list

You can also clear the list formatting applied for selected paragraphs.

```typescript
documenteditor.editor.clearList();
```

## Working with lists


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<div id="toolbar">
    <ejs-toolbar clicked="toolbarAction">
        <e-toolbar-items>
            <e-toolbar-item prefixIcon=" e-de-icon-Bullets " id="Bullets " tooltipText="Bullets "></e-toolbar-item>
            <e-toolbar-item prefixIcon="e-de-icon-Numbering " id="Numbering " tooltipText="Numbering "></e-toolbar-item>
            <e-toolbar-item text="Clear " tooltipText="Clear List " id="clearlist "></e-toolbar-item>
        </e-toolbar-items>
    </ejs-toolbar>
</div>
<div id="documenteditor " style="width:100%;height:100% ">
    <ejs-documenteditor isReadOnly=false enableEditor=true enableSelection=true enableSfdtExport=true enableEditor=true id="container "></ejs-documenteditor>
</div>

<script>
    var documenteditor;
    document.addEventListener('DOMContentLoaded', function () {
        documenteditor = document.getElementById("container ").ej2_instances[0];
        documenteditor.resize();
        updateContainerSize();

        function toolbarAction(args) {
            switch (args.item.id) {
                case 'Bullets':
                    //To create bullet list
                    documenteditor.editor.applyBullet('\uf0b7', 'Symbol');
                    break;
                case 'Numbering':
                    //To create numbering list
                    documenteditor.editor.applyNumbering('%1)', 'UpRoman');
                    break;
                case 'clearlist':
                    //To clear list
                    documenteditor.editor.clearList();
                    break;
            }
        };
    });
</script>
{% endhighlight %}
{% highlight c# tabtitle="List.cs" %}
{% endhighlight %}{% endtabs %}



## Editing numbered list

Document editor restarts the numbering or continue numbering for a numbered list. These options are found in the built-in context menu, if the list value is selected.

![Image](images/list.JPG)

## See Also

* [List dialog](../asp-net-core/dialog#list-dialog)
