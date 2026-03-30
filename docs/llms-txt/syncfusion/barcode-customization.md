# Source: https://docs.syncfusion.com/flutter/barcode/barcode-customization.md

# Source: https://docs.syncfusion.com/winui/barcode/barcode-customization.md

# Source: https://docs.syncfusion.com/windowsforms/barcode/barcode-customization.md

# Source: https://docs.syncfusion.com/wpf/barcode/barcode-customization.md

# Barcode Customization in WPF Barcode (SfBarcode)

The color of the barcode can be customized by modifying the DarkBarBrush and LightBarBrush properties of the barcode control. 

{% highlight html %}

<sync:SfBarcode x:Name="barcode" Text="82698640929" DarkBarBrush=âRedâ LightBarBrush="Blueâ Symbology="QRBarcode"/>

{% endhighlight  %}


The DarkBarBrush represents the color of the dark bar (Black color usually) and the LightBarBrush represents the color of the gap between two adjacent black bars (White color usually).

![WPF-Barcode-Red-Color-Combination](Barcode-Customization_images/wpf-barcode-red-color-combination.png)

Barcode color combinations- Red
{:.caption}


![WPF-Barcode-Blue-Color-Combination](Barcode-Customization_images/wpf-barcode-blue-color-combination.png)

Barcode color combinations- Blue
{:.caption}

N> The DarkBarBrush and LightBarBrush customizations are applicable only for one dimensional barcodes. In order for a barcode symbol to be recognized by a scanner, there must be an adequate contrast between the dark bars and the light spaces and not all the barcode scanners have support for colored barcodes.
