# Source: https://learn.adafruit.com/chumby-hacker-board/audio.md

# Chumby Hacker Board

## Audio

## Playing Local MP3s
You can play MP3's off of your USB key or if you've copied any to the **/mnt/storage** space with **btplay –start-daemon file.mp3**  
![](https://cdn-learn.adafruit.com/assets/assets/000/002/435/medium800/microcomputers_btplay.gif?1448059762)

MP3's will play in the background. To kill **btplay** run **killall btplay**  
  
Audio will play through the headphone jack at max volume, just plug in your favorite headphones! (Warning: it may be really loud!)

## Playing Remote MP3s
You can also stream music with **btplay** , just stick a URL in there! Of course, you will have to have network capability up and running first  
![](https://cdn-learn.adafruit.com/assets/assets/000/002/436/medium800/microcomputers_soma.gif?1448059757)

Just as before, just plug into the headphone jack to verify its working. (Warning: it may be really loud!)## Splitting out the A/V
The headphone jack is not actually just audio - its actually Audio and Video. That means that you if you just plug headphones you'll notice some buzzing - thats you listening to the video! Now if you're in a Cronenberg film this is probably OK but for most of us its very annoying! There are two solutions. One is to split out the 3 signals into RCA jacks (with a camcorder cable)  
![](https://cdn-learn.adafruit.com/assets/assets/000/002/437/medium800/microcomputers_avcable_MED.jpeg?1396783131)

and then recombining with an RCA Y cable (such as [a Y female-RCA to male 3.5mm](http://www.sweetwater.com/store/detail/YRA154/) or [this](http://www.sweetwater.com/store/detail/CMR206/)  
  
**Note** our A/V cables split out the signals as such - **Red** is Video, **White** and **Yellow** are stereo line-level audio which is not what you would expect!  
  
**Note** apparently like every A/V cable is slightly different. If you get one, try different colors to figure out which ones have audio coming out of them and which have video.

## Using the Mixer
If you want to change the volume of the headphones, you'll need to run the audio mixer software **amixer**  
![](https://cdn-learn.adafruit.com/assets/assets/000/002/438/medium800/microcomputers_amixer.gif?1448059751)

You can get and change the HeadPhone volume ( **HP** ) by running **amixer sget HP** and **amixer sset HP**

![](https://cdn-learn.adafruit.com/assets/assets/000/002/439/medium800/microcomputers_sgethp.gif?1448059746)

To set the volume to 1/2 for example, do this **amixer sset HP 64**

![](https://cdn-learn.adafruit.com/assets/assets/000/002/440/medium800/microcomputers_ssethp.gif?1448059741)

## Speaker
The iMX.233 has a built-in mono speaker amplifier that can push up to 2W into a 4 ohm speaker! To use, connect the two speaker inputs into the **Spkr** 0.1" JST connection near the power jack. You can use either pin, they are not polarized as it is a mono output. Don't ground either of the speaker pins, they are "bridge tied" to improve output volume  
  
The chumby is 'switched' by default - if you connect headphones into the jack, the speaker will turn off and vice versa.  
  
If you want the speaker on even with the headphone plugged in, you can use **amixer cset**  
![](https://cdn-learn.adafruit.com/assets/assets/000/002/441/medium800/microcomputers_amixercset.gif?1448059736)

For example, the Speaker Playback Switch is off, so we turn it on with **amixer cset numid=4 on** to reactivate

- [Previous Page](https://learn.adafruit.com/chumby-hacker-board/ethernet.md)
- [Next Page](https://learn.adafruit.com/chumby-hacker-board/sd-card.md)

## Featured Products

### USB 2.0 Powered Hub - 7 Ports with 5V 2A Power Supply

[USB 2.0 Powered Hub - 7 Ports with 5V 2A Power Supply](https://www.adafruit.com/product/961)
Add lots more USB capability to your Raspberry Pi or computer using this powered USB 2.0 hub. It adds a full **seven powered ports** , all at USB 2.0 speeds so you can use video cameras and other high speed devices (cheaper hubs are v1.1 and not as fast!)  
  
The extra sauce...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/961)
[Related Guides to the Product](https://learn.adafruit.com/products/961/guides)
### Miniature WiFi (802.11b/g/n) Module: For Raspberry Pi and more

[Miniature WiFi (802.11b/g/n) Module: For Raspberry Pi and more](https://www.adafruit.com/product/814)
Make your Internet of Things device cable-free by adding WiFi. Take advantage of the Raspberry Pi and Beagle Bone's USB port to add a low cost, but high-reliability wireless link. We tried half a dozen modules to find one that works well with the Pi and Bone without the need of recompiling...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/814)
[Related Guides to the Product](https://learn.adafruit.com/products/814/guides)
### 5V 2A (2000mA) switching power supply - UL Listed

[5V 2A (2000mA) switching power supply - UL Listed](https://www.adafruit.com/product/276)
This is an FCC/CE certified and UL listed power supply. Need a lot of 5V power? This switching supply gives a clean regulated 5V output at up to 2000mA. 110 or 240 input, so it works in any country. The plugs are "US 2-prong" style so you may need a plug adapter, but you can pick one...

Out of Stock
[Buy Now](https://www.adafruit.com/product/276)
[Related Guides to the Product](https://learn.adafruit.com/products/276/guides)
### 2.1mm to 1.7mm DC jack adapter

[2.1mm to 1.7mm DC jack adapter](https://www.adafruit.com/product/411)
We're carrying this adapter primarily to allow Chumby Hacker Board users to adapt our nice [5V @ 2A power supply](http://www.adafruit.com/products/276) to their CHB. But you can use this adapter for anything else that has a 1.7mm DC jack, such as a PSP.

In Stock
[Buy Now](https://www.adafruit.com/product/411)
[Related Guides to the Product](https://learn.adafruit.com/products/411/guides)
### USB MicroSD Card Reader/Writer - microSD / microSDHC / microSDXC

[USB MicroSD Card Reader/Writer - microSD / microSDHC / microSDXC](https://www.adafruit.com/product/939)
This is the cutest little microSD card reader/writer - but don't be fooled by its adorableness! It's wicked fast and supports up to 64 GB SDXC cards! Simply slide the card into the edge and plug it into your computer. No drivers are required, it shows up as a standard 'Mass...

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/939)
[Related Guides to the Product](https://learn.adafruit.com/products/939/guides)
### Ethernet Cable - 10 ft long

[Ethernet Cable - 10 ft long](https://www.adafruit.com/product/730)
We have so many Internet-connected goodies in the shop, we figured it's time to carry a cable so you can easily connect them up! This cable is 10 feet long, black and has all 8 wires installed. Perfect for use with the [BeagleBone](http://www.adafruit.com/products/513), <a...></a...>

No Longer Stocked
[Buy Now](https://www.adafruit.com/product/730)
[Related Guides to the Product](https://learn.adafruit.com/products/730/guides)
### USB to TTL Serial Cable - Debug / Console Cable for Raspberry Pi

[USB to TTL Serial Cable - Debug / Console Cable for Raspberry Pi](https://www.adafruit.com/product/954)
The cable is easiest way ever to connect to your microcontroller/Raspberry Pi/WiFi router serial console port. Inside the big USB plug is a USB\<-\>Serial conversion chip and at the end of the 36" cable are four wire - red power, black ground, white RX into USB port, and green TX out...

In Stock
[Buy Now](https://www.adafruit.com/product/954)
[Related Guides to the Product](https://learn.adafruit.com/products/954/guides)
### FTDI Serial TTL-232 USB Cable

[FTDI Serial TTL-232 USB Cable](https://www.adafruit.com/product/70)
Just about all electronics use TTL serial for debugging, bootloading, programming, serial output, etc. But it's rare for a computer to have a serial port anymore. This is a USB to TTL serial cable, with a FTDI FT232RL usb/serial chip embedded in the head. It has a 6-pin socket at the end...

In Stock
[Buy Now](https://www.adafruit.com/product/70)
[Related Guides to the Product](https://learn.adafruit.com/products/70/guides)

## Related Guides

- [CircuitPython Libraries on MicroPython using the Raspberry Pi Pico](https://learn.adafruit.com/circuitpython-libraries-on-micropython-using-the-raspberry-pi-pico.md)
- [Hallowing Minotaur Maze](https://learn.adafruit.com/hallowing-minotaur-maze.md)
- [Raspberry Pi Azure IoT Hub Dashboard with CircuitPython](https://learn.adafruit.com/raspberry-pi-iot-dashboard-with-azure-and-circuitpython.md)
- [Adafruit 2.9" eInk Display Breakouts and FeatherWings](https://learn.adafruit.com/adafruit-2-9-eink-display-breakouts-and-featherwings.md)
- [Pi SSD Media Server](https://learn.adafruit.com/pi-ssd-media-server.md)
- [Creating Slideshows in CircuitPython](https://learn.adafruit.com/creating-slideshows-in-circuitpython.md)
- [Network Interface Failover using FONA](https://learn.adafruit.com/network-interface-failover-using-fona.md)
- [Matrix Keypad](https://learn.adafruit.com/matrix-keypad.md)
- [Native MP3 decoding on Arduino](https://learn.adafruit.com/native-mp3-decoding-on-arduino.md)
- [Raspberry Pi HQ Camera Case](https://learn.adafruit.com/raspberry-pi-hq-camera-case.md)
- [Articulated Pi Display V2 Mount](https://learn.adafruit.com/pi-wall-mount.md)
- [World's Smallest MAME Arcade Cabinet](https://learn.adafruit.com/worlds-smallest-mame-arcade-cabinet.md)
- [Raspberry Pi E-Ink Weather Station using Python](https://learn.adafruit.com/raspberry-pi-e-ink-weather-station-using-python.md)
- [Getting Started with Raspberry Pi Pico and CircuitPython](https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython.md)
- [Adafruit QT Py and NeoPixel LEDs](https://learn.adafruit.com/qt-py-and-neopixel-leds.md)
