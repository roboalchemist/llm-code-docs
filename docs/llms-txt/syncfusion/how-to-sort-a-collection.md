# Source: https://docs.syncfusion.com/windowsforms/grouping/faq/how-to-sort-a-collection.md

# How to Sort a Collection

To sort your data, add the name of the property that you want to sort to the Engine.TableDescriptor.SortedColumns collection.

{% tabs %}
{% highlight C# %}
 
// Sort column A.
groupingEngine.TableDescriptor.SortedColumns.Add("A");
 
{% endhighlight %}

{% highlight vb %}
 
' Sort column A.
groupingEngine.TableDescriptor.SortedColumns.Add("A")

{% endhighlight %}
{% endtabs %}
