# Source: https://learn.adafruit.com/digital-shipping-scales/using-a-hd-150-scale.md

# Digital Shipping Scales

## Using a HD-150 Scale

The format of the HD-150 is different than that of the smaller scale. By default the scale is in&nbsp; **WorldShip** &nbsp;mode (a piece of UPS software). Its not a great format, and you need to press the&nbsp; **Data** &nbsp;button to have the transmisison occur. We suggest putting it into&nbsp; **SCI.3** &nbsp;mode which is continuous data transmission with higher resolution. Check the manual in the download section for how to get it into that mode

You will then be able to read from the data stream at&nbsp; **9600** &nbsp;baud, 8N1 no flow control.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/897/medium800/shipping_mw150.gif?1447976629)

As you can see the format is a little longer but its also human readable.| First | | | | | | | | | | | | | Last |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **:** | **W** | ' ' or **&nbsp;'-**' | lb1 | lb2 | lb3 | '.' | lb5 | lb6 | **l** | **b** | **S** &nbsp;if stable | **L** &nbsp;if lowbatt | 0x0D |
| **:** | **W** | ' ' or **&nbsp;'-**' | kg1 | kg2 | kg3 | '.' | kg5 | kg6 | **k** | **g** | **S** &nbsp;if stable | **L** &nbsp;if lowbatt | 0x0D |

Basically, its " **:W**" followed by a space or minus sign, then 3 digits of whole lb/kg, a decimal point and two fractional digits. The data format scale is indicated by two characters,&nbsp; **lb** &nbsp;or&nbsp; **kg'** &nbsp;and then two status characters that will indicate if the reading has&nbsp; **Stabilized** &nbsp;and if the battery/power is&nbsp; **Low**

We don't have this scale with example code yet but you can probably adapt the python code above for the HD-150 or HD-300 without too much difficulty (and if you do please edit the wiki page to add it!)

- [Previous Page](https://learn.adafruit.com/digital-shipping-scales/larger-scales.md)
- [Next Page](https://learn.adafruit.com/digital-shipping-scales/downloads.md)

## Related Guides

- [Barcode Scanner](https://learn.adafruit.com/barcode-scanner.md)
