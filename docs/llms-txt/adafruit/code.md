# Source: https://learn.adafruit.com/gps-dog-collar/code.md

# GPS Dog Collar

## Code

The following is the code for the project.&nbsp;

https://github.com/adafruit/Adafruit_Learning_System_Guides/blob/main/GPS_Dog_Collar/GPS_Dog_Collar/GPS_Dog_Collar.ino

## Code Walkthrough

If you scroll down a bit in the code, you will see where you enter the total distance you would like your dog to walk in a day. &nbsp;I have set the default to 3 miles.

```
//ENTER YOUR DESIRED DISTANCE GOAL (IN MILES)
//-------------------------------------------------------------------------------
float GOAL = 3; //Distances can include decimal points
//-------------------------------------------------------------------------------
```

I used the [TinyGPS library](http://arduiniana.org/libraries/tinygps/) to do most of the heavy lifting, and pulled a lot of code from my [Coobro Geo](http://www.adafruit.com/products/652) code. &nbsp;The heart of the code is all about taking constant distance measurements. &nbsp;Every time the code loops, it looks at where you were, and where you are.

```
unsigned long calc_dist(float flat1, float flon1, float flat2, float flon2)
{
  float dist_calc=0;
  float dist_calc2=0;
  float diflat=0;
  float diflon=0;

  diflat=radians(flat2-flat1);
  flat1=radians(flat1);
  flat2=radians(flat2);
  diflon=radians((flon2)-(flon1));

  dist_calc = (sin(diflat/2.0)*sin(diflat/2.0));
  dist_calc2= cos(flat1);
  dist_calc2*=cos(flat2);
  dist_calc2*=sin(diflon/2.0);
  dist_calc2*=sin(diflon/2.0);
  dist_calc +=dist_calc2;

  dist_calc=(2*atan2(sqrt(dist_calc),sqrt(1.0-dist_calc)));

  dist_calc*=6371000.0; //Converting to meters
  return dist_calc;
}
```

When standing still, the GPS coordinates will jump around slightly. &nbsp;I didn't want this to affect the total distance traveled, so I had the code first make sure you were moving. &nbsp;If you are moving, it adds the distance&nbsp;value from the code above&nbsp;to a running total to determine your total distance traveled.

```
if (gps.f_speed_kmph() &gt; 3.9)
  {
    if (start == 1)
    {
      start = 0;
      lastFlat = flat;
      lastFlon = flon;
    }
    else
    {
      //totalDistance = gps.distance_between(flat, flon, LONDON_LAT, LONDON_LON);
      totalDistance = totalDistance + calc_dist(flat, flon, lastFlat, lastFlon);
      lastFlat = flat;
      lastFlon = flon;
    }
  }
```

My favorite part of coding this project was making that tiny OLED display useful information that would be easy to see and understand at a quick glance. &nbsp;I started by creating a neat 'Acquiring Satellites' animation when you first turn on the device. &nbsp;I then created a nice bar graph that shows your progress towards your goal. &nbsp;Above the bar graph is a running mileage counter. &nbsp;All of these numbers can easily be converted to km if needed.

```
display.clearDisplay();
  
  display.setTextSize(1);
  display.setTextColor(WHITE);
  display.setCursor(0,0);
  
  float fDist = totalDistance;
  //convert meters to miles
  fDist *= 0.000621371192;
  //float fSpeed = gps.f_speed_kmph();
  printLCDFloat(fDist, 2);
  display.print(" Miles (");
  
  float targetDist = fDist / GOAL;
  
  printLCDFloat(targetDist*100, 0);
  display.print("%)");
  
  display.drawLine(0, 12, 0, 31, WHITE);
  
  display.drawLine(63, 28, 63, 31, WHITE);
  display.drawLine(127, 12, 127, 31, WHITE);
  display.drawLine(31, 28, 31, 31, WHITE);
  
  display.drawLine(95, 28, 95, 31, WHITE);
  display.drawLine(0, 28, 127, 28, WHITE);
  display.drawLine(0, 12, 127, 12, WHITE);
  
  display.fillRect(2, 14, (124 * targetDist), 13, 1);
  
  if (gps.hdop() &gt; 2000) {
    //display.fillRect(2, 14, (124), 13, BLACK);
    display.fillRect(0, 0, 128, 32, BLACK);
    display.fillCircle(6, 6, 2, WHITE);
    display.fillCircle(64, 6, 2, WHITE);
    display.fillCircle(122, 6, 2, WHITE);
    display.fillCircle(35, 6, 2, WHITE);
    display.fillCircle(93, 6, 2, WHITE);
    
    if (i==0){
      display.drawCircle(6, 6, 4, WHITE);
    }
    if (i==1){
      display.drawCircle(35, 6, 4, WHITE);
    }
    if (i==2){
      display.drawCircle(64, 6, 4, WHITE);
    }
    if (i==3){
      display.drawCircle(93, 6, 4, WHITE);
    }
    if (i==4){
      display.drawCircle(122, 6, 4, WHITE);
      i = 0;
    } else {
    i++;
    }
    
    display.setTextColor(WHITE);
    display.setCursor(5,20);
    display.print("Acquiring Satellites");
  }
    
  display.display();
```

- [Previous Page](https://learn.adafruit.com/gps-dog-collar/wiring.md)
- [Next Page](https://learn.adafruit.com/gps-dog-collar/going-further.md)

## Featured Products

### Adafruit Ultimate GPS Breakout - 66 channel w/10 Hz updates

[Adafruit Ultimate GPS Breakout - 66 channel w/10 Hz updates](https://www.adafruit.com/product/746)
We carry a few different GPS modules here in the Adafruit shop, but none that satisfied our every desire - that's why we designed this little GPS breakout board. We believe this is the **Ultimate** GPS module, so we named it that. It's got everything you want and...

In Stock
[Buy Now](https://www.adafruit.com/product/746)
[Related Guides to the Product](https://learn.adafruit.com/products/746/guides)
### Atmega32u4 Breakout Board

[Atmega32u4 Breakout Board](https://www.adafruit.com/product/296)
Toss out those FTDI cables and go USB-native with the ATmega32u4. After many months of back-orders, we finally received a shipment of these little guys and are excited to offer our breakout board. The little dev board keeps it simple, with just the bare essentials:

- Atmega32u4 - AVR...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/296)
[Related Guides to the Product](https://learn.adafruit.com/products/296/guides)
### Monochrome 128x32 SPI OLED graphic display

[Monochrome 128x32 SPI OLED graphic display](https://www.adafruit.com/product/661)
These displays are small, only about 1" diagonal, but very readable due to the high contrast of an OLED display. This display is made of 128x32 individual white OLED pixels, each one is turned on or off by the controller chip. Because the display makes its own light, no backlight is...

In Stock
[Buy Now](https://www.adafruit.com/product/661)
[Related Guides to the Product](https://learn.adafruit.com/products/661/guides)
### 3 x AAA Battery Holder with On/Off Switch and 2-Pin JST

[3 x AAA Battery Holder with On/Off Switch and 2-Pin JST](https://www.adafruit.com/product/727)
This battery holder connects 3 AAA batteries together in series for powering all kinds of projects. We spec'd these out because the box is slim, and 3 AAA's add up to about 3.3-4.5V, a very similar range to Lithium Ion/polymer (Li-Ion) batteries and have an on-off switch. That makes...

In Stock
[Buy Now](https://www.adafruit.com/product/727)
[Related Guides to the Product](https://learn.adafruit.com/products/727/guides)
### Adafruit Feather 32u4 Basic Proto

[Adafruit Feather 32u4 Basic Proto](https://www.adafruit.com/product/2771)
 **Feather** is the new development board from Adafruit, and like its namesake it is thin, light, and lets you fly! We designed Feather to be a new standard for portable microcontroller cores.

**This is the&nbsp;Feather 32u4 Basic Proto,** it has a bunch of...

In Stock
[Buy Now](https://www.adafruit.com/product/2771)
[Related Guides to the Product](https://learn.adafruit.com/products/2771/guides)
### Adafruit Feather 32u4 Adalogger

[Adafruit Feather 32u4 Adalogger](https://www.adafruit.com/product/2795)
Feather is the new development board from Adafruit, and like its namesake it is thin, light, and lets you fly! We designed Feather to be a new standard for portable microcontroller cores.

This is the&nbsp; **Adafruit Feather 32u4 Adalogger** &nbsp;- our take on an...

In Stock
[Buy Now](https://www.adafruit.com/product/2795)
[Related Guides to the Product](https://learn.adafruit.com/products/2795/guides)

## Related Guides

- [Adafruit Feather 32u4 Basic Proto](https://learn.adafruit.com/adafruit-feather-32u4-basic-proto.md)
- [Esenciales para CircuitPython](https://learn.adafruit.com/esenciales-para-circuitpython.md)
- [Arduino GPS Clock](https://learn.adafruit.com/arduino-clock.md)
- [SSD1306 OLED Displays with Raspberry Pi and BeagleBone Black](https://learn.adafruit.com/ssd1306-oled-displays-with-raspberry-pi-and-beaglebone-black.md)
- [Feather Fingerboard](https://learn.adafruit.com/feather-fingerboard.md)
- [Reverse Geocache Box](https://learn.adafruit.com/reverse-geocache-engagement-box.md)
- [How to Choose a Microcontroller](https://learn.adafruit.com/how-to-choose-a-microcontroller.md)
- [CircuitPython Hardware: SSD1306 OLED Display](https://learn.adafruit.com/micropython-hardware-ssd1306-oled-display.md)
- [Adafruit Ultimate GPS](https://learn.adafruit.com/adafruit-ultimate-gps.md)
- [3D Printed Case for Adafruit Feather](https://learn.adafruit.com/3d-printed-case-for-adafruit-feather.md)
- [Festive Feather Holiday Lights](https://learn.adafruit.com/festive-feather-holiday-lights.md)
- [Adafruit Feather 32u4 Adalogger](https://learn.adafruit.com/adafruit-feather-32u4-adalogger.md)
- [Superhero Power Gauntlet](https://learn.adafruit.com/superhero-power-gauntlet.md)
- [Magic Wand](https://learn.adafruit.com/magic-wand.md)
- [Monochrome OLED Breakouts](https://learn.adafruit.com/monochrome-oled-breakouts.md)
- [Arduino Ethernet + SD Card](https://learn.adafruit.com/arduino-ethernet-sd-card.md)
