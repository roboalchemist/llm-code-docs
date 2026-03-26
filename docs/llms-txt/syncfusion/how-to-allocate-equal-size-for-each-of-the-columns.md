# Source: https://docs.syncfusion.com/windowsforms/gridgrouping/faq/layout-and-appearance/how-to-allocate-equal-size-for-each-of-the-columns.md

# How to Allocate Equal Size for Each of the Columns in all the Tables

The parent and child table columnsâ width can be set equally in proportion to the grid control's client width by dynamically setting the columns width in TableModel.QueryColWidth event handler. When it deals with a nested table, QueryColWidth event of the entire nested table must be handled to set the respective nested table columns width. In QueryColWidth event handler, the available width for the columns can be calculated as follows,

availableArea = groupingGrid.ClientSize.Width - gridModel.ColWidths.GetTotal(0, girdModel.Cols.HeaderCount) - indentColsTotalWidth;

and the proportional columns width can be calculated as follows,

{% tabs %}
{% highlight c# %}

Size = (int) availableArea / (grid.TableDescriptor.VisibleColumns.Count);

{% endhighlight %}
{% endtabs %}