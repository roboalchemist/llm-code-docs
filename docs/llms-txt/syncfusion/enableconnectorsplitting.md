# Source: https://docs.syncfusion.com/wpf/diagram/interaction/dragging/enableconnectorsplitting.md

# Enable connector splitting in WPF Diagram (SfDiagram)

The connectors are used to create a link between two points, ports, or nodes to represent the relationship between them. You can split the connector between two nodes when dropping a new node onto an existing connector and create a connection between the new node and existing nodes by setting `EnableConnectorSplitting` as `true`. The default value of `EnableConnectorSplitting` is `false`.

{% tabs %}
{% highlight Xaml %}

<Syncfusion:SfDiagram x:Name="Diagram" EnableConnectorSplitting="True"/>

{% endhighlight %}

{% highlight C# %}

SfDiagram Diagram = new SfDiagram();

Diagram.EnableConnectorSplitting = true;

{% endhighlight %}
{% endtabs %}

![SplitandJoin](Drag_images/ConnectorSplitting.gif)