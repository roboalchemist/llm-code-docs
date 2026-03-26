# Source: https://docs.syncfusion.com/windowsforms/classic/currency-edit/calculatorsettings.md

# Calculator Settings in Windows Forms CurrencyEdit

A [CurrencyEdit](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.CurrencyEdit.html) control has a text field and a Calculator button, pressing which will open a Calculator control. The below image illustrates the same.

![Calculator](Overview_images/Overview_img416.png) 

The below properties which controls the behavior of the Calculator button.

* [ShowCalculator](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.CurrencyEdit.html#Syncfusion_Windows_Forms_Tools_CurrencyEdit_ShowCalculator)
* [CalculatorButton](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.CurrencyEdit.html#Syncfusion_Windows_Forms_Tools_CurrencyEdit_CalculatorButton)
* [CalculatorLayoutType](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.CurrencyEdit.html#Syncfusion_Windows_Forms_Tools_CurrencyEdit_CalculatorLayoutType)
* [PopupCalculatorAlignment](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.CurrencyEdit.html#Syncfusion_Windows_Forms_Tools_CurrencyEdit_PopupCalculatorAlignment)
* [CloseAction](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.CurrencyEdit.html#Syncfusion_Windows_Forms_Tools_CurrencyEdit_CloseAction)

{% tabs %}

{% highlight c# %}

this.currencyEdit1.CalculatorLayoutType = Syncfusion.Windows.Forms.Tools.CalculatorLayoutTypes.WindowsStandard;

this.currencyEdit1.CloseAction = Syncfusion.Windows.Forms.Tools.CalcActions.CalcOperatorEquals;

this.currencyEdit1.PopupCalculatorAlignment = Syncfusion.Windows.Forms.Tools.CalculatorPopupAlignment.Left;

this.currencyEdit1.ShowCalculator =Â true;

this.currencyEdit1.TransferFromCalculator =Â true;

this.currencyEdit1.TransferToCalculator =Â true;

{% endhighlight %}

{% highlight vbnet %}

Me.currencyEdit1.CalculatorLayoutType = Syncfusion.Windows.Forms.Tools.CalculatorLayoutTypes.WindowsStandard

Me.currencyEdit1.CloseAction = Syncfusion.Windows.Forms.Tools.CalcActions.CalcOperatorEquals

Me.currencyEdit1.PopupCalculatorAlignment = Syncfusion.Windows.Forms.Tools.CalculatorPopupAlignment.Left

Me.currencyEdit1.ShowCalculator =Â True

Me.currencyEdit1.TransferFromCalculator =Â True

Me.currencyEdit1.TransferToCalculator =Â True

{% endhighlight %}

{% endtabs %}
