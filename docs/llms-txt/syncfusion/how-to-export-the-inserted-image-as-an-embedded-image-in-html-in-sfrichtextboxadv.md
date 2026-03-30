# Source: https://docs.syncfusion.com/document-processing/word/word-processor/wpf/faq-section/how-to-export-the-inserted-image-as-an-embedded-image-in-html-in-sfrichtextboxadv.md

# Source: https://docs.syncfusion.com/document-processing/word/word-processor/uwp/faq-section/how-to-export-the-inserted-image-as-an-embedded-image-in-html-in-sfrichtextboxadv.md

# Export Image as Embedded in HTML in UWP SfRichTextBoxAdv

This page explains how to export the inserted image as an Embedded image in HTML in Syncfusion&reg; UWP SfRichTextBoxAdv.

In the SfRichTextBoxAdv control, we offer an option to specify HTML export settings. By utilizing the [ImageNodeVisitedEvent](https://help.syncfusion.com/cr/uwp/Syncfusion.UI.Xaml.RichTextBoxAdv.ImageNodeVisitedEventArgs.html) event of the [HtmlImportExportSettings](https://help.syncfusion.com/cr/uwp/Syncfusion.UI.Xaml.RichTextBoxAdv.HtmlImportExportSettings.html) instance, you can both retrieve and define the image stream and image source. When setting the image source as Empty, the inserted picture can be exported as an embedded image in the HTML.

The following code example illustrates to export the inserted image as an Embedded image in HTML in the SfRichTextBoxAdv.

{% tabs %}
{% highlight c# %}
// Hooks the event handler for ImageNodeVisited event.
richTextBoxAdv.HtmlImportExportSettings.ImageNodeVisited += HtmlImportExportSettings_ImageNodeVisited;

/// <summary>
/// Handles the ImageNodeVisited event of the richTextBoxAdv control.
/// </summary>
/// <param name="obj">The source of the event.</param>
/// <param name="args">The <see cref="ImageNodeVisitedEventArgs"/> instance containing the event data.</param>
 private void HtmlImportExportSettings_ImageNodeVisited(object obj, Syncfusion.UI.Xaml.RichTextBoxAdv.ImageNodeVisitedEventArgs args)
        {
            if (args.IsSaving)
            {
                args.Source = string.Empty;
            }
        }
		
// Unhooks the event handler for ImageNodeVisited event.
richTextBoxAdv.HtmlImportExportSettings.ImageNodeVisited -= HtmlImportExportSettings_ImageNodeVisited;
{% endhighlight %}
{% endtabs %}