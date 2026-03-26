# Source: https://docs.syncfusion.com/windowsforms/grid-control/how-to/cell-types/how-to-enable-double-click-on-the-formula-cell.md

# How to enable double-click on the formula cell in WinForms GridControl

To enable double-click on the formula cell, set ForceEditWhenActivated property to _False_. ActivateCurrentCellBehavior property cannot be achieved in GridFormulaCellRender unless the property is set to _False_. 

{% tabs %}
{% highlight c# %}

this.gridControl1.ActivateCurrentCellBehavior = GridCellActivateAction.DblClickOnCell;
GridFormulaCellRenderer.ForceEditWhenActivated = false ;

{% endhighlight %}

{% highlight vb %}
Me.gridControl1.ActivateCurrentCellBehavior = GridCellActivateAction.DblClickOnCell
GridFormulaCellRenderer.ForceEditWhenActivated = False

{% endhighlight %}
{% endtabs %}