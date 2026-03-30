# Source: https://docs.syncfusion.com/windowsforms/diagram/faq/how-to-smooth-out-the-edges-of-the-shapes-in-a-diagram.md

# How To Smooth-out the Edges Of the Shapes In a Diagram

You can use the Diagram.Model.RenderingStyle.SmoothingMode property to smooth-out the edges, lines and curves of the shapes in a diagram.

{% tabs %}

{% highlight c# %}

this.diagram1.Model.RenderingStyle.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.HighQuality;

{% endhighlight %}

{% highlight vbnet %}

Me.diagram1.Model.RenderingStyle.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.HighQuality

{% endhighlight %}

{% endtabs %}
