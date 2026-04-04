# Source: https://docs.syncfusion.com/windowsforms/gridgrouping/faq/groups/how-to-apply-grouping-properties-for-toplevelgroup.md

# How to Apply Grouping Properties for TopLevelGroups

Grouping properties for TopLevelGroups can be applied using the code snippet below.

{% tabs %}
{% highlight c# %}

//Hides the AddNewRecord field before details row.
this.gridGroupingControl1.TableDescriptor.TopLevelGroupOptions.ShowAddNewRecordBeforeDetails=false;

//Hides the Header cells.
this.gridGroupingControl1.TableDescriptor.TopLevelGroupOptions.ShowColumnHeaders=false;

//Adds the Filter Bar to the Child level groups.
this.gridGroupingControl1.TableDescriptor.TopLevelGroupOptions.ShowFilterBar=true;

//Sets the caption.
this.gridGroupingControl1.TableDescriptor.TopLevelGroupOptions.CaptionText="Custom";

//Shows the group footer.
this.gridGroupingControl1.TableDescriptor.TopLevelGroupOptions.ShowGroupFooter=true;

{% endhighlight  %}

{% highlight vb %}

'Hides the AddNewRecord before details.
Me.gridGroupingControl1.TableDescriptor.TopLevelGroupOptions.ShowAddNewRecordBeforeDetails=False

'Hides the column headers.
Me.gridGroupingControl1.TableDescriptor.TopLevelGroupOptions.ShowColumnHeaders=False

'Adds the Filter Bar to the Top level groups.
Me.gridGroupingControl1.TableDescriptor.TopLevelGroupOptions.ShowFilterBar=True

'Sets the caption.
Me.gridGroupingControl1.TableDescriptor.TopLevelGroupOptions.CaptionText="Custom"

'Shows the group footer.
Me.gridGroupingControl1.TableDescriptor.TopLevelGroupOptions.ShowGroupFooter=True

{% endhighlight  %}
{% endtabs %}
