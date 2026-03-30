# Source: https://docs.syncfusion.com/windowsforms/percent-textbox/keysettings.md

# Source: https://docs.syncfusion.com/windowsforms/integer-textbox/keysettings.md

# Key Settings in Windows Forms Integer TextBox (Integertextbox)

Sometimes there may be some situation for entering large values, like in Mega, Kilo etc., In such situations, if we add some sort of keyboard support, it will be very much useful for the users.

For example if the user wants to enter 32000, he just needs to enter 32 and then press the 'K'. The value will change to 32000 automatically. This is illustrated in the code snippet given below.

{% tabs %}
{% highlight C# %}
private voidÂ integerTextBox1_KeyDown(objectÂ sender, KeyEventArgs e)
{
    longÂ v = integerTextBox1.IntegerValue;
    switch(e.KeyCode)
    {
        // Enter the value as multiples of thousand.
        caseÂ Keys.G : v = v * 1000000000;
        break;
        caseÂ Keys.M : v = v * 1000000;
        break;
        caseÂ Keys.K : v = v * 1000;
        break;
    }
    integerTextBox.IntegerValue = v;
}
{% endhighlight %}
{% highlight VB %}
Private SubÂ integerTextBox1_KeyDown(ByValÂ senderÂ As Object,Â ByValÂ eÂ AsÂ KeyEventArgs)
DimÂ vÂ As LongÂ = integerTextBox1.IntegerValue
SelectÂ e.KeyCode

' Enter the value as multiples of thousand.
CaseÂ Keys.G
v = v * 1000000000

CaseÂ Keys.M
v = v * 1000000

CaseÂ Keys.K
v = v * 1000
End Select
integerTextBox1.IntegerValue = v
End Sub
{% endhighlight %}
{% endtabs %}

## Shortcut keys

Sometimes there may be some situations for incrementing or decrementing the value in the IntegerTextBox. In such situations, it is better to use shortcut keys.

The following implementation will illustrate how this can be achieved. Here we are usingÂ UpÂ andÂ DownÂ keys for incrementing and decrementing respectively. We cannot use the '-' key, because it is already reserved to enter the minus sign.

{% tabs %}
{% highlight C# %}
private voidÂ integerTextBox1_KeyDown(objectÂ sender, KeyEventArgs e)
{
    longÂ v = integerTextBox1.IntegerValue;
    switch(e.KeyCode)
    {
        // Increments and decrements values.
        caseÂ Keys.Up : v++;
        break;
        
        caseÂ Keys.Down : v--;
        break;
    }
    integerTextBox1.IntegerValue = v;
}
{% endhighlight %}
{% highlight VB %}
Private SubÂ integerTextBox1_KeyDown(ByValÂ senderÂ As Object,Â ByValÂ eÂ AsÂ KeyEventArgs)
DimÂ vÂ As LongÂ = integerTextBox1.IntegerValue
SelectÂ e.KeyCode

' Increments and decrements values.
CaseÂ Keys.Up
v = v+1

CaseÂ Keys.Down
v = v-1
End Select
integerTextBox1.IntegerValue = v
End Sub
{% endhighlight %}
{% endtabs %}
