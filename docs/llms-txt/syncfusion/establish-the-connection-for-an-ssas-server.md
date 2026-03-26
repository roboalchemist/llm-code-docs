# Source: https://docs.syncfusion.com/wpf/olap-common/how-to/establish-the-connection-for-an-ssas-server.md

# Establish the connection for an SSAS Server

A valid string is required to establish connection for an OlapDataManager.

Here is the code snippet that demonstrates how to connect SSAS by using connection string:

{% tabs %}
{% highlight c# %}

OlapDataManagerÂ dataManagerÂ =Â newÂ OlapDataManager("DataSource=localhost;Â InitialÂ Catalog=AdventureÂ WorksÂ DW");

{% endhighlight  %}

{% highlight vbnet %}

Dim dataManager As New OlapDataManager("DataSource=localhost; Initial Catalog=Adventure Works DW")
{% endhighlight  %}
{% endtabs %}
{% tabs %}

{% highlight c# %}

Syncfusion.Olap.DataProvider.IDataProviderÂ dataProviderÂ =Â newÂ Syncfusion.Olap.DataProvider.AdomdDataProvider("DataSource=localhost;Â InitialÂ Catalog=AdventureÂ WorksÂ DW");

OlapDataManagerÂ dataManagerÂ =Â newÂ OlapDataManager(dataProvider); 

{% endhighlight  %}

{% highlight vbnet %}

Dim dataProvider As Syncfusion.Olap.DataProvider.IDataProvider = New Syncfusion.Olap.DataProvider.AdomdDataProvider("DataSource=localhost; Initial Catalog=Adventure Works DW")

Dim dataManager As New OlapDataManager(dataProvider)

{% endhighlight  %}
{% endtabs %}
