# Source: https://docs.syncfusion.com/wpf/olap-common/how-to/add-the-elements-to-an-axis.md

# Add the elements to an Axis

After creating the element, add the element to the specific axis. The OlapReport contains the axis as CategoricalElements, SeriesElement and SliceElements. By adding the created elements to any of these elements group, you can specify the axis position of the elements.

The following codes will describe the adding of the elements to categorical, series element:

{% tabs %}
{% highlight c# %}



///AddingÂ ColumnÂ Members
olapReport.CategoricalElements.Add(dimensionElementColumn);
///AddingÂ MeasureÂ Element
olapReport.CategoricalElements.Add(measureElementColumn);

///AddingÂ RowÂ Members
olapReport.SeriesElements.Add(dimensionElementRow);

{% endhighlight  %}



{% highlight vbnet %}



'''Adding Column Members

olapReport.CategoricalElements.Add(dimensionElementColumn)

'''Adding Measure Element

olapReport.CategoricalElements.Add(measureElementColumn)



'''Adding Row Members

olapReport.SeriesElements.Add(dimensionElementRow)



{% endhighlight  %}
{% endtabs %}
