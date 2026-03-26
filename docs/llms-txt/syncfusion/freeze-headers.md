# Source: https://docs.syncfusion.com/uwp/pivot-grid/common/freeze-headers.md

# Source: https://docs.syncfusion.com/wpf/pivot-grid/freeze-headers.md

# Source: https://docs.syncfusion.com/wpf/olap-grid/freeze-headers.md

# Freeze Headers in WPF Olap Grid

The OLAP grid provides built-in support to freeze the column and row headers. This can be achieved by setting the `FreezeHeaders` property of OLAP grid to **"true"**.

{% tabs %}
  
{% highlight xaml %}

<syncfusion:OlapGrid  FreezeHeaders="True"> 
</syncfusion:OlapGrid>

{% endhighlight %}

{% highlight c# %}

// To freeze OlapGrid Headers
this.OlapGrid1.FreezeHeaders = true;

{% endhighlight %}

{% highlight vbnet %}

' To freeze OlapGrid Headers
Me.OlapGrid1.FreezeHeaders = True

{% endhighlight %}

{% endtabs %}

![Enables the freeze headers in OlapGrid](Freeze-Headers_images/Freeze-Headers_img1.png)

A sample demo is available in the following location.

{system drive:}\Users\&lt;User Name&gt;\AppData\Local\Syncfusion\EssentialStudio\&lt;Version Number&gt;\WPF\OlapGrid.WPF\Samples\Appearance\Frozen Header


