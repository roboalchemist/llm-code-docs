# Source: https://docs.syncfusion.com/wpf/olap-common/how-to/connect-wcf-service-in-silverlight-application.md

# Connect WCF Service in Silverlight application

The user can connect the above WCF service using Channel Factory by CustomBinding (Or BasicHttpBinding) and End Point Address values.

The below code snippet demonstrates how to connect the WCF service:

{% tabs %}
{% highlight c# %}

BindingÂ customBindingÂ =Â newÂ CustomBinding(newÂ BinaryMessageEncodingBindingElement(),Â newÂ HttpTransportBindingElementÂ {Â MaxReceivedMessageSizeÂ =Â 2147483647Â });

EndpointAddressÂ addressÂ =Â newÂ EndpointAddress(newÂ Uri(App.Current.Host.Source.ToString()Â +Â "../../../../Services/OlapManager.svc/binary"));

ChannelFactory<IOlapDataProvider>Â clientChannelÂ =Â newÂ ChannelFactory<IOlapDataProvider>(customBinding,Â address);

IOlapDataProviderÂ _dataProviderÂ =Â clientChannel.CreateChannel();



////SetsÂ theÂ dataÂ providerÂ (WCFÂ ServiceÂ connection)Â inÂ OlapDataManager

_olapDataManager.DataProviderÂ =Â _dataProvider;

{% endhighlight  %}

{% highlight vbnet %}

Dim customBinding As Binding = NewÂ CustomBinding(New BinaryMessageEncodingBindingElement(),New HttpTransportBindingElement() With { _

Key .MaxReceivedMessageSize = 2147483647 _

})

Dim address As New EndpointAddress(New Uri(App.Current.Host.Source.ToString() &Â "../../../../Services/OlapManager.svc/binary"))

Dim clientChannel As New ChannelFactory(Of IOlapDataProvider)(customBinding, address)

Dim _dataProvider As IOlapDataProviderÂ = clientChannel.CreateChannel()



'''SetsÂ theÂ dataÂ providerÂ (WCFÂ ServiceÂ connection)Â inÂ OlapDataManager

_olapDataManager.DataProviderÂ =Â _dataProvider

{% endhighlight  %}
{% endtabs %}
