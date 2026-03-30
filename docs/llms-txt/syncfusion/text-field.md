# Source: https://docs.syncfusion.com/windowsforms/currency-textbox/text-field.md

# Text Field in Windows Forms Currency Textbox (CurrencyTextbox)

The text field of a CurrencyTextBox control can be customized using the properties available. The below image illustrates the various sections of the control.

![Text field](Overview_images/Overview_img490.png) 

## Text

The default text in the CurrencyTextBox can be edited throughÂ [Text](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.CurrencyTextBox.html#Syncfusion_Windows_Forms_Tools_CurrencyTextBox_Text)Â property. Default value is $2.00. The text can be aligned to Left, Right or Center usingÂ TextAlignÂ property.

{% tabs %}

{% highlight c# %}

this.currencyTextBox2.Text =Â "$25.00";

this.currencyTextBox1.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;

{% endhighlight %}

{% highlight vbnet %}

Me.currencyTextBox2.Text =Â "$25.00"

Me.currencyTextBox1.TextAlign = System.Windows.Forms.HorizontalAlignment.Right

{% endhighlight %}

{% endtabs %}

![Text](Overview_images/Overview_img491.png) 



### Multiline Feature

The CurrencyTextBox control can be made multiline by settingÂ [Multiline](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.textbox.multiline?redirectedfrom=MSDN&view=netframework-4.7.2#System_Windows_Forms_TextBox_Multiline)Â property to true. Using the below properties we can control the behavior of control.Â 

* [Lines](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.textboxbase.lines?redirectedfrom=MSDN&view=netframework-4.7.2#System_Windows_Forms_TextBoxBase_Lines)
* [WordWrap](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.textboxbase.wordwrap?redirectedfrom=MSDN&view=netframework-4.7.2#System_Windows_Forms_TextBoxBase_WordWrap)
* [ScrollBars](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.textboxbase.wordwrap?redirectedfrom=MSDN&view=netframework-4.7.2#System_Windows_Forms_TextBoxBase_WordWrap)


{% tabs %}

{% highlight c# %}

this.currencyTextBox1.Multiline =Â true;

this.currencyTextBox2.Text =Â "$12,456,456,456,456,456,456,456.00";

this.currencyTextBox2.WordWrapÂ = "true"

this.currencyTextBox1.ScrollBars = System.Windows.Forms.ScrollBars.Both;

{% endhighlight %}

{% highlight vbnet %}

Me.currencyTextBox1.Multiline =Â True

Me.currencyTextBox2.Text =Â "$12,456,456,456,456,456,456,456.00"

Me.currencyTextBox2.WordWrapÂ =Â True

Me.currencyTextBox1.ScrollBars = System.Windows.Forms.ScrollBars.Both

{% endhighlight %}

{% endtabs %}

![CurrecyTextBox multiline support](Overview_images/Overview_img492.png) 



![CurrencyTextBox word wrap support](Overview_images/Overview_img493.png)



![CurrencyTextBox scroll bar support](Overview_images/Overview_img494.png) 



### Password Character

We can display password characters instead of the digits in the text field usingÂ [PasswordChar](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.textbox.passwordchar?redirectedfrom=MSDN&view=netframework-4.7.2#System_Windows_Forms_TextBox_PasswordChar)Â property. To use the system password character in the text field, setÂ [UseSystemPasswordChar](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.textbox.usesystempasswordchar?redirectedfrom=MSDN&view=netframework-4.7.2#System_Windows_Forms_TextBox_UseSystemPasswordChar)Â property to true.

{% tabs %}

{% highlight c# %}

this.currencyTextBox1.UseSystemPasswordChar =Â false;

this.currencyTextBox1.PasswordChar =Â '*';

{% endhighlight %}

{% highlight vbnet %}

Me.currencyTextBox1.UseSystemPasswordChar =Â False

Me.currencyTextBox1.PasswordChar =Â '*'

{% endhighlight %}

{% endtabs %}

![Password character](Overview_images/Overview_img495.png)



### Banner Text Support

We can set banner text for the CurrencyTextBox control. ReferÂ BannerTextProvider ComponentÂ topic for more details.

We need to do the below settings to make Banner text feature available for the control.

{% tabs %}

{% highlight c# %}

this.currencyTextBox1.AllowNull =Â true;

this.currencyTextBox1.NullString = "";

this.currencyTextBox1.Text = "";

{% endhighlight %}

{% highlight vbnet %}

Me.currencyTextBox1.AllowNull =Â True

Me.currencyTextBox1.NullString = ""

Me.currencyTextBox1.Text = ""

{% endhighlight %}

{% endtabs %}

![Banner text support](Overview_images/Overview_img496.png)



## Number and Decimal Digits

The CurrencyTextBox text field has a number part and a decimal part. The properties which controls appearance and behavior of the text field are discussed in this section.

### Number part

The below properties lets you decide the formatting of the number part of CurrencyTextBox control.

* [CurrencyNumberDigits](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.CurrencyTextBox.html#Syncfusion_Windows_Forms_Tools_CurrencyTextBox_CurrencyNumberDigits)
* [CurrencyPositivePattern](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.CurrencyTextBox.html#Syncfusion_Windows_Forms_Tools_CurrencyTextBox_CurrencyPositivePattern)
* [CurrencyNegativePattern](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.CurrencyTextBox.html#Syncfusion_Windows_Forms_Tools_CurrencyTextBox_CurrencyNegativePattern)


{% tabs %}

{% highlight c# %}

this.currencyTextBox1.NumberDigits = 10;

this.currencyTextBox1.CurrencyPositivePattern = 1;

this.currencyTextBox1.CurrencyNegativePattern = 2;

{% endhighlight %}

{% highlight vbnet %}

Me.currencyTextBox1.NumberDigits = 10

Me.currencyTextBox1.CurrencyPositivePattern = 1

Me.currencyTextBox1.CurrencyNegativePattern = 2

{% endhighlight %}

{% endtabs %}

### Decimal Part

The below properties lets you decide the formatting of the CurrencyTextBox control's number part.

* [CurrencyDecimalDigits](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.CurrencyTextBox.html#Syncfusion_Windows_Forms_Tools_CurrencyTextBox_CurrencyDecimalDigits)
* [CurrencyDecimalSeparator](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.CurrencyTextBox.html#Syncfusion_Windows_Forms_Tools_CurrencyTextBox_CurrencyDecimalSeparator)
* [CurrencyGroupSeparator](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.CurrencyTextBox.html#Syncfusion_Windows_Forms_Tools_CurrencyTextBox_CurrencyGroupSeparator)
* [CurrencyGroupSizes](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.CurrencyTextBox.html#Syncfusion_Windows_Forms_Tools_CurrencyTextBox_CurrencyGroupSizes)
* [DecimalValue](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.CurrencyTextBox.html#Syncfusion_Windows_Forms_Tools_CurrencyTextBox_DecimalValue)
* [RemoveDecimalZeros](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.CurrencyTextBox.html#Syncfusion_Windows_Forms_Tools_CurrencyTextBox_RemoveDecimalZeros)


![Decimal part](Overview_images/Overview_img497.png) 

{% tabs %}

{% highlight c# %}

this.currencyTextBox1.CurrencyDecimalDigits = 3;

this.currencyTextBox1.CurrencyDecimalSeparator = ".";

this.currencyTextBox1.CurrencyGroupSeparator = ",";

this.currencyTextBox1.CurrencyGroupSizes =Â newÂ int[] {3};

this.currencyTextBox1.RemoveDecimalZeros =Â true;

{% endhighlight %}

{% highlight vbnet %}

Me.currencyTextBox1.CurrencyDecimalDigits = 3

Me.currencyTextBox1.CurrencyDecimalSeparator =Â "."

Me.currencyTextBox1.CurrencyGroupSeparator =Â ","

Me.currencyTextBox1.CurrencyGroupSizes =Â NewÂ Integer() {3}

Me.currencyTextBox1.RemoveDecimalZeros =Â True

{% endhighlight %}

{% endtabs %}

![Decimal Part](Overview_images/Overview_img498.png) 



![Decimal Part](Overview_images/Overview_img499.png) 



## Negative Part

The default negative sign '-' can be changed by [NegativeSign](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.NumberTextBoxBase.html#Syncfusion_Windows_Forms_Tools_NumberTextBoxBase_NegativeSign) property to any other special characters. We can specify the behavior of the Currency TextBox by [NegativeInputPendingOnSelectAll](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.NumberTextBoxBase.html#Syncfusion_Windows_Forms_Tools_NumberTextBoxBase_NegativeInputPendingOnSelectAll) when its content is fully selected and negative key is pressed by the user. When [NegativeInputPendingOnSelectAll](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.NumberTextBoxBase.html#Syncfusion_Windows_Forms_Tools_NumberTextBoxBase_NegativeInputPendingOnSelectAll) set to 'True', the current value is not changed. The next key stroke is taken to a new value and the entire content of the TextBox is replaced by the negative value of the key stroke entered.

For example, if the current value of the TextBox is 1.00 with all the text being selected and when the user presses the negative key followed by key 5, the value will be  '-5'.

When it is set to false, the current value is changed to negative value immediately. For example, if the current value of the TextBox is 1.00 with all the text being selected and when the user presses the negative key, the value is '-1'.

{% tabs %}

{% highlight c# %}

this.currencyTextBox1.NegativeSign = "-";

this.currencyTextBox1.NegativeInputPendingOnSelectAll =Â true;

{% endhighlight %}

{% highlight vbnet %}

Me.currencyTextBox1.NegativeSign =Â "-"

Me.currencyTextBox1.NegativeInputPendingOnSelectAll =Â True

{% endhighlight %}

{% endtabs %}

## Values

The maximum and minimum value of the currency can be specified by MaxValue and MinValue properties.

[MaxValue](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.CurrencyTextBox.html#Syncfusion_Windows_Forms_Tools_CurrencyTextBox_MaxValue)
[MinValue](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.CurrencyTextBox.html#Syncfusion_Windows_Forms_Tools_CurrencyTextBox_MinValue)
[EnforceMinMaxDuringValidating](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.NumberTextBoxBase.html#Syncfusion_Windows_Forms_Tools_NumberTextBoxBase_EnforceMinMaxDuringValidating)

{% tabs %}

{% highlight c# %}

this.currencyTextBox1.MaxValue=10;

this.currencyTextBox1.MinValue=0;

this.currencyTextBox1.EnforceMinMaxDuringValidating=Â true;

{% endhighlight %}

{% highlight vbnet %}

Me.currencyTextBox1.MaxValue=10

Me.currencyTextBox1.MinValue=0

Me.currencyTextBox1.EnforceMinMaxDuringValidating =Â True;

{% endhighlight %}

{% endtabs %}

### Null String

If you want to display null string instead of actualÂ decimalÂ values, you can setÂ [NullString](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.NumberTextBoxBase.html#Syncfusion_Windows_Forms_Tools_NumberTextBoxBase_NullString)Â property to any values. To display the null string setÂ AllowNullÂ to true.

[NullString](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.NumberTextBoxBase.html#Syncfusion_Windows_Forms_Tools_NumberTextBoxBase_NullString)
[AllowNull](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.NumberTextBoxBase.html#Syncfusion_Windows_Forms_Tools_NumberTextBoxBase_AllowNull)

{% tabs %}

{% highlight c# %}

this.currencyTextBox1.NullString =Â "NULL";

this.currencyTextBox1.AllowNull =Â true;

{% endhighlight %}

{% highlight vbnet %}

Me.currencyTextBox1.NullString =Â "NULL"

Me.currencyTextBox1.AllowNull =Â True

{% endhighlight %}

{% endtabs %}

![Null string](Overview_images/Overview_img500.png) 



## Currency Symbol

The currency symbol that will be used for formatting the display is specified by settingÂ [CurrencySymbol](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.CurrencyTextBox.html#Syncfusion_Windows_Forms_Tools_CurrencyTextBox_CurrencySymbol)Â to any special characters.

{% tabs %}

{% highlight c# %}

this.currencyTextBox1.CurrencySymbol = "#";

{% endhighlight %}

{% highlight vbnet %}

Me.currencyTextBox1.CurrencySymbol =Â "#"

{% endhighlight %}

{% endtabs %}
