# Source: https://docs.syncfusion.com/windowsforms/grouping/faq/how-to-group-a-collection.md

# How to Group a Collection

To sort your data, add the name of the property you want to sort to the Engine.TableDescriptor.GroupedColumns collection. 

{% tabs %}
{% highlight C# %}

// Group column A.
groupingEngine.TableDescriptor.GroupedColumns.Add("A");

{% endhighlight %}
 
{% highlight vb %}
 
' Group column A.
groupingEngine.TableDescriptor.GroupedColumns.Add("A")
{% endhighlight %}
{% endtabs %}
