# Source: https://docs.syncfusion.com/windowsforms/classic/databoundgrid/how-to/how-to-include-an-icon-in-the-column-header.md

# Source: https://docs.syncfusion.com/windowsforms/grid-control/how-to/cell-types/how-to-include-an-icon-in-the-column-header.md

# How to include an icon in the column header in WinForms GridControl

The GridControl will allow you to place images in cells by specifying style.ImageIndex and style.ImageList value for the cell, provided style.CellType is either "Static" or "Text Box". So, to make your header cell hold an icon, make it "Static" and set the following properties.

{% tabs %}
{% highlight c# %}

//GridControl.
this.gridControl1[0,3].CellType = "Static";
this.gridControl1[0,3].CellAppearance = GridCellAppearance.Raised;
this.gridControl1[0,3].ImageList = this.imageList1; 
this.gridControl1[0,3].ImageIndex = 1; 

{% endhighlight  %}

{% highlight vb %}
'GridControl. 
Me.gridControl1(0,3).CellType = "Static"
Me.gridControl1(0,3).CellAppearance = GridCellAppearance.Raised
Me.gridControl1(0,3).ImageList = imageList
Me.gridControl1(0,3).ImageIndex = 1

{% endhighlight  %}
{% endtabs %}