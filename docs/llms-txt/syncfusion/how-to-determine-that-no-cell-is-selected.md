# Source: https://docs.syncfusion.com/windowsforms/classic/databoundgrid/how-to/how-to-determine-that-no-cell-is-selected.md

# How to Determine that No Cell is Selected

This page explains How to Determine that No Cell is Selected and more details.

## How to Determine that No Cell is Selected

To determine whether the cell is selected or not, use GetSelectedRange method. It returns the list with selected range. If it returns the range as zero, then no cell is selected.

* ranges - It sets the range of cells to be selected.
* ConsiderCurrentCell

True - If the current cell should be treated as selected range.

{% tabs %}
{% highlight c# %}

GridRangeInfoList rangeList = null;
this.gridDataBoundGrid1.Selections.GetSelectedRanges(out rangeList, false);

if (rangeList.Count == 0)
{
    Console.WriteLine("no selection");
}

{% endhighlight %}

{% highlight vb %}

Dim rangeList As GridRangeInfoList = Nothing
Me.gridDataBoundGrid1.Selections.GetSelectedRanges(rangeList,False)
If rangeList.Count = 0 Then
Console.WriteLine("no Selection")
End If

{% endhighlight %}
{% endtabs %}

