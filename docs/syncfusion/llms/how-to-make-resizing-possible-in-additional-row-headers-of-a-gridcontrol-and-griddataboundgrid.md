# Source: https://docs.syncfusion.com/windowsforms/grid-control/how-to/managing-rows-and-columns/how-to-make-resizing-possible-in-additional-row-headers-of-a-gridcontrol-and-griddataboundgrid.md

# Resizing possible in additional row headers in WinForms GridControl

This page explains How to make resizing possible in additional row headers of a GridControl and GridDataBoundGrid and more details.

## How to make resizing possible in additional row headers of a GridControl and GridDataBoundGrid

The resizing of additional row headers on the grid can be made possible by setting ResizeColsBehavior flag to Grid.GridResizeCellsBehavior.InsideGrid.

{% tabs %}
{% highlight c# %}

grid.ResizeColsBehavior = (((Syncfusion.Windows.Forms.Grid.GridResizeCellsBehavior.ResizeSingle
| Syncfusion.Windows.Forms.Grid.GridResizeCellsBehavior.InsideGrid)
| Syncfusion.Windows.Forms.Grid.GridResizeCellsBehavior.OutlineHeaders)
| Syncfusion.Windows.Forms.Grid.GridResizeCellsBehavior.OutlineBounds);

{% endhighlight %}

{% highlight vb %}

grid.ResizeColsBehavior = (((Syncfusion.Windows.Forms.Grid.GridResizeCellsBehavior.ResizeSingle
| Syncfusion.Windows.Forms.Grid.GridResizeCellsBehavior.InsideGrid)
| Syncfusion.Windows.Forms.Grid.GridResizeCellsBehavior.OutlineHeaders)
Dim Syncfusion.Windows.Forms.Grid.GridResizeCellsBehavior.OutlineBounds) As |

{% endhighlight %}
{% endtabs %}