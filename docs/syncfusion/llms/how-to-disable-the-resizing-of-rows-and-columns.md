# Source: https://docs.syncfusion.com/windowsforms/gridgrouping/faq/general/how-to-disable-the-resizing-of-rows-and-columns.md

# How to Disable the Resizing of Rows and Columns

This can be done using the below code.

{% tabs %}
{% highlight C# %}

//Code to disable the resizing of rows.
this.gridGroupingControl1.TableModel.Options.ResizeRowsBehavior = Syncfusion.Windows.Forms.Grid.GridResizeCellsBehavior.None;

//Code to disable the column resizing.
this.gridGroupingControl1.TableModel.Options.ResizeColsBehavior = Syncfusion.Windows.Forms.Grid.GridResizeCellsBehavior.None;


{% endhighlight %}

{% highlight vb %}

'Code to disable the column resizing.
Me.gridGroupingControl1.TableModel.Options.ResizeColsBehavior = Syncfusion.Windows.Forms.Grid.GridResizeCellsBehavior.None

'Code to disable the resizing of rows.
Me.gridGroupingControl1.TableModel.Options.ResizeRowsBehavior = Syncfusion.Windows.Forms.Grid.GridResizeCellsBehavior.None

{% endhighlight %}
{% endtabs %}

