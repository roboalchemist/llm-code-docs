# Source: https://docs.syncfusion.com/windowsforms/xptaskbar/faq/how-to-set-the-focus-rectangle-for-xptaskbaritem-after-selection.md

# How to set the focus rectangle for XPTaskBarItem after selection

This can be achieved by setting the [DrawFocusRect](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.XPTaskBarBox.html#Syncfusion_Windows_Forms_Tools_XPTaskBarBox_DrawFocusRect) property to `true`.

{% tabs %}

{% highlight C# %}   

this.xpTaskBarBox1.DrawFocusRect = true;

{% endhighlight %}



{% highlight VB %} 

Me.xpTaskBarBox1.DrawFocusRect = True

{% endhighlight %}

{% endtabs %}
