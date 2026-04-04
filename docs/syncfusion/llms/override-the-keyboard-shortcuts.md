# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es6/how-to/override-the-keyboard-shortcuts.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/javascript-es5/how-to/override-the-keyboard-shortcuts.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/vue/how-to/override-the-keyboard-shortcuts.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/react/how-to/override-the-keyboard-shortcuts.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/angular/how-to/override-the-keyboard-shortcuts.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-mvc/how-to/override-the-keyboard-shortcuts.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/asp-net-core/how-to/override-the-keyboard-shortcuts.md

# How to override the keyboard shortcuts in document editor

Document editor triggers the [`keyDown`](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.DocumentEditor.DocumentEditor.html#Syncfusion_EJ2_DocumentEditor_DocumentEditor_KeyDown) event every time when any key is entered and provides an instance of `DocumentEditorKeyDownEventArgs`. You can use the `isHandled` property to override the keyboard shortcut behavior.

## Preventing default keyboard shortcut

The following code shows how to prevent the `CTRL + C` keyboard shortcut for copying selected content in document editor.


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-documenteditor isReadOnly=false enableEditor=true enableSelection=true id="container"></ejs-documenteditor>

<script>
    var documenteditor;
    document.addEventListener('DOMContentLoaded', function () {
        documenteditor = document.getElementById("container").ej2_instances[0];
        documentEditor.keyDown = function (args) {
            var keyCode = args.event.which || args.event.keyCode;
            var isCtrlKey = (args.event.ctrlKey || args.event.metaKey) ? true : ((keyCode === 17) ? true : false);
            //67 is the character code for 'C'
            if (isCtrlKey && keyCode === 67) {
                //To prevent copy operation set isHandled to true
                args.isHandled = true;
            }
        }
    });
</script>
{% endhighlight %}
{% highlight c# tabtitle="Prevent-default.cs" %}
{% endhighlight %}{% endtabs %}


## Override or define the keyboard shortcut

Override or define a new keyboard shortcut behavior instead of preventing the keyboard shortcut.

For example, `Ctrl + S` keyboard shortcut saves the document in SFDT format by default, and there is no behavior for `Ctrl + Alt + S`. The following code demonstrates how to override the `Ctrl + S` shortcut to save a document in DOCX format and define `Ctrl + Alt + S` to save the document in SFDT format.


{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-documenteditor isReadOnly=false enableEditor=true enableSelection=true enableWordExport=true enableSfdtExport=true id="container"></ejs-documenteditor>

<script>
    var documenteditor;
    document.addEventListener('DOMContentLoaded', function () {
        documenteditor = document.getElementById("container").ej2_instances[0];
        documentEditor.keyDown = function (args) {
            var keyCode = args.event.which || args.event.keyCode;

            var isCtrlKey = (args.event.ctrlKey || args.event.metaKey) ? true : ((keyCode === 17) ? true : false);

            var isAltKey = args.event.altKey ? args.event.altKey : ((keyCode === 18) ? true : false);

            // 83 is the character code for 'S'
            if (isCtrlKey && !isAltKey && keyCode === 83) {
                //To prevent default save operation, set the isHandled property to true
                args.isHandled = true;
                documentEditor.save('sample', 'Docx');
                args.event.preventDefault();
            } else if (isCtrlKey && isAltKey && keyCode === 83) {
                documentEditor.save('sample', 'Sfdt');
            }
        }
    });
</script>
{% endhighlight %}
{% highlight c# tabtitle="Override.cs" %}
{% endhighlight %}{% endtabs %}

