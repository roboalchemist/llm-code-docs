# Source: https://docs.syncfusion.com/windowsforms/gridgrouping/faq/selections/how-to-select-a-record-programmatically.md

# How to Select a Record programmatically

The following code illustrates how to select a record programmatically.

{% tabs %}
{% highlight c# %}

//Selects the 3rd record.
this.gridGroupingControl1.Table.SelectedRecords.Add(this.gridGroupingControl1.Table.Records[3]);

{% endhighlight %}

{% highlight vb %}

'Selects the 3rd record.
Me.gridGroupingControl1.Table.SelectedRecords.Add(Me.gridGroupingControl1.Table.Records(3))

{% endhighlight %}
{% endtabs %}