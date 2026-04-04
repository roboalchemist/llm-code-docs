# Source: https://docs.syncfusion.com/windowsforms/gridgrouping/faq/records/how-to-access-sorted-or-filtered-records.md

# How to Access Sorted or Filtered Records

This can be done using the following code snippet.

{% tabs %}
{% highlight c# %}

//Loops through the filtered records.
foreach(Record fr in this.gridGroupingControl1.Table.FilteredRecords)
{
    Console.WriteLine(fr.Info);
}

{% endhighlight %}

{% highlight vb %}

'Loops through the filtered records.
For Each fr As Record In Me.gridGroupingControl1.Table.FilteredRecords
    Console.WriteLine(fr.Info)
Next fr

{% endhighlight %}
{% endtabs %}
