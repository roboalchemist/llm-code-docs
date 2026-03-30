# Source: https://docs.syncfusion.com/windowsforms/gridgrouping/faq/displayelements/how-to-find-displayelement-type.md

# How To Find DisplayElement Type

You can find the type of particular DisplayElement using the code below.

{% tabs %}
{% highlight c# %}

//Accesses the type of display element.
Console.WriteLine(this.gridGroupingControl1.Table.DisplayElements[rowIndex].Kind);

{% endhighlight %}

{% highlight vb %}

'Accesses the type of display element.
Console.WriteLine(Me.gridGroupingControl1.Table.DisplayElements(rowIndex).Kind)

{% endhighlight %}
{% endtabs %}
