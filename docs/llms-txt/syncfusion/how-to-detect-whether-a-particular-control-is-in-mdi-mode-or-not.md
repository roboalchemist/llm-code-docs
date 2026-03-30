# Source: https://docs.syncfusion.com/windowsforms/docking-manager/faq/mdichild/how-to-detect-whether-a-particular-control-is-in-mdi-mode-or-not.md

# How to detect whether a particular control is in MDI mode or not?


`IsMDIMode` method lets you detect whether the specified control is in MDI child mode or not. The return value will be `true` if the control is in MDI mode, else value will be `false`.



{% tabs %}

{% highlight C# %}

this.dockingManager1.IsMDIMode(this.listBox2);

{% endhighlight %}

{% highlight VB %}


Me.dockingManager1.IsMDIMode(Me.listBox2)

{% endhighlight %}

{% endtabs %}
