# Source: https://docs.syncfusion.com/windowsforms/splash-screen/faq/how-to-access-the-default-panel-of-a-splashcontrol.md

#  How to Access the Default Panel of a SplashControl

The default panel of a SplashControl can be accessed through the SplashControlPanel property.
The example given below illustrates how the background color of a SplashControl's internal panel can be changed.

{% tabs %}
{% highlight C# %}

this.splashControl1.SplashControlPanel.BackgroundColor = new Syncfusion.Drawing.BrushInfo(Syncfusion.Drawing.GradientStyle.Vertical, System.Drawing.Color.RosyBrown, System.Drawing.SystemColors.ControlLight);

{% endhighlight %}

{% highlight vb %}

Me.splashControl1.SplashControlPanel.BackgroundColor = New Syncfusion.Drawing.BrushInfo(Syncfusion.Drawing.GradientStyle.Vertical, System.Drawing.Color.RosyBrown, System.Drawing.SystemColors.ControlLight)

{% endhighlight %}
{% endtabs %}
