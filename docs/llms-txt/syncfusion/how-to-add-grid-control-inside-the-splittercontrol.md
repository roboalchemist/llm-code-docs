# Source: https://docs.syncfusion.com/windowsforms/splitter/faq/how-to-add-grid-control-inside-the-splittercontrol.md

# How to add Grid control inside the SplitterControl

The SplitterControl can be embedded with Grid control and the following code example allows addition of a Grid inside the SplitterControl.

{% tabs %}

{% highlight C# %}



privateÂ Syncfusion.Windows.Forms.Grid.GridControlÂ gridControl1;

this.gridControl1 = new Syncfusion.Windows.Forms.Grid.GridControl();

this.gridControl1.ColCount = 10;

this.gridControl1.RowCount = 100;

this.splitterControl1.Controls.Add(this.gridControl1);

{% endhighlight %}

{% highlight VB %}



Private WithEventsÂ gridControl1Â AsÂ GridControl

Me.gridControl1 =Â NewÂ Syncfusion.Windows.Forms.Grid.GridControl()

Me.gridControl1.ColCount = 10

Me.gridControl1.RowCount = 100

Me.splitterControl1.Controls.Add(Me.gridControl1)

{% endhighlight %}

{% endtabs %}