# Source: https://docs.syncfusion.com/windowsforms/classic/combobox/faq/how-to-programmatically-select-the-record-in-the-dropdown.md

# How to programmatically select the record in the Dropdown

This page explains How to Programmatically Select the Record in the Dropdown that matches the Text Typed in ComboBoxAdv and more details.

## How to Programmatically Select the Record in the Dropdown that matches the Text Typed in ComboBoxAdv

You can handle the DropDown event of the ComboBoxAdv control and set it as shown in the following code example.

{% tabs %}
{% highlight c# %}

//ComboBoxAdv dropdown event
private void comboBoxAdv1_DropDown(object sender, System.EventArgs e)
{
    this.comboBoxAdv1.ListBox.SelectedItem = this.comboBoxAdv1.TextBox.Text;
}

{% endhighlight %}

{% highlight vb %}

'ComboBoxAdv dropdown event
Private Sub comboBoxAdv1_DropDown(ByVal sender As Object, ByVal e As System.EventArgs)
    Me.comboBoxAdv1.ListBox.SelectedItem = Me.comboBoxAdv1.TextBox.Text
End Sub

{% endhighlight %}
{% endtabs %}

