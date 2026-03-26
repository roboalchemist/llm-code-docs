# Source: https://docs.syncfusion.com/windowsforms/gridgrouping/faq/displayelements/how-to-access-a-particular-displayelement-if-rowindex-is-provided.md

# How to Access a Particular DisplayElement if Row Index is Provided

You can access DisplayElements with row index by using the following code.

{% tabs %}
{% highlight c# %}

// Accesses a particular display element.
Element el=this.gridGroupingControl1.Table.DisplayElements[rowIndex].ParentElement;
{% endhighlight %}

{% highlight vb %}

' Accesses a particular display element.
Dim el As Element = Me.gridGroupingControl1.Table.DisplayElements(rowIndex).ParentElement

{% endhighlight %}
{% endtabs %}
