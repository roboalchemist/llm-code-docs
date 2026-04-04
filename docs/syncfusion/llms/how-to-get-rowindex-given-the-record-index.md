# Source: https://docs.syncfusion.com/windowsforms/gridgrouping/faq/records/how-to-get-rowindex-given-the-record-index.md

# How to Get Row Index Given the Record Index

This can be done using the following code snippet.

{% tabs %}
{% highlight c# %}

int position = gridGroupingControl1.Table.DisplayElements.IndexOf(record);

{% endhighlight %}

{% highlight vb %}

Dim position As Integer = gridGroupingControl1.Table.DisplayElements.IndexOf(record)

{% endhighlight %}
{% endtabs %}
