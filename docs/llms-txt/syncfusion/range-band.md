# Source: https://docs.syncfusion.com/uwp/sparkline/range-band.md

# Source: https://docs.syncfusion.com/wpf/sparkline/range-band.md

# Range Band in WPF Sparkline (SfSparkline)

Range band feature used to highlight the particular mentioned range along Y axis.

{% tabs %}

{% highlight xaml %}

<Syncfusion:SfLineSparkline 

			ItemsSource="{Binding UsersList}" 

			BandRangeStart="2000â

			BandRangeEnd="-1000â RangeBandBrush="Greenâ

			YBindingPath="NoOfUsers">

</Syncfusion:SfLineSparkline >

{% endhighlight %}

{% highlight c# %}

SfLineSparkline sparkline = new SfLineSparkline()
{

	ItemsSource = new SparkViewModel().UsersList,

	YBindingPath = "NoOfUsers",

	BandRangeStart = 2000,

	BandRangeEnd = -1000,

	RangeBandBrush = new SolidColorBrush(Colors.Green)

};

{% endhighlight %}

{% endtabs %}

Following is the snapshot for range band,

![Range-Band_img1](Range-Band_images/Range-Band_img1.png)
