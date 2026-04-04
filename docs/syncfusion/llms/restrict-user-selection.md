# Source: https://docs.syncfusion.com/wpf/rating/restrict-user-selection.md

# Source: https://docs.syncfusion.com/maui/rating/restrict-user-selection.md

# Restrict user selection in .NET MAUI Rating (SfRating)

[`SfRating`](https://help.syncfusion.com/cr/maui/Syncfusion.Maui.Inputs.SfRating.html) control support for changeable or unchangeable values for Rating control. This is achieved by the [`IsReadOnly`](https://help.syncfusion.com/cr/maui/Syncfusion.Maui.Inputs.SfRating.html#Syncfusion_Maui_Inputs_SfRating_IsReadOnly) property. When this property is set to True, the Rating value becomes unchangeable. By default, this property value is set to False.

{% tabs %}

{% highlight xaml %}

<rating:SfRating x:Name="rating" IsReadOnly="true" />

{% endhighlight %}

{% highlight C# %}


SfRating rating = new SfRating();
rating.IsReadOnly = true;

	
{% endhighlight %}

{% endtabs %}

![readOnly](images/IsReadOnly.gif)


