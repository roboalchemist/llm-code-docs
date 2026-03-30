# Source: https://docs.syncfusion.com/windowsforms/autocomplete/faq/how-to-remove-default-selection-from-autocomplete-drop-down.md

# How to remove default selection from AutoComplete dropdown?

To remove the default selection in AutoComplete dropdown, set SelectedIndex property to _-1_ inside the DropdownDisplayed event of the AutoComplete control as follows.



{% highlight C# %}


private void autoComplete1_DropDownDisplayed(object sender, EventArgs e)

{

    this.autoComplete1.SelectedIndex = -1;

}
{% endhighlight %}





{% highlight vbnet %}




Private Sub autoComplete1_DropDownDisplayed(ByVal sender As Object, ByVal e As EventArgs)

    Me.autoComplete1.SelectedIndex = -1

End Sub
{% endhighlight %}