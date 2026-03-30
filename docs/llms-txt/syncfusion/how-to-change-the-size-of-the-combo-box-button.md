# Source: https://docs.syncfusion.com/windowsforms/grid-control/how-to/cell-types/how-to-change-the-size-of-the-combo-box-button.md

# How to change the size of the combo box Button in WinForms GridControl

Change the size of the combobox button by changing the ButtonBarSize in the CellModel for the control. 

{% tabs %}
{% highlight c# %}

//Creates Combobox Cell model object.
GridComboBoxCellModel model = this.grid.Model.CellModels["ComboBox"] as GridComboBoxCellModel;

//Assigns a new value to its ButtonBarSize property. 
model.ButtonBarSize = new Size(8, 8);

{% endhighlight %}

{% highlight vb %}

'Creates Combobox Cell model object.
Dim model As GridComboBoxCellModel = CType(Me.Grid.Model.CellModels("ComboBox"), GridComboBoxCellModel)

'Assigns a new value to its ButtonBarSize property.
model.ButtonBarSize = New Size(8, 8)

{% endhighlight %}
{% endtabs %}