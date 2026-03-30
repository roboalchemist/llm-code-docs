# Source: https://docs.syncfusion.com/windowsforms/textbox/textboxext-events.md

# TextboxExt Events in Windows Forms TextBox (TextBoxExt)

The list of events and a detailed explanation about each of them is given in the following sections.

<table>
<tr>
<th>
NumericUpDownExt Events</th><th>
Description</th></tr>
<tr>
<td>
Border3DStyleChanged</td><td>
This event occurs when the Border3DStyle property is changed.</td></tr>
<tr>
<td>
BorderColorChanged</td><td>
This event occurs when the BorderColor property is changed.</td></tr>
<tr>
<td>
BorderSidesChanged</td><td>
This event occurs when the BorderSides property is changed.</td></tr>
<tr>
<td>
BorderStyleChanged</td><td>
This event occurs when the ClipText property is changed.</td></tr>
<tr>
<td>
CharacterCasingChanged</td><td>
This event occurs when the CharacterCasing property is changed.</td></tr>
<tr>
<td>
HideSelectionChanged</td><td>
This event occurs when the HideSelection property is changed.</td></tr>
<tr>
<td>
MaximumSizeChanged</td><td>
This event occurs when the MaximumSize property is changed.</td></tr>
<tr>
<td>
MinimumSizeChanged</td><td>
This event occurs when the MinimumSize property is changed.</td></tr>
<tr>
<td>
MultilineChanged</td><td>
This event occurs when the Multiline property is changed.</td></tr>
<tr>
<td>
ReadOnlyChanged</td><td>
This event occurs when the ReadOnly property is changed.</td></tr>
<tr>
<td>
TextAlignChanged</td><td>
This event occurs when the TextAlign property is changed.</td></tr>
<tr>
<td>
ThemesEnabledChanged</td><td>
This event occurs when the ThemesEnabled property is changed.</td></tr>
</table>

## Border3DStyleChanged

