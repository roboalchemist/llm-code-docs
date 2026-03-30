# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/javascript-es6/how-to/identify-the-context-menu-opened.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/javascript-es5/how-to/identify-the-context-menu-opened.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/vue/how-to/identify-the-context-menu-opened.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/react/how-to/identify-the-context-menu-opened.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/angular/how-to/identify-the-context-menu-opened.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/asp-net-mvc/how-to/identify-the-context-menu-opened.md

# Source: https://docs.syncfusion.com/document-processing/excel/spreadsheet/asp-net-core/how-to/identify-the-context-menu-opened.md

# Identify the context menu opened in ASP.NET Core Spreadsheet control

The Spreadsheet includes several context menus that will open and display depending on the action. When you right-click on a cell, for example, a context menu with options related to the cell element appears.

The class name returned by the [contextMenuBeforeOpen](https://help.syncfusion.com/cr/aspnetcore-js2/Syncfusion.EJ2.Spreadsheet.Spreadsheet.html#Syncfusion_EJ2_Spreadsheet_Spreadsheet_ContextMenuBeforeOpen) event can be used to identify the context menu that is opened. The context menus and their class names are tabulated below.

| Class name | Context menu name |
|-------|---------|
| .e-sheet-content | Cell context menu |
| .e-toolbar-item | Footer context menu |
| .e-rowhdr-table | Row header context menu |
| .e-colhdr-table | Column header context menu |

The following code example shows how to identify the context menu opened.

{% tabs %}
{% highlight cshtml tabtitle="CSHTML" %}
<ejs-spreadsheet id="spreadsheet" contextMenuBeforeOpen="contextMenuBeforeOpen">

</ejs-spreadsheet>

<script>

    function contextMenuBeforeOpen(args) {
        if (ejs.base.closest(args.event.target, '.e-sheet-content')) {
            console.log('Cell Context Menu');
        } else if (ejs.base.closest(args.event.target, '.e-colhdr-table')) {
            console.log('Column Header Context Menu');
        } else if (ejs.base.closest(args.event.target, '.e-rowhdr-table')) {
            console.log('Row Header Context Menu');
        } else if (ejs.base.closest(args.event.target, '.e-toolbar-item')) {
            console.log('Footer Context Menu');
        }
    }

</script>
{% endhighlight %}
{% endtabs %}

