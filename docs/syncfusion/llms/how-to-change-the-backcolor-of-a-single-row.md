# Source: https://docs.syncfusion.com/windowsforms/classic/databoundgrid/how-to/how-to-change-the-backcolor-of-a-single-row.md

# Source: https://docs.syncfusion.com/windowsforms/grid-control/how-to/appearance/how-to-change-the-backcolor-of-a-single-row.md

# How to change the BackColor of a single row

GridControl.RowStyles collection contains [GridStyleInfo](/windowsforms/Grid/Cell-Style-Architecture#gridstyleinfo-class-overview) objects that provide row style settings for the GridControl. Changing the properties on a particular RowStyle will affect all the cells in that row (unless a particular cell has a more specific style setting, like a [CellStyle](/windowsforms/Grid/Cell-Style-Architecture#properties), applied).

{% tabs %}
{% highlight c# %}

//Sets the BackColor of the 3rd row.
gridControl1.RowStyles[3].BackColor = Color.Red;
{% endhighlight  %}

{% highlight vb %}
'Sets the BackColor of the 3rd row.
GridControl1.RowStyles(3).BackColor = Color.Red

{% endhighlight  %}
{% endtabs %}