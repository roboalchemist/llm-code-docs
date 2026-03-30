# Source: https://docs.syncfusion.com/windowsforms/docking-manager/faq/dockstate/how-to-restore-the-original-docking-windows-layout-that-was-set-within-the-windows-forms-designer.md

# How to restore the original docking windows layout that was set within the Windows Forms designer?

Calling `LoadDesignerDockState()` method at run time, will restore the docking windows layout that was set in the Designer.


{% tabs %}

{% highlight C# %}

this.dockingManager1.LoadDesignerDockState();

{% endhighlight %}

{% highlight VB %}

Me.dockingManager1.LoadDesignerDockState()

{% endhighlight %}

{% endtabs %}


