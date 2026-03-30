# Source: https://docs.syncfusion.com/windowsforms/double-textbox/overriding-the-behavior-of-certain-keystrokes-in-a-doubletextbox.md

# Overriding the Behavior in a Double text box in Windows Forms

This can be done by overriding the HandleSubtractKey(). Given below is the code snippet which shows an example of how to clear the text when the NegativeSign is changed.

{% tabs %}
{% highlight C# %}  
publicÂ classÂ DoubleTextBoxAdvÂ : Syncfusion.Windows.Forms.Tools.DoubleTextBox
{
Â Â Â Â publicÂ DoubleTextBoxAdv() :Â base() { }
Â Â Â Â privateÂ boolÂ deleteonnegative =Â false;
Â Â Â Â publicÂ boolÂ DeleteOnNegative
Â Â Â  {
Â Â Â Â Â Â Â Â get
Â Â Â Â Â Â Â  {
Â Â Â Â Â Â Â Â Â Â Â Â returnÂ deleteonnegative;
Â Â Â Â Â Â Â  }
Â Â Â Â Â Â Â Â set
Â Â Â Â Â Â Â  {
Â Â Â Â Â Â Â Â Â Â Â  deleteonnegative =Â value;
Â Â Â Â Â Â Â  }
Â Â Â  }
 Â Â Â // Overrides the behavior of SubtractKey so that the text is cleared when the NegativeSign is changed.
Â Â Â Â protectedÂ overrideÂ Syncfusion.Windows.Forms.Tools.NumberModifyStateÂ HandleSubtractKey()
Â Â Â  {
Â Â Â Â Â Â Â Â ifÂ (deleteonnegative ==Â true)
Â Â Â Â Â Â Â  {
Â Â Â Â Â Â Â Â Â Â Â Â ifÂ (this.NegativeSign ==Â "-"Â &&Â this.Text.StartsWith("-"))
Â Â Â Â Â Â Â Â Â Â Â  {
Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â this.Clear();
Â Â Â Â Â Â Â Â Â Â Â  }
Â Â Â Â Â Â Â  }
Â Â Â Â Â Â Â Â returnÂ base.HandleSubtractKey();
Â Â Â  }
}
{% endhighlight %}
{% highlight VB %} 
PublicÂ ClassÂ DoubleTextBoxAdv
Â Â Â Â InheritsÂ Syncfusion.Windows.Forms.Tools.DoubleTextBox
Â Â Â Â PublicÂ SubÂ New()
Â Â Â Â Â Â Â Â MyBase.New()
Â Â Â Â EndÂ Sub
Â Â Â Â PrivateÂ m_deleteonnegativeÂ AsÂ BooleanÂ =Â False
  Â Â PublicÂ PropertyÂ DeleteOnNegative()Â AsÂ Boolean
Â Â Â Â Â Â Â Â Get
Â Â Â Â Â Â Â Â Â Â Â Â ReturnÂ m_deleteonnegative
Â Â Â Â Â Â Â Â EndÂ Get
Â Â Â Â Â Â Â Â Set(ByValÂ valueÂ AsÂ Boolean)
Â Â Â Â Â Â Â Â Â Â Â  m_deleteonnegative = value
Â Â Â Â Â Â Â Â EndÂ Set
Â Â Â Â EndÂ Property
Â Â Â Â ' Overrides the behavior of Subtract Key so that the text is cleared when the NegativeSign is changed.
Â Â Â Â ProtectedÂ OverloadsÂ OverridesÂ FunctionÂ HandleSubtractKey()Â AsSyncfusion.Windows.Forms.Tools.NumberModifyState
Â Â Â Â Â Â Â Â IfÂ m_deleteonnegative =Â TrueÂ Then
Â Â Â Â Â Â Â Â Â Â Â Â IfÂ Me.NegativeSign =Â "-"Â AndAlsoÂ Me.Text.StartsWith("-")Â Then
Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Me.Clear()
Â Â Â Â Â Â Â Â Â Â Â Â EndÂ If
Â Â Â Â Â Â Â Â EndÂ If
Â Â Â Â Â Â Â Â ReturnÂ MyBase.HandleSubtractKey()
Â Â Â Â EndÂ Function
EndÂ Class
{% endhighlight %}
{% endtabs %}

![Double text box key strokes](DoubleTextBox-images/DoubleTextBox_img5.png)

