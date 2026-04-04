# Source: https://docs.syncfusion.com/windowsforms/classic/multiselectioncombobox/faq/how-to-bind-a-multiselectioncombobox-with-external-data-source.md

# MultiSelectionCombobox in Windows Forms

This page explains How to Bind a MultiSelectionComboBox with External Data Source and more details.

## How to Bind a MultiSelectionComboBox with External Data Source

You can achieve this by using DataSource and DisplayMember properties in MultiSelectionComboBox. 

The following code sample defines how to bind MultiSelectionComboBox with datasource.

{% tabs %}
{% highlight c# %}

// Create a DataTable.Â Â Â Â Â Â Â Â Â Â Â Â Â 
DataTable dt =Â newÂ DataTable("Table1");

// Adding Columns.
dt.Columns.Add("FirstName");
dt.Columns.Add("LastName");
dt.Columns.Add("occupation");
dt.Columns.Add("place");

// Create a Data Set.
DataSet ds =Â newÂ DataSet();
ds.Tables.Add(dt);
dt.Rows.Add(newÂ string[] { "John", "Tina", "Doctor", "Italy" });
dt.Rows.Add(newÂ string[] { "Mary", "anu", "Teacher", "America" });
dt.Rows.Add(newÂ string[] { "asha", "roy", "Staff", "London" });
dt.Rows.Add(newÂ string[] { "George", "Gaskin", "Nurse", "germany" });
dt.Rows.Add(newÂ string[] { "sam", "jens", "Engineer", "Russia" });
dt.Rows.Add(newÂ string[] { "Ben", "Geo", "Developer", "India" });

// Create a DataView.
DataView view =Â newÂ DataView(dt);

// Set DataSource.
this.comboBoxAdv1.DataSource = view;

// Set DisplayMember.
this.comboBoxAdv1.DisplayMember = "place";

{% endhighlight %}

{% highlight vb %}

' Create a DataTable.Â Â Â Â 
DimÂ dtÂ AsÂ DataTable =Â NewÂ DataTable("Table1")

' Adding Columns.
dt.Columns.Add("FirstName")Â 
dt.Columns.Add("LastName")Â 
dt.Columns.Add("occupation")Â 
dt.Columns.Add("place")

' Create a Data Set.
DimÂ dsÂ AsÂ DataSet =Â NewÂ DataSetÂ 
ds.Tables.Add(dt)Â 
dt.Rows.Add(NewÂ String() {"John", "Tina", "Doctor", "Italy"})Â 
dt.Rows.Add(NewÂ String() {"Mary", "anu", "Teacher", "America"})Â 
dt.Rows.Add(NewÂ String() {"asha", "roy", "Staff", "London"})Â 
dt.Rows.Add(NewÂ String() {"George", "Gaskin", "Nurse", "germany"})Â 
dt.Rows.Add(NewÂ String() {"sam", "jens", "Engineer", "Russia"})Â 
dt.Rows.Add(NewÂ String() {"Ben", "Geo", "Developer", "India"})

' Create a DataView.
DimÂ viewÂ AsÂ DataView =Â NewÂ DataView(dt)

' Set DataSource.Â 
Me.comboBoxAdv1.DataSource = view

' Set DisplayMember.
Me.comboBoxAdv1.DisplayMember = "place"

{% endhighlight %}
{% endtabs %}
