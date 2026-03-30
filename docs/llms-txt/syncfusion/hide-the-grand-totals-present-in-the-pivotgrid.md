# Source: https://docs.syncfusion.com/wpf/pivot-grid/how-to/hide-the-grand-totals-present-in-the-pivotgrid.md

# How to hide the Grand Total present in the PivotGrid?

It can be achieved by setting the property `ShowGrandTotals` to false. By default, PivotGrid displays Grand Total for both column and row headers. 
It can be mentioned either in *XAML* or in *Code-Behind*.

If through *XAML*, please refer the below code sample.

{% highlight xaml %}

    <Grid>
       <syncfusion:PivotGridControl x:Name="pivotGrid" ShowGrandTotals="False">
       </syncfusion:PivotGridControl>
    </Grid>

{% endhighlight %}

Else if through *Code-Behind*, please refer the below code sample.

{% highlight C# %}

    public MainWindow()
        {
            InitializeComponent();
            this.pivotGrid.ShowGrandTotals = false;
        }

{% endhighlight %}
