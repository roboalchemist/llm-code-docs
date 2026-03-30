# Source: https://docs.syncfusion.com/wpf/olap-common/how-to/load-xml-report-file.md

# Load XML report file

You can load the XML report set by using the LoadReport method.

The following code snippet will illustrate the loading of the report:
{% tabs %}
{% highlight c# %}



olapDataManager.LoadReport(@"C:\SampleReport\RevenueAnalysis.xml");
{% endhighlight  %}


{% highlight vbnet %}



olapDataManager.LoadReport("C:\SampleReport\RevenueAnalysis.xml")

{% endhighlight  %}
{% endtabs %}

## For Silverlight:



The saved report file can be used with OlapDataManager by serializing it to type OlapReport with XmlSerializer.

The following code snippet will illustrate the loading of a saved XML report file:

{% tabs %}
{% highlight c# %}



Â privateÂ voidÂ LoadReport()
Â {
Â Â Â Â OpenFileDialogÂ dlgÂ =Â newÂ OpenFileDialog();
Â Â Â Â dlg.FilterÂ =Â "XMLÂ filesÂ (*.xml)|*.xml";
Â bool?Â bÂ =Â dlg.ShowDialog();

Â Â Â Â ifÂ (b.HasValueÂ &&Â b.Value)
Â Â Â Â {
Â Â Â Â Â Â Â Â OlapReportÂ reportÂ =Â null;

Â Â Â  Â Â Â Â usingÂ (FileStreamÂ streamÂ =Â dlg.File.OpenRead())
Â Â Â Â Â Â Â Â {
Â Â Â Â Â Â Â Â Â Â Â System.Xml.Serialization.XmlSerializerÂ serializerÂ =Â newÂ System.Xml.Serialization.XmlSerializer(typeof(OlapReportCollection));
Â Â Â Â Â Â Â Â Â Â Â OlapReportCollectionÂ olapReportCollectionÂ =Â serializer.Deserialize(stream)Â asÂ OlapReportCollection;
Â Â Â Â Â Â Â Â Â Â reportÂ =Â olapReportCollection[0];Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â 
Â Â Â Â Â Â Â Â }
Â Â Â Â Â Â Â Â olapDataManager.SetCurrentReport(report);Â Â Â Â Â Â Â Â Â 
Â Â Â Â }Â Â Â Â Â Â Â Â Â Â Â Â 
}


{% endhighlight  %}
{% highlight vbnet %}



Private Sub LoadReport()

Dim dlg As OpenFileDialog = New OpenFileDialog()

dlg.Filter = "XML files (*.xml)|*.xml"

Dim b As Nullable(Of Boolean) = dlg.ShowDialog()



If b.HasValue AndAlso b.Value Then

Dim report As OlapReport = Nothing



Using stream As FileStream = dlg.File.OpenRead()

Dim serializer As System.Xml.Serialization.XmlSerializer = New System.Xml.Serialization.XmlSerializer(GetType(OlapReportCollection))

Dim olapReportCollection As OlapReportCollection = TryCast(serializer.Deserialize(stream), OlapReportCollection)

report = olapReportCollection(0)

End Using

olapDataManager.SetCurrentReport(report)

End If

 End Sub

{% endhighlight  %}
{% endtabs %}
