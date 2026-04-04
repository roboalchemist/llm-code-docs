# Source: https://docs.syncfusion.com/windowsforms/double-textbox/eventhandling.md

# Event Handling in Windows Forms Double TextBox

## DoubleValueChanged Event

This [DoubleValueChanged](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.DoubleTextBox.html) event is handled when the double value in the text field is changed.

{% tabs %}
{% highlight C# %}  
privateÂ voidÂ doubleTextBox1_DoubleValueChanged(objectÂ sender,Â EventArgsÂ e)
{
Â Â Â MessageBox.Show("Double Value is changed");
}
{% endhighlight %}
{% highlight VB %} 
Private SubÂ doubleTextBox1_DoubleValueChanged(ByValÂ senderÂ As Object,Â ByValÂ eÂ AsÂ EventArgs)
MessageBox.Show("Double Value is changed")
End Sub
{% endhighlight %}
{% endtabs %}

## Enabling Fixed Change using Shortcut Keys

Sometimes there may occur situations for incrementing or decrementing the value in DoubleTextBox. In such situations it is better to use shortcut keys. The following implementation will give you an idea on how to achieve this. Here the Up and Down keys are used for incrementing and decrementing respectively. We cannot use '-' because it is already reserved to enter the minus sign.

{% tabs %}
{% highlight C# %}  
private voidÂ doubleTextBox1_KeyDown(objectÂ sender,KeyEventArgs e)
{
    decimal v=doubleTextBox1.DoubleValue;
    switch(e.KeyCode)
    {
        // Up and Down keys are used for incrementing and decrementing respectively.
        caseÂ Keys.Up : v++;break;
        caseÂ Keys.Down : v--;break;
    }
    doubleTextBox1.DoubleValue=v;
}
{% endhighlight %}
{% highlight VB %} 
Private SubÂ doubleTextBox1_KeyDown(ByValÂ senderÂ As Object,Â ByValÂ eÂ AsÂ KeyEventArgs)
DimÂ vÂ AsÂ Decimal = doubleTextBox1.DoubleValue
SelectÂ e.KeyCode
' Up and Down keys are used for incrementing and decrementing respectively.
CaseÂ Keys.Up
v=v+1
CaseÂ Keys.Down
v=v-1
End Select
doubleTextBox1.DoubleValue = v
End Sub
{% endhighlight %}
{% endtabs %}
