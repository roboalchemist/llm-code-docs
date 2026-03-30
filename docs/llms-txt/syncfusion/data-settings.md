# Source: https://docs.syncfusion.com/windowsforms/classic/combobox/data-settings.md

# Data Settings in Windows Forms ComboBoxAdv(Classic)

Data for the ComboBoxAdv is added through String Collection Editor, invoked throughÂ the ComboBoxAdv.Items property.

![Overview_img302](Overview_images/Overview_img302.png) 

{% tabs %}
{% highlight c# %}

//Adding data to ComboBoxAdv

this.comboBoxAdv1.Items.AddRange(new object[] { "Currency", "DateTimePicker", "ComboBoxAdv", "AutoComplete", "ListBox", "ContextMenu", "CurrencyEdit" });

{% endhighlight %}

{% highlight vb %}

'Adding data to ComboBoxAdv

Me.comboBoxAdv1.Items.AddRange(New Object() {"Currency", "DateTimePicker", "ComboBoxAdv", "AutoComplete", "ListBox", "ContextMenu", _

"CurrencyEdit"})

{% endhighlight %}
{% endtabs %}

![Overview_img303](Overview_images/Overview_img303.png)


N> ComboBoxAdv can also be bound to an external Data source like Data Table. 
ReferÂ [Data binding](/windowsforms/ComboBoxAdv/Advanced-Featureshtml#data-binding)Â _topic To set image for dropdown items refer_Â [Image settings](/windowsforms/ComboBoxAdv/ComboBoxAdv-appearancehtml#image-settings)
