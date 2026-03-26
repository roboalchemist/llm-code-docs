# Source: https://docs.syncfusion.com/windowsforms/gridgrouping/faq/records/how-to-access-unfiltered-records.md

# How to Access Unfiltered Records

This can be done using the following code snippet.

{% tabs %}
{% highlight c# %}

foreach(Record r in this.gridGroupingControl1.Table.Records)
{
    foreach(Record fr in this.gridGroupingControl1.Table.FilteredRecords)
    {
        if(r!=fr)
        {
            Console.WriteLine(r.Info);
        }
    }
}

{% endhighlight %}

{% highlight vb %}

For Each r As Record In Me.gridGroupingControl1.Table.Records
For Each fr As Record In Me.gridGroupingControl1.Table.FilteredRecords
If Not r Is fr Then
    Console.WriteLine(r.Info)
End If
Next fr
Next r

{% endhighlight %}
{% endtabs %}
