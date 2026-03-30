# Source: https://docs.syncfusion.com/windowsforms/gridgrouping/faq/selections/how-to-access-selected-records.md

# How to Access Selected Records

The selected records can be accessed using the code snippet below.

{% tabs %}
{% highlight c# %}

//Accesses Selected records in GridGroupingControl.      
foreach(SelectedRecord rec in this.gridGroupingControl1.Table.SelectedRecords)
System.Diagnostics.Trace.WriteLine(rec.Record.Info);

{% endhighlight %}

{% highlight vb %}

'Accesses Selected records in GridGroupingControl.
For Each rec As SelectedRecord In Me.gridGroupingControl1.Table.SelectedRecords
Console.WriteLine(rec.Record.Info)
Next rec

{% endhighlight %}
{% endtabs %}

