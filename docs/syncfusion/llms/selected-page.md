# Source: https://docs.syncfusion.com/wpf/tab-splitter/selected-page.md

# Selected Page in WPF Tab Splitter

You can set the selected page by using the [IsSelectedPage](https://help.syncfusion.com/cr/wpf/Syncfusion.Windows.Tools.Controls.SplitterPage.html#Syncfusion_Windows_Tools_Controls_SplitterPage_IsSelectedPage) property. If this property is set to _true_, the page is selected, else it is not selected.

{%tabs%}
{% highlight xaml %}

Â <!-- Adding TabSplitter -->

<syncfusion:TabSplitter Name="tabsplitter">



Â Â Â  <!-- Adding TabSplitterItem -->

<syncfusion:TabSplitterItem Header="Window1.xml" Â Name="tabSplitterItem1">



Â Â Â Â Â Â Â  <!-- Adding TopPanelItems -->

Â Â Â Â Â Â Â  <syncfusion:TabSplitterItem.TopPanelItems>Â 

Â Â Â Â Â Â Â Â Â Â Â  <!-- Adding SplitterPage -->

<syncfusion:SplitterPage IsSelectedPage="True" Name="splitterPage1" Header="XAML">

Â Â Â Â Â Â Â Â Â Â Â  </syncfusion:SplitterPage>

Â Â Â Â Â Â Â  </syncfusion:TabSplitterItem.TopPanelItems>



Â Â Â Â Â Â Â  <!-- Adding BottomPanelItems -->

Â Â Â Â Â Â Â  <syncfusion:TabSplitterItem.BottomPanelItems>Â 

Â Â Â Â Â Â Â Â Â Â Â  <!-- Adding SplitterPage -->

Â Â Â Â Â Â Â Â Â Â Â  <syncfusion:SplitterPage Name="splitterPage2" Header="Design">

Â Â Â Â Â Â Â Â Â Â Â  </syncfusion:SplitterPage>

Â Â Â Â Â Â Â  </syncfusion:TabSplitterItem.BottomPanelItems>



Â Â Â  </syncfusion:TabSplitterItem>



</syncfusion:TabSplitter>
{% endhighlight %}

{% highlight c# %}



// Enable the IsSelectedPage property.

splitterPage1.IsSelectedPage = true;
{% endhighlight %}

{%endtabs%}
![Selected page](Selected-Page_images/Selected-Page_img1.png)





