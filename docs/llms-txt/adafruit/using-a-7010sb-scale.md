# Source: https://learn.adafruit.com/digital-shipping-scales/using-a-7010sb-scale.md

# Digital Shipping Scales

## Using a 7010SB Scale

Reading from the 7010SB is really easy, its just plain serial at 2400 baud 8N1 no flow control. The scale spits out data every 1/10 second so you just need to listen for the latest weight.![](https://cdn-learn.adafruit.com/assets/assets/000/000/892/medium800/shipping_2400b8n1.gif?1447976605)

There are two possible formats for the data, one for each measurement scale. The second byte indicates what scale you are in.| | First | | | | | | | | | Last |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Lbs/Oz. | 0x02 | **0x0B** | 0x80 | 0x80 | lb1 | lb2 | lb3 | oz1 | oz2 | 0x0D |
| Grams | 0x02 | **0x0C** | 0x80 | 0x80 | g1 | g2 | g3 | g4 | g5 | 0x0D |

- **STX** &nbsp;character - Hex&nbsp; **0x02** , indicates "Start of TeXt"
- Scale indicator - Hex&nbsp; **0xB0** &nbsp;for lb/oz and&nbsp; **0xC0** &nbsp;for grams
- Hex 0x80 (placeholder)
- Hex 0x80 (placeholder)
- First character of weight, ascii format
- Second character of weight, ascii format
- Third character of weight, ascii format
- Fourth character of weight, ascii format - single Ounces in Lb/Oz weight
- Fifth character of weight, ascii format - 1/10th Ounces in Lb/Oz weight
- Finishing carriage return - Hex&nbsp; **0x0D**

For example, if we are weighing a box that is&nbsp; **1 lb 4.1 oz** &nbsp;this is the output:

![](https://cdn-learn.adafruit.com/assets/assets/000/000/893/medium800/shipping_lbsoz.gif?1447976613)

Note that the weight shows up in&nbsp; **ascii** &nbsp;character format (so its&nbsp; **0x31 0x34 0x31&nbsp;** not&nbsp; **0x01 0x04 0x01** ) If you need to convert to raw number, just subtract hex 0x30

Grams is a little simpler since its metric. It weighs about 390 grams.

![](https://cdn-learn.adafruit.com/assets/assets/000/000/894/medium800/shipping_grams.gif?1447976621)

You can see the 390 (385-395 g.) printed out. There is no fractional/decimals.## Code Examples for the 7010SB
We like to use python for its cross-platform compatibility. You'll need to install&nbsp; **pySerial** &nbsp;extension to access the serial port. Under windows the&nbsp; **COM port&nbsp;** will be whatever the USB adapter shows up as or **COM1** &nbsp;or&nbsp; **COM2** &nbsp;if using the built-in ports. For Macs/Linux check under&nbsp; **/dev/cu\*&nbsp;** or&nbsp; **/dev/ttyusb** \* - or run&nbsp; **dmesg** &nbsp;after plugging in the adapter for hints about what the device is called.```
SERIALPORT = "COM1" 
# this uses pySerial found here http://pyserial.sourceforge.net/
# it currently exists for python 2.5
import serialser = serial.Serial(SERIALPORT, 2400, timeout=1)
while True:
    while True:x = ser.read()
    if (ord(x) == 13):
        breakstart = ord(ser.read()) # this is always 2 if the scale is on (i think - not totally sure what this is)
        mode = ord(ser.read()) # 176 = oz/lbs     #192 = grams
        nonce1 = ord(ser.read())
        nonce2 = ord(ser.read())
        if start != 2 or nonce1 != 128 or nonce2 != 128:
            continue
        value0 = int(ser.read()) # only used for lbs * 10
        value1 = int(ser.read())
        value2 = int(ser.read())
        value3 = int(ser.read())
        value4 = int(ser.read())
        if mode == 176: #oz
            weight = ((value0 * 10 + value1) * 16) + (value2 * 10 + value3) + (value4 * 0.1)
            unit = 'oz'
        elif mode == 192: #grams
        weight = value1 * 1000 + value2 * 100 + value3 * 10 + value4 
        unit = 'g'
    print str(weight) + unit 
ser.close(
```

- [Previous Page](https://learn.adafruit.com/digital-shipping-scales/smaller-scale-0-10-lb.md)
- [Next Page](https://learn.adafruit.com/digital-shipping-scales/larger-scales.md)

## Related Guides

- [Barcode Scanner](https://learn.adafruit.com/barcode-scanner.md)
