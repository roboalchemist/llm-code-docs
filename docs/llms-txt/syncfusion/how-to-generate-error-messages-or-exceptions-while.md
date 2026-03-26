# Source: https://docs.syncfusion.com/windowsforms/calculation-engine/faq/common/how-to-generate-error-messages-or-exceptions-while.md

# How to generate error messages or exceptions while performing String-related calculations?

Normally the CalcEngine will not display an invalid error message or exception while performing mathematical operations with string or text. To generate an invalid error message or exception, the TreatStringAsZero property must be set to _false_.

For example, if a string is multiplied with a number (for example, âtextâ * 10), the calculated result will be zero. But, if the TreatStringAsZero property is set to _false,_ the â#VALUE!â exception will be generated.

{% highlight c# %}



this.engine.TreatStringsAsZero = false;

{% endhighlight %}

{% highlight vbnet %}



Me.engine.TreatStringsAsZero = False


{% endhighlight %}


