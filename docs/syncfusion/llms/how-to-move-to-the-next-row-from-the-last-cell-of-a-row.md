# Source: https://docs.syncfusion.com/windowsforms/grid-control/how-to/managing-rows-and-columns/how-to-move-to-the-next-row-from-the-last-cell-of-a-row.md

# How to move to the next row from the last cell of a row

Set the WrapCellBehavior property to wrap a row when the Tab or Enter key is pressed.

{% tabs %}
{% highlight c# %}

//Sets WrapCellBehavior property to Wrap Row to move to the next row.
this.grid.Model.Options.WrapCellBehavior = GridWrapCellBehavior.WrapRow; 

{% endhighlight %}

{% highlight vb %}

'Sets WrapCellBehavior property to Wrap Row to move to the next row.
Me.grid.Model.Options.WrapCellBehavior = GridWrapCellBehavior.WrapRow

{% endhighlight %}
{% endtabs %}
