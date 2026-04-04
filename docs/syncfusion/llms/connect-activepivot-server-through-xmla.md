# Source: https://docs.syncfusion.com/wpf/olap-common/how-to/connect-activepivot-server-through-xmla.md

# Connect ActivePivot Server through XMLA



The user can connect the Active Pivot server through XMLA (XML for Analysis) services using the OlapDataManager in our OLAP controls.



The following code illustrates how to connect to Active Pivot server:


{% tabs %}
{% highlight c# %}

// Connecting to Active Pivot Server

OlapDataManager DataManager = new OlapDataManager(@"DataÂ Source=http://localhost:8081/var_s/xmla;Â  InitialÂ Catalog=VaRCubes; UserÂ ID=;Â Password=;Â TransportÂ Compression=None;");

DataManager.DataProvider.ProviderNameÂ =Â Syncfusion.Olap.DataProvider.Providers.ActivePivot;

{% endhighlight  %}

{% highlight vbnet %}

' Connecting to Active Pivot Server 

Dim DataManager As OlapDataManager = New OlapDataManager("Data Source=http://localhost:8081/var_s/xmla;  Initial Catalog=VaRCubes; User ID=; Password=; Transport Compression=None;")

DataManager.DataProvider.ProviderNameÂ =Â Syncfusion.Olap.DataProvider.Providers.ActivePivot

{% endhighlight  %}
{% endtabs %}

[Refer here](http://quartetfs.com/) for more information about Active Pivot server.

