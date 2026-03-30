# Source: https://docs.syncfusion.com/windowsforms/gridgrouping/faq/general/how-to-group-a-column-programmatically.md

# How to Group a Column Programmatically

To group a column programmatically, use the following code.

{% tabs %}
{% highlight C# %}

//Shows the GroupDropArea.
this.gridGroupingControl1.ShowGroupDropArea = true;

//Groups by "Col1".
this.gridGroupingControl1.TableDescriptor.GroupedColumns.Add("Col1", ListSortDirection.Ascending);

{% endhighlight %}

{% highlight vb %}

'Shows the GroupDropArea.
Me.gridGroupingControl1.ShowGroupDropArea = True

'Groups by "Col1".
Me.gridGroupingControl1.TableDescriptor.GroupedColumns.Add("Col1", ListSortDirection.Ascending)

{% endhighlight %}
{% endtabs %}
