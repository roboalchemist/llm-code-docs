# Source: https://docs.syncfusion.com/wpf/olap-client/calculated-members.md

# Calculated Members in WPF Olap Client

This feature allows users to define measures and members using the calculated member editor. The calculated member editor can be opened just by clicking the respective icon available in the OLAP client toolbar. The icon will be visible only by setting the `IsCalculatedMembersEnabled` property to true.

![Calculated memeber option is enabled in OlapClient toolbar](Calculated-Members_images/Calculated-Members_img1.png)

![Calculated member editor window](Calculated-Members_images/Calculated-Members_img2.png)

{% tabs %}

{% highlight xaml %}

<CheckBoxÂ Name="chk_CalcMember  ToolTip="Enable/DisableÂ CalculatedÂ Members"Â Content="EnableÂ CalculatedÂ Members"Â 
          IsChecked="{BindingÂ ElementName=olapClient1,Â Path=IsCalculatedMembersEnabled}"/>

{% endhighlight %}

{% highlight C# %}  

this.olapClient1.IsCalculatedMembersEnabledÂ =Â true;Â 

{% endhighlight %} 

{% highlight vbnet %}

Me.olapClient1.IsCalculatedMembersEnabledÂ =Â TrueÂ 

{% endhighlight %}

{% endtabs %}

A sample demo is available at the following location.

{system drive}:\Users\&lt;User Name&gt;\AppData\Local\Syncfusion\EssentialStudio\&lt;Version Number&gt;\WPF\OlapClient.WPF\Samples\Product Showcase\CalculatedMembers


