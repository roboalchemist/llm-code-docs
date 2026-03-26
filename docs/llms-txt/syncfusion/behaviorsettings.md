# Source: https://docs.syncfusion.com/windowsforms/integer-textbox/behaviorsettings.md

# Behavior Settings in Windows Forms Integer TextBox

The behavior settings of the IntegerTextBox control are discussed below.

## Negative key settings

The integer value of the IntegerTextBox can be reset or changed to a negative value using the properties given below.

* [DeleteSelectionOnNegative](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.NumericTextBox.html#Syncfusion_Windows_Forms_Tools_NumericTextBox_DeleteSelectionOnNegative)
* [NegativeInputPendingOnSelectAll](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.NumberTextBoxBase.html#Syncfusion_Windows_Forms_Tools_NumberTextBoxBase_NegativeInputPendingOnSelectAll)

{% tabs %}
{% highlight C# %}
this.integerTextBox1.DeleteSelectionOnNegative =Â true;
this.integerTextBox1.NegativeInputPendingOnSelectAll =Â true;
{% endhighlight %}
{% highlight VB %}
Me.integerTextBox1.DeleteSelectionOnNegative =Â True
Me.integerTextBox1.NegativeInputPendingOnSelectAll =Â True
{% endhighlight %}
{% endtabs %}

## AllowLeadingZeros

The [AllowLeadingZeros](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.IntegerTextBox.html#Syncfusion_Windows_Forms_Tools_IntegerTextBox_AllowLeadingZeros) property can be used to include zeros before the beginning value of the integer value of the control.

{% tabs %}
{% highlight C# %}
this.integerTextBox1.AllowLeadingZeros =Â true;
{% endhighlight %}
{% highlight VB %}
Me.integerTextBox1.AllowLeadingZeros =Â True
{% endhighlight %}
{% endtabs %}

![AllowLeadingZeros](Overview_images/Overview_img457.png) 
