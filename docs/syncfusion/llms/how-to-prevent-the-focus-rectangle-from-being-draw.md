# Source: https://docs.syncfusion.com/windowsforms/tabcontrol/faq/how-to-prevent-the-focus-rectangle-from-being-draw.md

# How to prevent the Focus Rectangle from being drawn in the Tabs?

You can easily do this by handling the [DrawItem](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.TabControlAdv.html) event, adjusting the [DrawTabEventArgs](https://help.syncfusion.com/cr/windowsforms/Syncfusion.Windows.Forms.Tools.DrawTabEventArgs.html) and delegating drawing to the default drawing logic.

{% tabs %}

{% highlight C# %}


private void TabControlExt_DrawItem(object sender, Syncfusion.Windows.Forms.Tools.DrawTabEventArgs drawItemInfo)

{

// To indicate that the tab gets drawn as if itâs not focused (without the focus rect).

drawItemInfo.State &= ~DrawItemState.Focus;



// Then forward drawing to default drawing logic.

drawItemInfo.DrawBackground();

drawItemInfo.DrawInterior();

drawItemInfo.DrawBorders();

}

{% endhighlight %}

{% highlight VB %}

Private Sub TabControlExt_DrawItem(sender As Object, drawItemInfo As Syncfusion.Windows.Forms.Tools.DrawTabEventArgs)

'To indicate that the tab gets drawn as if itâs not focused (without the focus rect).

Dim & As drawItemInfo.State = ~DrawItemState.Focus



'Then forward drawing to default drawing logic.

drawItemInfo.DrawBackground()

drawItemInfo.DrawInterior()

drawItemInfo.DrawBorders()

End Sub

{% endhighlight %}

{% endtabs %}
