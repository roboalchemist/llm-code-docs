# Source: https://docs.syncfusion.com/windowsforms/gridgrouping/faq/layout-and-appearance/how-to-freeze-specified-columns.md

# How to Freeze Specified Columns

You can freeze Specified columns by making use of the code given below.

{% tabs %}
{% highlight c# %}

//Adds a specified column index  to freeze
this. gridGroupingControl1.TableModel.Cols.FreezeRange(1, 1);

//Adds a range of columns to freeze.
this. gridGroupingControl1.TableModel.Cols.FreezeRange(1, 3);

{% endhighlight %}

{% highlight vb %}

'Adds a specified column index  to freeze
Me. gridGroupingControl1.TableModel.Cols.FreezeRange(1, 1)

'Adds a range of columns to freeze.
Me. gridGroupingControl1.TableModel.Cols.FreezeRange(1, 3)

{% endhighlight %}
{% endtabs %}