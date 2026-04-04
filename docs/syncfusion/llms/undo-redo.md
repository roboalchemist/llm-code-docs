# Source: https://docs.syncfusion.com/windowsforms/grid-control/undo-redo.md

# Source: https://docs.syncfusion.com/windowsforms/diagram/undo-redo.md

# Source: https://docs.syncfusion.com/wpf/image-editor/undo-redo.md

# Source: https://docs.syncfusion.com/maui/imageeditor/undo-redo.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/javascript-es6/undo-redo.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/javascript-es5/undo-redo.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/vue/undo-redo.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/react/undo-redo.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/blazor/undo-redo.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/angular/undo-redo.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/asp-net-mvc/undo-redo.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/asp-net-core/undo-redo.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/wpf/undo-redo.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/uwp/undo-redo.md

# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/flutter/undo-redo.md

# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/maui/undo-redo.md

# Undo and Redo in .NET MAUI PDF Viewer (SfPdfViewer)

If you performed any undesired actions when adding, removing, moving, resizing or editing annotations, you can undo and redo the action to restore the previous state. This section will go through how to perform the undo and redo the changes made on the annotations.

For desktop platforms such as Windows and macOS, you can also use the following shortcut keys to perform the actions.

<table>
<tr>
<th>Action & Shortcut keys</th>
<th>Windows</th>
<th>macOS</th>
</tr>
<tr>
<th>Undo</th>
<td><code>Ctrl</code> + <code>z</code></td>
<td><code>Command</code> + <code>z</code></td>
</tr>
<tr>
<th>Redo</th>
<td><code>Ctrl</code> + <code>y</code></td>
<td><code>Command</code> + <code>y</code></td>
</tr>
</table>

## Undo

You can perform undo to reverse the most recent action performed on the annotations using the [UndoCommand](https://help.syncfusion.com/cr/maui/Syncfusion.Maui.PdfViewer.SfPdfViewer.html#Syncfusion_Maui_PdfViewer_SfPdfViewer_UndoCommand) of the [SfPdfViewer](https://help.syncfusion.com/cr/maui/Syncfusion.Maui.PdfViewer.SfPdfViewer.html). The following code examples explain how to bind the command to a button in XAML to perform the action on button click, and also execute the command programmatically as well.

{% tabs %}
{% highlight XAML %}
<syncfusion:SfPdfViewer x:Name="PdfViewer"/>
<Button x:Name="Undo" Command="{Binding Path=UndoCommand,Source={x:Reference PdfViewer}}"/>
{% endhighlight %}
{% highlight C# %}
void PerformUndo()
{
    // Undo the last operation using the UndoCommand of `SfPdfViewer` instance.
    PdfViewer.UndoCommand.Execute(true);
}
{% endhighlight %}
{% endtabs %}

## Redo

You can perform redo to restore the last undone function using the [RedoCommand](https://help.syncfusion.com/cr/maui/Syncfusion.Maui.PdfViewer.SfPdfViewer.html#Syncfusion_Maui_PdfViewer_SfPdfViewer_RedoCommand) of the [SfPdfViewer](https://help.syncfusion.com/cr/maui/Syncfusion.Maui.PdfViewer.SfPdfViewer.html).. The following code examples explains how to bind the command to a button in XAML to perform the action on button click and also executing the command programmatically as well.

{% tabs %}
{% highlight XAML %}
<syncfusion:SfPdfViewer x:Name="PdfViewer"/>
<Button x:Name="Redo" Command="{Binding Path=RedoCommand,Source={x:Reference PdfViewer}}"/>{% endhighlight %}
{% highlight C# %}
void PerformRedo()
{
    // Redo the last operation using the RedoCommand of `SfPdfViewer` instance.
    PdfViewer.RedoCommand.Execute(true);
}
{% endhighlight %}
{% endtabs %}