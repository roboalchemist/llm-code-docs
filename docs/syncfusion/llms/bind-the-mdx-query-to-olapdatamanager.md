# Source: https://docs.syncfusion.com/wpf/olap-common/how-to/bind-the-mdx-query-to-olapdatamanager.md

# Bind the MDX query to OlapDataManager

MDX query is one of the inputs accepted by the OlapDataManager to process the data in the connected data source. There are two way to pass the MDX query to OlapDataManager:

1. Through MdxQuery property
2. Through ExecuteCellSet() method argument 



OlapDataManager will accept the MDX query in the string format through any one of this and process the data based on the query. Once the connection is established you can pass the MDX query in string format.

The following code will illustrate the passing of the MXD query as input:

{% tabs %}
{% highlight c# %}

OlapDataManagerÂ olapDataManagerÂ =Â newÂ OlapDataManager("DataSource=localhost;Â InitialÂ Catalog=AdventureÂ WorksÂ DW");
stringÂ mdxQueryÂ =Â 

@"SELECTÂ NONÂ EMPTYÂ ({Hierarchize({DrilldownLevel(

[Customer].[CustomerÂ Geography].[AllÂ Customers])})}Â *Â 

{[MEASURES].[InternetÂ SalesÂ Amount]})Â dimensionÂ properties

Â member_typeÂ ONÂ COLUMNS,Â NONÂ EMPTYÂ (Hierarchize(

DrilldownLevel([Date].[Fiscal].[AllÂ Periods]))Â )Â 

dimensionÂ propertiesÂ member_typeÂ ONÂ ROWSÂ 

FROMÂ [AdventureÂ Works]Â Â CELLÂ PROPERTIESÂ 

VALUE,Â FORMAT_STRING,Â FORMATTED_VALUE";
olapDataManager.MdxQueryÂ =Â mdxQuery;
olapDataManager.ExecuteCellSet();


{% endhighlight  %}
{% highlight vbnet %}



Dim olapDataManager As OlapDataManager = New OlapDataManager("DataSource=localhost; Initial Catalog=Adventure Works DW")

Dim mdxQuery As String = "SELECTÂ NONÂ EMPTYÂ ({Hierarchize({DrilldownLevel({

[Customer].[CustomerÂ Geography].[AllÂ Customers]})})}Â *Â 

{[MEASURES].[InternetÂ SalesÂ Amount]})Â dimensionÂ properties

Â member_typeÂ ONÂ COLUMNS,Â NONÂ EMPTYÂ ({Hierarchize({

DrilldownLevel({[Date].[Fiscal].[AllÂ Periods]})})}Â )Â 

dimensionÂ propertiesÂ member_typeÂ ONÂ ROWSÂ 

FROMÂ [AdventureÂ Works]Â Â CELLÂ PROPERTIESÂ 

VALUE,Â FORMAT_STRING,Â FORMATTED_VALUE"

olapDataManager.MdxQuery = mdxQuery

olapDataManager.ExecuteCellSet()

{% endhighlight  %}
{% endtabs %}

This will accept the MDX query as a string and assign it to the OlapDataManagerâd MdxQuery property and invoke the data process.

{% tabs %}
{% highlight c# %}

OlapDataManagerÂ olapDataManagerÂ =Â newÂ OlapDataManager("DataSource=localhost;Â InitialÂ Catalog=AdventureÂ WorksÂ DW");
stringÂ mdxQueryÂ =Â 

@"SELECTÂ NONÂ EMPTYÂ ({Hierarchize({DrilldownLevel({

[Customer].[CustomerÂ Geography].[AllÂ Customers]})})}Â *Â 

{[MEASURES].[InternetÂ SalesÂ Amount]})Â dimensionÂ properties

Â member_typeÂ ONÂ COLUMNS,Â NONÂ EMPTYÂ ({Hierarchize({

DrilldownLevel({[Date].[Fiscal].[AllÂ Periods]})})}Â )Â 

dimensionÂ propertiesÂ member_typeÂ ONÂ ROWSÂ 

FROMÂ [AdventureÂ Works]Â Â CELLÂ PROPERTIESÂ 

VALUE,Â FORMAT_STRING,Â FORMATTED_VALUE";

olapDataManager.ExecuteCellSet(mdxQuery);

{% endhighlight  %}



{% highlight vbnet %}



Dim olapDataManager As OlapDataManager = New OlapDataManager("DataSource=localhost; Initial Catalog=Adventure Works DW")

Dim mdxQuery As String = "SELECTÂ NONÂ EMPTYÂ ({Hierarchize({DrilldownLevel({

[Customer].[CustomerÂ Geography].[AllÂ Customers]})})}Â *Â 

{[MEASURES].[InternetÂ SalesÂ Amount]})Â dimensionÂ properties

Â member_typeÂ ONÂ COLUMNS,Â NONÂ EMPTYÂ ({Hierarchize({

DrilldownLevel({[Date].[Fiscal].[AllÂ Periods]})})}Â )Â 

dimensionÂ propertiesÂ member_typeÂ ONÂ ROWSÂ 

FROMÂ [AdventureÂ Works]Â Â CELLÂ PROPERTIESÂ 

VALUE,Â FORMAT_STRING,Â FORMATTED_VALUE"

olapDataManager.ExecuteCellSet(mdxQuery)

{% endhighlight  %}

{% endtabs %}


## Sequential Diagram 

The following sequential diagram is matching when user gives input as MDX query:



![Bind-the-MDX-query-to-OlapDataManager_img1](Bind-the-MDX-query-to-OlapDataManager_images/Bind-the-MDX-query-to-OlapDataManager_img1.png)





OLAP base sequential diagram
{:.caption}





