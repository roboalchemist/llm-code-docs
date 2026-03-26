# Source: https://docs.syncfusion.com/windowsforms/docking-manager/faq/general/how-to-hide-caption-lines-in-dockingmanager.md

# How to hide caption lines in DockingManager?

Caption lines which is displayed in Metro style can be hidden by disabling the `ShowMetroCaptionDottedLines` property.


{% tabs %}

{% highlight C# %}

//To hide the caption lines in Metro style

this.dockingManager1.ShowMetroCaptionDottedLines = false;

{% endhighlight %}

{% highlight VB %}

'To hide the caption lines in Metro style

Me.dockingManager1.ShowMetroCaptionDottedLines = false

{% endhighlight %}

{% endtabs %}

