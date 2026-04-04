# Source: https://docs.syncfusion.com/windowsforms/percent-textbox/percenttextbox-events.md

# PercentTextBox Events in Windows Forms Percent TextBox

The list of events and a detailed explanation about each of them is given in the following sections.

* [BindablePercentValueChanged](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.PercentTextBox.html)
* [BindableValueChanged](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.NumberTextBoxBase.html)
* [Border3DStyleChanged](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.TextBoxExt.html)
* [BorderColorChanged](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.TextBoxExt.html)
* [BorderSidesChanged](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.TextBoxExt.html)
* [BorderStyleChanged](https://docs.microsoft.com/en-us/dotnet/api/system.windows.forms.textboxbase.borderstylechanged?redirectedfrom=MSDN&view=netframework-4.7.2)
* [ClipTextChanged](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.NumberTextBoxBase.html)
* [DoubleValueChanged](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.PercentTextBox.html)
* [FormattedTextChanged](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.NumberTextBoxBase.html)
* [HideSelectionChanged](https://docs.microsoft.com/en-us/dotnet/api/system.windows.forms.textboxbase.hideselectionchanged?redirectedfrom=MSDN&view=netframework-4.7.2)
* [MinimumSizeChanged](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.TextBoxExt.html)
* [MaximumSizeChanged](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.TextBoxExt.html)
* [MultilineChanged](https://docs.microsoft.com/en-us/dotnet/api/system.windows.forms.textboxbase.multilinechanged?redirectedfrom=MSDN&view=netframework-4.7.2)
* [ReadOnlyChanged](https://docs.microsoft.com/en-us/dotnet/api/system.windows.forms.textboxbase.readonlychanged?redirectedfrom=MSDN&view=netframework-4.7.2)
* [RightToLeftChanged](https://docs.microsoft.com/en-us/dotnet/api/system.windows.forms.control.righttoleftchanged?redirectedfrom=MSDN&view=netframework-4.7.2)
* [SetNull](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.NumberTextBoxBase.html)
* [TextAlignChanged](https://docs.microsoft.com/en-us/dotnet/api/system.windows.forms.textbox.textalignchanged?redirectedfrom=MSDN&view=netframework-4.7.2)
* [ThemesEnabledChanged](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.TextBoxExt.html)
* [ValidationError](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.NumberTextBoxBase.html)

## BindablePercentValueChanged

This [BindablePercentValueChanged](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.PercentTextBox.html) event occurs when theÂ [BindablePercentValue](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.PercentTextBox.html#Syncfusion_Windows_Forms_Tools_PercentTextBox_BindablePercentValue)Â property is changed. The [BindablePercentValue](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.PercentTextBox.html#Syncfusion_Windows_Forms_Tools_PercentTextBox_BindablePercentValue) property is a wrapper property that indicates the percent value. This property can be used to set the value of the control to 'Null'.

The event handler receives an argument of typeÂ EventArgsÂ containing data related to this event.

{% tabs %}
{% highlight C# %}
privateÂ voidÂ percentTextBox1_BindablePercentValueChanged(objectÂ sender,Â EventArgsÂ e)
{
    Console.WriteLine(" BindablePercentValueChanged event is raised ");
}
{% endhighlight %}
{% highlight vb %}
PrivateÂ SubÂ percentTextBox1_BindablePercentValueChanged(ByValÂ senderÂ AsÂ Object,Â ByValÂ eÂ AsÂ EventArgs)
Console.WriteLine(" BindablePercentValueChanged event is raised ")
EndÂ Sub
{% endhighlight %}
{% endtabs %}

## BindableValueChanged 

This [BindableValueChanged](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.NumberTextBoxBase.html) event occurs when theÂ [BindableValue](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.NumberTextBoxBase.html#Syncfusion_Windows_Forms_Tools_NumberTextBoxBase_BindableValue)Â property is changed. The [BindableValue](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.NumberTextBoxBase.html#Syncfusion_Windows_Forms_Tools_NumberTextBoxBase_BindableValue) property is a wrapper property that indicates the value. This property can be used to set the value of the control to 'Null'.

The event handler receives an argument of typeÂ EventArgsÂ containing data related to this event.

{% tabs %}
{% highlight C# %}
privateÂ voidÂ percentTextBox1_BindableValueChanged(objectÂ sender,Â EventArgsÂ e)
{
    Console.WriteLine(" BindableValueChanged event is raised ");
}
{% endhighlight %}
{% highlight VB %}
PrivateÂ SubÂ percentTextBox1_BindableValueChanged(ByValÂ senderÂ AsÂ Object,Â ByValÂ eÂ AsÂ EventArgs)
Console.WriteLine(" BindableValueChanged event is raised ")
EndÂ Sub
{% endhighlight %}
{% endtabs %}

## Border3DStyleChanged

This [Border3DStyleChanged](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.TextBoxExt.html) event occurs when theÂ [Border3DStyle](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.TextBoxExt.html#Syncfusion_Windows_Forms_Tools_TextBoxExt_Border3DStyle)Â property is changed. The [Border3DStyle](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.TextBoxExt.html#Syncfusion_Windows_Forms_Tools_TextBoxExt_Border3DStyle) property indicates the style of the 3D border.

The event handler receives an argument of typeÂ EventArgsÂ containing data related to this event.

{% tabs %}
{% highlight C# %}
privateÂ voidÂ percentTextBox1_Border3DStyleChanged(objectÂ sender,Â EventArgsÂ e)
{
    Console.WriteLine(" Border3DStyleChanged event is raised ");
}
{% endhighlight %}
{% highlight vb %}
PrivateÂ SubÂ percentTextBox1_Border3DStyleChanged(ByValÂ senderÂ AsÂ Object,Â ByValÂ eÂ AsÂ EventArgs)
Console.WriteLine(" Border3DStyleChanged event is raised ")
EndÂ Sub
{% endhighlight %}
{% endtabs %}

## BorderColorChanged 

This [BorderColorChanged](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.TextBoxExt.html) event occurs when theÂ [BorderColor](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.TextBoxExt.html#Syncfusion_Windows_Forms_Tools_TextBoxExt_BorderColor)Â property is changed. The [BorderColor](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.TextBoxExt.html#Syncfusion_Windows_Forms_Tools_TextBoxExt_BorderColor) property indicates the color of the 2D border.

The event handler receives an argument of typeÂ EventArgsÂ containing data related to this event.

{% tabs %}
{% highlight C# %}
privateÂ voidÂ percentTextBox1_BorderColorChanged(objectÂ sender,Â EventArgsÂ e)
{
    Console.WriteLine(" BorderColorChanged event is raised ");
}
{% endhighlight %}
{% highlight VB %}
PrivateÂ SubÂ percentTextBox1_BorderColorChanged(ByValÂ senderÂ AsÂ Object,Â ByValÂ eÂ AsÂ EventArgs)
Console.WriteLine(" BorderColorChanged event is raised ")
EndÂ Sub
{% endhighlight %}
{% endtabs %}

## BorderSidesChanged 

This [BorderSidesChanged](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.TextBoxExt.html) event occurs when theÂ [BorderSides](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.TextBoxExt.html#Syncfusion_Windows_Forms_Tools_TextBoxExt_BorderSides)Â property is changed. The [BorderSides](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.TextBoxExt.html#Syncfusion_Windows_Forms_Tools_TextBoxExt_BorderSides) property indicates the border sides of the panel.

The event handler receives an argument of typeÂ EventArgsÂ containing data related to this event.

{% tabs %}
{% highlight C# %}

privateÂ voidÂ percentTextBox1_BorderSidesChanged(objectÂ sender,Â EventArgsÂ e)
{
    Console.WriteLine(" BorderSidesChanged event is raised ");
}

{% endhighlight %}

{% highlight vb %}

PrivateÂ SubÂ percentTextBox1_BorderSidesChanged(ByValÂ senderÂ AsÂ Object,Â ByValÂ eÂ AsÂ EventArgs)
Console.WriteLine(" BorderSidesChanged event is raised ")
EndÂ Sub

{% endhighlight %}
{% endtabs %}

## BorderStyleChanged 

This [BorderStyleChanged](https://docs.microsoft.com/en-us/dotnet/api/system.windows.forms.textboxbase.borderstylechanged?redirectedfrom=MSDN&view=netframework-4.7.2) event occurs when theÂ [BorderStyle](https://docs.microsoft.com/en-us/dotnet/api/system.windows.forms.textboxbase.borderstyle?redirectedfrom=MSDN&view=netframework-4.7.2#System_Windows_Forms_TextBoxBase_BorderStyle)Â property is changed. The [BorderStyle](https://docs.microsoft.com/en-us/dotnet/api/system.windows.forms.textboxbase.borderstyle?redirectedfrom=MSDN&view=netframework-4.7.2#System_Windows_Forms_TextBoxBase_BorderStyle) property indicates whether the edit control should have a border.

The event handler receives an argument of typeÂ EventArgsÂ containing data related to this event.

{% tabs %}
{% highlight C# %}

privateÂ voidÂ percentTextBox1_BorderStyleChanged(objectÂ sender,Â EventArgsÂ e)
{
    Console.WriteLine(" BorderStyleChanged event is raised ");
}

{% endhighlight %}

{% highlight vb %}

PrivateÂ SubÂ percentTextBox1_BorderStyleChanged(ByValÂ senderÂ AsÂ Object,Â ByValÂ eÂ AsÂ EventArgs)
Console.WriteLine(" BorderStyleChanged event is raised ")
EndÂ Sub

{% endhighlight %}
{% endtabs %}

## ClipTextChanged 

This [ClipTextChanged](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.NumberTextBoxBase.html) event occurs when theÂ [ClipText](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.PercentTextBox.html#Syncfusion_Windows_Forms_Tools_PercentTextBox_ClipText)Â property is changed. The [ClipText](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.PercentTextBox.html#Syncfusion_Windows_Forms_Tools_PercentTextBox_ClipText) property returns the clipped text without the formatting.

The event handler receives an argument of typeÂ EventArgsÂ containing data related to this event.

{% tabs %}
{% highlight C# %}
privateÂ voidÂ percentTextBox1_ClipTextChanged(objectÂ sender,Â EventArgsÂ e)
{
    Console.WriteLine(" ClipTextChanged event is raised ");
}
{% endhighlight %}
{% highlight vb %}
PrivateÂ SubÂ percentTextBox1_ClipTextChanged(ByValÂ senderÂ AsÂ Object,Â ByValÂ eÂ AsÂ EventArgs)
Console.WriteLine(" ClipTextChanged event is raised ")
EndÂ Sub
{% endhighlight %}
{% endtabs %}

## DoubleValueChanged

This [DoubleValueChanged](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.PercentTextBox.html) event occurs when theÂ [DoubleValue](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.PercentTextBox.html#Syncfusion_Windows_Forms_Tools_PercentTextBox_DoubleValue)Â property is changed. The [DoubleValue](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.PercentTextBox.html#Syncfusion_Windows_Forms_Tools_PercentTextBox_DoubleValue) property specifies the double value of the PercentTextBox control.

The event handler receives an argument of typeÂ EventArgsÂ containing data related to this event.

{% tabs %}
{% highlight C# %}

privateÂ voidÂ percentTextBox1_FormattedTextChanged(objectÂ sender,Â EventArgsÂ e)
{
    Console.WriteLine(" DoubleValueChanged event is raised ");
}

{% endhighlight %}

{% highlight vb %}

PrivateÂ SubÂ percentTextBox1_FormattedTextChanged(ByValÂ senderÂ AsÂ Object,Â ByValÂ eÂ AsÂ EventArgs)
Console.WriteLine(" DoubleValueChanged event is raised ")
EndÂ Sub

{% endhighlight %}
{% endtabs %}

## FormattedTextChanged

This [FormattedTextChanged](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.NumberTextBoxBase.html) event occurs when theÂ [FormattedText](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.PercentTextBox.html#Syncfusion_Windows_Forms_Tools_PercentTextBox_FormattedText)Â property is changed. The [FormattedText](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.PercentTextBox.html#Syncfusion_Windows_Forms_Tools_PercentTextBox_FormattedText) property returns the formatted text with the formatting.

The event handler receives an argument of typeÂ EventArgsÂ containing data related to this event.

{% tabs %}
{% highlight C# %}

privateÂ voidÂ percentTextBox1_FormattedTextChanged(objectÂ sender,Â EventArgsÂ e)
{
    Console.WriteLine(" FormattedTextChanged event is raised ");
}

{% endhighlight %}

{% highlight vb %}

PrivateÂ SubÂ percentTextBox1_FormattedTextChanged(ByValÂ senderÂ AsÂ Object,Â ByValÂ eÂ AsÂ EventArgs)
Console.WriteLine(" FormattedTextChanged event is raised ")
EndÂ Sub

{% endhighlight %}
{% endtabs %}

## HideSelectionChanged 

This [HideSelectionChanged](https://docs.microsoft.com/en-us/dotnet/api/system.windows.forms.textboxbase.hideselectionchanged?redirectedfrom=MSDN&view=netframework-4.7.2) event occurs when theÂ [HideSelection](https://docs.microsoft.com/en-us/dotnet/api/system.windows.forms.textboxbase.hideselection?redirectedfrom=MSDN&view=netframework-4.7.2#System_Windows_Forms_TextBoxBase_HideSelection)Â property is changed. The [HideSelection](https://docs.microsoft.com/en-us/dotnet/api/system.windows.forms.textboxbase.hideselection?redirectedfrom=MSDN&view=netframework-4.7.2#System_Windows_Forms_TextBoxBase_HideSelection) property indicates that the selection should be hidden when the edit control loses focus.

The event handler receives an argument of typeÂ EventArgsÂ containing data related to this event.

{% tabs %}
{% highlight C# %}

privateÂ voidÂ percentTextBox1_HideSelectionChanged(objectÂ sender,Â EventArgsÂ e)
{
    Console.WriteLine(" HideSelectionChanged event is raised ");
}

{% endhighlight %}

{% highlight vb %}

PrivateÂ SubÂ percentTextBox1_HideSelectionChanged(ByValÂ senderÂ AsÂ Object,Â ByValÂ eÂ AsÂ EventArgs)
Console.WriteLine(" HideSelectionChanged event is raised ")
EndÂ Sub

{% endhighlight %}
{% endtabs %}

## MinimumSizeChanged 

This [MinimumSizeChanged](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.TextBoxExt.html) event occurs when theÂ [MinimumSize](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.TextBoxExt.html#Syncfusion_Windows_Forms_Tools_TextBoxExt_MinimumSize)Â property is changed. The [MinimumSize](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.TextBoxExt.html#Syncfusion_Windows_Forms_Tools_TextBoxExt_MinimumSize) property gets / sets the minimum size of the control.

The event handler receives an argument of typeÂ EventArgsÂ containing data related to this event.

{% tabs %}
{% highlight C# %}

privateÂ voidÂ percentTextBox1_MinimumSizeChanged(objectÂ sender,Â EventArgsÂ e)
{
    Console.WriteLine(" MinimumSizeChanged event is raised ");
}

{% endhighlight %}

{% highlight vb %}

PrivateÂ SubÂ percentTextBox1_MinimumSizeChanged(ByValÂ senderÂ AsÂ Object,Â ByValÂ eÂ AsÂ EventArgs)
Console.WriteLine(" MinimumSizeChanged event is raised ")
EndÂ Sub

{% endhighlight %}
{% endtabs %}

## MaximumSizeChanged 

This [MaximumSizeChanged](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.TextBoxExt.html) event occurs when theÂ [MaximumSize](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.TextBoxExt.html#Syncfusion_Windows_Forms_Tools_TextBoxExt_MaximumSize)Â property is changed. The [MaximumSize](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.TextBoxExt.html#Syncfusion_Windows_Forms_Tools_TextBoxExt_MaximumSize) property gets / sets the maximum size of the control.

The event handler receives an argument of typeÂ EventArgsÂ containing data related to this event.

{% tabs %}
{% highlight C# %}

privateÂ voidÂ percentTextBox1_MaximumSizeChanged(objectÂ sender,Â EventArgsÂ e)
{
    Console.WriteLine(" MaximumSizeChanged event is raised ");
}

{% endhighlight %}

{% highlight vb %}

PrivateÂ SubÂ percentTextBox1_MaximumSizeChanged(ByValÂ senderÂ AsÂ Object,Â ByValÂ eÂ AsÂ EventArgs)
Console.WriteLine(" MaximumSizeChanged event is raised ")
EndÂ Sub

{% endhighlight %}
{% endtabs %}

## MultilineChanged 

This [MultilineChanged](https://docs.microsoft.com/en-us/dotnet/api/system.windows.forms.textboxbase.multilinechanged?redirectedfrom=MSDN&view=netframework-4.7.2) event occurs when theÂ [Multiline](https://docs.microsoft.com/en-us/dotnet/api/system.windows.forms.textbox.multiline?redirectedfrom=MSDN&view=netframework-4.7.2#System_Windows_Forms_TextBox_Multiline)Â property is changed. The [Multiline](https://docs.microsoft.com/en-us/dotnet/api/system.windows.forms.textbox.multiline?redirectedfrom=MSDN&view=netframework-4.7.2#System_Windows_Forms_TextBox_Multiline) property controls whether the text of the edit control can span more than one line.

The event handler receives an argument of typeÂ EventArgsÂ containing data related to this event.

{% tabs %}
{% highlight C# %}

privateÂ voidÂ percentTextBox1_MultilineChanged(objectÂ sender,Â EventArgsÂ e)
{
    Console.WriteLine(" MultilineChanged event is raised ");
}

{% endhighlight %}

{% highlight vb %}

PrivateÂ SubÂ percentTextBox1_MultilineChanged(ByValÂ senderÂ AsÂ Object,Â ByValÂ eÂ AsÂ EventArgs)
Console.WriteLine(" MultilineChanged event is raised ")
EndÂ Sub

{% endhighlight %}
{% endtabs %}

## ReadOnlyChanged 

This [ReadOnlyChanged](https://docs.microsoft.com/en-us/dotnet/api/system.windows.forms.textboxbase.readonlychanged?redirectedfrom=MSDN&view=netframework-4.7.2) event occurs when theÂ [ReadOnly](https://docs.microsoft.com/en-us/dotnet/api/system.windows.forms.textboxbase.readonly?redirectedfrom=MSDN&view=netframework-4.7.2#System_Windows_Forms_TextBoxBase_ReadOnly)Â property is changed. The [ReadOnly](https://docs.microsoft.com/en-us/dotnet/api/system.windows.forms.textboxbase.readonly?redirectedfrom=MSDN&view=netframework-4.7.2#System_Windows_Forms_TextBoxBase_ReadOnly) property controls whether the text in the edit control can be changed or not.

The event handler receives an argument of typeÂ EventArgsÂ containing data related to this event.

{% tabs %}
{% highlight C# %}

privateÂ voidÂ percentTextBox1_ReadOnlyChanged(objectÂ sender,Â EventArgsÂ e)
{
    Console.WriteLine(" ReadOnlyChanged event is raised ");
}

{% endhighlight %}

{% highlight vb %}

PrivateÂ SubÂ percentTextBox1_ReadOnlyChanged(ByValÂ senderÂ AsÂ Object,Â ByValÂ eÂ AsÂ EventArgs)
Console.WriteLine(" ReadOnlyChanged event is raised ")
EndÂ Sub

{% endhighlight %}
{% endtabs %}

## RightToLeftChanged 

This [RightToLeftChanged](https://docs.microsoft.com/en-us/dotnet/api/system.windows.forms.control.righttoleftchanged?redirectedfrom=MSDN&view=netframework-4.7.2) event occurs when theÂ [RightToLeft](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.NumberTextBoxBase.html#Syncfusion_Windows_Forms_Tools_NumberTextBoxBase_RightToLeft)Â property is changed. The [RightToLeft](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.NumberTextBoxBase.html#Syncfusion_Windows_Forms_Tools_NumberTextBoxBase_RightToLeft) property indicates whether the components should be drawn right-to-left for RTL languages.

The event handler receives an argument of typeÂ EventArgsÂ containing data related to this event.

{% tabs %}
{% highlight C# %}

privateÂ voidÂ percentTextBox1_RightToLeftChanged(objectÂ sender,Â EventArgsÂ e)
{
    Console.WriteLine(" RightToLeftChanged event is raised ");
}

{% endhighlight %}

{% highlight vb %}

PrivateÂ SubÂ percentTextBox1_RightToLeftChanged(ByValÂ senderÂ AsÂ Object,Â ByValÂ eÂ AsÂ EventArgs)
Console.WriteLine(" RightToLeftChanged event is raised ")
EndÂ Sub

{% endhighlight %}
{% endtabs %}

## SetNull 

This [SetNull](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.NumberTextBoxBase.html) event occurs when the NULL state is to be set based on a value.

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

privateÂ voidÂ percentTextBox1_SetNull(objectÂ sender, Syncfusion.Windows.Forms.Tools.SetNullEventArgsÂ e)
{
    Console.WriteLine(" SetNull event is raised ");
}

{% endhighlight %}

{% highlight vb %}

PrivateÂ SubÂ percentTextBox1_SetNull(ByValÂ senderÂ AsÂ Object,Â ByValÂ eÂ AsSyncfusion.Windows.Forms.Tools.SetNullEventArgs)
Console.WriteLine(" SetNull event is raised ")
EndÂ Sub

{% endhighlight %}
{% endtabs %}

## TextAlignChanged 

This [TextAlignChanged](https://docs.microsoft.com/en-us/dotnet/api/system.windows.forms.textbox.textalignchanged?redirectedfrom=MSDN&view=netframework-4.7.2) event occurs when theÂ [TextAlign](https://docs.microsoft.com/en-us/dotnet/api/system.windows.forms.textbox.textalign?redirectedfrom=MSDN&view=netframework-4.7.2#System_Windows_Forms_TextBox_TextAlign)Â property is changed. The [TextAlign](https://docs.microsoft.com/en-us/dotnet/api/system.windows.forms.textbox.textalign?redirectedfrom=MSDN&view=netframework-4.7.2#System_Windows_Forms_TextBox_TextAlign) property indicates how the text should be aligned for edit controls.

The event handler receives an argument of typeÂ EventArgsÂ containing data related to this event.

{% tabs %}
{% highlight C# %}

privateÂ voidÂ percentTextBox1_TextAlignChanged(objectÂ sender,Â EventArgsÂ e)
{
    Console.WriteLine(" TextAlignChanged event is raised ");
}

{% endhighlight %}

{% highlight vb %}

PrivateÂ SubÂ percentTextBox1_TextAlignChanged(ByValÂ senderÂ AsÂ Object,Â ByValÂ eÂ AsÂ EventArgs)
Console.WriteLine(" TextAlignChanged event is raised ")
EndÂ Sub

{% endhighlight %}
{% endtabs %}

## ThemesEnabledChanged 

This [ThemesEnabledChanged](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.TextBoxExt.html) event occurs when theÂ [ThemesEnabled](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.TextBoxExt.html#Syncfusion_Windows_Forms_Tools_TextBoxExt_ThemesEnabled)Â property is changed. The [ThemesEnabled](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.TextBoxExt.html#Syncfusion_Windows_Forms_Tools_TextBoxExt_ThemesEnabled) property specifies whether or not to use XP Themes when theÂ [BorderStyle](https://docs.microsoft.com/en-us/dotnet/api/system.windows.forms.textboxbase.borderstyle?redirectedfrom=MSDN&view=netframework-4.7.2#System_Windows_Forms_TextBoxBase_BorderStyle)Â property is set to 'Fixed3D'.

The event handler receives an argument of typeÂ EventArgsÂ containing data related to this event.

{% tabs %}
{% highlight C# %}
privateÂ voidÂ percentTextBox1_ThemesEnabledChanged(objectÂ sender,Â EventArgsÂ e)
{
    Console.WriteLine(" ThemesEnabledChanged event is raised ");
}
{% endhighlight %}
{% highlight VB %}
PrivateÂ SubÂ percentTextBox1_ThemesEnabledChanged(ByValÂ senderÂ AsÂ Object,Â ByValÂ eÂ AsÂ EventArgs)
Console.WriteLine(" ThemesEnabledChanged event is raised ")
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

privateÂ voidÂ percentTextBox1_ValidationError(objectÂ sender, Syncfusion.Windows.Forms.Tools.ValidationErrorArgsÂ e)
{
    Console.WriteLine(" ValidationError event is raised ");
}

{% endhighlight %}

{% highlight vb %}

PrivateÂ SubÂ percentTextBox1_ValidationError(ByValÂ senderÂ AsÂ Object,Â ByValÂ eÂ AsSyncfusion.Windows.Forms.Tools.ValidationErrorArgs)
Console.WriteLine(" ValidationError event is raised ")
EndÂ Sub

{% endhighlight %}
{% endtabs %}
