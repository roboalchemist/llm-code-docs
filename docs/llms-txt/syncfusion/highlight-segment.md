# Source: https://docs.syncfusion.com/uwp/sparkline/highlight-segment.md

# Source: https://docs.syncfusion.com/wpf/sparkline/highlight-segment.md

# Highlight Segment in WPF Sparkline (SfSparkline)

This feature enable to highlight the column segments on mouse move and this is applicable for column and win-loss sparkline.

{% tabs %}

{% highlight xaml %}

<Syncfusion:SfColumnSparkline HighlightSegment="True" ItemsSource="{Binding UsersList}" YBindingPath="NoOfUsers" >

</Syncfusion:SfColumnSparkline>
		
{% endhighlight %}  

{% highlight c# %}

SfColumnSparkline sparkline = new SfColumnSparkline()
{

    ItemsSource = new SparkViewModel().UsersList,

    YBindingPath = "NoOfUsers",

    HighlightSegment = true

};

{% endhighlight %}

{% endtabs %}

Following is the snapshot for highlight segment,

![Highlight-Segment_img1](Highlight-Segment_images/Highlight-Segment_img1.png)
