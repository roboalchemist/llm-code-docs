# Source: https://learn.adafruit.com/digital-shipping-scales/smaller-scale-0-10-lb.md

# Digital Shipping Scales

## Smaller Scale (0-10 lb)

For 99% of our packages, the weight of the box is under 10lb. So far we've found the&nbsp; **Salter Brecknell 7010SB** &nbsp;is a small, fairly well made scale. You can pick up the whole package for about $60-$70. This is actually a fair price, the accuracy ranges from 0.1 oz (for under 5lb packages) to 0.5 oz (for 5-10 lb packages). This is totally acceptable for shipping where under a few lbs, the postage is done by the oz and over 5 lb postage tends to be done by the lb.![](https://cdn-learn.adafruit.com/assets/assets/000/000/889/medium800/shipping_7010sbfront.jpg?1396766660)

The scale comes with a wall plug and a serial cable. The plug has a 3.5mm 'audio' plug and the serial cable has only two conductors - ground and TX - connected to a 2.5mm audio plug. To use, simply power it up and plug the serial port to your computer.&nbsp;[We buy computers with COM ports built into them so that the COM port is fixed in hardware](http://wiki.ladyada.net/adacomputer)&nbsp;, but&nbsp;[you can also use any USB to serial converter cable that will give you a USB plug](http://www.adafruit.com/index.php?main_page=product_info&cPath=33&products_id=18).![](https://cdn-learn.adafruit.com/assets/assets/000/000/890/medium800/shipping_7010sbplugs.jpg?1396766665)

If you are trying to connect to a microcontroller/microcomputer, you can use a male DB-9 and then use a MAX232 or similar to convert from the +-10V inverted serial that comes out of the cable and convert it to plain 3.3-5V TTL serial

The bottom has two removable plates. One reveals a 9V battery (you can turn this into a portable scale but we think the 9V plug works best) and the other reveals some THM PCB. Not really sure what that's for but perhaps during test they use it?

![](https://cdn-learn.adafruit.com/assets/assets/000/000/891/medium800/shipping_bottom.jpg?1396766672)

- [Previous Page](https://learn.adafruit.com/digital-shipping-scales/overview.md)
- [Next Page](https://learn.adafruit.com/digital-shipping-scales/using-a-7010sb-scale.md)

## Related Guides

- [Barcode Scanner](https://learn.adafruit.com/barcode-scanner.md)
