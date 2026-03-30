# Source: https://docs.syncfusion.com/windowsforms/classic/databoundgrid/how-to/how-to-set-the-width-of-a-column.md

# Source: https://docs.syncfusion.com/windowsforms/grid-control/how-to/managing-rows-and-columns/how-to-set-the-width-of-a-column.md

# How to set the width of a column

Changing a column's width is simple whether you are using the designer or code. In the designer, use ColWidthsEntries collection. In code, use GridControl.ColWidths collection to specify the width of a column. 

{% tabs %}
{% highlight c# %}

//Sets size of column 3 to 250.
this.gridControl1.ColWidths[3] = 250;

{% endhighlight  %}

{% highlight vb %}

'Sets size of column 3 to 250.
Me.GridControl1.ColWidths(3) = 250 

{% endhighlight  %}
{% endtabs %}