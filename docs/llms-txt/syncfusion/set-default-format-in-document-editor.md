# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es6/how-to/set-default-format-in-document-editor.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es5/how-to/set-default-format-in-document-editor.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/vue/how-to/set-default-format-in-document-editor.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/react/how-to/set-default-format-in-document-editor.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/angular/how-to/set-default-format-in-document-editor.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-mvc/how-to/set-default-format-in-document-editor.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-core/how-to/set-default-format-in-document-editor.md

# How to set the default character, paragraph and section format in Document Editor component

You can set the default character format, paragraph format and section format in Document editor.

## Set the default character format

You can use `setDefaultCharacterFormat` method to set the default character format. For example, Document editor default font size is 11 and you can change it as any valid value.


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
        container.documentEditor.setDefaultCharacterFormat({fontSize: 20});
    }
</script>


{% endhighlight %}
{% highlight c# tabtitle="Character-format-font.cs" %}
{% endhighlight %}{% endtabs %}


Similarly, you can change the required `CharacterFormatProperties` default value.

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
        var defaultCharacterFormat = {
            bold: false,
            italic: false,
            baselineAlignment: 'Normal',
            underline: 'None',
            fontColor: "#000000",
            fontFamily: 'Algerian',
            fontSize: 12
        };
        container.documentEditor.setDefaultCharacterFormat(defaultCharacterFormat);
    }
</script>


{% endhighlight %}
{% highlight c# tabtitle="Character-format.cs" %}
{% endhighlight %}{% endtabs %}


## Set the default paragraph format

You can use `setDefaultParagraphFormat` API to set the default paragraph format. You can change the required `ParagraphFormatProperties` default value.


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
        var defaultParagraphFormat = {
            beforeSpacing: 8,
            lineSpacing: 1.5,
            leftIndent: 24,
            textAlignment: "Center"
        };
        container.documentEditor.setDefaultParagraphFormat(defaultParagraphFormat);
    }
</script>


{% endhighlight %}
{% highlight c# tabtitle="Paragraph-format.cs" %}
{% endhighlight %}{% endtabs %}



## Set the default section format

You can use `setDefaultSectionFormat` API to set the default section format. You can change the required `SectionFormatProperties` default value.


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
        var defaultSectionFormat = {
            pageWidth: 500,
            pageHeight: 800,
            headerDistance: 56,
            footerDistance: 48,
            leftMargin: 12,
            rightMargin: 12,
            topMargin:0,
            bottomMargin:0
        };
        container.documentEditor.setDefaultSectionFormat(defaultSectionFormat);
    }
</script>


{% endhighlight %}
{% highlight c# tabtitle="Section-format.cs" %}
{% endhighlight %}{% endtabs %}

