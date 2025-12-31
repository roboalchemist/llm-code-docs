# Source: https://learn.adafruit.com/usb-dc-and-solar-lipoly-charger/design-notes.md

# USB, DC & Solar Lipoly Charger

## Design Notes

## Is this a Max Power Point Tracker (MPPT)?

This design is not a 'true' MPPT, and we did that for a reason! Max power point trackers work by 'tracking' the voltage and current curve of a solar panel so that the total Power (Voltage \* Current) is maximized. This means that as the light changes, the voltage and current must be carefully tracked. In general, the way controllers perform MPPT is to have a DC/DC converter - that's because to have the best power conversion you'll want DC/DC not linear converters (that lose any excess voltage as heat). For example, say you want to charge a 6V lead acid battery and you have a 12V (approx) panel. The voltage will range between 9V and 14V depending on current draw and visible light. The buck converter will do its best to keep the current draw so that the total power available at the&nbsp;_output_&nbsp;is maximized.

This&nbsp;[diagram from Linear](https://www.analog.com/media/en/technical-documentation/lt-journal-article/LTJournal_V20N4_Jan11.pdf "Link: https://www.analog.com/media/en/technical-documentation/lt-journal-article/LTJournal\_V20N4\_Jan11.pdf")&nbsp;is really good at describing how it works:

![](https://cdn-learn.adafruit.com/assets/assets/000/001/521/medium800/projects_linearmppt.gif?1447864288)

The Green lines show the I-V curve of the panel for a&nbsp;_given_&nbsp;light condition. As the light increases the voltages stay sort of the same but the&nbsp;_amount of current_&nbsp;you can draw goes up! If you can keep the DC/DC converter operating on the red line, that's the maximum power.

**However, there are some side effects to using a MPPT design.**

First is that DC/DC converters are expensive, and adding a DC/DC converter to a LiPo charger chip increases the cost by 2x. For small panels, if the MPPT increases the efficiency by 30% but you can double the panel size for the same price increase, it might be easier to just go with a larger panel.

Second is that DC/DC converters are not necessarily more efficient than a linear converter at low voltages and currents. At the voltages we're talking about, a 6V panel charging a 4V battery, the max power point will tend to be around 5V - only a volt above the battery. Considering there's a 0.5V drop with the input diode, the added inefficiency of a DC/DC converter is about equivalent to the extra voltage drop used by the linear charger. For this reason, you tend to see MPPT controllers only for multi-ampere chargers for big lead acid batteries and really big panels.

**So the upshot is...**

If your panel voltage is ~1V above your battery charging voltage, your current draw is under an Ampere, and you control the current draw to keep the voltage steady at around the 'max power voltage' (the red line up above), it's possible to get near-MPPT performance, without the complexity of a DC/DC converter, and without the high price. That's what the design of this charger does.

## Why a special solar charger?
We've had a lot of customers that are interested in making solar powered projects, so we wanted to make a lipo charger board that is specifically designed with Solar & USB charging in mind. We'll explain why...

Most people try to plug a solar panel directly into a lipo charger and while it&nbsp;_sort of&nbsp;_works, the battery takes&nbsp;_forever_&nbsp;to charge because the efficiency is terrible! That's because most lipo chargers are meant to plug into a USB port or wall, and are very simple in their design. USB ports supply 5V at up to 500mA and they're pretty solid - the voltage doesn't change much even at the max current draw. So when you plug a charger into a computer with a USB port, they just draw 500mA or so and happily chug away. Same goes for wall adapters. The voltage and current limits are kept steady.

Solar panels are a little different, the voltage and current&nbsp;_vary constantly_&nbsp;depending on sunlight available. They are unstable! That instability confuses battery chargers, which causes them to do one of two things: rapidly turn on and off as they try to draw more current from the panel than possible and/or draw much less current than they can, to keep the voltage from collapsing

Here is a diagram of a&nbsp; **single&nbsp;** solar cell, in various light conditions (the colored rainbow lines):

![](https://cdn-learn.adafruit.com/assets/assets/000/001/522/medium800/projects_Solar-Cell-IV-curve-with-MPP.png?1396773674)

We find these diagrams common but a bit confusing. So we'll show how to use them. Pick the top red line (maximum light) and start at the very right of the line where it meets the horizontal scale. This is the current (I) = 0 point. We're drawing _no current_&nbsp;and the voltage of the cell is 0.5V. 0.5V is the&nbsp; **open circuit voltage**. Keep following the graph up and to the left. As the current draw increases, the voltage drops slightly until we reach the point of drawing 38mA (0.038A). At this point, the voltage is around 0.4V. Next draw a bit more current, moving to the left some more and the voltage starts&nbsp;_collapsing._We can try to draw more current but as you can see, drawing even a tiny bit more than 38mA makes the cell voltage drop to 0V. 38mA is the&nbsp; **short circuit current**

Depending on the light conditions, the amount of maximum current can range, from 38mA (red) to 32 mA (orange) down to 5mA (yellow) or even lower. Solar cells can be made larger (the short circuit current is bigger) but the voltage of the cell is fixed at 0.5V open circuit - it's just part the physics of the cell. However, you can connect a bunch of cells in series to add them up. A 6V&nbsp; **panel** &nbsp;has 12&nbsp; **cells** &nbsp;(12 \* 0.5V = 6V)

Now you can see what happens if you connect a 6V solar panel to a lipoly charger. As long as the current being drawn by the charger is less than the panel's short circuit current at that light condition, everything is peachy. The moment the light changes even a little, and the current the lipo charger wants is higher than the short circuit current, the charger becomes&nbsp; **unstable:&nbsp;** it will draw too much current, which will cause the voltage to collapse, which causes the charger to turn off, which reduces the current draw, which makes the panel voltage recover, which turns on the charger again, which then draws too much current, and the cycle repeats.

You can see this happen in the image from my scope below:

![](https://cdn-learn.adafruit.com/assets/assets/000/001/523/medium800/projects_TEK0001.jpeg?1396773679)

The scale is 1V per square, and the 0V point is one square above the bottom of the display (see the 2-\> on the left) The **&nbsp;open circuit voltage&nbsp;** of the panel is about 6.5V, the lipo charger draws some current and quickly the panel voltage collapses. After 250 us, the charger tries again, but fails again. The lipo charger may seem to be charging because the&nbsp; **CHRG** &nbsp;light is on but really its doing a poor job of it!

## Solar Optimization!
OK so how do we fix this problem? The issue we have here is that the voltage collapses during high current draw. We need to find a way to keep the lipo charger from drawing too much current, and backing off when the voltage starts to droop. We looked high and low and finally found a chip that has something like this built in. The MCP73871 calls it Voltage Proportional Charge Control (VPCC) and basically, it does precisely what we want. We can set the voltage to a point just above the battery charge voltage point (say 4.5V) and then instruct the charger to draw as much current as possible. It will automatically increase/reduce the charge rate to keep the voltage higher than 4.5V!  
![](https://cdn-learn.adafruit.com/assets/assets/000/001/524/medium800/projects_vpcc.gif?1447864291)

In this case, we set the voltage using two resistors, the voltage divider ends up stabilizing it at ~4.5V. Because the voltage collapse of a panel is really sudden, we still end up needing a little more help stabilizing the panel. We do that by adding a BFC (Big Freaking Capacitor).![](https://cdn-learn.adafruit.com/assets/assets/000/001/525/medium800/projects_inputcap.gif?1447864291)

This schottky diode charges a 4700uF capacitor from the panel - the diode prevents the capacitor from draining back into the panel.- [Previous Page](https://learn.adafruit.com/usb-dc-and-solar-lipoly-charger/using-the-charger.md)
- [Next Page](https://learn.adafruit.com/usb-dc-and-solar-lipoly-charger/downloads.md)

## Featured Products

### Lithium Ion Battery Pack - 3.7V 4400mAh

[Lithium Ion Battery Pack - 3.7V 4400mAh](https://www.adafruit.com/product/354)
Need a big battery for your project? This lithium-ion pack is made of 2 balanced 2200mAh cells for a total of 4400mA capacity! The cells are connected in parallel and spot-welded to a protection circuit that provides over-voltage, under-voltage, and over-current protection.

Each cell can...

In Stock
[Buy Now](https://www.adafruit.com/product/354)
[Related Guides to the Product](https://learn.adafruit.com/products/354/guides)
### USB / DC / Solar Lithium Ion/Polymer charger

[USB / DC / Solar Lithium Ion/Polymer charger](https://www.adafruit.com/product/390)
Make your projects to go green this summer with our specialized USB/Solar Lithium Ion Polymer Battery charger! This charger is a very unique design, perfect for outdoor projects, or DIY iPod chargers. We've spent over a year testing and tinkering with this charger to come up with a plug...

In Stock
[Buy Now](https://www.adafruit.com/product/390)
[Related Guides to the Product](https://learn.adafruit.com/products/390/guides)
### Lithium Ion Polymer Battery - 3.7v 1200mAh

[Lithium Ion Polymer Battery - 3.7v 1200mAh](https://www.adafruit.com/product/258)
Lithium-ion polymer (also known as 'lipo' or 'lipoly') batteries are thin, light, and powerful. The output ranges from 4.2V when completely charged to 3.7V. This battery has a capacity of 1200mAh for a total of about 4.5 Wh. If you need a larger battery, <a...></a...>

In Stock
[Buy Now](https://www.adafruit.com/product/258)
[Related Guides to the Product](https://learn.adafruit.com/products/258/guides)
### Male DC Power adapter - 2.1mm plug to screw terminal block

[Male DC Power adapter - 2.1mm plug to screw terminal block](https://www.adafruit.com/product/369)
If you need to connect a battery pack or wired power supply to a board that has a DC jack - this adapter will come in very handy! There is a 2.1mm DC plug on one end, and a screw terminal block on the other. The terminals are labeled with positive/negative assuming a positive-tip configuration...

In Stock
[Buy Now](https://www.adafruit.com/product/369)
[Related Guides to the Product](https://learn.adafruit.com/products/369/guides)
### MintyBoost Kit

[MintyBoost Kit](https://www.adafruit.com/product/14)
The world's first and only open-source hardware charger: The MintyBoost®!  
  
**New version!** Works with the new iPhone 4 & 5 and more! **Please review the [Minty Boost project page(s)](//learn.adafruit.com/minty-boost) before purchase and...**

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/14)
[Related Guides to the Product](https://learn.adafruit.com/products/14/guides)
### 10K Precision Epoxy Thermistor

[10K Precision Epoxy Thermistor](https://www.adafruit.com/product/372)
Need to measure something damp? This epoxy-coated precision 1% 10K thermistor is an inexpensive way to measure temperature in weather or liquids. The resistance in 25 °C is 10K (+- 1%). The resistance goes down as it gets warmer and goes up as it gets cooler. <a...></a...>

In Stock
[Buy Now](https://www.adafruit.com/product/372)
[Related Guides to the Product](https://learn.adafruit.com/products/372/guides)
### Large 6V 3.7W Solar Panel

[Large 6V 3.7W Solar Panel](https://www.adafruit.com/product/417)
Harness even more power from the sun with this nice big solar panel. We had these custom made for us when customers let us know they needed more than what our 2W panel could provide. This panel is a 12-cell (6V) assembly mounted onto a fiberglass PCB and covered with PET plastic which protects...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/417)
[Related Guides to the Product](https://learn.adafruit.com/products/417/guides)
### Large 6V 3.5W Solar panel

[Large 6V 3.5W Solar panel](https://www.adafruit.com/product/500)
These panels come to us from Voltaic Systems, makers of fine solar-powered bags and packs. These are waterproof, scratch resistant, and UV resistant. They use a high efficiency monocrystalline cell. They output 6V at 530 mA via 3.5mm x 1.1mm DC jack connector - a nice upgrade to the 2W panels...

Out of Stock
[Buy Now](https://www.adafruit.com/product/500)
[Related Guides to the Product](https://learn.adafruit.com/products/500/guides)

## Related Guides

- [Solar Boost Bag](https://learn.adafruit.com/solar-boost-bag.md)
- [Mailbox Notification Service](https://learn.adafruit.com/mailbox-notification-service.md)
- [Portable Solar Charging Tracker](https://learn.adafruit.com/portable-solar-charging-tracker.md)
- [Collin's Lab: Solar](https://learn.adafruit.com/collins-lab-solar.md)
- [Solar Charging Handbag](https://learn.adafruit.com/solar-charging-handbag.md)
- [Compost Friend!](https://learn.adafruit.com/compost-optimization-machine.md)
- [Adafruit TPL5110 Power Timer Breakout](https://learn.adafruit.com/adafruit-tpl5110-power-timer-breakout.md)
- [PyLeap ESP32-S3 TFT Boxing Glove Tracker w/ Adafruit IO](https://learn.adafruit.com/esp32-s2-tft-boxing-glove-tracker-w-adafruit-io.md)
- [Adafruit HUSB238 USB Type C Power Delivery Breakout](https://learn.adafruit.com/adafruit-husb238-usb-type-c-power-delivery-breakout.md)
- [Adafruit bq25185 USB / DC / Solar Lithium Ion/Polymer Charger](https://learn.adafruit.com/adafruit-bq25185-usb-dc-solar-lithium-ion-polymer-charger.md)
- [Adafruit LM73100 Ideal Diode Breakout](https://learn.adafruit.com/adafruit-lm73100-ideal-diode-breakout.md)
- [Glowing Birthday Number Crown](https://learn.adafruit.com/glowing-birthday-number-crown.md)
- [Adafruit INA23x DC Current Voltage Power Monitor](https://learn.adafruit.com/adafruit-ina237-dc-current-voltage-power-monitor.md)
- [Zelda LED UltraHand](https://learn.adafruit.com/ultrahand.md)
- [Bo-Katan LED Headband](https://learn.adafruit.com/led-headband.md)
