# Source: https://docs.syncfusion.com/wpf/range-slider/minimum-and-maximum.md

# Minimum and Maximum in WPF Range Slider (SfRangeSlider)

Gets or sets the minimum and maximum possible value of the range.

{% tabs %}

{% highlight XAML %}

 <editors:SfRangeSlider
                    Width="500"
                    Maximum="100"
                    Minimum="0" />

{% endhighlight %}

{% highlight C# %}

            Grid parentGrid = new Grid();
            SfRangeSlider rangeSlider = new SfRangeSlider()
            {
                Width = 500,
                Maximum = 100,
                Minimum = 0
            };

            parentGrid.Children.Add(rangeSlider);
            this.Content = parentGrid;

{% endhighlight %}

{% endtabs %}
