# Source: https://docs.syncfusion.com/maui/chips/how-to/applying-fonticon-to-syncfusion-chip-control.md

# Setting the FontIcon to SfChip

SfChip is supported to display the font icon by setting [`FontImageSource`] to its [ImageSource](https://help.syncfusion.com/cr/maui/Syncfusion.Maui.Core.SfChip.html#Syncfusion_Maui_Core_SfChip_ImageSource) property with following below steps.

Create the instance for `FontImageSource` and set to `ImageSource` property of SfChip as shown in the below code snippet.

{% tabs %}

{% highlight xaml %}

   <chip:SfChip x:Name="chip" 
                Text="Syncfusion" 
                ShowIcon="True"
                FontSize="17"
                TextColor="White"
                Background="#512dcd"
                WidthRequest="120"
                HeightRequest="40"
                ImageSize="15"
                Padding="0,0,0,2">
        <chip:SfChip.ImageSource>
            <FontImageSource Glyph="&#xEB52;" 
                             Size="12"
                             Color="White"
                             FontFamily="Segoe MDL2 Assets">
            </FontImageSource>
        </chip:SfChip.ImageSource>
    </chip:SfChip>

{% endhighlight %}

{% highlight c# %}

var fontImageSource = new FontImageSource
{
    Glyph = "\uEB52",
    Size = 12,
    Color = Colors.White,
    FontFamily = "Segoe MDL2 Assets"
};
SfChip chip = new SfChip
{
    ShowIcon = true,
    Text = "Syncfusion",
    FontSize = 17,
    TextColor = Colors.White,
    Background = Color.FromArgb("#512dcd"), 
    WidthRequest = 120,
    HeightRequest = 40,
    ImageSize = 15,
    Padding = new Thickness(0, 0, 0, 2),
    ImageSource = fontImageSource
};
 
{% endhighlight %}

{% endtabs %}

![.NET MAUI chip icon font support](images/AppIcon.png)
