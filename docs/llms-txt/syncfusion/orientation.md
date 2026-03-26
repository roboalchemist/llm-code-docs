# Source: https://docs.syncfusion.com/uwp/menu/orientation.md

# Source: https://docs.syncfusion.com/uwp/linear-gauge/orientation.md

# Source: https://docs.syncfusion.com/uwp/bullet-graph/orientation.md

# Source: https://docs.syncfusion.com/windowsforms/tab-splitter-container/orientation.md

# Source: https://docs.syncfusion.com/windowsforms/rating-control/orientation.md

# Source: https://docs.syncfusion.com/windowsforms/bullet-graph/orientation.md

# Source: https://docs.syncfusion.com/wpf/tab-splitter/orientation.md

# Source: https://docs.syncfusion.com/wpf/range-slider/orientation.md

# Source: https://docs.syncfusion.com/wpf/linear-gauge/orientation.md

# Source: https://docs.syncfusion.com/wpf/bullet-graph/orientation.md

# Source: https://docs.syncfusion.com/maui/toolbar/orientation.md

# Source: https://docs.syncfusion.com/maui/stepprogressbar/orientation.md

# Source: https://docs.syncfusion.com/maui/pyramid-charts/orientation.md

# Source: https://docs.syncfusion.com/maui/funnel-charts/orientation.md

# Orientation in .NET MAUI Funnel Chart

The rendering direction of the funnel chart can be changed using the [Orientation](https://help.syncfusion.com/cr/maui/Syncfusion.Maui.Charts.SfFunnelChart.html#Syncfusion_Maui_Charts_SfFunnelChart_Orientation) property. The default value of this property is Vertical, which arranges segments from bottom to top, and it can be set to Horizontal to render segments from right to left.

{% tabs %}

{% highlight xml %}

<chart:SfFunnelChart Orientation="Horizontal">
. . .
</chart:SfFunnelChart>

{% endhighlight %}

{% highlight c# %}

SfFunnelChart chart = new SfFunnelChart();
. . .
chart.Orientation = Horizontal;
this.Content = chart;

{% endhighlight %}

{% endtabs %}

![Orientation in MAUI Chart](Orientation_images/MAUI_orientation_chart.png)