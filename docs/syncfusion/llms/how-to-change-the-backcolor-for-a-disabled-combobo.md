# Source: https://docs.syncfusion.com/windowsforms/classic/combobox/faq/how-to-change-the-backcolor-for-a-disabled-combobo.md

# How to change the BackColor for a disabled ComboBoxAdv

This page explains How to Change the BackColor for a Disabled ComboBoxAdv Control and more details.

## Â How to Change the BackColor for a Disabled ComboBoxAdv Control

Previously, once the ComboBoxAdv control was disabled, theÂ BackColorÂ property of the control could not be changed. This was due to the fact that, by default, all the properties of the control were disabled once the control was disabled.

Now, you can set the BackColor for the ComboBoxAdv control even in its disabled state by using theÂ UseBackColor property.

{% tabs %}
{% highlight c# %}

//To change the backcolor of disabled ComboBoxAdv
this.comboBoxAdv1.UseBackColor = true;
this.comboBoxAdv1.BackColor = Color.Red;


{% endhighlight %}


{% highlight vb %}

'To change the backcolor of disabled comboBoxAdv
 Me.comboBoxAdv1.UseBackColor = True
 Me.comboBoxAdv1.BackColor = Color.Red

{% endhighlight %}
{% endtabs %}