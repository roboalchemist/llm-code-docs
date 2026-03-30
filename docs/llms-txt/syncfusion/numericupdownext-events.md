# Source: https://docs.syncfusion.com/windowsforms/numericupdown/numericupdownext-events.md

# NumericUpDownExt Events in Windows Forms NumericUpDown

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
ReadOnlyChanged</td><td>
This event occurs when the ReadOnly property is changed.</td></tr>
<tr>
<td>
ThemeChanged</td><td>
This event occurs when the ThemesEnabled property is changed.</td></tr>
<tr>
<td>
ValueChanged</td><td>
This event occurs when the Value property is changed.</td></tr>
</table>

## Border3DStyleChanged

This event occurs when theÂ Border3DStyleÂ property is changed. The Border3DStyle property indicates the style of the 3D border.

The event handler receives an argument of typeÂ EventArgsÂ containing data related to this event.

{% tabs %}
{% highlight c# %}

privateÂ voidÂ numericUpDownExt1_Border3DStyleChanged(objectÂ sender,Â EventArgsÂ e)
{
    Console.WriteLine(" Border3DStyleChanged event is raised ");
}

{% endhighlight %}

{% highlight vb %}

PrivateÂ SubÂ numericUpDownExt1_Border3DStyleChanged(ByValÂ senderÂ AsÂ Object,Â ByValÂ eÂ AsÂ EventArgs)
Console.WriteLine(" Border3DStyleChanged event is raised ")
EndÂ Sub

{% endhighlight %}
{% endtabs %}

## BorderColorChanged

This event occurs when theÂ BorderColorÂ property is changed. The BorderColor property indicates the color of the 2D border.

The event handler receives an argument of typeÂ EventArgsÂ containing data related to this event.

{% tabs %}
{% highlight c# %}

privateÂ voidÂ numericUpDownExt1_BorderColorChanged(objectÂ sender,Â EventArgsÂ e)
{
    Console.WriteLine(" BorderColorChanged event is raised ");
}

{% endhighlight %}

{% highlight vb %}

PrivateÂ SubÂ numericUpDownExt1_BorderColorChanged(ByValÂ senderÂ AsÂ Object,Â ByValÂ eÂ AsÂ EventArgs)
Console.WriteLine(" BorderColorChanged event is raised ")
EndÂ Sub

{% endhighlight %}
{% endtabs %}

## BorderSidesChanged

This event occurs when theÂ BorderSidesÂ property is changed. The BorderSides property indicates the border sides of the panel.

The event handler receives an argument of typeÂ EventArgsÂ containing data related to this event.

{% tabs %}
{% highlight c# %}

privateÂ voidÂ numericUpDownExt1_BorderSidesChanged(objectÂ sender,Â EventArgsÂ e)
{
    Console.WriteLine(" BorderSidesChanged event is raised ");
}

{% endhighlight %}

{% highlight vb %}

PrivateÂ SubÂ numericUpDownExt1_BorderSidesChanged(ByValÂ senderÂ AsÂ Object,Â ByValÂ eÂ AsÂ EventArgs)
Console.WriteLine(" BorderSidesChanged event is raised ")
EndÂ Sub

{% endhighlight %}
{% endtabs %}

## BorderStyleChanged

This event occurs when theÂ BorderStyleÂ property is changed. The BorderStyle property indicates whether the edit control should have a border.

The event handler receives an argument of typeÂ EventArgsÂ containing data related to this event.

{% tabs %}
{% highlight c# %}

privateÂ voidÂ numericUpDownExt1_BorderStyleChanged(objectÂ sender,Â EventArgsÂ e)
{
    Console.WriteLine(" BorderStyleChanged event is raised ");
}

{% endhighlight %}

{% highlight vb %}

PrivateÂ SubÂ numericUpDownExt1_BorderStyleChanged(ByValÂ senderÂ AsÂ Object,Â ByValÂ eÂ AsÂ EventArgs)
Console.WriteLine(" BorderStyleChanged event is raised ")
EndÂ Sub

{% endhighlight %}
{% endtabs %}

## ReadOnlyChanged

This event occurs when theÂ ReadOnlyÂ property is changed. The ReadOnly property gets / sets a value indicating whether the text can be changed by the use of the up or down buttons only.

The event handler receives an argument of typeÂ EventArgsÂ containing data related to this event.

{% tabs %}
{% highlight c# %}

privateÂ voidÂ numericUpDownExt1_ReadOnlyChanged(objectÂ sender,Â EventArgsÂ e)
{
    Console.WriteLine(" ReadOnlyChanged event is raised ");
}

{% endhighlight %}

{% highlight vb %}

PrivateÂ SubÂ numericUpDownExt1_ReadOnlyChanged(ByValÂ senderÂ AsÂ Object,Â ByValÂ eÂ AsÂ EventArgs)
Console.WriteLine(" ReadOnlyChanged event is raised ")
EndÂ Sub

{% endhighlight %}
{% endtabs %}

## ThemeChanged

This event occurs when theÂ ThemesEnabledÂ property is changed. The ThemesEnabled property indicates whether XP Themes (visual styles) should be used for this control when available.

The event handler receives an argument of typeÂ EventArgsÂ containing data related to this event.

{% tabs %}
{% highlight c# %}

privateÂ voidÂ numericUpDownExt1_ThemeChanged(objectÂ sender,Â EventArgsÂ e)
{
    Console.WriteLine(" ThemeChanged event is raised ");
}

{% endhighlight %}

{% highlight vb %}

PrivateÂ SubÂ numericUpDownExt1_ThemeChanged(ByValÂ senderÂ AsÂ Object,Â ByValÂ eÂ AsÂ EventArgs)
Console.WriteLine(" ThemeChanged event is raised ")
EndÂ Sub

{% endhighlight %}
{% endtabs %}

## ValueChanged

This event occurs when theÂ ValueÂ property is changed. The Value property gets / sets the value assigned to the spin box (also known as an up-down control).

The event handler receives an argument of typeÂ EventArgsÂ containing data related to this event.

{% tabs %}
{% highlight c# %}

privateÂ voidÂ numericUpDownExt1_ValueChanged(objectÂ sender,Â EventArgsÂ e)
{
    Console.WriteLine(" ValueChanged event is raised ");
}

{% endhighlight %}

{% highlight vb %}

PrivateÂ SubÂ numericUpDownExt1_ValueChanged(ByValÂ senderÂ AsÂ Object,Â ByValÂ eÂ AsÂ EventArgs)
Console.WriteLine(" ValueChanged event is raised ")
EndÂ Sub

{% endhighlight %}
{% endtabs %}
