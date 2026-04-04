# Source: https://docs.syncfusion.com/wpf/olap-common/how-to/showhide-the-expander-buttons-in-olap-controls.md

# Show/hide the Expander buttons in OLAP controls

There is a property in OlapReport called ShowExpanders, which is used to show/hide the expander buttons in the OLAP controls. By using this property, we can disable or enable the drill down/up behavior of the OLAP control. 

To show the Expanders:

{% tabs %}
{% highlight c# %}



Â //// Displaying the Expander button in Controls
Â olapReport.ShowExpandersÂ =Â true;


{% endhighlight  %}


{% highlight vbnet %}



'Displaying the Expander button in Controls

olapReport.ShowExpandersÂ =Â True 



{% endhighlight  %}
{% endtabs %}

To hide the Expanders: 

{% tabs %}
{% highlight c# %}



Â //// Displaying the Expander button in Controls
Â olapReport.ShowExpandersÂ =Â false;



{% endhighlight  %}

{% highlight vbnet %}



'Displaying the Expander button in Controls

olapReport.ShowExpandersÂ =Â False 




{% endhighlight  %}
{% endtabs %}