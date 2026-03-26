# Source: https://docs.syncfusion.com/windowsforms/hub-tile/faq/how-to-freeze-hubtile-functionality-in-runtime.md

# How to freeze HubTile functionality in runtime?

You can achieve it by enabling [IsFrozen](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.HubTile.html#Syncfusion_Windows_Forms_Tools_HubTile_IsFrozen) property of HubTile.

{% tabs %}
{% highlight C# %}
this.HubTile1.IsFrozen = true;
{% endhighlight %}
{% highlight VB %} 
Me.HubTile1.IsFrozen = True
{% endhighlight %}
{% endtabs %}
