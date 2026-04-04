# Source: https://docs.syncfusion.com/windowsforms/treemap/weightvaluepath.md

# Source: https://docs.syncfusion.com/wpf/treemap/weightvaluepath.md

# WeightValuePath in WPF TreeMap (SfTreeMap)

The WeightValuePath ofSfTreeMap is a path to a field on the source object, which serve as the "weight" of the object. 


{% highlight xaml %}



    <Grid Background="Black">

        <Grid.DataContext>

            <local:PopulationViewModel/>

        </Grid.DataContext>

        <syncfusion:SfTreeMap ItemsSource="{Binding PopulationDetails}" 

                              WeightValuePath="Populationâ/>

    </Grid>

{% endhighlight %}



N> The specified field must be available in each and every sub class (object) defined in hierarchical (nested) data collection.

![WeightValuePath_img1](WeightValuePath_images/WeightValuePath_img1.png)



