# Source: https://docs.syncfusion.com/windowsforms/numericupdown/key-support.md

# Key support in Windows Forms NumericUpDown (NumericUpDownExt)

Sometimes there may occur some situations for entering large values, like in Mega, Kilo etc. In such situations if you add some sort of keyboard support, it will be very much useful for the you.

For example if you want to enter 22000, you just need to enter 22 and then press 'K'. The value will change to 22000 automatically. This is illustrated in the code snippet given below.

{% tabs %}
{% highlight c# %}

private voidÂ numericUpDownExt1_KeyDown(objectÂ sender, KeyEventArgs e)
{
    decimal v = integerTextBox1.Value;
    switch(e.KeyCode)
    {

// Entering the value as multiples of thousand.
        caseÂ Keys.G : v = v * 1000000000;
        break;
        
        caseÂ Keys.M : v = v * 1000000;
        break;
        
        caseÂ Keys.K : v = v * 1000;
        break;
    }
    integerTextBox.Value = v;
}

{% endhighlight %}

{% highlight vb %}

Private SubÂ numericUpDownExt1_KeyDown(ByValÂ senderÂ As Object,Â ByValÂ eÂ AsÂ KeyEventArgs)
DimÂ vÂ AsÂ Decimal = numericUpDownExt1.Value
SelectÂ e.KeyCode

' Entering the value as multiples of thousand.
CaseÂ Keys.G
v = v * 1000000000

CaseÂ Keys.M
v = v * 1000000

CaseÂ Keys.K
v = v * 1000
End Select
numericUpDownExt1.Value = v
End Sub

{% endhighlight %}
{% endtabs %}
