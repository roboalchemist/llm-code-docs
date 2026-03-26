# Source: https://docs.syncfusion.com/windowsforms/checkbox/checkboxadv-events.md

# CheckBoxAdv Events in Windows Forms CheckBox (CheckBoxAdv)

This section gives detailed explanation about the [CheckStateChanged](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.CheckBoxAdv.html) and [CheckedChanged](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.CheckBoxAdv.html) events in [CheckBoxAdv](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.CheckBoxAdv.html) control.

<table>
<tr>
<th>
CheckBoxAdv Events</th><th>
Description</th></tr>
<tr>
<td>
CheckStateChanged</td><td>
This event occurs when the CheckState property is changed.</td></tr>
<tr>
<td>
CheckedChanged</td><td>
This event is raised when the Checked property is changed.</td></tr>
</table>

## CheckStateChanged Event

This event is raised when the [CheckState](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.CheckBoxAdv.html#Syncfusion_Windows_Forms_Tools_CheckBoxAdv_CheckState) property of [CheckBoxAdv](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.CheckBoxAdv.html) is changed and the event handler receives an argument of type EventArgs containing data related to this event.

{% tabs %}
{% highlight c# %}

private void checkBoxAdv1_CheckStateChanged(object sender, EventArgs e)
{
    Console.WriteLine(" CheckStateChanged event is raised");
}

{% endhighlight %}

{% highlight vb %}

Private Sub checkBoxAdv1_CheckStateChanged(ByVal sender As Object, ByVal e As EventArgs)
Console.WriteLine(" CheckStateChanged event is raised")
End Sub

{% endhighlight %}
{% endtabs %}

## CheckedChanged Event

This event is raised when theÂ [Checked](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.CheckBoxAdv.html#Syncfusion_Windows_Forms_Tools_CheckBoxAdv_Checked)Â property is changed and this property changes automatically when the [CheckState](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.CheckBoxAdv.html#Syncfusion_Windows_Forms_Tools_CheckBoxAdv_CheckState) property is changed.

{% tabs %}
{% highlight c# %}

private void checkBoxAdv1_CheckedChanged(object sender, EventArgs e)
{
    if (!checkBoxAdv1.Checked)
        MessageBox.Show("Checkbox Unchecked");
    else
        MessageBox.Show("Checkbox checked");
}

{% endhighlight %}

{% highlight vb %}

PrivateÂ SubÂ checkBoxAdv1_CheckedChanged(ByValÂ senderÂ AsÂ Object,Â ByValÂ eÂ AsÂ EventArgs)
IfÂ NotÂ checkBoxAdv1.CheckedÂ Then
MessageBox.Show("Checkbox checkedâ)
Else
MessageBox.Show("Checkbox checkedâ)
EndÂ If
EndÂ Sub

{% endhighlight %}
{% endtabs %}
