# Source: https://docs.syncfusion.com/wpf/olap-common/how-to/bind-an-olapreport-with-olapdatamanager.md

# Bind an OlapReport with OlapDataManager

Once the connection is established, you can create and bind the OlapReport to the manger by using any one of the following property and methods:

### Property

1. CurrentReport

### Methods

1. SetCurrentReport
2. LoadOlapDataManager
3. LoadReportDefinitionFile
4. LoadReportDefinitionFromStream  

### Methods for Silverlight

1. SetCurrentReport
2. LoadReportFromStream



The following code snippet will illustrate the binding of OlapReport using these methods with a sample OlapReport:

## Sample OlapReport

{% tabs %}

{% highlight c# %}

OlapDataManagerÂ OlapDataManagerÂ =Â newÂ OlapDataManager

(@"DataSource=localhost;Â InitialÂ Catalog=AdventureÂ WorksÂ DW");

OlapReportÂ olapReportÂ =Â newÂ OlapReport();

olapReport.Name =Â "Customer Report";
olapReport.CurrentCubeNameÂ =Â "AdventureÂ Works";

DimensionElementÂ dimensionElementColumnÂ =Â newÂ DimensionElement();
//SpecifyingÂ theÂ NameÂ forÂ theÂ DimensionÂ Element
dimensionElementColumn.NameÂ =Â "Customer";
dimensionElementColumn.AddLevel("CustomerÂ Geography",Â "Country");

MeasureElementsÂ measureElementColumnÂ =Â newÂ MeasureElements();
//SpecifyingÂ theÂ NameÂ forÂ theÂ MeasureÂ Element
measureElementColumn.Elements.Add(newÂ MeasureElementÂ 

{Â NameÂ =Â "InternetÂ SalesÂ Amount"Â });

DimensionElementÂ dimensionElementRowÂ =Â newÂ DimensionElement();
//SpecifyingÂ theÂ DimensionÂ Name
dimensionElementRow.NameÂ =Â "Date";
dimensionElementRow.AddLevel("Fiscal",Â "FiscalÂ Year");

///AddingÂ ColumnÂ Members
olapReport.CategoricalElements.Add(dimensionElementColumn);
///AddingÂ MeasureÂ Element
olapReport.CategoricalElements.Add(measureElementColumn);
///AddingÂ RowÂ Members
olapReport.SeriesElements.Add(dimensionElementRow);

{% endhighlight  %}

{% highlight vbnet %}



Dim OlapDataManager As OlapDataManager = New OlapDataManager                  ("DataSource=localhost;Â InitialÂ Catalog=AdventureÂ WorksÂ DW") DimÂ olapReport1Â AsÂ OlapReportÂ =Â NewÂ OlapReport()

olapReport.Name =Â "Customer Report"
olapReport1.CurrentCubeNameÂ =Â "AdventureÂ Works" 
DimÂ dimensionElementColumnÂ AsÂ DimensionElementÂ =Â 

NewÂ DimensionElement()
'SpecifyingÂ theÂ NameÂ forÂ theÂ DimensionÂ Element
dimensionElementColumn.NameÂ =Â "Customer"
dimensionElementColumn.AddLevel("CustomerÂ Geography",Â "Country")

DimÂ measureElementColumnÂ AsÂ MeasureElementsÂ =Â NewÂ MeasureElements()
'SpecifyingÂ theÂ NameÂ forÂ theÂ MeasureÂ Element

measureElementColumn.Elements.Add(NewÂ MeasureElementÂ WithÂ {.NameÂ =Â "InternetÂ SalesÂ Amount"})

DimÂ dimensionElementRowÂ AsÂ DimensionElementÂ =Â NewÂ DimensionElement()
'SpecifyingÂ theÂ DimensionÂ Name
dimensionElementRow.NameÂ =Â "Date"
dimensionElementRow.AddLevel("Fiscal",Â "FiscalÂ Year")

'AddingÂ ColumnÂ Members
olapReport1.CategoricalElements.Add(dimensionElementColumn)
'AddingÂ MeasureÂ Element

olapReport1.CategoricalElements.Add(measureElementColumn)
'AddingÂ RowÂ Members
olapReport1.SeriesElements.Add(dimensionElementRow)

{% endhighlight  %}
{% endtabs %}
