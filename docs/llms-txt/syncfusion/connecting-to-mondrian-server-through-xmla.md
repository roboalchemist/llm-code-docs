# Source: https://docs.syncfusion.com/wpf/olap-common/how-to/connecting-to-mondrian-server-through-xmla.md

# Connecting to Mondrian Server through XMLA



The following code illustrates how to connect to the Mondrian server:


{% tabs %}
{% highlight c# %}



// Connecting to Mondrian Server

OlapDataManager DataManager = new OlapDataManager(@"DataÂ Source = http://localhost:8080/mondrian/xmla; Initial Catalog = FoodMart;"); //Where localhost is the machine name which has installed Mondrian Services. For example http://bi.syncfusion.com:8080/mondrian/xmla



DataManager.DataProvider.ProviderNameÂ =Â Syncfusion.Olap.DataProvider.Providers.Mondrian;


{% endhighlight  %}

{% highlight vbnet %}



' Connecting to Mondrian Server

Dim DataManager As New OlapDataManager("Data Source = http://localhost:8080/mondrian/xmla; Initial Catalog =FoodMart;")
'Where localhost is the machine name which has installed Mondrian Services. For example http://bi.syncfusion.com:8080/mondrian/xmla



DataManager.DataProvider.ProviderNameÂ =Â Syncfusion.Olap.DataProvider.Providers.Mondrian


{% endhighlight  %}
{% endtabs %}

[Refer here](http://mondrian.pentaho.com/) for more information about Mondrian XMLA configurations.



