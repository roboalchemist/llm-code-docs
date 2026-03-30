# Source: https://docs.syncfusion.com/wpf/olap-common/how-to/get-the-reports-in-the-olapdatamanager-as-a-stream.md

# Get the reports in the OlapDataManager as a stream

You can get the report collection in the OlapDataManager as a stream by using GetReportAsStream method. This method will return the current report collection of the OlapDataManager as a stream.

The following code snippet will explain obtaining the report as a stream:

{% tabs %}
{% highlight c# %}

StreamÂ reportStreamÂ =Â olapDataManager.GetReportAsStream();

{% endhighlight  %}

{% highlight vbnet %}

DimÂ reportStreamÂ AsÂ StreamÂ =Â olapDataManager.GetReportAsStream()


{% endhighlight  %}
{% endtabs %}