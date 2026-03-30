# Source: https://docs.syncfusion.com/windowsforms/integer-textbox/integertextboxevents.md

# Integertextbox Events in Windows Forms Integer TextBox

The list of events and a detailed explanation about each of them is given in the following sections.

* [BindableValueChanged](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.NumberTextBoxBase.html)
* [ClipTextChanged](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.NumberTextBoxBase.html)
* [FormattedTextChanged](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.NumberTextBoxBase.html)
* [IntegerValueChanged](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.IntegerTextBox.html)
* [SetNull](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.NumberTextBoxBase.html)
* [ValidationError](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.NumberTextBoxBase.html)

## BindableValueChanged

This [BindableValueChanged](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.NumberTextBoxBase.html) event occurs when theÂ [BindableValue](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.NumberTextBoxBase.html#Syncfusion_Windows_Forms_Tools_NumberTextBoxBase_BindableValue)Â property is changed. The [BindableValue](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.NumberTextBoxBase.html#Syncfusion_Windows_Forms_Tools_NumberTextBoxBase_BindableValue) property is a wrapper property that indicates the value. This property can be used to set the value of the control to 'Null'.

The event handler receives an argument of typeÂ EventArgsÂ containing data related to this event.

{% tabs %}
{% highlight C# %}
privateÂ voidÂ integerTextBox1_BindableValueChanged(objectÂ sender,Â EventArgsÂ e)
{
    Console.WriteLine(" BindableValueChanged event is raised ");
}
{% endhighlight %}
{% highlight VB %}
PrivateÂ SubÂ integerTextBox1_BindableValueChanged(ByValÂ senderÂ AsÂ Object,Â ByValÂ eÂ AsÂ EventArgs)
Console.WriteLine(" BindableValueChanged event is raised ")
EndÂ Sub
{% endhighlight %}
{% endtabs %}

## ClipTextChanged

This [ClipTextChanged](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.NumberTextBoxBase.html) event occurs when theÂ [ClipText](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.NumberTextBoxBase.html#Syncfusion_Windows_Forms_Tools_NumberTextBoxBase_ClipText)Â property is changed. The [ClipText](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.NumberTextBoxBase.html#Syncfusion_Windows_Forms_Tools_NumberTextBoxBase_ClipText) property returns the clipped text without the formatting.

The event handler receives an argument of typeÂ EventArgsÂ containing data related to this event.

{% tabs %}
{% highlight C# %}
privateÂ voidÂ integerTextBox1_ClipTextChanged(objectÂ sender,Â EventArgsÂ e)
{
    Console.WriteLine(" ClipTextChanged event is raised ");
}
{% endhighlight %}
{% highlight VB %}
PrivateÂ SubÂ integerTextBox1_ClipTextChanged(ByValÂ senderÂ AsÂ Object,Â ByValÂ eÂ AsÂ EventArgs)
Console.WriteLine(" ClipTextChanged event is raised ")
EndÂ Sub
{% endhighlight %}
{% endtabs %}

## FormattedTextChanged

This [FormattedTextChanged](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.NumberTextBoxBase.html) event occurs when theÂ [FormattedText](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.NumberTextBoxBase.html#Syncfusion_Windows_Forms_Tools_NumberTextBoxBase_FormattedText)Â property is changed. The [FormattedText](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.NumberTextBoxBase.html#Syncfusion_Windows_Forms_Tools_NumberTextBoxBase_FormattedText) property returns the formatted text with the formatting.

The event handler receives an argument of typeÂ EventArgsÂ containing data related to this event.

{% tabs %}
{% highlight C# %}
privateÂ voidÂ integerTextBox1_FormattedTextChanged(objectÂ sender,Â EventArgsÂ e)
{
    Console.WriteLine(" FormattedTextChanged event is raised ");
}
{% endhighlight %}
{% highlight VB %}
PrivateÂ SubÂ integerTextBox1_FormattedTextChanged(ByValÂ senderÂ AsÂ Object,Â ByValÂ eÂ AsÂ EventArgs)
Console.WriteLine(" FormattedTextChanged event is raised ")
EndÂ Sub
{% endhighlight %}
{% endtabs %}

## IntegerValueChanged

This [IntegerValueChanged](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.IntegerTextBox.html) event occurs when theÂ [IntegerValue](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.IntegerTextBox.html#Syncfusion_Windows_Forms_Tools_IntegerTextBox_IntegerValue)Â property is changed. The [IntegerValue](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.IntegerTextBox.html#Syncfusion_Windows_Forms_Tools_IntegerTextBox_IntegerValue) property specifies the integer value of the text.

The event handler receives an argument of typeÂ EventArgsÂ containing data related to this event.

{% tabs %}
{% highlight C# %}
privateÂ voidÂ integerTextBox1_IntegerValueChanged(objectÂ sender,Â EventArgsÂ e)
{
    Console.WriteLine(" IntegerValueChanged event is raised ");
}
{% endhighlight %}
{% highlight VB %}
PrivateÂ SubÂ integerTextBox1_IntegerValueChanged(ByValÂ senderÂ AsÂ Object,Â ByValÂ eÂ AsÂ EventArgs)
Console.WriteLine(" IntegerValueChanged event is raised ")
EndÂ Sub
{% endhighlight %}
{% endtabs %}

## SetNull

This event occurs when the [NULLState](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.NumberTextBoxBase.html#Syncfusion_Windows_Forms_Tools_NumberTextBoxBase_NullState) is to be set based on a value.

The event handler receives an argument of typeÂ [SetNullEventArgs](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.SetNullEventArgs.html)Â containing data related to this event. The following [SetNullEventArgs](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.SetNullEventArgs.html)Â members provide information specific to this event.

<table>
<tr>
<th>
Members</th><th>
Description</th></tr>
<tr>
<td>
Cancel</td><td>
Gets / sets a value indicating whether the event should be canceled.</td></tr>
<tr>
<td>
NullValue</td><td>
Returns the NULL value.</td></tr>
</table>

{% tabs %}
{% highlight C# %}
privateÂ voidÂ integerTextBox1_SetNull(objectÂ sender, Syncfusion.Windows.Forms.Tools.SetNullEventArgsÂ e)
{
    Console.WriteLine(" SetNull event is raised ");
}
{% endhighlight %}
{% highlight VB %}
PrivateÂ SubÂ integerTextBox1_SetNull(ByValÂ senderÂ AsÂ Object,Â ByValÂ eÂ AsSyncfusion.Windows.Forms.Tools.SetNullEventArgs)
Console.WriteLine(" SetNull event is raised ")
EndÂ Sub
{% endhighlight %}
{% endtabs %}

## ValidationError

This [ValidationError](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.NumberTextBoxBase.html) event occurs when the input text is invalid for the current state of the control.

The event handler receives an argument of typeÂ ValidationErrorArgsÂ containing data related to this event. The following ValidationErrorArgsÂ members provide information specific to this event.

<table>
<tr>
<th>
Members</th><th>
Description</th></tr>
<tr>
<td>
ErrorMessage</td><td>
Returns the error message.</td></tr>
<tr>
<td>
InvalidText</td><td>
Returns the invalid text as it would have been if the error had not intercepted it.</td></tr>
<tr>
<td>
StartPosition</td><td>
Returns the location of the invalid input in the invalid text.</td></tr>
</table>

{% tabs %}
{% highlight C# %}
privateÂ voidÂ integerTextBox1_ValidationError(objectÂ sender, Syncfusion.Windows.Forms.Tools.ValidationErrorArgsÂ e)
{
    Console.WriteLine(" ValidationError event is raised ");
}
{% endhighlight %}
{% highlight VB %}
PrivateÂ SubÂ integerTextBox1_ValidationError(ByValÂ senderÂ AsÂ Object,Â ByValÂ eÂ AsSyncfusion.Windows.Forms.Tools.ValidationErrorArgs)
Console.WriteLine(" ValidationError event is raised ")
EndÂ Sub
{% endhighlight %}
{% endtabs %}
