# Source: https://docs.syncfusion.com/uwp/sparkline/customize-segment-brush.md

# Source: https://docs.syncfusion.com/wpf/sparkline/customize-segment-brush.md

# Customize segment brush in WPF Sparkline (SfSparkline)

We can able to customize the first, last, negative, high and low point brushes as like markers in area and line sparkline.

{% tabs %}

{% highlight xaml %}

<Syncfusion:SfColumnSparkline ItemsSource="{Binding UsersList}" YBindingPath="NoOfUsers" >

            <Syncfusion:SfColumnSparkline.SegmentTemplateSelector>

                <Syncfusion:SegmentTemplateSelector FirstPointBrush="Yellow" LastPointBrush="Yellow" HighPointBrush="Red"/>

            </Syncfusion:SfColumnSparkline.SegmentTemplateSelector>

        </Syncfusion:SfColumnSparkline>
		
{% endhighlight  %}

{% highlight c# %}

SfColumnSparkline sparkline = new SfColumnSparkline()
{

    ItemsSource = new SparkViewModel().UsersList,

    YBindingPath = "NoOfUsers"

};

SegmentTemplateSelector selector = new SegmentTemplateSelector()
{

    FirstPointBrush = new SolidColorBrush(Colors.Yellow),

    LastPointBrush = new SolidColorBrush(Colors.Yellow),

    HighPointBrush = new SolidColorBrush(Colors.Red)

};

sparkline.SegmentTemplateSelector = selector;

{% endhighlight %}

{% endtabs %}

Following is the snapshot for customize segment,

![Customize-segment-brush_img1](Customize-segment-brush_images/Customize-segment-brush_img1.png)
