# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es6/how-to/optimize-sfdt.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es5/how-to/optimize-sfdt.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/vue/how-to/optimize-sfdt.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/react/how-to/optimize-sfdt.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/blazor/how-to/optimize-sfdt.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/angular/how-to/optimize-sfdt.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-mvc/how-to/optimize-sfdt.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-core/how-to/optimize-sfdt.md

# How to optimize the SFDT file

Starting from version v21.1.x, the SFDT file generated in Word Processor component is optimized by default to reduce the file size. All static keys are minified, and the final JSON string is compressed. This helps reduce the SFDT file size relative to a DOCX file and provides the following benefits,
* File transfer between client and server through the internet gets faster.
* The new optimized SFDT files require less storage space than the old SFDT files.
Hence, the optimized SFDT file can't be directly manipulated as JSON string.

> This feature comes with a public API to switch between the old and new optimized SFDT format, allowing backward compatibility.

As a backward compatibility to create older format SFDT files, refer the following code changes,

<table>
<tr>
<td>Client/Server</td><td>Old Code</td><td>New Code from v21.1.x</td>
</tr>
<tr>
<td>Client-side</td>
<td>



{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}

<ejs-documenteditorcontainer id="container" serviceUrl="/api/DocumentEditor/" enableToolbar=true created="onCreated" height="590px"></ejs-documenteditorcontainer>

{% endhighlight %}
{% endtabs %}

</td>
<td>


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}

<ejs-documenteditorcontainer id="container" serviceUrl="/api/DocumentEditor/" enableToolbar=true created="onCreated" height="590px"></ejs-documenteditorcontainer>

<script>
    var container;
    function onCreated() {
        var documenteditorElement = document.getElementById("container");
        container = documenteditorElement.ej2_instances[0];
        container.documentEditorSetting = {
            optimizeSfdt: false
        };
    }
</script>


{% endhighlight %}
{% endtabs %}



</td>
</tr>
<tr>
<td>Server-side C#</td>
<td>
{% tabs %}
{% highlight C# tabtitle="C#" %}
WordDocument sfdtDocument = WordDocument.Load(stream, formatType);
string sfdt = Newtonsoft.Json.JsonConvert.SerializeObject(sfdtDocument);
{% endhighlight %}
{% endtabs %}
</td>
<td>
{% tabs %}
{% highlight C# tabtitle="C#" %}
WordDocument sfdtDocument = WordDocument.Load(stream, formatType);
sfdtDocument.OptimizeSfdt = false;
string sfdt = Newtonsoft.Json.JsonConvert.SerializeObject(sfdtDocument);
{% endhighlight %}
{% endtabs %}
</td>
</tr>
</table>

To convert from older format SFDT from a new optimized SFDT file, refer the following code example,

<table>
<tr>
<td>Client/Server</td><td>Code example</td>
</tr>
<tr>
<td>Client-side</td>
<td>


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}

<ejs-documenteditorcontainer id="container" serviceUrl="/api/DocumentEditor/" enableToolbar=true created="onCreated" height="590px"></ejs-documenteditorcontainer>

<script>
    var container;
    function onCreated() {
        var documenteditorElement = document.getElementById("container");
        container = documenteditorElement.ej2_instances[0];
        container.documentEditorSetting = {
            optimizeSfdt: false
        };
    }
</script>


{% endhighlight %}
{% endtabs %}


</td>
</tr>
<tr>
<td>Server-side C#</td>
<td>
{% tabs %}
{% highlight C# tabtitle="C#" %}
using(Syncfusion.DocIO.DLS.WordDocument docIODocument = WordDocument.Save(optimizedSfdt)) {
    sfdtDocument = WordDocument.Load(docIODocument);
    sfdtDocument.OptimizeSfdt = false;
    string oldSfdt = JsonSerializer.Serialize(sfdtDocument);
}
{% endhighlight %}
{% endtabs %}
</td>
</tr>
</table>