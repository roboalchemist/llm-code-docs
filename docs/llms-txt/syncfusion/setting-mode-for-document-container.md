# Source: https://docs.syncfusion.com/wpf/tabbed-mdi-form/setting-mode-for-document-container.md

# setting mode for document container in WPF Tabbed MDI Form

Document Container supports two important modes which are listed below. 

* TDI - Tabbed Document Interface
* MDI - Multiple Document Interface

To set the Document Container in TDI mode, use the following code snippet.



{% tabs %}
{% highlight xaml %}
<!-- Adding Document Container -->
<syncfusion:DocumentContainer Name="DocContainer" Mode="TDI">â¦....â¦....
</syncfusion:DocumentContainer>
{% endhighlight %}

{% highlight C# %}
//Creating instance of Document ContainerDocumentContainer DocContainer = new DocumentContainer();
//Set mode as TDIDocContainer.Mode = DocumentContainerMode.TDI;â¦.......â¦.......
//Adding control to window this. Content = DocContainer;
{% endhighlight %}
{% endtabs %}


The following is the screen shot of a document container, which is in TDI mode.



![Setting-Mode-for-Document-Container_img1](Setting-Mode-for-Document-Container_images/Setting-Mode-for-Document-Container_img1.jpeg)





To set the Document Container in MDI mode, use the following code snippet.


{% highlight xaml %}
<!-- Adding Document Container -->
<syncfusion:DocumentContainer Name="DocContainer" Mode="MDI">  â¦....  â¦....
</syncfusion:DocumentContainer>
{% endhighlight %}

{% highlight C# %} 
//Creating instance of Document Container
DocumentContainer DocContainer = new DocumentContainer();
//Set mode as MDIDocContainer.
Mode = DocumentContainerMode.MDI;â¦.......â¦.......
//Adding control to window this.
Content = DocContainer;
{% endhighlight %}



The following screen shot shows the document container in MDI mode.



![Setting-Mode-for-Document-Container_img2](Setting-Mode-for-Document-Container_images/Setting-Mode-for-Document-Container_img2.jpeg)



