# Source: https://docs.syncfusion.com/wpf/olap-common/how-to/apply-the-filter-through-filter-element.md

# Apply the Filter through filter element

The filter element will get information such as filter condition and filter value from the user, from the filter expression and then get the elements on which the filter has to apply.

The following codes describe the creation of the filter element and its application: 

{% tabs %}
{% highlight c# %}



DimensionElementÂ dimensionElementColumnÂ =Â newÂ DimensionElement();
//SpecifyingÂ theÂ NameÂ forÂ theÂ DimensionÂ Element
dimensionElementColumn.NameÂ =Â "Customer";

MeasureElementsÂ measureElementColumnÂ =Â newÂ MeasureElements();
measureElementColumn.Elements.Add(newÂ MeasureElementÂ {Â NameÂ =Â "InternetÂ SalesÂ Amount"Â });

FilterElementÂ filterElementÂ =Â newÂ FilterElement(AxisPosition.Categorical);
filterElement.Elements.Add(measureElementColumn);
filterElement.Elements.Add(dimensionElementColumn);
filterElement.FilterCaseÂ =Â FilterCase.GreaterThan;
filterElement.FilterValue.Add(newÂ MeasureElementÂ {Â NameÂ =Â "InternetÂ SalesÂ Amount",Â VisibleÂ =Â trueÂ });
filterElement.FilterValue.Add(newÂ FilterValueÂ {Â Filter_ValueÂ =Â 2700000.00Â });
filterElement.IsFilterConditionÂ =Â true;
///Â AddingÂ ColumnÂ Members
olapReport.CategoricalElements.Add(dimensionElementColumn);
olapReport.CategoricalElements.IsFilterOrSortOnÂ =Â true;
///AddingÂ MeasureÂ Element
olapReport.FilterElements.Add(filterElement);


{% endhighlight  %}


{% highlight vbnet %}



Dim dimensionElementColumn As DimensionElement = New DimensionElement()

'Specifying the Name for the Dimension Element

dimensionElementColumn.Name = "Customer"



Dim measureElementColumn As MeasureElements = New MeasureElements()

measureElementColumn.Elements.Add(New MeasureElement With {.Name = "Internet Sales Amount"})



Dim filterElement As FilterElement = New FilterElement(AxisPosition.Categorical)

filterElement.Elements.Add(measureElementColumn)

filterElement.Elements.Add(dimensionElementColumn)

filterElement.FilterCase = FilterCase.GreaterThan



filterElement.FilterValue.Add(New MeasureElement With {.Name = "Internet Sales Amount", .Visible = True})



filterElement.FilterValue.Add(New FilterValue With {.Filter_Value = 2700000.0})

filterElement.IsFilterCondition = True

''' Adding Column Members

olapReport.CategoricalElements.Add(dimensionElementColumn)

olapReport.CategoricalElements.IsFilterOrSortOn = True

'''Adding Measure Element

olapReport.FilterElements.Add(filterElement)


{% endhighlight %}
{% endtabs %}

