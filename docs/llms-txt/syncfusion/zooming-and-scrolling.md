# Source: https://docs.syncfusion.com/windowsforms/pivot-chart/zooming-and-scrolling.md

# Source: https://docs.syncfusion.com/wpf/olap-chart/zooming-and-scrolling.md

# Zooming and Scrolling in WPF Olap Chart

The OLAP chart for WPF allows you to zoom in to a narrower range within the OLAP chart.

In the zooming mode, a zooming toolkit is displayed at the top-left corner of the OLAP chart. Using the buttons in the zooming toolkit, ChartSeries can be zoomed in, out, reset, or closed.

![Zooming-and-scrolling_img1](Zooming-and-scrolling_images/Zooming-and-scrolling_img1.png)

The visibility of the zooming toolkit or individual buttons in the toolkit can be controlled by using the following properties:

_Property_

* **ZoomInButtonVisibility**: Gets or sets the zoom in button visibility.
* **ZoomOutButtonVisibility**: Gets or sets the zoom out button visibility.
* **ZoomCloseButtonVisibility**: Gets or sets the zoom close button visibility.
* **ZoomResetButtonVisibility**: Gets or sets the zoom reset button visibility.

The following code sample illustrates the above settings.

{% tabs %}

{% highlight xaml %}

<syncfusion:OlapChartÂ Name="olapChart"Â 
    syncfusion:ChartZoomingToolkit.ZoomInButtonVisibility="{BindingÂ IsChecked,Â 
          ElementName=cbxZoomIn,Â Converter={StaticResourceÂ boolToVisibilityConverter}}"
    syncfusion:ChartZoomingToolkit.ZoomOutButtonVisibility="{BindingÂ IsChecked,Â 
          ElementName=cbxZoomOut,Â Converter={StaticResourceÂ boolToVisibilityConverter }}"
    syncfusion:ChartZoomingToolkit.ZoomCloseButtonVisibility="{BindingÂ IsChecked,Â 
          ElementName=cbxZoomClose,Â Converter={StaticResourceÂ boolToVisibilityConverter }}"
    syncfusion:ChartZoomingToolkit.ZoomResetButtonVisibility="{BindingÂ IsChecked,Â 
          ElementName=cbxZoomReset,Â Converter={StaticResourceÂ boolToVisibilityConverter }}">
</syncfusion:OlapChart>

{% endhighlight %}

{% highlight c# %}
 
ChartZoomingToolkit.SetZoomInButtonVisibility(olapChart,Â Visibility.Collapsed);
ChartZoomingToolkit.SetZoomOutButtonVisibility(olapChart,Â Visibility.Hidden);
ChartZoomingToolkit.SetZoomResetButtonVisibility(olapChart,Â Visibility.Collapsed);
ChartZoomingToolkit.SetZoomingToolkitVisibility(olapChart,Â Visibility.Visible);

{% endhighlight %}

{% highlight vbnet %}
  
ChartZoomingToolkit.SetZoomInButtonVisibility(olapChart,Â Visibility.Collapsed)
ChartZoomingToolkit.SetZoomOutButtonVisibility(olapChart,Â Visibility.Hidden)
ChartZoomingToolkit.SetZoomResetButtonVisibility(olapChart,Â Visibility.Collapsed)
ChartZoomingToolkit.SetZoomingToolkitVisibility(olapChart,Â Visibility.Visible)

{% endhighlight %}

{% endtabs %}

A sample demo is available at the following location.

{system drive}:\Users\&lt;User Name&gt;\AppData\Local\Syncfusion\EssentialStudio\&lt;Version Number&gt;\WPF\OlapChart.WPF\Samples\Zooming and Scrolling\Zooming and Scrolling Demo