The [Border3DStyleChanged](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.TextBoxExt.html#Syncfusion_Windows_Forms_Tools_TextBoxExt_Border3DStyleChanged) event occurs when the [Border3DStyle](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.TextBoxExt.html#Syncfusion_Windows_Forms_Tools_TextBoxExt_Border3DStyle) property is changed. The `Border3DStyle` property indicates the style of the 3D border.

The event handler receives an argument of typeÂ EventArgsÂ containing data related to this event.

{% tabs %}
{% highlight c# %}

privateÂ voidÂ textBoxExt1_Border3DStyleChanged(objectÂ sender,Â EventArgsÂ e)
{
	Console.WriteLine(" Border3DStyleChanged event is raised ");
}

{% endhighlight %}

{% highlight vb %}

PrivateÂ SubÂ textBoxExt1_Border3DStyleChanged(ByValÂ senderÂ AsÂ Object,Â ByValÂ eÂ AsÂ EventArgs)
Console.WriteLine(" Border3DStyleChanged event is raised ")
EndÂ Sub

{% endhighlight %}
{% endtabs %}

## BorderColorChanged

The [BorderColorChanged](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.TextBoxExt.html#Syncfusion_Windows_Forms_Tools_TextBoxExt_BorderColorChanged) event occurs when the [BorderColor](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.TextBoxExt.html#Syncfusion_Windows_Forms_Tools_TextBoxExt_BorderColor) property is changed. The `BorderColor` property indicates the color of the 2D border.

The event handler receives an argument of typeÂ EventArgsÂ containing data related to this event.

{% tabs %}
{% highlight c# %}

privateÂ voidÂ textBoxExt1_BorderColorChanged(objectÂ sender,Â EventArgsÂ e)
{
	Console.WriteLine(" BorderColorChanged event is raised ");
}

{% endhighlight %}

{% highlight vb %}

PrivateÂ SubÂ textBoxExt1_BorderColorChanged(ByValÂ senderÂ AsÂ Object,Â ByValÂ eÂ AsÂ EventArgs)
Console.WriteLine(" BorderColorChanged event is raised ")
EndÂ Sub

{% endhighlight %}
{% endtabs %}

## BorderSidesChanged

The [BorderSidesChanged](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.TextBoxExt.html#Syncfusion_Windows_Forms_Tools_TextBoxExt_BorderSidesChanged) event occurs when the [BorderSides](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.TextBoxExt.html#Syncfusion_Windows_Forms_Tools_TextBoxExt_BorderSides) property is changed. The `BorderSides` property indicates the border sides of the panel.

The event handler receives an argument of typeÂ EventArgsÂ containing data related to this event.

{% tabs %}
{% highlight c# %}

privateÂ voidÂ textBoxExt1_BorderSidesChanged(objectÂ sender,Â EventArgsÂ e)
{
	Console.WriteLine(" BorderSidesChanged event is raised ");
}

{% endhighlight %}

{% highlight vb %}

PrivateÂ SubÂ textBoxExt1_BorderSidesChanged(ByValÂ senderÂ AsÂ Object,Â ByValÂ eÂ AsÂ EventArgs)
Console.WriteLine(" BorderSidesChanged event is raised ")
EndÂ Sub

{% endhighlight %}
{% endtabs %}

## BorderStyleChanged

The [BorderStyleChanged](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.textboxbase.borderstylechanged?view=windowsdesktop-7.0&viewFallbackFrom=netcore-3.1&redirectedfrom=MSDN) event occurs when the [BorderStyle](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.textboxbase.borderstyle?view=windowsdesktop-7.0&viewFallbackFrom=netcore-3.1&redirectedfrom=MSDN#System_Windows_Forms_TextBoxBase_BorderStyle) property is changed. The `BorderStyle` property indicates whether the edit control should have a border.

The event handler receives an argument of typeÂ EventArgsÂ containing data related to this event.

{% tabs %}
{% highlight c# %}

privateÂ voidÂ textBoxExt1_BorderStyleChanged(objectÂ sender,Â EventArgsÂ e)
{
	Console.WriteLine(" BorderStyleChanged event is raised ");
}

{% endhighlight %}

{% highlight vb %}

PrivateÂ SubÂ textBoxExt1_BorderStyleChanged(ByValÂ senderÂ AsÂ Object,Â ByValÂ eÂ AsÂ EventArgs)
Console.WriteLine(" BorderStyleChanged event is raised ")
EndÂ Sub

{% endhighlight %}
{% endtabs %}

## CharacterCasingChanged

The [CharacterCasingChanged](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.TextBoxExt.html#Syncfusion_Windows_Forms_Tools_TextBoxExt_CharacterCasingChanged) event occurs when the [CharacterCasing](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.TextBoxExt.html#Syncfusion_Windows_Forms_Tools_TextBoxExt_CharacterCasing) property is changed. The `CharacterCasing` property gets or sets the case of the characters as they are typed.

The event handler receives an argument of typeÂ EventArgsÂ containing data related to this event.

{% tabs %}
{% highlight c# %}

privateÂ voidÂ textBoxExt1_CharacterCasingChanged(objectÂ sender,Â EventArgsÂ e)
{
	Console.WriteLine(" CharacterCasingChanged event is raised ");
}

{% endhighlight %}

{% highlight vb %}

PrivateÂ SubÂ textBoxExt1_CharacterCasingChanged(ByValÂ senderÂ AsÂ Object,Â ByValÂ eÂ AsÂ EventArgs)
Console.WriteLine(" CharacterCasingChanged event is raised ")
EndÂ Sub

{% endhighlight %}
{% endtabs %}

## HideSelectionChanged

The [HideSelectionChanged](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.textboxbase.hideselectionchanged?view=windowsdesktop-7.0&viewFallbackFrom=netcore-3.1&redirectedfrom=MSDN) event occurs when the [HideSelection](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.textboxbase.hideselection?view=windowsdesktop-7.0&viewFallbackFrom=netcore-3.1&redirectedfrom=MSDN#System_Windows_Forms_TextBoxBase_HideSelection) property is changed. The `HideSelection` property indicates that the selection should be hidden when the edit control loses focus.

The event handler receives an argument of typeÂ EventArgsÂ containing data related to this event.

{% tabs %}
{% highlight c# %}

privateÂ voidÂ textBoxExt1_HideSelectionChanged(objectÂ sender,Â EventArgsÂ e)
{
	Console.WriteLine(" HideSelectionChanged event is raised ");
}

{% endhighlight %}

{% highlight vb %}

PrivateÂ SubÂ textBoxExt1_HideSelectionChanged(ByValÂ senderÂ AsÂ Object,Â ByValÂ eÂ AsÂ EventArgs)
Console.WriteLine(" HideSelectionChanged event is raised ")
EndÂ Sub

{% endhighlight %}
{% endtabs %}

## MaximumSizeChanged 

The [MaximumSizeChanged](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.TextBoxExt.html#Syncfusion_Windows_Forms_Tools_TextBoxExt_MaximumSizeChanged) event occurs when the [MaximumSize](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.TextBoxExt.html#Syncfusion_Windows_Forms_Tools_TextBoxExt_MaximumSize) property is changed. The `MaximumSize` property gets or sets the maximum size of the control.

The event handler receives an argument of typeÂ EventArgsÂ containing data related to this event.

{% tabs %}
{% highlight c# %}

privateÂ voidÂ textBoxExt1_MaximumSizeChanged(objectÂ sender,Â EventArgsÂ e)
{
	Console.WriteLine(" MaximumSizeChanged event is raised ");
}

{% endhighlight %}

{% highlight vb %}

PrivateÂ SubÂ textBoxExt1_MaximumSizeChanged(ByValÂ senderÂ AsÂ Object,Â ByValÂ eÂ AsÂ EventArgs)
Console.WriteLine(" MaximumSizeChanged event is raised ")
EndÂ Sub

{% endhighlight %}
{% endtabs %}

## MinimumSizeChanged 

The [MinimumSizeChanged](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.TextBoxExt.html#Syncfusion_Windows_Forms_Tools_TextBoxExt_MinimumSizeChanged) event occurs when the [MinimumSize](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.TextBoxExt.html#Syncfusion_Windows_Forms_Tools_TextBoxExt_MinimumSize) property is changed. The `MinimumSize` property gets or sets the minimum size of the control.

The event handler receives an argument of typeÂ EventArgsÂ containing data related to this event.

{% tabs %}
{% highlight c# %}

privateÂ voidÂ textBoxExt1_MinimumSizeChanged(objectÂ sender,Â EventArgsÂ e)
{
	Console.WriteLine(" MinimumSizeChanged event is raised ");
}

{% endhighlight %}

{% highlight vb %}

PrivateÂ SubÂ textBoxExt1_MinimumSizeChanged(ByValÂ senderÂ AsÂ Object,Â ByValÂ eÂ AsÂ EventArgs)
Console.WriteLine(" MinimumSizeChanged event is raised ")
EndÂ Sub

{% endhighlight %}
{% endtabs %}

## MultilineChanged 

The [MultilineChanged](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.textboxbase.multilinechanged?view=windowsdesktop-7.0&viewFallbackFrom=netcore-3.1&redirectedfrom=MSDN) event occurs when the [Multiline](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.textbox.multiline?view=windowsdesktop-7.0&viewFallbackFrom=netcore-3.1&redirectedfrom=MSDN#System_Windows_Forms_TextBox_Multiline) property is changed. The `Multiline` property controls whether the text of the edit control can span more than one line.

The event handler receives an argument of typeÂ EventArgsÂ containing data related to this event.

{% tabs %}
{% highlight c# %}

privateÂ voidÂ textBoxExt1_MultilineChanged(objectÂ sender,Â EventArgsÂ e)
{
	Console.WriteLine(" MultilineChanged event is raised ");
}

{% endhighlight %}

{% highlight vb %}

PrivateÂ SubÂ textBoxExt1_MultilineChanged(ByValÂ senderÂ AsÂ Object,Â ByValÂ eÂ AsÂ EventArgs)
Console.WriteLine(" MultilineChanged event is raised ")
EndÂ Sub

{% endhighlight %}
{% endtabs %}

## ReadOnlyChanged 

The [ReadOnlyChanged](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.textboxbase.readonlychanged?view=windowsdesktop-7.0&viewFallbackFrom=netcore-3.1&redirectedfrom=MSDN) event occurs when the [ReadOnly](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.textboxbase.readonly?view=windowsdesktop-7.0&viewFallbackFrom=netcore-3.1&redirectedfrom=MSDN#System_Windows_Forms_TextBoxBase_ReadOnly) property is changed. The `ReadOnly` property controls whether the text in the edit control can be changed or not.

The event handler receives an argument of typeÂ EventArgsÂ containing data related to this event.

{% tabs %}
{% highlight c# %}

privateÂ voidÂ textBoxExt1_ReadOnlyChanged(objectÂ sender,Â EventArgsÂ e)
{
	Console.WriteLine(" ReadOnlyChanged event is raised ");
}

{% endhighlight %}

{% highlight vb %}

PrivateÂ SubÂ textBoxExt1_ReadOnlyChanged(ByValÂ senderÂ AsÂ Object,Â ByValÂ eÂ AsÂ EventArgs)
Console.WriteLine(" ReadOnlyChanged event is raised ")
EndÂ Sub

{% endhighlight %}
{% endtabs %}

## TextAlignChanged 

The [TextAlignChanged](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.textbox.textalignchanged?view=windowsdesktop-7.0&viewFallbackFrom=netcore-3.1&redirectedfrom=MSDN) event occurs when the [TextAlign](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.textbox.textalign?view=windowsdesktop-7.0&viewFallbackFrom=netcore-3.1&redirectedfrom=MSDN#System_Windows_Forms_TextBox_TextAlign) property is changed. The `TextAlign` property indicates how the text should be aligned in TextBoxExt control.

The event handler receives an argument of typeÂ EventArgsÂ containing data related to this event.

{% tabs %}
{% highlight c# %}

privateÂ voidÂ textBoxExt1_TextAlignChanged(objectÂ sender,Â EventArgsÂ e)
{
	Console.WriteLine(" TextAlignChanged event is raised ");
}

{% endhighlight %}

{% highlight vb %}

PrivateÂ SubÂ textBoxExt1_TextAlignChanged(ByValÂ senderÂ AsÂ Object,Â ByValÂ eÂ AsÂ EventArgs)
Console.WriteLine(" TextAlignChanged event is raised ")
EndÂ Sub

{% endhighlight %}
{% endtabs %}

## ThemesEnabledChanged

The [ThemesEnabledChanged](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.TextBoxExt.html#Syncfusion_Windows_Forms_Tools_TextBoxExt_ThemesEnabledChanged) event occurs when the [ThemesEnabled](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.TextBoxExt.html#Syncfusion_Windows_Forms_Tools_TextBoxExt_ThemesEnabled) property is changed. The `ThemesEnabled` property specifies whether or not to use XP Themes when the [BorderStyle](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.textboxbase.borderstyle?view=windowsdesktop-7.0&viewFallbackFrom=netcore-3.1&redirectedfrom=MSDN#System_Windows_Forms_TextBoxBase_BorderStyle) property is set to `Fixed3D`.

The event handler receives an argument of typeÂ EventArgsÂ containing data related to this event.

{% tabs %}
{% highlight c# %}

privateÂ voidÂ textBoxExt1_ThemesEnabledChanged(objectÂ sender,Â EventArgsÂ e)
{
	Console.WriteLine(" ThemesEnabledChanged event is raised ");
}

{% endhighlight %}

{% highlight vb %}

PrivateÂ SubÂ textBoxExt1_ThemesEnabledChanged(ByValÂ senderÂ AsÂ Object,Â ByValÂ eÂ AsÂ EventArgs)
Console.WriteLine(" ThemesEnabledChanged event is raised ")
EndÂ Sub

{% endhighlight %}
{% endtabs %}
