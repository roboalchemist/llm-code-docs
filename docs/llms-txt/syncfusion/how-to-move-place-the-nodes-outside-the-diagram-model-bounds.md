# Source: https://docs.syncfusion.com/windowsforms/diagram/faq/how-to-move-place-the-nodes-outside-the-diagram-model-bounds.md

# How To Move / Place the Nodes Outside the Diagram Model's Bounds

Setting the model's BoundaryConstraintsEnabled property to 'false', will let you place the nodes outside the bounds of the diagram model.

{% tabs %}

{% highlight c# %}

diagram1.Model.BoundaryConstraintsEnabled = false;

{% endhighlight %}

{% highlight vbnet %}

diagram1.Model.BoundaryConstraintsEnabled = False

{% endhighlight %}

{% endtabs %}