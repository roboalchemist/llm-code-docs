# Source: https://docs.syncfusion.com/wpf/olap-common/drill-replace.md

# Drill Replace in WPF OLAP Common

Drill replace displays only the immediate child members and ancestors on drill-down and drill-up respectively.

The following code illustrates how to achieve drill replace support in a current report.

{% tabs %}
{% highlight c# %}

olapDataManager.CurrentReport.DrillTypeÂ =Â DrillType.DrillReplace;


{% endhighlight %}


{% highlight vbnet %}

olapDataManager.CurrentReport.DrillTypeÂ =Â DrillType.DrillReplace

{% endhighlight %}
{% endtabs %}


