# Source: https://docs.syncfusion.com/wpf/olap-common/how-to/add-usewhereclauseforslicing-to-an-application.md

# Add UseWhereClauseForSlicing to an Application

The user can add the UseWhereClauseForSlicing property to an application by setting the property to a Boolean value.  To perform the slicing operation using the âWhereâ clause, set the property to _true_. To perform the slicing operation using the âSelectâ clause, set the property to _false_.  By default, the value of the UseWhereClauseForSlicing property is _true_.



To perform slicing operation using âWhereâ clause:

{% tabs %}
{% highlight c# %}

OlapDataManager.UseWhereClauseForSlicing = true;

{% endhighlight  %}

{% highlight vbnet %}

OlapDataManager.UseWhereClauseForSlicing = True 

{% endhighlight  %}
{% endtabs %}

To perform slicing operation using âSelectâ clause:
{% tabs %}
{% highlight c# %}

this.olapGridControl1.OlapDataManager.UseWhereClauseForSlicing = false;


{% endhighlight  %}
{% highlight vbnet %}

Me.olapGridControl1.OlapDataManager.UseWhereClauseForSlicing = False

{% endhighlight  %}
{% endtabs %}
