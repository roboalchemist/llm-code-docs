# Source: https://docs.syncfusion.com/windowsforms/grid-control/how-to/general/how-to-control-the-way-grid-handles-exceptions.md

# How to control the way Grid handles exceptions

Syncfusion.Windows.Forms.ExceptionManager has static members that you can use to control how the grid handles exceptions. 

To suspend the grid's error handling, try.

{% tabs %}
{% highlight c# %}

//Suspends Grid's Error Handling.
Syncfusion.Windows.Forms.ExceptionManager.SuspendCatchExceptions()

{% endhighlight %}

{% highlight vb %}

'Suspends Grid's Error Handling.
Syncfusion.Windows.Forms.ExceptionManager.SuspendCatchExceptions()

{% endhighlight %}
{% endtabs %}

N> You can also subscribe to an event (Syncfusion.Windows.Forms.ExceptionManager.ExceptionCatched) to get any exception thrown and handle them by yourself or re-throw them.
