# Source: https://docs.syncfusion.com/wpf/olap-common/how-to/save-the-report-as-xml-file.md

# Save the report as XML file

The user can save the current report set of OlapDataManager as an XML file for the future needs by using the SaveReport method.

The following code snippet will illustrate the saving of the current report set as an XML file:

{% tabs %}
{% highlight c# %}



olapDataManager.SaveReport(@"C:\SampleReport\RevenueAnalysis.xml");


{% endhighlight  %}


{% highlight vbnet %}



olapDataManager.SaveReport("C:\SampleReport\RevenueAnalysis.xml")


{% endhighlight  %}
{% endtabs %}


## For Silverlight:

You can save the current report of OlapDataManger as an XML file for their future use by serializing the report with XmlSerializer.

The following code snippet will illustrate the saving of the current report set as an XML file:

{% tabs %}
{% highlight c# %}



privateÂ voidÂ SaveReport()
{
Â Â Â SaveFileDialogÂ dlgÂ =Â newÂ SaveFileDialog();
 Â Â dlg.FilterÂ =Â "XMLÂ filesÂ (*.xml)|*.xml";

Â Â Â bool?Â bÂ =Â dlg.ShowDialog();

Â  Â ifÂ (b.HasValueÂ &&Â b.Value)
Â Â Â {
Â Â Â Â Â Â usingÂ (StreamÂ streamÂ =Â dlg.OpenFile())
Â Â  Â Â Â {
Â Â Â Â Â Â Â Â Â System.Xml.Serialization.XmlSerializerÂ serializerÂ =Â newÂ System.Xml.Serialization.XmlSerializer(typeof(OlapReport));
Â Â Â Â Â Â Â Â Â serializer.Serialize(stream,Â this.olapDataManager.CurrentReport);Â Â Â Â Â Â Â Â Â Â Â Â Â 
Â Â Â Â Â Â }
Â Â Â }Â Â Â Â Â Â Â Â Â Â Â Â 
}
{% endhighlight  %}




{% highlight vbnet %}



Private Sub SaveReport()

   Dim dlg As SaveFileDialog = New SaveFileDialog()

   dlg.Filter = "XML files (*.xml)|*.xml"



   Dim b As Nullable(Of Boolean) = dlg.ShowDialog()



   If b.HasValue AndAlso b.Value Then

Using stream As Stream = dlg.OpenFile()

Dim serializer As System.Xml.Serialization.XmlSerializer = New System.Xml.Serialization.XmlSerializer(GetType(OlapReport))

serializer.Serialize(stream, Me.olapDataManager.CurrentReport)

End Using

   End If

End Sub



{% endhighlight  %}
{% endtabs %}
