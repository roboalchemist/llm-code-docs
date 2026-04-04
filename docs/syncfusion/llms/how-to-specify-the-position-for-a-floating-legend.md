# Source: https://docs.syncfusion.com/windowsforms/chart/faq/how-to-specify-the-position-for-a-floating-legend.md

# How to specify the position for a Floating Legend

When the LegendPosition property of the ChartControl is set to ChartDock.Floating, the position of the legend defaults to the top-right corner of the ChartArea. Once this is done, you can specify the coordinates via the Legend.Location property of the ChartLegend.

{% tabs %}

{% highlight c# %}

this.chartControl1.LegendPosition = ChartDock.Floating;

this.chartControl1.Legend.Location = new Point(20,20);

{% endhighlight %}

{% highlight vb %}

Me.ChartControl1.LegendPosition = ChartDock.Floating

Me.ChartControl1.Legend.Location = New Point(20,20)

{% endhighlight %}

{% endtabs %}

{% seealso %}

[Chart Legend](/windowsforms/chart/chart-legend-and-legend-items#chartlegend)

{% endseealso %}