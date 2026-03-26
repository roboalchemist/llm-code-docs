# Source: https://docs.syncfusion.com/windowsforms/gridgrouping/faq/summaries/how-to-format-summary-rows.md

# How to Format Summary Rows

The following code shows how to format summary rows.

{% tabs %}
{% highlight c# %}

//summaryColumnDescriptor is GridSummaryColumnDescriptor. 

//Changes the backcolor of the SummaryFieldCell.
summaryColumnDescriptor.Appearance.SummaryFieldCell.BackColor = Color.LightBlue;

//Changes the type of SummaryFieldCell.
summaryColumnDescriptor.Appearance.SummaryFieldCell.CellType = "ComboBox";

{% endhighlight  %}

{% highlight vb %}

'summaryColumnDescriptor is GridSummaryColumnDescriptor. 

'Changes the backcolor of the SummaryFieldCell.
summaryColumnDescriptor.Appearance.SummaryFieldCell.BackColor = Color.LightBlue

'Changes the type of SummaryFieldCell.
summaryColumnDescriptor.Appearance.SummaryFieldCell.CellType = "ComboBox"

{% endhighlight  %}
{% endtabs %}