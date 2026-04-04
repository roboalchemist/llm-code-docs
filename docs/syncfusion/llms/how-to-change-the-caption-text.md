# Source: https://docs.syncfusion.com/windowsforms/gridgrouping/faq/general/how-to-change-the-caption-text.md

# How to Change the Caption Text

This can be done using the code below.

{% tabs %}
{% highlight C# %}

// Sets the caption text.

// {TableName} - Displays the CaptionSection.ParentTableDescriptor.Name

//{CategoryName} - Displays the CaptionSection.ParentGroup.Name

//{Category} - Displays the CaptionSection.ParentGroup.Category

//{RecordCount} - Displays the CaptionSection.ParentGroup.GetFilteredRecordCount()
this.gridGroupingControl1.TopLevelGroupOptions.CaptionText = "TableName is {TableName} : {Category} : {RecordCount}";

{% endhighlight %}

{% highlight vb %}

'Sets the caption text.

' {TableName} - Displays the CaptionSection.ParentTableDescriptor.Name

'{CategoryName} - Displays the CaptionSection.ParentGroup.Name

'{Category} - Displays the CaptionSection.ParentGroup.Category

'{RecordCount} - Displays the CaptionSection.ParentGroup.GetFilteredRecordCount()
Me.gridGroupingControl1.TopLevelGroupOptions.CaptionText = "TableName is {TableName} : {Category} : {RecordCount}"

{% endhighlight %}
{% endtabs %}
