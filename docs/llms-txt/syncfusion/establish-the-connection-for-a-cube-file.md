# Source: https://docs.syncfusion.com/wpf/olap-common/how-to/establish-the-connection-for-a-cube-file.md

# Establish the connection for a Cube file

A valid string is required to establish connection for an OlapDataManager.

Here is the code snippet that demonstrates how to connect cube file by using connection string:

{% tabs %}
{% highlight c# %}

OlapDataManagerÂ dataManagerÂ =Â newÂ OlapDataManager("DataSource= AdventureWorks_Ext.cub;Â Provider=MSOLAP");

{% endhighlight  %}

{% highlight vbnet %}

Dim dataManager As New OlapDataManager("DataSource= AdventureWorks_Ext.cub;Â Provider=MSOLAP")


{% endhighlight  %}
{% endtabs %}



{% tabs %}
{% highlight c# %}

Syncfusion.Olap.DataProvider.IDataProviderÂ dataProviderÂ =Â newÂ Syncfusion.Olap.DataProvider.AdomdDataProvider("DataSource= AdventureWorks_Ext.cub;Â Provider=MSOLAP");

OlapDataManagerÂ dataManagerÂ =Â newÂ OlapDataManager(dataProvider); 

{% endhighlight  %}


{% highlight vbnet %}

Dim dataProvider As Syncfusion.Olap.DataProvider.IDataProvider = New Syncfusion.Olap.DataProvider.AdomdDataProvider("DataSource= AdventureWorks_Ext.cub;Â Provider=MSOLAP")

Dim dataManager As New OlapDataManager(dataProvider)

{% endhighlight  %}

{% endtabs %}
