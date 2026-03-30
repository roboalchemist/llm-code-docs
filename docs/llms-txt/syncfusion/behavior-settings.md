# Source: https://docs.syncfusion.com/windowsforms/classic/autocomplete/behavior-settings.md

# Source: https://docs.syncfusion.com/windowsforms/textbox/behavior-settings.md

# Source: https://docs.syncfusion.com/windowsforms/statusbaradvpanel/behavior-settings.md

# Source: https://docs.syncfusion.com/windowsforms/percent-textbox/behavior-settings.md

# Source: https://docs.syncfusion.com/windowsforms/numericupdown/behavior-settings.md

# Source: https://docs.syncfusion.com/windowsforms/maskedtextbox/behavior-settings.md

# Behavior Settings in MaskedEditBox

The behavior settings of the MaskedEditBox control are discussed below.

### Prompt and padding character settings

The [MaskedEditBox](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.MaskedEditBox.html) control allows you to add prompt characters in the input.

<table>
<tr>
<th>
MaskedEditBox Properties</th><th>
Description</th></tr>
<tr>
<td>
AllowPrompt</td><td>
Specifies if the prompt character can be allowed to be entered as an input character.</td></tr>
<tr>
<td>
PaddingCharacter</td><td>
Specifies the character that will be used instead of mask characters when the mask position has not been filled when the text property is used.</td></tr>
<tr>
<td>
PaddingCharacterInt</td><td>
Gets / sets the integer version of the padding character.</td></tr>
<tr>
<td>
Prompt Character</td><td>
Gets / sets the character that will be used instead of the mask characters when the mask position has not been filled.</td></tr>
<tr>
<td>
PromptCharacterInt</td><td>
Gets / sets the integer version of the PromptCharacter.</td></tr>
<tr>
<td>
PassivePromptCharacter</td><td>
Gets / sets the character that will be used instead of the mask characters when the mask position has not been filled (when the control does not have the focus).</td></tr>
<tr>
<td>
PassivePromptCharacterInt</td><td>
Gets / sets the integer version of the PassivePromptCharacter.</td></tr>
</table>


{% tabs %}

{% highlight C# %}  

this.maskedEditBox1.AllowPrompt =Â true;
this.maskedEditBox.PaddingCharacterInt = 0;
this.maskedEditBox1.PromptCharacterInt = 37;
this.maskedEditBox1.PassivePromptCharacterInt = 47;

{% endhighlight %}

{% highlight VB %} 

Me.maskedEditBox1.AllowPrompt =Â True
Me.maskedEditBox.PaddingCharacterInt = 0
Me.maskedEditBox1.PromptCharacterInt = 37
Me.maskedEditBox1.PassivePromptCharacterInt = 47

{% endhighlight %}

{% endtabs %}

N>Â We can trim the additional spaces present in the mask by setting theÂ PaddingCharacterIntÂ property to '0'.

### MaxLength

The maximum length of the text can be set using the property given below.


<table>
<tr>
<td>
MaskedEditBox Property</td><td>
Description</td></tr>
<tr>
<td>
MaxLength</td><td>
Specifies the maximum number of characters that can be entered into the edit control. The default value is set to '32767'.</td></tr>
</table>

{%tabs %}

{% highlight C# %}  

this.maskedEditBox1.MaxLength = 32800;Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â 

{% endhighlight %}

{% highlight VB %} 

Me.maskedEditBox1.MaxLength = 32800

{% endhighlight %}

{% endtabs %}

### ReadOnly

The ReadOnly mode can be enabled for the MaskedEditBox control using the below given property.

<table>
<tr>
<th>
MaskedEditBox Property</th><th>
Description</th></tr>
<tr>
<td>
ReadOnly</td><td>
Specifies whether the text in the edit control can be changed or not.</td></tr>
</table>

{% tabs %}

{% highlight C# %}  

this.maskedEditBox1.ReadOnly =Â true;

{% endhighlight %}

{% highlight VB %} 

Me.maskedEditBox1.ReadOnly =Â True

{% endhighlight %}

{% endtabs %}
