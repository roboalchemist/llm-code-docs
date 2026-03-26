# Source: https://docs.syncfusion.com/windowsforms/gridgrouping/faq/sorting/how-to-refresh-binding-list-data-source-automatically-when-grid-grouping-control-changes.md

# How to Refresh Binding List Data Source automatically when Grid Grouping Control Changes

To refresh binding list data source automatically when GridGroupingControl changes, you need to set TableDirty property to _â__Trueâ_ in GridGroupingControl. Doing this invalidates Grid Table to its current changes. Refreshing Data Source takes place only while using the data source as Binding List. The following code sample shows how to refresh Binding List Data Source when GridGroupingControl changes.

{% tabs %}
{% highlight c# %}

this.Grid.Table.TableDirty = â_Trueâ_

{% endhighlight %}

{% highlight vbnet %}

this.Grid.Table.TableDirty = _âTrueâ_
  
{% endhighlight %}
{% endtabs %} 

Sample: [http://www.syncfusion.com/downloads/support/directtrac/118685/GridDeleteTest-1197463268.zip](http://www.syncfusion.com/downloads/support/directtrac/118685/GridDeleteTest-1197463268.zip)

