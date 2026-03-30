# Source: https://docs.syncfusion.com/windowsforms/integer-textbox/bannertextsupport.md

# Banner Text Support in Windows Forms Integer TextBox

The IntegerTextBox control can display banner text in the text field, at run time. AÂ [BannerTextProvider](/windowsforms/watermark-text-provider/overview) should be available for this purpose. Also, we need to set [AllowNull](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.NumberTextBoxBase.html#Syncfusion_Windows_Forms_Tools_NumberTextBoxBase_AllowNull), [NullString](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.NumberTextBoxBase.html#Syncfusion_Windows_Forms_Tools_NumberTextBoxBase_NullString) and [Text](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.IntegerTextBox.html#Syncfusion_Windows_Forms_Tools_IntegerTextBox_Text) properties as below, to make this feature effective.

{% tabs %}

{% highlight C# %}

this.integerTextBox1.AllowNull =Â true;
this.integerTextBox1.NullString = "";
this.integerTextBox1.Text = "";

{% endhighlight %}

{% highlight VB %}

Me.integerTextBox1.AllowNull =Â True
Me.integerTextBox1.NullString = ""
Me.integerTextBox1.Text = ""

{% endhighlight %}
{% endtabs %}
