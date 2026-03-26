# Source: https://docs.syncfusion.com/uwp/pivot-grid/olap/all-level-type-member.md

# All-Level Type Member in UWP Pivot Grid (SfPivotGrid)

This feature enables you to display the âAllâ level type member across the rows and columns in the SfPivotGrid. This member behaves as parent to other members in its hierarchy by controlling their visibility through an expander.

To display the âAllâ level type member, set the `ShowLevelTypeAll` property to true as shown in the following code snippet. By default, it is set as false.

{% tabs %}

{% highlight c# %}

pivotGrid1.OlapDataManager.ShowLevelTypeAll = true;

{% endhighlight %}

{% highlight vb %}

pivotGrid1.OlapDataManager.ShowLevelTypeAll = True

{% endhighlight %}

{% endtabs %}

![PivotGrid_AllTypeEnabled](All-Level-Type-Member_images/PivotGrid_AllTypeEnabled.png)
