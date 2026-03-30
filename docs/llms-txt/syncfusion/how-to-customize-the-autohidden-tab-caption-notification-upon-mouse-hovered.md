# Source: https://docs.syncfusion.com/windowsforms/docking-manager/faq/hiding-controls/how-to-customize-the-autohidden-tab-caption-notification-upon-mouse-hovered.md

# How to customize the AutoHidden Tab caption notification upon mouse hovered?

In DockingManager, by default the width of the AutoHidden Tab can be adjusted for notification purpose upon mouse hovered on it.

This can be achieved by using the `EnableAutoAdjustCaption` property.


<table>
<tr>
<th>
Property</th><th>
Description</th></tr>
<tr>
<td>
EnableAutoAdjustCaption</td><td>
GetsÂ orÂ setsÂ whetherÂ toÂ AutoÂ adjustÂ theÂ AutoHiddenTabÂ width uponÂ MouseÂ hoverÂ andÂ selection.</td></tr>
</table>


{% tabs %}

{% highlight C# %}

//Â GetsÂ orÂ setsÂ whetherÂ toÂ AutoÂ adjustÂ theÂ AutoHiddenTabÂ widthÂ uponÂ mouseÂ hoverÂ andÂ selection

this.dockingManager1.EnableAutoAdjustCaptionÂ =Â false;

{% endhighlight %}


{% highlight VB %}

'GetsÂ orÂ setsÂ whetherÂ toÂ AutoÂ adjustÂ theÂ AutoHiddenTabÂ widthÂ uponÂ mouseÂ hoverÂ andÂ selection

Me.dockingManager1.EnableAutoAdjustCaptionÂ =Â false

{% endhighlight %}

{% endtabs %}

