# Source: https://docs.syncfusion.com/windowsforms/autocomplete/faq/how-to-delete-the-items-in-the-list-at-run-time.md

# How to delete the items in the list at runtime?

You can delete items in the list at runtime by enabling the AllowListDelete property and then pressing the Delete key.


{% highlight C# %}


this.autoComplete1.AllowListDelete = true;

{% endhighlight %}



{% highlight vbnet %}





Me.autoComplete1.AllowListDelete = True
{% endhighlight %}