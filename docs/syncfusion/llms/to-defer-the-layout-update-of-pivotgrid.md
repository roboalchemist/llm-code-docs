# Source: https://docs.syncfusion.com/wpf/pivot-grid/how-to/to-defer-the-layout-update-of-pivotgrid.md

# How to set defer layout update in PivotGrid?

It can be achieved by setting the property `DeferLayoutUpdate` to true via code or through the DeferLayoutUpdate check-box (UI option) inside PivotSchemaDesigner control. 

If through *XAML*, please refer the below code sample.

{% highlight xaml %}

        <syncfusion:PivotGridControl HorizontalAlignment="Left" Name="pivotGrid" VerticalAlignment="Top" 
                 DeferLayoutUpdate="True" ItemSource="{Binding   Source={StaticResource data}}" >
        </syncfusion:PivotGridControl>
     
{% endhighlight %}

Else if through *Code-behind*, please refer the below code sample.

{% highlight C# %}

        public MainWindow()
        {
            InitializeComponent();
            pivotGrid.DeferLayoutUpdate = true;
        } 
		
{% endhighlight %}

