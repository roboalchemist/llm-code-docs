# Source: https://docs.syncfusion.com/windowsforms/gridgrouping/faq/general/how-to-access-the-current-record.md

# How to Access the Current Record

To access the current record, use the following code.

{% tabs %}
{% highlight C# %}

Record rec = this.gridGroupingControl1.Table.CurrentRecord;
Trace.WriteLine(rec.ToString());

{% endhighlight %}

{% highlight vb %}

Dim rec As Record = Me.gridGroupingControl1.Table.CurrentRecord
Trace.WriteLine(rec.ToString())

{% endhighlight %}
{% endtabs %}
