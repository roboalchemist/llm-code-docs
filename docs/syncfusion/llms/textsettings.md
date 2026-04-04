# Source: https://docs.syncfusion.com/windowsforms/percent-textbox/textsettings.md

# Source: https://docs.syncfusion.com/windowsforms/integer-textbox/textsettings.md

# Source: https://docs.syncfusion.com/windowsforms/folder-browser/textsettings.md

# Source: https://docs.syncfusion.com/windowsforms/classic/currency-edit/textsettings.md

# Text Settings in Windows Forms CurrencyEdit

The below properties will let you control the behavior of the text in the [CurrencyEdit](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.CurrencyEdit.html) control.

* [ShowTextBox](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.CurrencyEdit.html#Syncfusion_Windows_Forms_Tools_CurrencyEdit_ShowTextBox)
* [Text](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.CurrencyEdit.html#Syncfusion_Windows_Forms_Tools_CurrencyEdit_Text)
* [TextBox](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.CurrencyEdit.html#Syncfusion_Windows_Forms_Tools_CurrencyEdit_TextBox)
* [TextAlign](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.ButtonEdit.html#Syncfusion_Windows_Forms_Tools_ButtonEdit_TextAlign)
* [TransferFromCalculator](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.CurrencyEdit.html#Syncfusion_Windows_Forms_Tools_CurrencyEdit_TransferFromCalculator)
* [TransferToCalculator](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.CurrencyEdit.html#Syncfusion_Windows_Forms_Tools_CurrencyEdit_TransferToCalculator)
* [DecimalValue](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.CurrencyEdit.html#Syncfusion_Windows_Forms_Tools_CurrencyEdit_DecimalValue)

{% tabs %}
{% highlight C# %}
this.currencyEdit1.ShowTextBox =Â true;
this.currencyEdit1.Text =Â "$400.00";
this.currencyEdit1.TextAlign =Â HorizontalAlignment.Right;
this.currencyEdit1.TransferFromCalculator=true;
this.currencyEdit1.TransferToCalculator=Â false;
this.currencyEdit1.TextBox.DecimalValue =Â newÂ decimal(newÂ int[] {40000, 0, 0, 131072});
{% endhighlight %}
{% highlight VB %}
Me.currencyEdit1.ShowTextBox =Â True
Me.currencyEdit1.Text =Â "$400.00"
Me.currencyEdit1.TextAlign =Â HorizontalAlignment.Right
Me.currencyEdit1.TransferFromCalculator =Â True
Me.currencyEdit1.TransferToCalculator =Â False
Me.currencyEdit1.TextBox.DecimalValue =Â NewÂ Decimal(NewÂ Integer() {40000, 0, 0, 131072})
{% endhighlight %}
{% endtabs %}

![Text settings](Overview_images/Overview_img417.png) 


N> EnablingÂ [CurrencyEdit.UseVisualStyle](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.ButtonEdit.html#Syncfusion_Windows_Forms_Tools_ButtonEdit_UseVisualStyle)Â property and by setting visual style for control using [CurrencyEdit.ButtonStyle](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.ButtonEdit.html#Syncfusion_Windows_Forms_Tools_ButtonEdit_ButtonStyle) property, we can change the appearance of the calculator button.
