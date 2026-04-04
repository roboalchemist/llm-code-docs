# Source: https://docs.syncfusion.com/document-processing/excel/excel-library/net/faqs/in-which-situation-we-use-enablepartialtrustcode-property.md

# When should use EnablePartialTrustCode property?

Enable the EnablePartialTrustCode property only in restricted, hosted environments such as Azure App Service. Because, there will be a GDI+ exception thrown while handling meta file images such as emf and wmf formats. When this property is enabled, the images will not be rendered instead of throwing exception.

N> Azure or other sandboxes hosting: set EnablePartialTrustCode = true to bypass EMF/WMF GDI+ exceptions.
Other environments: keep EnablePartialTrustCode = false for fullâfidelity image rendering.

Use the following code snippet to set the EnablePartialTrustCode property

{% tabs %}
{% highlight c# tabtitle="C# [Cross-platform]" %}
IApplication application = excelEngine.Excel;
application.EnablePartialTrustCode = false; // Setting the EnablePartialTrustCode to false
{% endhighlight %}

{% highlight c# tabtitle="C# [Windows-specific]" %}
IApplication application = excelEngine.Excel;
application.EnablePartialTrustCode = false; // Setting the EnablePartialTrustCode to false
{% endhighlight %}

{% highlight vb.net tabtitle="VB.NET [Windows-specific]" %}
Dim application As IApplication = excelEngine.Excel
application.EnablePartialTrustCode = False ' Setting EnablePartialTrustCode to False
{% endhighlight %}
{% endtabs %}