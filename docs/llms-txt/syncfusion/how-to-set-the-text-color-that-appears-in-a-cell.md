# Source: https://docs.syncfusion.com/windowsforms/grid-control/how-to/appearance/how-to-set-the-text-color-that-appears-in-a-cell.md

# How to set the text color that appears in a cell

Harnessing the ability to customize text color to your application allows you endless possibilities. Use the TextColor property of cells style and set it to color value.

{% tabs %}
{% highlight c# %}

//Modifies the TextColor of a cell.
gridControl1[rowIndex, colIndex].TextColor = Color.Red;
{% endhighlight  %}

{% highlight vb %}
'Modifies the TextColor of a cell.
GridControl1(rowIndex, colIndex).TextColor = Color.Red
{% endhighlight  %}
{% endtabs %}