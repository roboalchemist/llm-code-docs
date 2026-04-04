# Source: https://docs.syncfusion.com/wpf/olap-gauge/xaml-configuration.md

# Source: https://docs.syncfusion.com/wpf/olap-grid/xaml-configuration.md

# Source: https://docs.syncfusion.com/wpf/olap-chart/xaml-configuration.md

# XAML Configuration in WPF Olap Chart

XAML configuration is one of the important features of the OLAP chart, as it helps users to configure the control entirely through XAML by eliminating the required code in code behind. 

### Properties 
* **DataSource.ConnectionString**: Specifies the connection string of the data manager.
* **DataSource.ConnectionName**: Specifies the connection name, which is available in the App.Config file of the application.
* **DataSource.DataManagerName**: Specifies the data manager name.
* **SharedDataManagerName**: Specifies the data manager name, which is available in the shared data manager collection.
* **ReportName**: Specifies the OLAP report name.
* **CurrentCubeName**: Specifies the current cube name of an OLAP report.
* **CategoricalAxis**: Specifies the categorical axis of the OLAP report.
* **SeriesAxis**: Specifies the series axis of the OLAP report.
* **SlicerAxis**: Specifies the slicer axis of the OLAP report.
* **CalculatedMembers**: Specifies the calculated members of the OLAP report.

Adding an OLAP report to the OLAP chart in design time is described in the following code sample.

{% highlight xaml %}

<syncfusion:OlapChartÂ x:Name="olapChart"Â HorizontalAlignment="Stretch" ReportName="SalesReport"
		CurrentCubeName="AdventureÂ Works"Â SharedDataManagerName="localManager"
		olapshared:DataSource.DataManagerName="localManager"
		olapshared:DataSource.ConnectionString="datasource=localhost; initialÂ catalog=adventureÂ worksÂ dw">
<!- Adding Elements to Categorical Axis -->
	<syncfusion:OlapChart.CategoricalAxis>
		Â <syncfusion:DimensionÂ Name="Date"Â HierarchyName="Fiscal"Â LevelName="FiscalÂ Year"Â IncludeMembers="FYÂ 2002,Â FYÂ 2003"Â Â />Â Â Â <!- Multiple Members where specified by comma separate -->Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â 
		Â <syncfusion:KpiÂ Name="Revenue"Â ShowGoal="True"Â ShowStatus="True"Â ShowValue="True"Â ShowTrend="True"Â />
	</syncfusion:OlapChart.CategoricalAxis>
<!- Adding Elements to Series Axis -->
	<syncfusion:OlapChart.SeriesAxis>
		Â <syncfusion:DimensionÂ Name="SalesÂ Channel"Â HierarchyName="SalesÂ Channel"Â LevelName="SalesÂ Channel"Â />
	 Â Â Â Â <syncfusion:DimensionÂ Name="Product"Â HierarchyName="ProductÂ ModelÂ Lines"Â LevelName="ProductÂ Line"Â IncludeMembers="Road"Â />
	</syncfusion:OlapChart.SeriesAxis>
</syncfusion:OlapChart>

{% endhighlight %}
 
![XAML-Configuration_img1](XAML-Configuration_images/XAML-Configuration_img1.png)

A sample demo is available at the following location.

{system drive}:\Users\&lt;User Name&gt;\AppData\Local\Syncfusion\EssentialStudio\&lt;Version Number&gt;\WPF\OlapChart.WPF\Samples\Defining Reports\ XAML Configuration Demo

