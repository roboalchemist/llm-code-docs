# Source: https://docs.syncfusion.com/windowsforms/docking-manager/faq/general/how-to-change-the-dock-tab-alignment.md

# How to change the dock tab alignment?

The tabs of the Docked window are placed at the bottom, by default. To place the tabs of the docked window at different sides set the propertyÂ `DockTabAlignment`Â with desired values such as Top, Bottom, Left, and Right.

{% tabs %}

{% highlight C# %}

//To set the Tab alignment as Right.

this.dockingManager.DockTabAlignment = Syncfusion.Windows.Forms.Tools.DockTabAlignmentStyle.Right;

{% endhighlight %}


{% highlight VB %}

'To set the Tab alignment as Right.

Me.dockingManager.DockTabAlignment = Syncfusion.Windows.Forms.Tools.DockTabAlignmentStyle.Right;
 
{% endhighlight %}

{% endtabs %}



