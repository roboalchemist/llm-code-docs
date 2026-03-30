# Source: https://docs.syncfusion.com/windowsforms/docking-manager/faq/dockedgroup/how-to-determine-whether-any-two-controls-are-in-the-same-tabbed-group.md

# How to determine whether any two controls are in the same tabbed group?

To determine whether two controls are in same tabbed group `IsSameTabbedGroup` method can be used.

{% tabs %}

{% highlight C# %}


this.dockingManager.IsSameTabbedGroup(this.listBox1,this.listBox2);


{% endhighlight %}

{% highlight VB %}


Me.dockingManager.IsSameTabbedGroup(Me.listBox1,Me.listBox2)

{% endhighlight %}

{% endtabs %}



