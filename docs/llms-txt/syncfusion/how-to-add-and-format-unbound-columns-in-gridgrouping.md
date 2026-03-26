# Source: https://docs.syncfusion.com/windowsforms/gridgrouping/faq/general/how-to-add-and-format-unbound-columns-in-gridgrouping.md

# How to Add and Format Unbound Columns in GridGrouping Control

The unbound columns can be added and formatted using the below code.

{% tabs %}
{% highlight C# %}

//Adds unbound column in GridGroupingControl.
this.gridGroupingControl1.TableDescriptor.UnboundFields.Add("UnboundColumn1");

//Formats the Unbound column.
this.gridGroupingControl1.TableDescriptor.Columns["UnboundColumn1"].Appearance.AnyRecordFieldCell.CellType = "CheckBox";
this.gridGroupingControl1.TableDescriptor.Columns["UnboundColumn1"].Appearance.AnyRecordFieldCell.BackColor = Color.LightSteelBlue;

{% endhighlight %}

{% highlight vb %}

'Adds an Unbound column in a  GridGroupingControl.
Me.gridGroupingControl1.TableDescriptor.UnboundFields.Add("UnboundColumn1")

'Formats an Unbound column in GridGroupingControl.
Me.gridGroupingControl1.TableDescriptor.Columns("UnboundColumn1").Appearance.AnyRecordFieldCell.CellType = "CheckBox"
Me.gridGroupingControl1.TableDescriptor.Columns("UnboundColumn1").Appearance.AnyRecordFieldCell.BackColor = Color.LightSteelBlue

{% endhighlight %}
{% endtabs %}
