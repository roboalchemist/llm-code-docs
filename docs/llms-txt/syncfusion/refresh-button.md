# Source: https://docs.syncfusion.com/wpf/breadcrumb/refresh-button.md

# Refresh Button in WPF Breadcrumb (HierarchyNavigator)

The Refresh button enables the HierarchyNavigatorRefreshButtonClick event to initiate in the HierarchyNavigator control.

![Refresh-Button_img1](Refresh-Button_images/Refresh-Button_img1.png)


{% tabs %}
{% highlight xaml %}
<locals:HierarchyNavigatorÂ HierarchyNavigatorRefreshButtonClick="HierarchyNavigatorRefreshButtonClick"Â />
{% endhighlight %}

{% highlight C# %}
HierarchyNavigatorÂ hierarchyNavigatorÂ =Â newÂ HierarchyNavigator();
<br>
hierarchyNavigator.HierarchyNavigatorRefreshButtonClickÂ +=Â newÂ EventHandler(HierarchyNavigatorRefreshButtonClick);

privateÂ voidÂ HierarchyNavigatorRefreshButtonClick(objectÂ sender,Â EventArgsÂ e)
<br>
{<br>     //OccursÂ whenÂ RefreshÂ ButtonÂ Click<br>}
{% endhighlight %}

{% endtabs %}

