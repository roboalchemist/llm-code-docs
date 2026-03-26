# Source: https://docs.syncfusion.com/wpf/classic/richtextboxadv/inserting-a-ui-element.md

# Inserting-a-UI-Element in WPF RichTextBoxAdv (Classic)

In order to insert a UI element in the document, ParagraphAdv provides an inline called UIContainerAdv.

### Properties



<table>
<tr>
<th>
Property</th><th>
Description</th><th>
Type</th><th>
Data Type</th></tr>
<tr>
<td>
Height</td><td>
Specifies the height of the image.</td><td>
Dependency Property</td><td>
Double</td></tr>
<tr>
<td>
Width</td><td>
Specifies the width of the image.</td><td>
Dependency Property</td><td>
Double</td></tr>
<tr>
<td>
UIElement</td><td>
Specifies the UI element to be added.</td><td>
Dependency Property</td><td>
UIElement</td></tr>
<tr>
<td>
FitToContent</td><td>
Fits the UIElement based on the size of a page.</td><td>
Dependency Property</td><td>
Boolean</td></tr>
</table>


## Adding UIElement to an Application

UIContainerAdv can be used to add a UI element directly to an application by using the following code snippet: 

{% tabs %}
{% highlight xaml %}


 Â Â Â 
 <syncfusion:RichTextBoxAdv Height="300" Width="400" x:Name="richtext">Â Â Â Â Â Â Â Â Â Â Â 
 <syncfusion:DocumentAdv>Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â  
 <syncfusion:SectionAdv>Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â 
 <syncfusion:ParagraphAdv >Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â 
 <syncfusion:UIContainerAdv >Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â  
 <Button />Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â 
 </syncfusion:UIContainerAdv>Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â 
 </syncfusion:ParagraphAdv>Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â 
 </syncfusion:SectionAdv>Â Â Â Â Â Â Â Â Â Â Â 
 </syncfusion:DocumentAdv>Â Â Â Â Â Â Â  
 </syncfusion:RichTextBoxAdv>
{% endhighlight %}
 
{% highlight C# %}

Â Â Â Â Â       
RichTextBoxAdv richtext = new RichTextBoxAdv();           
DocumentAdv document = new DocumentAdv();           
SectionAdv section = new SectionAdv();          
 ParagraphAdv paragraph = new ParagraphAdv();           
 UIContainerAdv uicontainer = new UIContainerAdv();           
 uicontainer.UIElement = new Button();           
 paragraph.Inlines.Add(uicontainer);          
 section.Blocks.Add(paragraph);           
 document.Sections.Add(section);          
 richtext.Document = document;
{% endhighlight %}
{% endtabs %}

## Limitations

Cut, copy, and paste operations are not permitted for the UIElement.

