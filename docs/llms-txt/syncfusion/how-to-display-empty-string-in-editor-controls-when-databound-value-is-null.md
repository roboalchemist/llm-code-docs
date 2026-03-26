# Source: https://docs.syncfusion.com/windowsforms/integer-textbox/faq/how-to-display-empty-string-in-editor-controls-when-databound-value-is-null.md

# How to display empty string in editor controls when data bound value is null

We can display empty string when data bound value is null. For this we need to bind the editor controls (like IntegerTextBox, DoubleTextBox, etc.,) toÂ BindableValueÂ property and also we need to setÂ [AllowNull](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.NumberTextBoxBase.html#Syncfusion_Windows_Forms_Tools_NumberTextBoxBase_AllowNull)Â to true andÂ [NullString](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.NumberTextBoxBase.html#Syncfusion_Windows_Forms_Tools_NumberTextBoxBase_NullString)Â property to empty string.

Find the code snippet below, which illustrates the same.

{% tabs %}
{% highlight C# %}
this.integerTextBox1.NullString =Â "";
this.integerTextBox1.AllowNull =Â true;
this.integerTextBox1.DataBindings.Add("BindableValue", boundView,Â "IntegerField");
{% endhighlight %}
{% highlight VB %}
Me.integerTextBox1.NullString =Â ""
Me.integerTextBox1. AllowNull =Â True
Me.integerTextBox1.DataBindings.Add("BindableValue", boundView,Â "IntegerField")
{% endhighlight %}
{% endtabs %}
