# Source: https://docs.syncfusion.com/windowsforms/pivot-chart/faq/how-to-enable-drill-down-in-pivotchart.md

# How to enable drill down in PivotChart

The PivotChart has in-built support to drill up and down the PivotSeries population. This behavior can be achieved by enabling the AllowDrillDown property.

{% highlight C# %}



this.pivotChart1.AllowDrillDown = true;

{% endhighlight %}

{% highlight vbnet %}



Me.pivotChart1.AllowDrillDown = True

{% endhighlight %}

Sample: <InstalledLocation> Syncfusion\EssentialStudio\<InstalledVersion>\Windows\PivotChart.Windows\Samples\PivotChart Layout\DrillDown Demo\CS