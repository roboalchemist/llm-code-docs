# Source: https://docs.syncfusion.com/windowsforms/grid-control/how-to/cell-styles/how-to-make-a-cell-display-if-it-is-not-wide-enough.md

# How to make a cell display '...' if it is not wide enough

You must set GridStyleInfo'sTrimming property to achieve this. To enable trimming for the whole grid, set this property in TableStyle. To enable trimming on a column, row, or cell basis, set this style property using techniques that are appropriate for the grid that you are using as discussed in the topics on changing BackColor.

{% tabs %}
{% highlight c# %}

//Sets Ellipsis Text for the whole grid.
this.grid.TableStyle.Trimming = StringTrimming.EllipsisWord;

{% endhighlight %}

{% highlight vb %}

'Sets Ellipsis Text for the whole grid.
Me.grid.TableStyle.Trimming = StringTrimming.EllipsisWord

{% endhighlight %}
{% endtabs %}
