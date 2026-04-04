# Source: https://docs.syncfusion.com/maui/digitalgauge/character-segment-types.md

# Character Types in .NET MAUI Digital Gauge (SfDigitalGauge)

The digital characters can be display in the following four different segments:

â¢	SevenSegment
â¢	FourteenSegment
â¢	SixteenSegment
â¢	EightCrossEightDotMatrix

## Seven segment

The seven-segment type is capable of displaying numbers and a few uppercase letters efficiently.

{% tabs %}

{% highlight xaml %}

     <gauge:SfDigitalGauge Text="12345" 
                          CharacterType="SevenSegment" 
                         />

{% endhighlight %}

{% highlight c# %}

            SfDigitalGauge digital = new SfDigitalGauge();

            digital.Text = "12345";

            digital.CharacterType = DigitalGaugeCharacterType.SevenSegment;

{% endhighlight %}

{% endtabs %}

![seven-segment](Images\seven-segment.png)

## Fourteen segment

The fourteen-segment type is capable of displaying numbers and the alphabet efficiently.

{% tabs %}

{% highlight xaml %}

     <gauge:SfDigitalGauge Text="12345" 
                          CharacterType="FourteenSegment" 
                         />

{% endhighlight %}

{% highlight c# %}

            SfDigitalGauge digital = new SfDigitalGauge();

            digital.Text = "12345";

            digital.CharacterType = DigitalGaugeCharacterType.FourteenSegment;

{% endhighlight %}

{% endtabs %}

![fourteen-segment](Images\fourteen-segment.png)

## Sixteen segment

The sixteen-segment type is capable of displaying numbers and the alphabet clearly.

{% tabs %}

{% highlight xaml %}

     <gauge:SfDigitalGauge Text="12345" 
                          CharacterType="SixteenSegment" 
                         />

{% endhighlight %}

{% highlight c# %}

            SfDigitalGauge digital = new SfDigitalGauge();

            digital.Text = "12345";

            digital.CharacterType = DigitalGaugeCharacterType.SixteenSegment;

{% endhighlight %}

{% endtabs %}

![sixteen-segment](Images\sixteen-segment.png)

## EightCrossEightDotMatrix segment

The dot matrix segment type is capable of displaying numbers, the alphabet, and special characters efficiently.

{% tabs %}

{% highlight xaml %}

     <gauge:SfDigitalGauge Text="12345" 
                          CharacterType="EightCrossEightDotMatrix" 
                         />

{% endhighlight %}

{% highlight c# %}

            SfDigitalGauge digital = new SfDigitalGauge();

            digital.Text = "12345";

            digital.CharacterType = DigitalGaugeCharacterType.EightCrossEightDotMatrix;

{% endhighlight %}

{% endtabs %}

![eightcrosseightdotmatrix-segment](Images\eightcrosseightdotmatrix-segment.png)
