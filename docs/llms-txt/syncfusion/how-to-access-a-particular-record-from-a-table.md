# Source: https://docs.syncfusion.com/windowsforms/gridgrouping/faq/records/how-to-access-a-particular-record-from-a-table.md

# How to Access a Particular Record from a Table

This can be done using the following code snippet.

{% tabs %}
{% highlight c# %}

//Uses the record Index to access a particular record from a table.
Record r=this.gridGroupingControl1.Table.Records[RecordIndex];

{% endhighlight %}

{% highlight vb %}

'Uses the record Index to access a particular record from a table.
Dim r As Record = Me.gridGroupingControl1.Table.Records(RecordIndex)

{% endhighlight %}
{% endtabs %}
