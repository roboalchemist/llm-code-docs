# Source: https://docs.syncfusion.com/windowsforms/gridgrouping/faq/summaries/how-to-retrieve-a-summary-item.md

# How to Retrieve a Summary Item

The following code shows how to retrieve a summary item.

{% tabs %}
{% highlight c# %}

//summaryColumnDescriptor is GridSummaryColumnDescriptor. 
string item=GridEngine.GetSummaryText(this.gridGroupingControl1.Table.TopLevelGroup,summaryColumnDescriptor)

{% endhighlight  %}

{% highlight vb %}

'summaryColumnDescriptor is GridSummaryColumnDescriptor. 
Dim item As String = GridEngine.GetSummaryText(Me.gridGroupingControl1.Table.TopLevelGroup, summaryColumnDescriptor)

{% endhighlight  %}
{% endtabs %}